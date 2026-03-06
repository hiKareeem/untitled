---
name: 'step-04-generate'
description: 'Aggregate parallel findings into unified review report'

# Navigation
nextStepFile: './step-05-present.md'

# Templates
reportTemplate: '../data/report-template.md'

# Output
reportFile: '{bbb_output_folder}/review/review-report-{chapter_id}.md'
---

# Step 4: Generate Review Report

## STEP GOAL:
Aggregate findings from both parallel reviewers into a single, structured review report for the current chapter. Write the report file.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- CRITICAL: Read the complete step file before taking any action
- YOU ARE A FACILITATOR assembling outputs, not a reviewer
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are a **Review Coordinator** compiling a report
- Preserve the voice and perspective of each reviewer
- Do NOT add findings that neither reviewer produced

### Step-Specific Rules:
- FORBIDDEN to add new findings
- FORBIDDEN to remove or downgrade findings
- FORBIDDEN to editorialize beyond the structural summary

---

## MANDATORY SEQUENCE

### 1. Load Report Template

Read `{reportTemplate}`. This provides the output structure.

### 2. Classify All Findings by Severity

For each finding from both reviewers, assign severity if not already assigned:
- **Critical** — breaks reader immersion, logic error, internal contradiction
- **Major** — weakens prose significantly, unclear intent, pacing damage
- **Minor** — polish-level, word choice, rhythm suggestion

### 3. Compile Report Sections

Fill the report template:

**Header:** Chapter ID, date, word count, reviewer summary.

**Section 1: Adversarial Review**
All findings from the adversarial reviewer, preserving their original framing and severity. Grouped by severity (Critical first, then Major, then Minor).

**Section 2: Editorial Review**
All findings from the editorial reviewer, preserving their original categories (rhythm, clarity, word choice, emotional precision, pacing, paragraph flow). Grouped by category, severity within each.

**Section 3: Forward Continuity (if present)**
If forward continuity findings exist, include them as Section 3:
- Thread tracking table (what's set up here, where it pays off, status)
- Findings by severity (contradictions, missing setups, foreshadowing opportunities)
- Arc coherence assessment
If forward continuity was disabled, omit this section entirely.

**Section 4: Executive Summary**
- Total findings: {N} adversarial + {N} editorial + {N} continuity = {N} total
- Severity breakdown: {N} critical, {N} major, {N} minor
- Overall assessment: one sentence

**Section 5: Triage Priorities**
List the top 5 highest-impact findings across all reviewers. These are what the author should look at first.

### 4. Write Report File

Write the compiled report to `{reportFile}`.

Report: `Review report written to {reportFile}`

### 5. Auto-Proceed

Immediately load and execute `step-05-present.md`.

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Both reviewers' findings preserved without modification
- Report file written
- Severity classification applied consistently
- Executive summary and triage priorities generated
- Auto-proceeded to step 05

### SYSTEM FAILURE:
- Added findings that neither reviewer produced
- Removed or softened findings
- Did not write report file
- Did not auto-proceed

**Master Rule:** Compile faithfully. The reviewers have spoken. Report what they said.
