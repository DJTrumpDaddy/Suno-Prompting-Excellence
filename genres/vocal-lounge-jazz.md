# Genre: Intimate Vocal Lounge Jazz

> **Status:** Reviewed; audio validation pending
> **Last updated:** 2026-10-27
> **Suno version scope:** v6
> **Evidence:** Official product documentation, musical education sources, and explicitly untested prompting recommendations

## Overview

This guide targets a mid-century small-combo vocal jazz arrangement: relaxed swing, soft male crooning, acoustic piano, upright bass, brushes, clarinet and tenor saxophone. The era, instrument choices, dry humor and restrained dynamics form a particular creative brief, not a universal definition of lounge jazz. Start with the existing melody and lyric wording when refining a song.

Suno's glossary identifies crooning with intimate singing and distinguishes rubato, a cappella and scat. [1] Berklee's jazz singing curriculum treats articulation, dynamics, interpretation and rhythmic phrasing as distinct performance choices. [2] These support precise musical descriptions; they do not prove a tag is reliably executed by v6.

## Style Block Recommendations

### Core Direction

Candidate anchor: `1960s small-combo vocal jazz, relaxed swing, intimate male crooning`.

Use "smooth" to describe the desired voice when that is the intended meaning. The more specific genre anchor above is an editorial choice to test; no model-routing claim about the phrase "smooth jazz" has been established here.

### Instrument and Performance Roles

The wording below is a proposed arrangement, not a tested Suno recipe.

| Element | Candidate wording | Reason for the choice |
|---------|-------------------|-----------------------|
| Vocal | One male crooner, comfortably low-to-mid register, clear diction, fully sung conversational delivery | Communicates voice character without equating intimacy with whispering or speech |
| Phrasing | Relaxed behind-the-beat vocal phrasing over a steady rhythm section | Separates vocal placement from whole-band tempo changes |
| Piano | Sparse acoustic piano comping beneath the singer; a separate melodic solo | Gives accompaniment and soloing different roles |
| Bass | Walking upright bass | Walking bass describes a note on each beat; a two-beat feel is a different option [3] |
| Drums | Soft brushed drums, light swing pulse | An arrangement choice for the requested quiet texture, not a guarantee of brush rendering |
| Reeds | Warm clarinet and mellow tenor saxophone, brief fills between sung lines, one featured soloist at a time | Reduces competing lead directions; Yamaha documents clarinet's use as a swing solo instrument [4] |
| Dynamics | Restrained verses and a gentle chorus lift | Gives the refrain contrast without prescribing a loud climax |
| Recording | Close lead vocal, natural acoustic balance, subtle room ambience | Specifies audible production goals instead of requiring exact microphone or tape emulation |

Berklee's arranging curriculum separates form, instrument writing, articulation, dynamics and endings. [5] Assigning explicit roles here is an application of that framework, not a model benchmark.

### Conflicts to Resolve

- "Powerful vocals" and "reserved vocals" leave the intensity ambiguous. Choose the intended delivery explicitly.
- Global "heavy rubato" requests tempo freedom. If the band should keep swinging, put the flexible phrasing on the singer and reserve free time for the outro. Rubato and steady accompaniment can coexist; explain which part may move. [1]
- "Swing" alone does not specify ensemble size. Keep the small-combo instrumentation explicit rather than adding big-band cues. Historical swing arrangements often used separate saxophone, trumpet and trombone sections. [3]
- An instrument solo may retain accompaniment. An a cappella passage has no instruments; a solo voice additionally specifies one singer. [1]
- Do not force a new key, chord progression, AABA form or exact syllable count onto an existing song merely because it is jazz. Preserve the supplied words and pronunciation choices.

## Lyric Structure Recommendations

Use the song's actual verse/refrain structure. Put concise transition cues near the relevant passage; leave general tone and accompaniment in Style. Suggested fragments to compare:

```text
[Piano Solo]
[Instrumental]
```

```text
[Clarinet Solo]
[Instrumental]
```

```text
[Saxophone Solo]
[Instrumental]
```

```text
[Outro]
[A Cappella]
```

