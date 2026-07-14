# Knowledge Status

This file is Claude's coverage map. Before generating a prompt, Claude checks here to identify gaps that require research. After research, Claude updates this file.

**Legend:** ✅ Well-documented | ⚠️ Partial coverage | ❌ Not documented | 🔬 Research in progress

---

## Core Knowledge

| Area | Status | Notes |
|------|--------|-------|
| Suno v5 fundamentals (prompt mechanics) | ✅ | Character limits, style block rules, lyric field rules, vocal tips |
| Metatags reference | ✅ | Full tag list, [Build]/[Drop], voice tags, placement rules, pipe syntax, energy tags, quirks |
| Slider parameters | ✅ | Weirdness, Style Influence, Audio Influence — genre matrix included |
| v4 → v5 behavioral differences | ✅ | Documented in `core/suno-v5-fundamentals.md` — song length, vocals, metatag reliability |
| v5 → v5.5 behavioral differences | ✅ | Documented in `core/suno-v5-fundamentals.md` — Voices, Custom Models, My Taste, Audio Influence change |
| v5.5 Audio Influence slider change | ✅ | Documented in `core/sliders.md` — melody bleeds at much lower values; use ≤8% for vibe-only |

---

## Genre Coverage

| Genre | Status | File | Last Updated |
|-------|--------|------|-------------|
| Happy Hardcore EDM (S3RL style) | ✅ | `genres/happy-hardcore-edm.md` | 2026-05-09 |
| Rock (classic, indie, hard, soft) | ✅ | `genres/rock.md` | 2026-05-09 |
| Metal (thrash, death, black, metalcore, power, doom) | ✅ | `genres/metal.md` | 2026-05-09 |
| Punk (classic, hardcore, pop-punk, Oi!, anarcho) | ✅ | `genres/punk.md` | 2026-05-09 |
| Alternative (grunge, post-grunge, shoegaze, emo, indie) | ✅ | `genres/alternative.md` | 2026-05-09 |
| Electronic / Dance (EDM: house, techno, trance, DnB, dubstep, future bass) | ✅ | `genres/electronic-dance.md` | 2026-05-09 |
| Ambient (drone, dark ambient, nature, space, new age) | ✅ | `genres/ambient.md` | 2026-05-09 |
| Indie (indie rock, indie pop, bedroom pop, post-punk revival, art rock) | ✅ | `genres/indie.md` | 2026-05-09 |
| Soul & Funk (classic funk, neo-soul, classic soul, deep funk) | ✅ | `genres/soul-funk.md` | 2026-05-09 |
| Country (classic, outlaw, honky-tonk, Nashville, Americana) | ✅ | `genres/country.md` | 2026-05-09 |
| Folk & Acoustic (traditional, singer-songwriter, indie folk, Celtic) | ✅ | `genres/folk-acoustic.md` | 2026-05-09 |
| Blues (Delta, Chicago, Texas, electric, blues rock) | ✅ | `genres/blues.md` | 2026-05-09 |
| Reggae / Dancehall (roots, dub, dancehall, lovers rock) | ✅ | `genres/reggae.md` | 2026-05-09 |
| Pop (mainstream, synth-pop, dance-pop, indie pop, bedroom pop) | ✅ | `genres/pop.md` | 2026-05-09 |
| Hip-Hop / Rap (trap, boom bap, lo-fi, melodic rap, cloud rap, phonk, drill) | ✅ | `genres/hip-hop.md` | 2026-05-09 |
| R&B / Soul (neo-soul, contemporary R&B, new jack swing, classic soul) | ✅ | `genres/rnb-soul.md` | 2026-05-09 |
| K-Pop (idol pop, dark concept, ballad, EDM-pop hybrid, multilingual) | ✅ | `genres/k-pop.md` | 2026-05-09 |
| Jazz (bebop, swing, cool, modal, Latin jazz, smooth, fusion) | ✅ | `genres/jazz.md` | 2026-05-09 |
| Classical (symphony, piano solo, string quartet, baroque, cinematic) | ✅ | `genres/classical.md` | 2026-05-09 |
| Latin (reggaeton, salsa, cumbia, bachata, bossa nova, tango) | ✅ | `genres/latin.md` | 2026-05-09 |

---

## Structural Techniques

| Technique | Status | Location |
|-----------|--------|---------|
| Standard verse/chorus/bridge | ✅ | `core/metatags.md` |
| Through-composed (no repeating sections) | ❌ | Needs research |
| Multi-genre transitions | ❌ | Needs research |
| Spoken word sections | ✅ | `core/metatags.md` — `[Spoken]` tag, pipe syntax, energy control for spoken intros in high-energy genres |
| Rap/sung hybrid | ⚠️ | See `core/metatags.md` — `[Rap]` tag notes |
| Long-form (5+ sections) | ❌ | Needs research |
| Instrumental sections within vocal tracks | ⚠️ | See `core/metatags.md` |

---

## Pitfall Coverage

