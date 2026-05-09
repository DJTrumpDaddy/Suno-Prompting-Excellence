# Genre: Hip-Hop / Rap

> **Status:** Draft
> **Last updated:** 2026-05-09
> **Suno version scope:** v5, v5.5

---

## Overview

Hip-hop and rap covers a wide BPM range (70–100 BPM for most subgenres; trap often sits at 140 BPM half-time feel making the rhythmic pocket feel like ~70 BPM) and is built around rhythmic vocal delivery, 808 sub-bass, and percussion-dominant production. Major subgenres Suno handles: trap, boom bap, lo-fi hip-hop, phonk, melodic rap, cloud rap, and drill.

The single biggest challenge in Suno for this genre is forcing rap delivery instead of singing. Suno's default behaviour tilts melodic. Without explicit rap-forcing tags and the `[Rap Verse]` metatag in the lyrics, Suno will sing your rap verses in a pop register. The `[Rap Verse]` metatag is the most critical tool in this genre's toolkit.

**Sonic fingerprint:**
- 808 sub-bass as the primary low-end anchor (trap) or sampled/live bass (boom bap)
- Kick and snare pattern defines the subgenre: trap = off-beat rattling snare + rolling hi-hats; boom bap = punchy kick on 1&3, snare on 2&4, swing feel
- Rhythmic spoken/rap vocal delivery over the beat — not sung
- Hi-hat patterns are subgenre identity markers (fast rolling = trap; crisp sparse = boom bap; bouncy = drill)
- Minimal melodic content in verses; hook/chorus may be sung or melodic

---

## Style Block Recommendations

### Core Tags

Always lead with the specific subgenre — `"hip-hop"` alone produces generic output:

**Trap:**
```
trap, 140 BPM, rap vocals, heavy 808 bass, rolling hi-hats, rattling snare, dark synth, aggressive, street, polished mix
```

**Boom Bap:**
```
boom bap, 90 BPM, rap vocals, punchy kick, crisp snare, swing rhythm, dusty samples, lo-fi texture, lyrical, NYC
```

**Lo-fi Hip-Hop (instrumental/chill):**
```
lo-fi hip-hop, 80 BPM, jazzy chords, warm vinyl crackle, mellow, laid-back, Rhodes piano, soft drums
```

**Melodic Rap / Cloud Rap:**
```
melodic rap, 90 BPM, rap-singing, atmospheric pads, autotuned vocals, introspective, hazy, trap-influenced, spacious mix
```

### Effective Modifiers

- `"rap vocals"` — the most important style tag; explicitly biases Suno toward spoken delivery over singing
- `"rhythmic delivery"` — reinforces non-melodic vocal flow
- `"spoken flow"` — another forcing function for rap vs. singing
- `"heavy 808"` — sustained sub-bass boom; specify character or Suno defaults to a generic bass
- `"distorted 808"` — clipped, gritty low-end (phonk, hard trap)
- `"fast rolling hi-hats"` — trap-defining percussion
- `"crisp hi-hats"` — boom bap percussion character
- `"bouncy hi-hats"` — UK drill / drill character
- `"dusty samples"` — boom bap lo-fi texture
- `"vinyl crackle"` — adds lo-fi warmth
- `"ad-libs"` — generates background hype vocals (common in trap)
- `"crowd hype"` — backing vocal energy for stadium/banger feel

### Tags to Avoid

- `"singing"`, `"melodic vocals"` — directly contradicts rap delivery; Suno will sing your rap verses
- Conflicting subgenre stacking: `"boom bap trap drill"` — these have incompatible rhythmic signatures; pick one primary subgenre
- `"acoustic guitar"`, `"orchestral"` — instruments that fight the urban electronic aesthetic; qualify explicitly if intentional (e.g., `"acoustic guitar sample, boom bap"`)
- `"classical"`, `"metal"` — obvious genre contamination
- `"ambient"` — suppresses the rhythmic drive hip-hop requires

---

## Lyric Structure Recommendations

### Typical Structure

Hip-hop structure varies by subgenre but the core pattern is:

```
[Intro]
(4–8 bars — beat intro, optional spoken ad-lib)

[Verse 1]
(16 bars — 16 lines of rap; tell the story, establish the flow)

[Hook]
(4–8 lines — often sung or melodic; the repeatable payoff)

[Verse 2]
(16 bars — escalate; new rhymes, same flow or deliberate switch)

[Hook]

[Bridge]
(optional — 4–8 lines; tempo shift, introspective break, or featured artist slot)

[Hook]

[Outro]
(4–8 lines — cooldown or final statement)
```

