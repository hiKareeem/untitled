# Workflow Specification: CharacterAudit

**Module:** bmad-book-builder
**Status:** Specification — To be created via create-workflow workflow
**Created:** 2026-01-24
**Priority:** P0 (Critical Gap — Feature Parity with AgentAdam)

---

## Workflow Overview

**Goal:** Verify character psychological coherence after each chapter

**Description:** Continuity Editor performs character-specific audits to check that character behavior in each chapter aligns with their established psychological profile, contradictions, and arc progression. Each audit produces a pass/fail report for every contradiction.

**Workflow Type:** Create-only (per-chapter audit)

---

## Why This Workflow Exists

> **🎯 ÉCART CRITIQUE IDENTIFIÉ — Analyse AgentAdam vs BBB**
>
> AgentAdam possède un système d'audit par personnage qui vérifie la cohérence psychologique chapitre après chapitre. BBB n'a actuellement que des vérifications de continuité générales.
>
> **Sans ce workflow, les personnages peuvent devenir incohérents.** Les contradictions établies dans les profils ne sont pas vérifiées dans l'écriture.
>
> **Référence :** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (section 5)
>
> **Impact :** HAUT — Garantit la qualité et la cohérence des personnages à long terme
> **Effort :** MOYEN — Workflow structuré avec checks cohérents

---

## Workflow Structure

### Entry Point

```yaml
---
name: character-audit
description: Verify character psychological coherence after each chapter
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/character-audit'
---
```

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Select Chapter & Character | Choose which chapter and character to audit |
| 2 | Load Character Profile | Read the character's complete dossier |
| 3 | Extract Chapter Behavior | Identify what character does/thinks/feels in chapter |
| 4 | Check Contradictions | **Verify each contradiction (5+) against behavior** |
| 5 | Verify Arc Progression | Check if character is progressing through their arc |
| 6 | Generate Audit Report | Create pass/fail report with ✅/❌ for each contradiction |

---

## Character-Specific Audit Template

> **Basé sur le système d'audit d'AgentAdam (section 5 de l'analyse)**

```markdown
## Audit - Chapter XX - [Character Name]

### Appearance in This Chapter
- Scenes: [list of scenes]
- Key Actions: [what they do]
- Émotions dominantes: [what they feel]

### Cohérence psychologique — Vérification des contradictions
- ✅/❌ Contradiction 1 (Valeurs vs Actions): [check against behavior] — COHÉRENT/INCOHÉRENT
- ✅/❌ Contradiction 2 (Image de soi vs Réalité): [check against behavior] — COHÉRENT/INCOHÉRENT
- ✅/❌ Contradiction 3 (Conscient vs Inconscient): [check against behavior] — COHÉRENT/INCOHÉRENT
- ✅/❌ Contradiction 4 (Idéalisme vs Pragmatisme): [check against behavior] — COHÉRENT/INCOHÉRENT
- ✅/❌ Contradiction 5 (Passé vs Présent): [check against behavior] — COHÉRENT/INCOHÉRENT
- ✅/❌ Contradiction 6+ (autres): [check against behavior] — COHÉRENT/INCOHÉRENT

### Évolution de l'arc
- Phase actuelle: [X]/5
- Progression: [description of how they changed]
- Prochaine étape: [anticipation for next chapter]

### Problèmes identifiés
- [Any inconsistencies found]
- [Suggestions for correction]

### Score de cohérence
- Score: [X]/5 contradictions cohérentes
- Statut: ✅ PASS / ❌ FAIL / ⚠️ WARN
```

---

## Workflow Inputs

### Required Inputs

- Chapter number to audit
- Character name to audit
- Chapter text (or reference to chapter file)
- Character dossier (already exists in `characters/`)

---

## Workflow Outputs

### Output Format

- [X] Document-producing (audit reports)

### Output Files

- `audits/audit-chapitre-{XX}-{character-name}.md` — Character-specific audit report
- `audits/audit-summary-chapitre-{XX}.md` — Summary of all character audits for chapter

---

## Agent Integration

### Primary Agent

**Continuity Editor** (Quality & Coherence Specialist)

The Continuity Editor already exists and has general continuity checking capabilities. This workflow gives them a structured, character-specific framework.

---

## Implementation Notes

### Critical Features (from AgentAdam analysis):

1. **Per-Character Audits**: Each character gets their own audit file per chapter
2. **Contradiction Checking**: EVERY contradiction (5+) from the character profile must be checked
3. **Pass/Fail System**: ✅/❌ for clear status tracking
4. **Arc Progression Tracking**: Verify characters are actually changing according to their arc
5. **Problem Identification**: Specific suggestions when incoherence is detected

### Example from AgentAdam (section 5 of analysis):
```markdown
## Audit - Chapter 12 - Marc

### Cohérence psychologique
- ✅ Contradiction Valeurs vs Actions: Marc hésite avant de décider pragmatique — COHÉRENT
- ❌ Contradiction Individualisme vs Collectivisme: Marc agit trop seul sans justification — INCOHÉRENT
- ✅ Contradiction Idéalisme vs Pragmatisme: Marc compromet ses idéaux — COHÉRENT

### Problèmes identifiés
- Marc prend une décision sans consultation du groupe (en conflit avec son évolution vers le collectif)
- Suggestion: Ajouter une scène de délibération ou montrer son conflit interne
```

---

## When to Use This Workflow

- **After each chapter is written** — Run audit for each character appearing in chapter
- **During revision** — Re-run audits to verify corrections
- **Before final manuscript** — Comprehensive audit of all chapters

---

## Automatic Trigger

> **🎯 DÉCLENCHEMENT AUTOMATIQUE**
>
> Ce workflow est **automatiquement déclenché** par le workflow **Chapter-Write** après la finalisation de chaque chapitre.
>
> **Quand :** Après Step 7 (Finalize) de Chapter-Write
> **Condition :** Pour chaque personnage présent dans le chapitre
> **Mode :** L'utilisateur peut choisir d'exécuter immédiatement ou différer

**Ceci garantit que la cohérence des personnages est vérifiée systématiquement après chaque chapitre.**

---

## Future Enhancements

- Batch mode: Audit all characters in a chapter at once
- Cross-chapter analysis: Identify patterns across multiple chapters
- Metric tracking: Character coherence score over entire manuscript

---

_This is a specification. Use the create-workflow workflow to build this workflow._

**Reference Analysis:** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (sections 2, 5, 9, 10)
