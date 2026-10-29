import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import generate
from revision import (
    DEFAULT_SETTINGS, RevisionError, RevisionRequest, parse_json, read_text,
    request_revision, split_lyrics, validate_revision, write_outputs,
)

EXAMPLES = Path(__file__).resolve().parents[1] / "examples" / "revision"
LYRICS = (EXAMPLES / "lyrics.txt").read_text(encoding="utf-8")
STYLE = (EXAMPLES / "style.txt").read_text(encoding="utf-8")


def request(changes=(("style", "Make the male voice nasally and nerdy."),), **kwargs):
    return RevisionRequest(LYRICS, STYLE, changes, **kwargs)


def response(req, **overrides):
    fields = dict(title="Words Intact", style=req.style, lyrics=req.target_lyrics(),
                  settings=dict(req.settings), notes="Untested prompting hypothesis.")
    fields.update(overrides)
    return json.dumps(fields, ensure_ascii=False)


def client_for(text, stop_reason="end_turn"):
    client = MagicMock()
    stream = client.messages.stream.return_value.__enter__.return_value
    stream.text_stream = iter([text[:17], text[17:]])
    stream.get_final_message.return_value = SimpleNamespace(stop_reason=stop_reason)
    return client


class IntegrityTests(unittest.TestCase):
    def test_style_only_preserves_dialogue_and_spellings_exactly(self):
        req = request()
        sections, report = validate_revision(req, response(req, style="Nasally nerdy male character voice."))
        self.assertEqual(sections["lyrics"], LYRICS)
        self.assertEqual(report["lyric_text_diff"], "")
        self.assertEqual(report["metatag_diff"], "")
        self.assertIn("Nasally", report["style_diff"])

    def test_words_punctuation_case_pronunciation_and_whitespace_rejected(self):
        replacements = [
            ("Lowkenuinely", "Low-genuinely"), ("Ahhh-men", "Amen"),
            ("fine-domme", "findom"), ("Wait, so…", "Wait, so..."),
            ("you're", "you’re"), ("iconic", "Iconic"), ("?", "!"),
            ("words alone", "words  alone"), ("\n\n", "\n"),
            ("[Chorus]\nOh-oh-oh", "[Chorus]\n Oh-oh-oh"),
        ]
        req = request()
        for before, after in replacements:
            with self.subTest(before=before, after=after), self.assertRaisesRegex(RevisionError, "LYRIC INTEGRITY FAILED"):
                validate_revision(req, response(req, lyrics=LYRICS.replace(before, after, 1)))

    def test_final_newline_is_protected(self):
        req = request()
        self.assertTrue(LYRICS.endswith("\n"))
        with self.assertRaisesRegex(RevisionError, "LYRIC INTEGRITY FAILED"):
            validate_revision(req, response(req, lyrics=LYRICS[:-1]))

    def test_inline_brackets_parentheses_and_speaker_labels_are_protected(self):
        for lyrics in ("I mean [this], not (that).\n", "(Ahhh-men)\n", "Alex: Wait—what?!\n"):
            req = RevisionRequest(lyrics, STYLE, (("metatags", "Add an Intro cue."),))
            with self.subTest(lyrics=lyrics), self.assertRaisesRegex(RevisionError, "LYRIC INTEGRITY FAILED"):
                validate_revision(req, response(req, lyrics=lyrics.replace("a", "o").replace("A", "O")))

    def test_tag_insert_replace_remove_reported_separately(self):
        req = request(changes=(("metatags", "Unaccompanied opening dialogue."),))
        proposed = LYRICS.replace("[Intro]", "[Intro]\n[A Cappella]").replace("[Male, Deadpan]", "[Male, Spoken]")
        proposed = proposed.replace("[Female, Spoken]\n", "")
        _, report = validate_revision(req, response(req, lyrics=proposed))
        self.assertEqual(report["lyric_text_diff"], "")
        self.assertIn("A Cappella", report["metatag_diff"])
        self.assertIn("Female, Spoken", report["metatag_diff"])

    def test_moving_tag_requires_metatag_scope(self):
        req = request()
        moved = LYRICS.replace("[Male, Deadpan]\n", "").replace("[Chorus]", "[Male, Deadpan]\n[Chorus]", 1)
        with self.assertRaisesRegex(RevisionError, "Metatags changed or moved"):
            validate_revision(req, response(req, lyrics=moved))

    def test_preserving_words_cannot_hide_removed_line_in_brackets(self):
        req = request(changes=(("metatags", "Simplify cues."),))
        modified = LYRICS.replace("Ahhh-men. It's a fine-domme situation—not a typo.", "[Ahhh-men. It's a fine-domme situation—not a typo.]")
        with self.assertRaisesRegex(RevisionError, "LYRIC INTEGRITY FAILED"):
            validate_revision(req, response(req, lyrics=modified))

    def test_repeated_sections_cannot_be_collapsed_duplicated_or_abbreviated(self):
        req = request(changes=(("metatags", "Simplify cues."),))
        chorus = "[Chorus]\nOh-oh-oh, leave my words alone!\n"
        proposals = [LYRICS.replace(chorus, "", 1), LYRICS + chorus,
                     LYRICS.replace(chorus, "[Repeat Chorus]\n", 1)]
        for proposed in proposals:
            with self.subTest(proposed=proposed), self.assertRaisesRegex(RevisionError, "LYRIC INTEGRITY FAILED"):
                validate_revision(req, response(req, lyrics=proposed))

    def test_word_order_cannot_change(self):
        req = request()
        lines = LYRICS.split("\n")
        lines[2], lines[4] = lines[4], lines[2]
        with self.assertRaisesRegex(RevisionError, "LYRIC INTEGRITY FAILED"):
            validate_revision(req, response(req, lyrics="\n".join(lines)))

    def test_literal_bracket_line_is_protected_even_with_tag_permission(self):
        req = RevisionRequest("[Intro]\n[Oh, no!]\n", STYLE, (("metatags", "Change intro cue."),),
                              literal_tags=frozenset({"[Oh, no!]"}))
        validate_revision(req, response(req, lyrics="[Spoken]\n[Oh, no!]\n"))
        with self.assertRaisesRegex(RevisionError, "LYRIC INTEGRITY FAILED"):
            validate_revision(req, response(req, lyrics="[Spoken]\n[Oh, yes!]\n"))

    def test_windows_newlines_are_equivalent_but_unicode_is_not_normalized(self):
        req = request()
        sections, _ = validate_revision(req, response(req, lyrics=LYRICS.replace("\n", "\r\n")))
        self.assertEqual(sections["lyrics"], LYRICS)
        req = RevisionRequest("Café\n", STYLE, (("style", "Jazz"),))
        with self.assertRaisesRegex(RevisionError, "LYRIC INTEGRITY FAILED"):
            validate_revision(req, response(req, lyrics="Cafe\u0301\n"))

    def test_style_and_settings_locked_without_scope(self):
        req = request(changes=(("metatags", "Simplify cues."),))
        with self.assertRaisesRegex(RevisionError, "Style changed"):
            validate_revision(req, response(req, style="New style"))
        with self.assertRaisesRegex(RevisionError, "Settings changed"):
            validate_revision(req, response(req, settings={**req.settings, "Weirdness": "30"}))

    def test_targeted_settings_revision(self):
        req = request(changes=(("settings", "Compare Weirdness 30."),))
        _, report = validate_revision(req, response(req, settings={**req.settings, "Weirdness": "30"}))
        self.assertEqual(report["settings_after"]["Weirdness"], "30")
        self.assertEqual(report["style_diff"], "")


