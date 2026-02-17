---
name: 'step-02-load'
description: 'Load all reference files into shared context'

# Navigation
nextStepFile: './step-03-analyze.md'

# Output
outputFile: '{bbb_output_folder}/review/review-report-{scope}.md'

# Input Sources (from step-01)
reviewScope: '{scope}'
targetChapters: '{target_chapters}'
bibleFolder: '{bbb_output_folder}/bible/'
chaptersFolder: '{bbb_output_folder}/book-1/chapters/'
foundationFolder: '{bbb_output_folder}/foundation/'
styleProfilePath: '{bbb_output_folder}/style-profile.md'
charactersFolder: '{bbb_output_folder}/characters/'
thematicAnalysisPath: '{bbb_output_folder}/thematic-analysis.md'
reviewReportsFolder: '{bbb_output_folder}/review/'
---

# Step 2: Load Context

## STEP GOAL:
To perform a one-time load of all reference files into shared context, establishing the knowledge base for comprehensive coherence analysis across all 6 review categories.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Continuity Editor** preparing for comprehensive review
- Like a building inspector reviewing blueprints before inspection
- Thorough context loading is essential for accurate analysis
- You organize reference materials for efficient analysis workflow

### Step-Specific Rules:
- Focus ONLY on loading and organizing reference materials
- FORBIDDEN to start analysis in this step
- Load ALL available files - missing files are noted, not skipped
- Organize context for efficient cross-referencing during analysis

## EXECUTION PROTOCOLS:
- Load files in priority order (core → recommended → optional)
- Organize content by category for easy reference
- Note missing files in context for analysis phase
- Update frontmatter with review quality assessment
- Auto-proceed to step 3 after all files loaded

## CONTEXT BOUNDARIES:
- Has access to {reviewScope} and {targetChapters} from step 1
- All files detected in step 1 should be loaded if available
- Target chapters must be loaded for review
- Focus: Data loading and organization, not analysis

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

**Reference:** `../data/loading-procedures.md` contains detailed procedures for all loading operations.

### 1. Announce Loading Phase
See: Loading Announcement section in loading-procedures.md

### 2. Load Target Chapter Content (CORE)
See: Target Chapter Content Loading section in loading-procedures.md

### 3. Load Chapter Plans (CORE)
See: Chapter Plans Loading section in loading-procedures.md

### 4. Load Living Bible (CORE - 5 Dimensions)
See: Living Bible Loading section in loading-procedures.md

### 5. Load Previous Chapter Summaries (CORE)
See: Previous Chapter Summaries Loading section in loading-procedures.md

### 6. Load Style Profile (STRONGLY RECOMMENDED)
See: Style Profile Loading section in loading-procedures.md

### 7. Load Character Dossiers (OPTIONAL)
See: Character Dossiers Loading section in loading-procedures.md

### 8. Load Thematic Tracking (OPTIONAL)
See: Thematic Tracking Loading section in loading-procedures.md

### 9. Load Previous Reviews (OPTIONAL)
See: Previous Reviews Loading section in loading-procedures.md

### 10. Assess Review Quality
See: Review Quality Assessment section in loading-procedures.md

Store as `reviewQuality` in output frontmatter.

### 11. Update Output Frontmatter

Update {outputFile} frontmatter with:
```yaml
reviewQuality: '{quality_assessment}'
bibleDimensionsLoaded: {count}
previousSummariesCount: {count}
styleProfileAvailable: {boolean}
optionalEnhancements: {count}
```

### 12. Present Context Summary
See: Context Summary Template section in loading-procedures.md

**Select:** `[C]` Continue to Analysis

### MENU HANDLING LOGIC:

- IF C: Update {outputFile} frontmatter with stepsCompleted: ['step-01-init', 'step-02-load'], lastStep: 'step-02-load', then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- All target chapter content loaded
- Chapter plans loaded for each target chapter
- Living Bible dimensions loaded (all available)
- Previous chapter summaries loaded
- Style profile loaded (if available)
- Optional files loaded (if available)
- Review quality assessed and recorded
- Frontmatter updated with context summary

### SYSTEM FAILURE:
- Not loading target chapter content
- Not loading chapter plans
- Not attempting to load Living Bible dimensions
- Not loading previous summaries (critical for narrative coherence)
- Not updating frontmatter with quality assessment

**Master Rule:** Context loading must be comprehensive - every available file should be loaded. Missing files are noted, not skipped. The analysis phase depends on thorough context preparation.
