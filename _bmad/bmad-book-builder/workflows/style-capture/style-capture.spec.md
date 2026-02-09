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

> **🎯 CRITICAL REQUIREMENT — Based on the AgentAdam vs BBB analysis**
>
> AgentAdam uses **precise quantitative metrics** to maintain style coherence. BBB must implement these metrics to achieve parity.
>
> **Reference:** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (section 3)
>
> **Without these metrics, the Style Coach lacks rigor and cannot guarantee vocal coherence.**

### Required Metrics:

| Metric | Target | Calculation | Purpose |
|--------|--------|-------------|---------|
| **TTR (Type-Token Ratio)** | > 0.175 | (Unique Words / Total Words) | Measures lexical diversity |
| **Average Sentence Length** | 20-24 words | (Total Words / Sentences) | Maintains the author's rhythm |
| **Sentence Complexity Ratio** | 80% complex / 20% simple | (Complex Sentences / Total) | Balances complexity vs clarity |
| **Paragraph Length Variation** | Mixed for rhythm | Analyze distribution | Creates rhythmic variation |

### TTR Calculation Details:
```
TTR = (Number of unique words / Total words)

Example:
- Text: "The black cat. The white dog. The cat and the dog."
- Unique words: 5 (the, cat, black, dog, white)
- Total words: 9
- TTR = 5/9 = 0.556 (excellent)

Minimum threshold: 0.175
Alert if below threshold: Increase vocabulary diversity
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
- Detect and avoid: excessive adverbs, passive voice, cliche phrases, generic dialogue
- Metrics: lexical diversity, sentence variety, vocabulary richness

---

_This is a specification. Use the create-workflow workflow to build this workflow._
