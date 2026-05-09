# Genre: Blues

> **Status:** Verified
> **Last updated:** 2026-05-09
> **Suno version scope:** v5, v5.5

---

## Overview

Blues is the foundational American genre from which rock, jazz, R&B, and soul all descend. It centers on the 12-bar chord progression, blue notes (flattened 3rd, 5th, 7th), call-and-response phrasing, and deeply expressive vocals. BPM range: 60–120 depending on subgenre. Principal subgenres:

- **Delta Blues** — raw, spare; acoustic slide guitar, upright bass or stomped beat, one or two instruments; 60–80 BPM
- **Chicago Blues** — urban electric; electric guitar and harmonica over a rhythm section (bass, drums, piano optional); 80–100 BPM
- **Texas Blues** — cleaner electric tone, more rock-adjacent, flashy guitar leads; 90–120 BPM
- **Electric Blues / Blues Rock** — heavier distortion, rock drum feel; 95–120 BPM

Suno v5 tends to sanitize blues: it produces melodically smooth output with clean guitar tones and polished production rather than the grit, bent notes, and expressive rawness that define authentic blues. The primary prompting challenge is forcing Suno toward "dirty" rather than "clean" tonal territory.

**Sonic fingerprint:**
- Electric guitar with mild to heavy grit (overdrive, not full distortion unless blues-rock)
- Slide guitar or bending notes (Delta: acoustic slide; Chicago: electric slide or fretted bends)
- Harmonica (blues harp) — notably effective when named explicitly
- Upright bass or electric bass walking a 12-bar pattern
- Drums: loose, shuffled, laid-back feel — not tight or quantized
- Vocals: gritty, expressive, emotionally raw, call-and-response tendency

---

## Style Block Recommendations

### Core Tags

Delta Blues (acoustic, raw):
```
Delta blues, acoustic slide guitar, open tuning, gritty male vocals, spare arrangement, upright bass, stomped percussion, raw recording, 70 BPM
```

Chicago Blues (electric, band):
```
Chicago blues, electric guitar, blues harmonica, walking bass, shuffled drums, soulful male vocals, bar-band feel, urban blues, 90 BPM
```

Texas Blues (clean electric, expressive):
```
Texas blues, clean electric guitar, SRV style, expressive guitar leads, Hammond organ, shuffled groove, soulful vocals, 105 BPM
```

Blues Rock (heavier, rock-adjacent):
```
blues rock, overdriven electric guitar, blues harmonica, powerful male vocals, driving drums, heavy bottom end, Allman Brothers feel, 110 BPM
```

### Effective Modifiers

- `"12-bar blues"` — explicitly signals the chord structure; Suno v5 responds to this and produces more authentic harmonic movement
- `"blues harmonica"` / `"harmonica"` — naming the instrument explicitly produces harmonica; without it, Suno often omits it even for blues prompts
- `"slide guitar"` — triggers the characteristic bottleneck/slide tone; add `"acoustic"` or `"electric"` to specify
- `"gritty"` — the most reliable single modifier for moving Suno away from clean/polished output
- `"overdriven electric guitar"` — targets tube-amp overdrive tone without full metal distortion
- `"shuffled groove"` / `"shuffle rhythm"` — signals the characteristic swing-eighth rhythmic feel of Chicago blues
- `"call-and-response"` — prompts Suno toward alternating vocal/instrument phrasing
- `"raw recording"` / `"lo-fi"` — discourages polished production; adds tape-era texture
- `"SRV style"` / `"Muddy Waters style"` — artist references work in v5 and anchor the era and tone
- `"amp reverb"` / `"room sound"` — adds live-performance ambience
- `"walking bass"` — specifies the characteristic bass pattern
- `"bent notes"` — signals expressive pitch bending in guitar lines
- `"no autotune"` — critical for preserving the raw, imperfect vocal character

### Tags to Avoid

- `"smooth"` — the enemy of authentic blues; suppresses grit and produces R&B-adjacent clean output
- `"pop"` — overrides blues structure toward verse-chorus pop forms; eliminates 12-bar feel
- `"clean guitar"` alone — blues requires some grit; clean guitar pushes toward jazz or folk territory
- `"synth"` / `"electronic"` — incompatible with acoustic/analog blues identity unless targeting blues-electronic fusion deliberately
- `"fast"` alone without BPM — Suno may jump to 140+ BPM, which erases the blues feel
- Over-stacking mood descriptors (10+ emotion words) — produces a blended, indistinct output; 4–6 mood/texture descriptors is the effective ceiling

---

## Lyric Structure Recommendations

### Typical Structure

Standard 12-bar blues (three verses, traditional AAB form):
```
[Intro - guitar, 12-bar turnaround]
[Verse 1]
[Verse 2]
[Guitar Solo]
[Verse 3]
[Outro - guitar fade]
```

