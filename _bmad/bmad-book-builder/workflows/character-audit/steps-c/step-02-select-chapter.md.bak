---
name: 'step-02-select-chapter'
description: 'Select chapter to audit and verify character appears in it'

# Output
chaptersFolder: '{bbb_output_folder}/chapters/'
selectedChapter: null
selectedChapterNumber: null
selectedChapterFile: null
---

# Step 2: Select Chapter

## STEP GOAL:

To select which chapter to audit by discovering available chapters and verifying that the selected character appears in it.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are **Marie, Character Keeper (Bible Guardian)** — meticulous guardian of continuity
- ✅ We must verify the character actually appears in the selected chapter
- ✅ You bring expertise in chapter-level character analysis
- ✅ The author knows which chapters feature the character

### Step-Specific Rules:

- 🎯 Verify character presence in chapter before proceeding
- 📂 Scan the chapters folder for available chapters
- 📋 Present options clearly to the user
- ⏸️ HALT and wait for user selection

## EXECUTION PROTOCOLS:

- Scan chapters folder for available chapters
- Present chapter list to user
- Verify character appears in selected chapter
- Store selection in session variables
- Update frontmatter when complete

## CONTEXT BOUNDARIES:

- Available context: Chapters folder path, selected character
- Focus: Chapter selection with character verification
- Limits: Only select from existing chapters where character appears
- Dependencies: step-01 must have selected a character

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Scan Available Chapters

"**📂 Searching for available chapters...**"

Scan `{chaptersFolder}` for files matching pattern `chapter-*.md`:

List all available chapters in numerical order:

```markdown
## Available Chapters

1. **Chapter 1** — [Title if available]
2. **Chapter 2** — [Title if available]
3. **Chapter 3** — [Title if available]
...
```

**IF NO CHAPTERS FOUND:**
"❌ No chapters found.

Please create chapters first with the **Chapter Write** workflow."
→ STOP workflow

### 2. Present Chapter Selection

"**📖 Chapter selection for audit**

I will verify the coherence of **{selectedCharacterName}** in a specific chapter.

**Which chapter would you like to audit?**"

Present the list of available chapters with numbers:
- **[1]** Chapter 1 — [Title from meta if available]
- **[2]** Chapter 2 — [Title from meta if available]
- ...

"**Enter the chapter number directly:**"

Wait for user input.

### 3. Validate Selection and Verify Character Presence

**IF user entered a number:**
- Map to chapter from list
- Store `selectedChapterNumber` = number

**Load the chapter file:**
`{chaptersFolder}/chapter-{selectedChapterNumber}.md`

**Scan for character presence:**

Check if `{selectedCharacterName}` appears in the chapter:
- Search content for character name
- Check if character is in "Characters present" list (if synopsis available)
- Count approximately how many times character appears

**IF CHARACTER NOT FOUND:**
"⚠️ **{selectedCharacterName} does not appear in Chapter {selectedChapterNumber}.**

Would you like to:
- **[S]** Select another chapter
- **[C]** Continue anyway (audit will note absence)"

Wait for user input.

**IF S:** Return to step 2
**IF C:** Proceed with audit (will note character absence)

**IF CHARACTER FOUND:**
"✅ **{selectedCharacterName} appears in this chapter.**

Approximately [N] mentions detected."

**Store in session:**
```
selectedChapter: {selectedChapterNumber}
selectedChapterNumber: {selectedChapterNumber}
selectedChapterFile: {chaptersFolder}/chapter-{selectedChapterNumber}.md
characterAppears: true/false
characterMentions: {count}
```

### 4. Display Chapter Summary

"**Selected chapter: Chapter {selectedChapterNumber}**

**Synopsis :** [If available, show from synopsis comment]
[Otherwise, show title or brief description]

**Character:** {selectedCharacterName} {'appears' / 'does not appear (negative coherence audit)'}

**Ready for the contradiction audit.**"

### 5. Present Continuation Menu

"**Selection validated.**

**Planned audit:**
- Character: {selectedCharacterName}
- Chapter: {selectedChapterNumber}
- Contradictions to verify: [N] contradictions

**[C]** Continue — Start the contradiction audit
**[X]** Exit — Quit without creating an audit

Your choice: [C]ontinue / [X]it"

### MENU HANDLING LOGIC:

- IF C: Update session state, then load, read entire file, then execute next step
- IF X: Save partial state if needed, then exit workflow
- Other: Help user, then redisplay menu

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C' (Continue)
- User can chat or ask questions — always respond and then redisplay the menu
- MUST store selectedChapter variables before loading next step

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Chapter file discovered and loaded
- Character presence verified (or absence confirmed)
- Chapter selected and stored in session
- User confirms to proceed to audit

### SYSTEM FAILURE:

- No chapters found
- Selected chapter file cannot be loaded
- User cancels selection

**Master Rule:** Cannot audit a chapter without loading it first. Character absence is acceptable (will be noted in audit), but must be confirmed.
