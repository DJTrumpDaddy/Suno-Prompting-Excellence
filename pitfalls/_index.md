# Pitfalls Index

Quick-lookup table: symptom → diagnosis file. When a user reports a problem, scan this table first.

---

## Structural Issues

| Symptom | Likely Cause | File |
|---------|-------------|------|
| Section tag ignored (e.g. bridge never appears) | Tag placement or count | *(not yet documented)* |
| Song ends too early / truncates | Lyric length exceeded limit | *(not yet documented)* |
| Sections repeat more than expected | Missing structural variety cues | *(not yet documented)* |
| Intro runs too long | No explicit first verse cue | *(not yet documented)* |

## Sonic / Mix Issues

| Symptom | Likely Cause | File |
|---------|-------------|------|
| Vocals buried under instruments | Mix style tags or intensity | *(not yet documented)* |
| Instrument bleed into vocal sections | No `[Instrumental]` section delineation | *(not yet documented)* |
| Wrong instrument dominant in mix | Style tag specificity | *(not yet documented)* |
| Muddy low-end / unclear mix | Conflicting genre tags | *(not yet documented)* |

## Style / Genre Issues

| Symptom | Likely Cause | File |
|---------|-------------|------|
| Wrong genre feel entirely | Style block tag conflicts | *(not yet documented)* |
| Mood mismatch (happy when intended dark) | Mood modifier absent or diluted | *(not yet documented)* |
| Tempo too fast / slow | No explicit tempo cue in style block | *(not yet documented)* |
| Style tags cancelled out each other | Contradictory descriptors | *(not yet documented)* |

## Lyric Issues

| Symptom | Likely Cause | File |
|---------|-------------|------|
| Lines repeated verbatim across sections | Lyrics too short; Suno padded | *(not yet documented)* |
| Words garbled / unintelligible | Unusual vocabulary or names | *(not yet documented)* |
| Chorus lyrics ignored | Lyrics exceeded processing window | *(not yet documented)* |
| Language switched mid-song | Language mixing in lyrics | *(not yet documented)* |

---

## Adding a New Entry

1. Create `pitfalls/[symptom-slug].md` using the template below
2. Add a row to the appropriate table above
3. Update `KNOWLEDGE_STATUS.md` pitfall coverage section

### Pitfall File Template

```markdown
# Pitfall: [Symptom Name]

**Classification:** Structural | Sonic | Style | Lyrics
**Severity:** High | Medium | Low
**First documented:** YYYY-MM-DD

## Symptom
What the user observes.

## Root Cause
What in the Suno v5 processing chain causes this.

## Diagnosis Questions
- Question to distinguish this from similar issues

## Fix
Step-by-step remedy with example.

## Prevention
How to avoid this in the initial prompt.

## Failed Approaches
- Tried X → did not fix because Y (YYYY-MM-DD)

## Sources
- Source (date)
```
