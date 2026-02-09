# Workflow Specification: ChapterWrite

**Module:** bmad-book-builder
**Status:** Placeholder — To be created via create-workflow workflow
**Created:** 2026-01-24

---

## Workflow Overview

**Goal:** Write a complete chapter in author's authentic voice

**Description:** Chapter Writer references style profile, story bible, chapter plan, and previous chapters to generate a complete chapter (3000-6000 words) that maintains continuity and authentic voice.

**Workflow Type:** Create-only

---

## Workflow Structure

### Entry Point

```yaml
---
name: chapter-write
description: Write individual chapters maintaining continuity and voice
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/chapter-write'
---
```

### Mode

- [ ] Create-only (steps-c/)
- [X] Tri-modal (steps-c/, steps-e/, steps-v/)

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Load Context | Load style profile, bible, chapter plan, previous chapters |
| 2 | Chapter Brief | Review what this chapter must accomplish (from plan) |
| 3 | Draft | Generate chapter content following plan, matching voice |
| 4 | Self-Review | Check against plan, bible, style profile |
| 5 | User Review | User reads, provides feedback |
| 6 | Revise | Make user-requested changes |
| 7 | Finalize | Lock chapter, update tracking files |

---

## Workflow Inputs

### Required Inputs

- Chapter number
- Chapter plan (from Foundation)
- Style profile (from StyleCapture)
- Story bible (from Character Keeper)

### Optional Inputs

- Previous chapters (for continuity)
- Thematic context (from Thematic Weaver)
- Rhythm guidelines (from Rhythm Monitor)

---

## Workflow Outputs

### Output Format

- [X] Document-producing
- [ ] Non-document

### Output Files

- `chapters/chapter-{N}.md` — Complete chapter text
- `chapters/chapter-{N}-meta.yaml` — Chapter metadata (word count, POV, timeline)

---

## Agent Integration

### Primary Agent

**Chapter Writer** — generates content, manages revision loop

### Other Agents Referenced

- Style Coach (style profile reference)
- Character Keeper (bible reference)
- Continuity Editor (review integration)

---

## Automatic Workflow Triggers

> **🎯 AUTOMATIC CONNECTIONS — Following dependency analysis**
>
> Once the chapter is finalized, this workflow **automatically triggers** tracking workflows to ensure project coherence.

### After Chapter Finalization (Step 7)

When a chapter is completed and locked, automatically trigger:

| Workflow | Purpose | Trigger Condition |
|----------|---------|-------------------|
| **Review** | Validate coherence and quality before finalizing | **Always triggered (first priority)** |
| **Bible-Update** | Extract new info (chronology, characters, locations, objects) | Always triggered |
| **Character-Audit** | Verify psychological coherence for each character in chapter | If characters appear in chapter |
| **Theme-Tracker** | Track thematic advancement in this chapter | Always triggered |
| **Rhythm-Analysis** | Analyze pacing and tension of completed chapter | Always triggered |

### Implementation of Automatic Triggers

In Step 7 (Finalize), after locking the chapter:

```yaml
Step 7: Finalize
  Actions:
    - Lock chapter file
    - Update chapter metadata
    - TRIGGER: Bible-Update workflow
    - TRIGGER: Character-Audit workflow (for each character present)
    - TRIGGER: Theme-Tracker workflow
    - TRIGGER: Rhythm-Analysis workflow
    - Present summary of triggered workflows to user
    - User can choose to run triggers immediately or defer
```

### User Choice Flow

After chapter finalization, present to user:

```
📝 Chapter XX finalized!

Workflows automatically triggered:
✅ Review — Validate coherence and quality (RECOMMENDED FIRST)
✅ Bible-Update — Update the narrative bible
✅ Character-Audit — Verify character coherence (X characters present)
✅ Theme-Tracker — Track thematic progression
✅ Rhythm-Analysis — Analyze rhythm and tension

[C] Run all workflows now
[S] Select which to run
[R] Review only — Then the others after corrections
[D] Defer — I will run them manually later
```

---

## Implementation Notes

**Key Features to Implement:**
- Style profile matching (replicate author's voice)
- Bible integration (accurately reference characters, locations, objects)
- Continuity maintenance (build on previous chapters)
- Plan adherence (follow chapter plan from Foundation)
- Revision loop (accept user feedback and revise)
- **Automatic trigger system** — Chain to other workflows after completion

**Anti-Slop Enforcement:**
- Avoid excessive adverbs
- Prefer active voice
- Use author's vocabulary patterns
- Match sentence length distribution
- Preserve author's imagery preferences

---

## Integration with Other Workflows

This workflow is the **central hub** that triggers multiple post-chapter workflows:

- **Bible-Update** → Keeps story bible current with each chapter
- **Character-Audit** → Ensures characters remain psychologically coherent
- **Theme-Tracker** → Tracks how themes evolve through the story
- **Rhythm-Analysis** → Monitors pacing and tension consistency

---

_This is a specification. Use the create-workflow workflow to build this workflow._
