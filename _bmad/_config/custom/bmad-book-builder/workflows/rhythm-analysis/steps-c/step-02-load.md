---
name: Load Content
description: Charger le contenu des chapitres sélectionnés et préparer les données
nextStepFile: step-03-analyze.md
---

# Step 02: Load Content

## Objectif

Charger le contenu des chapitres sélectionnés et préparer les données pour l'analyse.

---

## Instructions pour l'Agent

### 1. Charger les Fichiers Chapitres

Pour chaque chapitre dans `chapters_to_analyze`:

```
Lecture des fichiers...
```

Utilise l'outil Read pour charger:
- Le contenu complet du chapitre
- Les métadonnées (si présentes dans le frontmatter)

### 2. Extraire les Métriques de Base

Pour chaque chapitre, calcule:

| Métrique | Description |
|----------|-------------|
| `word_count` | Nombre total de mots |
| `paragraph_count` | Nombre de paragraphes |
| `scene_count` | Nombre de scènes (délimitées par `---` ou `###`) |
| `dialogue_ratio` | Pourcentage de dialogue vs narration |
| `avg_sentence_length` | Longueur moyenne des phrases |

> **Référence:** Voir `data/references/pacing-analysis-framework.md` pour les définitions détaillées des métriques et leurs méthodes de calcul.

### 3. Identifier les Scènes

Parse le chapitre pour identifier:
- Les délimiteurs de scènes (séparateurs, titres de section)
- Le début et fin de chaque scène
- Les personnages présents par scène

Structure de données:
```
scenes:
  - id: 1
    title: {titre_ou_description}
    start_line: {n}
    end_line: {n}
    word_count: {n}
    characters: [{list}]
    location: {lieu}
```

### 4. Charger le Contexte Complémentaire (si disponible)

Tente de charger:
- `story-bible.md` - Structure narrative attendue
- Chapitres précédents (pour comparaison si scope = single)
- `analysis/rhythm-*.md` précédents (pour tendances)

### 5. Confirmer le Chargement

Affiche un résumé:

```
Contenu chargé pour analyse:

📖 Chapitre {N}: "{titre}"
   - {word_count} mots
   - {scene_count} scènes identifiées
   - {paragraph_count} paragraphes
   - Ratio dialogue: {percentage}%

Prêt pour l'analyse de rythme.
```

---

## Validation

Avant de continuer:
- [ ] Tous les chapitres chargés avec succès
- [ ] Métriques de base calculées
- [ ] Scènes identifiées et délimitées
- [ ] Contexte complémentaire chargé (si disponible)

---

## Navigation

**Step précédent:** [Step 01: Init](step-01-init.md)
**Prochain step:** [Step 03: Analyze](step-03-analyze.md)

---

## Gestion des Erreurs

- **Fichier introuvable:** Retourne au Step 01 pour resélectionner
- **Fichier vide:** Signale et propose de skip ou d'attendre
- **Format inattendu:** Tente de parser au mieux, signale les anomalies