class ExplicitEditTests(unittest.TestCase):
    def setUp(self):
        self.edits = tuple(json.loads((EXAMPLES / "lyric-edits.json").read_text()))

    def test_edit_one_repeated_occurrence_only(self):
        req = request(changes=(), lyric_edits=self.edits)
        target = req.target_lyrics()
        self.assertEqual(target.count("leave my words alone!"), 1)
        self.assertEqual(target.count("keep my words intact!"), 1)
        _, report = validate_revision(req, response(req))
        self.assertIn("keep my words intact!", report["lyric_text_diff"])
        self.assertEqual(report["metatag_diff"], "")
        with self.assertRaisesRegex(RevisionError, "LYRIC INTEGRITY FAILED"):
            validate_revision(req, response(req, lyrics=target.replace("leave my words alone!", "keep my words intact!")))

    def test_requested_edit_must_be_applied(self):
        req = request(changes=(), lyric_edits=self.edits)
        with self.assertRaisesRegex(RevisionError, "LYRIC INTEGRITY FAILED"):
            validate_revision(req, response(req, lyrics=LYRICS))

    def test_multiline_replacements_use_original_line_numbers(self):
        edits = ({"line": 3, "before": LYRICS.splitlines()[2], "after": "First line.\nSecond line."},
                 self.edits[0])
        req = request(changes=(), lyric_edits=edits)
        self.assertIn("First line.\nSecond line.", req.target_lyrics())
        self.assertEqual(req.target_lyrics().count("keep my words intact!"), 1)
        validate_revision(req, response(req))

    def test_invalid_edits_fail_before_api(self):
        valid = self.edits[0]
        cases = [({**valid, "line": 0},), ({**valid, "line": True},),
                 ({**valid, "line": 999},), ({**valid, "before": "Wrong!"},),
                 ({**valid, "after": "[Chorus]"},), (valid, valid),
                 ({**valid, "extra": "x"},), ({"line": 1, "before": "[Intro]", "after": "Hello"},)]
        for edits in cases:
            with self.subTest(edits=edits), self.assertRaises(RevisionError):
                request(lyric_edits=edits)

    def test_natural_language_lyric_permission_does_not_disable_guard(self):
        req = request(changes=(("style", "Also fix Lowkenuinely to genuinely."),))
        with self.assertRaisesRegex(RevisionError, "LYRIC INTEGRITY FAILED"):
            validate_revision(req, response(req, lyrics=LYRICS.replace("Lowkenuinely", "genuinely")))


