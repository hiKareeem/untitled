---
name: 'step-02-edit'
description: 'Make targeted edits to existing chapter'

# Navigation
nextStepFile: './step-03-finalize.md'

# Output
outputFile: '{bbb_output_folder}/book-1/chapters/chapter-{chapter_number}.md'

# Reference
antiSlopChecklist: '../data/anti-slop-checklist.md'
---

# Step 2: Edit Chapter

## STEP GOAL:

To make targeted edits to the loaded chapter based on author requests.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- NEVER generate content without user input
- YOU ARE A FACILITATOR helping with specific edits

### Role Reinforcement:

- Author directs what to change
- Make only requested modifications
- Maintain voice consistency

## MANDATORY SEQUENCE

### 1. Present Chapter Sections

"**Chapter {N} Sections:**

{list major sections/scenes}

What would you like to edit? You can:
- Request specific passage changes
- Adjust tone or pacing
- Fix continuity issues
- Revise dialogue
- Other modifications"

### 2. Collect Edit Requests

Wait for author to describe desired edits.

### 3. Apply Edits

For each edit request:
1. Locate the passage
2. Apply the change matching author's voice
3. Run anti-slop check
4. Show before/after

### 4. Confirm Edits

"**Edits Applied:**

{list changes made}

Proceed to finalize the edited chapter?"

**Select an option:** `[C]` Continue to Finalize `[M]` More Edits

### MENU HANDLING LOGIC:

- IF C: Update chapter, load {nextStepFile}
- IF M: Return to step 2 for more edits
