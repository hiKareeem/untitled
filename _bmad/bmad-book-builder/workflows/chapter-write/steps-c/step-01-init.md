---
name: 'step-01-init'
description: 'Initialize chapter writing and discover all required inputs'

# Navigation
nextStepFile: './step-02-brief.md'
continueFile: './step-01b-continue.md'

# Output
outputFile: '{bbb_output_folder}/chapters/chapter-{chapter_number}.md'
metaFile: '{bbb_output_folder}/chapters/chapter-{chapter_number}-meta.yaml'
chapterTemplate: '../data/chapter-template.md'
metaTemplate: '../data/meta-template.yaml'

# Input Discovery - 7 REQUIRED INPUTS
inputDocuments: []
requiredInputCount: 7

# Input Sources
chapterPlanFolder: '{bbb_output_folder}/foundation/'
styleProfilePath: '{bbb_output_folder}/style-profile.md'
storyBiblePath: '{bbb_output_folder}/bible/'
chaptersFolder: '{bbb_output_folder}/chapters/'
thematicContextPath: '{bbb_output_folder}/thematic-analysis.md'
rhythmGuidelinesPath: '{bbb_output_folder}/rhythm-profile.md'

# Input Patterns
inputFilePatterns:
  - 'chapter-plan-*.md'
  - 'style-profile.md'
  - 'bible-*.md'
  - 'chapter-*-meta.yaml'
  - 'thematic-analysis.md'
  - 'rhythm-profile.md'

# Reference Documents
requiredInputsSpec: '../data/references/required-inputs-specification.md'
preWritingChecklist: '../data/references/pre-writing-checklist.md'
executionModesSpec: '../data/references/execution-modes.md'
---

# Step 1: Initialize Chapter Writing

## STEP GOAL:

To check for existing workflow continuation, gather the chapter number from the user, and discover/load all 7 required input documents before proceeding to chapter brief.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:

- You are a **Chapter Writer** collaborating with an author
- This is a partnership - you bring narrative craft expertise, the author brings creative vision
- We engage in collaborative dialogue, not command-response
- You help transform chapter plans into authentic prose

### Step-Specific Rules:

- Focus ONLY on initialization and input discovery
- FORBIDDEN to start writing chapter content in this step
- ALL 7 inputs are REQUIRED - workflow cannot proceed without them
- Check for existing workflow before starting new

## EXECUTION PROTOCOLS:

- Check for existing chapter output before new workflow
- Discover and load all 7 required inputs
- Create output file from template
- Update frontmatter stepsCompleted when complete
- FORBIDDEN to load next step until all inputs loaded

## CONTEXT BOUNDARIES:

- This is the first step - no prior context exists
- All inputs must be discovered from prior workflows
- Chapter number determines which plan to use and which summaries to load
- Focus: Setup and discovery, not content generation

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Check for Existing Workflow

Look for existing chapter output file at {outputFile}:

- **IF EXISTS and has `stepsCompleted` array:**
  → "Found an existing chapter in progress. Let me check where we left off..."
  → STOP and load {continueFile}

- **IF NOT EXISTS:**
  → Continue to step 2

### 2. Welcome and Gather Chapter Number

"**Welcome to Chapter Write!**

I'll help you write a complete chapter in your authentic voice. Before we begin, I need to gather all the necessary context.

**Which chapter are you writing?**

Please provide the chapter number (e.g., 1, 2, 3...):"

Wait for user to provide chapter number. Store as `{chapter_number}`.

### 3. Discover Required Inputs

"**Gathering required context for Chapter {chapter_number}...**"

Search for and validate ALL 7 required inputs per `{requiredInputsSpec}`:

**Validation Protocol:**
- Read `{requiredInputsSpec}` for detailed specification of each input
- Follow the validation checks specified for each input
- Present discovery results table as specified

**Quick Reference:**
- Input 1: Chapter Plan → `{chapterPlanFolder}/chapter-plan-{chapter_number}.md`
- Input 2: Style Profile → `{styleProfilePath}`
- Input 3: Story Bible → `{storyBiblePath}` (bible files)
- Input 4: Previous Summaries → `{chaptersFolder}/chapter-*-meta.yaml` (if chapter > 1)
- Input 5: Thematic Context → `{thematicContextPath}`
- Input 6: Rhythm Guidelines → `{rhythmGuidelinesPath}`

### 4. Validate Discovery Results

Present discovery summary as specified in `{requiredInputsSpec}`.

**IF ANY INPUT MISSING:**
"Cannot proceed - missing required inputs. Please complete the workflows indicated above."
→ STOP workflow

**IF ALL INPUTS FOUND:**
"All required inputs found! Loading context..."
→ Continue to step 5

### 5. Offer Execution Mode

Offer execution mode choice as specified in `{executionModesSpec}`.

**Process:**
- Present mode selection options (Quick Start vs Full Review)
- Wait for user selection
- Store as `{execution_mode}` (values: 'quick', 'full')

**Branching Logic:**
- **IF Quick Start:** Skip to step 6 (Create Output File), then proceed to step-02-brief
- **IF Full Review:** Continue to step 5.5 below

### 5. Load All Inputs (Full Review Mode ONLY)

Load and read each input document as specified in `{requiredInputsSpec}`:

1. **Chapter Plan:** Load and store key points, goals, scene breakdown
2. **Style Profile:** Load quantitative and qualitative style traits
3. **Story Bible:** Load character details, locations, objects, rules
4. **Previous Summaries:** Load summaries and keyPoints from all prior chapters
5. **Thematic Context:** Load themes, motifs, emotional arcs
6. **Rhythm Guidelines:** Load pacing patterns, sentence distributions

"**Context loaded successfully!**

Ready to write Chapter {chapter_number}: {chapter_title_from_plan}"

### 5.5. Pre-Writing Checklist (Full Review Mode ONLY)

Execute the pre-writing checklist as specified in `{preWritingChecklist}`.

**Process:**
- Read `{preWritingChecklist}` for complete 22-point checklist
- Systematically verify each item across 4 categories
- Report any missing elements: "⚠️ Missing: [item]. Please address before proceeding."
- ONLY when ALL items checked: "✅ All checklist items verified!"

**Completion:** Present completion message as specified in `{preWritingChecklist}`.

### 6. Create Output File

Create new chapter output file from {chapterTemplate}:

- Set `chapterNumber: {chapter_number}`
- Set `createdDate: {current_date}`
- Set `author: {user_name}`
- Set `stepsCompleted: ['step-01-init']`
- Set `lastStep: 'step-01-init'`

### 7. Present Status and Continue

Display completion message as specified in `{executionModesSpec}` for the selected mode.

**Process:**
- Present mode-specific status display (Quick Start or Full Review)
- Present common closing menu
- Handle menu selection as specified

**Menu Options:**
- `[C]` Continue to Brief
- Handle other inputs per menu handling logic

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Continuation check performed
- Chapter number gathered from user
- All 7 required inputs discovered and validated
- All inputs loaded into context
- Output file created from template
- Frontmatter updated with stepsCompleted

### SYSTEM FAILURE:

- Starting chapter without all 7 inputs
- Skipping continuation check
- Proceeding with missing required inputs
- Not loading input documents into context
- Not creating output file

**Master Rule:** ALL 7 inputs are REQUIRED. Do not proceed without complete context.
