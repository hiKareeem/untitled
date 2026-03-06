# Review Workflow Specification

> **Status:** Active — v2.0 (upgraded from placeholder)
> **Module:** bmad-book-builder
> **Last Updated:** 2026-03-06

---

## Purpose

Post-hoc chapter-by-chapter review of completed manuscript prose. Two parallel review perspectives — **Adversarial** (cynical critic finding weaknesses) and **Editorial** (prose quality, clarity, polish) — run simultaneously via subagents. Findings are aggregated into a unified report per chapter. Author advances to the next chapter manually.

This workflow is designed for the current project phase: **all chapters are written**. Continuity, character consistency, style compliance, and thematic tracking were handled during the chapter-write workflow (steps 04/05) and are not repeated here. This review focuses on what a fresh reader and a hostile critic would find.

---

## Architecture

### Execution Model: Parallel Subagents

Step 03 dispatches **two or three subagents simultaneously** using the Task tool:

1. **Adversarial Reviewer** — receives only the chapter text and the adversarial review procedure. No project context. Finds >=10 issues with the prose as if encountering it cold. Derived from `review-adversarial-general.xml`.

2. **Editorial Reviewer** — receives the chapter text plus the style profile and the editorial review procedure. Assesses prose quality: sentence rhythm, word choice, clarity, emotional precision, pacing within scenes, paragraph-level flow. Not a copyeditor — a substantive editor.

3. **Forward Continuity Reviewer** (optional, default ON) — receives the chapter text, the POV character name, and metadata summaries for all future chapters in that character's POV chain. Checks: setups without payoffs, dropped threads, contradictions with future developments, missing foreshadowing, arc coherence. Uses chapter metadata YAML files (~1500 tokens each) rather than full chapter text to manage context.

All run in parallel via Task tool subagents. If parallel dispatch unavailable, run sequentially with persona adoption.

### Chapter Progression: Manual

After reviewing findings for a chapter, the author chooses:
- **[N] Next Chapter** — advance to next chapter in sequence
- **[R] Re-review** — re-run analysis on current chapter (e.g., after making edits)
- **[F] Toggle Forward Continuity** — enable/disable the forward continuity reviewer
- **[Q] Quit** — end the review session

There is no automatic advancement. The author controls pace.

### Chapter Sequence

Default order: `prologue`, `chapter-1` through `chapter-51`, `epilogue`. The workflow tracks current position and offers the next in sequence. Author can override and jump to any chapter.

---

## Steps (Create Mode)

| Step | File | Purpose |
|------|------|---------|
| 01 | `step-01-init.md` | Welcome, select starting chapter, detect files |
| 02 | `step-02-load.md` | Load chapter content + style profile |
| 03 | `step-03-analyze.md` | Dispatch parallel subagents (adversarial + editorial) |
| 04 | `step-04-generate.md` | Aggregate findings into review report |
| 05 | `step-05-present.md` | Present findings, manual chapter advancement |

Step 05 loops back to Step 02 when the author selects [N] Next Chapter or [R] Re-review.

---

## Agents

| Agent | Role | Context Given |
|-------|------|---------------|
| Adversarial Reviewer | Cynical critic, finds weaknesses | Chapter text only |
| Editorial Reviewer | Substantive editor, prose quality | Chapter text + style profile |
| Forward Continuity Reviewer | Forward setup/payoff checker | Chapter text + forward POV chapter metadata |

The adversarial and editorial reviewers receive no bible data, character dossiers, or worldbuilding references. The forward continuity reviewer receives metadata summaries (not full text) of the character's future chapters.

---

## Output

- **Per-chapter report:** `{bbb_output_folder}/review/review-report-{chapter_id}.md`
- **Session tracking:** `{bbb_output_folder}/review/review-session.yaml` (tracks which chapters have been reviewed, current position)

### Issue Severity

- **Critical** — breaks reader immersion, logic error, contradicts what the text itself establishes
- **Major** — weakens the prose significantly, unclear intent, pacing damage
- **Minor** — polish-level, word choice, rhythm suggestion

---

## Triggering

Invoked manually via `/review` or equivalent. Not auto-triggered. This is an author-driven editorial pass.

---

## Dependencies

- Chapter files in `{bbb_output_folder}/book-{N}/chapters/`
- Chapter metadata in `{bbb_output_folder}/book-{N}/metadata/` (for forward continuity)
- Trilogy chapter index at `{bbb_output_folder}/trilogy-chapter-index.md` (for forward continuity)
- Style profile at `{bbb_output_folder}/style-profile.yaml`
- Subagent/Task tool capability for parallel dispatch

---

## Data Files

| File | Purpose |
|------|---------|
| `data/report-template.md` | Output template for per-chapter reports |
| `data/analysis-procedures/adversarial-review.md` | Subagent prompt for adversarial reviewer |
| `data/analysis-procedures/editorial-review.md` | Subagent prompt for editorial reviewer |
| `data/analysis-procedures/forward-continuity-review.md` | Subagent prompt for forward continuity reviewer |
| `data/classification-rules/severity-classification.md` | Issue severity definitions |