class ResponseTests(unittest.TestCase):
    def test_malformed_missing_duplicate_and_wrong_type_fields_fail(self):
        req = request()
        value = json.loads(response(req))
        cases = ["```json\n" + response(req) + "\n```", response(req)[:-5], "[]",
                 json.dumps({k: v for k, v in value.items() if k != "lyrics"}),
                 response(req, lyrics=None), response(req, style=""),
                 response(req, settings={}), response(req, unexpected=True),
                 '{"title":"One","title":"Two"}', response(req, settings={**req.settings, "Weirdness": 30})]
        for text in cases:
            with self.subTest(text=text), self.assertRaises(RevisionError):
                validate_revision(req, text)

    def test_audio_influence_requires_explicit_workflow(self):
        with self.assertRaisesRegex(RevisionError, "Audio Influence"):
            request(settings={**DEFAULT_SETTINGS, "Audio Influence": "50"})
        req = request(settings={**DEFAULT_SETTINGS, "Audio Influence": "50"}, audio_reference=True)
        validate_revision(req, response(req))

    def test_suno_model_is_separate_from_drafting_model(self):
        with self.assertRaisesRegex(RevisionError, "v6 family"):
            request(settings={**DEFAULT_SETTINGS, "Model": "claude-opus-4-7"})

    def test_api_receives_exact_files_and_scoped_changes(self):
        req = request()
        client = client_for(response(req))
        output, report = request_revision(req, "KB text", "Base instructions", "test-drafting-model", "comedy", client)
        self.assertEqual(output["lyrics"], LYRICS)
        call = client.messages.stream.call_args.kwargs
        self.assertEqual(call["model"], "test-drafting-model")
        payload = json.loads(call["messages"][0]["content"].split("REVISION REQUEST (JSON):\n")[1])
        self.assertEqual(payload["original_lyrics"], LYRICS)
        self.assertEqual(payload["source_style"], STYLE)
        self.assertEqual(payload["genre_hint"], "comedy")
        self.assertEqual(payload["baseline_settings"]["Model"], "v6")
        self.assertEqual(report["drafting_model"], "test-drafting-model")

    def test_truncated_or_refused_response_is_never_accepted(self):
        req = request()
        for reason in ("max_tokens", "refusal", "tool_use", None):
            with self.subTest(reason=reason), self.assertRaisesRegex(RevisionError, "Incomplete"):
                request_revision(req, "", "", "test", client=client_for(response(req), reason))

    def test_api_error_is_not_published(self):
        client = MagicMock()
        client.messages.stream.side_effect = RuntimeError("sensitive provider detail")
        with self.assertRaises(RevisionError) as error:
            request_revision(request(), "", "", "test", client=client)
        self.assertNotIn("sensitive", str(error.exception))

    @patch.dict("os.environ", {}, clear=True)
    def test_missing_key_has_clear_error_without_sdk(self):
        with self.assertRaisesRegex(RevisionError, "ANTHROPIC_API_KEY"):
            request_revision(request(), "", "", "test")


