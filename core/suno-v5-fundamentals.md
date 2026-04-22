# Suno v5 Fundamentals

> **Status:** Research in progress — populated 2026-04-22
> **Scope:** Suno v5 only. v4 differences noted explicitly where known.

---

## How Suno v5 Interprets Prompts

*(Research being compiled — this section will be populated from verified sources)*

Suno v5 processes two main inputs:

1. **Style block** — The genre/mood/instrument descriptor text. Controls the overall sonic character.
2. **Lyrics** — The full lyric text including metatags. Controls song structure and content.

These are processed independently; changes to the style block do not alter lyric interpretation and vice versa.

---

## Style Block Rules

- Comma-separated descriptors
- Recommended length: under ~120 characters
- More specific = more reliable output (e.g. "melancholic indie folk, fingerpicked acoustic guitar, breathy female vocals" beats "sad folk song")
- Avoid contradictory genre tags (e.g. "heavy metal, soft acoustic ballad" — Suno will interpolate unpredictably)

---

## Lyrics Processing

- Suno reads lyrics top-to-bottom and generates audio following the metatag structure
- Sections without metatags are treated as continuation of the previous section
- Very long lyric blocks (rough threshold: ~400+ words) may cause truncation or repetition

---

## v4 → v5 Key Differences

*(To be documented from research)*

---

## Instrumental vs. Vocal Tracks

- Add `[Instrumental]` as a standalone section tag for sections without vocals
- A fully instrumental song can be indicated in the style block ("instrumental") or via `[Instrumental]` wrapping the entire lyric body

---

## Known Limits

| Parameter | Known Limit |
|-----------|------------|
| Style block length | ~120 chars recommended |
| Lyric length | ~400 words before truncation risk |
| Max song length | ~4 min in standard generation |
| Section tags per song | No hard limit; 6-8 typical |

---

## Sources

*(To be populated from research)*
