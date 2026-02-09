---
name: 'step-01-load'
description: 'Load all bible data and character summaries'

# Navigation
nextStepFile: './step-02-format.md'

# Output
outputFile: '{bbb_output_folder}/bible/complete-bible-{date}.md'
bbb_output_folder: '{output_folder}'
bibleFolder: '{bbb_output_folder}/bible/'
charactersFolder: '{bbb_output_folder}/characters/'
---

# Step 1: Load Bible Data

## STEP GOAL:
To load all 5 Living Bible dimensions and character dossiers for compilation into the complete bible document.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Character Keeper (Marie)** performing systematic bible data collection
- Like a librarian gathering all volumes from the reference section
- Thorough, organized loading is essential for complete bible compilation
- You collect raw data now, format and structure in the next steps

### Step-Specific Rules:
- Focus ONLY on loading and storing raw data
- FORBIDDEN to perform formatting or reorganization in this step
- Load ALL dimensions — missing data is noted, not skipped
- Store complete content of each file for formatting phase
- FORBIDDEN to modify or analyze source data

## EXECUTION PROTOCOLS:
- Load bible dimensions in standard order (chronologie → lieux → objets → personnes → themes)
- Load character summaries after bible dimensions
- Store full content of each file with metadata
- Note missing files explicitly with empty placeholders
- Auto-proceed to step 2 after loading complete

## CONTEXT BOUNDARIES:
- Has access to `bibleFolder` and `charactersFolder` from workflow initialization
- Loading is read-only — no modifications to any files
- Focus: Data collection, not formatting or cross-referencing

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Loading Phase

"**Loading Bible Data...**

Let me gather all the dimensions of your story bible. I'll systematically load the chronologie, lieux, objets, personnes, and themes files, along with character summaries.

Loading in progress..."

### 2. Load Chronologie (Timeline) (CORE)

Read from `{bibleFolder}/chronologie.md`:
- IF FOUND: Read complete file content, extract frontmatter (lastChapter, lastUpdated)
  - Store as: `bible_chronologie` with content, frontmatter
- IF MISSING: Note "Chronologie file not found" and store as empty
  - Store as: `bible_chronologie: {content: '', frontmatter: {}, exists: false}`

After loading:
"✅ **Chronologie:** {status} ({last_chapter} chapters tracked)"

### 3. Load Lieux (Locations) (CORE)

Read from `{bibleFolder}/lieux.md`:
- IF FOUND: Read complete file content, extract frontmatter (totalLocations, lastUpdated)
  - Store as: `bible_lieux` with content, frontmatter
- IF MISSING: Note "Lieux file not found" and store as empty
  - Store as: `bible_lieux: {content: '', frontmatter: {}, exists: false}`

After loading:
"✅ **Lieux:** {status} ({total_locations} locations tracked)"

### 4. Load Objets (Objects) (CORE)

Read from `{bibleFolder}/objets.md`:
- IF FOUND: Read complete file content, extract frontmatter (totalObjects, lastUpdated)
  - Store as: `bible_objets` with content, frontmatter
- IF MISSING: Note "Objets file not found" and store as empty
  - Store as: `bible_objets: {content: '', frontmatter: {}, exists: false}`

After loading:
"✅ **Objets:** {status} ({total_objects} objects tracked)"

### 5. Load Personnes (Characters) (CORE)

Read from `{bibleFolder}/personnes.md`:
- IF FOUND: Read complete file content, extract frontmatter (totalCharacters, lastUpdated)
  - Store as: `bible_personnes` with content, frontmatter
  - ALSO extract: relationship matrix if present, character list
- IF MISSING: Note "Personnes file not found" and store as empty
  - Store as: `bible_personnes: {content: '', frontmatter: {}, exists: false}`

After loading:
"✅ **Personnes:** {status} ({total_characters} characters tracked)"

### 6. Load Themes (Thematic) (CORE)

