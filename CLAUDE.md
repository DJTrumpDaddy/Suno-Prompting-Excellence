# Suno v6 Advanced Mode — Repository Instructions

Maintain this KB and use it to draft Suno prompts. Follow [SKILL.md](SKILL.md) for the four-artifact generation format.

## Before Generating

1. Read `KNOWLEDGE_STATUS.md`, `core/suno-v6-fundamentals.md`, `core/metatags.md` and `core/sliders.md`.
2. Load the matching genre file and relevant pitfalls. Check version scope; existing genre recipes are v5/v5.5 material, not validated v6 presets.
3. Research material gaps with official Suno sources first. Distinguish documented controls from listening-tested outcomes and untested workflow advice.
4. Produce Title, Style block, Lyrics and Settings. Include Variety, Max Mode and Exclude where applicable, along with the model and creative sliders.
5. Preserve supplied wording and pronunciation spellings unless edits are requested. Keep UI settings and explanations out of paste-ready Style/Lyrics text.

Do not enforce old character caps, descriptor counts, bridge placement or outro-length rules as v6 facts. Do not claim undocumented parser internals or guaranteed tag behavior. The current v6 core guides take precedence over historical notes.

## Feedback Triage

1. Classify the issue: structural, sonic, style or lyrics.
2. Check `pitfalls/_index.md`, the exact model, prompt, controls and reference inputs.
3. Propose one targeted comparison and explain the evidence or uncertainty.
4. Ask the user to test it. Do not report a fix as confirmed without a listening result.
5. Record a confirmed remedy in `pitfalls/`; record failed or unconfirmed attempts in `research-log/`. Include model, date and result evidence.

## KB Updates

- Use `genres/_template.md` for new genre files and set the actual model/evidence scope.
- Update `KNOWLEDGE_STATUS.md` after KB changes. A focused update does not count as a full genre audit.
- Cite source URLs and access dates; separate official documentation from observations and conjecture.
- Commit KB changes with a descriptive message, for example `kb: update v6 Advanced mode prompting guidance`.

## CLI Tools

```bash
python generate.py "your song idea here"
python generate.py --genre synthwave "neon-soaked love song"
python feedback.py "the bridge was ignored entirely"
python feedback.py "the bridge was ignored" --commit "user-tested remedy here" --filename bridge-ignored
python feedback.py "vocals were buried" --log-failed "adding clear vocals to Style"
```

The CLI uses the Anthropic API to draft text, not the Suno generation API. It does not browse automatically; report research gaps rather than claiming to have researched or heard a result. Keep the existing `---TITLE---`, `---STYLE---`, `---LYRICS---`, `---SLIDERS---` and `---NOTES---` parser markers. The `---SLIDERS---` block now carries all creation settings, including nonnumeric options.
