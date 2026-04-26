# Genre: R&B / Soul

> **Status:** Draft
> **Last updated:** 2026-04-26
> **Suno version scope:** v5

---

## Overview

R&B and soul covers a wide stylistic range from classic Motown soul and 90s new jack swing to contemporary neo-soul (Erykah Badu, D'Angelo) and modern alternative R&B (SZA, Frank Ocean, FKA Twigs). BPM typically sits between 70–100 BPM, with a strong emphasis on groove, expressive vocal performance, and harmonic richness. The genre is defined by emotional delivery above all else.

Suno v5 handles R&B and soul well in broad strokes — it reliably produces smooth grooves, warm bass, and emotive vocals. The main risks are oversaturation (too much reverb, too many harmonic layers blurring the mix) and era ambiguity (Suno may default to a generic "radio R&B" sound without clear subgenre and era tags). Neo-soul specifically benefits from very explicit instrument and production tags to avoid sliding toward contemporary pop-R&B.

**Sonic fingerprint:**
- Warm, intimate vocal delivery — runs, ad-libs, and vibrato are expected
- Rhodes electric piano or warm acoustic piano as primary harmonic instrument
- Soft, brushed or programmed drums with a strong backbeat feel
- Warm sub-bass (bass guitar or synth bass) that locks with the kick
- Layered harmonies in the chorus and bridge (call-and-response is idiomatic)
- Production warmth: analog saturation, light vinyl texture, or live-room room reverb
- Chord extensions are characteristic: maj7, min9, dominant 9ths

---

## Style Block Recommendations

### Core Tags

Always lead with the specific subgenre — `"R&B"` alone produces workable but generic output:

**Neo-Soul:**
```
neo-soul, 78 BPM, soulful female vocals, Rhodes electric piano, warm sub bass, brushed drums, jazzy chords, layered harmonies, analog warmth, intimate, introspective
```

**Contemporary R&B (SZA / Frank Ocean register):**
```
contemporary R&B, 85 BPM, breathy female vocals, vocal runs, lush production, warm bass, synth pads, emotional, late-night vibe, polished mix
```

**90s New Jack Swing:**
```
new jack swing, 95 BPM, smooth male vocals, groovy beat, swing rhythm, 90s R&B, nostalgic, polished production, romantic, punchy drums
```

**Classic Soul:**
```
soul, 90 BPM, powerful female vocals, gospel influence, brass section, organ, warm bass guitar, emotional, raw, soulful, vintage production
```

### Effective Modifiers

- `"soulful vocals"` — the primary vocal character tag; reliably produces expressive delivery
- `"vocal runs"` — triggers melismatic embellishment (essential for soul/gospel-influenced R&B)
- `"ad-libs"` — generates background vocal layers and emotional exclamations
- `"call and response"` — triggers the signature back-and-forth vocal pattern between lead and backing vocals
- `"Rhodes electric piano"` — the defining neo-soul instrument; specify by name, not just `"electric piano"`
- `"warm analog production"` — biases toward vintage warmth; reduces digital sharpness
- `"jazzy chords"` — encourages extended harmonies (maj7, min9)
- `"brushed drums"` — lighter drum texture for slower, more intimate R&B
- `"silky smooth vocals"` — polished, controlled vocal character
- `"slow jam"` — explicitly marks lower-BPM romantic R&B register
- `"gospel influence"` — adds choir texture and emotional uplift to soul tracks

### Tags to Avoid

- `"rap"`, `"spoken word"` — exclude explicitly if not doing hip-hop R&B crossover; Suno may add spoken sections unprompted
- `"heavy distortion"`, `"metal"`, `"hard rock"` — obvious contamination
- `"ambient"` alone — suppresses the groove and rhythmic backbone R&B requires
- `"EDM"`, `"drop"`, `"build"` — push the model toward electronic dance structure, undoing the organic R&B feel
- `"lo-fi"` without qualification — reads as lo-fi hip-hop aesthetic rather than analog R&B warmth; use `"warm analog production"` or `"vintage soul production"` instead
- Stacking too many vocal descriptors (e.g., `"soulful, powerful, breathy, raspy, silky"`) — confuses the model; pick 2–3 that match the emotional register

---

## Lyric Structure Recommendations

### Typical Structure

R&B and soul use conventional verse-chorus structure but depend heavily on the pre-chorus as an emotional escalator:

```
[Intro]
(2–4 lines or instrumental; sets mood and key)

[Verse 1]
(6–8 lines — intimate storytelling; personal, vulnerable, specific)

[Pre-Chorus]
(2–4 lines — emotional tension rises; the "almost" moment before the release)

[Chorus]
(4–6 lines — the emotional release; hook phrase repeated; most intense vocal delivery)

[Verse 2]
(6–8 lines — deepening the story or shifting perspective)

[Pre-Chorus]

[Chorus]

[Bridge]
(4–8 lines — emotional peak or breakdown; often features key modulation feel,
ad-lib section, or call-and-response)

[Chorus]
(final repeat — often more embellished vocally; can label [Chorus x2])

[Outro]
(fade with vocal ad-libs, or definitive emotional close)
```

For slow jams and neo-soul, the structure can be more fluid — longer verses, shorter choruses, extended instrumental interludes:
```
[Intro]
[Verse 1]
[Chorus]
[Verse 2]
[Chorus]
[Instrumental Break]
[Bridge]
[Chorus]
[Outro | Ad-libs]
```

### Genre-Specific Metatags

- `[Pre-Chorus]` — essential; without it, the emotional arc of the song flattens
- `[Chorus | Sung Hook | Soulful]` — inline vocal direction reinforces the payoff character
- `[Bridge | Ad-libs]` — cues the expressive improvisational section typical in soul bridges
- `[Instrumental Break]` — for neo-soul, a Rhodes or bass interlude section works well; signals the model to generate an extended instrumental passage
- `[Outro | Ad-libs]` — the classic soul outro fade with improvised vocal runs
- `[Call and Response]` — can be embedded within chorus or bridge to trigger vocal call-and-response pattern
- Avoid `[Rap Verse]` unless intentionally doing an R&B/hip-hop hybrid
- Avoid `[Drop]` — biases toward EDM rather than soul

### Line Length & Rhyme Scheme

- Verse: 8–12 syllables; unhurried, conversational, emotional specificity valued over density
- Pre-chorus: 6–10 syllables; shorter, more urgent
- Chorus: 6–10 syllables; hook phrase should carry the emotional weight of the song's title or theme
- Bridge: freer — can break rhyme scheme intentionally for raw emotional effect
- AABB rhyme in verses is standard; ABAB also common for more poetic writing
- Chorus: AABB or repeated couplet; title phrase should appear at least twice
- Soul/gospel tradition: second-person address ("you", "Lord") or direct confession ("I need", "I feel") reads most authentically

### Lyric Density Tips

- Verse: moderate density; let the groove breathe between lines
- Chorus: emotional density, not syllabic density — strong words, simple phrasing
- Bridge: allow space for the vocal performance to be the content; fewer words, more feeling
- Write ad-lib directions in parentheses within bridge and outro lines — Suno reads these as performance cues: `(yeah, uh-huh, come on)`

---

## Slider Settings

| Slider | Recommended Value (0–100) | Rationale |
|--------|--------------------------|-----------|
| Weirdness | 25–45 | Classic soul and 90s R&B: 25–35. Neo-soul and alternative R&B: 35–50 — the genre has more experimental tolerance. Avoid pushing above 55; the groove becomes unstable. |
| Style Influence | 70–85 | R&B needs high style adherence to anchor the urban warm sound and prevent drift to generic pop. Use 80–85 with specific subgenre tags; drop to 70–75 with detailed instrument tags. |
| Audio Influence | 55–70 | Only if uploading a reference track; useful for matching a specific vocal timbre or Rhodes character. |

**Oversaturation pass:** If the mix is too warm/muddy, drop Style Influence to 65 and add `"clean mix"` or `"crisp production"` to the style block. This tends to thin the harmonic layers slightly.

---

## Known Quirks & Pitfalls

- **Mix is oversaturated — too much reverb, blurry harmonics** → This is the most common R&B failure in Suno. Cause: stacking too many warmth/lush tags. Fix: reduce style block to 8–10 focused tags; add `"clean mix"` or `"dry vocals with subtle reverb"` to counteract. Avoid `"lush"`, `"rich"`, and `"warm"` all simultaneously — one or two warmth descriptors is enough.

- **Suno generates pop-R&B instead of neo-soul** → Era and instrument specificity is the fix. Add `"Rhodes electric piano"` (by name), `"brushed drums"`, `"jazzy chords"`, `"analog warmth"`, and drop the BPM to 75–80. Without instrument specifics, Suno defaults to contemporary radio R&B production.

- **Vocal runs are absent** → Add `"vocal runs"` and `"melismatic vocals"` to style block. Without these, Suno generates controlled smooth delivery with no embellishment.

- **Bridge lacks energy contrast** → The bridge must differ from the chorus in lyric density and emotional register. If the bridge lyrics are as dense as the chorus, Suno won't shift production energy. Use `[Bridge | Contrast]` or `[Bridge | Ad-libs]` and write sparser, more improvisational bridge lines.

- **90s new jack swing sounds generic** → Add `"swing rhythm"`, `"punchy drums"`, and a specific BPM (`"95 BPM"`). The swing feel is the genre's identity — without `"swing rhythm"` in the style block, Suno generates a straight-feel groove that reads as generic contemporary R&B.

- **Outro fades too quickly** → Write at least 6–8 lines of `[Outro]` content with ad-lib direction. Suno's closing sections reflect the length of lyric material provided; a 2-line outro produces a hard cut.

---

## Example Prompt

### Example 1: Neo-soul — late night, introspective

**Style block:**
```
neo-soul, 76 BPM, soulful female vocals, vocal runs, Rhodes electric piano, warm sub bass, brushed drums, jazzy chords, layered harmonies, analog warmth, introspective, late-night vibe, intimate atmosphere
```

**Lyrics skeleton:**
```
[Intro]
(Rhodes plays softly — 4 bars)

[Verse 1]
The candle burned down to the wick last night
I sat with all my questions in the fading light
You always knew the words before I said a thing
But silence has a way of carrying everything

I keep your memory in the hollow of my chest
Some days it's a burden, some days it's what I need the best
I trace the outline of a life we should have had
In the spaces between all the good and all the bad

[Pre-Chorus]
Maybe I was wrong to hold on this long
Maybe love was right but the timing was wrong
Tell me, tell me—

[Chorus]
I'm still here in the quiet
Still learning how to breathe
I'm still standing in the riot
Of everything you mean to me
Still here

[Verse 2]
I played our songs on shuffle just to hear your voice
Found an old voicemail and I made a choice
To let it play until the feeling passed
Nothing good that's real was ever meant to last

But I carry what we built like it's a sacred thing
Every ordinary Tuesday that the memory brings
The way the morning light would catch your coffee cup
I'm still learning how to put all that stuff up

[Pre-Chorus]
Maybe I was wrong to hold on this long
Maybe love was right but the timing was wrong
Tell me, tell me—

[Chorus]
I'm still here in the quiet
Still learning how to breathe
I'm still standing in the riot
Of everything you mean to me
Still here

[Bridge]
(yeah)
Some nights I almost call
Some nights I let it go
Some nights the wall comes down
And I just need you to know
(uh-huh)
That I am better now
And I am healing slow
But something stays with me
Wherever that I go

[Chorus]
I'm still here in the quiet
Still learning how to breathe
I'm still standing in the riot
Of everything you mean to me
Still here

[Outro]
Still here, still here
(vocal runs — improvised)
I'm right here, right here
(yeah, mmm)
Learning to let go
(fade)
```

**Notes:** The parenthetical ad-lib directions in `[Bridge]` and `[Outro]` (`(yeah)`, `(uh-huh)`, `(mmm)`) act as performance cues — Suno treats them as vocal improvisation signals, which is idiomatic to soul. The `[Pre-Chorus]` cut-off line ("Tell me, tell me—") creates the emotional tension-before-release the genre depends on. Rhodes electric piano by name is mandatory in the style block for this subgenre.

---

## Research Sources

- HookGenius — "Suno Prompts for R&B Music" (2026-04-22)
- HookGenius — "Suno Style Tags List: 300+ Tested Tags by Genre & Mood" (2026-04-22)
- GitHub / entrepeneur4lyf — "suno_ai_meta_tags_guide" (accessed 2026-04-26)
- Jack Righteous — "Top Music Genres 2025: Create Hip-Hop & R&B with AI" (2026-04-22)
- Travis Nicholson / Medium — "Complete List of Suno AI Genres (100+ Styles)" (Mar 2026)
- HookGenius — "Suno v5 Complete Guide" (2026-04-22)
- Research compiled 2026-04-26
