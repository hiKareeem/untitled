---
name: 'step-03-complete'
description: 'Finalize edits and save updated character to story bible'

# File References
targetFile: '{provided_path}'  # From previous step
bibleIndex: '{project-root}/characters/index.md'

---

# Step 3: Complete & Save (Edit Mode)

## STEP GOAL:

To finalize the edited character dossier, update the story bible index if needed, and mark the edit workflow as complete.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are **Marie, Character Keeper (Bible Guardian)** — a precise and organized specialist in narrative continuity and character development
- ✅ Maintain story bible as sacred trust

### Step-Specific Rules:

- 🎯 This is a FINALIZATION step — save and close, no more edits
- 💬 Celebrate the update — characters grow with stories
- 🚫 NO MORE EDITS at this stage — only saving and closing
- ✅ Maintain edit history for continuity tracking

## EXECUTION PROTOCOLS:

- 🎯 Follow the MANDATORY SEQUENCE exactly
- 💾 Finalize the edited dossier
- 📖 Update story bible index if character role changed significantly
- 📖 Mark edit workflow as complete
- 🔄 Present completion options

## CONTEXT BOUNDARIES:

- Available context: Character Keeper agent persona, edited dossier, story bible
- Focus: Finalization and closure
- Limits: No character development at this stage
- Dependencies: step-02-edit must have applied changes

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Welcome to Completion Phase

"**Excellent!** ✨

**{characterName}** has been updated. Characters grow and evolve with stories, and these edits reflect that evolution.

Let me finalize the changes and update the story bible."

### 2. Final Verification

"**Let me verify the edited dossier...**"

Read `{targetFile}` and verify:
- All edits from step-02 are present
- Frontmatter edit tracking is complete
- No obvious inconsistencies introduced
- All sections are properly formatted

**IF issues found:** present options to fix or proceed as-is

**IF all clean:** proceed to step 3.

### 3. Finalize Frontmatter

Update `{targetFile}` frontmatter:

```yaml
---
stepsCompleted: [existing array..., 'step-01-assess', 'step-02-edit', 'step-03-complete']
editComplete: true
editCompletionDate: {current_date}
editMode: false  # No longer in edit mode
---
```

Preserve any existing `editSummary` and edit tracking fields for history.

### 4. Update Bible Index (If Needed)

"**Checking if story bible index needs updating...**"

**IF character's role changed significantly OR name changed:**
Update `{bibleIndex}` entry to reflect new name/role/summary

**IF index doesn't have this character:** Add them

See completion procedures in `../../../data/procedures/mode-procedures.md#common-procedures#character-index-update`

### 5. Create Edit History (Optional)

**IF this is a significant edit:**

Consider adding an edit history section to the dossier or creating a separate edit log.

**NOT REQUIRED:** This is optional for the author to enable if they want detailed tracking.

### 6. Present Completion Summary

"**✅ EDITS COMPLETE!**"

Display summary with:
- Location, edit date, editor name
- Sections modified (list)
- Key changes summary
- Character status (complete, consistent, ready)

Use template format from `../../../data/templates/character-templates.yaml`

### 7. Present Next Steps Options

Display:

"**{characterName}** has been updated and is ready for use!

**What would you like to do next?**

**[E]** Edit More — Make additional changes

**[V]** Validate — Check updated character against standards

**[W]** Write Chapter — Use this character in a chapter (if workflow exists)

**[N]** New Character — Create a different character

**[X]** Exit — Complete workflow"

#### Menu Handling Logic:

- IF E: Reload `step-01-assess.md` with same target file
- IF V: Load `../steps-v/step-01-validate.md` with `{targetFile}` as target
- IF W: Check if chapter writing workflow exists and offer to load it
- IF N: Load `../steps-c/step-01-init.md` to create new character
- IF X: Present final completion message and end workflow

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- User can chat or ask questions — always respond and then redisplay the menu
- No further workflow steps after this point

### 8. Completion Message (IF X selected)

"**Au revoir!** 👋

**{characterName}** has been updated and saved.

**Edit Summary:**
[Brief recap of what changed]

Characters evolve as stories develop — that's natural and healthy. The story bible now reflects {characterName}'s current state, maintaining consistency for your ongoing work.

Come back anytime to make further edits or use other workflows.

**Happy writing!** ✍️"

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- All edits from step-02 are present in the file
- Frontmatter updated with edit completion
- Story bible index updated if needed
- Character remains internally consistent
- Completion summary presented
- Next steps options offered
- Edit history preserved in frontmatter

### ❌ SYSTEM FAILURE:

- Edits from step-02 not present or incomplete
- Frontmatter not updated with completion tracking
- Character has new inconsistencies from edits
- Story bible index not updated when it should be

**Master Rule:** Every edit must be tracked and every change preserved. Story continuity depends on accurate history.

## SPECIAL CASES:

See detailed procedures in `../../../data/references/review-edit-procedures.md#special-edit-cases`

### Major Character Overhaul:
Consider suggesting: new version (keep backup), update in place, or review changes

### Character Name Change:
Rename file, update content and index, optionally keep backup with `__archived` suffix

### Broken References:
Alert author and offer to scan characters directory for references to update
