# Suno v6 Lyrics and Metatag Guidance

> **Reviewed:** 2026-10-27.
> **Status:** Practical conventions to test, not an official command grammar or a listening-validated v6 tag catalog.

Suno documents a dedicated lyrics field in its [Custom workflow](https://help.suno.com/en/articles/2415873). The official pages reviewed in [the v6 fundamentals](suno-v6-fundamentals.md#sources) do not establish a complete tag syntax, reliability tiers or strict parsing rules.

## Start with Simple Structure

Put a section label on its own line before the associated lyrics. This is a readable convention; it does not guarantee exact section timing or completion.

| Candidate cue | Intended direction |
|---------------|--------------------|
| `[Intro]` | Opening passage |
| `[Verse 1]`, `[Verse 2]` | Distinct verses |
| `[Pre-Chorus]` | Transition into the hook |
| `[Chorus]` | Main refrain |
| `[Bridge]` | Contrasting section wherever the composition needs it |
| `[Instrumental]`, `[Interlude]`, `[Guitar Solo]` | Instrumental passage or featured instrument |
| `[Build]`, `[Drop]` | Energy rise and payoff, when the genre fits |
| `[Outro]`, `[Fade Out]` | Intended ending |

Begin with fewer cues. Add one only when a listening result suggests it is needed. Describe important arrangement changes in Style as well. A fully instrumental track should use the available Instrumental control, not depend solely on a tag.

## Delivery and Multiple Voices

Candidates such as `[Spoken]`, `[Rap Verse]`, `[Whispered]`, `[Harmonies]` and `[Duet]` express intent. They may be ignored, blended or carried into another section. Reinforce an essential delivery in Style and check the result.

For character exchanges, define the voices using audible traits in Style and keep turn labels simple in Lyrics. Names alone are not voice identities. Do not promise exact switching or a separate controllable singer for every character tag.

Pipe notation such as `[Verse 1 | spoken | sparse]` is an optional experiment. It is not a verified v6 API; the pipe does not guarantee local scope, precedence, or a reset at the next section. Prefer plain section labels if an elaborate header is ignored or sung.

## Preserve the User's Words

Keep intentional spelling, phonetics, punctuation, repeated syllables and stretched vowels unless the user asks for edits. For a prompting-only revision, change the surrounding instructions rather than rewriting the lyric content. Show proposed pronunciation changes separately.

Punctuation, spacing and line breaks can suggest phrasing but do not encode exact pauses or note lengths. Parentheses can be interpreted as singable text. Keep explanatory prose outside the paste-ready Lyrics field.

## Optional Structure Example

Original illustrative lyrics; no audio validation:

```text
[Verse 1]
The kettle clicks, the room turns blue
I set another cup for you

[Chorus]
Leave a light beside the door
I am coming home once more

[Bridge]
The road is quiet after rain
I hear your laughter once again

[Chorus]
Leave a light beside the door
I am coming home once more

[Outro]
Leave a light
```

Use the structure the song needs. Repeating a chorus is a composition choice, not a mandatory parser requirement.

## When a Lyric Cue Is Ignored

**Evidence:** Documentation review on 2026-10-27; these comparisons have not been listening-tested. No dedicated lyric-tag compliance control or complete v6 bracket grammar was found in the reviewed official sources.

1. Identify the audible requirement: the correct solo instrument, an unaccompanied ending, a softer singer, or an exact duration. Keep the lyric wording fixed.
2. Test one simpler local cue while holding Style, settings and references constant. For example, compare a detailed piano-solo instruction with `[Piano Solo]` followed by `[Instrumental]`. Shorter wording is a hypothesis, not an established reliability advantage.
3. In a separate comparison, reinforce an essential transition in Style. For an `[Outro]` / `[A Cappella]` cue, try: "All instruments stop before the outro; the same singer finishes alone." Keep subtle performance preferences in the global brief rather than stacking them onto every section.
4. Evaluate the passage across the generated alternatives. Record what was actually followed; one successful take does not establish a universal tag rule.
5. If the rest of the recording works, target the affected region with Replace Section. Suno documents selecting a region, entering a prompt, previewing alternatives and adjusting the transition. [1]

| Requirement | Prompt or editing approach |
|-------------|----------------------------|
| A particular instrument takes a solo | Name it in Style and try a short local solo cue; verify by listening |
| Voice alone at the end | State the accompaniment stop explicitly and try an a cappella cue; replace or extend the ending if needed |
| A section of a chosen length | Use the editor's beat-count control when adding a section; a lyric tag such as `8 bars` is only a request [1] |
| An exact silent gap or cutoff | Edit the audio timeline in Studio or a DAW; `[Long pause]` and `[End]` do not establish exact timing |
| Preserve an existing melody | Use Cover with the recording as its reference; textual lyric tags alone do not carry the source melody [2] |

Documented editing controls do not guarantee that every generated replacement will satisfy the requested sound. Labels and availability can vary by client and plan.

**Slider limits:** Style Influence concerns Style input; Variety can rewrite Style; Weirdness concerns experimentation. None is documented as a strict lyric-tag compliance control. Max Mode is described for consistency and fidelity-sensitive work, not exact tag execution. See [sliders.md](sliders.md).

Sources accessed 2026-10-27:

1. [Suno: How to Use Song Editor](https://help.suno.com/en/articles/6141505) — updated 2025-05-30; region prompts and beat count for added sections. The [v6 feature overview](https://help.suno.com/en/articles/13924801), updated 2026-09-09, confirms Replace Section remains in the current toolset.
2. [Suno: Cover](https://suno.com/products/covers) — source audio and melody preservation; no publication date shown.

See the [research record](../research-log/2026-10-27-v6-lyric-tags-and-vocal-lounge-jazz.md) for evidence limits and proposed comparisons.

## Claims Not Established for v6

Do not carry forward the old guide's universal claims that:

- Lowercase section labels are ignored.
- A bridge must follow the second chorus.
- An outro requires four or more lines to prevent looping.
- More than one tag per four lines is invalid.
- Pipe modifiers never affect later sections.
- Every v5/v5.5 tag retains identical behavior in v6.

Record successful and unsuccessful tests with the exact model, complete prompt, controls and listening outcome before upgrading these conventions into narrower recommendations.
