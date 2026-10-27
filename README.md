# Suno v6 Advanced Mode Prompting — Knowledge Base

A maintained knowledge base for creating Suno prompts with Claude or other assistants. The current general guidance targets **v6 Advanced mode**: manual Style, Lyrics and creation controls. Suno's help pages also call this workflow Custom mode.

**General guidance reviewed:** 2026-10-27. This was a documentation review, not an audio-generation benchmark. Existing genre guides retain their v5/v5.5 scope until individually tested.

## Start Here

| File | Purpose |
|------|---------|
| [core/suno-v6-fundamentals.md](core/suno-v6-fundamentals.md) | Current fields, style brief, vocal direction, lyric preservation and sources |
| [core/sliders.md](core/sliders.md) | Creative controls, including Variety and Max Mode |
| [core/metatags.md](core/metatags.md) | Sparse lyric cues and limits of unverified tag rules |
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

## Scope and Updates

Use [core/suno-v5-fundamentals.md](core/suno-v5-fundamentals.md) only for historical context. A documented field or control is not evidence that a prompt trick works reliably, and a polished template is not an audio test.

When updating the KB, cite the source and date, identify the model and evidence level, and update `KNOWLEDGE_STATUS.md`. Record uncertain ideas in the research log; put confirmed remedies in `pitfalls/` only after a reported listening test.
