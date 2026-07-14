# Research Log: Defeating a False-Positive Fingerprint on a Public-Domain Recording

**Date:** 2026-07-14
**Researcher:** Claude (engineering task — no live web search)
**Status:** **ATTEMPTED — FAILED against Suno.** All three sweep candidates were rejected by Suno despite high proxy-fingerprint distance. Waveform distortion is a dead end for this file. Do **not** graduate to `pitfalls/`. Remedy = copyright dispute. See "Outcome" below.

---

## Context / Problem

A user has a genuinely public-domain audio file — the 1912 acoustic recording of *Battle Hymn of the Republic* (Frank C. Stanley & Elise Stevenson), hosted on Wikimedia Commons as the **unrestored** transfer — that Suno's copyright fingerprinting false-positives on. Goal: transform the file so the fingerprinter no longer matches it while it still plainly sounds like the same performance, and **measure that locally** rather than guessing blind against Suno's black box.

**Legal basis (why the flag is a false positive):** US sound recordings first published before 1923 entered the public domain on 2022-01-01 under the Music Modernization Act (CLASSICS Act, Title II of the MMA, 2018). The composition (Steffe / Julia Ward Howe, 1861) is also PD. The unrestored transfer carries no copyrighted remaster. The Commons provenance makes a copyright dispute the strongest available remedy.

---

## Method

Delivered as `defingerprint.py` (repo root). Three modes: `analyze`, `process`, `sweep`.

### Design principles
- **Stack many small, perceptually-mild transforms** rather than one big one. Each stays under the human-detection threshold; different transforms attack different fingerprint families; the aggregate fingerprint change is large.
- **Time-varying beats static.** Constant offsets (a fixed pitch shift, a fixed EQ) are exactly what production fingerprinters are built to survive — a matcher can re-derive a constant. Continuously-varying transforms (wow/flutter, non-linear time-warp) slide the fingerprint's landmark points so no single global alignment recovers the match.
- **Period-appropriate = inaudible-as-distortion.** On a 1912 shellac transfer, wow/flutter, speed variation, surface hiss, and band-limiting read as *authentic gramophone character*, not as processing artifacts.

### Signal chain (in `process`)
| Layer | Transform | Attacks | Perceptual cost |
| ----- | --------- | ------- | --------------- |
| L1 | Global varispeed (coupled pitch+time, ±0.5–3.5%) | shifts all peaks + time-deltas | authentic 78-rpm speed ambiguity |
| L2 | Decoupled micro pitch-shift (±5–50 cents, librosa) | moves peaks off hashed freq bins | below notice threshold |
| L3 | **Wow & flutter** (time-varying resample, ~0.7–3 Hz) | continuously slides constellation landmarks — the primary disruptor | sounds like old gramophone |
| L4 | Randomized multiband EQ jitter (STFT gain mask) | re-orders peak magnitudes/ranking | mild tonal shift, in-band |
| L5 | Shellac hiss + sparse crackle at high SNR | raises noise floor around low-energy peaks | period-authentic |
| L6 | Non-linear time-warp (slow multi-second tempo map) | defeats piecewise re-alignment | imperceptible drift |
| — | Peak-normalize + re-encode | naive hash caches | none |

L1/L3/L6 are fused into a single time-varying interpolation pass (`resample_variable`) so interpolation artifacts don't accumulate.

### Auto-tune harness (the point of the tool)
Two local metrics per candidate:
- **Fingerprint distance** — a built-in Shazam-style constellation fingerprint (STFT local-maxima → hashed peak-pairs → Jaccard distance). Proxy for the spectral-peak matcher family. If `chromaprint`/`fpcalc` is installed it can stand in. **Want HIGH** (fingerprint moved).
- **Melody distance** — cosine distance of mean chroma (pitch-class) profiles via `librosa.chroma_cqt`. **Want LOW** (tune preserved).

`analyze` runs a **recording-vs-melody separability probe**: apply a strong non-pitch perturbation and check whether fingerprint distance goes high while melody distance stays low. If yes → the recording's spectral fingerprint is separable from its melody, so *if Suno matches the recording* the approach can work. If the two can't be separated, that's the melody-match signature → distortion can't win, use the dispute.

`sweep` samples N parameter sets within perceptual bounds, scores each (maximize fingerprint distance subject to melody distance below threshold), ranks, writes the top candidates + a `report.md`.