Modern blues with chorus (hybrid structure, more radio-friendly):
```
[Intro]
[Verse 1]
[Chorus]
[Verse 2]
[Chorus]
[Guitar Solo]
[Verse 3]
[Chorus]
[Outro]
```

### Genre-Specific Metatags

- `[Intro - 12-bar turnaround]` — primes Suno's guitar for the blues entry riff
- `[Verse]` — in traditional blues, each verse often uses AAB lyric form (two identical or near-identical lines followed by a punchline line)
- `[Guitar Solo]` — reliable in v5; explicitly triggers a guitar break; add `[Guitar Solo - slide guitar]` or `[Guitar Solo - electric]` for specificity
- `[Harmonica Solo]` — works in v5; place after a verse or between sections; Suno must have harmonica in the style block for this to work
- `[Chorus]` — use for hybrid structures; traditional 12-bar blues does not have a chorus — omit if going for authentic structure
- `[Outro - fade]` / `[Outro - guitar]` — signals a trailing-off close; classic blues tracks often fade out on a guitar riff

### Line Length & Rhyme Scheme

- **AAB lyric form (traditional):** Line A is sung, repeated (or slightly varied), then Line B provides the punchline/resolution. Each set of three lines covers 4 bars of the 12-bar progression.
  ```
  Example:
  Woke up this morning, nothing left to find (A)
  Said I woke up this morning, nothing left to find (A, repeated)
  Packed my bag and left my troubles behind (B)
  ```
- **Syllable count:** 8–14 syllables per line; the triple-time feel of shuffled blues accommodates longer lines naturally
- **Rhyme scheme:** AAB per verse in traditional blues; AABB or ABAB in modern hybrid structures
- **Content:** Blues lyrics are concrete and personal — name the pain directly. Abstraction weakens the genre's emotional contract. Specific objects, places, and actions ("left my boots by the riverside," "third shot of rye") outperform vague grief.

---

## Slider Settings

| Slider | Recommended Value (0–100) | Rationale |
|--------|--------------------------|-----------|
| Weirdness | 20–35 | Blues tolerates some expressive roughness and improvisation (higher than folk), but the 12-bar form and pentatonic palette are conventions Suno must stay inside. Keep moderate to preserve structure while allowing expressive variation. |
| Style Influence | 60–75 | Moderate-high adherence locks in the instrument palette and shuffled groove. Dropping below 55 risks the clean-pop drift that is the genre's main pitfall. |
| Audio Influence | 65–75 | Only relevant with reference audio. A close-mic live blues recording (single guitar and vocal, or small band) transfers timbral character well. Avoid polished studio references. |

---

## Known Quirks & Pitfalls

- **Issue:** Guitar tone is clean and shiny instead of gritty or overdriven — sounds like jazz or pop guitar rather than blues. → **Fix:** Add `"overdriven electric guitar"`, `"gritty"`, `"amp overdrive"`, or `"tube amp"` to the style block. Name the guitar tone explicitly: `"warm overdriven Strat"` or `"dirty Telecaster"`. Reference artists work: `"SRV style"`, `"Muddy Waters style"`.

- **Issue:** Harmonica does not appear in the output despite being part of the blues feel requested. → **Fix:** Name `"blues harmonica"` or `"harmonica"` explicitly in the style block — Suno does not infer it from `"Chicago blues"` alone. If you want a harmonica solo, add a `[Harmonica Solo]` metatag at the desired position in the lyrics field; Suno v5 treats this as an instruction.

- **Issue:** Suno produces a pop-blues track with a standard verse-chorus-verse structure instead of 12-bar feel. → **Fix:** Add `"12-bar blues"` to the style block as an explicit structural cue. In the lyrics, write verses in AAB form and omit `[Pre-Chorus]` and `[Build]` tags — these signal pop structure. Keeping the lyric structure traditional reinforces the sonic structure.

- **Issue:** Vocals are smooth and melodically safe — no bends, growls, or raw expression. → **Fix:** Use `"raw vocals"`, `"gritty vocals"`, `"gravelly male voice"`, `"no autotune"`. Add `"expressive"` and avoid `"smooth"` entirely. For Delta-style rawness, combine `"raw recording"` with `"lo-fi"` to signal a low-budget, unprocessed vocal treatment.

- **Issue:** Drums are tight and quantized — sounds like modern pop/R&B rather than a loose, human blues feel. → **Fix:** Add `"shuffled groove"`, `"loose drums"`, `"laid-back feel"`, or `"live drummer"`. The shuffle is the defining rhythmic feel of Chicago blues; naming it explicitly is the most reliable fix. Avoid `"tight drums"` or `"punchy kick"`.

