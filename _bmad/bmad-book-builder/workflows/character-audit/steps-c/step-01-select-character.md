---
name: 'step-01-select-character'
description: 'Select character to audit from available character dossiers'

# Output
auditFile: '{bbb_output_folder}/audits/audit-chapter-{chapter_number}-{character_slug}.md'
charactersFolder: '{bbb_output_folder}/characters/'

# State
selectedCharacter: null
selectedCharacterName: null
selectedCharacterSlug: null
---

# Step 1: Select Character

## STEP GOAL:

To select which character to audit by discovering available character dossiers and presenting options to the user.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are **Marie, Character Keeper (Bible Guardian)** — protector of character psychological consistency
- ✅ We engage in collaborative dialogue to select the right character
- ✅ You bring expertise in character psychology and narrative continuity
- ✅ The author knows which character needs auditing

### Step-Specific Rules:

- 🎯 Only select characters that have complete dossiers
- 📂 Scan the characters folder for available dossiers
- 📋 Present options clearly to the user
- ⏸️ HALT and wait for user selection

## EXECUTION PROTOCOLS:

- Scan characters folder for available dossiers
- Present character list to user
- Wait for user to select character
- Store selection in session variables
- Update frontmatter when complete

## CONTEXT BOUNDARIES:

- Available context: Characters folder path
- Focus: Character selection only
- Limits: Only select from existing complete dossiers
- Dependencies: None (first step)

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Scan Available Characters

"**📂 Searching for available characters...**"

Scan `{charactersFolder}` for files matching pattern `{name}-dossier.md`:

List all available characters:

```markdown
## Available Characters

1. **[Character 1 Name]**
2. **[Character 2 Name]**
3. **[Character 3 Name]]
...
```

**IF NO CHARACTERS FOUND:**
"❌ No character dossier found.

Please create characters first with the **Build Characters** workflow."
→ STOP workflow

### 2. Present Character Selection

"**👤 Character selection for audit**

I will verify the psychological coherence of a character in a specific chapter.

**Which character would you like to audit?**"

Present the list of available characters with numbers:
- **[1]** [Character Name] — [Brief role/description if available]
- **[2]** [Character Name] — [Brief role/description if available]
- ...

"**Enter the character number or the character name:**"

Wait for user input.

### 3. Validate Selection

**IF user entered a number:**
- Map to character from list
- Store `selectedCharacter` = full name
- Store `selectedCharacterSlug` = lowercase-with-dashes version

**IF user entered a name:**
- Search for matching dossier file
- IF FOUND: Store selection
- IF NOT FOUND: "Character not found. Please select from the list." → Return to step 2

**Store in session:**
```
selectedCharacter: "{character_name}"
selectedCharacterName: "{character_name}"
selectedCharacterSlug: "{character_slug}"
```

### 4. Load Character Dossier

"**Loading {selectedCharacterName}'s dossier...**"

Load the complete character dossier from:
`{charactersFolder}/{selectedCharacterSlug}-dossier.md`

Verify the dossier contains:
- ✅ Internal Contradictions section
- ✅ At least 5 contradictions listed
- ✅ Transformation Arc section
- ✅ Personality section

**IF DOSSIER INCOMPLETE:**
"⚠️ {selectedCharacterName}'s dossier is incomplete.

Missing sections: [list]

Please complete the dossier with the **Build Characters** workflow before proceeding with the audit."
→ STOP workflow

### 5. Display Character Summary

"**Selected character: {selectedCharacterName}**

**Identified contradictions:** [N] contradictions
1. [Contradiction 1]
2. [Contradiction 2]
3. [Contradiction 3]
4. [Contradiction 4]
5. [Contradiction 5]
[N+如有更多]

**Current arc phase:** [X]/5
[One-line description of where they are in their arc]

**Ready for the chapter audit.**"

### 6. Present Continuation Menu

"**Selection validated.**

**[C]** Continue — Select the chapter to audit
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
- MUST store selectedCharacter variables before loading next step

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Character dossier discovered and loaded
- At least 5 contradictions present in dossier
- Arc section present
- Character selected and stored in session
- User confirms to proceed

### SYSTEM FAILURE:

- No character dossiers found
- Selected character dossier incomplete (missing contradictions or arc)
- User cancels selection

**Master Rule:** Cannot audit a character without a complete dossier with at least 5 contradictions. This is the foundation of psychological consistency checking.