These are cue fragments, not a complete lyric prompt or a verified tag catalog. Describe the intended instrumental passages, then check for unwanted vocal entry. For the ending, reinforce the band stopping in Style. If a cue keeps being missed, use [the section-editing workflow](../core/metatags.md#when-a-lyric-cue-is-ignored).

### Pacing and Solo Duration

At a steady **80 quarter-note BPM in 4/4**, one bar takes `4 × 60 / 80 = 3 seconds`. This is arrangement arithmetic, not measured Suno performance:

| Suggested length | Duration under those assumptions |
|------------------|---------------------------------|
| 4 bars | 12 seconds |
| 8 bars | 24 seconds |
| 16 bars | 48 seconds |

Three solos of 8 + 8 + 16 bars total 96 seconds; a 4-bar introduction brings that to 108 seconds before any sung sections. Such lengths may suit a showcase arrangement, but are not automatic defaults for a compact vocal tune. Compare shorter breaks only if listening suggests the lyric momentum suffers. Tempo changes, free time and ignored cues can change actual duration. Use the editor when duration must be controlled. [6]

## Settings

Use [the current control guide](../core/sliders.md), not the historical jazz numeric matrix.

| Setting | Suggested approach | Evidence |
|---------|--------------------|----------|
| Model | v6 | Officially positioned for control [7] |
| Weirdness | Keep the existing value for prompt-only comparisons; without a baseline, start at 50 and compare 30 separately if desired | 50 is the documented reference; 30 is an untested experiment [8] |
| Style Influence | Record and hold the existing value; 80 can be a comparison point, not an optimum | Controls Style adherence, not guaranteed lyric-cue compliance [8] |
| Variety | 0 | Prevents Variety from revising the intended Style wording [7] |
| Audio Influence | N/A without a reference; otherwise record and hold the current value | No v6 jazz-specific threshold established |
| Max Mode | Consider for a longer cover or a consistency-focused full take; extra credits | Documented use cases, not exact section control [7] |
| Vocal / Instrumental | Male, if that matches the brief; Instrumental off for a vocal song | Keep a full-song setting distinct from instrumental interludes |
| References | Use the intended source recording in Cover when retaining its melody | Cover is an audio-reference workflow [9] |

Candidate Exclude field, tailored to this particular restrained acoustic brief: `trumpet, trombone, brass section, big band, theatrical belting, backing vocals, scat singing, electronic drums, synthesizers`. Use only unwanted elements; exclusions remain requests. Do not add a whole-song exclusion of instruments that must play before an a cappella ending.

## Known Quirks and Pitfalls

No v6-specific fix is confirmed in this guide. These are comparisons to run only when the corresponding symptom is heard:

| Symptom | Single-change experiment |
|---------|--------------------------|
| Vocal sounds theatrical | Replace ambiguous intensity language with intimate crooning and restrained volume |
| Accompaniment drifts in tempo | Replace whole-song heavy rubato with flexible vocal phrasing over a steady rhythm section |
| Reeds obscure the lyric | Specify short fills between sung phrases |
| Solo instrument is missed | Simplify that solo cue, holding Style and settings fixed |
| Band continues through the ending | Make the accompaniment stop explicit; if unresolved, replace or extend the ending |
| Instrumental breaks weaken pacing | Compare a shorter selected section rather than rebuilding the entire song |

## Example Prompt

**Status:** Original starting brief; not audio-tested. Keep supplied lyrics in the separate Lyrics field.

```text
1960s small-combo vocal jazz, relaxed 80 BPM swing. One intimate male crooner with clear diction, dry humor and fully sung conversational phrasing. Acoustic piano comps sparsely over walking upright bass and soft brushed drums. Warm clarinet and mellow tenor saxophone answer between vocal lines and take separate instrumental solos. The singer phrases gently behind the beat while the band keeps steady time. Restrained dynamics with a subtle lift in the refrain. Close lead vocal and natural room ambience. All instruments stop before the free-time outro; the same singer finishes alone and resolves into silence.
```

80 BPM and the unaccompanied ending are choices for this brief, not genre requirements. For a lyric-cue experiment, hold this Style text fixed and compare only the cue under test. Record model, references, full fields, settings, result links and the audible outcome before promoting a recommendation to a confirmed fix.

## Research Sources

All accessed 2026-10-27. Music education sources establish vocabulary and practice, not Suno reliability.

1. [Suno: Music Glossary](https://help.suno.com/en/articles/9010177) — updated 2025-11-17; musical terms and descriptive prompting.
2. [Berklee: Jazz Singing 101](https://online.berklee.edu/courses/jazz-singing-101) — Jan Shapiro's course description and syllabus; no article update date shown.
3. [Herbie Hancock Institute of Jazz: The Swing Era, Performance Practices](https://www.jazzinamerica.org/LessonPlan/11/4/136) — historical ensemble and rhythm-section roles; not a specific 1960s lounge recipe.
4. [Yamaha: The Modern Clarinet](https://www.yamaha.com/en/musical_instrument_guide/clarinet/structure/structure002.html) — instrument maker's guide; warm timbre and swing solo use.
5. [Berklee: Arranging 1, Rhythm Section](https://online.berklee.edu/courses/arranging-1-rhythm-section) — Dan Moretti and Suzanne Dean; course description and syllabus.
6. [Suno: Song Editor](https://help.suno.com/en/articles/6141505) — updated 2025-05-30; section prompting and beat count when adding sections.
7. [Suno: v6 FAQ](https://help.suno.com/en/articles/13924481) — updated 2026-09-09; model choice, Variety and Max Mode.
8. [Suno: Creative Sliders](https://help.suno.com/en/articles/6141377) — updated 2025-06-03; general definitions, not v6 jazz optima.
9. [Suno: Cover](https://suno.com/products/covers) — source recording and melody preservation.
