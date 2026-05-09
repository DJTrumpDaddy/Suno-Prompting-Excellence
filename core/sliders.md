# Suno v5 Slider Parameters

> **Status:** Researched and verified — 2026-05-09
> **Scope:** Suno v5 and v5.5. Slider names differ from v4.
> **v5.5 audit (2026-05-09):** Weirdness and Style Influence unchanged. Audio Influence behavior changed significantly — see dedicated v5.5 section below.

---

## Overview

Suno v5 exposes three creative control sliders. They **control behavior, not quality** — they shape how closely the AI follows your prompt vs. how freely it deviates.

**Starting point for any new song:** Weirdness ~50, Style Influence ~60. Then adjust one at a time.

---

## The Three Sliders

### Weirdness (0–100)
**Question it answers:** *"How far can this drift from expected structure?"*

Controls novelty and surprise in melody, rhythm, phrasing, and arrangement. Higher values introduce unexpected turns; lower values produce predictable, genre-typical results.

| Range | Behavior |
|-------|----------|
| 0–30 | Very safe, predictable; stays tightly in the genre lane |
| 31–50 | Neutral baseline; slight natural variation |
| 51–70 | Noticeable melodic/rhythmic deviation; interesting but sometimes inconsistent |
| 71–100 | Experimental, chaotic; structures may break down |

**Genre guidance:**
- Classical, acoustic, worship: 25–45
- Pop, R&B: 35–50
- Hip-hop/trap: 40–55
- Synthwave, electronic: 50–65
- Ambient, experimental: 70–85

### Style Influence (0–100)
**Question it answers:** *"How tightly should the output stay in the lane I described?"*

Controls loyalty to your style block. Higher values = more genre-faithful output. Too high = less useful variation across multiple generations.

| Range | Behavior |
|-------|----------|
| 0–30 | Loosely follows style; large drift possible |
| 31–55 | Moderate — allows natural variation within the genre |
| 56–80 | Strong adherence to your style block |
| 81–100 | Very tight; can reduce interesting variation |

**Genre guidance:**
- Radio Pop: 65–80
- Worship/Gospel: 70–85
- Hip-hop/Trap: 55–70
- Orchestral: 45–60
- Ambient/Experimental: 35–55

### Audio Influence (0–100)
**Only available when you upload a reference audio clip.**

**Question it answers:** *"How strongly should the uploaded source lead?"*

Controls how closely Suno follows an uploaded audio reference (melody, style, or vocal character).

> **⚠️ v5.5 behavior change:** Audio Influence behaves significantly differently in v5.5 vs v5. The zones below reflect the v5.5 model. See the v5.5 notes section for details.

**v5.5 zones (updated):**

| Range | Behavior |
|-------|----------|
| 0–5% | Almost kills melodic influence; vibe only |
| 8% | Practical sweet spot — vibe extraction without melody bleed |
| 15–25% | Faint trace of motif |
| 20–30% | Picks up original melody fairly firmly |
| 40% | Recommended for voice cloning (preserves vocal character) |
| 50%+ | Remix/Mashup territory |
| 70%+ | Near cover feel |
| 76–100% | Very tight match; sounds like a cover |

**Use cases (v5.5):**
- Vibe/mood extraction only: 0–8%
- Faint stylistic influence: 10–20%
- Voice cloning with Voices feature: ~40%
- Strong style match: 60–70% (caution: melody will bleed)
- Cover/mashup intent: 75%+

---

## Slider × Genre Quick Reference

