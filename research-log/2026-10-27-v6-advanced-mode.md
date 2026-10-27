# v6 Advanced Mode — General Guidance Review

**Date:** 2026-10-27
**Status:** Documentation review; no Suno listening tests or paid API calls.
**Scope:** General prompting and the existing generation/triage entry points. Genre-specific retesting is outstanding.

## Primary Sources Reviewed

| Source | Published/updated | Used for |
|--------|-------------------|----------|
| [v6 FAQ](https://help.suno.com/en/articles/13924481) | 2026-09-09 | Variety, Max Mode, migration and Simple-mode workflow distinction |
| [Current Models: v6](https://help.suno.com/en/articles/13924737) | 2026-09-09 | Model choice |
| [Creative Sliders](https://help.suno.com/en/articles/6141377) | 2025-06-03 | General slider definitions; not a v6 preset study |
| [Own lyrics](https://help.suno.com/en/articles/2415873) | 2025-12-19 | Manual Custom workflow terminology |
| [Exclude](https://help.suno.com/en/articles/3161921) | 2025-12-19 | Dedicated exclusions field |
| [Vocal Gender](https://help.suno.com/en/articles/10153473) | 2026-09-09 | UI voice selection and Style description |

All accessed 2026-10-27. The core guides cite these at the relevant claims. Search results from community guides were not treated as official v6 specifications.

## Editorial Decisions

- Use “Advanced mode” for the requested manual workflow, while noting that official help still says “Custom.” Do not claim a verified client-wide renaming or UI layout.
- Make `core/suno-v6-fundamentals.md` the active base layer; retain the v5 fundamentals as historical context.
- Treat style templates, phrasing advice, tags and comparison settings as suggestions until listening evidence exists.
- Preserve intentional lyric wording and pronunciation spellings during prompt-only edits.
- Keep the existing CLI response markers, with all creation controls carried in the settings block.

## Claims Not Carried Forward as v6 Facts

- Fixed character caps and silent truncation, or an optimal number of style tags.
- Mandatory title case, second-chorus bridge placement, minimum four-line outros or tag-density limits.
- Guaranteed pipe-modifier isolation or exact multi-character voice assignment.
- Exact reference-audio thresholds for melody retention or voice identity.
- Universal quality improvements at particular slider values.

## Follow-up Evidence Needed

Record the exact model, complete fields, all settings, reference inputs and result links for multiple listening comparisons. Test one change at a time. Confirm spoken-versus-sung delivery, voice differentiation, section transitions and endings before calling a prompt remedy reliable. No uncertain fix was promoted to `pitfalls/` in this pass.

## Local Validation

- Checked relative Markdown links and code-fence balance.
- Compiled both Python scripts and ran their help commands plus genre listing.
- Loaded both KB paths and confirmed they use v6 fundamentals and controls.
- Checked existing output markers with numeric and nonnumeric settings, pronunciation spellings and the unconfirmed-fix flow.
- No Anthropic API or Suno generation calls were made.
