---
name: Analyze
description: Effectuer l'analyse approfondie du rythme narratif
nextStepFile: step-04-report.md
---

# Step 03: Analyze

## Objectif

Effectuer l'analyse approfondie du rythme narratif: pacing, tension, transitions, et beats.

---

## Instructions pour l'Agent

### 1. Analyse du Pacing par Scène

Pour chaque scène identifiée, détermine le type de pacing (action, transition, ou reflection) et évalue les indicateurs clés.

> **Référence:** Consultez `data/references/pacing-analysis-framework.md` pour:
> - Définitions détaillées des types de pacing
> - Critères d'évaluation et indicateurs
> - Métriques de pacing (event density, sentence velocity, dialogue ratio)
> - Système de scoring complet

**Processus:**
```
Analyse de pacing en cours...

Scène 1: "{titre}" → ACTION (haute densité d'événements, phrases courtes)
Scène 2: "{titre}" → REFLECTION (introspection, phrases longues)
...
```

### 2. Cartographie de la Tension

Évalue le niveau de tension (1-10) à chaque point clé du chapitre.

> **Référence:** Consultez `data/references/tension-mapping-procedures.md` pour:
> - Échelle de tension détaillée (1-10)
> - Points d'évaluation obligatoires
> - 5 composantes de calcul de tension
> - Formes de courbes idéales et problématiques
> - Techniques de construction de tension

**Processus:**
Construis la courbe de tension:
```
Courbe de tension du chapitre:

Opening:     ████████░░ (8/10) - Hook efficace
Mid-point:   ██████░░░░ (6/10) - Plateau
Climax:      █████████░ (9/10) - Peak atteint
Resolution:  ████░░░░░░ (4/10) - Décélération appropriée
```

### 3. Analyse des Transitions

Évalue chaque transition entre scènes selon le type et la qualité.

> **Référence:** Consultez `data/references/transition-analysis-guide.md` pour:
> - Définitions des types de transitions (cut, fade, bridge)
> - Critères d'évaluation de qualité (0-10)
> - Guide de sélection du type approprié
> - Problèmes courants et solutions

**Processus:**
```
Transitions analysées:

Scène 1 → 2: FADE (ellipse temporelle) ✓ Fluide
Scène 2 → 3: CUT (changement de POV) ⚠️ Légèrement abrupt
...
```

### 4. Mapping des Beats

Identifie les beats narratifs du chapitre et évalue leur impact.

> **Référence:** Consultez `data/references/beat-mapping-system.md` pour:
> - Définitions des types de beats (reveal, reversal, decision, action, emotional)
> - Processus d'identification des beats
> - Système d'évaluation de l'impact
> - Distribution optimale des beats
> - Modèle de cartographie

**Processus:**
```
Beats identifiés:

1. [15%] REVEAL - Le secret de Marcus exposé → Tension +2
2. [40%] DECISION - Emma choisit de partir → Pivot narratif
3. [75%] REVERSAL - L'allié devient antagoniste → Peak tension
4. [90%] EMOTIONAL - Réconciliation → Résolution
```

### 5. Évaluation du Flow

Analyse la fluidité de lecture à travers les composantes du flow.

> **Référence:** Consultez `data/references/flow-assessment-criteria.md` pour:
> - Analyse du rythme des phrases (longueur, structure, variété)
> - Analyse du rythme des paragraphes (longueur, organisation)
> - Évaluation du momentum et de la continuité
> - Système de scoring complet (0-10)
> - Problèmes courants et solutions

**Processus:**
Évaluez les 5 composantes du flow: rythme des phrases, rythme des paragraphes, momentum, continuité, et immersion.

### 6. Balance Action/Réflexion

Calcule le ratio global:

```
Balance Action/Réflexion:

Action:     ████████████████░░░░ (65%)
Réflexion:  ███████░░░░░░░░░░░░░ (35%)

→ Dans la zone optimale (60-70% / 30-40%)
```

---

## Synthèse d'Analyse

Compile les résultats:

```
Analyse complète du chapitre {N}:

PACING:     {score}/10 - {assessment}
TENSION:    {score}/10 - {assessment}
TRANSITIONS:{score}/10 - {assessment}
BEATS:      {score}/10 - {assessment}
FLOW:       {score}/10 - {assessment}
BALANCE:    {score}/10 - {assessment}

SCORE GLOBAL: {average}/10

Points forts:
- {strength_1}
- {strength_2}

Points d'attention:
- {issue_1}
- {issue_2}
```

---

## Validation

Avant de générer le rapport:
- [ ] Pacing de chaque scène analysé
- [ ] Courbe de tension cartographiée
- [ ] Transitions évaluées
- [ ] Beats identifiés et mappés
- [ ] Flow et balance analysés
- [ ] Scores calculés

---

## Navigation

**Step précédent:** [Step 02: Load](step-02-load.md)
**Prochain step:** [Step 04: Report](step-04-report.md)