| Genre | Weirdness | Style Influence | Notes |
|-------|----------|----------------|-------|
| Radio Pop | 35–50 | 65–80 | Stability and punch for chorus |
| Hip-hop / Trap | 40–55 | 55–70 | Some drift adds flow feel |
| R&B / Soul | 40–55 | 60–75 | High style keeps vocal lane |
| Worship / Gospel | 25–40 | 70–85 | Very faithful, emotional |
| Metal | 45–60 | 55–70 | Some weirdness for riff variation |
| Lo-fi Hip-hop | 50–65 | 40–60 | Lower style = chillhop drift |
| Synthwave | 50–65 | 55–70 | Mid weirdness for retro drift |
| Classical / Orchestral | 30–50 | 45–60 | Lower weirdness for structure |
| Acoustic Folk | 35–50 | 55–70 | Straightforward |
| Ambient | 65–80 | 35–55 | High weirdness defines the genre |
| EDM / House | 45–60 | 55–70 | Build/drop contrast matters more |
| Jazz | 55–70 | 50–65 | Weirdness supports improv feel |

---

## Practical Tips

- **Change one slider at a time** and compare the same 20–30 seconds of output
- **For chorus stability:** lower Weirdness (35–45), raise Style Influence (70–85)
- **For verse exploration:** raise Weirdness slightly, lower Style Influence slightly
- **A drop only feels big if the build was thinner** — this is a structural issue, not a slider one
- **Sliders don't fix structural problems** — if Suno ignores a section, that's a metatag issue, not a Weirdness issue

---

## Common Slider Mistakes

| Mistake | Why It's Wrong |
|---------|---------------|
| Max Weirdness for all genres | Destroys genre identity; output sounds chaotic |
| Max Style Influence always | Reduces variation; every generation sounds the same |
| Lowering Weirdness to fix a structural issue | Sliders don't control structure; use metatags instead |
| Not adjusting sliders between verse and chorus edits | Chorus needs more stability (lower Weirdness) than verse |
| Using Audio Influence > 20 expecting vibe-only in v5.5 | v5.5 picks up melody much earlier — use ≤8% for vibe-only |
| Using 20–40% Audio Influence as "safe zone" in v5.5 | This was the v5 safe zone; in v5.5 it picks up the original melody firmly |

---

## v5.5 Slider Notes

> Research date: 2026-05-09

### Weirdness — Unchanged
No behavioral change in v5.5. All genre recommendations in the Slider × Genre table remain valid.

### Style Influence — Unchanged
No behavioral change in v5.5. All genre recommendations remain valid.

### Audio Influence — Significant Change in v5.5

**What changed:** Before v5.5, Audio Influence (also called "Inspo") functioned as a vibe extractor — mid-range settings (20–40%) would pull the mood, groove, and texture of a reference while generating original chord progressions and melodies. In v5.5, the model "locks onto" the original melody at much lower slider values, behaving more like a Remix tool.

**v5 vs v5.5 comparison:**

| Slider Value | v5 Behavior | v5.5 Behavior |
|-------------|-------------|---------------|
| 0–5% | No influence | No influence (unchanged) |
| 8% | Near-zero influence | Practical sweet spot for pure vibe |
| 20–30% | Loose vibe extraction (safe zone) | Picks up original melody firmly |
| 40–60% | Moderate style match | Remix/Mashup territory |
| 61–75% | Strong style/vocal match | Near cover feel |
| 76–100% | Cover risk | Cover (unchanged) |

**Practical implications:**
- **For vibe extraction:** Use 0–8% in v5.5 (was 20–40% in v5)
- **For voice cloning with Voices:** Use ~40% to preserve vocal character
- **Avoid the "risky midrange":** 20–50% in v5.5 blends vibe extraction with unwanted melody lock-on
- **If using Inspo playlists:** Curate the playlist carefully; v5.5 is less forgiving of melodic references in the source

---

## Sources

- JackRighteous — "How to: Suno's Advanced Sliders (Weirdness, Style & Audio Influence)"
- JackRighteous — "Creative Control Sliders in Suno v5"
- Suno official help — "How to Use: Creative Sliders"
- HookGenius — "Suno v5 Complete Guide" (2026)
- GenX Notes — "Suno v5.5 Inspo feels more like Remix now — and how I deal with it" (2026)
- GenX Notes — "What do the Weirdness, Style Influence, and Audio Influence sliders do in Suno?" (2026)
- Research compiled 2026-04-22; v5.5 Audio Influence section added 2026-05-09
