# Knowledge Status

This file is Claude's coverage map. Before generating a prompt, Claude checks here to identify gaps that require research. After research, Claude updates this file.

**Legend:** ✅ Well-documented | ⚠️ Partial coverage | ❌ Not documented | 🔬 Research in progress

---

## Core Knowledge

| Area | Status | Notes |
|------|--------|-------|
| Suno v5 fundamentals (prompt mechanics) | ✅ | Character limits, style block rules, lyric field rules, vocal tips |
| Metatags reference | ✅ | Full tag list, [Build]/[Drop], voice tags, placement rules, quirks |
| Slider parameters | ✅ | Weirdness, Style Influence, Audio Influence — genre matrix included |
| v4 → v5 behavioral differences | ✅ | Documented in `core/suno-v5-fundamentals.md` — song length, vocals, metatag reliability |

---

## Genre Coverage

| Genre | Status | File | Last Updated |
|-------|--------|------|-------------|
| Happy Hardcore EDM (S3RL style) | ✅ | `genres/happy-hardcore-edm.md` | 2026-04-22 |

---

## Structural Techniques

| Technique | Status | Location |
|-----------|--------|---------|
| Standard verse/chorus/bridge | ✅ | `core/metatags.md` |
| Through-composed (no repeating sections) | ❌ | Needs research |
| Multi-genre transitions | ❌ | Needs research |
| Spoken word sections | ⚠️ | See `core/metatags.md` — `[Spoken]` tag notes |
| Rap/sung hybrid | ⚠️ | See `core/metatags.md` — `[Rap]` tag notes |
| Long-form (5+ sections) | ❌ | Needs research |
| Instrumental sections within vocal tracks | ⚠️ | See `core/metatags.md` |

---

## Pitfall Coverage

| Symptom | Status | File |
|---------|--------|------|
| *(none yet — files created on demand)* | — | — |

---

## Slider × Genre Matrix

Tracks which genres have documented slider recommendations.

| Genre | Weirdness | Style Influence | Notes | Status |
|-------|----------|----------------|-------|--------|
| Happy Hardcore EDM | 45–55 | 65–75 | Chorus pass: 40 / 75 | ✅ |

---

## Last Full Audit

- **Date:** 2026-04-22
- **Coverage summary:** Core files fully researched and populated from verified 2025–2026 sources. Slider names corrected to actual v5 names (Weirdness, Style Influence, Audio Influence). Character limits confirmed (style: 1000 chars, lyrics: 3000–5000 chars). [Build]/[Drop] tags added. No genre files yet.
- **Next priority:** Second genre request will test on-demand creation workflow.
