# Suno v5 Metatags Reference

> **Status:** Researched and verified — 2026-05-09
> **Scope:** Suno v5 and v5.5. v5 respects metatags significantly more consistently than v4.
> **v5.5 audit (2026-05-09):** No metatag changes confirmed between v5 and v5.5. All tags function identically. Reliability tiers unchanged. The same tag set applies to both versions.

---

## How Metatags Work

Metatags are bracketed keywords placed in the **Lyrics field** on their own line, *before* the section they describe. They are "structural reinforcement cues" — they tell Suno where section boundaries are and what performance intent applies.

```
[Verse 1]
In the silence of the night
I feel you close to me

[Chorus]
We are fire and light
```

**Rules:**
- Each metatag goes on its own line
- Use title case: `[Verse]` not `[verse]` (lowercase may be ignored)
- Keep tags short: 1–3 words maximum; longer tags are less reliably parsed
- Don't over-stack — more than ~1 tag per 4 lines causes skipping behavior
- Tags work best as structural signals, not paragraph-level micro-direction

---

## Structure Tags

| Tag | Effect | Notes |
|-----|--------|-------|
| `[Intro]` | Opens the song, usually instrumental or short | Suno may extend or shorten; keep it brief |
| `[Verse]` / `[Verse 1]` | Standard lyric verse | Numbered variants produce more distinct content |
| `[Verse 2]` | Second verse | Numbered helps Suno differentiate from Verse 1 |
| `[Pre-Chorus]` | Build section before chorus | Reliably triggers transitional energy |
| `[Chorus]` | Main hook/refrain | Most-weighted section; repeat lyrics reinforce memorability |
| `[Post-Chorus]` | Continuation after chorus | Less consistent; use sparingly or skip |
| `[Bridge]` | Contrasting section | **Place after second chorus** — before that, often skipped |
| `[Hook]` | Short, memorable melodic phrase | Interchangeable with `[Chorus]` in practice |
| `[Outro]` / `[Ending]` | Closing section | Give at least 4 lines or Suno will loop |
| `[Fade Out]` | Signals gradual volume fade at end | Works in most genres |

---

## Instrumental & Energy Tags

| Tag | Effect | Notes |
|-----|--------|-------|
| `[Instrumental]` | Suppresses vocals for that section | Most reliable when wrapping an entire section |
| `[Interlude]` | Short instrumental break between sections | Implies shorter gap than `[Instrumental]` |
| `[Break]` | Drum break or full arrangement drop | In EDM/hip-hop, triggers a full breakdown moment |
| `[Solo]` | Featured instrument solo | Name the instrument in the style block for best results |
| `[Build]` | Gradually increases energy/complexity/intensity | v5 addition; use before a Drop or Chorus for tension |
| `[Drop]` | Payoff moment — rhythm, bass, or hook engages fully | v5 addition; only impactful when preceded by a thin Build |

### [Build] and [Drop] Usage Rules
- `[Build]` = the rising conflict; `[Drop]` = the moment it breaks open
- Use `[Build]` in bridge or pre-chorus positions only — not in every section
- The verse before a build should be **musically thin** to create contrast
- Don't stack `[Build]` with 10+ other modifiers — causes drift
- Genre fit: EDM, dubstep, hip-hop, pop — less relevant for folk or classical

---

## Vocal Delivery Tags

| Tag | Effect | Notes |
|-----|--------|-------|
| `[Rap]` / `[Rap Verse]` | Hip-hop vocal delivery | Suno defaults to melody; tag explicitly to force rap |
| `[Spoken]` / `[Spoken Word]` | Spoken delivery, no melody | Reliable in v5; may drift to half-sung occasionally |
| `[Whispered]` | Very soft, close-mic vocal | Works well for intimacy; genre-dependent |
| `[Belted]` | Powerful, high-volume vocal delivery | Best in pop, gospel, musical theatre |
| `[Falsetto]` | High, light head-voice | Works in R&B, indie pop |
| `[Ad-lib]` | Improvised-sounding background vocals | Inconsistent; may be ignored |
| `[Harmonies]` | Stacked background harmonies | Most reliable in pop, soul, gospel |
| `[Duet]` | Two-voice delivery | Specify male/female in style block for best result |

### Forcing Rap When Suno Sings Instead
Add to style block: `"rap vocals, spoken flow, rhythmic delivery"`
Add to lyrics section header: `[Rap Verse]` instead of `[Verse]`
Both together = most reliable.

---

## Pipe Syntax (Multi-Modifier Tags)

Suno v5 supports stacking multiple descriptors inside a single section tag using the pipe `|` character. This lets you set energy, mood, and delivery at the section level rather than relying on the style block to do it globally.

