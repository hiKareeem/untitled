---
name: 'step-01-load'
description: 'Load existing chapter for editing'

# Navigation
nextStepFile: './step-02-edit.md'

# Input
chaptersFolder: '{bbb_output_folder}/book-1/chapters/'
---

# Step 1: Load Chapter for Editing

## STEP GOAL:

To load an existing chapter for targeted editing.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- YOU ARE A FACILITATOR, not a content generator

### Role Reinforcement:

- You are helping edit an existing chapter
- Load chapter and context for targeted modifications

## MANDATORY SEQUENCE

### 1. List Available Chapters

Search {chaptersFolder} for existing chapters:

"**Available Chapters for Editing:**

{list chapters with status and word count}

Which chapter would you like to edit?"

### 2. Load Selected Chapter

Load the chapter and its metadata:
- chapter-{N}.md (content)
- chapter-{N}-meta.yaml (metadata)

"**Loaded Chapter {N}: {title}**

- Words: {count}
- Status: {status}
- Last Modified: {date}

Ready to proceed to editing."

### 3. Present Menu

**Select an option:** `[C]` Continue to Edit

### MENU HANDLING LOGIC:

- IF C: Load {nextStepFile}
- IF Any other: Help user, redisplay menu
