---
description: Extract Suno-related findings from a "Suno Prompts" project conversation and commit the right updates to the knowledge base repo.
allowed-tools: Read Write Edit Bash WebSearch
argument-hint: [path/to/exported-conversation.txt or paste conversation content]
---

You are performing a knowledge base update from conversation content exported or copied from the **"Suno Prompts"** claude.ai project. Your job is to extract every KB-worthy finding, classify it correctly, write it to the right file, and commit.

---

## Step 1 — Load Current KB State

Read these files before doing anything else so you know what's already documented:

@KNOWLEDGE_STATUS.md

Existing genre files:
!`ls genres/ 2>/dev/null | grep -v '_template'`

Existing pitfall files:
!`ls pitfalls/ 2>/dev/null | grep -v '_index'`

Recent KB commits (to avoid duplicating work already committed):
!`git log --oneline -15`

---

## Step 2 — Get the Conversation Content

**If `$ARGUMENTS` is a file path** → read it with the Read tool.
**If `$ARGUMENTS` is raw pasted text** → use it directly as the source.
**If `$ARGUMENTS` is empty** → ask the user:
> "Please paste the conversation content from your Suno Prompts project, or provide a path to an exported conversation file. You can copy multiple sessions together — I'll process them all."

---

## Step 3 — Scan for Findings

Read the provided content carefully. For each finding you identify, note:
- What type it is (see taxonomy below)
- What the exact evidence is (quote the signal phrase)
- What KB action it warrants

### Finding Taxonomy

#### Type A — Confirmed Fix
**Signals:** User explicitly said the fix worked: *"that fixed it", "perfect", "worked!", "yes that's it",* or any unambiguous positive confirmation after testing a proposed remedy.
**Action:** Write to `pitfalls/[symptom-slug].md` (use template from `pitfalls/_index.md`). Add a row to `pitfalls/_index.md`. Update `KNOWLEDGE_STATUS.md`.
**⚠️ Rule:** If there's any ambiguity — user said "seems better" or didn't report back — treat as Type B instead.

#### Type B — Attempted Fix (Outcome Unknown or Failed)
**Signals:** A fix was proposed but user didn't confirm, or user reported it didn't help.
**Action:** Write to `research-log/YYYY-MM-DD-[topic].md` with status "attempted, unconfirmed" or "attempted, failed". Never write these to `pitfalls/`.

#### Type C — New Reported Issue (No Fix Yet)
**Signals:** User describes a generation problem with no proposed or confirmed fix: *"Suno ignored the bridge", "vocals were buried", "the style felt wrong"*.
**Action:** Add a row to `pitfalls/_index.md` marked "not yet documented". Write a stub to `pitfalls/[symptom-slug].md` with the Symptom section filled but Fix left blank.

#### Type D — Gap Detection
**Signals:** A genre was requested that has no `genres/[genre].md` file, Claude flagged thin KB coverage, or an undocumented structural technique (through-composed, multi-genre transitions, 5+ sections) came up.
**Action:**
- For missing genre: run a targeted `WebSearch` for `"[genre] Suno v5 prompt guide"`, then create `genres/[genre].md` using `@genres/_template.md` as the base. Update `KNOWLEDGE_STATUS.md` genre table.
- For structural technique: research and add to the appropriate `core/` file or a new genre file.

#### Type E — Generation Feedback / Style Notes
**Signals:** Notes on what worked or didn't in a specific prompt: *"the style block nailed it", "next time add X to the style block", "slider at 70 was too high for this genre"*, slider values confirmed or revised, style tag combinations observed to work.
**Action:**
- Genre-specific findings → update or create `genres/[genre].md`
- Slider observations → update `genres/[genre].md` slider section
- If the full prompt + outcome is rated/noted → add to `examples/[song-slug].md` and `examples/_index.md`

#### Type F — General KB Improvement
**Signals:** A metatag behaved unexpectedly, a character limit was hit, a v5 mechanic was observed that isn't documented.
**Action:** Update the relevant `core/` file. Note the finding and its source date.

---

## Step 4 — Write the Updates

Process all findings in priority order: D (gaps), A (confirmed fixes), C (new issues), E (generation feedback), B (failed attempts), F (general).

For each write:
- Check the target file exists before creating it (don't overwrite existing content — append or update in place)
- Use `YYYY-MM-DD` = today's date in all file headers and log entries
- Keep the existing file structure from templates

After all writes, update `KNOWLEDGE_STATUS.md`:
- Add any new genre rows to the Genre Coverage table
- Add any new pitfall rows to Pitfall Coverage
- Update the "Last Full Audit" section with today's date and a one-line summary

---

## Step 5 — Commit and Push

Stage and commit all changed files with an appropriate message. Use these prefixes:

```
kb: add genres/[genre].md — initial research
kb: update genres/[genre].md — [what changed]
pitfalls: add [symptom].md — user-confirmed fix
pitfalls: update _index.md — [N] new entries
research-log: [date] [topic] — attempted, [outcome]
kb: update KNOWLEDGE_STATUS.md — [summary]
examples: add [slug].md — [rating]
```

If multiple file types changed, list them in the commit body.

Then push:
```bash
git push
```

---

## Step 6 — Report to User

Show a brief summary:

```
KB Update Summary
─────────────────────────────
Findings extracted:    N
  Confirmed fixes:     N  → pitfalls/
  New issues logged:   N  → pitfalls/_index.md
  Gaps researched:     N  → genres/
  Generation notes:    N  → genres/ or examples/
  Failed attempts:     N  → research-log/
  Skipped (already documented): N

Files written/updated:
  [list of files]

Commit: [message]
```

If any finding was skipped, explain why in one line.
