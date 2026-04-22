#!/usr/bin/env python3
"""
Suno v5 Feedback Triage

Report a problem with a Suno generation and get a diagnosed fix.
Confirmed fixes are written to the KB; failed attempts are logged.

Usage:
  python feedback.py "the vocals were completely buried by the guitar"
  python feedback.py "the bridge section was never generated"
  python feedback.py --commit "the bridge was ignored" --fix "use [Bridge] not [bridge]"
"""

import argparse
import os
import sys
from datetime import date
from pathlib import Path

import anthropic

REPO_ROOT = Path(__file__).parent
CORE_DIR = REPO_ROOT / "core"
PITFALLS_DIR = REPO_ROOT / "pitfalls"
RESEARCH_LOG_DIR = REPO_ROOT / "research-log"

TRIAGE_SYSTEM_PROMPT = """You are an expert in diagnosing Suno v5 generation failures.

You have access to a knowledge base of known pitfalls. Your job is to:

1. CLASSIFY the issue:
   - Structural (section tags ignored, wrong arrangement, truncation)
   - Sonic (vocal issues, instrument bleed, mix problems)
   - Style (wrong genre feel, mood mismatch, tempo)
   - Lyrics (repeated lines, truncation, garbled words)

2. DIAGNOSE the likely root cause in Suno v5's processing

3. CHECK if this is already documented in the pitfalls index

4. PROPOSE a specific fix with example (show the before/after in the prompt)

5. EXPLAIN your reasoning — why do you believe this fix works mechanically in Suno v5?

6. ASSESS your confidence: High / Medium / Low
   - High = matches a documented pitfall pattern
   - Medium = plausible based on Suno v5 fundamentals
   - Low = speculative, needs user testing

Format your response EXACTLY as:

---CLASSIFICATION---
[Structural | Sonic | Style | Lyrics]

---ROOT_CAUSE---
[Explanation of what caused this in Suno v5]

---KNOWN_PITFALL---
[Yes: [pitfall file name] | No: this is undocumented]

---FIX---
[Specific fix with before/after example]

---REASONING---
[Why this fix works mechanically]

---CONFIDENCE---
[High | Medium | Low] — [brief justification]

---KB_ACTION---
[WRITE_TO_PITFALLS: [suggested-filename].md | LOG_AS_FAILED: [reason] | ALREADY_DOCUMENTED]
"""


