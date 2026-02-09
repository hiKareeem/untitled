# Migration Procedures Reference

## Overview

This document defines the standard procedures for migrating existing writing projects to BBB structure. Follow these procedures to ensure safe, complete migrations.

## Migration Modes

### HYBRID Mode (Default)
- **Originals**: PRESERVED in original location
- **BBB Content**: Created as copies in new structure
- **Risk**: ZERO - No data loss possible
- **Rollback**: Delete BBB folders only
- **Use When**: Always - this is the safest approach

### CLEAN Mode (Not Recommended)
- **Originals**: Moved or deleted
- **BBB Content**: Replaces originals
- **Risk**: HIGH - Potential data loss
- **Rollback**: Requires backups
- **Use When**: Never - not supported in BBB workflows

## Pre-Migration Checklist

Before starting migration:

- [ ] Project path validated and exists
- [ ] Author confirmed this is the correct project
- [ ] Migration plan document created
- [ ] Content analysis completed
- [ ] Structure mapping documented
- [ ] Migration plan reviewed by author
- [ ] Explicit PROCEED approval obtained

## Migration Sequence

### Phase 1: Discovery (Step 1)

**Goal**: Locate and validate the project

**Steps**:
1. Accept project path from user
2. Validate path exists
3. Confirm this is the correct project
4. Create initial migration plan document
5. Store project context for next steps

**Output**: Validated project path, initial migration plan

### Phase 2: Analysis (Step 2)

**Goal**: Identify and catalog all content

**Steps**:
1. Scan directory structure systematically
2. Identify content types using detection patterns
3. Catalog chapters, characters, themes, other content
4. Generate content inventory
5. Store detection results for mapping

**Detection Patterns**:

*Chapters*:
- Folders: `chapters/`, `chapitres/`, `chapter/`, `text/`, `manuscript/`
- Files: `chapter-*.md`, `chapitre-*.md`, `ch-*.md`
- Sequential numbering: 01, 02, 03...
- Minimum 3 files to confirm

*Characters*:
- Folders: `characters/`, `personnages/`, `chars/`, `cast/`
- Files with character names
- Character dossiers with psychology/backstory

*Themes*:
- Folders: `themes/`, `thematiques/`, `motifs/`, `ideas/`
- Files about themes, symbols, metaphors

*Psychology*:
- Folders: `psychology/`, `psychologie/`, `character-psychology/`
- Files about motivations, arcs, emotional states

*Structure*:
- Folders: `structure/`, `architecture/`, `outline/`, `plan/`
- Plot breakdown, beat sheets, scene lists

**Output**: Content inventory with paths and counts

### Phase 3: Mapping (Step 3)

**Goal**: Map existing content to BBB structure

**Steps**:
1. Load detected content from analysis
2. Map each content type to BBB equivalent
3. Handle non-standard structures
4. Generate mapping document
5. Store mapping for plan generation

**Output**: Structure mapping document

### Phase 4: Plan Generation (Step 4)

**Goal**: Create comprehensive migration plan

**Steps**:
1. Load all previous data (discovery, analysis, mapping)
2. Generate complete migration plan document
3. Calculate time estimates
4. Assess risks honestly
5. Present plan for review

**Plan Sections**:
1. Executive Summary
2. Detected Content
3. Migration Strategy (HYBRID mode)
4. Before/After Structure
5. Migration Steps
6. Risks and Warnings
7. Approval Required

**Time Estimates**:
- Simple: 15-30 minutes
- Medium: 30-60 minutes
- Complex: 60-90 minutes

**Output**: Complete migration plan document

### Phase 5: Review (Step 5)

**Goal**: Obtain author approval before execution

**Steps**:
1. Present executive summary
2. Show before/after structure
3. Explain migration steps
4. Present risks and warnings
5. Offer review options (Party Mode, Advanced Elicitation)
6. Allow plan modifications
7. Obtain explicit PROCEED or ABORT

**Quality Gate**: This is the critical approval point. NO execution without explicit PROCEED.

**Output**: Approved migration plan, or aborted workflow

### Phase 6: Execution (Step 6)

**Goal**: Safely execute the migration plan

**Steps**:
1. Verify approval status
2. Initialize execution log
3. Create BBB folder structure
4. Migrate chapters with frontmatter
5. Convert characters to YAML
6. Migrate other content
7. Final verification
8. Complete execution log
9. Update migration plan status