For trap/drill specifically, hooks are often shorter and more rhythmically repetitive:
```
[Intro]
[Rap Verse]
[Hook]
[Rap Verse 2]
[Hook]
[Outro]
```

### Genre-Specific Metatags

- `[Rap Verse]` — **the single most critical metatag for this genre**. Without it, Suno defaults to singing. Use instead of or in addition to `[Verse]` in all rap sections. `[Verse | Rhythmic Rap]` is an alternative form.
- `[Hook]` — prefer over `[Chorus]` for most hip-hop; hooks are rhythmically tighter than pop choruses. `[Chorus | Sung Hook]` works for melodic rap where the hook is explicitly sung.
- `[Rap Verse 2]` — use for the second verse to maintain explicit rap delivery signalling.
- `[Spoken Word]` — for intro monologues or bridge spoken sections.
- `[Instrumental Break]` — signals a production-only section (beat switch, sample flip).
- `[Ad-libs]` — triggers background hype vocals within a section; works well inside `[Hook]`.
- Avoid `[Build]` and `[Drop]` — these bias the model toward EDM structure, not hip-hop.

### Line Length & Rhyme Scheme

- Standard bar: 8–12 syllables, matching the 4/4 beat at the specified BPM
- Boom bap: AABB end rhymes; dense internal rhymes within lines for a lyrical feel
- Trap: AABB or looser rhyme; repetitive hook with 2–4 word phrases
- Multi-syllable internal rhymes are natural for boom bap; Suno handles them if you write them into the skeleton
- Hook: 2–4 word hook phrase repeated 4–8 times; short is stronger than complex
- 16-line verse blocks (16 bars) are the standard; 8-line verses are acceptable for shorter tracks
- First word of each bar is rhythmically load-bearing — strong consonants land better than soft vowels

### Lyric Density Tips

- Verse: dense; pack syllables to the beat — leave no dead space
- Hook: opposite; sparse, repetitive, rhythmically simple
- Bridge: can break density pattern intentionally (slower/more emotional)
- Write rap lyrics to the beat count, not to page appearance — count syllables aloud

---

## Slider Settings

| Slider | Recommended Value (0–100) | Rationale |
|--------|--------------------------|-----------|
| Weirdness | 30–50 | Mainstream hip-hop: 30–45. Experimental/cloud rap/phonk: 50–65. High weirdness in boom bap risks losing the swing feel. |
| Style Influence | 70–85 | Hip-hop needs high style adherence to anchor the urban sound and prevent genre drift toward pop. First 2–3 tags carry ~60–70% of the character. |
| Audio Influence | 55–70 | Only if uploading a reference beat; useful for matching a specific 808 character or drum mix. |

---

## Known Quirks & Pitfalls

- **Suno sings the rap verse instead of rapping** → This is the most common failure. Fix: (1) use `[Rap Verse]` metatag in every rap section, (2) add `"rap vocals"` and `"rhythmic delivery"` to style block, (3) exclude `"melodic vocals"`, `"singing"` from tags. All three fixes together are more reliable than any single one.

- **Wrong subgenre output despite explicit tag** → Genre tag position matters critically. Place the subgenre first in the style block. `"trap, heavy 808, rap vocals..."` outperforms `"...rap vocals, heavy 808, trap"`. The first 2–3 tags carry disproportionate influence.

- **808 bass is weak or absent** → Specify the 808 character: `"heavy 808"` for sustained sub-bass, `"distorted 808"` for clipped phonk-style grit. Generic `"bass"` or `"bass guitar"` does not reliably produce 808 sub-bass.

- **Hi-hat pattern is wrong for the subgenre** → Each subgenre has a signature hi-hat: trap needs `"fast rolling hi-hats"`, boom bap needs `"crisp hi-hats"`, drill needs `"bouncy hi-hats"`. Without specifying, Suno averages across patterns and the rhythmic identity collapses.

- **Conflicting subgenre bleed** → Avoid stacking `"boom bap"` + `"trap"` + `"drill"` together. These have incompatible rhythmic DNA. Choose one primary subgenre and one mood modifier at most.

- **Hook gets rapped instead of sung** → For melodic rap or hooks that should be sung, use `[Chorus | Sung Hook]` and add `"sung hook"` or `"melodic hook"` to the style block. The model needs an explicit signal that the hook is an exception to the rap-delivery instruction.