### v5.5 Audit Notes

> Audited 2026-05-09. No breaking changes confirmed.

- 12-bar blues structural prompt still the most reliable structural signal in v5.5
- Harmonica forcing technique (name explicitly in style block) unchanged
- AAB lyric form still the most natural fit for blues verses
- Gritty tone is still essential — "smooth" remains the enemy; v5.5's prompt accuracy improvement means "gritty", "raw" tags are more faithfully respected
- v5.5 instrument separation improvement benefits blues: guitar and harmonica are more distinctly separated in the mix
- All slider recommendations remain valid

---

## Example Prompt

### Example 1: Chicago electric blues

**Style block:**
```
Chicago blues, electric guitar, blues harmonica, walking bass, shuffled groove, gritty male vocals, bar-band feel, overdriven amp, no autotune, 92 BPM
```

**Lyrics skeleton:**
```
[Intro - electric guitar, 12-bar turnaround, 8 bars]

[Verse 1]
Left my woman standing in the driving rain (A)
Said I left my woman standing in the driving rain (A)
Now I'm sleeping on a southbound midnight train (B)

[Verse 2]
Borrowed money from a man I should've never known (A)
Said I borrowed money from a man I should've never known (A)
Now that man is somewhere calling me his own (B)

[Harmonica Solo]

[Verse 3]
Chicago wind cuts right down to the bone (A)
Said that Chicago wind cuts right down to the bone (A)
A man can be surrounded and still die alone (B)

[Guitar Solo - electric, overdriven]

[Verse 4]
Come tomorrow morning I'll get back on my feet (A)
Said come tomorrow morning I'll get back on my feet (A)
Till then the devil and the rain can have this street (B)

[Outro - guitar and harmonica, fade]
```

**Notes:** AAB lyric form in each verse reinforces the 12-bar structure. Placing `[Harmonica Solo]` before the guitar solo creates a two-break structure that feels like a full band arrangement. The `[Intro]` direction primes the electric guitar tone before the vocal enters.

### Example 2: Delta blues (acoustic, sparse)

**Style block:**
```
Delta blues, acoustic slide guitar, open G tuning, gritty baritone vocals, upright bass, sparse arrangement, raw recording, lo-fi, 68 BPM
```

**Lyrics skeleton:**
```
[Intro - single slide guitar, open-tuned, raw]

[Verse 1]
I got a crossroads feeling in my boots today (A)
I said I got a crossroads feeling in my boots today (A)
North or south I'm going either way (B)

[Verse 2]
Red clay road don't care whose feet it wears (A)
Said red clay road don't care whose feet it wears (A)
Walk it long enough and nobody stares (B)

[Guitar Solo - acoustic slide, open tuning]

[Verse 3]
Devil offered me a good deal at the line (A)
Said the devil offered me a good deal at the line (A)
Told him thanks but I've been buying back my time (B)

[Outro - slide guitar, single string, fade]
```

**Notes:** Delta blues works best with maximum restraint. `"sparse arrangement"` and omitting drum tags keeps Suno from adding a kit. The `"open G tuning"` detail signals slide guitar technique; Suno v5 responds to tuning specifics as tonal cues.

---

## Research Sources

- [How to Prompt Suno AI for a Blues Track That Actually Works — Tanmoy Das / Medium](https://medium.com/write-a-catalyst/how-to-prompt-suno-ai-for-a-blues-track-that-actually-works-e60516e89436) (2026-04-26)
- [Suno AI Prompts for Jazz & Blues Music — Travis Nicholson / Medium](https://travisnicholson.medium.com/suno-ai-prompts-for-jazz-blues-music-bf8725575943) (2026-04-26)
- [Suno AI Prompt Guide (A–C) — Jack Righteous](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/bookmark-this-suno-ai-a-z-prompts-guide-a-to-c) (2026-04-26)
- [Suno Style Tags List: 300+ Tested Tags — HookGenius](https://hookgenius.app/learn/suno-style-tags-guide/) (2026-04-26)
- [AI Music Prompt: Tested List of Suno AI Guitar Style Artist-Inspired Prompts 2025 — Vocal.media](https://vocal.media/art/ai-music-prompt-tested-list-of-suno-ai-guitar-style-artist-inspired-prompts-2025) (2026-04-26)
- [Suno v5 Prompting Best Practices Guide — Scribd](https://www.scribd.com/document/933827832/Suno-v5-and-best-prompt-tips-of-Suno-v5) (2026-04-26)
- [Suno AI Prompt Guide: Limits, Tips & 20+ Examples — MusicSmith](https://musicsmith.ai/blog/ai-music-generation-prompts-best-practices) (2026-04-26)
