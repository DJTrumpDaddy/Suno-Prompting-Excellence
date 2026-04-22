#!/usr/bin/env python3
"""
Suno v5 Prompt Generator

Usage:
  python generate.py "an 80s synth ballad about a road trip with my dad"
  python generate.py --genre metal "a song about overcoming grief"
  python generate.py --list-genres
"""

import argparse
import os
import sys
from pathlib import Path

import anthropic

REPO_ROOT = Path(__file__).parent
CORE_DIR = REPO_ROOT / "core"
GENRES_DIR = REPO_ROOT / "genres"
PITFALLS_DIR = REPO_ROOT / "pitfalls"

SYSTEM_PROMPT = """You are an expert Suno v5 prompt engineer with deep knowledge of how Suno v5 interprets style blocks, metatags, slider settings, and lyric structure.

You have been given a knowledge base (KB) of research on Suno v5. Use it as your primary reference.

Your task is to produce four artifacts for a song prompt:

1. **TITLE** — The song title as it would appear in Suno
2. **STYLE BLOCK** — The style/genre/mood text fed into Suno's style field (comma-separated descriptors, ~120 chars max)
3. **LYRICS** — Full lyrics using Suno metatags ([Verse], [Chorus], [Bridge], etc.)
4. **SLIDER SETTINGS** — Recommended Suno v5 slider values with a one-line rationale for each

Before generating, audit your coverage:
- Is the requested genre well-covered in the KB?
- Are there structural requirements (unusual structure, multi-genre, spoken word) that need special handling?
- Are there known style tag conflicts for this combination?

If the KB is thin on any of these, note the gap explicitly before your output (label it GAP DETECTED:).

Format your response EXACTLY as:
---TITLE---
[title here]

---STYLE---
[style block here]

---LYRICS---
[full lyrics with metatags]

---SLIDERS---
[slider name]: [value] — [one-line rationale]
[slider name]: [value] — [one-line rationale]
...

---NOTES---
[any gaps detected, caveats, or suggestions for the user]
"""


def read_file_safe(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def load_knowledge_base(genre_hint: str | None = None) -> str:
    sections = []

    # Always load: status + fundamentals
    status = read_file_safe(REPO_ROOT / "KNOWLEDGE_STATUS.md")
    if status:
        sections.append(f"## KNOWLEDGE_STATUS\n\n{status}")

    fundamentals = read_file_safe(CORE_DIR / "suno-v5-fundamentals.md")
    if fundamentals:
        sections.append(f"## CORE: Suno v5 Fundamentals\n\n{fundamentals}")

    metatags = read_file_safe(CORE_DIR / "metatags.md")
    if metatags:
        sections.append(f"## CORE: Metatags\n\n{metatags}")

    sliders = read_file_safe(CORE_DIR / "sliders.md")
    if sliders:
        sections.append(f"## CORE: Sliders\n\n{sliders}")

    # Genre-specific file if it exists
    if genre_hint:
        genre_file = GENRES_DIR / f"{genre_hint.lower().replace(' ', '-')}.md"
        genre_content = read_file_safe(genre_file)
        if genre_content:
            sections.append(f"## GENRE: {genre_hint}\n\n{genre_content}")

    # Always load pitfalls index
    pitfalls_index = read_file_safe(PITFALLS_DIR / "_index.md")
    if pitfalls_index:
        sections.append(f"## PITFALLS INDEX\n\n{pitfalls_index}")

    return "\n\n---\n\n".join(sections)


def parse_response(text: str) -> dict:
    sections = {"title": "", "style": "", "lyrics": "", "sliders": "", "notes": ""}
    markers = {
        "---TITLE---": "title",
        "---STYLE---": "style",
        "---LYRICS---": "lyrics",
        "---SLIDERS---": "sliders",
        "---NOTES---": "notes",
    }
    current = None
    buffer = []

    for line in text.splitlines():
        stripped = line.strip()
        if stripped in markers:
            if current is not None:
                sections[current] = "\n".join(buffer).strip()
            current = markers[stripped]
            buffer = []
        elif current is not None:
            buffer.append(line)

    if current is not None:
        sections[current] = "\n".join(buffer).strip()

    return sections


def print_output(sections: dict) -> None:
    divider = "─" * 60

    print(f"\n{divider}")
    print("  TITLE")
    print(divider)
    print(sections["title"])

    print(f"\n{divider}")
    print("  STYLE BLOCK")
    print(divider)
    print(sections["style"])

    print(f"\n{divider}")
    print("  LYRICS")
    print(divider)
    print(sections["lyrics"])

    print(f"\n{divider}")
    print("  SLIDER SETTINGS")
    print(divider)
    print(sections["sliders"])

    if sections["notes"]:
        print(f"\n{divider}")
        print("  NOTES")
        print(divider)
        print(sections["notes"])

    print(f"\n{divider}\n")


def list_genres() -> None:
    files = sorted(GENRES_DIR.glob("*.md"))
    available = [f.stem for f in files if not f.stem.startswith("_")]
    if available:
        print("Available genre files:")
        for g in available:
            print(f"  {g}")
    else:
        print("No genre files yet. They are created on demand during generation.")


def generate(idea: str, genre_hint: str | None, model: str) -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    kb = load_knowledge_base(genre_hint)

    user_message = f"""Knowledge Base:\n\n{kb}\n\n---\n\nSong idea: {idea}"""
    if genre_hint:
        user_message += f"\nGenre hint: {genre_hint}"

    print(f"\nGenerating prompt for: \"{idea}\"", file=sys.stderr)
    print("Reading knowledge base...", file=sys.stderr)

    with client.messages.stream(
        model=model,
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    ) as stream:
        full_text = ""
        print("Generating", end="", flush=True, file=sys.stderr)
        for text in stream.text_stream:
            full_text += text
            print(".", end="", flush=True, file=sys.stderr)
        print(" done\n", file=sys.stderr)

    sections = parse_response(full_text)
    print_output(sections)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a Suno v5 prompt from a song idea.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("idea", nargs="?", help="Song idea description")
    parser.add_argument("--genre", "-g", help="Genre hint (loads genre-specific KB file)")
    parser.add_argument(
        "--model",
        "-m",
        default="claude-opus-4-7",
        help="Claude model to use (default: claude-opus-4-7)",
    )
    parser.add_argument("--list-genres", action="store_true", help="List available genre files")

    args = parser.parse_args()

    if args.list_genres:
        list_genres()
        return

    if not args.idea:
        parser.print_help()
        sys.exit(1)

    generate(args.idea, args.genre, args.model)


if __name__ == "__main__":
    main()
