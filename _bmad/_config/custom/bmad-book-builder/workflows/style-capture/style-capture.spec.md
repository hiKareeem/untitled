# Workflow Specification: StyleCapture

**Module:** bmad-book-builder
**Status:** Placeholder — To be created via create-workflow workflow
**Created:** 2026-01-24

---

## Workflow Overview

**Goal:** Analyze and learn author's writing voice

**Description:** Style Coach analyzes author's writing samples (blog posts, short stories, previous chapters) to extract voice patterns: TTR, sentence length, vocabulary, imagery preferences.

**Workflow Type:** Create-only

---

## Workflow Structure

### Entry Point

```yaml
---
name: style-capture
description: Analyze and learn author's writing voice
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/style-capture'
---
```

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Collect Samples | Get writing samples from author (min 2000 words recommended) |
| 2 | Analyze Quantitative Metrics | **Calculate TTR, sentence length, complexity ratio** (CRITICAL — see Quantitative Metrics below) |
| 3 | Identify Qualitative Patterns | Favorite words, phrases, imagery themes, transitions |
| 4 | Detect Anti-Patterns | Generic patterns to avoid (slop detection) |
| 5 | Generate Profile | Create comprehensive style profile for Chapter Writer |

---

## Quantitative Metrics — CRITICAL REQUIREMENT

> **🎯 EXIGENCE CRITIQUE — Basée sur l'analyse AgentAdam vs BBB**
>
> AgentAdam utilise des **métriques quantitatives précises** pour maintenir la cohérence du style. BBB doit implémenter ces métriques pour atteindre la parité.
>
> **Référence :** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (section 3)
>
> **Sans ces métriques, le style Coach manque de rigueur et ne peut garantir la cohérence vocale.**

### Required Metrics:

| Metric | Target | Calculation | Purpose |
|--------|--------|-------------|---------|
| **TTR (Type-Token Ratio)** | > 0.175 | (Unique Words / Total Words) | Mesure la diversité lexicale |
| **Average Sentence Length** | 20-24 words | (Total Words / Sentences) | Maintient le rythme de l'auteur |
| **Sentence Complexity Ratio** | 80% complex / 20% simple | (Complex Sentences / Total) | Équilibre complexité vs clarté |
| **Paragraph Length Variation** | Mixed for rhythm | Analyze distribution | Crée variation rythmique |

### TTR Calculation Details:
```
TTR = (Nombre de mots uniques / Nombre total de mots)

Exemple :
- Texte : "Le chat noir. Le chien blanc. Le chat et le chien."
- Mots uniques : 5 (le, chat, noir, chien, blanc)
- Total mots : 9
- TTR = 5/9 = 0.556 (excellent)

Seuil minimum : 0.175
Alerte si sous le seuil : Augmenter la diversité vocabulaire
```

### Implementation Requirements for Step 2:
```yaml
Step 2: Analyze Quantitative Metrics
  Actions:
    - Calculate TTR from writing samples
    - Calculate average sentence length
    - Analyze sentence complexity distribution
    - Track paragraph length variation
    - Compare against targets
    - Alert if metrics below threshold
  Output:
    - metrics-section in style-profile.yaml
    - Recommendations for improvement
```

---

## Workflow Inputs

### Required Inputs

- Author's writing samples (blog posts, short stories, previous chapters)
- **Minimum recommended: 2000 words** for reliable metrics calculation

---

## Workflow Outputs

### Output Format

- [X] Document-producing

### Output Files

- `style-profile.yaml` — Author's comprehensive voice profile
  - **quantitative-metrics:** TTR, sentence length, complexity ratio
  - **qualitative-patterns:** Vocabulary, imagery, transitions
  - **anti-patterns:** Slop detection results
  - **recommendations:** Style preservation guidance

---

## Agent Integration

### Primary Agent

Style Coach

---

## Implementation Notes

**Anti-Slop Resources:**
- https://github.com/blader/humanizer — Humanizer tool for making AI text more human-like
- Detect and avoid: excessive adverbs, passive voice, cliché phrases, generic dialogue
- Metrics: lexical diversity, sentence variety, vocabulary richness

---

_This is a specification. Use the create-workflow workflow to build this workflow._
