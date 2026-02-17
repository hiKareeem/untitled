---
name: 'step-01-load-context'
description: 'Load all data sources for comprehensive audit'

# Navigation
nextStepFile: './step-02-narrative-arc.md'

# Output
outputFile: '{bbb_output_folder}/audit/project-audit-{date}.md'
bbb_output_folder: '{output_folder}'
chaptersFolder: '{bbb_output_folder}/book-1/chapters/'
charactersFolder: '{bbb_output_folder}/characters/'
bibleFolder: '{bbb_output_folder}/bible/'
auditsFolder: '{bbb_output_folder}/audits/'
reportsFolder: '{bbb_output_folder}/reports/'
trackingFolder: '{bbb_output_folder}/book-1/tracking/'
foundationFolder: '{bbb_output_folder}/foundation/'
auditScope: '{auditScope}'
targetChapters: '{targetChapters}'
---

# Step 1: Load Context

## STEP GOAL:
To load all necessary data sources for comprehensive project audit including manuscript chapters, Living Bible dimensions, previous review reports, character audits, and tracking data.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Continuity Editor (Claude)** performing systematic data collection for comprehensive audit
- Like a senior editor gathering all materials before manuscript review
- Thorough context loading is essential for accurate project health assessment
- You load data now, analyze patterns in subsequent steps

### Step-Specific Rules:
- Focus ONLY on loading and organizing data from all sources
- FORBIDDEN to perform analysis or generate insights in this step
- Load ALL available sources — missing data is noted, not skipped
- Store loaded data in structured format for analysis phases
- Auto-proceed to step 2 after loading complete

## EXECUTION PROTOCOLS:
- Load data sources in logical order (chapters → bible → reports → audits → tracking → foundation)
- Collect content, metadata, and availability status for all sources
- Note missing files and directories explicitly
- Store all loaded data in structured format for analysis steps
- Auto-proceed to step 2 after loading complete

## CONTEXT BOUNDARIES:
- Has access to `bbb_output_folder` and all subfolder paths from workflow initialization
- Has `auditScope` and `targetChapters` from scope selection
- Loading is read-only — no modifications to any files
- Focus: Data collection and organization, not analysis

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Loading Phase

"**Loading Audit Context...**

Let me gather all the materials for comprehensive project health assessment. I'll systematically load the manuscript, Living Bible dimensions, previous reviews, and tracking data.

Loading in progress..."

### 2. Load Manuscript Chapters (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Loading Procedures" section for detailed chapter loading protocols.

**IF auditScope = 'all':**
- Scan `{chaptersFolder}` for `chapter-*.md` pattern
- Extract: number, title, content, word count, modification date
- Store as: `chapter_{N}_data` with complete metadata
- Store sorted: `manuscript_chapters` array

**IF auditScope = 'selected':**
- Load only chapters specified in `targetChapters`
- Check existence of `chapter-{N}.md` for each
- Store found chapters as `chapter_{N}_data`
- Note missing chapters explicitly
- Store sorted: `manuscript_chapters` array

After loading:
"✅ **Manuscript Chapters:** {count} chapters loaded ({total_words} total words)"
  - Chapters: {list of chapter numbers and titles}
  - ⚠️ Note any missing chapters if scope = 'selected'

### 3. Load Chapter Plan (CORE)

Read chapter plan from `{foundationFolder}/chapter-plan.md`:
- IF FOUND: Extract planned chapters with numbers, titles, structure
  - Store as: `chapter_plan` with chapter_number, chapter_title, planned_beat
- IF MISSING: Store empty object with note "Chapter plan not found"

After loading:
"✅ **Chapter Plan:** {status}"

### 4. Load Living Bible Dimensions (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Living Bible Dimension Loading" section.

Load all 5 standard dimensions using these paths:
1. Chronologie: `{bibleFolder}/chronologie.md` or `timeline.md`
2. Lieux: `{bibleFolder}/lieux.md` or `locations.md`
3. Objets: `{bibleFolder}/objets.md` or `objects.md`
4. Personnes: `{bibleFolder}/personnes.md` or `characters.md`
5. Themes: `{bibleFolder}/themes.md` or `thematic.md`

