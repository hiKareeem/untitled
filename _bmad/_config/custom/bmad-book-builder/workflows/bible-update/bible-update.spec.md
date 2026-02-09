# Workflow Specification: BibleUpdate

**Module:** bmad-book-builder
**Status:** Specification — Enhanced with AgentAdam analysis
**Created:** 2026-01-24
**Updated:** 2026-01-24
**Priority:** P2 (Standard Feature — Bible Maintenance)

---

## Workflow Overview

**Goal:** Update story bible after chapter completion

**Description:** Character Keeper extracts new information from completed chapters and updates the story bible — characters, locations, objects, timeline, and thematic progression.

**Workflow Type:** Edit-only (continuous updates)

---

## Relationship to Living-Bible Workflow

> **📌 NOTE IMPORTANTE**
>
> Ce workflow **Bible-Update** est une **version simplifiée** de **Living-Bible**.
>
> **Bible-Update** : Extraction automatique depuis les chapitres écrits
> **Living-Bible** : Système complet multi-dimensionnel avec suivi structuré
>
> Pour les nouveaux projets, **préférer Living-Bible** qui offre plus de profondeur.
> Bible-Update est utile pour des mises à jour rapides après l'écriture.

---

## Workflow Structure

### Entry Point

```yaml
---
name: bible-update
description: Update story bible after each chapter
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/bible-update'
---
```

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Load Chapter | Load completed chapter content |
| 2 | Extract Chronology | Identify timeline events, day progression |
| 3 | Extract Characters | Track character appearances, states, relationship changes |
| 4 | Extract Locations | Record locations used, resources, events |
| 5 | Extract Objects | Track plot-critical objects, status changes |
| 6 | Extract Themes | Identify thematic advancement in chapter |
| 7 | Validate Continuity | Check for inconsistencies with existing bible |
| 8 | Update Bible | Save all extracted information to bible files |

---

## Extraction Template (per Chapter)

> **Basé sur la méthodologie AgentAdam de suivi multi-dimensionnel**

```markdown
## Chapitre XX - Extraction

### Chronologie
- Jour dans l'histoire: [X]
- Événements clés: [list]

### Personnes présentes
- [Character 1]: [Actions, état psychologique, changements]
- [Character 2]: [Actions, état psychologique, changements]

### Lieux utilisés
- [Location 1]: [Description, ressources utilisées, événements]
- [Location 2]: [Description, ressources utilisées, événements]

### Objets notables
- [Object 1]: [Statut, changements, signification]
- [Object 2]: [Statut, changements, signification]

### Thèmes avancés
- [Theme 1]: [Comment ce chapitre fait progresser le thème]
- [Theme 2]: [Comment ce chapitre fait progresser le thème]

### Incohérences détectées
- [Any continuity issues found during extraction]
```

---

## Workflow Inputs

### Required Inputs

- Completed chapter content
- Current story bible (for cross-reference)

---

## Workflow Outputs

### Output Format

- [X] Data update
- [X] Document-producing (extraction summary)

### Output Files

- `bible/chronologie.md` — Updated timeline
- `bible/personnes.md` — Updated character states
- `bible/lieux.md` — Updated location records
- `bible/objets.md` — Updated object inventory
- `bible/themes.md` — Updated thematic progression
- `bible/extract-chapitre-{XX}.md` — Extraction record for chapter

---

## Agent Integration

### Primary Agent

**Character Keeper** (Bible Guardian)

The Character Keeper is specifically designed as the bible manager.

---

## When to Use This Workflow

- **After completing each chapter** — Extract all new information
- **During revision** — Update bible with changes
- **For continuity checks** — Verify information is tracked correctly

**For comprehensive tracking**, use the **Living-Bible** workflow instead.

---

## Implementation Notes

### Cross-Reference Checks:

When updating one section, verify:
- **Chronologie → Personnes**: Are characters in the right place at the right time?
- **Personnes → Lieux**: Do location references match character movements?
- **Personnes → Thèmes**: Do character actions align with thematic arcs?
- **Objets → Chronologie**: Are objects created/used at consistent times?

---

## Integration with Other Workflows

- **Living-Bible** — Comprehensive multi-dimensional tracking (preferred)
- **Chapter-Write** — Should trigger bible-update after completion
- **Character-Audit** — Uses bible for character state verification
- **Theme-Tracker** — Integrates with thematic progression

---

_This is a specification. Use the create-workflow workflow to build this workflow._

**Reference Analysis:** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (sections 4, 8)
