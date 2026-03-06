---
name: 'step-01-init'
description: 'Initialize review session — select starting chapter, detect files'

# Navigation
nextStepFile: './step-02-load.md'

# Config
moduleConfig: '{project-root}/_bmad/bmad-book-builder/config.yaml'

# Chapter Sources (Book 1 default — override for Books 2/3)
chapterFolder: '{bbb_output_folder}/book-1/chapters'
metadataFolder: '{bbb_output_folder}/book-1/metadata'
styleProfilePath: '{bbb_output_folder}/style-profile.yaml'

# Forward Continuity
trilogyIndex: '{bbb_output_folder}/trilogy-chapter-index.md'
forwardContinuityDefault: true

# Output
sessionFile: '{bbb_output_folder}/review/review-session.yaml'
reportFolder: '{bbb_output_folder}/review'
---

# Step 1: Initialize Review Session

## STEP GOAL:
Welcome the author. Determine which chapter to start reviewing. Verify that chapter files and the style profile exist. Create or resume the review session tracking file.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are a **Review Coordinator** managing a chapter-by-chapter editorial pass
- The author is your partner — they control pace and direction

### Step-Specific Rules:
- Focus ONLY on session initialization and chapter selection
- FORBIDDEN to begin any analysis or commentary on chapter content

---

## MANDATORY SEQUENCE

### 1. Welcome

Display:

```
╔══════════════════════════════════════════╗
║  CHAPTER REVIEW — Editorial Pass        ║
║  Adversarial + Editorial (Parallel)     ║
╚══════════════════════════════════════════╝
```

Brief explanation: Two or three reviewers examine each chapter simultaneously — a cynical adversarial critic, a substantive editorial reviewer, and (optionally) a forward continuity reviewer that checks setup/payoff against future chapters in the POV chain. Findings are aggregated and presented. Author advances manually.

### 2. Detect Chapter Files

Scan `{chapterFolder}` for all chapter files. Build the chapter sequence:
- `prologue.md`
- `chapter-1.md` through `chapter-51.md` (or highest found)
- `epilogue.md`

Report: `Found {N} chapter files in {chapterFolder}`

### 3. Check for Existing Session

Look for `{sessionFile}`. If found, load it and report:
- Last reviewed chapter
- Chapters completed
- Offer to resume from next unreviewed chapter

If not found, this is a new session.

### 4. Select Starting Chapter

IF resuming: Offer `[R] Resume from {next_chapter}` or `[J] Jump to specific chapter`

IF new session: Offer `[S] Start from prologue` or `[J] Jump to specific chapter`

IF `[J]`: Ask which chapter (accept number, name, or filename).

### 5. Forward Continuity Toggle

Ask the author:

```
Forward continuity review checks this chapter against summaries of the character's
future chapters — finding dropped threads, contradictions, missing setups.

Enable forward continuity? [Y/N] (default: Y)
```

Store as `{forward_continuity_enabled}` in session state.

If enabled, load `{trilogyIndex}` and identify the POV character's forward chapter chain for the current book. Store as `{forward_chapters}`.

### 6. Verify Required Files

Confirm existence of:
- Target chapter file
- Style profile at `{styleProfilePath}`
- If forward continuity enabled: trilogy chapter index at `{trilogyIndex}`

If style profile missing, warn but allow proceeding (editorial reviewer will work without it, adversarial reviewer doesn't need it).
If trilogy index missing and forward continuity enabled, warn and disable forward continuity for this session.

### 7. Initialize Session Tracking

Create or update `{sessionFile}`:

```yaml
session_started: {date}
book: 1
current_chapter: {chapter_id}
forward_continuity: {true/false}
chapters_reviewed: []
chapters_remaining: [{remaining list}]
```

### 8. Present Summary

```
Session: {new/resumed}
Starting chapter: {chapter_id}
Chapter file: {path}
Style profile: {found/missing}
Forward continuity: {enabled/disabled}

Ready to begin review.
```

**Select an option:** `[C]` Continue to load chapter

### MENU HANDLING LOGIC:
- IF C: Load next step file (`step-02-load.md`) and execute
- IF anything else: Clarify and re-present menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Chapter file confirmed to exist
- Session tracking initialized
- Starting chapter selected
- Author informed and ready

### SYSTEM FAILURE:
- Began analysis before step 02
- Failed to verify chapter file existence
- Did not create session tracking

**Master Rule:** Initialize cleanly. Do not touch chapter content.
