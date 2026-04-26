# Genre: Jazz

> **Status:** Verified
> **Last updated:** 2026-04-26
> **Suno version scope:** v5

---

## Overview

Jazz is an improvisation-forward genre with deep subgenre variation — bebop, swing, cool jazz, modal jazz, Latin jazz, smooth jazz, and fusion each require distinct prompt strategies. BPM ranges widely: ballads at 50–70, cool/modal at 80–120, swing standards at 120–160, bebop at 160–200+. Core instrumentation is piano, double bass, acoustic drums (brushed or sticks), and horns (trumpet, saxophone, trombone), often with guitar or vibraphone depending on the subgenre.

Suno v5 handles jazz better than earlier versions but defaults to "lounge jazz" when left underspecified. Swing feel, BPM, and subgenre must all be named explicitly to avoid generic smooth-jazz output. The `[Solo]` metatag is uniquely valuable here for triggering improvisation-style instrumental passages.

**Sonic fingerprint:**
- Swing or straight-eighth feel (must be specified — Suno defaults to straight-eighth pop feel)
- Walking bass line on upright/double bass
- Ride cymbal or brushed snare establishing the pulse
- Piano comping (voicings that support but don't overpower)
- Lead horn or piano carrying the melodic line
- 32- or 12-bar forms implied by chord changes (less reliable in Suno — use metatags to signal structure)
- Improvised passages between vocal sections are genre-defining

---

## Style Block Recommendations

### Core Tags

Choose one subgenre anchor first, then layer modifiers:

**Bebop:**
```
bebop jazz, fast tempo, 180 BPM, complex chord changes, saxophone lead, walking bass, ride cymbal, 1940s New York, Charlie Parker style, swing feel
```

**Swing/Big Band:**
```
swing jazz, big band, 130 BPM, brass section, piano, walking bass, swing feel, 1940s ballroom, Benny Goodman style, uplifting
```

**Cool Jazz:**
```
cool jazz, 100 BPM, muted trumpet, piano trio, brushed drums, restrained dynamics, Miles Davis Kind of Blue style, modal, introspective
```

**Smooth Jazz:**
```
smooth jazz, 95 BPM, electric piano, soprano saxophone, mellow, easy listening, polished production, contemporary, Kenny G style
```

**Bossa Nova:**
```
bossa nova, nylon string guitar, soft percussion, double bass, 110 BPM, Brazilian, João Gilberto style, gentle swing, intimate
```

### Effective Modifiers
- `"swing feel"` — critical for authentic jazz rhythmic pocket; without it, output sounds stiff
- `"walking bass"` — anchors the upright bass to its genre-correct role
- `"brushed drums"` — gives small-group ballad/cool feel; use `"ride cymbal"` for uptempo bebop
- `"jazz piano comping"` — keeps piano in a supportive rather than dominant role
- `"muted trumpet"` — signals Harmon mute, the cool-jazz signature sound
- `"saxophone lead"` — front the horn rather than piano; combine with subgenre for best results
- `"jazz guitar"` — invokes clean, single-coil archtop tone rather than rock guitar
- `"call and response"` — useful in big band contexts, cues brass-section interplay

### Tags to Avoid
- `"jazz"` alone — produces generic lounge output with no swing, wrong BPM, and often pop-style vocals
- `"electric guitar"` — routes to rock/blues production; use `"jazz guitar"` or `"archtop guitar"` instead
- `"synthesizer"` or `"electronic"` — dilutes acoustic character unless targeting fusion specifically
- `"EDM"`, `"trap"`, `"hip-hop"` — obvious rhythmic conflicts
- `"chill"` without further qualification — often merges with lo-fi and loses the harmonic complexity
- Multiple conflicting subgenres (e.g., `"bebop"` + `"smooth jazz"`) — Suno averages them to mud

---

## Lyric Structure Recommendations

### Typical Structure

Jazz vocals follow the AABA 32-bar standard form, or blues 12-bar form. For Suno v5, map these to metatags:

**Standard AABA vocal form:**
```
[Intro]
(4–8 bars instrumental — let Suno establish the feel)

[Verse 1]
(A section — 8 bars, introduce the theme)

[Verse 2]
(A section repeat — 8 bars, slight variation)

[Bridge]
(B section — 8 bars, harmonic contrast, emotional peak)

[Verse 3]
(A section return — 8 bars, resolution)

[Solo]
(instrumental improvisation — 16–32 bars; label this explicitly)

[Verse 4]
(optional final A section — outro feel)

[Outro]
(fade or tag ending)
```

**For instrumental jazz (no vocals):**
```
[Intro]
[Theme]
[Solo]
[Solo]
[Theme]
[Outro]
```

### Genre-Specific Metatags
- `[Solo]` — most important jazz-specific metatag; triggers an instrumental improvisation passage. Place after the second chorus or as a standalone section. Works reliably in v5.
- `[Intro]` — essential; sets the BPM feel and instrumentation before vocals enter. Keep it 2–4 lines or leave empty.
- `[Bridge]` — maps well to the B section of AABA form; use for harmonic contrast
- `[Outro]` — jazz songs often end on a "tag" (the last 4 bars repeated and ritardando); describe this in a comment line inside the section
- `[Instrumental]` — use for extended non-vocal passages if `[Solo]` doesn't trigger the right instrument
- Avoid `[Drop]` and `[Build]` — these are EDM concepts and confuse the model in jazz contexts

### Line Length & Rhyme Scheme
- 8–10 syllables per line is comfortable for swing delivery
- AABA rhyme scheme mirrors the musical form (A rhymes across sections 1, 2, 4; B section has its own rhyme)
- Blues 12-bar: AAB couplet form (first line stated, repeated with variation, third line resolves)
- Avoid forced rhymes — jazz lyrics prize natural speech rhythm over strict end-rhyme
- Scat syllables ("do-be-do", "sha-bop") can be placed in `[Solo]` or `[Outro]` sections; Suno v5 will sometimes render them as vocal flourishes

---

## Slider Settings

| Slider | Recommended Value (0–100) | Rationale |
|--------|--------------------------|-----------|
| Weirdness | 25–40 | Jazz needs harmonic sophistication, not randomness. Low Weirdness preserves the idiomatic chord vocabulary and rhythmic feel. Go higher (50+) only for free jazz or avant-garde. |
| Style Influence | 55–70 | Moderate-to-strong genre loyalty. Higher values (70+) for bebop/traditional where period authenticity matters; lower (50–55) for fusion where genre blending is intentional. |
| Audio Influence | 65–80 | Only if uploading a reference track. Jazz timbres (room acoustics, microphone warmth) benefit from a strong reference. |

---

## Known Quirks & Pitfalls

- **Issue:** Output sounds like generic lounge/elevator music despite jazz tags → **Fix:** Add a specific subgenre (`bebop`, `cool jazz`, `swing`) plus era (`1950s`, `1940s`, `contemporary`) and an artist reference (`Miles Davis style`, `Bill Evans style`). The three together dramatically increase specificity. Never use `"jazz"` alone.

- **Issue:** Swing feel is absent — rhythm sounds stiff and straight → **Fix:** Add `"swing feel"` explicitly to the style block. Suno v5 defaults to straight-eighth timing for pop. `"swing feel"` plus `"ride cymbal"` is the most reliable combination for uptempo jazz; `"swing feel"` plus `"brushed drums"` for ballads.

- **Issue:** Vocals default to pop style — vibrato-heavy, breathless, not jazz phrasing → **Fix:** Add `"jazz vocals"` or `"crooner"` (male) / `"jazz chanteuse"` (female) to the style block. For scat or wordless sections, place `[Solo]` and note `"vocal scat"` in the lyrics field for that section.

- **Issue:** `[Solo]` tag triggers a very short or non-existent instrumental break → **Fix:** Place `[Solo]` on its own line with a parenthetical note like `(saxophone improvisation, 16 bars)`. This gives Suno a duration cue. Also ensure the style block names the lead instrument so Suno knows which voice to solo.

- **Issue:** Piano dominates and buries the horn/vocal → **Fix:** Add `"jazz piano comping"` instead of `"piano"`. The word "comping" signals a supportive, behind-the-beat role. Also add the lead instrument explicitly: `"saxophone lead"` or `"trumpet lead"`.

- **Issue:** Walking bass is absent — bass sounds pop-mixed → **Fix:** Add `"walking bass"` and `"upright bass"` or `"double bass"` to style block. Without these, Suno uses a plucked electric bass pattern more suited to pop/R&B.

---

## Example Prompt

### Example 1: Bebop vocal track

**Style block:**
```
bebop jazz, 165 BPM, swing feel, saxophone lead, walking bass, ride cymbal, piano comping, 1950s New York, Charlie Parker style, upright bass, warm room acoustics
```

**Lyrics skeleton:**
```
[Intro]
(uptempo bebop theme, saxophone and piano)

[Verse 1]
The city wakes at half past three
The neon signs still calling me
I find my table, order rye
And watch the smoke curl toward the sky

[Verse 2]
The quartet locks on bar thirteen
The changes blur like things unseen
The saxophonist bends the note
And every word gets caught in my throat

[Bridge]
There's something in a flattened fifth
That makes the ordinary lift
And for a moment we are free
From everything that used to be

[Verse 3]
They call last set, the lights come low
But nobody is moving to go
A minor chord, a major dream
Nothing is quite what it would seem

[Solo]
(saxophone improvisation, 16 bars, bebop vocabulary)

[Outro]
One final phrase, the cymbal fades
The bass walks off through darker shades
```

**Notes:** The `[Solo]` section should be left lyrically sparse — just the parenthetical. Suno v5 will fill it with an instrumental passage. Adding `"bebop vocabulary"` in the parenthetical sometimes steers the phrasing. Keep the style block under 200 characters for fastest rendering; the full 1,000-char limit is available but shorter blocks often parse more reliably.

---

### Example 2: Cool jazz instrumental

**Style block:**
```
cool jazz, 95 BPM, muted trumpet, piano trio, brushed drums, double bass, modal, introspective, Miles Davis Kind of Blue style, 1959, soft dynamics
```

**Lyrics skeleton (instrumental structure):**
```
[Intro]
(piano establishes modal vamp)

[Theme]
(muted trumpet plays the head, 16 bars)

[Solo]
(piano solo, modal improvisation, 24 bars)

[Solo]
(trumpet solo, lyrical, sparse, 16 bars)

[Theme]
(return to head, quieter)

[Outro]
(bass and piano duo, fade)
```

**Notes:** Fully instrumental. No lyric content needed — use parenthetical structural notes inside each section tag. The double `[Solo]` is intentional; Suno v5 will attempt to render two distinct instrument solos when the style block names two lead instruments. Watch that the piano doesn't overpower; `"brushed drums"` and `"soft dynamics"` are load-bearing style tags.

---

## Research Sources

- [Suno AI Prompts for Jazz & Blues Music — Travis Nicholson, Medium](https://travisnicholson.medium.com/suno-ai-prompts-for-jazz-blues-music-bf8725575943) (2026-04-26)
- [Suno Jazz Prompts — HookGenius](https://hookgenius.app/learn/suno-jazz-prompts/) (2026-04-26)
- [Jazz Music Genre: The Definitive Guide for AI Music Creation — SunoPrompt.com](https://sunoprompt.com/music-style-genre/jazz-music-genre) (2026-04-26)
- [What Is Jazz Music? History, Sound, Variations & Suno AI Guide — Jack Righteous](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/what-is-jazz-music-history-sound-variations-suno-ai) (2026-04-26)
- [AI Jazz Improvisation: Current Limitations and What's Next in 2026 — Soundverse.ai](https://www.soundverse.ai/blog/article/ai-jazz-improvisation-current-limitations-1048) (2026-04-26)
- [Suno V5.5 Reference: Meta Tags, Style-of-Music — Blake Crosley](https://blakecrosley.com/guides/suno) (2026-04-26)
- [Suno Style Tag Research — HookGenius](https://hookgenius.app/learn/suno-style-tag-research/) (2026-04-26)
