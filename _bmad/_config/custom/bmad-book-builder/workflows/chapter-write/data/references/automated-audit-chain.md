# Automated Audit Chain Reference
# Used by chapter-write step-07-finalize for quality assurance

> **🎯 CHAÎNE D'AUTOMATISATION — Basée sur l'analyse AgentAdam vs BBB**
>
> AgentAdam utilise un système d'audits automatiques après chaque chapitre pour garantir la cohérence. BBB implémente maintenant une chaîne d'audit automatique qui déclenche Review → Living Bible Update → Character Audits → Thematic Tracking → Rhythm Analysis.
>
> **Référence :** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (sections 5, 7, 8)

## Chain Sequence

### Step 1: Review (CRITICAL)
**Validation de cohérence avant mise à jour de la bible**

**Action:** Execute Review workflow for this chapter

**Failure Handling:**
- ⚠️ Review a détecté des problèmes critiques
- La chaîne d'audit est PAUSÉE
- Options: Corriger / Ignorer / Différer

**Success:** Continue to Step 2

### Step 2: Living Bible Update
**Mise à jour des 5 dimensions**

**Dimensions updated:**
- Chronologie: Ajouter les événements du chapitre
- Lieux: Mettre à jour les états des lieux
- Objets: Mettre à jour les objets introduits/modifiés
- Personnes: Mettre à jour les états psychologiques
- Thèmes: Enregistrer la progression thématique

**Action:** Execute Living Bible Edit mode for this chapter

### Step 3: Character Audits
**Audits des personnages présents dans le chapitre**

**Process:**
1. Identifier les personnages présents (from synopsis)
2. Pour chaque personnage:
   - Vérification des contradictions (5+ par personnage)
   - Cohérence psychologique globale
   - Progression de l'arc

**Action:** For EACH character → Execute character-audit workflow (Create mode)

### Step 4: Thematic Tracking
**Mise à jour de la progression thématique**

**Tracked:**
- Thèmes abordés: [list]
- Phase de progression: [1-5]
- Porteurs de thème: [which characters]
- Résonances: [symbolic connections]

**Action:** Execute theme-tracker workflow (if available) or update themes.md

### Step 5: Rhythm Analysis (OPTIONNEL)
**Analyse du pacing du chapitre**

**Analyzed:**
- Courbe de tension
- Équilibre action/réflexion
- Variation des longueurs de phrases
- Fluidité narrative

**Action:** Ask user Y/N, then execute rhythm-analysis workflow if yes

## User Options

### [A] Automatic Chain
Execute all 5 steps in sequence
- Step 1 runs first (CRITICAL)
- Steps 2-4 run automatically
- Step 5 requires user confirmation

### [S] Selective Chain
User chooses which steps to execute (1-5, comma-separated)
Execute only selected steps in order

### [D] Defer
Skip audits now (NOT RECOMMENDED)
**Risks:**
- Incohérences dans les chapitres futurs
- Bible non synchronisée
- Personnages incohérents

**Manual execution later:**
- Review: `review -c {chapter_number}`
- Living Bible: `living-bible -e`
- Character Audit: `character-audit -c`

## Chain Completion Output

```
✅ Chaîne d'audit terminée !

Étapes exécutées: [list of completed steps]
Étapes sautées: [list of skipped steps, if any]

Résumé des résultats:
- Review: ✅/❌ [result]
- Living Bible: ✅/❌ [result]
- Character Audits: [N] audits créés
- Thematic Tracking: ✅/❌ [result if executed]
- Rhythm Analysis: ✅/❌ [result if executed]

Fichiers créés/mis à jour:
- [List audit files created]
- [List bible files updated]
- [List tracking files updated]
```

## Status Storage (Chapter Frontmatter)

```yaml
auditChain:
  review: completed/skipped/failed
  bibleUpdate: completed/skipped
  characterAudits: completed/skipped/partial
  thematicTracking: completed/skipped
  rhythmAnalysis: completed/skipped
  lastChainDate: {date}
```
