---
name: 'step-05-configure'
description: 'Generate complete framework configuration for Foundation workflow'

# Navigation
# This is the final step — no nextStepFile

# Input/Output
outputFile: '{bbb_output_folder}/foundation/framework-selection.yaml'

# Framework Data
frameworkDefinitions: './data/'
frameworkSelectionTemplate: './data/framework-selection-template.yaml'
---

# Step 5: Configure

## STEP GOAL:
To generate the complete `framework-selection.yaml` configuration file with full framework structure, reasoning, and Foundation integration settings.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER skip structural elements
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A CONFIGURATOR, generating complete output
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- ✅ You are the **Story Architect** completing the framework setup
- Generate complete, usable configuration
- Ensure Foundation has everything needed
- Your goal: Production-ready output

### Step-Specific Rules:
- 🎯 Generate COMPLETE framework structure
- 🚫 FORBIDDEN to skip beats/phases/steps
- 💬 Include all reasoning and metadata
- 📊 Create Foundation integration config
- ✅ VALIDATE output before completing

## EXECUTION PROTOCOLS:
- Load selected framework definition
- Generate complete framework structure
- Create Foundation configuration settings
- Write complete YAML output
- Validate output completeness
- Present completion summary

## CONTEXT BOUNDARIES:
- Selection made in Step 4
- Framework definitions in data files
- Focus: Configuration generation, not more education
- This is the final step — produce complete output

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise.

### 1. Load Framework Definition

Read `{outputFile}` to get `selectedFramework`.

Load framework definition from `{frameworkDefinitions}`:

**IF `save-the-cat`:**
- Load `save-the-cat.yaml`
- Extract all 15 beats with purposes

**IF `heros-journey`:**
- Load `heros-journey.yaml`
- Extract all 12 stages with purposes

**IF `snowflake`:**
- Load `snowflake.yaml`
- Extract all 10 steps with purposes

**IF `custom`:**
- Use `customFramework.description` from output file
- Generate structure based on author's description

### 2. Generate Framework Reasoning

Generate comprehensive reasoning for the selection using template:

```yaml
frameworkReasoning: |
  Based on your {genre} story with {scope} scope, {framework_name}
  was selected because:

  - {Reason 1: Specific story element that aligns with framework}
  - {Reason 2: Author goal that framework supports}
  - {Reason 3: Structural benefit for this story type}

  This framework will provide {key benefits} while maintaining
  flexibility for your creative process.

  {For custom:}
  Your custom approach was chosen because it aligns with your
  unique storytelling style: {brief description}.
```

### 3. Generate Framework Structure

Load appropriate structure template from `{frameworkDefinitions}/templates/`:

- `save-the-cat-structure-template.yaml` (for Save the Cat)
- `heros-journey-structure-template.yaml` (for Hero's Journey)
- `snowflake-structure-template.yaml` (for Snowflake Method)
- `custom-framework-template.yaml` (for Custom Framework)

For detailed information about each structure, see:
- `references/save-the-cat-structure.md`
- `references/heros-journey-structure.md`
- `references/snowflake-structure.md`
- `references/framework-overview.md`

### 4. Generate Foundation Configuration

Create configuration settings for Foundation workflow using template from `{frameworkDefinitions}/templates/framework-configuration-template.yaml`

Load act breakpoints from `{frameworkDefinitions}/templates/act-breakpoints-template.yaml` for the selected framework.

For detailed configuration procedures, see `{frameworkDefinitions}/references/framework-selection-procedures.md` - section "Step 5: Configuration Procedure"

### 5. Write Complete Output File

Write complete YAML to `{outputFile}`:

```yaml
---
stepsCompleted: ['step-01-analyze', 'step-02-recommend', 'step-03-explain', 'step-04-select', 'step-05-configure']
lastStep: 'step-05-configure'
date: '{current_date}'
user_name: '{user_name}'
workflow: 'framework-select'
version: '1.0.0'

# Framework Selection
selectedFramework: '{framework_name}'
frameworkReasoning: |
  {complete reasoning}

# Framework Structure
frameworkStructure:
  {complete structure as defined above}

# Foundation Integration
foundationConfig:
  {complete config as defined above}

# Story Analysis (from Step 1)
storyAnalysis:
  concept: '{story_concept}'
  genre: '{story_genre}'
  scope: '{story_scope}'
  audience: '{target_audience or null}'
  experienceLevel: '{author_experience or null}'

# Recommendations (from Step 2)
recommendations:
  primary: '{primary_recommendation}'
  secondary: [{secondary_recommendations}]
  reasoning: '{recommendation_reasoning}'

# Custom Framework (if applicable)
customFramework:
  {custom framework data or null}

# Metadata
selectionDate: '{current_date}'
configuredFor: 'Foundation workflow'
status: 'complete'
---
```

### 6. Validate Output

Verify the output file contains:

- ✅ `selectedFramework` set
- ✅ `frameworkReasoning` complete and detailed
- ✅ `frameworkStructure` with all beats/stages/steps
- ✅ `foundationConfig` with appropriate settings
- ✅ `storyAnalysis` preserved
- ✅ `recommendations` preserved
- ✅ `stepsCompleted` includes all 5 steps
- ✅ `status: complete`

**IF any missing:**
- Add missing elements
- Re-validate

### 7. Present Completion Summary

Display completion message from `{frameworkDefinitions}/references/framework-completion-message.md` - section "Step 5: Framework Configuration Complete"

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

For success/failure metrics, see `{frameworkDefinitions}/references/framework-selection-procedures.md` - section "Quality Assurance"

**Master Rule:** The output file must be COMPLETE and PRODUCTION-READY. Foundation will use this file directly — it cannot have missing or incomplete data. Validate thoroughly before completing.
