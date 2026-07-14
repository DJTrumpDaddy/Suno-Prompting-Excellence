#!/usr/bin/env python3
"""
Fingerprint-resistant transform for a public-domain recording.

Takes an audio file whose copyright is genuinely clear (e.g. a pre-1923 US
recording, public domain under the Music Modernization Act) but which an
acoustic fingerprinter false-positives on, and produces a version that still
plainly sounds like the same performance while its spectral fingerprint has
moved. It measures its own work with a local proxy so you are not guessing
blind against a black-box matcher.

Usage:
  python defingerprint.py analyze input.ogg
  python defingerprint.py process input.ogg --out out.wav --intensity medium
  python defingerprint.py sweep input.ogg --out-dir candidates --trials 10

Modes:
  analyze  Diagnose whether the recording's spectral fingerprint separates
           from its melody, and print baseline proxy metrics. No audio out.
  process  Apply the layered pipeline once at a low/medium/high preset.
  sweep    Generate N candidates, score each, and rank the best-sounding ones
           that move the fingerprint most. Writes files + report.md.

HONEST LIMITATIONS (read these):
  * The local fingerprint metric is a Shazam-style CONSTELLATION PROXY, not
    Suno's actual matcher. A local win does not guarantee a Suno win. The
    upload is the only ground truth.
  * If Suno matches the MELODY of the piece (cover/chroma detection) rather
    than this specific recording, no waveform transform can both preserve the
    tune and defeat the match. `analyze` reports the melody axis so you can
    see this; if candidates keep getting flagged, that is the signature, and
    the remedy is the platform's copyright dispute, not more distortion.
  * Circumventing a platform's content filter may breach its Terms of Service
    regardless of the file's copyright status. That is the operator's call.
"""

import argparse
import sys
from pathlib import Path

try:
    import numpy as np
    from scipy import ndimage
    from scipy import signal as sp_signal
    import soundfile as sf
except ImportError as exc:  # pragma: no cover - environment guard
    print(
        f"ERROR: missing a required audio dependency ({exc.name}).\n"
        "Install them with:  pip install -r requirements.txt",
        file=sys.stderr,
    )
    sys.exit(1)

try:
    import librosa

    HAVE_LIBROSA = True
except ImportError:
    HAVE_LIBROSA = False

REPO_ROOT = Path(__file__).parent

# Analysis constants (shared so both files land on the same time/freq grid).
ANALYSIS_SR = 22050
FP_NPERSEG = 1024
FP_HOP = 512
FP_PEAK_NEIGHBORHOOD = 20
FP_PEAK_PERCENTILE = 99.5
FP_MAX_PEAKS = 12000
FP_FAN = 6
FP_DT_MAX = 50

# Verdict thresholds for the `analyze` step (against the local proxy).
FP_SEPARABLE = 0.45  # proxy fingerprint distance we want to clear
CHROMA_TUNE_OK = 0.08  # melody distance below which the tune reads as intact


# --------------------------------------------------------------------------- #
# Audio I/O
# --------------------------------------------------------------------------- #
def load_audio(path: str) -> tuple[np.ndarray, int]:
    try:
        data, sr = sf.read(path, dtype="float64", always_2d=True)
    except Exception:  # noqa: BLE001 - fall back to librosa's decoders
        if not HAVE_LIBROSA:
            raise
        y, sr = librosa.load(path, sr=None, mono=True)
        return y.astype(np.float64), int(sr)
    mono = data.mean(axis=1)  # collapse to mono
    return mono, int(sr)


def save_audio(path: str, x: np.ndarray, sr: int) -> None:
    ext = Path(path).suffix.lower()
    if ext == ".ogg":
        sf.write(path, x, sr, format="OGG", subtype="VORBIS")
    elif ext == ".flac":
        sf.write(path, x, sr, format="FLAC", subtype="PCM_16")
    else:
        sf.write(path, x, sr, subtype="FLOAT")


