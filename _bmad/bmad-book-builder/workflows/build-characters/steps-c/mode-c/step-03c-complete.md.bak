---
name: 'step-03c-complete'
description: 'Save character(s) to story bible and complete free generation workflow'

# File References
outputFile: '{project-root}/characters/{character_name}-dossier.md'
bibleIndex: '{project-root}/characters/index.md'

# Parameters
single: true

---

# Step 3c: Complete & Save to Bible (Free Generation)

## STEP GOAL:
To finalize the generated character dossier(s), save them to the story bible, update the character index, and mark the workflow as complete.

## MANDATORY EXECUTION RULES (READ FIRST):

See: `../../../data/procedures/mode-procedures.md` - Mode C and Completion Procedure sections

### Step-Specific Rules:
- 🎯 This is a FINALIZATION step — save and organize, no more character development
- 💬 Celebrate completion — character creation is significant work
- 🚫 NO MORE EDITS at this stage — only saving and indexing
- ✅ Maintain story bible as sacred trust

## EXECUTION PROTOCOLS:
- 🎯 Follow the MANDATORY SEQUENCE exactly
- 💾 Save final dossier(s) to story bible
- 📖 Update character index
- 📖 Mark workflow as complete in frontmatter
- 🔄 Present completion options

## MANDATORY SEQUENCE

### 1. Welcome to Completion Phase

**IF single mode:**
"**Congratulations!** 🎉

**{characterName}** is complete. Through free generation, I've created a complex, authentic character with depth, contradictions, voice, and a compelling transformation arc.

Let me save them to the story bible for use in your stories."

**IF multiple mode:**
"**Congratulations!** 🎉

Your character cast is complete! Through free generation, I've created [N] diverse characters, each with depth, contradictions, voice, and compelling transformation arcs.

Let me save them to the story bible for use in your stories."

### 2. Final Verification

"**Before I finalize, let me verify the dossier(s) are complete...**"

**IF single:**
Check `{outputFile}` for all required sections.

**IF multiple:**
Check each character's file for all required sections.

**IF any section is incomplete:**
"I notice [character]'s [section] needs attention. Would you like to:
- [1] Return to generation step to complete it
- [2] Proceed as-is (will mark section as 'To be completed')"

Wait for author choice.

**IF all sections complete:**
"All sections complete. Proceeding to save..."

### 3. Update Completion Metadata

**IF single:**
Update `{outputFile}` frontmatter (see templates in `../../../data/templates/character-templates.yaml`):

```yaml
---
stepsCompleted: ['step-01-init', 'step-02c', 'step-03c-complete']
lastStep: 'step-03c-complete'
mode: C
single: true
characterName: {character_name}
date: {start_date}
completedDate: {current_date}
user_name: {user_name}
status: COMPLETE
---
```

**IF multiple:**
Update each character's frontmatter with `single: false`.

### 4. Update Character Index

"**Updating the story bible character index...**"

See completion procedure in `../../../data/procedures/mode-procedures.md`

**IF `{bibleIndex}` exists:** Add/update entries for all characters

**IF `{bibleIndex}` does not exist:** Create the index file with all characters

### 5. Present Completion Summary

**IF single:**
"**✅ CHARACTER COMPLETE!**"

Display:
- Location, creation date, mode, role
- All 9 sections completed
- Character highlights (3-5 bullet points)

**IF multiple:**
"**✅ CHARACTERS COMPLETE!**"

Display:
- Creation date, mode, character count
- Full cast list with roles
- Output location

### 6. Present Next Steps Options

"**The character(s) are now in the story bible, ready for use!**

**What would you like to do next?**

**[N]** New Characters — Create more characters
**[E]** Edit — Make changes to a character
**[V]** Validate — Check character(s) against standards
**[W]** Write Chapter — Use these characters in a chapter (if workflow exists)
**[X]** Exit — Complete workflow"

#### Menu Handling Logic:
- IF N: Reload `../../step-01-init.md`
- IF E: Load `../../steps-e/step-01-assess.md`
- IF V: Load `../../steps-v/step-01-validate.md`
- IF W: Check if chapter writing workflow exists
- IF X: Present final completion message

### 7. Completion Message (IF X selected)

**IF single:**
"**Goodbye!** 👋

**{characterName}** is saved and ready. Here's a quick reminder:
[Brief reminder of key character elements]

You created this character through free generation — I designed them based on your story context. The result is a character with depth, contradictions, and a clear transformation arc, ready to drive your narrative.

Come back anytime to create more characters or use the Chapter Writer workflow to bring **{characterName}** into your story.

**Happy writing!** ✍️"

**IF multiple:**
"**Goodbye!** 👋

Your character cast is saved and ready! Here's what I created:
[Brief overview of the cast and their dynamics]

You created these characters through free generation — I designed them based on your story context, ensuring diversity and avoiding stereotypes. Each character has depth, contradictions, and a clear transformation arc, ready to drive your narrative.

Come back anytime to create more characters or use the Chapter Writer workflow to bring these characters into your story.

**Happy writing!** ✍️"

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- All 9 dossier sections complete for each character
- Output file(s) saved to correct location(s)
- Completion metadata added to frontmatter (with mode: C)
- Character index updated or created with all characters
- Completion summary presented
- Next steps options offered

### ❌ SYSTEM FAILURE:
- Incomplete dossier sections not addressed
- Output file(s) not saved to correct location
- Character index not updated
- No completion metadata added

**Master Rule:** A character isn't complete until they're properly saved and indexed in the story bible. Consistency is sacred.

## SPECIAL CASES:

See: `../../../data/procedures/mode-procedures.md` - Special Cases section
- Bible Index Corruption
- Multiple Characters with Same Name
- Large Cast Management (>5 characters)
