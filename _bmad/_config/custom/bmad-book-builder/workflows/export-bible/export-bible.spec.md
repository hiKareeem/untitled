# Workflow Specification: ExportBible

**Module:** bmad-book-builder
**Status:** Placeholder — To be created via create-workflow workflow
**Created:** 2026-01-24

---

## Workflow Overview

**Goal:** Generate formatted story bible

**Description:** Compile all bible data into complete reference document with character profiles, location maps, relationship webs, and timeline.

**Workflow Type:** Create-only

---

## Workflow Structure

### Entry Point

```yaml
---
name: export-bible
description: Generate formatted story bible
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/export-bible'
---
```

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Load Bible Data | All tracking data |
| 2 | Format Document | Structure as readable reference |
| 3 | Generate Output | Complete bible document |

---

## Workflow Inputs

### Required Inputs

- All bible data

---

## Workflow Outputs

### Output Format

- [X] Document-producing

### Output Files

- `bible/complete-bible.md` — Formatted reference document

---

## Agent Integration

### Primary Agent

Character Keeper

---

_This is a specification. Use the create-workflow workflow to build this workflow._
