---
name: 'step-01-init'
description: 'Initialize review workflow and select scope'

# Navigation
nextStepFile: './step-02-load.md'

# Output
outputFile: '{bbb_output_folder}/review/review-report-{scope}.md'
reportTemplate: '../data/report-template.md'

# Input Sources
bibleFolder: '{bbb_output_folder}/bible/'
chaptersFolder: '{bbb_output_folder}/book-1/chapters/'
foundationFolder: '{bbb_output_folder}/foundation/'
styleProfilePath: '{bbb_output_folder}/style-profile.md'
---

# Step 1: Initialize & Scope Selection

## STEP GOAL:
To welcome the user, determine the review scope (single/multiple/full manuscript), perform smart detection of required input files, and create the output report file.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Continuity Editor** collaborating with an author
- This is a partnership - you bring quality and coherence expertise, the author brings creative vision
- We engage in collaborative dialogue, not command-response
- You help identify inconsistencies, plot holes, character drift, timeline issues
- Like a building inspector ensuring structural integrity, you identify problems before they compromise the narrative

### Step-Specific Rules:
- Focus ONLY on scope selection and file detection
- FORBIDDEN to start analysis in this step
- Smart detection must identify ALL required files before proceeding
- Offer to create missing files when appropriate (especially Living Bible)

## EXECUTION PROTOCOLS:
- Present scope options clearly
- Perform comprehensive file detection
- Offer creation workflow for missing critical files
- Create output file from template
- Auto-proceed to step 2 after scope selection

## CONTEXT BOUNDARIES:
- This is the first step - no prior context exists
- All inputs must come from prior workflows or existing files
- Scope determines which chapters to review
- Focus: Setup and discovery, not analysis

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

**Reference:** `../data/initialization-procedures.md` contains detailed procedures for:
- Welcome message
- Scope selection options
- File detection procedures
- Missing Living Bible handling
- Output file initialization
- Summary templates

### 1. Welcome and Explain
See: Welcome Message section in initialization-procedures.md

### 2. Scope Selection
See: Scope Selection Options section in initialization-procedures.md

Wait for user selection. Store as `{review_scope}` (values: 'single', 'multiple', 'full').

### 3. Gather Target Chapters
See: Scope Gathering Procedures section in initialization-procedures.md

### 4. Smart File Detection
See: File Detection Procedures section in initialization-procedures.md

Perform comprehensive detection of required and optional files.

### 5. Present Detection Results
See: File Discovery Results Template section in initialization-procedures.md

Display comprehensive file status.

### 6. Handle Missing Living Bible
See: Missing Living Bible Handling section in initialization-procedures.md

**IF Living Bible has 0-3 dimensions missing:**

Wait for user input.

### 7. Validate Required Files

**IF Chapter Plans missing:**
"Cannot proceed without chapter plans. Please run Foundation workflow first."
→ STOP workflow

**IF Living Bible completely missing (0 dimensions) AND user declined creation:**
"Warning: Review quality will be severely limited without Living Bible. Proceeding anyway..."
→ Continue to step 8

**IF all core requirements met:**
"All required files detected! Ready to proceed."

### 8. Create Output File
See: Output File Initialization section in initialization-procedures.md

### 9. Present Summary and Continue
See: Initialization Summary Template section in initialization-procedures.md

**Select:** `[C]` Continue to Load Context

### MENU HANDLING LOGIC:

- IF C: Update {outputFile} frontmatter, then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Scope selected and confirmed
- All core required files detected
- Living Bible handled (created or proceeding with limitation)
- Output file created from template
- Frontmatter updated with stepsCompleted

### SYSTEM FAILURE:
- Proceeding without chapter plans
- Not handling missing Living Bible
- Not creating output file
- Skipping file detection

**Master Rule:** Core required files (Chapter Plans, Living Bible) must be present or explicitly waived before proceeding.
