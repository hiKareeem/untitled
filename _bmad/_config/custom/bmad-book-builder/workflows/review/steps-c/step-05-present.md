---
name: 'step-05-present'
description: 'Present findings to author, manual chapter advancement'

# Navigation (loops back)
loadStepFile: './step-02-load.md'

# Session
sessionFile: '{bbb_output_folder}/review/review-session.yaml'
---

# Step 5: Present Findings & Advance

## STEP GOAL:
Present the review report to the author. Highlight the most important findings. Offer options to advance to the next chapter, re-review the current chapter, or end the session.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- CRITICAL: Read the complete step file before taking any action
- YOU ARE A FACILITATOR presenting results
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are a **Review Coordinator** presenting results
- The author decides what to do with findings
- Do NOT advocate for or against specific changes

### Step-Specific Rules:
- Focus ONLY on presentation and navigation
- FORBIDDEN to begin editing chapter content
- FORBIDDEN to dismiss or minimize findings

---

## MANDATORY SEQUENCE

### 1. Present Executive Summary

Display the executive summary from the report:

```
╔══════════════════════════════════════════╗
║  Review: {chapter_id}                   ║
║  {total} findings ({critical}C {major}M {minor}m) ║
╚══════════════════════════════════════════╝

{one-sentence overall assessment}
```

### 2. Present Triage Priorities

Display the top 5 highest-impact findings from the report. For each:
- Severity tag
- Source (Adversarial/Editorial)
- Finding summary
- Location in chapter (line reference or section)

### 3. Offer Full Report Access

```
Full report: {reportFile}
```

Offer to display the full adversarial section, full editorial section, or both on request.

### 4. Present Navigation Menu

```
What next?

[N] Next chapter ({next_chapter_id})
[R] Re-review {current_chapter_id} (re-run all reviewers)
[J] Jump to a different chapter
[F] Toggle forward continuity (currently: {enabled/disabled})
[Q] End review session
```

### 5. Menu Handling Logic

**IF [N] Next Chapter:**
1. Update `{sessionFile}`: add current chapter to `chapters_reviewed`, set `current_chapter` to next
2. Report: `Advancing to {next_chapter_id}...`
3. Load and execute `step-02-load.md` with the new chapter

**IF [R] Re-review:**
1. Report: `Re-reviewing {current_chapter_id}...`
2. Load and execute `step-02-load.md` with the same chapter

**IF [J] Jump:**
1. Ask which chapter (accept number, name, or filename)
2. Update `{sessionFile}`: set `current_chapter` to target
3. Load and execute `step-02-load.md` with the target chapter

**IF [F] Toggle Forward Continuity:**
1. Flip `{forward_continuity_enabled}` in session state
2. Update `{sessionFile}`
3. Report: `Forward continuity: {now enabled/now disabled}`
4. Re-present menu

**IF [Q] Quit:**
1. Update `{sessionFile}`: mark session paused, record timestamp
2. Display session summary:
   - Chapters reviewed this session: {list}
   - Total findings generated: {count}
   - Reports written: {list of files}
3. Display: `Session saved. Resume anytime with /review.`
4. End workflow.

**IF anything else:**
Clarify and re-present menu.

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Executive summary and triage priorities presented clearly
- Full report accessible on request
- Navigation options presented
- Session tracking updated on advancement
- Clean loop back to step 02 on advancement

### SYSTEM FAILURE:
- Began editing chapter content
- Auto-advanced without author input
- Did not update session tracking
- Lost chapter position state

**Master Rule:** Present. Wait. The author drives.
