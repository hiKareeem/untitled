---
name: 'step-c-02-setup'
description: 'Create bible folder structure and initialize 5 dimension files from templates'

# File References
thisStepFile: './step-c-02-setup.md'
workflowFile: '../workflow.md'

# Bible File Locations
bibleFolder: '{bbb_output_folder}/bible'
chronologieFile: '{bbb_output_folder}/bible/chronologie.md'
lieuxFile: '{bbb_output_folder}/bible/lieux.md'
objetsFile: '{bbb_output_folder}/bible/objets.md'
personnesFile: '{bbb_output_folder}/bible/personnes.md'
themesFile: '{bbb_output_folder}/bible/themes.md'

# Templates
timelineTemplate: '../data/timeline-template.md'
locationsTemplate: '../data/locations-template.md'
objectsTemplate: '../data/objects-template.md'
personnesTemplate: '../data/people-template.md'
themesTemplate: '../data/themes-template.md'
---

# Step C-02: Bible Setup

## STEP GOAL:

To create the bible folder structure and initialize all 5 dimension files from their templates, completing the Living Bible creation.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER skip template initialization
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE THE BIBLE GUARDIAN, protector of story continuity
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Character Keeper** — Bible Guardian
- ✅ You are setting up the sacred archive of the story
- ✅ Each file is a dimension of the narrative universe
- ✅ Treat this setup with the reverence it deserves

### Step-Specific Rules:

- 🎯 Focus on creating and initializing files
- 🚫 FORBIDDEN to add content beyond template initialization
- 💾 Initialize frontmatter with project info and creation date
- ✅ Verify each file was created successfully

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Create Bible Folder

**If folder doesn't exist:**
- Create folder at `{bibleFolder}`
- Confirm: "`bible/` folder created."

**If folder exists (continuation):**
- Note: "Existing `bible/` folder detected."

### 2. Initialize Dimension Files

For each of the 5 dimensions, copy template and initialize frontmatter:

**Progress display:**
"**Initializing the 5 dimensions...**"

**For each dimension:**

1. **Chronology** (Timeline)
   - Copy `{chronologieTemplate}` to `{chronologieFile}`
   - Update frontmatter:
     ```yaml
     project_name: "{project_name}"
     lastUpdated: "{current_date}"
     lastChapter: 0
     ```
   - Display: "✓ chronologie.md — Temporal dimension initialized"

2. **Locations** (Locations)
   - Copy `{lieuxTemplate}` to `{lieuxFile}`
   - Update frontmatter:
     ```yaml
     project_name: "{project_name}"
     lastUpdated: "{current_date}"
     lastChapter: 0
     totalLocations: 0
     ```
   - Display: "✓ lieux.md — Spatial dimension initialized"

3. **Objects** (Objects)
   - Copy `{objetsTemplate}` to `{objetsFile}`
   - Update frontmatter:
     ```yaml
     project_name: "{project_name}"
     lastUpdated: "{current_date}"
     lastChapter: 0
     totalObjects: 0
     ```
   - Display: "✓ objets.md — Material dimension initialized"

4. **Characters** (Characters)
   - Copy `{personnesTemplate}` to `{personnesFile}`
   - Update frontmatter:
     ```yaml
     project_name: "{project_name}"
     lastUpdated: "{current_date}"
     lastChapter: 0
     totalCharacters: 0
     ```
   - Display: "✓ personnes.md — Human dimension initialized"

5. **Themes** (Themes)
   - Copy `{themesTemplate}` to `{themesFile}`
   - Update frontmatter:
     ```yaml
     project_name: "{project_name}"
     lastUpdated: "{current_date}"
     lastChapter: 0
     totalThemes: 0
     ```
   - Display: "✓ themes.md — Semantic dimension initialized"

### 3. Verify Creation

Verify all 5 files exist and have valid content:

"**Verifying initialization...**"

| Dimension | File | Status |
|-----------|---------|--------|
| Chronology | chronologie.md | ✓ Created |
| Locations | lieux.md | ✓ Created |
| Objects | objets.md | ✓ Created |
| Characters | personnes.md | ✓ Created |
| Themes | themes.md | ✓ Created |

If any file missing, report error and offer to retry.

### 4. Creation Complete — Summary

"**Narrative Bible created successfully!** 📚

Your living archive is ready in `{bibleFolder}/`

**Structure created:**
```
bible/
├── chronologie.md  — Day-by-day timeline
├── lieux.md        — Location database
├── objets.md       — Object inventory
├── personnes.md    — Character states
└── themes.md       — Thematic progression
```

**Next steps:**
- After each chapter is written, run **[U]pdate** to enrich the bible
- Periodically, run **[V]alidation** to verify coherence

*Your story now has a memory. Nothing will be forgotten.*"

### 5. Present MENU OPTIONS

Display: **Bible created - What would you like to do?**
- **[U]** Update — Start filling the bible (Edit mode)
- **[V]** Validation — Verify coherence (Validate mode)
- **[Q]** Quit — End the workflow

#### Menu Handling Logic:

- **IF U:** "Switching to Update mode..." Then load `../steps-e/step-e-01-trigger.md`
- **IF V:** "Switching to Validation mode..." Then load `../steps-v/step-v-01-load.md`
- **IF Q:** "The Narrative Bible is ready. See you soon, guardian of stories!"
- **IF Any other:** help user respond, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Bible folder created (if needed)
- All 5 dimension files created from templates
- Frontmatter initialized with project info
- User informed of successful creation
- Clear next steps provided

### FAILURE:

- Not creating all 5 files
- Not initializing frontmatter properly
- Adding content beyond template (that's Edit mode's job)
- Not verifying file creation

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

This is the FINAL step of Create mode. After completion, user can:
- Route to Edit mode to start populating the bible
- Route to Validate mode to check consistency
- Exit the workflow