class FileAndCLITests(unittest.TestCase):
    def run_main(self, args):
        out, err = io.StringIO(), io.StringIO()
        with patch("sys.argv", ["generate.py", *args]), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                generate.main()
            except SystemExit as exc:
                code = exc.code
            else:
                code = 0
        return code, out.getvalue(), err.getvalue()

    def revision_args(self):
        return ["--revise", "--lyrics-file", str(EXAMPLES / "lyrics.txt"),
                "--style-file", str(EXAMPLES / "style.txt"), "--change", "style:Nasal male voice"]

    def test_existing_cli_and_model_options_unchanged(self):
        with patch("generate.generate") as old:
            self.assertEqual(self.run_main(["a road trip", "-g", "rock", "-m", "my-model"])[0], 0)
            old.assert_called_once_with("a road trip", "rock", "my-model")

    def test_existing_default_model_and_list_genres(self):
        with patch("generate.generate") as old:
            self.run_main(["a road trip"])
            old.assert_called_once_with("a road trip", None, "claude-opus-4-7")
        code, out, _ = self.run_main(["--list-genres"])
        self.assertEqual(code, 0)
        self.assertIn("vocal-lounge-jazz", out)

    def test_legacy_markers_still_parse(self):
        parsed = generate.parse_response("---TITLE---\nSong\n---STYLE---\nJazz\n---LYRICS---\nAhhh-men\n---SLIDERS---\nModel: v6\n---NOTES---\nUntested")
        self.assertEqual(parsed["lyrics"], "Ahhh-men")
        self.assertEqual(parsed["sliders"], "Model: v6")

    def test_help_and_empty_cli_work_without_sdk(self):
        self.assertEqual(self.run_main(["--help"])[0], 0)
        self.assertEqual(self.run_main([])[0], 1)

    def test_invalid_flags_or_input_fail_before_api(self):
        cases = [["--lyrics-file", "x"], ["--revise"], self.revision_args() + ["a new song"],
                 self.revision_args() + ["--list-genres"], self.revision_args()[:-2],
                 self.revision_args()[:-1] + ["voice:tenor"], self.revision_args()[:-1] + ["style:"],
                 self.revision_args()[:-1] + ["no-scope"], self.revision_args() + ["--literal-line", "999"],
                 ["--revise", "--lyrics-file", "missing.txt", "--style-file", str(EXAMPLES / "style.txt"), "--change", "style:x"]]
        with patch("revision.request_revision") as api:
            for args in cases:
                with self.subTest(args=args):
                    code, out, err = self.run_main(args)
                    self.assertEqual(code, 2)
                    self.assertEqual(out, "")
                    self.assertIn("error", err.lower())
            api.assert_not_called()

    def test_cli_writes_paste_ready_files_and_separate_audit(self):
        req = request()
        client = client_for(response(req, style="Nasal male character, organ, frenchcore after dialogue."))
        real_request = request_revision
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "take-b"
            def draft(*args):
                return real_request(*args, client=client)
            with patch("revision.request_revision", side_effect=draft):
                code, stdout, stderr = self.run_main(self.revision_args() + ["--output-dir", str(output)])
            self.assertEqual(code, 0, stderr)
            self.assertEqual((output / "lyrics.txt").read_text(), LYRICS)
            self.assertNotIn("STYLE BLOCK", (output / "style.txt").read_text())
            self.assertIn("LYRICS", stdout)
            self.assertIn("PASSED", stderr)
            audit = json.loads((output / "revision-report.json").read_text())
            self.assertEqual(audit["integrity"], "passed")
            self.assertEqual(json.loads((output / "settings.json").read_text()), DEFAULT_SETTINGS)

    def test_failed_integrity_leaves_no_stdout_or_output_files(self):
        req = request()
        real_request = request_revision
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "take-b"
            for lyrics in [LYRICS.replace("Lowkenuinely", "genuinely"), LYRICS + "Extra line!\n"]:
                client = client_for(response(req, lyrics=lyrics))
                def draft(*args):
                    return real_request(*args, client=client)
                with patch("revision.request_revision", side_effect=draft):
                    code, stdout, stderr = self.run_main(self.revision_args() + ["--output-dir", str(output)])
                self.assertEqual(code, 2)
                self.assertEqual(stdout, "")
                self.assertIn("LYRIC INTEGRITY FAILED", stderr)
                self.assertFalse(output.exists())

    def test_existing_output_is_not_overwritten_and_api_not_called(self):
        with tempfile.TemporaryDirectory() as tmp, patch("revision.request_revision") as api:
            path = Path(tmp) / "lyrics.txt"
            path.write_text("previous output")
            code, _, _ = self.run_main(self.revision_args() + ["--output-dir", tmp])
            self.assertEqual(code, 2)
            api.assert_not_called()
            self.assertEqual(path.read_text(), "previous output")

    def test_cli_exact_edits_need_no_freeform_change(self):
        args = self.revision_args()[:-2] + ["--lyric-edits-file", str(EXAMPLES / "lyric-edits.json")]
        def draft(req, *_):
            return validate_revision(req, response(req))
        with patch("revision.request_revision", side_effect=draft):
            code, out, err = self.run_main(args)
        self.assertEqual(code, 0, err)
        self.assertEqual(out.count("keep my words intact!"), 1)
        self.assertIn("explicitly authorized", err)

    def test_utf8_bom_crlf_bad_encoding_and_empty_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "text.txt"
            p.write_bytes(b"\xef\xbb\xbfHello\r\n")
            self.assertEqual(read_text(p), "Hello\n")
            p.write_bytes(b"\xff\xfe")
            with self.assertRaisesRegex(RevisionError, "UTF-8"):
                read_text(p)
            with self.assertRaisesRegex(RevisionError, "must not be empty"):
                RevisionRequest("", STYLE, (("style", "jazz"),))

    def test_disk_error_does_not_leave_partial_output(self):
        sections, report = validate_revision(request(), response(request()))
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp) / "output"
            with patch.object(Path, "write_text", side_effect=OSError("disk full")):
                with self.assertRaises(OSError):
                    write_outputs(directory, sections, report)
            self.assertFalse(directory.exists())
            self.assertEqual(list(Path(tmp).iterdir()), [])


if __name__ == "__main__":
    unittest.main()