# --------------------------------------------------------------------------- #
# Transform layers
# --------------------------------------------------------------------------- #
def _smooth_curve(n: int, sr: int, comps: list[tuple[float, float]], rng) -> np.ndarray:
    """A smooth [-1, 1] modulation built from a few low-frequency sines."""
    t = np.arange(n) / sr
    curve = np.zeros(n)
    for freq, amp in comps:
        phase = rng.uniform(0.0, 2.0 * np.pi)
        curve += amp * np.sin(2.0 * np.pi * freq * t + phase)
    peak = np.max(np.abs(curve))
    return curve / peak if peak > 0 else curve


def resample_variable(x: np.ndarray, base_speed: float, mod: np.ndarray | None) -> np.ndarray:
    """Resample with a time-varying rate: couples L1 varispeed, L3 wow/flutter,
    and L6 non-linear warp into a single interpolation pass."""
    n_in = len(x)
    n_out = int(round(n_in / base_speed))
    if mod is None:
        mod = np.zeros(n_out)
    elif len(mod) != n_out:
        mod = np.interp(np.linspace(0, len(mod) - 1, n_out), np.arange(len(mod)), mod)
    speed = np.maximum(base_speed * (1.0 + mod), 1e-6)
    pos = np.cumsum(speed)
    pos -= pos[0]  # start reading from sample 0
    pos = pos[pos <= (n_in - 1)]
    return np.interp(pos, np.arange(n_in), x)


def pitch_shift_cents(x: np.ndarray, sr: int, cents: float) -> np.ndarray:
    """Decoupled micro pitch shift (L2). Needs librosa; a no-op without it."""
    if not HAVE_LIBROSA or abs(cents) < 1e-6:
        return x
    shifted = librosa.effects.pitch_shift(
        y=x.astype(np.float32), sr=sr, n_steps=cents / 100.0, bins_per_octave=12
    )
    return shifted.astype(np.float64)


def eq_jitter(x: np.ndarray, sr: int, rng, max_db: float, n_bands: int) -> np.ndarray:
    """Mild randomized multiband EQ (L4): re-orders spectral peak magnitudes."""
    f, _, z = sp_signal.stft(x, fs=sr, nperseg=2048, noverlap=1536)
    n_freq = z.shape[0]
    centers = np.linspace(0, n_freq - 1, n_bands)
    band_gains_db = rng.uniform(-max_db, max_db, size=n_bands)
    gain_db = np.interp(np.arange(n_freq), centers, band_gains_db)
    z *= (10.0 ** (gain_db / 20.0))[:, None]
    _, y = sp_signal.istft(z, fs=sr, nperseg=2048, noverlap=1536)
    if len(y) >= len(x):
        return y[: len(x)]
    return np.pad(y, (0, len(x) - len(y)))


def add_period_noise(
    x: np.ndarray, sr: int, rng, hiss_snr_db: float, crackle_rate: float
) -> np.ndarray:
    """Period-appropriate shellac hiss + sparse crackle (L5) at high SNR."""
    n = len(x)
    rms = np.sqrt(np.mean(x**2)) + 1e-12

    hiss = rng.standard_normal(n)
    hb, ha = sp_signal.butter(2, 1500.0 / (sr / 2), btype="high")
    hiss = sp_signal.lfilter(hb, ha, hiss)
    hiss *= (rms * 10.0 ** (-hiss_snr_db / 20.0)) / (np.sqrt(np.mean(hiss**2)) + 1e-12)
    y = x + hiss

    if crackle_rate > 0:
        n_pops = int(crackle_rate * (n / sr))
        if n_pops > 0:
            idx = rng.integers(0, n, size=n_pops)
            sign = rng.integers(0, 2, size=n_pops) * 2 - 1
            amps = rng.uniform(0.2, 1.0, size=n_pops) * rms * 0.5 * sign
            pops = np.zeros(n)
            pops[idx] = amps
            lb, la = sp_signal.butter(2, 4000.0 / (sr / 2), btype="low")
            y = y + sp_signal.lfilter(lb, la, pops)
    return y


def normalize(x: np.ndarray, peak_db: float = -1.0) -> np.ndarray:
    peak = np.max(np.abs(x)) + 1e-12
    return x * (10.0 ** (peak_db / 20.0) / peak)