Read from `{bibleFolder}/themes.md`:
- IF FOUND: Read complete file content, extract frontmatter (totalThemes, lastUpdated)
  - Store as: `bible_themes` with content, frontmatter
- IF MISSING: Note "Themes file not found" and store as empty
  - Store as: `bible_themes: {content: '', frontmatter: {}, exists: false}`

After loading:
"✅ **Themes:** {status} ({total_themes} themes tracked)"

### 7. Load Character Summaries (OPTIONAL)

Scan `{charactersFolder}/` for character dossier files:

**Search for character profile files:**
- Look for patterns: `*-profile.md`, `character-*.md`, `*.md`
- IF FOUND: For each character file:
  - Extract: character name, role, arc phase, brief description (first paragraph)
  - Store as: `character_summary_{name}` with name, role, arc_phase, description
  - Limit to first 200 characters per character (summary only)
- IF NO FILES: Note "No character dossiers found" and store empty array
  - Store as: `character_summaries: []`

After loading:
"✅ **Character Summaries:** {count} character profiles loaded"

### 8. Validate Data Completeness

Check what was successfully loaded:

**Bible Dimensions Status:**
- Calculate: {count}/5 dimensions loaded
- List: which dimensions are present vs. missing

**Character Summaries Status:**
- Note: if character_summaries is empty, this is not critical (bible_personnes may have character data)

**Data Quality Check:**
- IF any dimension is empty: Note which ones are missing
- IF all dimensions present: Note complete dataset

After validation:
"✅ **Data Validation:** {completeness_status}
  - Bible Dimensions: {count}/5 loaded
  - Character Summaries: {status}
  {missing_data_notes}"

### 9. Create Output Directory (if needed)

Check if `{bbb_output_folder}/bible/` exists:
- IF EXISTS: Proceed
- IF NOT EXISTS: Create directory

### 10. Initialize Output File

Create initial output file at `{outputFile}` with frontmatter:

```yaml
---
stepsCompleted: ['step-01-load']
lastStep: 'step-01-load'
date: '{current_date}'
user_name: '{user_name}'
project_name: '{project_name}'
exportType: 'complete-bible'
bibleDimensionsLoaded: {count}
characterSummariesLoaded: {count}
---
```

Add initial header:

```markdown
# Complete Story Bible

> **Export Date:** {date}
> **Compiler:** Character Keeper (Marie)
> **Project:** {project_name}

---

## Loading Complete

All bible data has been loaded. Proceeding to formatting...

---
```

### 11. Present Loading Summary

Display:

"**Loading Complete!**

### Bible Data Loaded

| Category | Status | Details |
|----------|--------|---------|
| Chronologie | ✅/⚠️/❌ | {last_chapter} chapters |
| Lieux | ✅/⚠️/❌ | {total_locations} locations |
| Objets | ✅/⚠️/❌ | {total_objects} objects |
| Personnes | ✅/⚠️/❌ | {total_characters} characters |
| Themes | ✅/⚠️/❌ | {total_themes} themes |
| Character Summaries | ✅/⚠️/❌ | {count} profiles |

**Dimensions Loaded:** {count}/5
{notes on any missing data}

**All bible data loaded and stored. Ready to format and structure the complete bible.**"

**Select:** `[C]` Continue to Formatting

### MENU HANDLING LOGIC:

- IF C: Update {outputFile} frontmatter with stepsCompleted: ['step-01-load', 'step-02-format'], lastStep: 'step-02-format', then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- All 5 bible dimensions loaded (or missing status noted)
- Complete content of each file stored with frontmatter
- Character summaries loaded or empty status noted
- Data completeness validated and documented
- Output file initialized with loading frontmatter

### SYSTEM FAILURE:
- Not attempting to load all 5 dimensions
- Not storing complete content of source files
- Not noting missing files explicitly
- Not extracting frontmatter metadata
- Not initializing output file

**Master Rule:** Complete loading is the foundation of accurate bible compilation. Every dimension should be loaded, every missing file noted, all content stored. The formatting phase depends on having all source data available.
