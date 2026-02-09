---
name: Report
description: Générer le rapport d'analyse de rythme
nextStepFile: null
---

# Step 04: Report

## Objectif

Générer le rapport d'analyse de rythme et le sauvegarder dans le dossier analysis.

---

## Instructions pour l'Agent

### 1. Préparer le Dossier de Sortie

Vérifie/crée le dossier:
```
{project-root}/analysis/
```

### 2. Générer le Rapport

Utilise le template `data/templates/report-template.md` et remplis avec les données d'analyse.

**Sections à compléter:**
1. Executive Summary - Résumé et score global
2. Pacing Analysis - Tableau des scènes et distribution
3. Tension Curve - Visualisation ASCII et beats clés
4. Transitions Analysis - Tableau et score
5. Beat Mapping - Beats identifiés avec fonctions
6. Flow Assessment - Évaluation de la fluidité
7. Action/Reflection Balance - Ratio et assessment
8. Recommendations - Issues critiques, importantes, mineures
9. Comparison - Métriques vs moyenne du livre (si applicable)

> **Référence:** Les critères d'évaluation pour chaque section sont définis dans les documents de référence:
> - `data/references/pacing-analysis-framework.md` - pour les sections 2 et 7
> - `data/references/tension-mapping-procedures.md` - pour la section 3
> - `data/references/transition-analysis-guide.md` - pour la section 4
> - `data/references/beat-mapping-system.md` - pour la section 5
> - `data/references/flow-assessment-criteria.md` - pour la section 6

### 3. Déterminer le Nom du Fichier

Selon le scope:
- **Single chapter:** `rhythm-chapter-{N}.md`
- **Range:** `rhythm-chapters-{N}-to-{M}.md`
- **Full book:** `rhythm-full-{date}.md`

### 4. Écrire le Rapport

Utilise l'outil Write pour sauvegarder:
```
{project-root}/analysis/{filename}
```

### 5. Afficher le Résumé

Présente les findings clés à l'utilisateur:

```
═══════════════════════════════════════════════════════
     RAPPORT DE RYTHME - Chapitre {N}: "{titre}"
═══════════════════════════════════════════════════════

📊 SCORE GLOBAL: {score}/10 - {health_status}

┌─────────────────────────────────────────────────────┐
│ MÉTRIQUES CLÉS                                      │
├─────────────────────────────────────────────────────┤
│ Pacing:      {score}/10  {bar}                      │
│ Tension:     {score}/10  {bar}                      │
│ Transitions: {score}/10  {bar}                      │
│ Flow:        {score}/10  {bar}                      │
└─────────────────────────────────────────────────────┘

🔴 ISSUES CRITIQUES: {count}
{list_critical_issues}

🟡 POINTS D'ATTENTION: {count}
{list_important_issues}

🟢 POINTS FORTS:
{list_strengths}

📁 Rapport complet: analysis/{filename}
═══════════════════════════════════════════════════════
```

### 6. Recommandations d'Action

Selon les findings, propose les next steps:

**Si issues critiques:**
```
⚠️ Je recommande d'adresser les issues critiques avant de continuer.
Veux-tu que je détaille les corrections suggérées?
```

**Si healthy:**
```
✓ Le rythme de ce chapitre est solide!
Quelques ajustements mineurs sont suggérés dans le rapport complet.
```

**Si scope = full book:**
```
Vue d'ensemble du pacing complète.
Les chapitres {X, Y, Z} méritent une attention particulière.
```

### 7. Proposer les Workflows Connexes

```
Workflows suggérés:
- [RA] Analyser un autre chapitre
- [RE] Review - Révision complète du chapitre
- [CW] Chapter-Write - Continuer l'écriture
```

---

## Validation Finale

- [ ] Rapport généré et sauvegardé
- [ ] Résumé affiché à l'utilisateur
- [ ] Recommendations claires fournies
- [ ] Next steps proposés

---

## Navigation

**Step précédent:** [Step 03: Analyze](step-03-analyze.md)
**Fin du workflow**

---

## Output Produit

```
analysis/
└── rhythm-{scope}.md    # Rapport complet d'analyse de rythme
```

---

## Notes de Clôture

- Le rapport est autonome et peut être référencé ultérieurement
- Les scores sont comparables entre chapitres pour suivre les tendances
- Les issues critiques devraient être trackées jusqu'à résolution
- Ce workflow peut être re-exécuté après modifications pour vérifier les améliorations
