# Genre: Reggae / Dancehall

> **Status:** Verified
> **Last updated:** 2026-04-26
> **Suno version scope:** v5

---

## Overview

Reggae and its offshoots are Jamaican-origin genres whose defining rhythmic feature is the offbeat "skank" — guitar or piano chords landing on beats 2 and 4 (or the "and" of each beat in one-drop variants). Heavy, melodic bass dominates the low end. The drum pattern is laid-back and swinging, with the bass and kick drum locking together.

**Subgenres:**
- **Roots Reggae** — spiritual, Rastafarian themes; organic instruments; slow-medium BPM 65–85; artists: Bob Marley, Burning Spear, Culture
- **Reggae Rock** — electric guitar, rock energy, melodic hooks; BPM 80–100
- **Dub** — instrumental, heavy reverb and delay on all elements, bass-forward, echo chamber effects; BPM 65–85
- **Dancehall** — faster BPM 90–110; digital riddim (drum machine or programmed beats); toasting/deejay vocals, or melodic sung vocals; Jamaican patois influences
- **Lovers Rock** — smooth, romantic reggae; BPM 70–85; soft production, melodic focus

The main prompting challenge: Suno v5 understands "reggae" as a genre label but frequently defaults to the on-beat rhythmic placement (like rock or pop), missing the characteristic offbeat skank. Explicit instruction on the rhythmic feel is the most critical fix.

**Sonic fingerprint:**
- Offbeat guitar or piano skank (staccato chords on the upbeat)
- Deep, melodic bass — prominent, carrying melodic lines
- Drum pattern: one-drop (bass drum on beat 3 only) or rockers (kicks on 2 and 4); snare is minimal or replaced by rimshot
- Vocals: melodic, laid-back phrasing; Roots uses full legato; Dancehall uses rapid-fire toasting or melodic patois phrasing
- Horns section (optional): trumpet, trombone, saxophone for Roots and Rocksteady influence
- Dub: heavy spring reverb, tape echo, all elements drenched in effects

---

## Style Block Recommendations

### Core Tags

Roots Reggae:
```
roots reggae, offbeat guitar skank, deep melodic bass, one-drop drums, soulful male vocals, Rastafarian, organic instruments, warm mix, 75 BPM
```

Dub:
```
dub reggae, heavy bass, spring reverb, tape echo, one-drop drums, offbeat piano skank, instrumental, deep dub mix, 72 BPM
```

Dancehall:
```
dancehall, digital riddim, offbeat piano skank, deep bass, toasting vocals, Jamaican patois, energetic, programmed drums, 100 BPM
```

Reggae Rock:
```
reggae rock, electric guitar skank, melodic bass, driving drums, upbeat, melodic male vocals, sunny, 95 BPM
```

Lovers Rock:
```
lovers rock, smooth reggae, offbeat guitar, melodic bass, romantic, warm female vocals, soft horns, 80 BPM
```

### Effective Modifiers

- `"offbeat guitar skank"` — the single most critical tag; directly signals the characteristic upbeat chord placement; without this, Suno often defaults to on-beat strumming
- `"piano skank"` — alternative to guitar skank; effective for Dancehall and some Roots styles
- `"staccato chords"` — reinforces the choked, punchy nature of the skank
- `"one-drop drums"` — specifies the drum pattern (kick on beat 3 only, snare/rimshot on 2 and 4); the most authentic Roots drum feel
- `"deep melodic bass"` — reggae bass is not just rhythmic; it carries the groove melody
- `"sub-bass"` / `"heavy bottom end"` — for Dancehall and Dub where bass weight is paramount
- `"spring reverb"` / `"tape echo"` — essential Dub production cues
- `"horn section"` / `"brass"` — triggers trumpet/trombone/sax; appropriate for Roots and Rocksteady
- `"toasting vocals"` / `"deejay style"` — Dancehall vocal delivery; rapid-fire rhythmic phrasing
- `"Rastafarian"` / `"Jah"` — thematic cues that reinforce Roots Reggae authenticity
- `"digital riddim"` — signals programmed drum machine feel for Dancehall
- `"laid-back"` / `"irie"` — reinforces the relaxed groove feel for Roots
- `"no reverb"` / `"dry"` — only for Dancehall; Dub is the opposite

### Tags to Avoid

- `"rock"` alone without reggae anchors — Suno interprets as rock music, loses the offbeat skank entirely
- `"pop"` — overrides the rhythmic feel toward on-beat pop production
- `"on-beat guitar"` — explicitly contradicts the genre's defining feature
- `"tight drums"` / `"quantized"` — Roots and Dub need a loose, human feel; Dancehall may accept programmed but not "tight"
- `"smooth"` for anything other than Lovers Rock — suppresses the rhythmic grit
- `"synth lead"` for Roots — inappropriate; use for Dancehall only when electronic palette is intended
- `"acoustic guitar"` without skank direction — may produce folk-guitar strumming rather than the punchy reggae chop

---

## Lyric Structure Recommendations

### Typical Structure

