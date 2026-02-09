# Workflow Specification: LivingBible

**Module:** bmad-book-builder
**Status:** ✅ IMPLEMENTED (13 files, edit-only workflow)
**Created:** 2026-01-24
**Implemented:** 2026-01-24
**Priority:** P1 (Major Gap — Multi-Dimensional Story Tracking)

---

## Workflow Overview

**Goal:** Maintain a living, multi-dimensional story bible that evolves with the narrative

**Description:** Character Keeper (Bible Guardian) manages a comprehensive story bible that tracks chronology, locations, objects, character states, and themes as they evolve throughout the writing process. Unlike static bibles, this is a living document updated after each chapter.

**Workflow Type:** Edit-only (continuous updates throughout writing)

---

## Why This Workflow Exists

> **🎯 ÉCART MAJEUR IDENTIFIÉ — Analyse AgentAdam vs BBB**
>
> AgentAdam possède une **bible narrative vivante** avec suivi multi-dimensionnel (chronologie, lieux, objets, personnages, thèmes). BBB a seulement un workflow de mise à jour de base.
>
> **Sans ce workflow, la continuité à long terme est difficile.** Les détails se perdent, les incohérences s'accumulent.
>
> **Référence :** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (section 4)
>
> **Impact :** MOYEN — Essentiel pour les romans multi-chapitres avec personnages multiples
> **Effort :** ÉLEVÉ — Système complexe de suivi multi-dimensionnel

---

## Workflow Structure

### Entry Point

```yaml
---
name: living-bible
description: Maintain living, multi-dimensional story bible
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/living-bible'
---
```

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Select Update Trigger | Choose what event triggers update (chapter written, major event, character transformation) |
| 2 | Update Chronology | Add day-by-day events, timeline progression |
| 3 | Update Locations | Record new locations, resource changes, events per location |
| 4 | Update Objects | Track object inventory, origins, significance |
| 5 | Update Character States | Record current psychological states, relationship changes |
| 6 | Update Theme Progression | Track how themes evolve per chapter |

---

## Multi-Dimensional Tracking System

> **Basé sur le système de suivi d'AgentAdam (section 4 de l'analyse)**

### Dimension 1: Chronologie (Timeline)
```markdown
## Chronologie

### Jour 47
- Matin: Marc explore le secteur industriel
- Midi: Découverte des capsules de survie
- Après-midi: Confrontation avec Élise
- Soir: Réunion du conseil

### Jour 48
- [Events continue...]
```

**Purpose:** Track day-by-day progression, verify timing consistency

### Dimension 2: Lieux (Locations)
```markdown
## Lieux

### Secteur Industriel
- Découvert: Jour 12
- Resources: Outils, matériaux, anciens stocks
- Événements clés:
  - Jour 12: Première exploration
  - Jour 47: Découverte des capsules
  - Jour 50: Conflit pour le contrôle
- Personnalités présentes: Marc, Julie, Chen
- État actuel: Contrôlé par le groupe de Marc
```

**Purpose:** Track location inventory, resources, events, occupants

### Dimension 3: Objets (Objects)
```markdown
## Objets

### Capsules de survie
- Origine: Secteur industriel, vestige de l'Ancien Monde
- Découvert: Jour 47
- Quantité: 12 capsules
- Signification: Symbole d'espoir vs ressource limitée = conflit
- Propriétaire actuel: Contrôlées par Marc (tension)
- État: 3 utilisées, 9 restantes
```

**Purpose:** Track plot-critical objects, their status and significance

### Dimension 4: Personnes (Character States)
```markdown
## Personnes

### Marc
- État psychologique actuel: Phase 3/5 (Point de bascule)
- Relations actuelles:
  - Élise: Tension haute (conflit leadership)
  - Julie: Alliance fragile (intérêt romantique)
  - Chen: Doute croissant (loyauté en question)
- Dernière apparition: Chapitre 12
- Prochaine apparition planifiée: Chapitre 14
- Arc en cours: Individualisme → Collectivisme (en progrès)

### [Other characters...]
```

**Purpose:** Track character states, relationships, arc progression

### Dimension 5: Thèmes (Themes)
```markdown
## Thèmes

### Confiance vs Méfiance
- Progression:
  - Chapitre 1-5: Méfiance dominante (survie individuelle)
  - Chapitre 6-10: Premières ouvertures (nécessité du groupe)
  - Chapitre 11-15: Crise de confiance (trahison ou sacrifice)
  - Chapitre 16-20: Reconstruction (nouvelle dynamique)
  - Chapitre 21-25: Résolution (confiance gagnée ou perdue)
- Connections personnage-thème:
  - Marc: Arc de méfiance → confiance → test ultime
  - Julie: Confiance naïve → trahison → méfiance guérie
  - Chen: Méfiance pragmatique → confiance sélective
- Chapitre actuel: 12 (Phase 3 - Crise)
```

**Purpose:** Track thematic evolution, character-theme connections

---

## Workflow Inputs

### Required Inputs

- Trigger event type (chapter written, major event, character transformation)
- Chapter number (if chapter written)
- Chapter content (for extracting updates)

---

## Workflow Outputs

### Output Format

- [X] Document-producing (living bible updates)

### Output Files

- `bible/chronologie.md` — Day-by-day timeline
- `bible/lieux.md` — Location database with resources
- `bible/objets.md` — Object inventory and significance
- `bible/personnes.md` — Character state tracking
- `bible/themes.md` — Theme progression mapping

---

## Agent Integration

### Primary Agent

**Character Keeper** (Bible Guardian)

The Character Keeper already exists and is specifically designed as "Bible Guardian" — this workflow gives them the structured framework they need.

---

## Update Triggers

The workflow should be activated when:

1. **After each chapter is written** — Extract all new information from chapter
2. **Major events occur** — Deaths, revelations, location changes
3. **Characters transform** — Psychological breakthroughs, relationship changes
4. **Themes shift** — Thematic progression reaches new phase

---

## Implementation Notes

### Critical Features (from AgentAdam analysis):

1. **Multi-Dimensional Tracking**: 5 simultaneous tracking dimensions
2. **Living Document**: Bible evolves with story, not static
3. **Cross-Referenced**: Each dimension references others (location → characters present, object → significance)
4. **Extractable**: Information can be extracted for audits, reviews, continuity checks
5. **Searchable**: Quick lookup of character states, locations, objects

### File Structure (from AgentAdam):
```
bible/
├── chronologie.md      # Day-by-day timeline
├── lieux.md            # Location database
├── objets.md           # Object inventory
├── personnes.md        # Character states
└── themes.md           # Theme progression
```

---

## When to Use This Workflow

- **After completing each chapter** — Update all dimensions
- **During revision** — Verify continuity, fix inconsistencies
- **Before writing new chapter** — Check current states for reference
- **For manuscript review** — Extract summary for review

---

## Integration with Other Workflows

- **Character-Audit**: Uses `personnes.md` for current states
- **Chapter-Write**: References bible for continuity
- **Review**: Uses bible for comprehensive check
- **Export-Bible**: Compiles all dimensions into single document

---

## Future Enhancements

- Searchable index across all dimensions
- Visualization tools (timeline, relationship maps)
- Change tracking (what changed between chapters)
- Alert system (potential inconsistencies detected)

---

_This specification has been implemented. See `workflow.md` for the implementation._

**Reference Analysis:** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (sections 4, 8)

**Implementation Details:**
- 6 edit steps covering all 5 dimensions
- 5 bible templates for initialization
- Multi-trigger support (chapter, event, transformation, theme shift)
- Cross-reference capability between dimensions
