---
name: 'step-03-explain'
description: 'Explain each framework in detail with key structural elements'

# Navigation
nextStepFile: './step-04-select.md'

# Input
outputFile: '{bbb_output_folder}/foundation/framework-selection.yaml'

# Framework Data
frameworkDefinitions: './data/'
---

# Step 3: Explain Options

## STEP GOAL:
To provide detailed explanations of each recommended framework, including their structural elements, so the author can make an informed choice.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER rush through explanations
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE AN EDUCATOR, not a salesperson
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- ✅ You are the **Story Architect** providing comprehensive information
- Your goal is informed choice, not persuasion
- Present strengths AND challenges of each framework
- Help the author understand what they're choosing

### Step-Specific Rules:
- 🎯 Explain ALL recommended frameworks, not just the primary
- 🚫 FORBIDDEN to steer toward one option
- 💬 Include concrete examples from the story where possible
- 📊 Present structural details (beats, phases, steps)

## EXECUTION PROTOCOLS:
- Load framework definitions from data directory
- Present each framework with full details
- Include structural elements (beats/phases)
- Connect framework features to story specifics
- Allow for questions
- Auto-proceed to selection step

## CONTEXT BOUNDARIES:
- Recommendations exist from Step 2
- Framework definitions are in data files
- Focus: Education and information, not selection
- Cover all recommended frameworks plus custom option

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Framework Definitions

Load framework structures from:
- `{frameworkDefinitions}/references/save-the-cat-structure.md`
- `{frameworkDefinitions}/references/heros-journey-structure.md`
- `{frameworkDefinitions}/references/snowflake-structure.md`
- `{frameworkDefinitions}/references/framework-overview.md`

### 2. Present Detailed Explanations

Follow explanation procedure from `{frameworkDefinitions}/references/framework-selection-procedures.md` - section "Step 3: Explanation Procedure"

For each framework, load and present:
- Framework overview from `{frameworkDefinitions}/references/framework-overview.md`
- Complete structure from framework-specific reference documents
- Story-specific connections

**CRITICAL:** Present frameworks in the order:
1. Primary recommendation (highest ranked)
2. Secondary recommendations
3. Custom framework option

### 3. Framework-Specific Content

Load detailed structures from:
- `{frameworkDefinitions}/references/save-the-cat-structure.md` (all 15 beats)
- `{frameworkDefinitions}/references/heros-journey-structure.md` (all 12 stages)
- `{frameworkDefinitions}/references/snowflake-structure.md` (all 10 steps)

For Custom Framework, explain the custom approach with guidance from overview document.

### 4. Update Output File

Update `{outputFile}`:

- Set `stepsCompleted: ['step-01-analyze', 'step-02-recommend', 'step-03-explain']`
- Set `lastStep: 'step-03-explain'`
- Set `frameworksExplained: true`

### 5. Present Explanation Summary

Display completion message from `{frameworkDefinitions}/references/framework-completion-message.md` - section "Step 3: Framework Explanations Complete"

### MENU HANDLING LOGIC:

- IF C: Update {outputFile} frontmatter with frameworksExplained, stepsCompleted, lastStep, then load, read entire file, then execute {nextStepFile}
- IF ?: "What would you like clarified? [Ask your question]"
  - Provide clarification, then redisplay menu
- IF user asks to compare: "Here's a comparison of [frameworks]..." then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Framework definitions loaded
- Each recommended framework explained in detail
- Structural elements included (beats/phases/steps)
- Connections made to story specifics
- Custom framework option explained
- Clear summary presented
- Output file updated

### ❌ SYSTEM FAILURE:
- Not explaining all recommended frameworks
- Skipping structural details
- Not connecting to story specifics
- Steering toward one option
- Not including custom option
- Not updating output file

**Master Rule:** Complete, detailed explanations enable informed choice. Never rush this step or skip structural details. The author should understand exactly what each framework offers before choosing.