Standard Roots Reggae:
```
[Intro - bass and drums, instrumental]
[Verse 1]
[Chorus]
[Verse 2]
[Chorus]
[Bridge]
[Chorus]
[Outro - dub fade]
```

Dancehall (verse-hook driven):
```
[Intro - riddim, 4 bars]
[Verse 1]
[Hook]
[Verse 2]
[Hook]
[Verse 3]
[Hook]
[Outro]
```

Dub (instrumental with vocal fragments):
```
[Intro - bass and reverb, atmospheric]
[Verse 1 - sparse, echoed]
[Dub Break - instrumental, reverb heavy]
[Verse 2 - fragments]
[Outro - echo fade]
```

### Genre-Specific Metatags

- `[Intro - bass and drums]` — establishes the riddim before vocals; highly effective for grounding the rhythmic feel
- `[Verse]` — standard; Roots verses carry spiritual or narrative weight; Dancehall verses are dense with syllables
- `[Chorus]` — Roots choruses are often a call-and-response hook or a Jah/praise refrain
- `[Hook]` — preferred over `[Chorus]` for Dancehall; shorter, more repetitive, often a single memorable phrase
- `[Bridge]` — works in v5; use for a dub-style section with reduced vocals: `[Bridge - dub break, echo]`
- `[Outro - dub fade]` — signals a reverb/echo trail-off; very appropriate for Roots and Dub
- `[Dub Break]` — custom tag Suno v5 may partially interpret as an instrumental breakdown; pair with style cues in the lyrics text: `[Dub Break - bass and reverb, no vocals]`
- Avoid `[Build]` / `[Drop]` — these signal EDM/dance structure, which conflicts with reggae's groove-based flow

### Line Length & Rhyme Scheme

- **Roots Reggae:** 8–12 syllables per line; AABB or ABAB rhyme; lyrical content: peace, love, Jah, oppression, Africa, nature; vocabulary should be simple and resonant
- **Dancehall:** Rapid syllable density (12–16+ syllables per line acceptable); near-rhyme and assonance work; Jamaican patois vocabulary adds authenticity (`"riddim"`, `"inna"`, `"fi"`, `"nuh"`)
- **Lovers Rock:** 8–10 syllables; smooth ABAB; romantic imagery; avoid conflict-heavy themes
- **Rhythm tip:** Reggae lyrics often break from the beat in unexpected ways — the "late" delivery (slightly behind the beat) is stylistic. Write slightly longer lines than you think you need; Suno will naturally delay the resolution.

---

## Slider Settings

| Slider | Recommended Value (0–100) | Rationale |
|--------|--------------------------|-----------|
| Weirdness | 25–40 | Reggae tolerates rhythmic experimentation and dub-style treatment (Dub sits at the higher end). Roots should stay 25–30 to preserve the genre conventions; Dub can push to 40 for echo-chamber chaos. |
| Style Influence | 65–80 | Critical to keep high — the offbeat rhythmic feel requires strong style adherence. At lower values Suno drifts toward on-beat rock or pop rhythm quickly. |
| Audio Influence | 60–75 | Only relevant when uploading reference audio. A lo-fi or well-recorded analog reggae track transfers groove feel well. Avoid over-compressed modern references. |

---

## Known Quirks & Pitfalls

- **Issue:** The characteristic offbeat guitar skank is absent — guitar strums on the beat like rock or pop, losing the reggae feel entirely. → **Fix:** This is the genre's most common Suno failure. Add `"offbeat guitar skank"` or `"piano skank"` to the style block explicitly. Follow with `"staccato chords"` for reinforcement. The skank must be named; Suno does not infer it from `"reggae"` alone with sufficient reliability in v5.

- **Issue:** Bass is too quiet or thin — the characteristic reggae bass dominance is absent, and mid-range instruments dominate. → **Fix:** Add `"deep melodic bass"`, `"bass-forward mix"`, or `"heavy bottom end"` to the style block. Name the bass explicitly as a "hero instrument" — one of your 2–3 featured instruments. For Dub specifically, leading with `"dub reggae, heavy bass"` before all other descriptors prioritizes the low end.

- **Issue:** Drum pattern sounds like rock or pop — kick on 1 and 3, snare on 2 and 4, no reggae feel. → **Fix:** Use `"one-drop drums"` for Roots (kick only on beat 3, which is the defining Roots pattern). Use `"rockers drums"` for a more driving reggae beat. Avoid `"rock drums"` or `"pop drums"`. For Dancehall, `"digital riddim"` signals programmed patterns. `"laid-back drums"` helps shift the feel.

- **Issue:** Suno produces generic pop music with Jamaican-accented vocals but no rhythmic reggae feel. → **Fix:** Reggae identity lives in the rhythm section, not the vocals. Stack `"offbeat guitar skank"` + `"one-drop drums"` + `"deep melodic bass"` as the priority triplet. Vocal style alone (even with patois cues) is insufficient to generate authentic rhythm. The style block needs the rhythmic instruction first.

