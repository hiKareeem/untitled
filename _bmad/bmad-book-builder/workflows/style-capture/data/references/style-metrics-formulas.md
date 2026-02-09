# Style Metrics Formulas Reference
# Quantitative metrics used by Style Coach for voice analysis

> **Purpose:** This document contains the mathematical formulas and calculation methods for all quantitative style metrics used in BMad Book Builder.

---

## 1. TTR (Type-Token Ratio)

### Formula

```
TTR = (Unique Words / Total Words)
```

### Calculation Steps

1. **Tokenize** the text into words (split by whitespace, remove punctuation)
2. **Count total words** (N)
3. **Create unique word set** (case-insensitive)
4. **Count unique words** (U)
5. **Calculate**: TTR = U / N

### Example

```
Text: "Le chat noir. Le chien blanc. Le chat et le chien."

Words: [le, chat, noir, le, chien, blanc, le, chat, et, le, chien]
Total (N): 9

Unique Words: {le, chat, noir, chien, blanc, et}
Unique (U): 5

TTR = 5 / 9 = 0.556
```

### Interpretation

| TTR Range | Assessment |
|-----------|------------|
| > 0.175 | Excellent vocabulary diversity ✅ |
| 0.150 - 0.175 | Good variety |
| 0.125 - 0.150 | Adequate |
| < 0.125 | Limited vocabulary — consider more variety ⚠️ |

### Minimum Sample Size

**Minimum 100 words** required for reliable TTR calculation.
- Below 100 words: Alert user, request more samples

---

## 2. Average Sentence Length

### Formula

```
ASL = (Total Words / Number of Sentences)
```

### Calculation Steps

1. **Split into sentences** (by . ! ? and paragraph breaks)
2. **Count sentences** (S)
3. **Count total words** (W)
4. **Calculate**: ASL = W / S

### Target

| Range | Assessment |
|-------|------------|
| 20-24 words | Ideal for fiction ✅ |
| 15-19 words | Short, punchy — action scenes |
| 25-30 words | Longer, more complex — literary |
| > 30 words | Too long — consider breaking up ⚠️ |
| < 15 words | Too short — may feel choppy ⚠️ |

---

## 3. Sentence Complexity Ratio

### Formula

```
SCR = (Complex + Compound Sentences / Total Sentences)
```

### Sentence Types

**Simple:** One independent clause
- "She walked to the store."

**Compound:** Two+ independent clauses joined by conjunction
- "She walked to the store, and she bought bread."

**Complex:** Independent + dependent clause(s)
- "She walked to the store because she needed bread."

**Compound-Complex:** Two+ independent + dependent
- "She walked to the store, and she bought bread because she needed it."

### Calculation

1. **Classify each sentence** as simple, compound, or complex
2. **Count non-simple sentences** (C)
3. **Count total sentences** (T)
4. **Calculate**: SCR = C / T

### Target

| Ratio | Assessment |
|-------|------------|
| 70-90% | Good variety ✅ |
| > 90% | May feel overly complex |
| < 70% | May feel too simple |

**Minimum 20% simple sentences** for readability.

---

## 4. Paragraph Length Variation

### Formula

```
CV = (Standard Deviation of Paragraph Lengths / Mean Paragraph Length)
```

### Calculation Steps

1. **Count words per paragraph** (P₁, P₂, ..., Pₙ)
2. **Calculate mean**: μ = ΣP / n
3. **Calculate variance**: σ² = Σ(P - μ)² / n
4. **Calculate std deviation**: σ = √σ²
5. **Calculate coefficient of variation**: CV = σ / μ

### Interpretation

| CV | Assessment |
|----|------------|
| 0.3 - 0.5 | Good rhythm variation ✅ |
| < 0.3 | Too uniform — consider varying paragraph length |
| > 0.5 | High variation — check for consistency |

---

## 5. Transition Words Density

### Formula

```
TWD = (Transition Words / Total Words) × 1000
```

### Common Transition Words

**Addition:** also, and, furthermore, moreover, additionally
**Contrast:** but, however, nevertheless, yet, still
**Cause/Effect:** therefore, thus, consequently, as a result
**Sequence:** first, second, then, next, finally
**Example:** for example, for instance, specifically

### Calculation

1. **Count transition words** (T)
2. **Count total words** (W)
3. **Calculate**: TWD = (T / W) × 1000

### Target

| Range (per 1000 words) | Assessment |
|------------------------|------------|
| 15-25 | Good flow ✅ |
| < 15 | May feel abrupt — add transitions |
| > 25 | Too many — can feel repetitive |

---

## 6. Show vs Tell Ratio

### Classification

**Show:** Descriptive, sensory details, dialogue, action
- "Tears streamed down her face."

**Tell:** Abstract, summary statements
- "She was sad."

### Formula

```
STR = (Show Sentences / Total Sentences) × 100
```

### Target

| Ratio | Assessment |
|-------|------------|
| > 60% | Excellent showing ✅ |
| 40-60% | Good balance |
| < 40% | Too much telling — add sensory details ⚠️ |

---

## Calculation Order (Style-Capture Workflow)

1. **TTR** — Most fundamental, requires all words
2. **ASL** — Requires sentence count (from TTR)
3. **SCR** — Requires sentence classification
4. **CV** — Requires paragraph analysis
5. **TWD** — Can run in parallel
6. **STR** — Requires sentence classification

---

## Error Handling

### Insufficient Data

| Condition | Action |
|-----------|--------|
| Word count < 100 | Alert user, request more samples |
| No sentences found | Check text formatting |
| Single paragraph | Note variation unavailable |

### Anomalies

| Condition | Action |
|-----------|--------|
| TTR = 1.0 | Verify word tokenization |
| TTR < 0.05 | Verify word counting |
| ASL < 5 | Check sentence detection |
| ASL > 100 | May be run-on sentences |

---

*Reference document for BMad Book Builder Style Coach*
