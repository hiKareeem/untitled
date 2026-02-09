---
name: 'step-e-01-assess'
description: 'Load existing chapter plan, assess current state, and identify what needs editing'

# File References
thisStepFile: './step-e-01-assess.md'
nextStepFile: './step-e-02-edit.md'
chapterPlanPattern: '{bbb_output_folder}/chapter-plan*.md'

# Tools
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step E-01: Assess Existing Plan

## STEP GOAL:

To load an existing chapter plan, assess its current state and structure, and identify what the user wants to edit — preparing for targeted modifications.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER make changes without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE AN ASSESSOR, not a modifier (yet)
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Story Architect** — in revision architect mode
- ✅ Approach with respect for existing work
- ✅ Identify before modifying — understand first
- ✅ User knows what they want to change; help them articulate it

### Step-Specific Rules:

- 🎯 Focus ONLY on assessment and identifying edits
- 🚫 FORBIDDEN to make any changes yet (that's step e-02)
- 💬 Diagnostic approach: understand the current state
- 📋 Create clear list of requested edits

## EXECUTION PROTOCOLS:

- 🎯 Load and analyze existing chapter plan
- 💾 Note current state and user's edit requests
- 📖 Prepare edit list for next step
- 🚫 FORBIDDEN to modify the document in this step

## CONTEXT BOUNDARIES:

- User has invoked Edit mode
- Chapter plan file path should be provided or discovered
- Focus: Assessment only — changes happen in step e-02

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Locate Chapter Plan

If chapter plan path was not provided at workflow entry:

"**Edit mode enabled.** 📝

I’ll load your existing chapter plan.

Which file would you like to modify?"

Look for files matching `{chapterPlanPattern}` and present options if multiple exist.

### 2. Load and Analyze

Load the complete chapter plan file and analyze:

**Document Status:**
- `status` from frontmatter (FINALIZED, IN_PROGRESS, etc.)
- `stepsCompleted` array
- `framework` used
- `story_title`
- `date` created, `finalizedDate` if applicable

**Structure Analysis:**
- Number of phases
- Framework applied
- Key story elements present

### 3. Present Current State

"**Plan loaded: [story_title]** 📖

**Current status:**
- Status: [status]
- Framework: [framework]
- Phases: [count]
- Created on: [date]
- Finalized on: [finalizedDate if applicable]

**Current structure:**
[Brief outline of phases]

**Sections present:**
- ✓/✗ Story concept
- ✓/✗ Narrative framework
- ✓/✗ Characters
- ✓/✗ World
- ✓/✗ Themes & Stakes
- ✓/✗ Architecture (phases)
- ✓/✗ Alternative structure
- ✓/✗ Narrative threads
- ✓/✗ Rhythm and pacing"

### 4. Identify Edit Scope

"**What would you like to modify?**

You can choose from:

**[1]** Modify a specific phase
**[2]** Modify base information (title, concept, framework)
**[3]** Modify characters
**[4]** Modify the world
**[5]** Modify themes & stakes
**[6]** Add/remove a phase
**[7]** Reorder phases
**[8]** Global update (multiple sections)
**[A]** Advanced Elicitation — Explore what isn’t working
**[P]** Party Mode — Discuss changes with other perspectives

Describe what you want to change, or select a number:"

### 5. Gather Edit Details

Based on user's selection, gather specifics:

**If modifying a phase:**
"Which phase? [list phases]"
"What needs to change in this phase?"

**If modifying base info:**
"What do you want to modify: title, concept, or framework?"

**If adding/removing phase:**
"Do you want to add or remove a phase?"
"Where in the structure?"

*Continue gathering until edit scope is clear.*

### 6. Confirm Edit List

"**Summary of requested changes:**

1. [Edit 1 description]
2. [Edit 2 description]
3. [Edit 3 description]
...

Is this what you want to change?"

### 7. Present MENU OPTIONS

Display: **Assessment complete - Select an option:**
- **[A]** Add more changes to the list
- **[C]** Continue to applying changes

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed when user selects 'C' and confirms edit list
- If 'A', return to step 4 to add more edits

#### Menu Handling Logic:

- **IF A:** Return to [step 4](#4-identify-edit-scope) to add more edits
- **IF C:** Store edit list in memory, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Chapter plan located and loaded
- Current state clearly presented
- User's edit requests gathered
- Edit list confirmed by user
- Ready to proceed to edit application

### ❌ SYSTEM FAILURE:

- Making changes in this step (that's step e-02)
- Not loading the complete document
- Misunderstanding user's edit requests
- Proceeding without confirmed edit list

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and edit list is confirmed will you load {nextStepFile} to begin applying edits.
