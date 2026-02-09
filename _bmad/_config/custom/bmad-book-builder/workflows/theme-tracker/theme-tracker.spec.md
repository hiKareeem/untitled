# Workflow Specification: ThemeTracker

**Module:** bmad-book-builder
**Status:** Specification — Enhanced with AgentAdam analysis
**Created:** 2026-01-24
**Updated:** 2026-01-24
**Priority:** P2 (Standard Feature — Thematic Depth)

---

## Workflow Overview

**Goal:** Track thematic and emotional progression throughout narrative

**Description:** Thematic Weaver analyzes chapters for thematic thread presence, emotional beats, and character development moments. Maintains comprehensive tracking of how themes evolve from introduction to resolution.

**Workflow Type:** Edit-only (continuous tracking)

---

## Why This Workflow Exists

> **🎯 COMPLÈMENT À L'ANALYSE AGENTADAM VS BBB**
>
> AgentAdam possède un système de suivi thématique avec progression explicite par chapitre et connections personnage-thème. BBB doit offrir la même capacité.
>
> **Sans suivi thématique, les thèmes deviennent flous** et perdent leur impact émotionnel.
>
> **Référence :** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (sections 8, 10)
>
> **Impact :** MOYEN — Essentiel pour les romans thématiques
> **Effort :** MOYEN — Système de suivi structuré

---

## Workflow Structure

### Entry Point

```yaml
---
name: theme-tracker
description: Track thematic and emotional progression
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/theme-tracker'
---
```

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Load Chapter | Load chapter content |
| 2 | Identify Themes | Detect which thematic threads are present |
| 3 | Map Emotions | Track character emotional beats |
| 4 | Analyze Arc | Map character development per theme |
| 5 | Update Progression | Document how themes advanced in this chapter |
| 6 | Verify Consistency | Check thematic coherence with previous chapters |

---

## Theme Structure (from AgentAdam analysis)

```markdown
## Theme: [Theme Name] — e.g., "Confiance vs Méfiance"

### Core Question
[The central question this theme explores]

### Tension
[Opposing forces that create the theme]

### Progression by Chapter Phase
- **Chapitre 1-5**: [Introduction phase — how theme is introduced]
- **Chapitre 6-10**: [Exploration phase — how theme is tested]
- **Chapitre 11-15**: [Deepening phase — crisis point for theme]
- **Chapitre 16-20**: [Resolution phase — how theme resolves]
- **Chapitre 21-25**: [Final state — where theme ends]

### Character Connections
- **Character 1**: [How they embody theme, their arc]
- **Character 2**: [How they embody theme, their arc]
- **Character 3**: [How they embody theme, their arc]

### Per-Chapter Progression
| Chapter | Theme Event | Character Impact | Next Step |
|---------|-------------|------------------|-----------|
| 1 | Theme introduced | Initial positions | Setup for chapter 2 |
| 2 | First test | Complications | Setup for chapter 3 |
| ... | ... | ... | ... |
```

---

## Example from AgentAdam

```markdown
## Theme: Confiance vs Méfiance

### Progression
- Chapitre 1-5: Méfiance dominante (survie individuelle)
- Chapitre 6-10: Premières ouvertures (nécessité du groupe)
- Chapitre 11-15: Crise de confiance (trahison ou sacrifice)
- Chapitre 16-20: Reconstruction (nouvelle dynamique)
- Chapitre 21-25: Résolution (confiance gagnée ou perdue)

### Character Connections
- Marc: Arc de méfiance → confiance → test ultime
- Julie: Confiance naïve → trahison → méfiance guérie
- Chen: Méfiance pragmatique → confiance sélective
```

---

## Workflow Inputs

### Required Inputs

- Chapter content
- Current thematic tracking data

---

## Workflow Outputs

### Output Format

- [X] Data update
- [X] Document-producing (theme tracking)

### Output Files

- `tracking/themes.md` — Complete theme tracking with progression
- `tracking/emotions.md` — Emotional arc data per character
- `tracking/chapter-{XX}-themes.md` — Theme analysis per chapter

---

## Agent Integration

### Primary Agent

**Thematic Weaver** (Theme & Emotion Tracker)

Specializes in tracking themes and emotions throughout the narrative.

---

## When to Use This Workflow

- **After each chapter** — Update theme progression
- **During Foundation** — Establish main themes and their arcs
- **During revision** — Verify thematic consistency
- **Before final manuscript** — Ensure all themes resolve

---

## Automatic Trigger

> **🎯 DÉCLENCHEMENT AUTOMATIQUE**
>
> Ce workflow est **automatiquement déclenché** par le workflow **Chapter-Write** après la finalisation de chaque chapitre.
>
> **Quand :** Après Step 7 (Finalize) de Chapter-Write
> **Condition :** Toujours déclenché (chaque chapitre fait progresser les thèmes)
> **Mode :** L'utilisateur peut choisir d'exécuter immédiatement ou différer

**Ceci garantit que la progression thématique est suivie systématiquement à travers toute l'histoire.**

---

## Implementation Notes

### Thematic Depth Indicators:

A well-tracked theme should have:
1. **Clear question** — What is this theme really about?
2. **Opposing forces** — What creates the tension?
3. **Character connections** — Who embodies which side?
4. **Progression** — How does it evolve from start to finish?
5. **Resolution** — Does it resolve (and how)?

### Red Flags:

- ❌ Theme mentioned but never explored
- ❌ Character positions on theme never change
- ❌ Theme introduced but dropped
- ❌ No clear resolution (unless deliberate ambiguity)

---

## Integration with Other Workflows

- **Foundation** — Initial theme identification
- **Living-Bible** — Theme progression is one dimension
- **Bible-Update** — Extracts thematic info from chapters
- **Character-Audit** — Verify character thematic consistency

---

_This is a specification. Use the create-workflow workflow to build this workflow._

**Reference Analysis:** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (section 8)
