# Suno v5 Slider Parameters

> **Status:** Researched and verified — 2026-04-22
> **Scope:** Suno v5 and v5.5. Slider names differ from v4.

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

| Range | Behavior |
|-------|----------|
| 20–40 | Loose texture reference — only general mood/vibe |
| 41–60 | Moderate influence — direction without copying |
| 61–75 | Strong lead-vocal or style match |
| 76–100 | Very tight match; risks sounding like a cover |

**Use cases:**
- Lead vocal upload: 60–75
- Texture/mood reference: 20–40
- Style clone attempt: 70–85 (with legal/ethical care)

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
| Using Audio Influence > 75 without a clear reference | Output sounds like a cover rather than an original |

---

## Sources

- JackRighteous — "How to: Suno's Advanced Sliders (Weirdness, Style & Audio Influence)"
- JackRighteous — "Creative Control Sliders in Suno v5"
- Suno official help — "How to Use: Creative Sliders"
- HookGenius — "Suno v5 Complete Guide" (2026)
- Research compiled 2026-04-22
