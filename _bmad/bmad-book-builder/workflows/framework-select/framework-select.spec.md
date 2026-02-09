# Workflow Specification: FrameworkSelect

**Module:** bmad-book-builder
**Status:** ✅ Implemented — Complete workflow ready for use
**Created:** 2026-01-24
**Implemented:** 2026-01-25

---

## Workflow Overview

**Goal:** Choose narrative framework for story structure

**Description:** Story Architect recommends appropriate framework (Save the Cat, Hero's Journey, Snowflake) based on story type/genre, or helps create custom structure.

**Workflow Type:** Create-only

---

## Workflow Structure

### Entry Point

```yaml
---
name: framework-select
description: Choose narrative framework for structure
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/framework-select'
---
```

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Analyze Story | Understand story type, genre, scope |
| 2 | Recommend Framework | Suggest appropriate framework(s) |
| 3 | Explain Options | Detail what each framework offers |
| 4 | User Selection | Author chooses framework |
| 5 | Configure | Set up framework for use in Foundation |

---

## Workflow Inputs

### Required Inputs

- Story concept or type

---

## Workflow Outputs

### Output Format

- [X] Configuration

### Output Files

- `framework-selection.yaml` — Selected framework configuration

---

## Agent Integration

### Primary Agent

Story Architect

---

## Implementation Notes

**Implementation Date:** 2026-01-25
**Workflow Structure:** Step-file architecture with 5 sequential steps
**Primary Agent:** Story Architect
**Output Location:** `{bbb_output_folder}/foundation/framework-selection.yaml`

**Key Features:**
- File discovery: Checks for existing story-concept.md and project-brief.md
- Analysis-based recommendations: Ranks frameworks by suitability score
- Interactive selection: Letter-based menu with confirmation steps
- Complete configuration: Full framework structure with Foundation integration
- Custom framework support: Author-defined structures

**Framework Definitions:**
- Save the Cat: 15 beats, 4 acts, commercial fiction focus
- Hero's Journey: 12 stages, 3 phases, epic/transformation focus
- Snowflake Method: 10 steps, recursive process, character-first focus
- Custom: Author-defined approach

**Integration:**
Foundation workflow checks for `framework-selection.yaml` at startup and uses it if present for chapter planning and story structure.
