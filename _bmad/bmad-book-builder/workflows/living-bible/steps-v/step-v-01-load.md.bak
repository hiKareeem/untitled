---
name: 'step-v-01-load'
description: 'Load all 5 bible dimension files for integrity validation'

# File References
thisStepFile: './step-v-01-load.md'
nextStepFile: './step-v-02-integrity.md'
workflowFile: '../workflow.md'

# Bible File Locations
bibleFolder: '{bbb_output_folder}/bible'
chronologieFile: '{bbb_output_folder}/bible/chronologie.md'
lieuxFile: '{bbb_output_folder}/bible/lieux.md'
objetsFile: '{bbb_output_folder}/bible/objets.md'
personnesFile: '{bbb_output_folder}/bible/personnes.md'
themesFile: '{bbb_output_folder}/bible/themes.md'
---

# Step V-01: Load Bible for Validation

## STEP GOAL:

To load all 5 bible dimension files and prepare them for cross-dimensional integrity validation.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER start validation without loading all files
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE THE BIBLE GUARDIAN, sentinel of coherence
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Character Keeper** — Bible Guardian in **audit mode**
- ✅ You are about to examine the entire narrative archive
- ✅ Your job is to find inconsistencies before they become plot holes
- ✅ Be thorough, be precise, be the guardian the story deserves

### Step-Specific Rules:

- 🎯 Focus ONLY on loading and initial analysis
- 🚫 FORBIDDEN to start cross-checking yet (that's step V-02)
- 📊 Generate statistics on each dimension
- ⚠️ Note any obviously missing or corrupted files

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Verify Bible Folder Exists

Check that `{bibleFolder}` exists:

- If not exists: "No bible found. Start **[C]reate** mode first."
- Then return to workflow.md mode selection

### 2. Load All Dimension Files

For each dimension, load and verify:

**Chronologie:**
- Load `{chronologieFile}`
- If missing or empty: Flag as ERROR
- Extract: totalDays, lastUpdated, lastChapter

**Lieux:**
- Load `{lieuxFile}`
- If missing or empty: Flag as ERROR
- Extract: totalLocations, activeLocations, lastUpdated

**Objets:**
- Load `{objetsFile}`
- If missing or empty: Flag as ERROR
- Extract: totalObjects, activeObjects, lastUpdated

**Personnes:**
- Load `{personnesFile}`
- If missing or empty: Flag as ERROR
- Extract: totalCharacters, charactersInCrisis, lastUpdated

**Themes:**
- Load `{themesFile}`
- If missing or empty: Flag as ERROR
- Extract: totalThemes, themesInCrisis, lastUpdated

### 3. Present Bible Overview

"**Narrative Bible loaded for validation** 📚

**Vue d'ensemble des dimensions :**

| Dimension | Entries | Last Updated | Status |
|-----------|---------|--------------|------|
| Chronologie | [N] jours | [date] | ✓/⚠️ |
| Locations | [N] locations | [date] | ✓/⚠️ |
| Objects | [N] objects | [date] | ✓/⚠️ |
| Characters | [N] characters | [date] | ✓/⚠️ |
| Themes | [N] themes | [date] | ✓/⚠️ |

**Statistiques globales :**
- Temporal coverage: Day 1 to Day [X]
- Characters in crisis (phase 3+): [N]
- Themes in crisis (phase 3): [N]
- Last referenced chapter: [N]"

### 4. Check for Missing Files

If any dimension file is missing or empty:

"**⚠️ Missing or empty files detected:**

[List missing files]

Validation cannot be complete without these files.

Would you like to:
- **[C]** Create the missing files (starts Create mode)
- **[P]** Proceed with partial validation
- **[A]** Cancel and return to the main menu"

Handle accordingly.

### 5. Confirm Ready for Validation

If all files loaded successfully:

"**✅ All files are loaded and ready for validation.**

Validation will check:
- 🕰️ Temporal coherence (events in order, no paradoxes)
- 🗺️ Spatial coherence (characters are not in two places)
- 🔄 Cross-reference coherence (mentioned objects exist, etc.)
- 👥 Relational coherence (bidirectional relationships)
- 🎭 Thematic coherence (theme carriers consistent with their states)

**Ready to start validation?**"

### 6. Present MENU OPTIONS

Display: **Bible loaded - Select an option:**
- **[C]** Continue to integrity validation
- **[S]** View a detailed summary for a dimension
- **[A]** Cancel and return to the main menu

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed when user selects 'C'

#### Menu Handling Logic:

- **IF C:** Store all loaded data in memory, then load, read entire file, then execute `{nextStepFile}`
- **IF S:** Ask which dimension, display full summary, then redisplay menu
- **IF A:** "Validation canceled. Return to the main menu." Then return to workflow
- **IF Any other:** help user respond, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- All 5 dimension files found and loaded
- Statistics extracted from each file
- Overview presented to user
- User confirmed ready for validation
- Data stored in memory for step V-02

### FAILURE:

- Proceeding with missing files without user consent
- Starting cross-validation (that's step V-02)
- Not presenting overview
- Not checking file integrity

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and all files are loaded will you load `{nextStepFile}` to begin the integrity validation.