def read_file_safe(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def load_triage_kb() -> str:
    sections = []

    fundamentals = read_file_safe(CORE_DIR / "suno-v5-fundamentals.md")
    if fundamentals:
        sections.append(f"## Suno v5 Fundamentals\n\n{fundamentals}")

    metatags = read_file_safe(CORE_DIR / "metatags.md")
    if metatags:
        sections.append(f"## Metatags\n\n{metatags}")

    pitfalls_index = read_file_safe(PITFALLS_DIR / "_index.md")
    if pitfalls_index:
        sections.append(f"## Pitfalls Index\n\n{pitfalls_index}")

    # Load all existing pitfall files
    for pf in sorted(PITFALLS_DIR.glob("*.md")):
        if pf.stem != "_index":
            content = read_file_safe(pf)
            if content:
                sections.append(f"## Pitfall: {pf.stem}\n\n{content}")

    return "\n\n---\n\n".join(sections)


def parse_triage_response(text: str) -> dict:
    sections = {
        "classification": "",
        "root_cause": "",
        "known_pitfall": "",
        "fix": "",
        "reasoning": "",
        "confidence": "",
        "kb_action": "",
    }
    markers = {
        "---CLASSIFICATION---": "classification",
        "---ROOT_CAUSE---": "root_cause",
        "---KNOWN_PITFALL---": "known_pitfall",
        "---FIX---": "fix",
        "---REASONING---": "reasoning",
        "---CONFIDENCE---": "confidence",
        "---KB_ACTION---": "kb_action",
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


def print_triage(issue: str, sections: dict) -> None:
    divider = "─" * 60
    print(f"\n{divider}")
    print(f"  TRIAGE: {issue[:50]}{'...' if len(issue) > 50 else ''}")
    print(divider)

    print(f"\nClassification:  {sections['classification']}")
    print(f"\nRoot Cause:\n{sections['root_cause']}")
    print(f"\nKnown Pitfall:  {sections['known_pitfall']}")
    print(f"\nProposed Fix:\n{sections['fix']}")
    print(f"\nReasoning:\n{sections['reasoning']}")
    print(f"\nConfidence:  {sections['confidence']}")
    print(f"\nKB Action:  {sections['kb_action']}")
    print(f"\n{divider}\n")

    # Prompt user
    if "WRITE_TO_PITFALLS" in sections["kb_action"]:
        print("→ If this fix works for you, run with --commit to write it to the KB.")
        print("  If it fails, run with --log-failed to record the attempt.\n")
    elif "ALREADY_DOCUMENTED" in sections["kb_action"]:
        print("→ This pitfall is already in the KB. Check the pitfalls/ directory.\n")


def commit_to_pitfalls(issue: str, fix: str, classification: str, filename: str) -> None:
    today = date.today().isoformat()
    slug = filename.replace(".md", "").lower().replace(" ", "-")
    filepath = PITFALLS_DIR / f"{slug}.md"

    content = f"""# Pitfall: {slug.replace('-', ' ').title()}

**Classification:** {classification}
**Severity:** Medium
**First documented:** {today}

## Symptom
{issue}

## Root Cause
*(to be elaborated — run `python feedback.py "{issue}"` for full diagnosis)*

## Fix
{fix}

## Prevention
*(add prevention notes here)*

## Failed Approaches
*(none yet)*

## Sources
- User-confirmed fix ({today})
"""

    if filepath.exists():
        print(f"Pitfall file already exists: {filepath}")
        print("Appending confirmation note...")
        existing = filepath.read_text()
        filepath.write_text(existing + f"\n\n---\n*Re-confirmed by user on {today}*\n")
    else:
        filepath.write_text(content)
        print(f"Written to: {filepath}")

    # Update pitfalls index
    index_path = PITFALLS_DIR / "_index.md"
    # Simple note — full index update is done manually or by Claude
    print(f"\nRemember to update pitfalls/_index.md with a row for '{slug}'")


def log_failed(issue: str, attempted_fix: str) -> None:
    today = date.today().isoformat()
    log_path = RESEARCH_LOG_DIR / f"{today}-failed-fix.md"

    entry = f"""# Failed Fix Log — {today}

## Issue Reported
{issue}

## Attempted Fix
{attempted_fix}

## Why It Failed
*(add notes here)*

## Status
Attempted, failed. Do not re-suggest this approach.
"""

    RESEARCH_LOG_DIR.mkdir(exist_ok=True)
    if log_path.exists():
        existing = log_path.read_text()
        log_path.write_text(existing + f"\n\n---\n\n{entry}")
    else:
        log_path.write_text(entry)

    print(f"Logged failed attempt to: {log_path}")


def triage(issue: str, model: str) -> dict:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    kb = load_triage_kb()

    user_message = f"Knowledge Base:\n\n{kb}\n\n---\n\nUser-reported issue: {issue}"

    print(f"\nTriaging: \"{issue}\"", file=sys.stderr)

    with client.messages.stream(
        model=model,
        max_tokens=2048,
        system=TRIAGE_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    ) as stream:
        full_text = ""
        print("Analyzing", end="", flush=True, file=sys.stderr)
        for text in stream.text_stream:
            full_text += text
            print(".", end="", flush=True, file=sys.stderr)
        print(" done\n", file=sys.stderr)

    return parse_triage_response(full_text)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Triage a Suno v5 generation problem.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("issue", help="Description of the problem you experienced")
    parser.add_argument(
        "--commit",
        metavar="FIX",
        help="Commit a confirmed fix to pitfalls/ KB (provide the fix text)",
    )
    parser.add_argument(
        "--log-failed",
        metavar="FIX",
        help="Log a failed fix attempt to research-log/",
    )
    parser.add_argument(
        "--filename",
        default="",
        help="Filename for the pitfall entry (used with --commit)",
    )
    parser.add_argument(
        "--model",
        "-m",
        default="claude-opus-4-7",
        help="Claude model (default: claude-opus-4-7)",
    )

    args = parser.parse_args()

    if args.commit:
        if not args.filename:
            # Derive a slug from the issue
            slug = args.issue[:40].lower().replace(" ", "-").replace("'", "").replace('"', "")
            import re
            slug = re.sub(r"[^a-z0-9\-]", "", slug)
        else:
            slug = args.filename
        commit_to_pitfalls(args.issue, args.commit, "Unknown", slug)
        return

    if args.log_failed:
        log_failed(args.issue, args.log_failed)
        return

    sections = triage(args.issue, args.model)
    print_triage(args.issue, sections)


if __name__ == "__main__":
    main()
