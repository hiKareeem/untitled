# Gap Detection Criteria Reference

## Overview

This document defines the criteria for detecting missing BBB-required assets after migration. Use these criteria during gap detection (Step 7) to assess BBB foundation completeness.

## BBB-Required Assets

These are the core assets that BBB workflows require to function optimally.

### 1. Style Profile

**Path**: `bbb-output/style-profile.yaml`

**Purpose**: Captures the author's unique writing voice, style preferences, and prose characteristics.

**Why Required**: BBB uses the style profile to generate content that matches the author's voice, maintaining consistency across AI-assisted writing.

**Detection Criteria**:

**COMPLETE**:
- File exists at `bbb-output/style-profile.yaml`
- Contains all required sections:
  - Voice characteristics
  - Sentence structure patterns
  - Dialogue style
  - Description preferences
  - Punctuation and formatting preferences
- File is valid YAML

**PARTIAL**:
- File exists but incomplete sections
- Missing key style characteristics
- Invalid YAML format

**MISSING**:
- File does not exist

**Action if Missing**: Run `style-capture` workflow to analyze author's writing samples

**Time Estimate**: 15 minutes

**Workflow**: `bmad-book-builder:style-capture`

### 2. Chapter Plan

**Path**: `plans/chapter-plan.md`

**Purpose**: Defines the chapter-by-chapter outline, scene breakdowns, and story progression.

**Why Required**: Many BBB workflows use the chapter plan to understand story structure, maintain continuity, and guide content generation.

**Detection Criteria**:

**COMPLETE**:
- File exists at `plans/chapter-plan.md`
- Contains chapter-by-chapter outline
- Each chapter has:
  - Chapter number
  - Chapter title (or working title)
  - Brief description or scene list
  - Plot purpose
- Covers entire story arc

**PARTIAL**:
- File exists but incomplete
- Missing chapters in sequence
- Lacks detail (just titles, no descriptions)
- Doesn't cover full story

**MISSING**:
- File does not exist

**Action if Missing**: Run `foundation` workflow to create comprehensive chapter plan

**Time Estimate**: 30 minutes

**Workflow**: `bmad-book-builder:foundation`

### 3. Characters

**Path**: `story-bible/characters/*.yaml`

**Purpose**: Character profiles with psychology, relationships, and development arcs.

**Why Required**: Character-driven workflows need complete character information to maintain consistency and support character development.

**Detection Criteria**:

**COMPLETE**:
- `story-bible/characters/` folder exists
- All major characters have YAML files
- Each character file contains:
  - Name
  - Role/Archetype
  - Description
  - Psychology (motivations, conflicts)
  - Relationships (even if empty initially)
  - Contradictions (if applicable)
- Files are valid YAML

**PARTIAL**:
- Folder exists but characters missing key fields
- Some major characters lack files
- Missing psychology or relationships sections
- Invalid YAML format

**MISSING**:
- Folder does not exist
- Folder is empty
- No character files present

**Action if Missing**:
- Run `build-characters` workflow to enrich characters (20 min)
- Or manually complete character profiles (variable time)

**Time Estimate**: 20 minutes (workflow) or 30-60 minutes (manual)

**Workflow**: `bmad-book-builder:build-characters`

**Completeness Check**:
- Count number of character YAML files
- Verify each has required fields
- Check that main story characters are represented

### 4. Story Bible

**Path**: `story-bible/` (overall organization)

**Purpose**: Organized collection of all narrative reference materials.

**Why Required**: The story bible is the central reference for maintaining consistency across the narrative.

**Detection Criteria**:

**COMPLETE**:
- `story-bible/` folder exists with organized structure
- Contains subfolders:
  - `characters/` (with YAML files)
  - `themes/` (with themes.yaml)
  - `timeline/` (with timeline.yaml)
- Additional assets present:
  - `structure.md` (optional but recommended)
  - `locations/` (optional but recommended)
- Content is well-organized and accessible

