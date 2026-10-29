# Suno v6 Advanced Mode Prompting — Knowledge Base

A maintained knowledge base for creating Suno prompts with Claude or other assistants. The current general guidance targets **v6 Advanced mode**: manual Style, Lyrics and creation controls. Suno's help pages also call this workflow Custom mode.

**General guidance reviewed:** 2026-10-27. This was a documentation review, not an audio-generation benchmark. A focused v6 vocal lounge jazz guide separates sourced musical guidance from untested prompt experiments. Older genre guides retain their v5/v5.5 scope.

## Start Here

| File | Purpose |
|------|---------|
| [core/suno-v6-fundamentals.md](core/suno-v6-fundamentals.md) | Current fields, style brief, vocal direction, lyric preservation and sources |
| [core/sliders.md](core/sliders.md) | Creative controls, including Variety and Max Mode |
| [core/metatags.md](core/metatags.md) | Sparse lyric cues and limits of unverified tag rules |
| [genres/vocal-lounge-jazz.md](genres/vocal-lounge-jazz.md) | Intimate small-combo vocal swing: instrumentation, phrasing, pacing and v6 comparisons |
| [KNOWLEDGE_STATUS.md](KNOWLEDGE_STATUS.md) | Coverage, evidence gaps and historical genre settings |
| [SKILL.md](SKILL.md) / [CLAUDE.md](CLAUDE.md) | Reusable generation and maintenance instructions |
| `genres/[genre].md` | Genre vocabulary and historical examples; check version scope |
| [pitfalls/_index.md](pitfalls/_index.md) | Reported problems and confirmed fixes |
| `research-log/` | Dated research and experiments |

## Generation Workflow

1. Read the coverage map and current core guides.
2. Load relevant genre material; separate historical suggestions from v6 evidence.
3. Produce four artifacts: **Title**, **Style block**, **Lyrics**, **Settings**. Settings includes Exclude and applicable controls, not just sliders.
4. Preserve supplied lyrics and deliberate pronunciation spellings unless edits are requested.
5. Iterate with one change at a time. Record sources or listening evidence before marking a result confirmed.

The CLI tools `generate.py` and `feedback.py` load the v6 core guide. They use Anthropic to draft prompts or diagnose issues; they do not generate Suno audio or automatically browse for new research. Their existing output markers remain compatible.

## Revise an Existing Song Without Rewriting Its Words

Requires Python 3.10+ and `python -m pip install -r requirements.txt`. Set
`ANTHROPIC_API_KEY` in your environment. Existing commands still work:

```bash
python generate.py "an 80s synth ballad about a road trip with my dad"
python generate.py --genre metal "a song about overcoming grief"
python generate.py --list-genres
```

Revision mode reads **your current local UTF-8 files**; it does not need previous
chat attachments or download anything from Suno. Use a repeatable, scoped
`--change` for exactly what should change:

```bash
python generate.py --revise \
  --lyrics-file song-lyrics.txt --style-file song-style.txt \
  --change "style:Give the male character a nasally nerdy voice; retain the genre, arrangement, and other voices." \
  --output-dir revision-voice
```

The scopes are `style`, `metatags`, and `settings`. Fields without their scope are
locked. The Lyrics words remain locked **even when metatags can change**. Existing
`--genre` / `-g` and `--model` / `-m` also work with `--revise`; `--model` selects
the **Anthropic drafting model**, while `Model` in the settings file selects Suno.
Do not supply a positional song idea with `--revise`.

### Example: Keep Frenchcore Kicks Out of the Spoken Intro

The included files are illustrative text, not an earlier attachment or a tested
musical remedy. This command proposes a Style and cue revision while keeping the
dialogue, unusual spellings, repeated choruses, and settings fixed:

```bash
python generate.py --revise \
  --lyrics-file examples/revision/lyrics.txt \
  --style-file examples/revision/style.txt \
  --settings-file examples/revision/settings.json \
  --change "style:Keep the opening spoken dialogue unaccompanied; introduce frenchcore kicks only after that exchange. Preserve the later genre and instrumentation." \
  --change "metatags:Use a sparse opening cue for unaccompanied spoken dialogue; preserve the later section labels." \
  --output-dir revision-intro
```

For a controlled comparison, run **one scope/change at a time** and hold all
other inputs, settings, and audio references fixed. Text integrity does not prove
Suno will honor a cue; listen to the generated alternatives.

### Explicit Lyric Edits

Free-form `--change` text never disables protection. To deliberately change words,
punctuation, or phonetics, provide a JSON array of **exact replacements** using
`--lyric-edits-file`. For example, `examples/revision/lyric-edits.json` contains:

```json
[
  {
    "line": 11,
    "before": "Oh-oh-oh, leave my words alone!",
    "after": "Oh-oh-oh, keep my words intact!"
  }
]
```