**Execution Log**:
Maintain detailed log throughout execution:
- Timestamps for each operation
- Files copied/created
- Conversions performed
- Verification results
- Errors and recoveries

**Verification Checklist**:
- [ ] All folders created
- [ ] All chapters copied with frontmatter
- [ ] All characters converted to YAML
- [ ] Original files untouched
- [ ] No data corruption

**Output**: Migrated BBB structure, execution log

### Phase 7: Gap Detection (Step 7)

**Goal**: Identify missing BBB-required assets

**Steps**:
1. Verify migration success
2. Check all BBB-required assets
3. Determine status (Present, Partial, Missing)
4. Generate comprehensive gap report
5. Assess BBB readiness level
6. Calculate completion time estimates

**Required Assets**:
1. Style Profile - `bbb-output/style-profile.yaml`
2. Chapter Plan - `plans/chapter-plan.md`
3. Characters - `story-bible/characters/*.yaml` (completeness)
4. Story Bible - Overall organization
5. Locations - `story-bible/locations/` (optional)
6. Timeline - `story-bible/timeline/` (optional)

**BBB Readiness Levels**:
- **HIGH**: 0-1 gaps - Can proceed with minimal gaps
- **MEDIUM**: 2-3 gaps - Address gaps before full usage
- **LOW**: 4+ gaps - Complete foundation before writing

**Output**: Gap report with recommendations

### Phase 8: Foundation Completion (Step 8)

**Goal**: Guide author through gap completion

**Steps**:
1. Present gap summary
2. Offer completion options (All, Selective, Manual)
3. Launch recommended workflows
4. Generate final summary
5. Mark project as BBB-ready

**Workflow Launch Order** (optimal):
1. style-capture - Analyze author's voice (15 min)
2. foundation - Create chapter plan (30 min)
3. build-characters - Enrich characters (20 min)
4. living-bible - Organize story bible (15 min)

**Output**: Complete BBB-ready project, final summary

## Chapter Migration Procedure

For each chapter file:

1. **Read original chapter content**
2. **Extract chapter title** from content (first H1) or auto-generate
3. **Add BBB frontmatter**:
   ```yaml
   ---
   chapterNumber: {n}
   chapterTitle: "{title}"
   createdDate: "{current_date}"
   author: "{user_name}"
   migrationSource: "{original_path}"
   ---
   ```
4. **Write to** `chapters/chapter-{n}.md`
5. **Verify write succeeded**
6. **Log operation**

**Subprocess Optimization** (optional):
- Use subprocess for parallel chapter copying
- Purpose: Speed up large projects
- Return: List of successfully copied chapters
- Fallback: Sequential copying if subprocess unavailable

## Character Migration Procedure

For each character file:

1. **Read original character content**
2. **Extract information**:
   - Name
   - Role/Archetype
   - Description
   - Psychology (if present)
   - Contradictions (if present)
   - Other attributes
3. **Convert to YAML format**:
   ```yaml
   ---
   name: "{character_name}"
   role: "{role}"
   archetype: "{archetype}"

   description: |
     {description}

   psychology: |
     {psychology_if_present}

   contradictions:
     - {contradiction_1}
     - {contradiction_2}

   relationships: []
     # To be populated later

   notes: |
     Migrated from: {original_file}
     Migration date: {current_date}
   ---
   ```
4. **Write to** `story-bible/characters/{name}.yaml`
5. **Verify write succeeded**
6. **Log operation**

## Error Handling

### Verification Failure
If verification fails:
1. Log error details
2. Attempt recovery if possible
3. If unrecoverable: ABORT and report to user
4. Never proceed with errors

### Unrecoverable Error
If unrecoverable error occurs:
1. Stop all operations
2. Log error details
3. Report to user with clear explanation
4. Suggest rollback if appropriate
5. Do NOT proceed to next step

## Rollback Procedure

If migration fails or needs to be rolled back:

1. **Stop all operations**
2. **Assess state** - what has been done
3. **Delete BBB folders only**:
   - `bbb-output/`
   - `story-bible/`
   - `chapters/` (BBB version)
4. **Verify originals intact** - should be untouched
5. **Report to user** - what happened and why

**Critical**: Original files should NEVER be touched in HYBRID mode.

## Safety Rules

1. **NEVER modify original files**
2. **ALWAYS verify before proceeding**
3. **LOG every operation**
4. **CHECK for errors after each step**
5. **PRESERVE originals at all costs**
6. **ABORT on unrecoverable errors**
7. **OBTAIN approval before execution**
