# Content Detection Patterns Reference

## Overview

This document defines the patterns and procedures for detecting different content types in existing writing projects. Use these patterns during the analysis phase (Step 2) of migration.

## Detection Strategy

### Systematic Scanning

1. **List all directories and subdirectories** in project path
2. **Identify all markdown (.md) files**
3. **Note file organization patterns**
4. **Apply detection patterns** to categorize content
5. **Document findings** in content inventory

### Subprocess Optimization

For large projects with many files:
- Use subprocess for parallel file scanning
- Purpose: Efficiently traverse large directory structures
- Return: Complete directory tree and file listing
- Fallback: Sequential scanning in main thread

## Chapter Detection

### Folder Patterns

Look for folders with these names:
- `chapters/`
- `chapitres/` (French)
- `chapter/`
- `text/`
- `manuscript/`
- `manuscrit/` (French)
- `book/`
- `content/`

### File Patterns

Look for files with these patterns:
- `chapter-*.md` (numbered)
- `chapitre-*.md` (French, numbered)
- `ch-*.md` (abbreviated)
- `chapter-*.txt` (text format)
- Sequential numbering: 01, 02, 03...

### Confirmation Criteria

- **Minimum**: 3 files with chapter patterns
- **Strong**: Sequential numbering (01, 02, 03...)
- **Content**: Narrative prose, dialogue, scene descriptions

### What to Record

For each chapter source:
- **Count**: Total number of chapter files
- **Location**: Full path to chapter folder
- **Files**: List or summary of file names
- **Format**: File extension (md, txt, docx, etc.)
- **Numbering**: Sequential or non-sequential

## Character Detection

### Folder Patterns

Look for folders with these names:
- `characters/`
- `personnages/` (French)
- `chars/` (abbreviated)
- `cast/`
- `protagonists/`
- `people/`
- `roles/`

### File Patterns

Look for:
- Individual character files (e.g., `protagonist.md`, `hero.md`)
- Character name files (e.g., `john-doe.md`, `jane-smith.md`)
- Character dossiers with multiple sections

### Content Indicators

Files may contain:
- Physical descriptions
- Personality traits
- Backstory
- Psychology/motivation
- Relationships
- Character arcs

### Confirmation Criteria

- **Minimum**: 1 file with character content
- **Strong**: Multiple character files in dedicated folder
- **Content**: Named individuals with descriptions

### What to Record

For each character source:
- **Count**: Total number of character files
- **Location**: Full path to character folder
- **Format**: Individual files or combined document
- **Depth**: Basic (name/description) or detailed (psychology/arcs)

## Theme Detection

### Folder Patterns

Look for folders with these names:
- `themes/`
- `thematiques/` (French)
- `motifs/`
- `ideas/`
- `symbols/`
- `concept/`

### File Patterns

Look for:
- `themes.md`
- `symbolism.md`
- `motifs.md`
- Files about themes, symbols, metaphors

### Content Indicators

Files may contain:
- Theme definitions
- Symbol meanings
- Motif tracking
- Thematic analysis
- Symbol lists

### Confirmation Criteria

- **Minimum**: 1 file with theme content
- **Strong**: Dedicated folder with multiple theme files
- **Content**: Thematic concepts, symbols, or motifs

### What to Record

For each theme source:
- **Status**: DETECTED or NOT DETECTED
- **Location**: Full path if found
- **Format**: Single file or multiple files
- **Depth**: List only or detailed analysis

## Psychology Detection

### Folder Patterns

Look for folders with these names:
- `psychology/`
- `psychologie/` (French)
- `character-psychology/`
- `depth/`
- `motivation/`
- `inner-life/`

### File Patterns

Look for:
- `psychology.md`
- `motivation.md`
- `character-arcs.md`
- Files about motivations, emotional states, internal conflicts

### Content Indicators

Files may contain:
- Character motivations
- Psychological profiles
- Emotional states
- Internal conflicts
- Character arcs
- Trauma/backstory psychological impact

### Confirmation Criteria

- **Minimum**: 1 file with psychological content
- **Strong**: Dedicated folder with character psychology files
- **Content**: Deep character analysis beyond surface traits

### What to Record

For each psychology source:
- **Status**: DETECTED or NOT DETECTED
- **Location**: Full path if found
- **Format**: Individual files or combined
- **Integration**: Separate or part of character files

## Structure Detection

### Folder Patterns

Look for folders with these names:
- `structure/`
- `architecture/`
- `outline/`
- `plan/`
- `plot/`
- `story-structure/`

### File Patterns

