---
name: 'step-02-format'
description: 'Format and structure bible data sections'

# Navigation
nextStepFile: './step-03-crossref.md'

# Output
outputFile: '{bbb_output_folder}/bible/complete-bible-{date}.md'
---

# Step 2: Format Bible Sections

## STEP GOAL:
To format and structure each bible dimension with clean headings, consistent formatting, and visual hierarchy for reader-friendly reference.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Character Keeper (Marie)** performing systematic bible formatting
- Like a curator organizing reference materials for easy navigation
- Clean, consistent formatting is essential for usable reference documents
- You structure existing data, don't create new content

### Step-Specific Rules:
- Focus ONLY on formatting and structure from loaded data
- FORBIDDEN to add new information or modify source data
- Use consistent heading levels (H1 for main sections, H2 for subsections, H3 for details)
- Preserve all content from source files
- Create visual hierarchy with formatting (bold, lists, tables as appropriate)

## EXECUTION PROTOCOLS:
- Format dimensions in standard order (chronologie → lieux → objets → personnes → themes)
- Apply consistent heading structure to each dimension
- Preserve all content from loaded data
- Add section dividers for visual separation
- Append formatted sections to output file
- Auto-proceed to step 3 after formatting complete

## CONTEXT BOUNDARIES:
- Has access to all loaded bible data from step 1
- Formatting is additive — append to output file
- Focus: Structure and presentation, not cross-referencing (next step)

## REFERENCE DOCUMENTS

This step uses the following reference documents and templates:

- **Formatting Specifications:** `../data/references/bible-dimension-formatting-specs.md`
- **Export Procedures:** `../data/references/export-procedures.md`
- **Section Headers:** `../data/templates/section-headers.md`
- **Placeholders:** `../data/templates/placeholder-content.md`
- **Character Entries:** `../data/templates/character-summary-entry.md`

These documents contain detailed formatting templates, procedures, and quality standards for all bible dimensions.

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Formatting Phase

"**Formatting Bible Sections...**

Now I'll structure each dimension with clear headings and consistent formatting. Think of this as organizing a reference library — everything gets a proper place and clear labels.

Formatting in progress..."

### 2. Format All Bible Dimensions (CORE)

Format each dimension in standard order using the specifications from `../data/references/bible-dimension-formatting-specs.md`:

**For each dimension (Chronologie → Lieux → Objets → Personnes → Themes):**

1. Create section header using template from `../data/templates/section-headers.md`
2. Append full content from source OR placeholder from `../data/templates/placeholder-content.md`
3. Log completion with word count

**After each dimension:**
"✅ **{Dimension Name}:** Formatted with {word_count} words"

### 3. Format Character Summaries (OPTIONAL)

Format character summaries using the template from `../data/templates/character-summary-entry.md`:

**If character_summaries exist:**
- For each character: Create H3 heading with name, role, arc_phase, description
- Use template format from reference doc

**If character_summaries empty:**
- Append placeholder from `../data/templates/placeholder-content.md`

**After formatting:**
"✅ **Character Summaries:** Formatted {count} profiles"

### 4. Update Output File Frontmatter

Update {outputFile} frontmatter:

```yaml
---
stepsCompleted: ['step-01-load', 'step-02-format']
lastStep: 'step-02-format'
date: '{current_date}'
user_name: '{user_name}'
project_name: '{project_name}'
exportType: 'complete-bible'
bibleDimensionsLoaded: {count}
characterSummariesLoaded: {count}
formattingComplete: true
---
```

### 5. Present Formatting Summary

Display:

"**Formatting Complete!**

### Bible Sections Formatted

| Section | Status | Word Count |
|---------|--------|------------|
| Chronologie | ✅/⚠️ | {count} |
| Lieux | ✅/⚠️ | {count} |
| Objets | ✅/⚠️ | {count} |
| Personnes | ✅/⚠️ | {count} |
| Themes | ✅/⚠️ | {count} |
| Character Summaries | ✅/⚠️ | {count} profiles |

**Total Word Count:** {total_words}

**All bible data formatted with consistent structure and headings. Ready to add cross-references and table of contents.**"

**Select:** `[C]` Continue to Cross-Referencing

### MENU HANDLING LOGIC:

- IF C: Update {outputFile} frontmatter with stepsCompleted: ['step-01-load', 'step-02-format', 'step-03-crossref'], lastStep: 'step-03-crossref', then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- All 5 bible dimensions formatted with section headers
- Character summaries formatted if available
- Consistent heading structure applied (H1 for main sections, H2 for subsections)
- All source content preserved (no data loss)
- Placeholders added for missing dimensions
- Output file updated with formatted content
- Frontmatter updated with formatting completion status

### SYSTEM FAILURE:
- Not formatting all loaded dimensions
- Not preserving source content
- Inconsistent heading structure
- Missing section headers or dividers
- Not appending to output file
- Not updating frontmatter

**Master Rule:** Formatting creates the visual structure that makes the bible usable as a reference. Every dimension should be clearly labeled, consistently formatted, and fully preserved. The cross-referencing phase depends on having well-structured sections to link between.
