---
name: 'step-03-analyze'
description: 'Dispatch parallel subagent reviews — adversarial, editorial, and optionally forward continuity'

# Navigation
nextStepFile: './step-04-generate.md'

# Subagent Procedures
adversarialProcedure: '../data/analysis-procedures/adversarial-review.md'
editorialProcedure: '../data/analysis-procedures/editorial-review.md'
forwardContinuityProcedure: '../data/analysis-procedures/forward-continuity-review.md'
---

# Step 3: Parallel Review Analysis

## STEP GOAL:
Dispatch review subagents simultaneously using the Task tool. The Adversarial Reviewer and Editorial Reviewer always run. If forward continuity is enabled, the Forward Continuity Reviewer runs as a third parallel subagent. Collect all result sets and pass to step 04 for aggregation.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- CRITICAL: Read the complete step file before taking any action
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread. Run all reviews SEQUENTIALLY in your main context if parallel dispatch is unavailable.

### Role Reinforcement:
- You are a **Review Coordinator** dispatching specialist reviewers
- You do NOT review the chapter yourself
- You ONLY collect and forward results

### Step-Specific Rules:
- FORBIDDEN to add your own review opinions
- FORBIDDEN to filter or soften subagent findings
- All subagents MUST receive the analysis procedure file content as their primary instructions

---

## MANDATORY SEQUENCE

### 1. Load Analysis Procedures

Read procedure files:
- `{adversarialProcedure}` — instructions for the adversarial reviewer
- `{editorialProcedure}` — instructions for the editorial reviewer
- IF `{forward_continuity_enabled}`: `{forwardContinuityProcedure}` — instructions for the forward continuity reviewer

### 2. Dispatch Parallel Subagents

Launch **all** Task tool calls in a **single message** (parallel execution):

#### Subagent A: Adversarial Reviewer
- **Type:** `general`
- **Prompt:** Combine the adversarial procedure file content with the chapter text. The procedure file IS the complete instruction set — do not add framing beyond providing the chapter content.
- **Input:** Chapter text ONLY. No style profile. No project context.
- **Expected output:** Structured markdown list of >=10 findings with severity ratings.

#### Subagent B: Editorial Reviewer
- **Type:** `general`
- **Prompt:** Combine the editorial procedure file content with the chapter text AND the style profile. The procedure file IS the complete instruction set.
- **Input:** Chapter text + style profile.
- **Expected output:** Structured markdown list of findings organized by category (rhythm, clarity, word choice, emotional precision, pacing, paragraph flow).

#### Subagent C: Forward Continuity Reviewer (ONLY if `{forward_continuity_enabled}`)
- **Type:** `general`
- **Prompt:** Combine the forward continuity procedure file content with: (1) the chapter text, (2) the POV character name, (3) the forward chapter metadata. The procedure file IS the complete instruction set.
- **Input:** Chapter text + POV character name + forward POV chain list + all forward chapter metadata YAML summaries.
- **Expected output:** Structured markdown with thread tracking table, findings by severity, and arc coherence assessment.

**CRITICAL:** All Task calls MUST be in the same message to enable parallel execution. If forward continuity is disabled, only dispatch Subagents A and B.

### 3. Collect Results

Wait for all subagents to return. Store results as:
- `{adversarial_findings}` — raw output from Subagent A
- `{editorial_findings}` — raw output from Subagent B
- `{continuity_findings}` — raw output from Subagent C (if dispatched)

### 4. Fallback: Sequential Execution

IF the Task tool is unavailable or parallel dispatch fails:

1. First, adopt the adversarial reviewer persona. Read the adversarial procedure file. Review the chapter text following those instructions exactly. Produce the adversarial findings.
2. Then, adopt the editorial reviewer persona. Read the editorial procedure file. Review the chapter text + style profile following those instructions exactly. Produce the editorial findings.
3. IF forward continuity enabled: adopt the forward continuity reviewer persona. Read the forward continuity procedure file. Review the chapter text + forward metadata following those instructions exactly. Produce the continuity findings.

The output format must match what the subagents would produce.

### 5. Auto-Proceed

Display:

```
Review complete.
- Adversarial: {N} findings
- Editorial: {N} findings
- Forward Continuity: {N} findings / disabled

Generating report...
```

Immediately load and execute `step-04-generate.md`.

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Both reviews completed (parallel or sequential fallback)
- Findings collected without editorial filtering
- Procedure files were loaded and followed
- Auto-proceeded to step 04

### SYSTEM FAILURE:
- Added own review opinions beyond subagent output
- Filtered or softened findings
- Only ran one reviewer
- Did not follow procedure files

**Master Rule:** Dispatch. Collect. Do not editorialize.
