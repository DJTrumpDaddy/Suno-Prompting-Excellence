---
name: suno-prompting-excellence
description: Create and revise Suno v6 Advanced mode prompts, style briefs, lyric cues and creation settings. Use for song prompt generation or troubleshooting Suno outputs; preserve supplied lyric wording unless edits are requested.
---

# Suno v6 Advanced Mode Prompting

## Load the Current Guidance

Read [KNOWLEDGE_STATUS.md](KNOWLEDGE_STATUS.md), [core/suno-v6-fundamentals.md](core/suno-v6-fundamentals.md), [core/metatags.md](core/metatags.md) and [core/sliders.md](core/sliders.md). Load the matching `genres/[genre].md` and [pitfalls/_index.md](pitfalls/_index.md) as needed.

Treat existing v5/v5.5 genre advice as historical hypotheses unless a dated v6 result supports it. Research material gaps using official Suno documentation first. Separate documented features, user-tested outcomes and untested advice; never invent a successful test or an internal model mechanism.

## Produce Four Artifacts

**TITLE:** The display title.

**STYLE BLOCK:** A paste-ready compact brief covering genre/groove, instruments, vocal character, production and important arrangement changes. Use readable phrases or sentences; do not impose an invented tag count or character limit.

**LYRICS:** Exact supplied words with sparse section cues, or newly written lyrics when requested. Preserve pronunciation-directed spelling, syllable splits and punctuation. Put explanations outside the paste-ready block.

**SETTINGS:** A table with model, Weirdness, Style Influence, Variety, Max Mode, Exclude and Vocal Gender/Instrumental when relevant. Include Audio Influence only when the workflow provides it for an audio reference. State values or "use current UI default; record value" and give brief reasons. Keep settings out of the Style and Lyrics fields.

For a controlled first draft, use the choices in `core/sliders.md`, including Variety 0. Label starting advice as untested, not optimal. Check the current client's limits rather than asserting v5 caps.

## Apply Prompting Judgment

- Describe voices by audible traits; a character name alone does not specify timbre.
- Keep lyric cues concise. Do not promise exact speaker switching, tempo, section lengths or tag execution.
- Use Exclude for unwanted traits and positive Style wording for the intended sound.
- Do not assume the Style field executes Simple-mode editing or source-combination operations.
- Resolve contradictions without flattening an intentional genre blend or rewriting the user's words.

## Triage and Maintain

Classify an issue as structural, sonic, style or lyrics. Check the model, full input text, settings and references, then propose one comparison with a before/after example. Call the diagnosis a hypothesis when evidence is incomplete.

Request the listening result before recording a fix as confirmed. Save failed or unconfirmed experiments in `research-log/`; save confirmed fixes in `pitfalls/` with the exact model and evidence. Update `KNOWLEDGE_STATUS.md` after a KB change and commit changes according to [CLAUDE.md](CLAUDE.md).
