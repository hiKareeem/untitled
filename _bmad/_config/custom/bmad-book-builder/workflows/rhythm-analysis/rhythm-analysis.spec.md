# Workflow Specification: RhythmAnalysis

**Module:** bmad-book-builder
**Status:** Placeholder — To be created via create-workflow workflow
**Created:** 2026-01-24

---

## Workflow Overview

**Goal:** Analyze pacing and tension of chapter(s)

**Description:** Rhythm Monitor measures tension curve, action/reflection ratio, chapter length patterns, and climax placement.

**Workflow Type:** Create-only

---

## Workflow Structure

### Entry Point

```yaml
---
name: rhythm-analysis
description: Analyze pacing and tension
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/rhythm-analysis'
---
```

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Load Chapter(s) | Load content to analyze |
| 2 | Measure Tension | Plot tension curve |
| 3 | Analyze Balance | Action/reflection ratio |
| 4 | Check Patterns | Chapter length, climax placement |
| 5 | Generate Report | Pacing report with metrics and recommendations |

---

## Workflow Inputs

### Required Inputs

- Chapter(s) to analyze

---

## Workflow Outputs

### Output Format

- [X] Document-producing

### Output Files

- `analysis/rhythm-{scope}.md` — Pacing analysis report

---

## Agent Integration

### Primary Agent

**Rhythm Monitor** — Pacing and tension specialist

---

## When to Use This Workflow

- **After each chapter** — Analyze pacing and tension patterns
- **During revision** — Verify rhythm consistency
- **Before final manuscript** — Comprehensive pacing review

---

## Automatic Trigger

> **🎯 DÉCLENCHEMENT AUTOMATIQUE**
>
> Ce workflow est **automatiquement déclenché** par le workflow **Chapter-Write** après la finalisation de chaque chapitre.
>
> **Quand :** Après Step 7 (Finalize) de Chapter-Write
> **Condition :** Toujours déclenché (analyse du rythme du chapitre complété)
> **Mode :** L'utilisateur peut choisir d'exécuter immédiatement ou différer

**Ceci garantit que le rythme et la tension sont monitorés systématiquement.**

---

## Integration with Other Workflows

This workflow is triggered by **Chapter-Write** as part of the post-chapter analysis suite, alongside **Bible-Update**, **Character-Audit**, and **Theme-Tracker**.

---

_This is a specification. Use the create-workflow workflow to build this workflow._
