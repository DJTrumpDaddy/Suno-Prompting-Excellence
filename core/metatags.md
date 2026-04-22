# Suno v5 Metatags Reference

> **Status:** Research in progress — populated 2026-04-22
> **Scope:** Suno v5 behavior. Quirks noted where version-specific.

---

## Standard Section Tags

| Tag | Effect | Notes |
|-----|--------|-------|
| `[Intro]` | Opens the song, usually instrumental or short | Suno may extend or shorten automatically |
| `[Verse]` or `[Verse 1]` | Standard lyric verse | Numbered variants (`[Verse 1]`, `[Verse 2]`) help differentiation |
| `[Pre-Chorus]` | Build section before chorus | Reliably triggers a transitional feel |
| `[Chorus]` | Main hook | Most-weighted section; repeated lyrics reinforce it |
| `[Post-Chorus]` | Continuation after chorus | Less reliably implemented; use sparingly |
| `[Bridge]` | Contrasting section | Place after second chorus; may be ignored if placed too early |
| `[Outro]` | Closing section | Can be tagged `[Outro]` or `[Fade Out]` |

---

## Instrumental & Vocal Control Tags

| Tag | Effect | Notes |
|-----|--------|-------|
| `[Instrumental]` | Suppresses vocals for that section | Works most reliably when it wraps an entire section |
| `[Interlude]` | Short instrumental break | Similar to `[Instrumental]` but implies a shorter gap |
| `[Break]` | Drum break or full drop | Genre-dependent; in EDM/hip-hop contexts triggers a full breakdown |
| `[Solo]` | Instrument solo (guitar, synth, etc.) | Works better when instrument is specified in style block |

---

## Vocal Style Tags

| Tag | Effect | Notes |
|-----|--------|-------|
| `[Spoken]` | Spoken word delivery, no melody | Reliable in v5; may drift to half-sung |
| `[Rap]` | Rap/hip-hop vocal delivery | Works well; combine with fast lyric density |
| `[Hook]` | Short, repeated melodic phrase | Often used interchangeably with `[Chorus]` |
| `[Ad-lib]` | Improvised-sounding vocal additions | Less consistent; may be ignored |

---

## Annotation / Modifier Tags

*(Research in progress — these are tags that go inside section headers)*

- `[Verse 1 — melancholic]` — emotional direction within a section
- `[Chorus — big, anthemic]` — intensity modifier
- Named singer tags: `[Alice:]` before a lyric line (multi-voice songs)

---

## Known Quirks

- **`[Bridge]` placement matters** — bridges placed before the second chorus often get skipped. Place after the second chorus.
- **Numbered sections help** — `[Verse 1]` and `[Verse 2]` are more likely to produce distinct content than two `[Verse]` tags.
- **Case sensitivity** — `[verse]` (lowercase) may be ignored. Use title case: `[Verse]`.
- **Tag density** — too many tags in a short lyric block (>1 tag per 4 lines) can cause skipping.
- **`[Outro]` and repetition** — Suno v5 tends to loop the outro if it's too short. Give it at least 4 lines.

---

## Section Tag Placement Rules

```
[Intro]          ← Always first if used
[Verse 1]        ← First substantive section
[Pre-Chorus]     ← Optional, before chorus
[Chorus]         ← First appearance
[Verse 2]        ← Second verse
[Pre-Chorus]     ← Optional repeat
[Chorus]         ← Repeat
[Bridge]         ← After second chorus — NOT before
[Chorus]         ← Final chorus (optional)
[Outro]          ← Last section
```

---

## Sources

*(To be populated from research)*