Look for:
- `structure.md`
- `outline.md`
- `plot.md`
- `beats.md`
- `breakdown.md`

### Content Indicators

Files may contain:
- Plot outlines
- Beat sheets
- Scene lists
- Story structure analysis
- Act breakdowns
- Chapter summaries
- Plot points

### Confirmation Criteria

- **Minimum**: 1 file with structural content
- **Strong**: Detailed outline or beat sheet
- **Content**: Plot organization, scene breakdowns

### What to Record

For each structure source:
- **Status**: DETECTED or NOT DETECTED
- **Location**: Full path if found
- **Format**: Outline, beat sheet, or other
- **Detail**: High-level or detailed breakdown

## Location Detection

### Folder Patterns

Look for folders with these names:
- `locations/`
- `lieux/` (French)
- `places/`
- `settings/`
- `world/`
- `scenes/`

### File Patterns

Look for:
- Individual location files
- `settings.md`
- `world-building.md`

### Content Indicators

Files may contain:
- Location descriptions
- Setting details
- World-building notes
- Scene locations

### Confirmation Criteria

- **Minimum**: 1 file with location content
- **Strong**: Multiple location files in dedicated folder
- **Content**: Descriptions of places/settings

### What to Record

For each location source:
- **Status**: DETECTED or NOT DETECTED
- **Location**: Full path if found
- **Count**: Number of location files
- **Detail**: Brief mentions or detailed descriptions

## Timeline Detection

### Folder Patterns

Look for folders with these names:
- `timeline/`
- `chronologie/` (French)
- `time/`
- `chronology/`
- `events/`

### File Patterns

Look for:
- `timeline.md`
- `chronology.md`
- `events.md`
- `calendar.md`

### Content Indicators

Files may contain:
- Chronological events
- Timelines
- Calendars
- Event sequences
- Date tracking

### Confirmation Criteria

- **Minimum**: 1 file with timeline content
- **Strong**: Organized timeline with dates
- **Content**: Chronological event tracking

### What to Record

For each timeline source:
- **Status**: DETECTED or NOT DETECTED
- **Location**: Full path if found
- **Format**: Timeline, calendar, or event list
- **Detail**: Simple list or detailed timeline

## Other Content Detection

### Common Additional Content

**Notes**:
- Folders: `notes/`, `ideas/`, `scratch/`, `thoughts/`
- Content: Random notes, ideas, snippets

**Research**:
- Folders: `research/`, `reference/`, `inspiration/`
- Content: Research materials, references

**Drafts**:
- Folders: `drafts/`, `draft/`, `wip/`
- Content: Early drafts, work-in-progress

**Publishing**:
- Folders: `publishing/`, `submission/`, `query/`
- Content: Query letters, submission tracking

### What to Record

For any additional content:
- **Type**: What kind of content (notes, research, etc.)
- **Location**: Full path
- **Relevance**: Useful for BBB or not
- **Action**: Migrate, archive, or ignore

## Non-Standard Structures

### Handling Unusual Organizations

When projects don't follow standard patterns:

1. **Analyze folder names** for semantic meaning
2. **Read file contents** to determine purpose
3. **Map by content type** not folder name
4. **Document assumptions** in migration plan
5. **Ask author for clarification** if uncertain

### Red Flags

Watch for:
- Flat structure (all files in root)
- Combined files (multiple content types in one file)
- Scattered content (same content type in multiple locations)
- Unconventional naming
- Non-standard file formats

## Detection Best Practices

1. **Be thorough** - Check every folder and file
2. **Document assumptions** - Note why you categorized something
3. **Stay flexible** - Not all projects follow conventions
4. **Ask for confirmation** - When uncertain, verify with author
5. **Preserve everything** - Better to migrate too much than too little
6. **Think semantically** - What is this content FOR, not just what it's named

## Content Inventory Template

After detection, generate inventory:

```markdown
## Content Detected

### Chapters
- **Count:** [number]
- **Location:** [path/to/chapters]
- **Files:** [list or summary]
- **Format:** [md/txt/other]

### Characters
- **Count:** [number]
- **Location:** [path/to/characters]
- **Format:** [individual files or combined]

### Themes
- **Status:** [detected/not detected]
- **Location:** [path if found]

### Locations
- **Status:** [detected/not detected]
- **Location:** [path if found]

### Psychology
- **Status:** [detected/not detected]
- **Location:** [path if found]

### Structure
- **Status:** [detected/not detected]
- **Location:** [path if found]

### Other Content
- [List any other significant folders/files]
```
