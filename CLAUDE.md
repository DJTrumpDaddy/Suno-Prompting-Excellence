# Suno v5 Prompt Engineering System — Claude Instructions

This is a self-improving Suno v5 prompt engineering knowledge base. Follow this workflow for every interaction.

---

## When a User Asks to Generate a Song

### Step 1: Gap Detection (always run first)

Read `KNOWLEDGE_STATUS.md` and check:
- Is `genres/[genre].md` present and substantive for the requested genre?
- Are any structural techniques requested (through-composed, multi-genre, spoken word) covered in the KB?
- Are there known style tag interactions for this combination documented?
- Are genre-specific slider settings documented?

If any check is **thin or missing**:
1. Run targeted web search (use `WebSearch` tool)
2. Write findings to the appropriate KB file (create `genres/[genre].md` if it doesn't exist, use `genres/_template.md` as the base)
3. Update `KNOWLEDGE_STATUS.md` to reflect new coverage
4. Then proceed to generation

### Step 2: Load Relevant KB Files

Always read:
- `core/suno-v5-fundamentals.md`
- `core/metatags.md`
- `core/sliders.md`

If genre file exists: `genres/[genre].md`

### Step 3: Generate Four Artifacts

Output exactly:

**TITLE:** The song title

**STYLE BLOCK:**
```
[comma-separated style/genre/mood descriptors — ~120 chars]
```

**LYRICS:**
```
[Full lyrics with Suno metatags: [Verse], [Chorus], [Bridge], etc.]
```

**SLIDER SETTINGS:**
| Slider | Value (0–100) | Rationale |
|--------|--------------|-----------|
| Weirdness | X | ... |
| Style Influence | X | ... |
| Audio Influence | X | (only relevant if user uploads reference audio) |

---

## When a User Reports a Problem

### Feedback Triage Workflow

1. **Classify** the issue:
   - Structural (section ignored, wrong arrangement, truncation)
   - Sonic (vocals buried, instrument bleed, mix)
   - Style (wrong genre, mood mismatch, tempo)
   - Lyrics (repetition, truncation, garbling)

2. **Check** `pitfalls/_index.md` for a known solution

3. **If undocumented**: run targeted web search for the specific failure mode

4. **Propose** a specific fix with before/after example

5. **Ask user to test** the fix

6. **After user confirms result**:
   - Fix worked → write to `pitfalls/[symptom].md`, update `pitfalls/_index.md`
   - Fix failed → write to `research-log/YYYY-MM-DD-[topic].md` as "attempted, failed"
   - **Never commit unverified fixes to pitfalls/**

---

## KB Update Rules

- Genre files are created on-demand when a new genre is first requested
- Use `genres/_template.md` as the base for all new genre files
- `KNOWLEDGE_STATUS.md` must be updated after every KB write
- Research log entries go in `research-log/YYYY-MM-DD-[topic].md`
- Commit all KB changes after writing them (use descriptive commit messages)

---

## CLI Tools Available

```bash
# Generate a prompt
python generate.py "your song idea here"
python generate.py --genre synthwave "neon-soaked love song"

# Triage a problem
python feedback.py "the bridge was ignored entirely"

# Commit a confirmed fix to KB
python feedback.py "the bridge was ignored" --commit "use [Bridge] tag after second chorus" --filename bridge-ignored

# Log a failed fix
python feedback.py "vocals were buried" --log-failed "adding 'clear vocals' to style block"
```

---

## Commit Style

When writing KB updates to git:
- `kb: add genres/[genre].md — initial research`
- `kb: update KNOWLEDGE_STATUS.md — [genre] now covered`
- `pitfalls: add [symptom].md — user-confirmed fix`
- `research-log: [date] [topic] — attempted, failed`