**PARTIAL**:
- Folder exists but poorly organized
- Missing expected subfolders
- Content scattered or unstructured
- Lacks key organizational elements

**MISSING**:
- Folder does not exist
- Folder is empty

**Action if Missing**:
- Run `living-bible` workflow to organize story bible (15 min)
- Or manually organize structure (variable time)

**Time Estimate**: 15 minutes (workflow) or 20-30 minutes (manual)

**Workflow**: `bmad-book-builder:living-bible`

### 5. Themes (Optional but Recommended)

**Path**: `story-bible/themes/themes.yaml`

**Purpose**: Defines story themes, symbols, motifs, and thematic progression.

**Why Recommended**: Theme tracking workflows require theme definitions to function properly.

**Detection Criteria**:

**COMPLETE**:
- `story-bible/themes/` folder exists
- `themes.yaml` file exists
- Contains:
  - Theme definitions
  - Symbol meanings
  - Motif tracking
  - Thematic progression through story

**PARTIAL**:
- Folder or file exists but incomplete
- Missing theme definitions or symbols
- Lacks organization

**MISSING**:
- Folder does not exist
- File does not exist

**Action if Missing**: Can be created manually or through `theme-tracker` workflow

**Time Estimate**: 10-15 minutes

**Workflow**: `bmad-book-builder:theme-tracker`

**Note**: Not strictly required for core BBB functionality, but highly recommended.

### 6. Locations (Optional but Recommended)

**Path**: `story-bible/locations/`

**Purpose**: Detailed descriptions of story settings and locations.

**Why Recommended**: Location consistency is important for narrative coherence.

**Detection Criteria**:

**COMPLETE**:
- `story-bible/locations/` folder exists
- Contains location files for major settings
- Each location has detailed description

**PARTIAL**:
- Folder exists but locations incomplete
- Missing key settings

**MISSING**:
- Folder does not exist

**Action if Missing**: Create manually as needed during writing

**Time Estimate**: 5-10 minutes per location

**Note**: Not required for BBB to function, but useful for world-building.

### 7. Timeline (Optional but Recommended)

**Path**: `story-bible/timeline/timeline.yaml`

**Purpose**: Chronological tracking of story events and temporal relationships.

**Why Recommended**: Timeline consistency is crucial for plot logic.

**Detection Criteria**:

**COMPLETE**:
- `story-bible/timeline/` folder exists
- `timeline.yaml` file exists
- Contains chronological events
- Shows temporal relationships

**PARTIAL**:
- Folder or file exists but incomplete
- Missing key events

**MISSING**:
- Folder does not exist

**Action if Missing**: Create manually or through timeline tools

**Time Estimate**: 10-20 minutes

**Note**: Not required for BBB to function, but important for complex plots.

## Gap Detection Procedure

### 1. Verify Migration Success

Before gap detection:
- Check that migration completed
- Verify `bbb-onboarding-plan-{project_name}.md` status is "MIGRATION COMPLETE"
- Verify `bbb-onboarding-log-{project_name}.md` shows success
- Confirm BBB folders exist in project

**If migration incomplete**: Abort and return to Step 6.

### 2. Load Gap Report Template

Load `{bbb_output_folder}/bbb-gap-report-{project_name}.md` template for structure.

### 3. Check Each Asset Systematically

For each BBB-required asset:

1. **Check existence**: Does file/folder exist?
2. **Verify completeness**: If exists, is it complete?
3. **Determine status**: COMPLETE, PARTIAL, or MISSING
4. **Calculate time estimate**: How long to fix?
5. **Identify action**: Which workflow or manual action?

**Subprocess Optimization** (optional):
- Use subprocess to check multiple assets in parallel
- Purpose: Faster gap detection across many files
- Return: Status of all checked assets
- Fallback: Sequential checking if subprocess unavailable

### 4. Generate Gap Report

Create comprehensive gap report with:

