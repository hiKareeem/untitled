---
name: 'step-03-finalize'
description: 'Finalize edited chapter and update metadata if needed'

# Output
outputFile: '{bbb_output_folder}/chapters/chapter-{chapter_number}.md'
metaFile: '{bbb_output_folder}/chapters/chapter-{chapter_number}-meta.yaml'
---

# Step 3: Finalize Edits

## STEP GOAL:

To finalize the edited chapter and update metadata if the changes affect the summary or key points.

## MANDATORY SEQUENCE

### 1. Review Changes

"**Edit Summary for Chapter {N}:**

Changes made:
{list of edits applied}

Do these changes affect the chapter summary or key points?"

### 2. Update Metadata (If Needed)

IF changes affect summary:
- Regenerate summary section
- Update keyPoints if needed
- Update lastModified date

IF no summary changes:
- Update lastModified date only

### 3. Save and Confirm

"**Chapter {N} Edit Complete**

- Chapter updated: ✅
- Metadata updated: {yes/no}
- Last Modified: {date}

Your chapter edits have been saved."

(End of Edit workflow)
