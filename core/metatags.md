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

## Claims Not Established for v6

Do not carry forward the old guide's universal claims that:

- Lowercase section labels are ignored.
- A bridge must follow the second chorus.
- An outro requires four or more lines to prevent looping.
- More than one tag per four lines is invalid.
- Pipe modifiers never affect later sections.
- Every v5/v5.5 tag retains identical behavior in v6.

Record successful and unsuccessful tests with the exact model, complete prompt, controls and listening outcome before upgrading these conventions into narrower recommendations.
