# Suno v5 Fundamentals

> **Status:** Researched and verified — 2026-05-09
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
- **Recommended length:** 4–7 descriptors, ~80–150 characters (v5.5 prompt accuracy improvement makes fewer, precise tags outperform long lists)
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
| Max song length | ~2 minutes | Up to 8 minutes (paid plans) |
| Audio quality | Good, required post-production | Radio-ready mix out of the box |
| Vocal naturalness | Noticeable AI character | Natural phrasing, breathing, harmonies |
| Metatag reliability | Inconsistent, especially [Bridge] | Significantly more consistent |
| Style tag adherence | Moderate | Stronger; exclusions (e.g. "no autotune") respected |
| [Build]/[Drop] tags | Not available / unreliable | Added and functional in v5 |
| Emotional nuance | Limited | Clearer emotion parsing, better dynamics |

**v4.5 still has advantages in some cases:** Faster generation, heavier/faster genres can sometimes sound better in v4.5 because v5's audio quality processing occasionally softens extreme transients.

---

## v5 → v5.5 Key Differences

> Released March 26, 2026. Research date: 2026-05-09.

| Feature | v5 | v5.5 |
|---------|-----|------|
| Voice cloning | Not available | Voices: upload/record your own voice for use in generations (Pro/Premier) |
| Custom model fine-tuning | Not available | Custom Models: train on your own tracks (Pro/Premier, up to 3 variants) |
| Taste-based personalization | Not available | My Taste: passive preference learning from your usage (all users) |
| Prompt accuracy | Strong | Significantly improved — genre prompts more faithfully follow conventions |
| Vocal quality | Natural | Improved: breathing and emotional transitions closer to real human singing |
| Mix quality | Radio-ready | Improved: soundstage and instrument separation at professional studio level |
| Audio Influence slider | Loose vibe extraction at mid-settings | Behaves more like Remix — melody bleed-through at much lower settings |
| Chinese/dialect singing | Limited | Comprehensively enhanced recognition and articulation |
| Metatags | Full v5 tag set | Identical — all v5 tags work exactly the same |
| Character limits | Style: 1000 / Lyrics: 5000 | Unchanged |
| Max song length | Up to 8 min (paid) | Unchanged — still 8 min max per generation |

**Core prompting unchanged:** All v5 prompts, style tags, and metatags work identically in v5.5. The only behavioral change affecting prompt engineering is the Audio Influence slider (see `core/sliders.md`).

---

## v5.5 New Features

### Voices (Pro/Premier subscribers)

Voice cloning — hear what you sound like singing your own Suno songs.

**Setup:**
1. Record or upload a singing sample (15 seconds – 4 minutes)
2. Speak a random verification phrase (anti-deepfake protection)
3. Your Voice appears in the Create menu

**Prompting with a Voice:**
- Your existing prompts work unchanged — Voice adds your vocal identity as an additional layer
- Can hint style with `"in my own voice"` in the style block
- For voice cloning: set Audio Influence to ~40% to preserve vocal character without losing quality
- Voices are private and account-locked — cannot be shared or used by others

### Custom Models (Pro/Premier, up to 3 variants)

Train a personalized version of v5.5 on your own music catalog.

**What it does:**
- Upload your original tracks; the model learns your genre/production style
- Reduces style drift — more accurate genre reproduction for your specific aesthetic
- Prompting: standard v5.5 prompts apply; Custom Model adds your style as a baseline layer

### My Taste (all users)

Passive preference system — no user action required.

**What it does:**
- Suno tracks which genres, moods, and styles you generate most
- Soft-biases future generations toward your preferences without overriding prompts
- Becomes more effective over time as your usage history grows

---

## Negative Prompting — More Effective in v5.5

V5.5's improved prompt accuracy makes negative constraints more reliably respected:

- `"no autotune"` → more natural, unprocessed vocal delivery
- `"no synths"` → forces acoustic/organic instrumentation
- `"no drums"` → stripped percussion, beatless feel
- `"no electric guitar"` → eliminates distortion bleed in acoustic genres

**Best practice:** Use 1–2 precise negative constraints. Over-using them triggers conflicting instructions.

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
- Suno official blog: "Suno v5.5: More Expressive. More You." (2026-03-26)
- Digital Music News: "Suno Launches Version 5.5 With New 'Voices' Feature" (2026-03-26)
- suno.hk: "Major Update: Suno V5.5 Full Rollout! Complete Analysis" (2026)
- suno.bi: "Suno V5.5 Is Here: Voices, Custom Models & My Taste Explained" (2026)
- AlijeeWrites GitHub: "Mastering Suno v5.5 with Prompts, Styles and AI Music" (2026)
- Hookgenius: "Suno v5.5 Guide: Voices, Custom Models & My Taste" (2026)