```bash
python generate.py --revise \
  --lyrics-file examples/revision/lyrics.txt \
  --style-file examples/revision/style.txt \
  --lyric-edits-file examples/revision/lyric-edits.json \
  --output-dir revision-last-chorus
```

Only the **second occurrence** changes. Lines are 1-based physical lines in the
original file, including blank and cue lines. `before` must match exactly; duplicate
line targets and stale/mismatched text are rejected before an API call. `after`
may contain `\n` for an explicit multiline replacement, or be empty to leave a
blank line. All line numbers refer to the original file. Cue edits belong in a
`metatags:` request, not this file. The model must reproduce the authorized target
and cannot take the edit as permission to rewrite anything else.

### What the Integrity Check Guarantees

- Non-cue text is compared **exactly and in sequence**, including words,
  capitalization, punctuation, phonetic spellings, spaces, line breaks, and repeat
  counts. No spellcheck, fuzzy matching, Unicode normalization, or deduplication.
- UTF-8 BOMs are accepted on input; CRLF/CR line endings normalize to LF.
  Otherwise whitespace, including trailing newlines, stays protected.
- This tool's local convention treats a line consisting entirely of one or more
  square-bracket groups, such as `[Verse 1]` or `[Male, Deadpan]`, as a metatag.
  This is **not a claim about Suno's parser**. Inline brackets, parentheses, and
  speaker labels outside brackets remain protected text.
- If an entire bracketed line is meant to be sung/spoken literally, mark its
  original line number with `--literal-line 5` (repeatable). Every exact occurrence
  of that line is then protected, even if surrounding cues move.
- Cue changes are tracked separately with their positions relative to protected
  lines. Without `metatags:` permission, cues cannot change or move either.
- Missing, malformed, duplicate-key, truncated, or integrity-violating responses
  exit with status **2**, publish no paste-ready output, and report the problem on
  stderr. No silent repair or automatic paid retry. A lyric mismatch includes a
  diff for diagnosis. Recheck the request and retry explicitly if desired.

The guard checks text, not meaning or audio. Within an authorized Style, cue, or
settings scope, whether a proposal satisfies the requested musical change still
needs review. Cue text can be ignored or sung by Suno. In particular, do not put
unmarked literal sung words on bracket-only lines.

### Outputs and Settings

Validated fields print to stdout. Integrity results and separate **lyric-text**
and **metatag** diffs print to stderr. `--output-dir` writes a **new** directory:

| File | Use |
|------|-----|
| `style.txt` | Paste directly into Style |
| `lyrics.txt` | Paste directly into Lyrics; no report text or wrappers |
| `settings.txt` | Apply the listed v6 controls in Advanced mode |
| `settings.json` | Reuse as `--settings-file` on the next revision |
| `title.txt` | Suggested display title |
| `revision-report.json` | Separate text/cue/Style diffs, settings before/after, source/target/output hashes, requested changes, and notes |

Existing output directories are rejected before drafting to prevent overwriting
files. Source files are never edited. Validation completes before the output
directory is published.

`--settings-file` accepts a JSON object with string values. Supported keys are
`Model`, `Weirdness`, `Style Influence`, `Variety`, `Max Mode`, `Exclude`,
`Vocal Gender`, and `Instrumental`. Missing values use the untested starting
advice from `core/sliders.md`: v6, Weirdness 50, Variety 0, Max Mode Off,
Instrumental Off, no Exclude, and current UI defaults for Style Influence and
Vocal Gender. **These are not inferred settings from your existing song**; supply
its actual controls to preserve them. A `settings:` request is required to change
the resulting baseline.

For a workflow that actually uses source audio, add `--audio-reference` to include
Audio Influence (current UI default unless supplied in the settings JSON). This
flag describes your workflow; it does not load, upload, or analyze audio.

### Tests and Reuse

Run the offline suite from the repository root; no SDK, API key, or paid calls
are needed:

```bash
python -m unittest discover -s tests -v
```

Tests cover dialogue, punctuation and unusual spellings, repeated sections,
literal and inline brackets, cue relocation, narrowly authorized lyric edits,
field locking, malformed/truncated responses, output publication, and the old
CLI. API behavior is mocked; these tests do not validate live model compliance
or Suno audio.

`revision.py` also exposes `RevisionRequest`, `request_revision`,
`validate_revision`, and `write_outputs` for other callers. The drafting client
is injectable. Call `validate_revision` before exposing a response; it returns
paste-ready sections and an audit report or raises `RevisionError`.

## Scope and Updates

Use [core/suno-v5-fundamentals.md](core/suno-v5-fundamentals.md) only for historical context. A documented field or control is not evidence that a prompt trick works reliably, and a polished template is not an audio test.

When updating the KB, cite the source and date, identify the model and evidence level, and update `KNOWLEDGE_STATUS.md`. Record uncertain ideas in the research log; put confirmed remedies in `pitfalls/` only after a reported listening test.
