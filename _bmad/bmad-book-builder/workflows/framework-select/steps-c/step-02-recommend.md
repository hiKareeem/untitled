---
name: 'step-02-recommend'
description: 'Recommend appropriate narrative frameworks based on story analysis'

# Navigation
nextStepFile: './step-03-explain.md'

# Input
outputFile: '{bbb_output_folder}/foundation/framework-selection.yaml'

# Framework Data
frameworkDefinitions: './data/'
---

# Step 2: Recommend Framework

## STEP GOAL:
To analyze the story information and recommend the most appropriate narrative framework(s) with clear reasoning.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER recommend without analysis
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE AN ANALYST, not a decision maker
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- ✅ You are the **Story Architect** providing expert analysis
- Your recommendations are based on structural expertise, not personal preference
- Provide reasoned analysis, not arbitrary choices
- Your goal: Give the author informed options

### Step-Specific Rules:
- 🎯 Analyze story attributes against framework strengths
- 🚫 FORBIDDEN to make the final choice for the author
- 💬 Provide clear reasoning for each recommendation
- 📊 Consider multiple factors (genre, scope, experience)

## EXECUTION PROTOCOLS:
- Load story analysis from output file
- Load framework definitions from data directory
- Analyze fit between story and each framework
- Rank recommendations by suitability
- Present recommendations with reasoning
- Auto-proceed to explanation step

## CONTEXT BOUNDARIES:
- Story analysis exists from Step 1
- Framework definitions are in data files
- Focus: Analysis and recommendation, not final selection
- Always provide 2-3 options, never just one

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Story Analysis

Read `{outputFile}` and extract:

- `storyAnalysis.concept`
- `storyAnalysis.genre`
- `storyAnalysis.scope`
- `storyAnalysis.audience`
- `storyAnalysis.experienceLevel`

Display:

"**📊 Analyzing Your Story...**

Based on the story information you provided, I'm now analyzing which narrative frameworks would best serve your story.

<analysis in progress>"

### 2. Load Framework Definitions

Load framework overview from `{frameworkDefinitions}/references/framework-overview.md`

For each framework, extract:
- Framework name and description
- Best-suited genres and story types
- Key structural elements
- Complexity level
- Author experience suitability

### 3. Analyze Framework Fit

Follow analysis framework from `{frameworkDefinitions}/references/framework-selection-procedures.md` - section "Step 2: Framework Analysis Procedure" → "Analysis Framework"

Calculate suitability scores for each framework based on story attributes.

### 4. Rank Recommendations

Follow ranking logic from `{frameworkDefinitions}/references/framework-selection-procedures.md` - section "Step 2: Framework Analysis Procedure" → "Ranking Logic"

### 5. Generate Recommendation Report

Create detailed recommendations using the format from `{frameworkDefinitions}/references/framework-selection-procedures.md` - section "Step 2: Framework Analysis Procedure" → "Ranking Logic"

### 6. Update Output File

Update `{outputFile}`:

- Set `stepsCompleted: ['step-01-analyze', 'step-02-recommend']`
- Set `lastStep: 'step-02-recommend'`
- Set `recommendations.primary: {framework_name}`
- Set `recommendations.secondary: [{framework1}, {framework2}]`
- Set `recommendations.reasoning: {detailed_reasoning}`

### 7. Present Recommendations

Display completion message from `{frameworkDefinitions}/references/framework-completion-message.md` - section "Step 2: Framework Recommendations Complete"

### MENU HANDLING LOGIC:

- IF C: Update {outputFile} frontmatter with recommendations, stepsCompleted, lastStep, then load, read entire file, then execute {nextStepFile}
- IF ?: "Would you like me to clarify any recommendation? [Ask your question or press C to continue]"
  - Provide clarification, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Story analysis loaded from output file
- Framework definitions loaded
- Fit analysis performed for each framework
- Recommendations ranked by suitability
- At least 2-3 options provided (never just 1)
- Clear reasoning provided for each recommendation
- Output file updated with recommendations

### ❌ SYSTEM FAILURE:
- Not analyzing story attributes
- Not providing multiple options
- Making arbitrary recommendations without reasoning
- Not updating output file
- Skipping analysis steps

**Master Rule:** Recommendations must be reasoned and analytical. Never provide a single option or arbitrary choice. Always give the author informed alternatives.
