# Scan Procedures
# Reference file for step-01-scan

This file contains detailed scan procedures for collecting raw status data from all project directories.

## Chapter Plan Loading Procedure

**Location:** `{foundationFolder}/chapter-plan.md`

**Procedure:**
1. Read chapter plan file
2. Extract all planned chapters with numbers and titles
3. Store as: `planned_chapters` array with:
   - `chapter_number`: Integer
   - `chapter_title`: String
4. IF MISSING: Note "Chapter plan not found" and store empty array

**Output Format:**
```yaml
planned_chapters:
  - chapter_number: 1
    chapter_title: "Title"
  - chapter_number: 2
    chapter_title: "Title"
```

---

## Chapter Files Scan Procedure

**Location:** `{chaptersFolder}/`

**For each planned chapter:**

**Check for files:**
- `chapter-{N}.md` (main chapter file)
- `chapter-{N}-meta.yaml` (metadata file)

**IF chapter file exists:**
1. Read file to get word count (count words in content)
2. IF meta file exists: Read status field if present
3. Get file modification date
4. Store as: `chapter_{N}_status` with:
   - `file_exists`: true
   - `word_count`: Integer
   - `status_field`: String (or null)
   - `modified_date`: Date string

**IF chapter file doesn't exist:**
1. Store as: `chapter_{N}_status` with:
   - `file_exists`: false
   - `status`: 'planned'

**Output Format:**
```yaml
chapter_1_status:
  file_exists: true
  word_count: 2500
  status_field: "complete"
  modified_date: "2026-01-24"
chapter_2_status:
  file_exists: false
  status: "planned"
```

---

## Character Dossiers Scan Procedure

**Location:** `{charactersFolder}/`

**Search for character profile files:**
- Patterns: `*-profile.md`, `character-*.md`, `*.md`

**IF FOUND:**
For each file:
1. Read file to extract:
   - Character name
   - Arc progression phase (look for "Phase X/Y" pattern)
   - File modification date
2. Store as: `character_{name}_data` with:
   - `name`: String
   - `arc_phase`: String (e.g., "Phase 3/5")
   - `modified_date`: Date string
   - `file_exists`: true

**IF NO FILES:**
1. Note "No character dossiers found"
2. Store empty array

**Output Format:**
```yaml
character_protagonist_data:
  name: "Protagonist Name"
  arc_phase: "Phase 3/5"
  modified_date: "2026-01-24"
  file_exists: true
```

---

## Living Bible Dimensions Scan Procedure

**Location:** `{bibleFolder}/`

Scan for the 5 Living Bible dimensions:

### Dimension 1: Chronologie (Timeline)

**Search:** `chronologie.md` or `timeline.md`

**IF FOUND:**
1. Get file modification date
2. Scan content for chapter markers (e.g., "## Chapitre X", "## Chapter X")
3. Extract highest chapter number found
4. Store as: `bible_chronologie` with:
   - `exists`: true
   - `modified_date`: Date string
   - `last_chapter_marker`: Integer

**IF MISSING:**
1. Store as: `bible_chronologie` with:
   - `exists`: false

### Dimension 2: Lieux (Locations)

**Search:** `lieux.md` or `locations.md`

**IF FOUND:**
1. Get file modification date
2. Scan content for chapter markers
3. Extract highest chapter number found
4. Store as: `bible_lieux` with:
   - `exists`: true
   - `modified_date`: Date string
   - `last_chapter_marker`: Integer

**IF MISSING:**
1. Store as: `bible_lieux` with:
   - `exists`: false

### Dimension 3: Objets (Objects)

**Search:** `objets.md` or `objects.md`

**IF FOUND:**
1. Get file modification date
2. Scan content for chapter markers
3. Extract highest chapter number found
4. Store as: `bible_objets` with:
   - `exists`: true
   - `modified_date`: Date string
   - `last_chapter_marker`: Integer

**IF MISSING:**
1. Store as: `bible_objets` with:
   - `exists`: false

### Dimension 4: Personnes (Characters)

**Search:** `personnes.md` or `characters.md`

