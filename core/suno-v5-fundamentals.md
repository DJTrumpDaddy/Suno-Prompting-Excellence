# Suno v5 Fundamentals

> **Status:** Researched and verified — 2026-04-22
> **Scope:** Suno v5 and v5.5. v4/v4.5 differences noted explicitly.

---

## How Suno v5 Interprets Prompts

Suno v5 processes two independent inputs that do different jobs:

| Input | Field | Purpose |
|-------|-------|---------|
| **Style block** | Style field | Defines the broad sound world: genre, mood, instruments, production character |
| **Lyrics** | Lyrics/Custom field | Controls song structure, content, and local performance behavior via metatags |

These fields are processed separately. Style descriptors don't affect lyric interpretation, and lyric-level tags don't influence the style/tone of the track unless you also specify in the style block.

**Key principle:** The Style field is for *what it sounds like*. The Lyrics field is for *how it's structured*.

---

## Style Block Rules

- **Character limit:** 1000 characters in v5/v5.5 (silently truncated beyond this — no warning)
- **Recommended length:** 8–15 descriptors, ~120–200 characters for readability
- **Format:** Comma-separated tags
- **Front-load** your most important genre/mood tags — truncation removes the end first
- Specificity wins: `"synth-pop, melancholic, breathy female vocals, analog pads"` beats `"sad pop"`

### The 5-Part Style Formula
1. **Genre + subgenre** — `indie folk`, `melodic death metal`, `lo-fi hip-hop`
2. **Mood + energy** — `melancholic`, `euphoric`, `tense`, `laid-back`
3. **Vocal character** — `breathy female vocals`, `raspy male tenor`, `no vocals / instrumental`
4. **Key instruments + production** — `fingerpicked acoustic guitar, warm upright bass`, `808s, punchy hi-hats, wide stereo field`
5. **Tempo/era feel (optional)** — `mid-tempo`, `120 BPM`, `80s production aesthetic`

### Style Block Mistakes to Avoid
- **Contradictory tags** — `heavy metal, soft acoustic ballad` → Suno interpolates unpredictably
- **Over-stacking modifiers** — more than ~15 tags causes drift and dilution
- **Redundant synonyms** — `sad, melancholic, sorrowful` → pick one strong descriptor
- **Describing the song's theme in the style block** — that belongs in lyrics, not style

---

## Lyrics Field Rules

- **Character limit:** ~3,000 characters in standard mode; up to 5,000 characters in custom mode
- **Practical target:** 30–40 lines for a 3–4 minute song (~200–300 words)
- **Non-custom mode:** 500 character limit (much shorter — custom mode needed for full songs)
- Lyrics are read top-to-bottom; Suno generates audio following the metatag structure in sequence

### Lyric Writing Tips

**Punctuation as performance direction:**
- Commas, dashes, and ellipses signal micro-pauses and breath: `"I ran—and then I stood, / watching the lights…"`
- Extend vowels for sustained notes: `"Loooove"`, `"Ohhhh"`, `"Noooo"` — extra vowels act as dynamic markings

**Line density affects pacing:**
- Short, sparse lines → slower, more spacious delivery
- Dense, run-on lines → faster, more compressed delivery (useful for rap or urgency)

---

## v4 / v4.5 → v5 Key Differences

| Feature | v4 / v4.5 | v5 |
|---------|----------|-----|
| Max song length | ~2 minutes | ~4 minutes |
| Audio quality | Good, required post-production | Radio-ready mix out of the box |
| Vocal naturalness | Noticeable AI character | Natural phrasing, breathing, harmonies |
| Metatag reliability | Inconsistent, especially [Bridge] | Significantly more consistent |
| Style tag adherence | Moderate | Stronger; exclusions (e.g. "no autotune") respected |
| [Build]/[Drop] tags | Not available / unreliable | Added and functional in v5 |
| Song length capability | ~2 min | ~4 min with consistent quality |
| Emotional nuance | Limited | Clearer emotion parsing, better dynamics |

**v4.5 still has advantages in some cases:** Faster generation, heavier/faster genres can sometimes sound better in v4.5 because v5's audio quality processing occasionally softens extreme transients.

---

## Instrumental vs. Vocal Tracks

- Add `[Instrumental]` as a standalone section to suppress vocals for that section
- For fully instrumental tracks, add `instrumental` to the style block AND/OR wrap all content in `[Instrumental]`
- `[Solo]` triggers a featured instrument solo — most reliable when the instrument is also named in the style block

---

## Character Limits Summary

| Field | Mode | Limit | Notes |
|-------|------|-------|-------|
| Style block | Any | 1000 chars | Silently truncated; front-load critical tags |
| Lyrics | Non-custom | ~500 chars | Use custom mode for full songs |
| Lyrics | Custom | ~3000–5000 chars | ~30–40 lines for 3–4 min song |

---

## Sources

- CometAPI — "How to instruct Suno v5 with lyrics" (2025)
- HookGenius — "Suno v5 Complete Guide" (2026)
- HookGenius — "Suno Character Limits: Why Your Prompts Get Cut Off" (2026)
- Suno official help: "Introducing v5"
- JackRighteous — "Custom Lyrics in Suno v5: Precision & Control"
- Medium / Kristopher Dunham — "Suno v5 and Studio: Complete Guide" (2025)
