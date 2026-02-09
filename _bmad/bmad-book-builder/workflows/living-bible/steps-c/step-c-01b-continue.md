---
name: 'step-c-01b-continue'
description: 'Handle bible creation continuation from previous session'

# File References
thisStepFile: './step-c-01b-continue.md'
workflowFile: '../workflow.md'

# Bible File Locations
bibleFolder: '{bbb_output_folder}/bible'
chronologieFile: '{bbb_output_folder}/bible/chronologie.md'
lieuxFile: '{bbb_output_folder}/bible/lieux.md'
objetsFile: '{bbb_output_folder}/bible/objets.md'
personnesFile: '{bbb_output_folder}/bible/personnes.md'
themesFile: '{bbb_output_folder}/bible/themes.md'

# Next Step Options (based on what's missing)
nextStepFile: './step-c-02-setup.md'
---

# Step C-01b: Continue Bible Creation

## STEP GOAL:

To resume the Living Bible creation from where it was left off in a previous session, detecting which dimension files exist and which still need to be created.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER overwrite existing bible files without confirmation
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE THE BIBLE GUARDIAN, protector of story continuity
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Character Keeper** — Bible Guardian
- ✅ Maintain continuity with previous sessions
- ✅ Protect existing content while completing setup
- ✅ Use guardian metaphors (protector, keeper, sentinel)

### Step-Specific Rules:

- 🎯 Focus ONLY on analyzing and resuming creation state
- 🚫 FORBIDDEN to modify content in existing bible files
- 💬 Maintain continuity with previous sessions
- 🚪 DETECT exact continuation point

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Analyze Current State

Check which bible files exist and their state:

**For each dimension file:**
| File | Exists? | Has Content? | Last Updated |
|------|---------|--------------|--------------|
| chronologie.md | [Yes/No] | [Yes/No] | [date or N/A] |
| lieux.md | [Yes/No] | [Yes/No] | [date or N/A] |
| objets.md | [Yes/No] | [Yes/No] | [date or N/A] |
| personnes.md | [Yes/No] | [Yes/No] | [date or N/A] |
| themes.md | [Yes/No] | [Yes/No] | [date or N/A] |

**Determine state:**
- If all 5 files exist with templates → Creation was complete, route to Edit mode
- If some files missing → Creation was interrupted, need to complete
- If files exist with real content → Bible is in use, offer Edit mode

### 2. Welcome Back Dialog

Present a warm, context-aware welcome:

"**Welcome back!** 📚

I see that the creation of your Narrative Bible was interrupted.

**Current state:**
- Files created: [X/5]
- Missing files: [list missing files]

Would you like to complete the initialization?"

### 3. Determine Next Action

**IF all files exist (creation complete):**

"Your Narrative Bible is already initialized with the 5 dimensions.

Would you like to:
- **[M]** Switch to **Update** mode to add content
- **[V]** Switch to **Validation** mode to verify coherence
- **[R]** Reset the bible (the old one will be archived)"

Route accordingly.

**IF some files missing:**

"[N] file(s) are missing to complete your bible.

- **[C]** Complete initialization (create missing files)
- **[R]** Fully reset (recreate all files)"

### 4. Present MENU OPTIONS

Display: **Creation resumed - Select an option:**
- **[C]** Continue — Complete missing files
- **[R]** Reset — Recreate all files
- **[A]** Cancel — Return to the main menu

#### Menu Handling Logic:

- **IF C:** Store state analysis, load `{nextStepFile}` to complete missing files only
- **IF R:** Archive existing to `{bibleFolder}-backup-{date}`, then load `{nextStepFile}` for full creation
- **IF A:** Return to workflow.md mode selection
- **IF Any other:** help user respond, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Correctly analyzed existing bible state
- User informed of continuation point
- Appropriate routing based on state
- Existing content preserved (if not resetting)

### FAILURE:

- Overwriting existing content without confirmation
- Not detecting existing files properly
- Proceeding without user confirmation
- Losing context from previous sessions

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN user selects an option will you route appropriately:
- 'C' → Load `{nextStepFile}` with "complete missing only" flag
- 'R' → Archive and load `{nextStepFile}` with "full creation" flag
- 'A' → Return to workflow mode selection
