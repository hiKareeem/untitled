---
name: 'step-01-scan'
description: 'Scan project directories for status data'

# Navigation
nextStepFile: './step-02-analyze.md'

# Output
outputFile: '{bbb_output_folder}/reports/status-report-{date}.md'
bbb_output_folder: '{output_folder}'
chaptersFolder: '{bbb_output_folder}/book-1/chapters/'
charactersFolder: '{bbb_output_folder}/characters/'
bibleFolder: '{bbb_output_folder}/bible/'
auditsFolder: '{bbb_output_folder}/audits/'
trackingFolder: '{bbb_output_folder}/book-1/tracking/'
foundationFolder: '{bbb_output_folder}/foundation/'
---

# Step 1: Scan Project

## STEP GOAL:
To perform a comprehensive scan of all project directories to collect raw status data from chapters, characters, bible, audits, and tracking files.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Character Keeper (Marie)** performing systematic project scanning
- Like a librarian taking inventory across all sections of the library
- Thorough, organized scanning is essential for accurate status reporting
- You collect raw data now, analyze patterns in the next step

### Step-Specific Rules:
- Focus ONLY on scanning and collecting raw data
- FORBIDDEN to perform analysis or generate insights in this step
- Scan ALL locations — missing data is noted, not skipped
- Record file existence, modification dates, and key metadata
- Create organized data structure for analysis phase

## EXECUTION PROTOCOLS:
- Scan directories in logical order (chapters → characters → bible → audits → tracking)
- Collect existence, status, and metadata for all files
- Note missing files and directories explicitly
- Store all scan results in structured format for analysis
- Auto-proceed to step 2 after scan complete

## CONTEXT BOUNDARIES:
- Has access to `bbb_output_folder` and all subfolder paths from workflow initialization
- Scan is read-only — no modifications to any files
- Focus: Data collection, not analysis or reporting

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Scan Phase

"**Scanning Project Status...**

Let me check the records across all sections of your project. I'll systematically scan chapters, characters, bible, audits, and tracking to gather current status data.

Scanning in progress..."

### 2. Load Chapter Plan (CORE)

**Reference:** See `data/analysis/scan-procedures.md` → "Chapter Plan Loading Procedure"

Read chapter plan from `{foundationFolder}/chapter-plan.md`:
- IF FOUND: Extract all planned chapters with numbers and titles
- Store as: `planned_chapters` array with chapter_number, chapter_title
- IF MISSING: Note "Chapter plan not found" and store empty array

After loading:
"✅ **Chapter Plan:** {count} chapters planned"
  - Chapters: {list}

### 3. Scan Chapter Files (CORE)

**Reference:** See `data/analysis/scan-procedures.md` → "Chapter Files Scan Procedure"

For each planned chapter, check `{chaptersFolder}`:
- Check if `chapter-{N}.md` exists
- Check if `chapter-{N}-meta.yaml` exists
- IF chapter file exists: Read file to get word count, status field, modification date
- IF chapter file doesn't exist: Store as planned

After scanning:
"✅ **Chapters Scanned:** {count}/{total} chapters found"
  - Complete: {count}
  - In Draft: {count}
  - Planned: {count}

### 4. Scan Character Dossiers (CORE)

**Reference:** See `data/analysis/scan-procedures.md` → "Character Dossiers Scan Procedure"

Scan `{charactersFolder}/` for character files:
- Look for patterns: `*-profile.md`, `character-*.md`, `*.md`
- IF FOUND: Read each file to extract name, arc phase, modification date
- IF NO FILES: Note "No character dossiers found" and store empty array

After scanning:
"✅ **Characters Scanned:** {count} character dossiers found"
  - Characters: {list}

### 5. Scan Living Bible Dimensions (CORE)

**Reference:** See `data/analysis/scan-procedures.md` → "Living Bible Dimensions Scan Procedure"

Scan `{bibleFolder}/` for the 5 Living Bible dimensions:
- Chronologie (Timeline): `chronologie.md` or `timeline.md`
- Lieux (Locations): `lieux.md` or `locations.md`
- Objets (Objects): `objets.md` or `objects.md`
- Personnes (Characters): `personnes.md` or `characters.md`
- Themes (Thematic): `themes.md` or `thematic.md`

