---
name: 'step-03-crossref'
description: 'Add table of contents and cross-references'

# Navigation
nextStepFile: './step-04-export.md'

# Output
outputFile: '{bbb_output_folder}/bible/complete-bible-{date}.md'
---

# Step 3: Add Cross-References

## STEP GOAL:
To add a comprehensive table of contents and cross-references between related entries in the bible (e.g., character names in chronologie linked to personnes section).

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Character Keeper (Marie)** adding navigational aids to the bible
- Like a reference librarian adding cross-references and index entries
- Good cross-referencing makes the bible infinitely more usable
- You add navigation structure, don't modify content

### Step-Specific Rules:
- Focus ONLY on adding TOC and cross-reference links
- FORBIDDEN to modify existing content or add new information
- Create internal links using standard markdown anchor syntax
- Extract character names, locations, objects from existing content
- Add TOC at the beginning of the document

## EXECUTION PROTOCOLS:
- Extract key entities (characters, locations, objects, themes) from formatted sections
- Generate table of contents with anchor links
- Add cross-reference links where entities appear in multiple sections
- Prepend TOC to output file (insert before existing content)
- Auto-proceed to step 4 after cross-referencing complete

## CONTEXT BOUNDARIES:
- Has access to formatted bible content from step 2
- Cross-referencing is additive — adds TOC and links, doesn't modify content
- Focus: Navigation and connectivity between sections

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Cross-Referencing Phase

"**Adding Cross-References...**

Now I'll add a table of contents and create links between related entries. This makes it easy to jump from a character's mention in the timeline to their full profile, or from a location to its description.

Adding cross-references in progress..."

### 2. Extract Key Entities (CORE)

From the formatted bible content, extract:

**Character Names:**
- Scan personnes section for all character names (H3 headings typically)
- Store as: `entity_characters` array with name, anchor_id
- Pattern: names from "### [Character Name]" headings

**Location Names:**
- Scan lieux section for all location names (H3 headings or list items)
- Store as: `entity_locations` array with name, anchor_id
- Pattern: names from "### [Location Name]" headings

**Object Names:**
- Scan objets section for all object names (H3 headings or list items)
- Store as: `entity_objects` array with name, anchor_id
- Pattern: names from "### [Object Name]" headings or "**Object:** [Name]"

**Theme Names:**
- Scan themes section for all theme names (H3 headings or list items)
- Store as: `entity_themes` array with name, anchor_id
- Pattern: names from "### [Theme Name]" headings

**After extraction:**
"✅ **Entities Extracted:** {total} entities
  - Characters: {count}
  - Locations: {count}
  - Objects: {count}
  - Themes: {count}"

### 3. Generate Table of Contents (CORE)

Create comprehensive TOC:

```markdown
# Table of Contents

## Bible Dimensions

- [Chronologie (Timeline)](#chronologie-timeline)
- [Lieux (Locations)](#lieux-locations)
- [Objets (Objects)](#objets-objects)
- [Personnes (Characters)](#personnes-characters)
- [Themes (Thematic)](#themes-thematic)
- [Character Summaries](#character-summaries)

## Quick Reference

### Characters
{for each character: - [{name}](#{anchor_id})}

### Locations
{for each location: - [{name}](#{anchor_id})}

### Objects
{for each object: - [{name}](#{anchor_id})}

### Themes
{for each theme: - [{name}](#{anchor_id})}

---

```

**Anchor ID Format:**
- Convert to lowercase, replace spaces with hyphens, remove special chars
- Example: "Jean Dupont" → "#jean-dupont"

**After generation:**
"✅ **Table of Contents:** Generated with {total_entries} entries"

### 4. Add Cross-Reference Links (OPTIONAL)

For formatted sections, add cross-reference links where entities appear:

**In Chronologie section:**
- Find character names in event descriptions
- Replace with: `[{name}](#{anchor_id})` linking to personnages section
- Find location names in event descriptions
- Replace with: `[{name}](#{anchor_id})` linking to lieux section

**In Personnes section:**
- Find location names in character descriptions
- Replace with: `[{name}](#{anchor_id})` linking to lieux section
- Find object names in character descriptions
- Replace with: `[{name}](#{anchor_id})` linking to objets section

**Note:** Cross-referencing is best-effort based on entity extraction. Not all mentions may be linked if patterns don't match.

**After cross-referencing:**
"✅ **Cross-References:** Added {total_links} links between sections"

### 5. Insert Table of Contents (CORE)

Prepend the TOC to the beginning of the output file:

- Read current content of {outputFile}
- Insert TOC after frontmatter but before "## Loading Complete"
- Preserve all existing content
- Write updated content back to {outputFile}

**After insertion:**
"✅ **TOC Inserted:** Added at beginning of document"

### 6. Update Output File Frontmatter

Update {outputFile} frontmatter:

```yaml
---
stepsCompleted: ['step-01-load', 'step-02-format', 'step-03-crossref']
lastStep: 'step-03-crossref'
date: '{current_date}'
user_name: '{user_name}'
project_name: '{project_name}'
exportType: 'complete-bible'
bibleDimensionsLoaded: {count}
characterSummariesLoaded: {count}
formattingComplete: true
crossrefComplete: true
totalEntities: {total}
totalLinks: {total}
---
```

### 7. Present Cross-Referencing Summary

Display:

"**Cross-Referencing Complete!**

### Navigation Aids Added

| Feature | Status | Details |
|---------|--------|---------|
| Table of Contents | ✅ | {entries} entries |
| Character Links | ✅ | {count} links |
| Location Links | ✅ | {count} links |
| Object Links | ✅ | {count} links |
| Theme Links | ✅ | {count} links |

**Total Cross-References:** {total_links}

**The bible now has a table of contents and internal links for easy navigation between related entries. Ready to finalize and create the latest symlink.**"

**Select:** `[C]` Continue to Export

### MENU HANDLING LOGIC:

- IF C: Update {outputFile} frontmatter with stepsCompleted: ['step-01-load', 'step-02-format', 'step-03-crossref', 'step-04-export'], lastStep: 'step-04-export', then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Table of contents generated with all main sections
- Quick reference section created for characters, locations, objects, themes
- Entity names extracted from formatted content
- Cross-reference links added where entities appear in multiple sections
- TOC inserted at beginning of output file
- All existing content preserved
- Frontmatter updated with cross-referencing completion status

### SYSTEM FAILURE:
- Not generating table of contents
- Not extracting key entities from content
- Not adding cross-reference links
- Not inserting TOC at beginning of file
- Modifying existing content instead of just adding links
- Not updating frontmatter

**Master Rule:** Cross-referencing transforms the bible from a static document into an interconnected reference. The TOC provides overview navigation, while cross-reference links connect related entries. The final export phase depends on having a complete, navigable document.
