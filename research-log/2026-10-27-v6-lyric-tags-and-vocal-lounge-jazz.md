# v6 Lyric-Tag Adherence and Intimate Vocal Lounge Jazz

**Date:** 2026-10-27
**Status:** Documentation and musical research; all proposed prompt comparisons await listening results.
**Scope:** Lyric-cue adherence and a restrained mid-century small-combo vocal swing brief. No broad jazz audit, audio evaluation, Suno generation or paid API call was performed.

## Documented Findings

- Style Influence concerns the Style input. Weirdness controls experimentation; 50 is Suno's normal reference. The source does not establish a lyric-tag strength control. [1]
- Variety 0 retains the supplied style wording. Max Mode is recommended for longer tracks, close covers and consistency at additional credit cost. These are not exact timing guarantees. [2]
- Song Editor supports prompting replacements for a selected region; adding a section has a beat-count control. [3] The v6 overview confirms Replace Section is in the current editing toolset. [4]
- Cover uses an actual source recording to preserve its melodic foundation. Reusing Style and Lyrics text is not equivalent to supplying the audio reference. [5]
- Suno's glossary provides vocabulary for intimate vocals, tempo freedom, unaccompanied singing and instrumental roles, but does not establish a complete bracket grammar. [6]

## Genre Research and Editorial Application

The new [vocal lounge jazz guide](../genres/vocal-lounge-jazz.md) draws on Berklee's vocal and arranging curricula, the Herbie Hancock Institute of Jazz's swing lesson and Yamaha's clarinet guide. Exact sources and their limited roles are recorded there.

The working musical brief is intimate male crooning with relaxed swing, acoustic piano, walking upright bass, brushes and separately featured reeds. Specific instrument roles, restrained dynamics and a clearly located accompaniment stop make the intended arrangement easier to assess. Whether those descriptions improve Suno adherence remains untested.

Corrections to avoid overclaiming:

- Concise cue fragments are experiments, not proven higher-reliability syntax. Detailed bracket prose is not a set of enforceable commands either.
- Behind-the-beat vocal placement and a change in the whole band's tempo are different intentions. Do not remove expressive phrasing merely to obtain a steady accompaniment.
- A solo instrument can have accompaniment; a cappella means no instruments. Specify a single voice separately when needed.
- The previously proposed 8/8/16-bar solo plan is not a best-practice preset. At steady 80 quarter-note BPM in 4/4 it occupies 96 seconds; a 4-bar intro adds 12 seconds. These are calculated targets, not observed output timings.
- Weirdness 30 / Style Influence 80 is a possible comparison point, not a validated genre or tag-adherence optimum.
- Do not impose a fixed AABA form, syllable count or new harmonic scheme on the user's existing melody and words.

## Proposed Comparisons

Run only comparisons relevant to a listening problem, keeping the other fields, references and controls fixed. Compare multiple takes and record the actual settings.

| Question | Change | Listen for |
|----------|--------|------------|
| Does a simpler cue help? | Detailed solo direction versus `[Piano Solo]` plus `[Instrumental]` | Correct soloist, absence of singing, transition back to the verse |
| Does explicit global direction help the ending? | Add a clear band-stop sentence to Style while keeping the local cue fixed | All instruments cease; lead singer continues alone |
| Is rubato causing unwanted tempo drift? | Whole-song heavy rubato versus vocal phrasing over a steady rhythm section | Stable accompaniment with expressive vocal placement |
| Are the interludes too long? | Shorten one selected interlude | Lyric momentum and a natural section transition |
| Can a local edit solve an isolated problem? | Replace the affected passage instead of regenerating the whole track | Desired change plus an acceptable boundary with surrounding audio |

**Outcome:** No comparison has been run or reported. No remedy was added to confirmed pitfalls. Keep the source song's lyric text and pronunciation unchanged during prompting-only experiments.

## Primary Product Sources

All accessed 2026-10-27. Older feature descriptions are not v6 performance benchmarks.

1. [Creative Sliders](https://help.suno.com/en/articles/6141377) — updated 2025-06-03.
2. [v6 FAQ](https://help.suno.com/en/articles/13924481) — updated 2026-09-09.
3. [Song Editor](https://help.suno.com/en/articles/6141505) — updated 2025-05-30.
4. [What's New in v6](https://help.suno.com/en/articles/13924801) — updated 2026-09-09.
5. [Cover](https://suno.com/products/covers) — no publication date shown.
6. [Music Glossary](https://help.suno.com/en/articles/9010177) — updated 2025-11-17.

## Validation

- Passed relative Markdown file-link, code-fence balance and whitespace checks across all seven changed files.
- Loaded `vocal-lounge-jazz` through the existing CLI's knowledge loader and verified that it includes the new guide and current lyric-cue troubleshooting.
- Checked the solo-duration arithmetic independently. No changes to generation code were needed.
- No Suno generations or paid API calls were made; musical outcomes remain untested.
