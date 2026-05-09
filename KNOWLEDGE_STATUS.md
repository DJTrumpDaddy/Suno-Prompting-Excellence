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
| Rock (classic, indie, hard, soft) | ✅ | `genres/rock.md` | 2026-04-26 |
| Metal (thrash, death, black, metalcore, power, doom) | ✅ | `genres/metal.md` | 2026-04-26 |
| Punk (classic, hardcore, pop-punk, Oi!, anarcho) | ✅ | `genres/punk.md` | 2026-04-26 |
| Alternative (grunge, post-grunge, shoegaze, emo, indie) | ✅ | `genres/alternative.md` | 2026-04-26 |
| Electronic / Dance (EDM: house, techno, trance, DnB, dubstep, future bass) | ✅ | `genres/electronic-dance.md` | 2026-04-26 |
| Ambient (drone, dark ambient, nature, space, new age) | ✅ | `genres/ambient.md` | 2026-04-26 |
| Indie (indie rock, indie pop, bedroom pop, post-punk revival, art rock) | ✅ | `genres/indie.md` | 2026-04-26 |
| Soul & Funk (classic funk, neo-soul, classic soul, deep funk) | ✅ | `genres/soul-funk.md` | 2026-04-26 |
| Country (classic, outlaw, honky-tonk, Nashville, Americana) | ✅ | `genres/country.md` | 2026-04-26 |
| Folk & Acoustic (traditional, singer-songwriter, indie folk, Celtic) | ✅ | `genres/folk-acoustic.md` | 2026-04-26 |
| Blues (Delta, Chicago, Texas, electric, blues rock) | ✅ | `genres/blues.md` | 2026-04-26 |
| Reggae / Dancehall (roots, dub, dancehall, lovers rock) | ✅ | `genres/reggae.md` | 2026-04-26 |
| Pop (mainstream, synth-pop, dance-pop, indie pop, bedroom pop) | ✅ | `genres/pop.md` | 2026-04-26 |
| Hip-Hop / Rap (trap, boom bap, lo-fi, melodic rap, cloud rap, phonk, drill) | ✅ | `genres/hip-hop.md` | 2026-04-26 |
| R&B / Soul (neo-soul, contemporary R&B, new jack swing, classic soul) | ✅ | `genres/rnb-soul.md` | 2026-04-26 |
| K-Pop (idol pop, dark concept, ballad, EDM-pop hybrid, multilingual) | ❌ | `genres/k-pop.md` | *(file missing — to be created)* |

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
| Rock (classic/hard) | 30–45 | 60–75 | Hard rock pass: 35 / 70; Indie pass: 50 / 58 | ✅ |
| Metal | 25–40 | 70–85 | Death/black: 25 / 80; Metalcore: 40 / 70 | ✅ |
| Punk (classic/hardcore) | 30–45 | 65–78 | Classic: 35 / 75; Pop-punk: 45 / 62 | ✅ |
| Alternative | 40–55 | 58–72 | Grunge: 40 / 70; Shoegaze: 55 / 60 | ✅ |
| Electronic / Dance (EDM) | 20–40 | 60–80 | House: 25/70; DnB: 30/75; Dubstep: 25/80 | ✅ |
| Ambient | 45–65 | 30–50 | Higher Weirdness = more unusual texture | ✅ |
| Indie | 25–50 | 40–65 | Bedroom pop: 40–50; Post-punk: 20–30 | ✅ |
| Soul & Funk | 20–40 | 55–75 | Classic funk: 20–30; Neo-soul: 35–45 | ✅ |
| Country | 15–25 | 60–75 | Outlaw/Americana: 25; Nashville pop: 20 | ✅ |
| Folk & Acoustic | 10–20 | 65–80 | Traditional: 10–15; Indie folk: 15–20 | ✅ |
| Blues | 20–35 | 60–75 | Delta: 20–25; Chicago: 25–30; Blues rock: 30–35 | ✅ |
| Reggae / Dancehall | 25–40 | 65–80 | Roots: 25–30; Dub: 35–40; Dancehall: 30–35 | ✅ |

---

## Last Full Audit

- **Date:** 2026-04-26
- **Coverage summary:** Core files fully researched. 9 genre files now populated. Batch session added: electronic-dance, ambient, indie, soul-funk — all with full style tags, quirks, slider settings, and lyrics skeletons sourced from 2026 research.
- **Next priority:** Structural techniques (through-composed, multi-genre transitions, long-form).

## 2026-04-26 Update

- Added `genres/rock.md` — covers classic rock, indie rock, hard rock, soft rock; [Guitar Solo] tag guidance, era-cue technique, 2 full lyric skeletons
- Added `genres/metal.md` — covers thrash, death, black, metalcore, power metal, doom/sludge; harsh vocal prompting, double-kick tag, breakdown metatag, 2 full lyric skeletons
- Added `genres/punk.md` — covers classic punk, hardcore, pop-punk, Oi!, anarcho; anti-polish technique, BPM enforcement, gang vocals, 2 full lyric skeletons
- Added `genres/alternative.md` — covers grunge, post-grunge, shoegaze, emo, indie alt; loud-quiet-loud dynamic encoding, shoegaze wall-of-sound technique, 2 full lyric skeletons
- Updated Slider × Genre Matrix with all 4 new genres

## 2026-04-26 Update (batch 2)

- Added `genres/country.md` — classic, outlaw, honky-tonk, Nashville, Americana; pedal steel / fiddle forcing technique, twang vocal stack, 2 full lyric skeletons
- Added `genres/folk-acoustic.md` — traditional folk, singer-songwriter, indie folk, Celtic; exclusion-prompting guide, production restraint techniques, 2 full lyric skeletons
- Added `genres/blues.md` — Delta, Chicago, Texas, blues rock; 12-bar structural prompt, AAB lyric form, harmonica forcing technique, 2 full lyric skeletons
- Added `genres/reggae.md` — roots, dub, dancehall, lovers rock; offbeat skank forcing technique, one-drop drum pattern tag, dub echo stack, 2 full lyric skeletons
- Updated Slider x Genre Matrix with all 4 new genres