**IF FOUND:**
1. Get file modification date
2. Scan content for chapter markers
3. Extract highest chapter number found
4. Store as: `bible_personnes` with:
   - `exists`: true
   - `modified_date`: Date string
   - `last_chapter_marker`: Integer

**IF MISSING:**
1. Store as: `bible_personnes` with:
   - `exists`: false

### Dimension 5: Themes (Thematic)

**Search:** `themes.md` or `thematic.md`

**IF FOUND:**
1. Get file modification date
2. Scan content for chapter markers
3. Extract highest chapter number found
4. Store as: `bible_themes` with:
   - `exists`: true
   - `modified_date`: Date string
   - `last_chapter_marker`: Integer

**IF MISSING:**
1. Store as: `bible_themes` with:
   - `exists`: false

**Output Format:**
```yaml
bible_chronologie:
  exists: true
  modified_date: "2026-01-24"
  last_chapter_marker: 5
bible_lieux:
  exists: false
```

---

## Audit Reports Scan Procedure

**Location:** `{auditsFolder}/`

**Search for audit files:**
- Patterns: `character-audit-*.md`, `audit-*.md`

**IF FOUND:**
For each file:
1. Read file to extract:
   - Character name
   - Audit date (from file name or content)
2. Store as: `audit_{name}_data` with:
   - `character_name`: String
   - `audit_date`: Date string
   - `file_path`: String

**IF NO FILES:**
1. Note "No audit reports found"
2. Store empty array

**Output Format:**
```yaml
audit_protagonist_data:
  character_name: "Protagonist Name"
  audit_date: "2026-01-20"
  file_path: "/path/to/audit-file.md"
```

---

## Thematic Tracking Scan Procedure

**Location:** `{trackingFolder}/`

### Theme Tracking

**Search:** `themes.md`, `theme-tracking.md`, `thematic-analysis.md`

**IF FOUND:**
1. Read file to extract:
   - Theme names
   - Progression phases (look for "Phase X/Y" pattern)
   - Status indicators (On track, Needs attention, etc.)
2. Store as: `theme_tracking` array with:
   - `theme_name`: String
   - `progression`: String (e.g., "Phase 3/5")
   - `status`: String

**IF MISSING:**
1. Note "Theme tracking not found"
2. Store empty array

### Rhythm Tracking

**Search:** `rhythm.md`, `pacing.md`, `rhythm-analysis.md`

**IF FOUND:**
1. Read file to extract basic status
2. Store as: `rhythm_tracking` with:
   - `exists`: true
   - `modified_date`: Date string

**IF MISSING:**
1. Store as: `rhythm_tracking` with:
   - `exists`: false

**Output Format:**
```yaml
theme_tracking:
  - theme_name: "Redemption"
    progression: "Phase 2/4"
    status: "On track"
rhythm_tracking:
  exists: true
  modified_date: "2026-01-24"
```

---

## Recent Activity Collection Procedure

**Scan all BBB output folders for recent files:**

**Locations to scan:**
- `{chaptersFolder}/` — all .md files
- `{bibleFolder}/` — all .md files
- `{auditsFolder}/` — all .md files
- `{trackingFolder}/` — all .md files
- `{charactersFolder}/` — all .md files

**For each file found:**
1. Collect: file name, folder path, modification date
2. Sort all files by modification date (most recent first)
3. Take top 5 most recently modified files
4. Store as: `recent_activity` array with:
   - `file_name`: String
   - `folder`: String
   - `modified_date`: Date string

**Output Format:**
```yaml
recent_activity:
  - file_name: "chapter-5.md"
    folder: "chapters"
    modified_date: "2026-01-24"
  - file_name: "chronologie.md"
    folder: "bible"
    modified_date: "2026-01-23"
```

---

## Output Initialization Procedure

**Create initial output file at:** `{outputFile}`

**Frontmatter:**
```yaml
---
stepsCompleted: ['step-01-scan']
lastStep: 'step-01-scan'
date: '{current_date}'
user_name: '{user_name}'
scanComplete: true
---
```

**Initial Header:**
```markdown
# Status Report: {date}

> **Generated:** {date}
> **Reporter:** Character Keeper (Marie)
> **Project:** {project_name}

---

## Scan Data Collected

Scan complete. Proceeding to analysis...

---
```