- **Track sounds like generic pop-rap despite tags** → Raise Style Influence to 80–85. Add a second genre anchor in position 2–3 of the style block (e.g., `"trap, dark, 808, rap vocals"` rather than `"trap, emotional, melodic, 808"`). Emotional/melodic tags pull toward pop-rap.

### v5.5 Audit Notes

> Audited 2026-05-09. No breaking changes confirmed.

- [Rap Verse] metatag remains load-bearing in v5.5 — still required to prevent Suno from singing instead of rapping
- Subgenre-first style block positioning unchanged — trap, boom bap, phonk, drill must lead the tag list
- v5.5 prompt accuracy improvement: subgenre tags (e.g., "phonk", "drill", "cloud rap") follow more faithfully without needing as many reinforcing descriptors
- If using Audio Influence with a reference beat: v5.5 picks up the original melody/pattern more aggressively than v5. Use ≤8% for vibe-only
- Rap/sung hybrid techniques ([Rap Verse] + [Chorus]) unchanged and still effective
- Chinese/dialect rap support improved in v5.5 (new feature)

---

## Example Prompt

### Example 1: Hard trap track (dark, aggressive)

**Style block:**
```
trap, 140 BPM, rap vocals, heavy 808 bass, rolling hi-hats, rattling snare, dark synth pads, aggressive, street, menacing atmosphere, ad-libs, polished mix
```

**Lyrics skeleton:**
```
[Intro]
(beat plays — 8 bars)
Yeah
Uh

[Rap Verse]
I been moving through the darkness all alone
Built this empire brick by brick out on my own
Every night I had to grind while they was sleep
Now I'm counting up the paper in the deep
They was laughing when I told them what I'd be
Now they knocking at the door and I don't see
Had to learn that loyalty is bought and sold
Traded all my trust for something cold

Ride or die, you know the code or you don't
Some will pull the trigger right and some of them won't
Keep my circle tight because the leaks will kill you slow
Every hand that's reaching up is another that'll go
Watch the energy around you like a hawk
Some will talk the talk but never really walk
I been watching all the faces in the crowd
Moving quiet but the outcome gonna be loud

[Hook]
Count it up, count it up, check the bag
Everything I built they said I never had
Count it up, count it up, stack it high
Told me I would fall but now I'm touching sky
Count it up

[Rap Verse 2]
Woke up hungry now the hunger never dies
Had to sacrifice the comfort for the rise
Every setback was a setup for the win
Armour on before the battle starts again
Seen the snakes inside the garden looking sweet
You can spot the ones who fold when there's no heat
My foundation built on nights they never saw
Broke the ceiling but I'm always wanting more

Can't stop, won't stop, 'til the vision's real
Every number on the chart is just a feel
But the legacy I'm building gonna stay
Long after all the noise has gone away
Watch the throne 'cause I been climbing every step
Earned every breath with nothing but respect
They want a seat but they ain't pay the dues
Tell me what you're worth when you ain't got to lose

[Hook]
Count it up, count it up, check the bag
Everything I built they said I never had
Count it up, count it up, stack it high
Told me I would fall but now I'm touching sky
Count it up

[Outro]
Yeah
That's how it go
(beat fades)
```

**Notes:** The double `[Rap Verse]` / `[Rap Verse 2]` pattern reinforces rap delivery throughout. The `[Hook]` (not `[Chorus]`) keeps the hook tight and rhythmically anchored. The sparse `[Intro]` and `[Outro]` give Suno room to add beat atmosphere. Keep ad-libs in the style block — they appear as background vocals organically.

---

## Research Sources

- HookGenius — "How to Make Hip-Hop & Rap Music in Suno AI" (2026-04-22)
- HookGenius — "We Analyzed 1,000+ Suno Prompts — Here's What Actually Works" (2026-04-22)
- GitHub / entrepeneur4lyf — "suno_ai_meta_tags_guide" (accessed 2026-04-26)
- sunoprompt.com — "AI Hip-Hop and Rap Cheat Sheet 530 Styles for Prompts" (2026-04-22)
- Jack Righteous — "Suno AI Hip-Hop & R&B Tag Guide" (2026-04-22)
- Medium / Jean-Luc Benazet — "20 Hip Hop & Rap Suno AI Prompts That Actually Sound Like the Real Thing" (Mar 2026)
- Research compiled 2026-04-26