def process(x: np.ndarray, sr: int, params: dict) -> np.ndarray:
    """Run the full layered pipeline for one parameter set (deterministic)."""
    rng = np.random.default_rng(params["seed"])

    y = pitch_shift_cents(x, sr, params["pitch_cents"])  # L2

    n_out = int(round(len(y) / params["base_speed"]))
    wow = _smooth_curve(n_out, sr, params["wow_comps"], rng) * params["wow_depth"]
    warp = _smooth_curve(n_out, sr, params["warp_comps"], rng) * params["warp_depth"]
    y = resample_variable(y, params["base_speed"], wow + warp)  # L1 + L3 + L6

    y = eq_jitter(y, sr, rng, params["eq_max_db"], params["eq_bands"])  # L4
    y = add_period_noise(y, sr, rng, params["hiss_snr_db"], params["crackle_rate"])  # L5
    return normalize(y)  # re-encode/normalize happens on save


# --------------------------------------------------------------------------- #
# Parameter presets
# --------------------------------------------------------------------------- #
_WOW_COMPS = [(0.7, 1.0), (1.3, 0.6), (3.1, 0.3)]
_WARP_COMPS = [(0.05, 1.0), (0.09, 0.5)]


def _signed(rng, lo: float, hi: float) -> float:
    """A magnitude in [lo, hi] with a random sign — used for speed/pitch."""
    return rng.uniform(lo, hi) * (1 if rng.integers(0, 2) else -1)


def preset_params(intensity: str, seed: int, rng) -> dict:
    table = {
        "low": dict(spd=0.015, cents=15.0, wow=0.002, warp=0.003, eq=1.5, bands=5, snr=42.0, crk=1.0),
        "medium": dict(spd=0.025, cents=30.0, wow=0.004, warp=0.005, eq=2.5, bands=6, snr=36.0, crk=3.0),
        "high": dict(spd=0.035, cents=50.0, wow=0.006, warp=0.008, eq=3.5, bands=7, snr=30.0, crk=6.0),
    }
    p = table[intensity]
    return dict(
        base_speed=1.0 + _signed(rng, 0.005, p["spd"]),
        pitch_cents=_signed(rng, 5.0, p["cents"]),
        wow_depth=p["wow"],
        wow_comps=_WOW_COMPS,
        warp_depth=p["warp"],
        warp_comps=_WARP_COMPS,
        eq_max_db=p["eq"],
        eq_bands=p["bands"],
        hiss_snr_db=p["snr"],
        crackle_rate=p["crk"],
        seed=seed,
    )


def random_params(seed: int, rng) -> dict:
    """Sample within perceptual bounds for a sweep trial."""
    return dict(
        base_speed=1.0 + _signed(rng, 0.005, 0.035),
        pitch_cents=_signed(rng, 5.0, 50.0),
        wow_depth=rng.uniform(0.002, 0.007),
        wow_comps=_WOW_COMPS,
        warp_depth=rng.uniform(0.003, 0.009),
        warp_comps=_WARP_COMPS,
        eq_max_db=rng.uniform(1.5, 3.5),
        eq_bands=int(rng.integers(5, 8)),
        hiss_snr_db=rng.uniform(30.0, 42.0),
        crackle_rate=rng.uniform(1.0, 6.0),
        seed=seed,
    )


def recording_family_params(seed: int, rng) -> dict:
    """A perturbation that hits the SPECTRAL fingerprint hard while leaving the
    melody (pitch content) essentially untouched — the Step-0 separability probe."""
    return dict(
        base_speed=1.0,  # no tempo/pitch change from resampling rate
        pitch_cents=0.0,  # no pitch shift -> chroma preserved
        wow_depth=0.0015,  # tiny wobble only
        wow_comps=_WOW_COMPS,
        warp_depth=0.004,
        warp_comps=_WARP_COMPS,
        eq_max_db=3.5,
        eq_bands=7,
        hiss_snr_db=32.0,
        crackle_rate=5.0,
        seed=seed,
    )