For each dimension:
- IF FOUND: Get modification date, scan for chapter markers
- IF MISSING: Store as not exists

After scanning:
"✅ **Bible Dimensions Scanned:** {count}/5 dimensions found"
  - Available: {list}
  - Missing: {list}

### 6. Scan Audit Reports (OPTIONAL)

**Reference:** See `data/analysis/scan-procedures.md` → "Audit Reports Scan Procedure"

Scan `{auditsFolder}/` for character audit reports:
- Look for: `character-audit-*.md`, `audit-*.md`
- IF FOUND: Read each file to extract character name, audit date
- IF NO FILES: Note "No audit reports found" and store empty array

After scanning:
"✅ **Audit Reports:** {count} reports found"

### 7. Scan Thematic Tracking (OPTIONAL)

**Reference:** See `data/analysis/scan-procedures.md` → "Thematic Tracking Scan Procedure"

Scan `{trackingFolder}/` for tracking files:

**Theme Tracking:**
- Search: `themes.md`, `theme-tracking.md`, `thematic-analysis.md`
- IF FOUND: Read file to extract theme names, progression phases, status indicators
- IF MISSING: Note "Theme tracking not found" and store empty array

**Rhythm Tracking:**
- Search: `rhythm.md`, `pacing.md`, `rhythm-analysis.md`
- IF FOUND: Read file to extract basic status
- IF MISSING: Store as not exists

After scanning:
"✅ **Tracking Files:** Theme tracking {status}, Rhythm tracking {status}"

### 8. Collect Recent Activity (CORE)

**Reference:** See `data/analysis/scan-procedures.md` → "Recent Activity Collection Procedure"

Get modification dates for all project files:
- Scan all BBB output folders for .md files
- Collect file name, folder path, modification date
- Sort by modification date (most recent first)
- Take top 5 most recently modified files

After collecting:
"✅ **Recent Activity:** Collected last 5 modified files"

### 9. Create Output Directory (if needed)

Check if `{bbb_output_folder}/reports/` exists:
- IF EXISTS: Proceed
- IF NOT EXISTS: Create directory

### 10. Initialize Output File

**Reference:** See `data/analysis/scan-procedures.md` → "Output Initialization Procedure"

Create initial output file at `{outputFile}` with frontmatter and header as specified in the reference procedures.

### 11. Present Scan Summary

Display:

"**Scan Complete!**

### Data Collected

| Category | Items Found | Status |
|----------|-------------|--------|
| Chapters | {complete}/{draft}/{planned} | ✅ |
| Character Dossiers | {count} | ✅/⚠️ |
| Bible Dimensions | {count}/5 | ✅/⚠️ |
| Audit Reports | {count} | ✅/⚠️ |
| Theme Tracking | {status} | ✅/⚠️ |
| Rhythm Tracking | {status} | ✅/⚠️ |
| Recent Activity | 5 files | ✅ |

{notes on any missing data}

**Raw scan data collected. Ready to analyze patterns and generate status report.**"

**Select:** `[C]` Continue to Analysis

### MENU HANDLING LOGIC:

- IF C: Update {outputFile} frontmatter with stepsCompleted: ['step-01-scan', 'step-02-analyze'], lastStep: 'step-02-analyze', then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- All directories scanned (chapters, characters, bible, audits, tracking)
- Chapter plan loaded or missing status noted
- Chapter files scanned with metadata (word count, status, date)
- Character dossiers scanned with arc phases
- Bible dimensions scanned with chapter markers
- Audit reports scanned if available
- Theme and rhythm tracking scanned if available
- Recent activity collected (5 most recent files)
- Output file initialized with scan frontmatter

### SYSTEM FAILURE:
- Not scanning all required directories
- Not collecting file existence and metadata
- Not noting missing files explicitly
- Not collecting modification dates
- Not initializing output file

**Master Rule:** Thorough scanning is the foundation of accurate status reporting. Every file should be checked, every missing item noted, all metadata collected. The analysis phase depends on complete raw data collection.