**Table Format**:
| BBB Asset | Status | Missing? | Action Needed | Time Estimate |
|-----------|--------|----------|---------------|---------------|
| **Style Profile** | COMPLETE/PARTIAL/MISSING | yes/no | Run workflow X | XX min |
| **Chapter Plan** | COMPLETE/PARTIAL/MISSING | yes/no | Run workflow Y | XX min |
| **Characters** | COMPLETE/PARTIAL/MISSING | yes/no | Run workflow Z | XX min |
| **Story Bible** | COMPLETE/PARTIAL/MISSING | yes/no | Run workflow W | XX min |

**Detailed Analysis**:
For each gap, provide:
- What's missing or incomplete
- Why it matters
- How to fix it
- Time estimate
- Workflow recommendation (if applicable)

**Summary Statistics**:
- Total gaps detected
- Total estimated completion time
- Critical vs. optional gaps

### 5. Determine BBB Readiness Level

Based on gap analysis, assign overall readiness:

**HIGH Readiness** (0-1 gaps):
- Status: Ready to write with minimal gaps
- Recommendation: Optional improvements can be done later
- Can proceed with most workflows immediately

**MEDIUM Readiness** (2-3 gaps):
- Status: Functional but incomplete
- Recommendation: Address gaps before full workflow usage
- Some workflows may have limited functionality

**LOW Readiness** (4+ gaps):
- Status: Not ready for writing workflows
- Recommendation: Complete foundation before starting
- Many workflows will not function properly

## Asset Status Definitions

### COMPLETE
Asset exists and meets all requirements:
- All required fields present
- Properly formatted (YAML, markdown, etc.)
- Contains necessary detail
- Ready for workflow use

### PARTIAL
Asset exists but needs work:
- Missing some required fields
- Incomplete information
- Formatting issues
- Needs enrichment before optimal use

### MISSING
Asset does not exist:
- File or folder not found
- Must be created from scratch
- Requires workflow or manual creation

## Time Estimate Guidelines

**Style Profile**:
- COMPLETE: 0 min (already done)
- PARTIAL: 10 min (update existing)
- MISSING: 15 min (run workflow)

**Chapter Plan**:
- COMPLETE: 0 min (already done)
- PARTIAL: 15 min (fill gaps)
- MISSING: 30 min (run workflow)

**Characters**:
- COMPLETE: 0 min (already done)
- PARTIAL: 15 min (enrich existing)
- MISSING: 20-60 min (depending on character count)

**Story Bible**:
- COMPLETE: 0 min (already done)
- PARTIAL: 10 min (reorganize)
- MISSING: 15-30 min (create structure)

**Themes**:
- COMPLETE: 0 min (already done)
- PARTIAL: 5 min (add missing)
- MISSING: 10-15 min (create from scratch)

**Locations**:
- COMPLETE: 0 min (already done)
- PARTIAL: 5 min per location
- MISSING: 5-10 min per location

**Timeline**:
- COMPLETE: 0 min (already done)
- PARTIAL: 10 min (fill gaps)
- MISSING: 10-20 min (create from scratch)

## Critical vs. Optional Gaps

### Critical (Must Fix)
- Style Profile - Required for voice consistency
- Chapter Plan - Required for structure guidance
- Characters - Required for character workflows
- Story Bible organization - Required for reference access

### Optional (Nice to Have)
- Themes - Useful for theme tracking
- Locations - Useful for world-building
- Timeline - Useful for plot complexity

## Workflow Launch Order

When filling gaps, optimal order is:

1. **style-capture** (15 min) - Foundation for voice consistency
2. **foundation** (30 min) - Creates chapter plan and structure
3. **build-characters** (20 min) - Enriches character profiles
4. **living-bible** (15 min) - Organizes story bible

**Total Time**: ~80 minutes for complete foundation

## Best Practices

1. **Be thorough** - Check every asset systematically
2. **Be honest** - Don't gloss over partial completeness
3. **Provide clear actions** - Exactly what to do for each gap
4. **Estimate realistically** - Better to overestimate than under
5. **Prioritize critical gaps** - Focus on what's needed most
6. **Think holistically** - How gaps affect overall BBB usage
