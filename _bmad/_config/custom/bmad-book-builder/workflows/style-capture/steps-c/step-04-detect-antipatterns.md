---
name: 'step-04-detect-antipatterns'
description: 'Detect anti-patterns: slop, clichés, excessive adverbs, passive voice, generic dialogue'

# Navigation
nextStepFile: './step-05-generate.md'

# Data sources (from previous steps)
samplesSource: '{collected_samples}'
wordCount: '{word_count}'

# Reference documents
antipatternsReference: './data/references/anti-patterns-guide.md'
humanizerTool: 'https://github.com/blader/humanizer'
---

# Step 4: Anti-Pattern Detection

## STEP GOAL:
To detect and catalog anti-patterns (slop, clichés, excessive adverbs, passive voice, generic dialogue) in the collected writing samples, providing specific improvement suggestions.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- ✅ You are the **Style Coach** identifying areas for improvement
- This step requires diagnostic precision and constructive feedback
- Your goal: Help the author recognize and avoid common writing pitfalls
- Provide specific examples and actionable alternatives

### Step-Specific Rules:
- 🎯 Focus ONLY on anti-pattern detection (not qualitative patterns)
- 🚫 FORBIDDEN to criticize author's voice — focus on patterns to avoid
- 💬 Extract representative examples with specific alternatives
- 🔍 Reference {antipatternsReference} for all pattern definitions and examples
- 💾 Store results for step 05 (YAML generation)

## EXECUTION PROTOCOLS:
- Analyze all five anti-pattern categories in order
- Extract representative examples for each category detected
- Provide specific, actionable alternatives for each example
- Display findings to user for transparency
- Auto-proceed to step 05 (no user choice needed)

## CONTEXT BOUNDARIES:
- This step runs autonomously — no user interaction required
- Input: {collected_samples} from step 01
- Output: {anti_patterns} for step 05
- Focus: Generic patterns to avoid, not author-specific issues
- Dependencies: Step 01 must have collected samples
- Reference: {antipatternsReference} for comprehensive anti-pattern definitions

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Initialize Detection

Display: "**🔍 Starting Anti-Pattern Detection...**"

### 2. Detect Excessive Adverbs

**Reference:** See "Excessive Adverbs" section in {antipatternsReference} for patterns, examples, and storage format

**Procedure:** Scan for -ly adverbs, intensifiers, vague modifiers; extract 1-2 examples each; provide stronger verb alternatives

**Storage Format:** Use template from reference

**Minimum:** 3 patterns (or note "none detected")

### 3. Detect Passive Voice Overuse

**Reference:** See "Passive Voice Overuse" section in {antipatternsReference} for markers, examples, and storage format

**Procedure:** Scan for "to be" + past participle, hidden subjects, stative constructions; extract examples; provide active alternatives

**Storage Format:** Use template from reference

**Minimum:** 3 examples (or note "acceptable use - no overuse detected")

### 4. Detect Cliché Phrases

**Reference:** See "Cliché Phrases" section in {antipatternsReference} for patterns, examples, and storage format

**Procedure:** Scan for time-worn metaphors, overused idioms, generic descriptions; extract examples; provide fresh alternatives

**Storage Format:** Use template from reference

**Minimum:** 3 clichés (or note "few clichés detected - original language used")

### 5. Detect Generic Dialogue

**Reference:** See "Generic Dialogue" section in {antipatternsReference} for patterns, examples, and storage format

**Procedure:** Scan for unnatural exposition, on-the-nose emotions, uniform voices, lack of subtext; extract examples; provide improvements

**Storage Format:** Use template from reference

**Minimum:** 3 examples (or note "dialogue feels natural - no generic patterns detected")

**Note:** Only if dialogue exists in samples

### 6. Detect Slop Patterns

**Reference:** See "Slop Patterns" section in {antipatternsReference} for markers, examples, and storage format

**Procedure:** Scan for vague pronouns, noun strings, wordy phrases, filler words; extract examples; provide precise alternatives

**Storage Format:** Use template from reference

**Minimum:** 3 patterns (or note "precise writing - no slop detected")

### 7. Display Results

Display:

"**🔍 Anti-Pattern Detection Complete**

**Excessive Adverbs ({count} patterns detected):**
{For each pattern: original → alternative}

**Passive Voice ({count} examples detected):**
{For each example: original → alternative}

**Cliché Phrases ({count} detected):**
{For each cliché: original → alternative}

**Generic Dialogue ({count} issues detected):**
{For each example: original → alternative}

**Slop Patterns ({count} detected):**
{For each pattern: original → alternative}

**Note:** These are patterns to watch for and avoid. They don't diminish your voice — awareness helps you write stronger prose.

Next: Generate comprehensive style profile."

### 8. Store Results for Later Use

Create structured data object {anti_patterns}:

```
excessive_adverbs:
  {list from step 2}

passive_voice_overuse:
  {list from step 3}

cliche_phrases:
  {list from step 4}

generic_dialogue:
  {list from step 5}

slop_patterns:
  {list from step 6}
```

Store for use in step 05 YAML generation.

### 9. Auto-Proceed to Next Step

Display: "**Proceeding to Profile Generation...**"

#### Menu Handling Logic:
- After displaying results, immediately load, read entire file, then execute {nextStepFile}

#### EXECUTION RULES:
- This is an autonomous analysis step with no user choices
- Proceed directly to next step after detection complete

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- All five anti-pattern categories analyzed
- Representative examples extracted for patterns detected
- Specific, actionable alternatives provided for each example
- "None detected" or "Acceptable" noted when patterns absent
- Results displayed to user
- Data stored for step 05 YAML generation
- Proceeded to step 05 without error

### ❌ SYSTEM FAILURE:
- Skipping anti-pattern categories
- Not providing specific alternatives
- Criticizing author's voice instead of identifying generic patterns
- Not displaying results
- Not storing data for later use

**Master Rule:** Anti-pattern detection is diagnostic, not judgmental. Focus on common writing pitfalls, not the author's unique voice. Provide constructive alternatives that strengthen prose. Reference {antipatternsReference} for comprehensive patterns and examples.