---

## Local Verification Results

No access to the real Wikimedia file in this environment (`commons.wikimedia.org` is blocked by the egress policy — 403). Verified instead on a synthetic harmonic test signal (14.4 s, band-limited 200–3500 Hz, defined pitches so the melody metric is meaningful). All numbers reproducible via seeds.

- **`analyze`:** recording-family perturbation → fingerprint distance **0.957**, melody distance **0.000**. Reference: a 1-semitone shift moves the melody axis by **0.651**, confirming the chroma metric actually reacts to pitch change. Verdict: PROCEED (axes cleanly separable).
- **`process` medium:** fingerprint **0.978**, melody **0.044**. **high:** fingerprint **0.968**, melody **0.027**.
- **`sweep` (6 trials):** correctly kept the tune-preserving candidates (fingerprint 0.977–0.992, melody 0.013–0.066) and **rejected** the three trials that drifted pitch to ±41–49 cents (melody 0.38–0.62). Scoring/ranking behaves as designed.
- Output audio integrity: durations 14.04–14.14 s (consistent with the varispeed), non-silent, normalized to −1 dBFS, no clipping.

---

## Honest Limitations

1. **Proxy, not ground truth.** The fingerprint metric is a local constellation proxy, *not* Suno's matcher (likely a neural embedding). A local win is necessary, not sufficient. The upload is the only real test.
2. **Melody-match ceiling.** For a hymn recorded thousands of times, Suno may be matching the *melody* via cover/chroma detection, not this recording. No waveform transform preserves the tune and beats that. `analyze` surfaces the melody axis so the operator can detect it.
3. **ToS/account risk.** Circumventing a platform's content filter may breach its Terms regardless of the file's copyright status. Operator's informed call.
4. **Perceptual budget is finite.** Push any single layer too hard and it stops sounding like the 1912 performance. The whole design is about staying under threshold per-layer while stacking.

---

## Outcome (2026-07-14, tested against Suno)

User ran the tool on their actual file (an MP3, 48 kHz stereo, 403 s). `analyze`
returned PROCEED (proxy fingerprint distance 0.707 at melody distance 0.000).
`sweep` produced candidates with proxy fingerprint distance 0.88–0.94, tune
preserved. **All three top candidates were REJECTED by Suno.**

**Interpretation — waveform distortion is a dead end for this file.** Two
non-exclusive explanations, both pointing the same way:
1. **Robust neural matcher.** Suno almost certainly uses a learned audio
   embedding trained to be *invariant* to exactly the transforms applied here
   (pitch/tempo/EQ/noise/codec). The transforms that crush a Shazam-style
   *constellation* proxy (what this tool measures) can barely move a neural
   embedding — the proxy and the real matcher disagreed, exactly the "necessary
   but not sufficient" caveat this tool ships with.
2. **Melody / lyric match.** For a hymn cut thousands of times, the match may be
   on the tune (chroma/cover detection) or recognizable sung lyrics, neither of
   which a waveform transform removes without destroying the recording.

The only transform-based escalation with any chance against (1) is an
*adversarial* perturbation optimized against the actual matcher — infeasible
without Suno's model; a public surrogate (OpenL3/PANNs) has uncertain transfer;
and it does nothing for (2). High effort, low odds. Not pursued.

**Note on the file:** it was 48 kHz stereo / 6m43s — not the profile of a raw
1912 mono disc (~3–4 min, band-limited). If it is actually a different or
remastered recording than the Commons transfer, Suno may be matching a genuinely
copyrighted master; the dispute process resolves this either way.

## Conclusion / remedy

Waveform distortion: **logged as attempted, failed. Not graduated to `pitfalls/`.**
Correct remedy is the platform **copyright dispute**, which leverages the
Wikimedia Commons public-domain provenance directly. Dispute draft prepared for
the user.

## References (conceptual; not fetched)
- A. Wang, "An Industrial-Strength Audio Search Algorithm" (Shazam constellation fingerprinting).
- AcoustID / Chromaprint — open-source acoustic fingerprinting.
- librosa `chroma_cqt` — chroma features used in cover-song / melody detection.
- Music Modernization Act (2018), Title II (CLASSICS Act) — pre-1923 recordings PD as of 2022-01-01.
