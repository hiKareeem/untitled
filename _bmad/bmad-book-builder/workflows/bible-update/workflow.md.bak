# Bible Update Workflow

Update story bible after chapter completion with multi-dimensional extraction and continuity validation.

## Overview

**Goal:** Extract information from completed chapters and update the story bible (characters, locations, objects, timeline, thematic progression) with automatic continuity checks.

**Agent:** Character-Keeper (Bible Guardian)

**Workflow Type:** Edit-only (continuous bible maintenance)

**Duration:** 3-8 minutes (depending on chapter complexity)

## When to Use

- After completing each chapter (auto-triggered from Chapter-Write)
- During revision when updating existing chapters
- For manual bible maintenance and continuity verification

## What This Workflow Does

This workflow:
1. Loads the completed chapter and existing bible
2. Extracts multi-dimensional information (chronology, characters, locations, objects, themes)
3. Validates continuity and detects conflicts with existing bible
4. Presents conflicts for user approval if needed (or auto-proceeds if clean)
5. Updates all bible files and creates extraction record

## Prerequisites

- Story bible must exist (created by Foundation or Living-Bible workflow)
- Chapter file must be complete and readable
- Bible structure: `{project-root}/bible/` with 5 dimension files

## File Structure Expected

```
{project-root}/
├── bible/
│   ├── chronologie.md
│   ├── personnes.md
│   ├── lieux.md
│   ├── objets.md
│   ├── themes.md
│   └── extractions/
│       └── chapitre-{XX}.md
└── chapters/
    └── chapitre-{XX}.md
```

## Inputs

- `chapter_path` (optional) - Path to chapter file. If not provided, auto-detects last chapter.
- `chapter_number` (optional) - Override auto-detection of chapter number.

## Outputs

- Updated bible files (5 dimensions)
- Extraction record: `bible/extractions/chapitre-{XX}.md`
- Summary report of changes made

## Workflow Steps

The workflow follows 4 main phases:

### Step 01: Load Context
- Find and load chapter content
- Load existing bible files (5 dimensions)
- Check for previous extraction
- Validate prerequisites

### Step 02: Extract & Validate
- Multi-dimensional extraction (chronology, characters, locations, objects, themes)
- Cross-reference continuity checks
- Detect conflicts and inconsistencies
- Flag uncertain extractions
- Track first mentions of new entities

### Step 03: Approve Changes
- **If no conflicts:** Display summary and auto-proceed
- **If conflicts detected:** Present to user with proposed resolutions
- User can proceed, edit, or cancel

### Step 04: Update Bible
- Update 5 bible files (append to entity sections)
- Create extraction record for traceability
- Preserve existing formatting
- Generate summary report

## Smart Approval Logic

The workflow uses intelligent checkpointing:

- **Auto-proceed:** No conflicts detected, clear extractions → immediate update
- **Require approval:** Conflicts OR uncertain items detected → user checkpoint
- Always shows extraction summary for transparency

## Multi-Dimensional Extraction

The workflow extracts information across 5 dimensions:

1. **Chronologie:** Timeline events, day progression, flashbacks, narrative vs chronological order
2. **Personnes:** Characters present, actions, psychological state, POV, relationships, first mentions
3. **Lieux:** Locations used, descriptions, spatial continuity, first mentions
4. **Objets:** Plot-critical items, status changes, symbolic significance, first mentions
5. **Themes:** Thematic progression, emerging themes, connections

## Continuity Validation

Cross-reference checks performed:
- Chronologie ↔ Personnes (characters in right place/time)
- Personnes ↔ Lieux (spatial consistency)
- Characters ↔ Themes (thematic alignment)
- Objets ↔ Chronologie (object timeline consistency)

## Error Handling

- **Chapter not found:** Prompts for manual path
- **Bible missing:** Error "Run Foundation workflow first"
- **Extraction timeout:** Saves partial with incomplete flag, allows retry
- **No rollback needed:** Extraction records + git provide history

## Integration

- **Triggered by:** Chapter-Write workflow (automatic)
- **Uses data from:** Foundation or Living-Bible (bible structure)
- **Feeds into:** Character-Audit, Theme-Tracker workflows

## Notes

- This is a simplified version of Living-Bible workflow
- For new projects, consider Living-Bible for more comprehensive tracking
- Bible-Update focuses on post-chapter extraction vs continuous tracking
- All extractions are traceable via records in `bible/extractions/`

## Running the Workflow

The workflow is executed by Character-Keeper agent following the step files in `steps-c/`.

Each step provides detailed instructions for:
- What to analyze
- What tools to use
- What outputs to produce
- How to handle errors
- Success criteria

---

**Created:** 2026-01-25
**Based on spec:** bible-update.spec.md
**Agent:** Character-Keeper
