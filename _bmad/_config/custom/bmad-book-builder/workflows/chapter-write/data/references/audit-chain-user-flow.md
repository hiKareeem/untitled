# Automated Audit Chain - User Interaction Flow

**Purpose:** Guide users through the automated audit chain execution options.

**Reference:** See `data/references/automated-audit-chain.md` for complete technical documentation.

---

## Introduction to User

```text
🔗 Chaîne d'Audit Automatique

Pour garantir la cohérence de votre roman, je vais maintenant déclencher automatiquement une série d'audits de qualité.

La chaîne d'audit :
1. Review — Validation de cohérence (CRITICAL)
2. Living Bible Update — Mise à jour des 5 dimensions
3. Character Audits — Audit par personnage présent
4. Thematic Tracking — Mise à jour de la progression thématique
5. Rhythm Analysis — Analyse du pacing (optionnel)
```

---

## User Choice Prompt

```text
Comment souhaitez-vous procéder ?

[A] Automatique — Exécuter toute la chaîne (RECOMMANDÉ)
[S] Sélectif — Choisir quelles étapes exécuter
[D] Différer — Passer les audits pour l'instant (NON RECOMMANDÉ)

Votre choix : [A]utomatique / [S]électif / [D]ifférer
```

---

## Option A: Automatic Execution

**User Message:**
```text
Exécution de la chaîne d'audit automatique...
```

**Procedure:**
1. Load automated-audit-chain.md reference
2. Execute automatic chain sequence:
   - Step 1: Review → If fails, pause and ask [C]orrect/[I]gnore/[D]efer
   - Step 2: Living Bible Update
   - Step 3: Character Audits (for each character in chapter)
   - Step 4: Thematic Tracking
   - Step 5: Ask Y/N for Rhythm Analysis

---

## Option S: Selective Execution

**User Message:**
```text
Choisissez les étapes à exécuter :

[1] Review (Recommandé)
[2] Living Bible Update (Recommandé)
[3] Character Audits (Recommandé)
[4] Thematic Tracking
[5] Rhythm Analysis

Entrez les numéros des étapes à exécuter (séparés par des virgules) :
```

**Procedure:**
- Execute only selected steps in order (1-5)

---

## Option D: Defer Execution

**User Message:**
```text
⏸️ Chaîne d'audit différée

Les audits ne seront pas exécutés maintenant.

⚠️ IMPORTANT : Sans les audits, vous risquez :
- Incohérences dans les chapitres futurs
- Bible non synchronisée
- Personnages incohérents

Vous pourrez exécuter les audits manuellement plus tard :
- Review : `review -c {chapter_number}`
- Living Bible : `living-bible -e`
- Character Audit : `character-audit -c`

Voulez-vous vraiment différer ? [Y] Oui / [N] Annuler et exécuter la chaîne
```

**Procedure:**
- Wait for user confirmation
- If confirmed, skip audit chain
- If N cancelled, proceed to automatic execution

---

## Chain Completion Summary

**User Message:**
```text
✅ Chaîne d'audit terminée !

Étapes exécutées : [list of completed steps]
Étapes sautées : [list of skipped steps, if any]

Résumé des résultats :
- Review : ✅/❌ [result]
- Living Bible : ✅/❌ [result]
- Character Audits : [N] audits créés
- Thematic Tracking : ✅/❌ [result if executed]
- Rhythm Analysis : ✅/❌ [result if executed]

Fichiers créés/mis à jour :
- [List audit files created]
- [List bible files updated]
- [List tracking files updated]
```

---

## Chain Status Storage

**Store in Chapter Frontmatter:**

```yaml
auditChain:
  review: completed/skipped/failed
  bibleUpdate: completed/skipped
  characterAudits: completed/skipped/partial
  thematicTracking: completed/skipped
  rhythmAnalysis: completed/skipped
  lastChainDate: {date}
```

---

## Audit Chain Steps Reference

**Step 1: Review** (CRITICAL)
- Validates consistency
- If fails: Pause for user decision

**Step 2: Living Bible Update**
- Updates 5 dimensions
- Chronologie, Lieux, Objets, Personnes, Thèmes

**Step 3: Character Audits**
- One audit per character present in chapter
- Tracks character development

**Step 4: Thematic Tracking**
- Updates thematic progression
- Monitors theme evolution

**Step 5: Rhythm Analysis** (Optional)
- Analyzes chapter pacing
- Flow and rhythm assessment