| Symptom | Status | File |
|---------|--------|------|
| Copyright false-positive on public-domain audio | ⚠️ | `research-log/2026-07-14-fingerprint-false-positive-transforms.md` — waveform transforms (`defingerprint.py`) **tested and REJECTED by Suno**; signature of a melody / robust-neural match. Remedy = copyright dispute, not distortion. Not graduated to `pitfalls/`. |

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
| Pop | 35–50 | 65–80 | Dark pop: 40–50 / 65–75; Dance-pop: 35–45 / 70–80 | ✅ |
| Hip-Hop / Rap | 40–55 | 55–70 | Trap: 40–50; Boom bap: 45–55; Lo-fi: 50–60 / 45–60 | ✅ |
| R&B / Soul | 40–55 | 60–75 | Neo-soul: 45–55; Contemporary R&B: 40–50 | ✅ |
| K-Pop | 30–55 | 65–80 | Idol pop: 30–40 / 70–80; Dark concept: 40–55 / 65–75 | ✅ |
| Jazz | 55–70 | 50–65 | Bebop: 60–70; Smooth: 45–55; Swing: 50–60 | ✅ |
| Classical | 30–50 | 45–60 | Baroque: 30–40; Romantic: 40–50; Cinematic: 45–55 | ✅ |
| Latin | 25–45 | 60–80 | Reggaeton: 30–40; Salsa: 35–45; Bossa nova: 25–35 | ✅ |

---

## Last Full Audit

- **Date:** 2026-05-09
- **Coverage summary:** Full v5.5 audit complete. All 20 genre files verified against v5.5 behavior and version scope updated to `v5, v5.5`. `genres/k-pop.md` created (was listed in KNOWLEDGE_STATUS but file did not exist). Core files updated with v5 → v5.5 diff table, new features documentation, and Audio Influence slider behavior change. Slider × Genre Matrix completed for all 20 genres (Pop, Hip-Hop, R&B, K-Pop, Jazz, Classical, Latin rows were previously missing). Jazz and Classical genre files now listed in Genre Coverage table (were missing despite files existing).
- **Next priority:** Structural techniques (through-composed, multi-genre transitions, long-form 5+ sections).

---

## 2026-07-14 Update

- Added `defingerprint.py` — a CLI tool that transforms a public-domain recording that a fingerprinter false-positives on, so the fingerprint moves while the performance stays recognizable. Modes: `analyze` (recording-vs-melody separability diagnosis), `process` (layered pipeline at low/medium/high), `sweep` (parameter search + auto-ranking with a local proxy metric)
- Layered signal chain: coupled varispeed, decoupled micro pitch-shift, time-varying wow/flutter (primary disruptor), randomized multiband EQ, period-appropriate hiss/crackle, non-linear time-warp
- Built-in measurement harness: Shazam-style constellation fingerprint distance (want high) + chroma/melody distance (want low), so results are measurable locally instead of guessed against Suno
- Added audio deps to `requirements.txt` (numpy, scipy, soundfile, librosa; optional system binaries auto-detected)
- Created `research-log/2026-07-14-fingerprint-false-positive-transforms.md` — method, local verification results, and honest limitations (proxy ≠ Suno's matcher; melody-match ceiling; ToS/account risk)
- Pitfall Coverage: added a row for copyright false-positives on public-domain audio
- **Outcome (tested same day):** user ran the tool on their real file; all three sweep candidates were **REJECTED by Suno** despite high proxy-fingerprint distance. Waveform distortion is a dead end for this file — signature of a robust neural matcher and/or a melody/lyric match. Logged as *attempted, failed*; **nothing graduated to `pitfalls/`** (per CLAUDE.md). Correct remedy is the platform copyright dispute (leverages the file's public-domain provenance)

## 2026-05-09 Update (v5.5 Audit)

- v5.5 research: documented Voices, Custom Models, My Taste new features
- v5.5 research: documented significant Audio Influence slider behavior change (melody bleed at lower values; ≤8% sweet spot for vibe-only in v5.5)
- Updated `core/suno-v5-fundamentals.md` — added v5→v5.5 diff table, new features section, negative prompting guide; updated style block descriptor guidance from 8–15 to 4–7 tags
- Updated `core/metatags.md` — explicit v5.5 audit note confirming no tag changes between versions
- Updated `core/sliders.md` — Audio Influence behavior change documented, v5 vs v5.5 comparison table, updated zones, practical implications
- Created `research-log/` directory (was missing from initial scaffold)
- Created `research-log/2026-05-09-v5.5-changes.md` — full raw research dump
- Fixed KNOWLEDGE_STATUS: K-Pop was marked ✅ but `genres/k-pop.md` did not exist
- Created `genres/k-pop.md` — full genre file: idol pop, dark concept, ballad, EDM-pop hybrid, multilingual; [Rap Verse] forcing, [Pre-Chorus] as load-bearing tag, Korean lyrics guidance
- Audited all 20 genre files against v5.5 — version scope updated to `v5, v5.5`, v5.5 audit notes added to Known Quirks section in each file
- Completed Slider × Genre Matrix — added Pop, Hip-Hop, R&B, K-Pop, Jazz, Classical, Latin rows (7 were missing)
- Added Jazz, Classical, Latin rows to Genre Coverage table (files existed but were not listed)

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
