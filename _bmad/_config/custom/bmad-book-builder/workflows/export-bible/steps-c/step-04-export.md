---
name: 'step-04-export'
description: 'Finalize export and create latest symlink'

# Navigation
nextStepFile: null

# Output
outputFile: '{bbb_output_folder}/bible/complete-bible-{date}.md'
latestFile: '{bbb_output_folder}/bible/latest-complete-bible.md'
bbb_output_folder: '{output_folder}'
---

# Step 4: Finalize Export

## STEP GOAL:
To finalize the exported bible document by cleaning up temporary sections, creating the latest symlink, and presenting completion summary.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Character Keeper (Marie)** completing the bible export process
- Like a librarian finishing a new reference edition and cataloging it for access
- Proper finalization ensures the bible is easy to find and use
- You finalize the compilation, don't modify content

### Step-Specific Rules:
- Focus ONLY on cleanup and file management
- FORBIDDEN to modify bible content in finalization
- Remove temporary sections (e.g., "## Loading Complete")
- Create latest symlink or copy for easy access
- Present comprehensive completion summary

## EXECUTION PROTOCOLS:
- Remove temporary/placeholder sections from output file
- Create latest-complete-bible.md symlink/copy pointing to current export
- Update final frontmatter with completion status
- Present summary with file location, statistics, and usage guidance
- No auto-proceed — this is the final step

## CONTEXT BOUNDARIES:
- Has access to complete bible document from step 3
- Finalization is last step — no continuation
- Focus: Cleanup and delivery, not content modification

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Finalization Phase

"**Finalizing Bible Export...**

Now I'll clean up the temporary sections and create the latest version link for easy access. Your complete bible will be ready for use!

Finalizing in progress..."

### 2. Clean Up Temporary Sections (CORE)

Remove placeholder sections from output file:

**Read current content of {outputFile}**
**Remove these temporary sections:**
- "## Loading Complete" section (if present)
- Any "Loading in progress..." placeholders
- Any intermediate status messages

**Preserve:**
- All frontmatter
- Table of Contents
- All bible dimension content
- All cross-references
- Character summaries
- All actual content (not status messages)

**Write cleaned content back to {outputFile}**

**After cleanup:**
"✅ **Cleanup Complete:** Removed temporary sections"

### 3. Create Latest Symlink/Copy (CORE)

Create easy access to the most recent export:

**Copy approach (most compatible):**
- Read content of {outputFile}
- Write identical content to {latestFile}
- This creates a copy that always points to the latest export

**Alternative: Symlink (if supported)**
- Create symlink from {latestFile} → {outputFile}
- Note: Use copy method if symlink creation fails

**After creation:**
"✅ **Latest Link Created:** latest-complete-bible.md now points to this export"

### 4. Update Final Frontmatter (CORE)

Update {outputFile} frontmatter with final status:

```yaml
---
stepsCompleted: ['step-01-load', 'step-02-format', 'step-03-crossref', 'step-04-export']
lastStep: 'step-04-export'
date: '{current_date}'
user_name: '{user_name}'
project_name: '{project_name}'
exportType: 'complete-bible'
bibleDimensionsLoaded: {count}
characterSummariesLoaded: {count}
formattingComplete: true
crossrefComplete: true
finalizationComplete: true
totalEntities: {total}
totalLinks: {total}
exportComplete: true
---
```

**Update frontmatter of {latestFile} with same values**

### 5. Generate Export Statistics

Calculate final statistics:

**Word Counts:**
- Total word count of exported bible
- Word count per dimension (chronologie, lieux, objets, personnes, themes)
- Word count of character summaries

**Entity Counts:**
- Total characters tracked
- Total locations tracked
- Total objects tracked
- Total themes tracked

**Cross-Reference Counts:**
- Total links added
- Links per dimension

**File Information:**
- File path: {outputFile}
- Latest link: {latestFile}
- File size (in words and estimated KB)

**Store as:** `export_stats` with all above values

### 6. Present Completion Summary

Display:

"**✅ Bible Export Complete!**

Your complete story bible has been compiled and formatted.

### Export Statistics

| Metric | Count |
|--------|-------|
| **Total Word Count** | {total_words} |
| **Bible Dimensions** | {count}/5 |
| **Characters Tracked** | {total_characters} |
| **Locations Tracked** | {total_locations} |
| **Objects Tracked** | {total_objects} |
| **Themes Tracked** | {total_themes} |
| **Cross-References** | {total_links} |

### Content Breakdown

| Dimension | Words | Entities |
|-----------|-------|----------|
| Chronologie | {words} | {events} events |
| Lieux | {words} | {count} locations |
| Objets | {words} | {count} objects |
| Personnes | {words} | {count} characters |
| Themes | {words} | {count} themes |
| Character Summaries | {words} | {count} profiles |

### Export Location

**Timestamped Version:**
`{outputFile}`

**Latest Version (always current):**
`{latestFile}`

### Usage

- **Quick Reference:** Open `latest-complete-bible.md` for the most recent version
- **Archive Access:** Timestamped versions are preserved in the bible folder
- **Navigation:** Use the Table of Contents to jump between sections
- **Cross-References:** Click on character/location/object names to jump to their detailed entries

---

**Your story bible is ready for use! Use it as a reference while writing, share it with collaborators, or review it to check story consistency.**"

### 7. Workflow Complete

**This is the final step.** No further action required.

Display final confirmation:

"**🎉 Export Bible Workflow Complete!**

Thank you for using the Export Bible workflow. Your complete story bible has been successfully compiled.

To run this workflow again, use: `/export-bible`

For other workflows, use `/status-report` or see available commands."

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Temporary sections removed from output file
- All content preserved (no data loss in cleanup)
- latest-complete-bible.md created (copy or symlink)
- Frontmatter updated with final completion status
- Export statistics calculated accurately
- Comprehensive completion summary presented
- File locations clearly communicated

### SYSTEM FAILURE:
- Not removing temporary sections
- Removing actual content during cleanup
- Not creating latest symlink/copy
- Not updating frontmatter with completion status
- Not calculating or presenting statistics
- Not communicating file locations

**Master Rule:** Finalization delivers the finished product. The bible should be clean, complete, and accessible. The latest link ensures the most recent version is always easy to find, while timestamped versions preserve export history. The completion summary gives the user clear confirmation of what was produced and where to find it.
