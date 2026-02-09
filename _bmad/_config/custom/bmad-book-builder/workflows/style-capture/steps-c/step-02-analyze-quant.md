---
name: 'step-02-analyze-quant'
description: 'Calculate quantitative metrics: TTR, sentence length, complexity, paragraph variation'

# Navigation
nextStepFile: './step-03-analyze-qual.md'

# Data sources (from previous step)
samplesSource: '{collected_samples}'
wordCount: '{word_count}'

# Reference documents
formulasReference: './data/references/style-metrics-formulas.md'
---

# Step 2: Quantitative Analysis

## STEP GOAL:
To calculate precise quantitative metrics (TTR, sentence length, complexity ratio, paragraph variation) from the collected writing samples.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- ✅ You are the **Style Coach** performing technical quantitative analysis
- This step requires precision — metrics must be calculated correctly
- Your goal: Generate accurate numerical data for the style profile
- No creative interpretation here — follow the mathematical formulas exactly

### Step-Specific Rules:
- 🎯 Focus ONLY on quantitative metrics calculation
- 🚫 FORBIDDEN to add qualitative analysis in this step (that's step 3)
- 📏 Use exact formulas from {formulasReference} — no shortcuts or approximations
- ⚠️ Validate minimum word count before calculations
- 💾 Store results for step 05 (YAML generation)

## EXECUTION PROTOCOLS:
- Perform all four metric calculations in order
- Store results as structured data for later use
- Display findings to user for transparency
- Auto-proceed to step 03 (no user choice needed)

## CONTEXT BOUNDARIES:
- This step runs autonomously — no user interaction required
- Input: {collected_samples} from step 01
- Output: {quantitative_metrics} for step 05
- Focus: Mathematical precision, not creative analysis
- Dependencies: Step 01 must have collected samples
- Reference: {formulasReference} for all calculation formulas

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Validate Input

Display: "**📊 Starting Quantitative Analysis...**"

Check that {word_count} >= 100:

**IF word_count < 100:**

Display: "⚠️ **Insufficient Sample Size**

You have provided {word_count} words. This is below the minimum required (100 words) for reliable TTR calculation.

Please return to Step 1 and provide more writing samples."

**HALT and wait for user.**

**IF word_count >= 100:**

Continue to calculations.

### 2. Calculate TTR (Type-Token Ratio)

**Reference:** See TTR section in {formulasReference} for formula, procedure, and assessment templates

**Procedure:** Tokenize, count unique words, calculate TTR = unique/total, store as {ttr_value}

**Target:** > 0.175 (PASS if >=, ALERT if <)

**Assessment:** Use templates from reference based on status

### 3. Calculate Average Sentence Length

**Reference:** See Average Sentence Length section in {formulasReference} for formula, procedure, and assessment templates

**Procedure:** Split into sentences, count, calculate avg = words/sentences, store as {avg_sentence_length}

**Target:** 20-24 words (PASS if in range, ALERT if outside)

**Assessment:** Use templates from reference based on status

### 4. Calculate Sentence Complexity Ratio

**Reference:** See Sentence Complexity Ratio section in {formulasReference} for formula, definitions, procedure, and assessment templates

**Procedure:** Analyze sentences for complexity markers (subordinating/relative pronouns, conjunctions), calculate ratio, store as {complex_percentage} and {simple_percentage}

**Target:** 80% complex / 20% simple (PASS if 70-90%, ALERT otherwise)

**Assessment:** Use templates from reference based on status

### 5. Calculate Paragraph Length Variation

**Reference:** See Paragraph Length Variation section in {formulasReference} for procedure, categorization, and assessment templates

**Procedure:** Split into paragraphs, categorize (Short: 1-2, Medium: 3-6, Long: 7+), calculate percentages, store as {short_paragraph_pct}, {medium_paragraph_pct}, {long_paragraph_pct}

**Target:** Mixed distribution (MIXED if no category > 70%, VARIATION_NEEDED otherwise)

**Assessment:** Use templates from reference based on status

### 6. Display Results

Display:

"**📊 Quantitative Analysis Complete**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| **TTR (Lexical Diversity)** | {ttr_value:.3f} | > 0.175 | {ttr_status} |
| **Avg Sentence Length** | {avg_sentence_length:.1f} words | 20-24 | {sentence_status} |
| **Sentence Complexity** | {complex_percentage}% complex / {simple_percentage}% simple | 80%/20% | {complexity_status} |
| **Paragraph Variation** | Short: {short_paragraph_pct}% / Medium: {medium_paragraph_pct}% / Long: {long_paragraph_pct}% | Mixed | {paragraph_status} |

**Assessments:**

**TTR:** {ttr_assessment}
**Sentence Length:** {sentence_assessment}
**Complexity:** {complexity_assessment}
**Paragraphs:** {paragraph_assessment}

These metrics establish the quantitative foundation of your writing voice. Next: Qualitative pattern analysis."

### 7. Store Results for Later Use

Create structured data object {quantitative_metrics}:

```
ttr:
  value: {ttr_value}
  target: "> 0.175"
  status: {PASS/ALERT}
  assessment: {ttr_assessment}

sentence_length:
  value: {avg_sentence_length}
  target: "20-24 words"
  status: {PASS/ALERT}
  assessment: {sentence_assessment}

complexity:
  complex_percentage: {complex_percentage}
  simple_percentage: {simple_percentage}
  target: "80% complex / 20% simple"
  status: {PASS/ALERT}
  assessment: {complexity_assessment}

paragraph_variation:
  short_percentage: {short_paragraph_pct}
  medium_percentage: {medium_paragraph_pct}
  long_percentage: {long_paragraph_pct}
  target: "Mixed"
  status: {MIXED/VARIATION_NEEDED}
  assessment: {paragraph_assessment}
```

### 8. Auto-Proceed to Next Step

Display: "**Proceeding to Qualitative Pattern Analysis...**"

#### Menu Handling Logic:
- After displaying results, immediately load, read entire file, then execute {nextStepFile}

#### EXECUTION RULES:
- This is an autonomous analysis step with no user choices
- Proceed directly to next step after calculations complete

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- All four metrics calculated correctly (TTR, sentence length, complexity, paragraph variation)
- Results displayed to user
- Data stored for step 05 YAML generation
- Proceeded to step 03 without error

### ❌ SYSTEM FAILURE:
- Skipping metric calculations
- Using incorrect formulas
- Not validating minimum word count
- Not displaying results
- Not storing data for later use

**Master Rule:** Quantitative precision is CRITICAL. These metrics are the foundation of the style profile. All calculations must be mathematically correct. Reference {formulasReference} for exact formulas.
