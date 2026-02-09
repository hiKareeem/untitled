---
name: 'step-05b-complete'
description: 'Save character to story bible and complete autonomous workflow'

# File References
outputFile: '{project-root}/characters/{character_name}-dossier.md'
bibleIndex: '{project-root}/characters/index.md'

---

# Step 5b: Complete & Save to Bible (Autonomous)

## STEP GOAL:

To finalize **{characterName}**'s dossier, save it to the story bible, update the character index, and mark the workflow as complete.

## MANDATORY EXECUTION RULES (READ FIRST):

See: `../../../data/procedures/mode-procedures.md#common-execution-rules-all-modes`

### Step-Specific Rules:

- 🎯 This is a FINALIZATION step — save and organize, no more character development
- 💬 Celebrate completion — character creation is significant work
- 🚫 NO MORE EDITS at this stage — only saving and indexing
- ✅ Maintain story bible as sacred trust

## EXECUTION PROTOCOLS:

- 🎯 Follow the MANDATORY SEQUENCE exactly
- 💾 Save final dossier to story bible
- 📖 Update character index
- 📖 Mark workflow as complete in frontmatter
- 🔄 Present completion options

## CONTEXT BOUNDARIES:

- Available context: Character Keeper agent persona, complete dossier, story bible
- Focus: Finalization and organization
- Limits: No character development at this stage
- Dependencies: All previous steps must be complete

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Welcome to Completion Phase

"**Congratulations!** 🎉

**{characterName}** is complete. Through the autonomous process, we've created a complex, authentic character with depth, contradictions, voice, and a compelling transformation arc.

Let me save them to the story bible for use in your stories."

### 2. Final Verification

"**Before I finalize, let me verify the dossier is complete...**"

Check `{outputFile}` for all required sections (9 sections):

See `../../../data/references/character-frameworks.md#quality-standards-reference#completeness`

**IF any section is incomplete:**

"I notice [section] needs attention. Would you like to:
- [1] Return to review step to complete it
- [2] Proceed as-is (will mark section as 'To be completed')"

Wait for author choice.

**IF all sections complete:**

"All sections complete. Proceeding to save..."

### 3. Update Completion Metadata

Update `{outputFile}` frontmatter:

See template in `../../../data/templates/character-templates.yaml#frontmatter_complete_mode_b`

### 4. Verify Output Location

Verify `{outputFile}` is saved at the correct location:
`{project-root}/characters/{character_name}-dossier.md`

**Note:** The file should already exist from step-01-init. This step updates the metadata.

### 5. Update Character Index

"**Updating the story bible character index...**"

See: `../../../data/procedures/mode-procedures.md#common-procedures#character-index-update`

**IF `{bibleIndex}` exists:**
Read the index file and add/update the entry for **{characterName}**

See template in `../../../data/templates/character-templates.yaml#index_entry_template`
(Note: Status should be "COMPLETE (Autonomous Mode)")

**IF `{bibleIndex}` does not exist:**
Create the index file

See template in `../../../data/templates/character-templates.yaml#index_file_template`

### 6. Present Completion Summary

"**✅ CHARACTER COMPLETE!**"

Display summary:

```
═══════════════════════════════════════════════════════════
  CHARACTER DOSSIER: {characterName}
═══════════════════════════════════════════════════════════

  📁 Location: {outputFile}
  📅 Created: {completion_date}
  👤 Created by: {user_name}
  🎭 Mode: Autonomous
  🎭 Role: [story role]

  📚 SECTIONS COMPLETED:
  ✅ All 9 sections generated and approved

  🎯 CHARACTER HIGHLIGHTS:
  [3-5 bullet points of what makes this character distinctive]

═══════════════════════════════════════════════════════════
```

### 7. Present Next Steps Options

Display:

"**{characterName}** is now in the story bible, ready for use!

**What would you like to do next?**

**[N]** New Character — Create another character

**[E]** Edit — Make changes to {characterName}

**[V]** Validate — Check {characterName} against character standards

**[W]** Write Chapter — Use this character in a chapter (if workflow exists)

**[X]** Exit — Complete workflow"

#### Menu Handling Logic:

See: `../../../data/procedures/mode-procedures.md#menu-handling-logic`

- IF N: Reload `../../step-01-init.md` to create a new character
- IF E: Load `../../steps-e/step-01-assess.md` with `{outputFile}` as target
- IF V: Load `../../steps-v/step-01-validate.md` with `{outputFile}` as target
- IF W: Check if chapter writing workflow exists and offer to load it
- IF X: Present final completion message and end workflow

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- User can chat or ask questions — always respond and then redisplay the menu
- No further workflow steps after this point

### 8. Completion Message (IF X selected)

"**Goodbye!** 👋

**{characterName}** is saved and ready. Here's a quick reminder of what makes them special:

[Brief reminder of key character elements]

You created this character through autonomous mode — providing a concept that I developed into a full character profile. The result is a character with depth, contradictions, and a clear transformation arc.

Come back anytime to create more characters or use the Chapter Writer workflow to bring **{characterName}** into your story.

**Happy writing!** ✍️"

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- All 9 dossier sections complete and populated
- Output file saved to correct location
- Completion metadata added to frontmatter (with mode: B)
- Character index updated or created
- Completion summary presented
- Next steps options offered
- User confirms satisfaction with character

### ❌ SYSTEM FAILURE:

- Incomplete dossier sections not addressed
- Output file not saved to correct location
- Character index not updated
- No completion metadata added

**Master Rule:** A character isn't complete until they're properly saved and indexed in the story bible. Consistency is sacred.

## SPECIAL CASES:

See: `../../../data/procedures/mode-procedures.md#special-cases`

### Bible Index Corruption:
1. Alert the user: "The character index appears to be corrupted. Would you like me to recreate it?"
2. If yes, create fresh index with this character as first entry
3. If no, skip index update and alert user to manual fix needed

### Multiple Characters with Same Name:
1. Alert the user: "A character named '{characterName}' already exists in the bible. Would you like to:"
2. Options: [1] Overwrite / [2] Rename / [3] Keep both
3. Wait for user choice before proceeding