# --------------------------------------------------------------------------- #
# Measurement harness: constellation fingerprint + chroma/melody
# --------------------------------------------------------------------------- #
def _to_analysis(x: np.ndarray, sr: int) -> np.ndarray:
    if sr == ANALYSIS_SR:
        return x
    n_new = int(round(len(x) * ANALYSIS_SR / sr))
    return sp_signal.resample(x, n_new)


def constellation_hashes(x: np.ndarray, sr: int) -> set:
    """A compact Shazam-style landmark fingerprint (local proxy for the
    spectral-peak matcher family)."""
    xa = _to_analysis(x, sr)
    _, _, z = sp_signal.stft(xa, fs=ANALYSIS_SR, nperseg=FP_NPERSEG, noverlap=FP_HOP)
    s_db = 20.0 * np.log10(np.abs(z) + 1e-6)

    local_max = ndimage.maximum_filter(s_db, size=(FP_PEAK_NEIGHBORHOOD, FP_PEAK_NEIGHBORHOOD))
    peaks = (s_db == local_max) & (s_db > np.percentile(s_db, FP_PEAK_PERCENTILE))
    fbins, tbins = np.where(peaks)
    if len(fbins) == 0:
        return set()

    if len(fbins) > FP_MAX_PEAKS:  # keep the strongest to bound cost
        strongest = np.argsort(s_db[fbins, tbins])[-FP_MAX_PEAKS:]
        fbins, tbins = fbins[strongest], tbins[strongest]

    order = np.argsort(tbins)  # sort by time so we can break on dt
    fbins, tbins = fbins[order], tbins[order]

    hashes: set = set()
    for i in range(len(tbins)):
        f1, t1 = int(fbins[i]), int(tbins[i])
        pairs = 0
        for j in range(i + 1, len(tbins)):
            dt = int(tbins[j]) - t1
            if dt <= 0:
                continue
            if dt > FP_DT_MAX:
                break
            hashes.add((f1 // 2, int(fbins[j]) // 2, dt))
            pairs += 1
            if pairs >= FP_FAN:
                break
    return hashes


def fingerprint_distance(hashes_a: set, hashes_b: set) -> float:
    """Jaccard distance in [0, 1]; higher = fingerprint moved more (good)."""
    if not hashes_a and not hashes_b:
        return 0.0
    union = len(hashes_a | hashes_b)
    return 1.0 - (len(hashes_a & hashes_b) / union) if union else 0.0


def mean_chroma(x: np.ndarray, sr: int) -> np.ndarray:
    if HAVE_LIBROSA:
        chroma = librosa.feature.chroma_cqt(y=x.astype(np.float32), sr=sr)
        vec = chroma.mean(axis=1)
    else:
        vec = _chroma_fallback(x, sr)
    norm = np.linalg.norm(vec) + 1e-12
    return vec / norm


def _chroma_fallback(x: np.ndarray, sr: int) -> np.ndarray:
    f, _, z = sp_signal.stft(x, fs=sr, nperseg=4096, noverlap=3072)
    mag = np.abs(z).mean(axis=1)
    chroma = np.zeros(12)
    for i, freq in enumerate(f):
        if freq < 50.0 or freq > 5000.0:
            continue
        pitch_class = int(round(69 + 12 * np.log2(freq / 440.0))) % 12
        chroma[pitch_class] += mag[i]
    return chroma


def chroma_distance(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
    """Cosine distance of pitch-class profiles; higher = tune moved (bad)."""
    return float(1.0 - np.dot(vec_a, vec_b))


# --------------------------------------------------------------------------- #
# Modes
# --------------------------------------------------------------------------- #
def analyze(path: str) -> None:
    print(f"Loading {path} ...", file=sys.stderr)
    x, sr = load_audio(path)
    dur = len(x) / sr
    print(f"Loaded {dur:.1f}s @ {sr} Hz mono.", file=sys.stderr)
    if not HAVE_LIBROSA:
        print("NOTE: librosa not installed - pitch shift disabled, chroma uses a fallback.",
              file=sys.stderr)

    h_orig = constellation_hashes(x, sr)
    v_orig = mean_chroma(x, sr)
    print(f"Baseline: {len(h_orig)} fingerprint landmarks.", file=sys.stderr)

    print("Probing recording-vs-melody separability ...", file=sys.stderr)
    rng = np.random.default_rng(0)
    probe = process(x, sr, recording_family_params(0, rng))
    fp = fingerprint_distance(h_orig, constellation_hashes(probe, sr))
    ch = chroma_distance(v_orig, mean_chroma(probe, sr))

    # Reference: what a whole-semitone shift costs the melody axis (if available).
    ref_line = ""
    if HAVE_LIBROSA:
        semis = pitch_shift_cents(x, sr, 100.0)
        ch_ref = chroma_distance(v_orig, mean_chroma(semis, sr))
        ref_line = f"  (reference: a 1-semitone shift moves the melody axis by {ch_ref:.3f})"

    separable = fp >= FP_SEPARABLE and ch <= CHROMA_TUNE_OK

    print("\n" + "=" * 64)
    print("  DIAGNOSIS  (local proxy — not Suno's matcher)")
    print("=" * 64)
    print(f"  Fingerprint distance under recording-family perturbation : {fp:.3f}")
    print(f"    -> want HIGH (fingerprint moved).  threshold {FP_SEPARABLE:.2f}")
    print(f"  Melody distance under the same perturbation              : {ch:.3f}")
    print(f"    -> want LOW (tune preserved).       threshold {CHROMA_TUNE_OK:.2f}")
    if ref_line:
        print(ref_line)
    print("-" * 64)
    if separable:
        print("  VERDICT: PROCEED.  The recording's spectral fingerprint separates")
        print("  cleanly from its melody against the proxy. If Suno is matching THIS")
        print("  RECORDING, `sweep` can likely move it while keeping the tune. Test")
        print("  candidates on Suno for ground truth.")
    else:
        print("  VERDICT: CAUTION.  Could not move the proxy fingerprint without also")
        print("  disturbing the melody. If Suno is matching the MELODY of the piece,")
        print("  waveform distortion cannot win without wrecking the tune — the")
        print("  copyright dispute is the route (your Commons provenance is decisive).")
    print("=" * 64 + "\n")


def run_process(path: str, out: str, intensity: str, seed: int) -> None:
    print(f"Loading {path} ...", file=sys.stderr)
    x, sr = load_audio(path)
    rng = np.random.default_rng(seed)
    params = preset_params(intensity, seed, rng)
    print(f"Processing at intensity={intensity}, seed={seed} ...", file=sys.stderr)
    y = process(x, sr, params)

    h_orig = constellation_hashes(x, sr)
    fp = fingerprint_distance(h_orig, constellation_hashes(y, sr))
    ch = chroma_distance(mean_chroma(x, sr), mean_chroma(y, sr))
    save_audio(out, y, sr)

    print(f"\nWrote {out}")
    print(f"  fingerprint distance (want high): {fp:.3f}")
    print(f"  melody distance      (want low) : {ch:.3f}")
    if ch > CHROMA_TUNE_OK:
        print("  WARNING: melody distance is high - the tune may sound altered.")


def run_sweep(path: str, out_dir: str, trials: int, seed: int) -> None:
    print(f"Loading {path} ...", file=sys.stderr)
    x, sr = load_audio(path)
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    print("Fingerprinting original ...", file=sys.stderr)
    h_orig = constellation_hashes(x, sr)
    v_orig = mean_chroma(x, sr)

    results = []
    for i in range(trials):
        trial_seed = seed + i
        rng = np.random.default_rng(trial_seed)
        params = random_params(trial_seed, rng)
        y = process(x, sr, params)
        fp = fingerprint_distance(h_orig, constellation_hashes(y, sr))
        ch = chroma_distance(v_orig, mean_chroma(y, sr))
        kept = ch <= CHROMA_TUNE_OK
        score = fp - (0.0 if kept else 5.0 * (ch - CHROMA_TUNE_OK))
        results.append(dict(seed=trial_seed, params=params, fp=fp, ch=ch, score=score, kept=kept))
        print(f"  trial {i + 1}/{trials}: fp={fp:.3f} melody={ch:.3f} {'ok' if kept else 'HIGH'}",
              file=sys.stderr)

    results.sort(key=lambda r: r["score"], reverse=True)
    top = [r for r in results if r["kept"]][:3] or results[:3]
    for rank, r in enumerate(top, start=1):
        cand_path = out_path / f"candidate_{rank}_seed{r['seed']}.wav"
        save_audio(str(cand_path), process(x, sr, r["params"]), sr)
        r["file"] = cand_path.name

    _write_sweep_report(out_path, path, results, top)

    print(f"\nWrote {len(top)} ranked candidate(s) to {out_dir}/ and report.md")
    print(f"{'rank':<5}{'file':<32}{'fp(want hi)':<13}{'melody(want lo)'}")
    for rank, r in enumerate(top, start=1):
        print(f"{rank:<5}{r['file']:<32}{r['fp']:<13.3f}{r['ch']:.3f}")
    print("\nA/B the top candidates by ear, then upload the best to Suno (ground truth).")


def _write_sweep_report(out_path: Path, src: str, results: list[dict], top: list[dict]) -> None:
    lines = [
        "# Fingerprint sweep report",
        "",
        f"**Source:** `{src}`  ",
        f"**Trials:** {len(results)}  ",
        "**Objective:** maximize fingerprint distance (proxy, want high) while keeping",
        f"melody distance below {CHROMA_TUNE_OK} (tune preserved).",
        "",
        "> The fingerprint metric is a local constellation proxy, not Suno's matcher.",
        "> A high score here is necessary, not sufficient — verify by uploading.",
        "",
        "## Ranked candidates written",
        "",
        "| rank | file | fingerprint (want high) | melody (want low) |",
        "| ---- | ---- | ----------------------- | ----------------- |",
    ]
    for rank, r in enumerate(top, start=1):
        lines.append(f"| {rank} | `{r.get('file', '-')}` | {r['fp']:.3f} | {r['ch']:.3f} |")
    lines += ["", "## All trials", "",
              "| seed | fingerprint | melody | kept | base_speed | pitch(cents) |",
              "| ---- | ----------- | ------ | ---- | ---------- | ------------ |"]
    for r in results:
        p = r["params"]
        lines.append(
            f"| {r['seed']} | {r['fp']:.3f} | {r['ch']:.3f} | {'yes' if r['kept'] else 'no'} "
            f"| {p['base_speed']:.4f} | {p['pitch_cents']:+.1f} |"
        )
    (out_path / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Transform a public-domain recording to move its fingerprint.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = parser.add_subparsers(dest="mode", required=True)

    p_analyze = sub.add_parser("analyze", help="Diagnose separability + baseline metrics")
    p_analyze.add_argument("input", help="Input audio file")

    p_process = sub.add_parser("process", help="Apply the pipeline once at a preset")
    p_process.add_argument("input", help="Input audio file")
    p_process.add_argument("--out", "-o", required=True, help="Output audio file")
    p_process.add_argument("--intensity", "-i", default="medium",
                           choices=["low", "medium", "high"], help="Transform strength")
    p_process.add_argument("--seed", "-s", type=int, default=0, help="RNG seed (reproducible)")

    p_sweep = sub.add_parser("sweep", help="Search candidates and rank by the harness")
    p_sweep.add_argument("input", help="Input audio file")
    p_sweep.add_argument("--out-dir", "-o", required=True, help="Directory for candidates")
    p_sweep.add_argument("--trials", "-t", type=int, default=10, help="Number of candidates")
    p_sweep.add_argument("--seed", "-s", type=int, default=0, help="Base RNG seed")

    args = parser.parse_args()
    if args.mode == "analyze":
        analyze(args.input)
    elif args.mode == "process":
        run_process(args.input, args.out, args.intensity, args.seed)
    elif args.mode == "sweep":
        run_sweep(args.input, args.out_dir, args.trials, args.seed)


if __name__ == "__main__":
    main()
