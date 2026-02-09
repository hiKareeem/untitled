# Workflow Specification: Foundation

**Module:** bmad-book-builder
**Status:** Placeholder — To be created via create-workflow workflow
**Created:** 2026-01-24

---

## Workflow Overview

**Goal:** Transform raw story idea into structured chapter breakdown

**Description:** Story Architect asks targeted questions, applies selected narrative framework, and generates complete chapter-by-chapter plan with purpose, scenes, and emotional beats.

**Workflow Type:** Create-only (tri-modal: Brief/Create/Validate)

---

## Workflow Structure

### Entry Point

```yaml
---
name: foundation
description: Transform raw story idea into structured chapter breakdown
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/foundation'
---
```

### Mode

- [X] Tri-modal (steps-b/, steps-c/, steps-v/)

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Gather Story | Extract raw story concept/premise from user |
| 2 | Framework Selection | Choose narrative structure (Save the Cat, Hero's Journey, Snowflake, Custom) |
| 3 | Targeted Questions | Ask about protagonist, conflict, themes, stakes |
| 4 | Generate Structure | Apply framework to create chapter breakdown |
| 5 | Review & Refine | User reviews plan, makes adjustments |
| 6 | Finalize | Lock chapter structure for writing |

---

## Workflow Inputs

### Required Inputs

- Raw story concept/premise from user

### Optional Inputs

- Pre-selected narrative framework
- Existing character dossiers
- Pre-written scenes or ideas

---

## Workflow Outputs

### Output Format

- [X] Document-producing
- [ ] Non-document

### Output Files

- `chapter-plan.md` — Complete chapter breakdown with purpose, scenes, emotional beats
- `framework-summary.md` — Explanation of chosen framework and its application

---

## Agent Integration

### Primary Agent

Story Architect — leads entire process, generates structure

### Other Agents

- Character Keeper (if characters pre-exist)
- Thematic Weaver (for thematic arc input)

---

## Implementation Notes

**Key Features to Implement:**
- Framework-specific structures (Save the Cat = 15 beats, Hero's Journey = 12 stages, Snowflake = progressive complexity)
- Targeted questioning to extract story essence
- Chapter breakdown with: purpose, scenes, emotional beats, approximate word count
- User revision loop (can adjust structure before finalizing)

**Framework Templates Needed:**
- Save the Cat beat sheet
- Hero's Journey 12 stages
- Snowflake Method progressive steps
- Custom structure builder

---

_This is a specification. Use the create-workflow workflow to build this workflow._
