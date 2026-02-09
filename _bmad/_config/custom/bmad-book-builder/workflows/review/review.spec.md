# Workflow Specification: Review

**Module:** bmad-book-builder
**Status:** Placeholder — To be created via create-workflow workflow
**Created:** 2026-01-24

---

## Workflow Overview

**Goal:** Validate coherence and quality of chapter(s) or full manuscript

**Description:** Continuity Editor checks for inconsistencies, plot holes, character drift, timeline issues, and provides actionable report with fixes suggested.

**Workflow Type:** Create-only

---

## Workflow Structure

### Entry Point

```yaml
---
name: review
description: Validate coherence and quality of chapter(s)
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/review'
---
```

### Mode

- [X] Tri-modal (steps-b/, steps-c/, steps-v/)

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Load Content | Load chapter(s) for review |
| 2 | Load Reference | Load bible, previous chapters, plan |
| 3 | Validate Coherence | Check characters, locations, objects, timeline |
| 4 | Identify Issues | Catalog problems by category and severity |
| 5 | Generate Report | Create actionable report with fixes |
| 6 | Present Findings | Walk through issues with user |
| 7 | Track Resolutions | Allow user to mark issues as fixed |

---

## Workflow Inputs

### Required Inputs

- Chapter text or full manuscript
- Story bible
- Chapter plan (for structural review)

### Optional Inputs

- Previous chapters (for context)
- Style profile (for quality check)

---

## Workflow Outputs

### Output Format

- [X] Document-producing
- [ ] Non-document

### Output Files

- `review-report-{scope}.md` — Detailed coherence report with issues catalogued and prioritized

---

## Agent Integration

### Primary Agent

**Continuity Editor** — leads validation, generates report

### Other Agents Referenced

- Character Keeper (bible validation)
- Thematic Weaver (thematic coherence)
- Rhythm Monitor (pacing review)

---

## Automatic Trigger

> **🎯 DÉCLENCHEMENT AUTOMATIQUE**
>
> Ce workflow est **automatiquement déclenché** par le workflow **Chapter-Write** après la finalisation de chaque chapitre.
>
> **Quand :** Après Step 7 (Finalize) de Chapter-Write
> **Condition :** Toujours déclenché (**PREMIER PRIORITÉ** — avant les autres workflows)
> **Mode :** L'utilisateur peut choisir d'exécuter immédiatement ou différer
>
> **Pourquoi en priorité ?** Review identifie les problèmes de cohérence qui doivent être corrigés **avant** que la bible, les audits de personnages et le suivi thématique soient mis à jour. Mettre à jour la bible avec des informations incohérentes serait contre-productif.

**Ceci garantit que chaque chapitre est validé pour sa cohérence et sa qualité avant d'être considéré comme "finalisé".**

---

## When to Use This Workflow

- **After each chapter** — Automatic trigger from Chapter-Write (recommended)
- **During revision** — Comprehensive review of multiple chapters
- **Before final manuscript** — Full manuscript coherence check
- **Manually** — When author wants independent review at any time

---

## Implementation Notes

**Key Features to Implement:**
- Character consistency (personality, voice, motivation)
- Location accuracy (descriptions match, distances plausible)
- Object tracking (items don't appear/disappear)
- Timeline validation (events in correct order, plausible timing)
- Plot hole detection (contradictions, loose ends)
- Actionable issue reporting (specific examples, suggested fixes)

**Issue Categories:**
- Critical (breaks story logic) — Must fix before finalizing
- Major (noticeable inconsistency) — Should fix before publishing
- Minor (detail that should be fixed) — Polish before final

---

## Integration with Other Workflows

This workflow is **triggered first by Chapter-Write** because:
1. Review validates the chapter content
2. Once validated, THEN update the bible (Bible-Update)
3. THEN run specialized analysis (Character-Audit, Theme-Tracker, Rhythm-Analysis)

**Logical flow:** Chapter-Write → **Review** → (if passes) → Bible-Update → Character-Audit → Theme-Tracker → Rhythm-Analysis

---

_This is a specification. Use the create-workflow workflow to build this workflow._
