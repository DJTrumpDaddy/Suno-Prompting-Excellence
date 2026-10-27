# Suno v6 Advanced Mode Controls

> **Reviewed:** 2026-10-27. Official control descriptions plus explicitly untested starting advice.
> **Scope:** v6 family; exact behavior can vary by model, reference and workflow.

## What the Controls Mean

Set controls in the UI, separately from the Style and Lyrics text.

| Control | Documented function | Practical use |
|---------|---------------------|---------------|
| Weirdness | Moves from safe to chaotic; Suno describes 50% as its normal reference point [1] | Start at 50; compare lower values if you want less experimentation |
| Style Influence | Adjusts adherence to the style input from loose to strong [1] | Start with the UI default, record it, and compare stronger adherence if needed |
| Variety | Can alter the style prompt [2] | Use 0 for comparisons of your written prompt; raise deliberately for exploration |
| Audio Influence | Available with an audio upload [1] | Record the source and workflow; start from the UI default and compare settings |
| Max Mode | Uses extra credits for more intensive generation [2] | Consider for a promising longer or fidelity-sensitive take |

Variety, Weirdness and Style Influence address different things. Turning Variety off does not remove randomness or lock a melody. More Style Influence does not guarantee every lyric, section or voice assignment will be followed.

## Suggested First Pass — Not a Validated Preset

| Setting | Starting choice | Reason |
|---------|-----------------|--------|
| Model | v6, if available | Start with the model Suno recommends for control [3] |
| Variety | 0 | Keep your intended style wording for the comparison |
| Weirdness | 50 | Use the documented reference point before tuning |
| Style Influence | Current UI default; record the number | Avoid inventing a universal genre optimum |
| Audio Influence | N/A without an upload; otherwise record the UI default | Reference dependence matters |
| Max Mode | Off for an exploratory draft | Spend extra only when the experiment warrants it |
| Exclude / Vocal Gender | Match the request, if applicable | Keep separate from slider values |

These choices are workflow advice, not quality guarantees. If a concrete alternative is needed, compare Weirdness 30 versus 50 or a modest increase in Style Influence, changing only one control at a time. Those alternatives have not been audio-tested here.

## Troubleshooting Experiments

- **Style text changed:** inspect Variety and whether a prompt-enhancement action was used.
- **Wrong sound:** simplify conflicting descriptions, check references/personalization, then compare Style Influence settings.
- **Too unpredictable:** compare lower Weirdness while keeping the prompt and other inputs fixed.
- **Unwanted source melody:** compare Audio Influence settings or remove the reference. No percentage guarantees "vibe only."
- **Missing section or wrong voice:** inspect Lyrics and Style together and listen across several takes. Neither tags nor sliders guarantee structure.

Record the exact model, input text, values, reference, result links and observed outcome. Do not label a fix confirmed based only on a generated suggestion.

## Legacy Settings

Earlier revisions contained v5/v5.5 genre matrices and precise Audio Influence thresholds (including an 8% "vibe-only" rule and 40% voice rule). They are not validated v6 settings. Historical genre tables remain in [KNOWLEDGE_STATUS.md](../KNOWLEDGE_STATUS.md); use them only as experiments with their original version scope.

## Sources

Accessed 2026-10-27:

1. [Suno: How to Use: Creative Sliders](https://help.suno.com/en/articles/6141377) — updated 2025-06-03; official general definitions, not a v6 threshold study.
2. [Suno: v6 FAQ](https://help.suno.com/en/articles/13924481) — updated 2026-09-09; Variety and Max Mode.
3. [Suno: Current Models: v6](https://help.suno.com/en/articles/13924737) — updated 2026-09-09.
