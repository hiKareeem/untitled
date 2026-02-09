# Workflow Specification: AuditProject

**Module:** bmad-book-builder
**Status:** Placeholder — To be created via create-workflow workflow
**Created:** 2026-01-24

---

## Workflow Overview

**Goal:** Comprehensive project health check

**Description:** Continuity Editor runs full coherence audit across characters, timeline, plot, and style.

**Workflow Type:** Create-only

---

## Workflow Structure

### Entry Point

```yaml
---
name: audit-project
description: Comprehensive project health check
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/audit-project'
---
```

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Load All Chapters | Load complete manuscript |
| 2 | Run Coherence Check | Full consistency validation |
| 3 | Run Quality Check | Style, voice, prose quality |
| 4 | Compile Issues | All problems catalogued and prioritized |
| 5 | Generate Audit Report | Complete project health report |

---

## Workflow Inputs

### Required Inputs

- All chapters written so far

---

## Workflow Outputs

### Output Format

- [X] Document-producing

### Output Files

- `audit/project-audit.md` — Complete audit report

---

## Agent Integration

### Primary Agent

Continuity Editor

### Other Agents

- Character Keeper, Thematic Weaver, Rhythm Monitor

---

_This is a specification. Use the create-workflow workflow to build this workflow._