**Storage format:**
- Found: `bible_{dimension}: {exists: true, content, modified_date}`
- Missing: `bible_{dimension}: {exists: false}`

After loading:
"✅ **Living Bible:** {count}/5 dimensions loaded"
  - Available: {list}
  - Missing: {list}

### 5. Load Previous Review Reports (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Previous Reports Loading" section.

Scan `{reportsFolder}/` for review reports:
- Search: `review-*.md`, `review-report-*.md` patterns
- Extract: date, scope, issues count, key findings
- Store as: `review_report_{date}_data`
- Sort by date: `previous_reviews` array

After loading:
"✅ **Review Reports:** {count} previous reviews found"

### 6. Load Character Audit Reports (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Previous Reports Loading" section.

Scan `{auditsFolder}/` for character audit reports:
- Search: `character-audit-*.md`, `audit-*.md` patterns
- Extract: character name, audit date, arc phase, findings
- Store as: `character_audit_{name}_data`
- Sort by character: `character_audits` array

After loading:
"✅ **Character Audits:** {count} character audits found"

### 7. Load Theme Tracking (OPTIONAL)

Search `{trackingFolder}/` for theme tracking:
- Search: `themes.md`, `theme-tracking.md`, `thematic-analysis.md`
- IF FOUND: Extract theme names, progression phases, status
  - Store as: `theme_tracking: {exists: true, content, themes: []}`
- IF MISSING: Store as: `theme_tracking: {exists: false}`

After loading:
"✅ **Theme Tracking:** {status}"

### 8. Load Rhythm Analysis (OPTIONAL)

Search `{trackingFolder}/` for rhythm tracking:
- Search: `rhythm.md`, `pacing.md`, `rhythm-analysis.md`
- IF FOUND: Extract pacing analysis, rhythm patterns
  - Store as: `rhythm_tracking: {exists: true, content, findings: []}`
- IF MISSING: Store as: `rhythm_tracking: {exists: false}`

After loading:
"✅ **Rhythm Analysis:** {status}"

### 9. Load Project Context (OPTIONAL)

Search `{foundationFolder}/` for project context:
- Search: `project-context.md`, `story-brief.md`, `premise.md`
- IF FOUND: Extract premise, genre, themes, story structure
  - Store as: `project_context: {exists: true, content, premise, genre, themes}`
- IF MISSING: Store as: `project_context: {exists: false}`

After loading:
"✅ **Project Context:** {status}"

### 10. Create Audit Directory and Initialize Output File

Check if `{bbb_output_folder}/audit/` exists, create if needed.

Create initial output file at `{outputFile}` with frontmatter and header (see `data/templates/audit-report-template.md` for format).

### 11. Present Loading Summary

Display:

"**Context Loading Complete!**

### Data Sources Loaded

| Category | Items Loaded | Status |
|----------|--------------|--------|
| Manuscript Chapters | {count} chapters ({words} words) | ✅ |
| Chapter Plan | {status} | ✅/⚠️ |
| Living Bible Dimensions | {count}/5 | ✅/⚠️ |
| Previous Review Reports | {count} | ✅/⚠️ |
| Character Audits | {count} | ✅/⚠️ |
| Theme Tracking | {status} | ✅/⚠️ |
| Rhythm Analysis | {status} | ✅/⚠️ |
| Project Context | {status} | ✅/⚠️ |

{notes on any missing data}

**All context loaded. Ready to analyze narrative arc and structure.**"

Auto-proceeding to narrative arc analysis...

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- All manuscript chapters loaded (based on scope)
- Chapter plan loaded or missing status noted
- All available Living Bible dimensions loaded
- All previous review reports loaded
- All character audit reports loaded
- Theme tracking loaded if available
- Rhythm analysis loaded if available
- Project context loaded if available
- Output file initialized with loading frontmatter

### SYSTEM FAILURE:
- Not loading all available manuscript chapters
- Not loading all available bible dimensions
- Not loading previous review reports
- Not loading character audit reports
- Not noting missing data explicitly
- Not initializing output file

**Master Rule:** Comprehensive context loading is the foundation of accurate project auditing. Every available source should be loaded, every missing item noted, all data organized for analysis. The narrative arc and coherence analysis phases depend on complete context data.