- **Issue:** Dub requests produce a normal reggae track without echo, reverb, and the deconstructed dub aesthetic. → **Fix:** Use `"dub reggae"` not just `"dub"` (which is ambiguous with EDM dub/dubstep). Add `"spring reverb"`, `"tape echo"`, `"echo chamber"`, `"reverb-drenched"`. Include `"instrumental"` if vocals are not desired. The `[Bridge - dub break, echo]` metatag helps trigger the instrumental section.

---

## Example Prompt

### Example 1: Roots Reggae (spiritual, classic feel)

**Style block:**
```
roots reggae, offbeat guitar skank, deep melodic bass, one-drop drums, soulful male vocals, Rastafarian, warm organic mix, horn section, 74 BPM
```

**Lyrics skeleton:**
```
[Intro - bass and drums, 8 bars, no vocals]

[Verse 1]
Rise up in the morning with the light of Jah
Walk the dusty roads that stretch out wide and far
Every stone beneath your feet a chapter in the book
Every river that you cross is more than how it looks

[Chorus]
One love, one heart, one rhythm in the soul
The bass line is the river and the drum makes us whole
Rise up, rise up, let the morning in
One love, one heart, where the rivers begin

[Verse 2]
They built the walls up high to keep the people down
But roots grow deep beneath the coldest ground
No chain was ever forged that roots could not outlast
The present is the future and the future is the past

[Chorus]
One love, one heart, one rhythm in the soul
The bass line is the river and the drum makes us whole
Rise up, rise up, let the morning in
One love, one heart, where the rivers begin

[Bridge - horn section, dub fade, sparse]
Forward ever, backward never, Jah provide
Walk the righteous road with fire on your side

[Chorus]
One love, one heart, one rhythm in the soul
The bass line is the river and the drum makes us whole
Rise up, rise up, let the morning in
One love, one heart, where the rivers begin

[Outro - bass and guitar skank, echo fade]
```

**Notes:** The `[Intro]` direction establishes the rhythm section before the vocal enters — this is essential for Suno to lock in the offbeat feel. The `[Bridge]` direction (`horn section, dub fade, sparse`) calls on the horns already listed in the style block. The `[Outro]` echo cue triggers a natural Roots Reggae trail-off.

### Example 2: Dancehall (energetic, modern)

**Style block:**
```
dancehall, digital riddim, offbeat piano skank, heavy bass, sub-bass, toasting vocals, energetic, programmed drums, Jamaican patois, 102 BPM
```

**Lyrics skeleton:**
```
[Intro - riddim, 4 bars]

[Verse 1]
Step inna di dance when di riddim drop
Every gyal and every man just nuh stop
From di east side to di west, everybody lock
When di bass line hit you feel it to di top

[Hook]
Feel di riddim, feel di bass
Every dancer find your place
Dancehall vibe, no time to waste
Feel di riddim, feel di bass

[Verse 2]
DJ spin the tune and the crowd go wild
From di veteran pon di floor to the ragamuffin child
Every speaker in di dance pushing like a mile
Dancehall culture, original style

[Hook]
Feel di riddim, feel di bass
Every dancer find your place
Dancehall vibe, no time to waste
Feel di riddim, feel di bass

[Verse 3]
Nuh badda try to slow the flow when di dance is live
Inna di dancehall is how we survive
Bass line heavy, drum is tight
Dancehall music carry us through the night

[Hook]
Feel di riddim, feel di bass
Every dancer find your place
Dancehall vibe, no time to waste
Feel di riddim, feel di bass

[Outro - riddim, fade]
```

**Notes:** Dancehall lyrics lean into patois vocabulary to prime the vocal delivery style. `[Hook]` rather than `[Chorus]` signals the shorter, more repetitive Dancehall structure. At 102 BPM and with `"toasting vocals"`, Suno should produce a rhythmically dense, rapid-fire vocal delivery. If Suno sings smoothly instead of toasting, regenerate with `"deejay style"` added to the style block.

---

## Research Sources

- [Suno AI Reggae Prompts — Roots, Dancehall & Dub — HookGenius](https://hookgenius.app/learn/suno-reggae-prompts/) (2026-04-26)
- [Top Music Genres 2025: Create Reggae with Suno AI — Jack Righteous](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/top-music-genres-2025-create-reggae-suno) (2026-04-26)
- [Reggae Music for AI Creation: The Ultimate Guide & 80+ Prompts — SunoPrompt.com](https://sunoprompt.com/music-style-genre/reggae-music-genre) (2026-04-26)
- [Suno v5 Guide: Everything New + Best Prompts — HookGenius](https://hookgenius.app/learn/suno-v5-complete-guide/) (2026-04-26)
- [Suno AI Prompt Guide: Limits, Tips & 20+ Examples — MusicSmith](https://musicsmith.ai/blog/ai-music-generation-prompts-best-practices) (2026-04-26)
- [Complete List of Suno AI Prompts & Styles That Actually Work — James 99 / Medium](https://medium.com/@kvxxpb/complete-list-of-suno-ai-prompts-styles-that-actually-work-2025-7674ada36eec) (2026-04-26)
- [Negative Prompting in Suno v5: Complete Guide — Jack Righteous](https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/negative-prompting-suno-v5-guide) (2026-04-26)
