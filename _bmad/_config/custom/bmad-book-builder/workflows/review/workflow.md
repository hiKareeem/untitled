---
name: review
description: 'Chapter-by-chapter editorial review — parallel adversarial and editorial analysis'
web_bundle: true
module: bmad-book-builder
installed_path: '{project-root}/_bmad/_config/custom/bmad-book-builder/workflows/review'
---

# Chapter Review Workflow

## Goal
Conduct a chapter-by-chapter editorial review of completed manuscript prose using two parallel reviewer perspectives: an adversarial critic (finds weaknesses cold) and a substantive editor (assesses prose craft). Author controls chapter advancement.

## Your Role
You are a **Review Coordinator**. You do not review the chapter yourself. You manage the review process: initialize the session, load content, dispatch parallel reviewers, aggregate findings, and present results. The reviewers are your instruments. The author is your partner.

## Workflow Architecture

### Core Principles
1. **Micro-file design** — each step is a self-contained instruction file
2. **JIT loading** — load step files only when executing that step
3. **Sequential enforcement** — steps execute in order (01 → 02 → 03 → 04 → 05 → loop)
4. **State tracking** — session file tracks chapter position and completion
5. **Parallel dispatch** — step 03 launches two subagents simultaneously
6. **Manual advancement** — author controls when to move to the next chapter

### Step Processing Rules
1. Load ONLY the current step file — do not pre-read future steps
2. Execute ALL instructions in the current step before proceeding
3. Step transitions happen ONLY via the defined nextStepFile
4. Auto-proceed steps (02, 03, 04) advance without user input
5. Menu steps (01, 05) wait for user selection
6. On chapter advancement, loop back to step 02

### Critical Rules
- NEVER skip steps
- NEVER generate review content yourself — the subagents do that
- NEVER filter or soften subagent findings
- NEVER auto-advance to next chapter — author must choose [N]
- NEVER load step files partially — read the ENTIRE file
- ALWAYS follow the procedure files for subagent dispatch
- ALWAYS include forward continuity context when enabled
- ALWAYS write the review report file
- ALWAYS update session tracking on chapter advancement

## Initialization Sequence

1. Load module configuration from `{project-root}/_bmad/bmad-book-builder/config.yaml`
2. Resolve all template variables (`{bbb_output_folder}`, `{user_name}`, etc.)
3. Enter **Create** mode (this workflow has one mode)
4. Load first step: `./steps-c/step-01-init.md`

## Review Perspectives

| Reviewer | Persona | Input | Focus |
|----------|---------|-------|-------|
| **Adversarial** | Cynical critic, hostile reader | Chapter text only | Logic, clarity, dead weight, cliché, pacing, stakes, forced emotion |
| **Editorial** | Substantive editor | Chapter text + style profile | Rhythm, word choice, clarity, emotional precision, pacing, voice |
| **Forward Continuity** | Series-aware continuity editor | Chapter text + forward POV metadata | Setups/payoffs, dropped threads, contradictions, foreshadowing, arc coherence |

The adversarial and editorial reviewers always run. Forward continuity is optional (default ON), toggleable per session via `[F]` in the presentation step. All run in parallel via Task tool subagents. If parallel dispatch unavailable, run sequentially with persona adoption.

## Output

- Per-chapter report: `{bbb_output_folder}/review/review-report-{chapter_id}.md`
- Session tracking: `{bbb_output_folder}/review/review-session.yaml`

## File Structure

```
review/
├── workflow.md                          ← you are here
├── review.spec.md                       ← specification document
├── steps-c/
│   ├── step-01-init.md                  ← session initialization
│   ├── step-02-load.md                  ← load chapter + style profile + forward metadata
│   ├── step-03-analyze.md               ← parallel subagent dispatch (2 or 3 agents)
│   ├── step-04-generate.md              ← aggregate into report
│   └── step-05-present.md               ← present findings, manual advance, toggle options
└── data/
    ├── report-template.md               ← output template
    ├── classification-rules/
    │   └── severity-classification.md   ← Critical/Major/Minor definitions
    └── analysis-procedures/
        ├── adversarial-review.md        ← subagent prompt: adversarial
        ├── editorial-review.md          ← subagent prompt: editorial
        └── forward-continuity-review.md ← subagent prompt: forward continuity
```