```
[Intro | low energy | ambient | minimal]
[Verse 1 | spoken word | low energy]
[Chorus | high energy | layered vocals | euphoric]
[Bridge | intimate | soft | close-mic]
[Drop | high energy | distorted kick | intense]
```

**Rules:**
- Structure tag comes first: `[Verse | ...]` not `[low energy | Verse]`
- Pipe descriptors apply only to that section — they don't bleed into the next
- Use 1–3 modifiers max; stacking more causes drift
- Most useful for energy transitions: a `[Verse | low energy]` before a `[Drop | high energy]` creates the contrast the drop needs

**Confirmed working modifier vocabulary:**
- Energy: `low energy`, `high energy`, `building energy`
- Mood: `euphoric`, `intense`, `intimate`, `melancholic`, `uplifting`
- Delivery: `spoken word`, `whispered`, `close-mic`, `ambient`, `minimal`

---

## Energy & Mood Standalone Tags

These can be placed on their own line to shift the section's character:

```
[Energy: High]
[Energy: Low]
[Mood: Uplifting]
[Mood: Intense]
```

Less reliable than pipe syntax for section-scoped control — they can bleed into adjacent sections. Prefer pipe syntax when you need energy to change at a specific section boundary.

---

## Inline Vocal Modifiers

These can be used inside a section alongside lyrics (not necessarily on their own line):

```
[Verse 1]
[Whispered] In the silence of the night
[Building] I feel you close to me
[Belted] WE WERE NEVER MEANT TO SAY GOODBYE
```

---

## Multi-Voice / Character Tags

For songs with multiple distinct voices:
```
[Verse 1]
[Alice:] I waited by the door
[Bob:] I never thought you'd come
[Together:] But here we are
```
Specify voice characters in style block for personality consistency.

---

## Complete Tag Quick Reference

### Confirmed Reliable in v5
`[Intro]` `[Verse]` `[Verse 1]` `[Verse 2]` `[Verse 3]`
`[Pre-Chorus]` `[Chorus]` `[Bridge]` `[Outro]`
`[Instrumental]` `[Break]` `[Solo]`
`[Build]` `[Drop]`
`[Rap]` `[Rap Verse]` `[Spoken]`
`[Whispered]` `[Belted]` `[Harmonies]`

### Use With Care (Variable Reliability)
`[Post-Chorus]` `[Hook]` `[Interlude]` `[Ad-lib]` `[Falsetto]`
`[Fade Out]` — works in most but not all genres

### Pipe Syntax (Section-Scoped Modifiers)
`[Verse | low energy]` `[Chorus | high energy]` `[Intro | ambient | minimal]`
`[Verse | spoken word | low energy]` `[Drop | high energy | intense]`

### Known Problematic
- `[verse]` (lowercase) — may be ignored; use title case
- Bridges placed before the second chorus — often skipped
- More than ~1 tag per 4 lines — causes tag skipping
- Outro with fewer than 4 lines — Suno loops it
- Pipe modifiers beyond 3 descriptors — causes drift

---

## Recommended Song Structure Template

```
[Intro]
(optional 2-4 lines or leave empty for pure instrumental)

[Verse 1]
(4-8 lines)

[Pre-Chorus]
(2-4 lines — optional)

[Chorus]
(4-6 lines — the hook)

[Verse 2]
(4-8 lines — new content)

[Pre-Chorus]
(optional repeat)

[Chorus]
(repeat chorus lyrics)

[Bridge]
(4-6 lines — contrasting content)

[Chorus]
(final chorus — optional repeat)

[Outro]
(4+ lines — fade or definitive end)
```

---

## v5.5 Metatag Notes

> Research date: 2026-05-09

**No changes between v5 and v5.5.** All existing metatags work identically. No new tags were added; no tags were deprecated; no reliability tiers changed.

Community sources that continued referencing MILO-1080 in v5.5 context (blakecrosley.com) could not be accessed for verification — flagged for future research. All other confirmed sources agree: the tag system is unchanged.

**One practical improvement:** v5.5's improved prompt accuracy makes the existing tags slightly more reliable, particularly for niche genres. This is not a new tag behavior but an improvement in model compliance.

---

## Sources

- JackRighteous — "Suno AI Meta Tags & Song Structure Command Guide" (2026)
- JackRighteous — "Mastering [Build] & [Drop] in Suno AI for Dynamic Tracks"
- HookGenius — "All Suno Metatags: Structure, Voice & Style" (2026)
- Suno.wiki — "Voice Tags" FAQ
- Medium / James 99 — "The Ultimate Guide to Suno AI Metatags" (2025)
- TitanXT — "Guide to Suno AI Prompting: Metatags Explained"
- LilyS AI Notes — "Suno v5 Powerful Metatags" (2025)
- v5.5 audit: research-log/2026-05-09-v5.5-changes.md
