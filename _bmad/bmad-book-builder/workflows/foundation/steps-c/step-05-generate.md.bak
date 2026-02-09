---
name: 'step-05-generate'
description: 'Generate the phase-based story structure by applying the selected framework to the discovered elements'

# File References
thisStepFile: './step-05-generate.md'
nextStepFile: './step-06-review.md'
outputFile: '{bbb_output_folder}/chapter-plan-{project_name}.md'
chapterPlanTemplate: '../data/chapter-plan-template.md'

# Framework Data Files
saveTheCatData: '../data/save-the-cat.md'
herosJourneyData: '../data/heros-journey.md'
snowflakeMethodData: '../data/snowflake-method.md'
customFrameworkData: '../data/custom-framework.md'
methodeVareilleData: '../data/vareille-method.md'

# Reference Documents
structureGenerationGuide: '../data/templates/structure-generation-guide.md'
structureOutputTemplate: '../data/templates/structure-output-template.md'

# Tools (optional)
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 5: Generate Story Structure

## STEP GOAL:

To apply the selected framework to the discovered story elements, generating a complete phase-based story structure with objectives, conflicts, character evolution, and transitions for each phase.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 THIS STEP IS AUTONOMOUS — generate structure based on gathered inputs
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE NOW A GENERATOR, synthesizing all previous inputs
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Story Architect** — now in blueprint mode
- ✅ Use all gathered information (concept, framework, characters, world, themes)
- ✅ Apply framework systematically to create structure
- ✅ Ensure every phase has clear purpose and connections
- ✅ Architectural metaphors: building the blueprint, laying out the floor plan

### Step-Specific Rules:

- 🎯 Focus ONLY on generating the phase structure
- 🚫 FORBIDDEN to skip the framework application
- 💬 Prescriptive approach: systematic application of framework
- 🏗️ Ensure structural integrity — every phase must earn its place

## EXECUTION PROTOCOLS:

- 🎯 Load complete output document (concept + discovery)
- 🎯 Load structure generation guide for templates and principles
- 💾 Generate and append phase structure to output document
- 📖 Update frontmatter `stepsCompleted` to add 5 before loading next step
- 🚫 FORBIDDEN to load next step until structure is generated

## CONTEXT BOUNDARIES:

- Complete story concept from step 2
- Selected framework from step 3
- Four pillars discovery from step 4
- All framework data files available
- Structure generation guide provides comprehensive templates
- Generate structure based on ALL gathered inputs

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Generation Phase

"**The moment has come to build the plan.** 🏛️

I now have everything I need to draw the architecture of your story:
- ✅ Your concept and vision
- ✅ The **[framework name]** framework
- ✅ Your characters, world, and themes
- ✅ The key elements of the framework

Give me a moment to assemble all of this into a coherent structure..."

### 2. Load Framework Data and Generation Guide

Load the appropriate framework file based on `framework` in frontmatter:
- Save the Cat → {saveTheCatData}
- Hero's Journey → {herosJourneyData}
- Snowflake Method → {snowflakeMethodData}
- Marie Vareille → {methodeVareilleData}
- Custom → {customFrameworkData}

Load {structureGenerationGuide} for:
- Phase structure template
- Framework-to-phase mapping
- Structural analysis templates
- Verification checklist
- Generation principles

### 3. Generate Phase Structure

**Apply framework to create PHASES (not chapters) using templates from {structureOutputTemplate} and {structureGenerationGuide}:**

- Determine number of phases based on framework mapping from the guide
- For each phase, use the phase structure template
- Add structural analysis sections (3-act mapping, parallel threads, pacing)
- Add verification checklist

See {structureOutputTemplate} for complete output structure templates.
See {structureGenerationGuide} for generation principles and framework mappings.

### 4. Append Structure to Output

Append the complete generated structure to {outputFile}, after the discovery sections, using the template from {structureOutputTemplate}.

Update frontmatter:
- Add `5` to `stepsCompleted` array
- Add `structureGenerated: true`

Update frontmatter:
- Add `5` to `stepsCompleted` array
- Add `structureGenerated: true`

### 7. Present Generated Structure

"**Here is your story’s architecture!** 🏛️

[Brief summary of phases generated]

**Strengths of this structure:**
- [Strength 1]
- [Strength 2]

**Areas to watch:**
- [Potential weakness or area needing attention]

Take the time to read the full plan. In the next step, we’ll review it together and make any needed adjustments."

### 8. Present MENU OPTIONS

Display: **Structure generated - Select an option:**
- **[A]** Advanced Elicitation — Explore an aspect of the structure
- **[P]** Party Mode — Get perspectives on the structure
- **[C]** Continue to review and adjustments

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After A or P execution, return to this menu

#### Menu Handling Logic:

- **IF A:** Execute {advancedElicitationTask}, then redisplay menu
- **IF P:** Execute {partyModeWorkflow}, then redisplay menu
- **IF C:** Update frontmatter stepsCompleted, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Complete phase structure generated based on ALL gathered inputs
- Framework systematically applied using generation guide templates
- Each phase has: objectives, conflicts, character evolution, transitions
- 3-act mapping included
- Parallel threads identified
- Pacing analysis provided
- Verification checklist included
- Structure appended to output document
- Frontmatter updated

### ❌ SYSTEM FAILURE:

- Generating generic structure not based on user's specific inputs
- Skipping framework application
- Creating chapters instead of phases
- Missing key structural elements (transitions, arcs, threads)
- Not using the discovery from step 4
- Generating without loading all relevant context
- Not using the generation guide templates

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and structure is fully generated will you update frontmatter and load {nextStepFile} to begin the review phase.
