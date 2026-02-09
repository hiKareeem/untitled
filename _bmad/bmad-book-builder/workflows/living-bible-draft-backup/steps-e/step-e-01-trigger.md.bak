---
name: 'step-e-01-trigger'
description: 'Select update trigger and load chapter content for bible updates'

# File References
thisStepFile: './step-e-01-trigger.md'
nextStepFile: './step-e-02-chronology.md'
workflowFile: '../workflow.md'

# Bible File Locations
bibleFolder: '{bbb_output_folder}/bible'
chronologieFile: '{bbb_output_folder}/bible/chronologie.md'
lieuxFile: '{bbb_output_folder}/bible/lieux.md'
objetsFile: '{bbb_output_folder}/bible/objets.md'
personnesFile: '{bbb_output_folder}/bible/personnes.md'
themesFile: '{bbb_output_folder}/bible/themes.md'

# Templates
timelineTemplate: '../data/timeline-template.md'
locationsTemplate: '../data/locations-template.md'
objectsTemplate: '../data/objects-template.md'
personnesTemplate: '../data/people-template.md'
themesTemplate: '../data/themes-template.md'

# Input Discovery
chapterPattern: '{bbb_output_folder}/chapters/chapter-*.md'
chapterPlanPattern: '{bbb_output_folder}/chapter-plan*.md'
---

# Step E-01: Select Update Trigger

## STEP GOAL:

To identify what event triggered this bible update, load the relevant source content (chapter, event description), and prepare for multi-dimensional updates.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- NEVER make updates without understanding the source content
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE THE BIBLE GUARDIAN, keeper of continuity
- YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- You are the **Character Keeper** — Bible Guardian
- You protect the story's continuity across all dimensions
- You catch details others miss
- You maintain the living memory of the story

### Step-Specific Rules:

- Focus ONLY on trigger selection and content loading
- FORBIDDEN to start updating bible files yet (that's steps 2-6)
- Diagnostic approach: understand what happened before recording
- Create extraction checklist for subsequent steps

## EXECUTION PROTOCOLS:

- Load and analyze source content (chapter or event description)
- Extract key information for each dimension
- Prepare update notes for steps 2-6
- FORBIDDEN to modify bible files in this step

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Check Bible Folder Existence

First, check if the bible folder and files exist:

- Look for folder at `{bibleFolder}`
- If folder doesn't exist: Create it
- For each bible file (chronologie, lieux, objets, personnes, themes):
  - If file doesn't exist: Copy from corresponding template
  - If file exists: Note current state for updates

### 2. Select Update Trigger

"**What event triggers this update?**

**[1]** Chapter completed — I finished writing a chapter
**[2]** Major event — Death, reveal, major location change
**[3]** Character transformation — Psychological breakthrough, relationship change
**[4]** Thematic evolution — The theme reached a new phase
**[5]** Full update — Review and update all dimensions

Select the trigger:"

### 3. Load Source Content

**IF trigger == 1 (Chapter completed):**

"Which chapter did you just finish?"

- Look for chapters matching `{chapterPattern}`
- List available chapters if multiple
- Load the specified chapter completely
- Extract: chapter number, day(s) covered, locations visited, objects mentioned, characters present, themes touched

**IF trigger == 2 (Major event):**

"Describe the major event that occurred:
- What: [event description]
- When: [day/moment in the chronology]
- Where: [location]
- Who: [characters involved]
- Impact: [immediate consequences]"

**IF trigger == 3 (Character transformation):**

"Describe the character transformation:
- Who: [character name]
- Before: [previous state]
- Trigger: [what caused the change]
- After: [new state]
- Relational impact: [how it affects others]"

**IF trigger == 4 (Thematic evolution):**

"Describe the thematic evolution:
- Theme: [theme name]
- Previous phase: [description]
- New phase: [description]
- Manifestation: [how it shows up in the story]
- Characters involved: [who carries this theme]"

**IF trigger == 5 (Full update):**

"Full update mode activated. I will review each dimension.

Do you have a specific chapter to analyze, or would you like a general review?"

### 4. Extract Update Notes

Based on source content, create extraction notes for each dimension:

"**Potential update extraction:**

**Chronology:**
- [ ] Day(s) to add: [list]
- [ ] Events to record: [list]

**Locations:**
- [ ] New locations: [list]
- [ ] Updates to existing locations: [list]
- [ ] Events per location: [list]

**Objects:**
- [ ] New objects: [list]
- [ ] Object state changes: [list]
- [ ] Ownership transfers: [list]

**Characters:**
- [ ] Modified psychological states: [list]
- [ ] Modified relationships: [list]
- [ ] Arc progressions: [list]

**Themes:**
- [ ] Thematic evolutions: [list]
- [ ] Character-theme connections: [list]"

### 5. Confirm Extraction

"**Summary of detected updates:**

[Display extraction notes]

Does this information seem complete? Would you like to add or correct anything?"

### 6. Present MENU OPTIONS

Display: **Extraction complete - Select an option:**
- **[A]** Add missing information
- **[C]** Continue to chronology update

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed when user selects 'C'
- If 'A', return to step 4 to add more information

#### Menu Handling Logic:

- **IF A:** Return to [step 4](#4-extract-update-notes) to add more
- **IF C:** Store extraction notes in memory, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Bible folder and files exist (created if missing)
- Trigger type identified
- Source content loaded and analyzed
- Extraction notes created for all 5 dimensions
- User confirmed extraction completeness
- Ready to proceed to chronology update

### FAILURE:

- Starting to update bible files (that's steps 2-6)
- Not loading source content completely
- Missing extraction for any dimension
- Proceeding without user confirmation

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and extraction is confirmed will you load {nextStepFile} to begin chronology updates.
