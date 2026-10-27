# Suno v6 Advanced Mode Fundamentals

> **Reviewed:** 2026-10-27 against Suno's official documentation.
> **Scope:** General prompting in v6 Advanced mode; no listening tests performed in this update.
> **Evidence:** Documented controls are sourced below. Templates and workflow advice are starting hypotheses, not guaranteed model behavior.

## Choose the Workflow and Model

Here, **Advanced mode** means the manual lyrics-and-style workflow. Suno's help articles still call this **Custom mode**, with additional controls under **Advanced Options**. Follow the labels shown in your client; mode names and option placement can differ. [1]

Choose **v6** for a specific brief, **v6-wild** for exploration, or **v6-mini** for fast iteration. These are different models, so record the exact variant when comparing results. Suno lists v6 and v6-wild for Pro/Premier, and v6-mini for all users. [2]

Suno also documents multi-input instructions and automatic workflow selection in **Simple mode**. Do not assume a request to edit an existing song or combine source tracks becomes that operation merely by pasting it into Advanced mode's Style field. [3]

## Put Each Instruction in the Right Place

| Field or control | What to supply |
|------------------|----------------|
| Title | The display title |
| Style / Styles | Genre, groove, instruments, vocal delivery, production and major arrangement changes |
| Lyrics | The exact words, line breaks and sparse section/performance cues |
| Exclude | Unwanted instruments, styles or vocal traits; use the dedicated field [4] |
| Vocal Gender | Use the UI selector when relevant, then describe the voice in Style [5] |
| Instrumental | Use the client control for a fully instrumental track; do not rely on a bracket tag alone |
| Creative controls | Set actual UI values; writing slider numbers in Style is not a settings operation |

Treat Style and Lyrics as complementary directions for one performance. Do not assume their effects are isolated or that a lyric cue cannot influence the sound.

## Write a Clear Style Brief

This is an editorial starting template, not a parser grammar or an optimal tag count:

```text
[Main genre and era], [tempo or groove]. [Key instruments and their roles].
[Voice character, register and delivery]. [Production texture].
[One or two important arrangement changes].
```

Replace placeholders before use. A compact paragraph or clear comma-separated phrases are both reasonable experiments. Prioritize the few details that define the track, remove redundant adjectives, and resolve conflicting instructions. A genre blend is valid when you explain which elements belong to each genre.

Example — original, not audio-tested:

```text
Playful 1990s alternative pop, brisk straight groove. Dry drums, bouncing bass,
clipped guitar and short accordion fills. A nasal, conversational male baritone
with crisp consonants and deadpan phrasing. Close, mostly dry lead vocal.
Sparse verses open into a bright group-sung chorus, then a short decisive ending.
```

Optional **Exclude** example: `vocal fry, breathy lead, long melismatic runs`.
Specify the desired delivery positively as well; an exclusion is not a guarantee.

### Give the Voice a Character

Describe audible traits: register, resonance, articulation, attitude, accent if requested, and spoken versus sung delivery. A character name alone does not define a voice. For a duet, define both voices clearly and mark intended turns in Lyrics; stable casting and exact speaker changes still need listening checks.

## Preserve Lyrics and Use Sparse Cues

- Preserve supplied words, pronunciation spellings, syllable splits, punctuation and deliberate vowel extensions unless the user requests changes. Propose alternatives separately.
- Start with simple section labels such as `[Verse 1]`, `[Chorus]` and `[Bridge]`. See [metatags.md](metatags.md) for their evidence limits.
- Put local delivery cues near the relevant passage, and describe essential vocal traits in Style too.
- Line length and syllable density are useful pacing experiments. They do not specify exact timing, melody or note lengths.
- Avoid production paragraphs in Lyrics: they may be sung, ignored or interpreted inconsistently.
- Check the current UI's counters and validation. This review did not verify v6 character caps or silent truncation; do not reuse old 120/1,000/3,000/5,000-character claims as platform limits.

## Start a Controlled Comparison

1. Record the model, full Style/Lyrics/Exclude text, control values, and any Voice, Custom Model, Inspo or upload used.
2. Set **Variety to 0** when testing your exact style wording: Suno says Variety can revise the style prompt. This does not make generation deterministic. [3]
3. Use the [slider guide](sliders.md) for initial control choices; hold references and personalization constant.
4. Compare multiple takes, including the opening, chorus, transitions and ending. Change one prompt element or control per comparison.
5. Record whether the requested behavior actually happened; distinguish a preference from a reproducible improvement.

**Max Mode** costs extra credits. Suno recommends it for longer songs, fidelity-sensitive covers, style transfer and consistency; consider it when those goals matter, rather than enabling it for every draft. [3]

## Migration and Evidence Limits

Suno says pre-v6 models are retired; old recordings remain, while new iterations use v6 models. [3] The [v5/v5.5 fundamentals](suno-v5-fundamentals.md) and existing genre examples are historical references, not proof of v6 behavior.

There is no verified universal best slider preset, magic descriptor count, deterministic character casting, or complete v6 metatag grammar in the sources reviewed here. Do not claim exact bridge placement, title-case requirements, four-line outros, pipe scoping, or Audio Influence thresholds as established rules without version-specific evidence.

## Sources

All accessed 2026-10-27. Older help articles explain controls; they do not establish new v6-specific behavior.

1. [Suno: Can I use my own lyrics?](https://help.suno.com/en/articles/2415873) — updated 2025-12-19.
2. [Suno: Current Models: v6](https://help.suno.com/en/articles/13924737) — updated 2026-09-09.
3. [Suno: v6 FAQ](https://help.suno.com/en/articles/13924481) — updated 2026-09-09.
4. [Suno: How do I exclude elements of a song?](https://help.suno.com/en/articles/3161921) — updated 2025-12-19.
5. [Suno: Can I choose the gender of the singer in my song?](https://help.suno.com/en/articles/10153473) — updated 2026-09-09.
