# Suno v5 Prompt Engineering — Knowledge Base

This repository is a self-improving knowledge base for generating high-quality Suno v5 prompts using Claude. It is actively maintained by Claude: knowledge gaps are detected before each generation run, researched, and written back here.

---

## How Claude Uses This Repo

Every time a user submits a song idea, Claude:

1. **Reads** `KNOWLEDGE_STATUS.md` to assess coverage for the request's genre, structure, and techniques
2. **Detects gaps** — if coverage is thin or absent, runs targeted web research before generating
3. **Generates** four artifacts: Title, Style block, Lyrics with metatags, Slider settings
4. **Improves** — when users report issues, Claude diagnoses, researches, and writes confirmed fixes into `pitfalls/`; failed experiments go to `research-log/` so they aren't repeated

---

## Directory Structure

```
/
├── README.md                    # This file
├── KNOWLEDGE_STATUS.md          # Coverage map — what's solid vs. thin
│
├── core/
│   ├── suno-v5-fundamentals.md  # How Suno v5 interprets prompts, slider behavior
│   ├── metatags.md              # Full metatag reference + known quirks
│   └── sliders.md               # Slider parameter guide with genre context
│
├── genres/                      # One file per genre (created on demand)
│   ├── _template.md             # Template for new genre files
│   └── [genre].md
│
├── pitfalls/                    # Failure modes, indexed by symptom
│   ├── _index.md                # Symptom → file lookup
│   └── [symptom].md
│
├── examples/                    # Rated prompt examples
│   ├── _index.md
│   └── [song-slug].md
│
└── research-log/                # Raw research dumps (pre-distillation)
    └── YYYY-MM-DD-[topic].md
```

---

## Files Claude Loads Every Session

| File | Purpose |
|------|---------|
| `KNOWLEDGE_STATUS.md` | Fast gap detection — what's covered, what's thin |
| `core/suno-v5-fundamentals.md` | Always-loaded base layer for prompt mechanics |
| `genres/[genre].md` | Loaded per-request when genre matches |
| `pitfalls/_index.md` | Consulted when user reports an issue |

---

## Scope

All content is scoped to **Suno v5**. If a finding applies to an earlier version, it is labeled explicitly (e.g., `[v4 only]`). Version differences that affect prompting behavior are documented in `core/suno-v5-fundamentals.md`.

---

## Contributing / Updating

Claude updates this repo autonomously as part of its workflow. Manual edits are welcome — if you add findings, update `KNOWLEDGE_STATUS.md` to reflect the new coverage.
