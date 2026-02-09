---
name: 'step-03-analyze-qual'
description: 'Extract qualitative patterns: favorite words, phrases, imagery, transitions'

# Navigation
nextStepFile: './step-04-detect-antipatterns.md'

# Data sources (from previous steps)
samplesSource: '{collected_samples}'
wordCount: '{word_count}'
---

# Step 3: Qualitative Pattern Analysis

## STEP GOAL:
To identify and extract qualitative voice patterns (favorite words, characteristic phrases, imagery themes, and transition patterns) from the collected writing samples.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- ✅ You are the **Style Coach** performing qualitative pattern analysis
- This step requires both analytical precision and creative insight
- Your goal: Identify the distinctive patterns that make this author's voice unique
- Find concrete examples that demonstrate each pattern

### Step-Specific Rules:
- 🎯 Focus ONLY on qualitative pattern extraction
- 🚫 FORBIDDEN to detect anti-patterns in this step (that's step 4)
- 💬 Extract representative examples for each pattern
- 🔍 Look for what makes this voice distinctive, not just common patterns
- 💾 Store results for step 05 (YAML generation)

## EXECUTION PROTOCOLS:
- Analyze all four pattern categories in order
- Extract 3-5 representative examples per category
- Use exact quotations from samples (not paraphrases)
- Display findings to user for transparency
- Auto-proceed to step 04 (no user choice needed)

## CONTEXT BOUNDARIES:
- This step runs autonomously — no user interaction required
- Input: {collected_samples} from step 01
- Output: {qualitative_patterns} for step 05
- Focus: What makes this author's voice distinctive
- Dependencies: Step 01 must have collected samples

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Initialize Analysis

Display: "**🔍 Starting Qualitative Pattern Analysis...**"

### 2. Identify Favorite Words

**Goal:** Find 3-5 words that appear frequently or characteristically in the author's writing.

**Procedure:**
1. Scan {collected_samples} for word frequency patterns
2. Look beyond common words (the, and, is, etc.)
3. Identify distinctive vocabulary choices:
   - Repeated evocative words (e.g., "luminous," "fragmented," "whisper")
   - Characteristic adjectives (e.g., "sharp," "brittle," "warm")
   - Signature nouns (e.g., "shadows," "echoes," "thresholds")
4. For each word, extract 1-2 example sentences showing usage

**Store as:**
```
favorite_words:
  - word: "[word]"
    examples:
      - "[sentence with word in context]"
      - "[another sentence if available]"
```

**Minimum:** 3 words
**Maximum:** 5 words (most distinctive only)

### 3. Identify Characteristic Phrases

**Goal:** Find 3-5 phrases or expressions that are signature to this author's voice.

**Procedure:**
1. Scan for recurring phrases, sentence structures, or expressions
2. Look for distinctive patterns like:
   - Metaphorical expressions (e.g., "time like a river," "silence thick as wool")
   - Characteristic sentence openings (e.g., "In the end," "Looking back now")
   - Signature comparisons (e.g., "like X," "as if Y")
   - Idiosyncratic word combinations
3. For each phrase, extract the full sentence showing context

**Store as:**
```
characteristic_phrases:
  - phrase: "[phrase or expression]"
    examples:
      - "[full sentence showing phrase in context]"
```

**Minimum:** 3 phrases
**Maximum:** 5 phrases

### 4. Identify Imagery Themes

**Goal:** Find 3-5 dominant imagery patterns or metaphorical themes.

**Procedure:**
1. Analyze for recurring imagery categories:
   - Nature imagery (weather, landscapes, seasons)
   - Sensory imagery (textures, sounds, colors, smells)
   - Emotional imagery (weight, light/dark, temperature)
   - Movement imagery (flow, stillness, fragmentation)
   - Spatial imagery (height, depth, distance, containment)
2. Identify the dominant themes across the samples
3. For each theme, extract representative passages

**Store as:**
```
imagery_themes:
  - theme: "[imagery category or theme]"
    examples:
      - "[passage demonstrating this imagery]"
```

**Minimum:** 3 themes
**Maximum:** 5 themes

### 5. Identify Transition Patterns

**Goal:** Find 3-5 characteristic ways the author connects ideas or moves between thoughts.

**Procedure:**
1. Analyze for transition patterns:
   - Sentence-to-sentence transitions (e.g., "And yet," "Meanwhile," "In contrast")
   - Paragraph transitions (e.g., "Hours later," "Looking back," "What she didn't know")
   - Temporal shifts (e.g., flashbacks, time jumps)
   - Perspective shifts (e.g., from external to internal)
2. Extract examples showing each transition type
3. Note if author prefers abrupt vs smooth transitions

**Store as:**
```
transition_patterns:
  - pattern: "[transition type or characteristic connector]"
    examples:
      - "[example showing this transition]"
```

**Minimum:** 3 patterns
**Maximum:** 5 patterns

### 6. Display Results

Display:

"**🔍 Qualitative Pattern Analysis Complete**

**Favorite Words ({count}):**
{For each word: word + example}

**Characteristic Phrases ({count}):**
{For each phrase: phrase + example}

**Imagery Themes ({count}):**
{For each theme: theme + example}

**Transition Patterns ({count}):**
{For each pattern: pattern + example}

**Note:** These examples will be validated by you in the final review step. You can remove any that don't feel representative of your voice.

Next: Anti-pattern detection."

### 7. Store Results for Later Use

Create structured data object {qualitative_patterns}:

```
favorite_words:
  {list from step 2}

characteristic_phrases:
  {list from step 3}

imagery_themes:
  {list from step 4}

transition_patterns:
  {list from step 5}
```

Store for use in step 05 YAML generation.

### 8. Auto-Proceed to Next Step

Display: "**Proceeding to Anti-Pattern Detection...**"

#### Menu Handling Logic:
- After displaying results, immediately load, read entire file, then execute {nextStepFile}

#### EXECUTION RULES:
- This is an autonomous analysis step with no user choices
- Proceed directly to next step after analysis complete

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- All four pattern categories analyzed
- 3-5 examples extracted per category
- All examples are exact quotations (not paraphrased)
- Results displayed to user
- Data stored for step 05 YAML generation
- Proceeded to step 04 without error

### ❌ SYSTEM FAILURE:
- Skipping pattern categories
- Extracting fewer than 3 examples per category
- Using paraphrased examples instead of exact quotations
- Not displaying results
- Not storing data for later use

**Master Rule:** Qualitative patterns reveal the soul of an author's voice. Extract concrete, representative examples that demonstrate what makes this writing distinctive.
