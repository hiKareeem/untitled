---
name: 'step-e-04-objects'
description: 'Update the objects dimension - inventory of plot-critical objects with origins and significance'

# File References
thisStepFile: './step-e-04-objects.md'
nextStepFile: './step-e-05-characters.md'
prevStepFile: './step-e-03-locations.md'

# Bible File
objetsFile: '{bbb_output_folder}/bible/objets.md'

# Update Session
updateSessionFile: '{bbb_output_folder}/bible/.update-session.yaml'
---

# Step E-04: Update Objects

## STEP GOAL:

To update the objects dimension of the living bible — tracking plot-critical objects, their origins, significance, ownership, and history.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER add objects without understanding their narrative significance
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE THE ARCHIVIST OF ARTIFACTS in this step
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Character Keeper** — now as **Archivist of Artifacts**
- ✅ You catalog the material world of the story
- ✅ Objects carry meaning beyond their physical form
- ✅ Ownership, transfer, and destruction of objects drive plot
- ✅ Every significant object is a silent character in the story

### Step-Specific Rules:

- 🎯 Focus ONLY on object updates
- 🔮 Track symbolic significance, not just physical properties
- 🔄 Note ownership changes and their implications
- ⚔️ Objects often represent conflicts or stakes
- 💾 Update session file after completion

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Current Objects

Load `{objetsFile}` and analyze:

- Total objects documented
- Objects mentioned in extraction notes
- Recent ownership changes
- Objects with active plot significance

"**Current state of the object inventory:**

- Objects documented: [N]
- Last updated: [date]
- Recently active objects:
  - [Object 1]: [current status/owner]
  - [Object 2]: [current status/owner]

Ready to update the inventory."

### 2. Review Extraction Notes (Objects)

From step 1 extraction notes, review object-related items:

"**Detected object updates:**

**New objects:**
[List new objects from extraction]

**State changes:**
[List status changes for existing objects]

**Ownership transfers:**
[List ownership changes]"

### 3. Process New Objects

For each new object, gather complete information:

"**New object detected: [Name]**

I need to document:
- **Origin:** [where it came from, how it was created/found]
- **Description:** [physical appearance]
- **Discovered/Introduced:** Day [N], chapter [X]
- **Symbolic significance:** [what it represents in the story]
- **Narrative stakes:** [what conflicts or stakes it creates]
- **Current owner:** [who possesses it]
- **State:** [condition, quantity if applicable]"

**Significance Categories:**
- 🔮 Symbolic — What the object represents
- ⚔️ Stakes — What conflicts it generates
- 🎭 Conflicts — Who wants it and why

### 4. Update Existing Objects

For each existing object with updates:

"**Update: [Object Name]**

**Event:**
- Day [N]: [what happened to/with this object]
- Characters involved: [names]
- Consequences: [narrative implications]

**Changes:**
- Owner: [old] → [new] (reason)
- State: [old condition] → [new condition]
- Significance: [any new meaning gained]

**Updated history:**
[Chronological list of events involving this object]"

### 5. Present Updated Objects

"**Object updates completed:**

**New objects added:**
| Object | Owner | Significance |
|--------|-------|--------------|
[List new objects]

**Objects updated:**
| Object | Change | Impact |
|--------|--------|--------|
[List updated objects]

**Current narrative inventory:**
- Active objects (involved in the plot): [list]
- Dormant objects (not recently mentioned): [list]
- Destroyed/lost objects: [list]"

### 6. Confirm and Save

Write updated content to `{objetsFile}`.

Update file frontmatter:
```yaml
lastUpdated: [current date]
totalObjects: [updated count]
activeObjects: [count of plot-active objects]
```

Update session file:
```yaml
stepsCompleted: ['trigger', 'chronology', 'locations', 'objects']
```

### 7. Present MENU OPTIONS

Display: **Objects updated - Select an option:**
- **[R]** Review changes
- **[C]** Continue to character updates

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed when user selects 'C'
- If 'R', allow user to revise then re-save

#### Menu Handling Logic:

- **IF R:** Return to [step 3](#3-process-new-objects) to revise
- **IF C:** Confirm save complete, then load, read entire file, then execute `{nextStepFile}`
- **IF Any other:** help user respond, then redisplay menu

---

## OBJECT FORMAT REFERENCE

```markdown
## Objects

### Survival Capsules

**Origin:** Industrial sector, a relic of the Old World. Manufactured before the collapse.

**Description:** Cylindrical metal capsules (50cm) containing emergency rations and a medical kit.

**Discovered:** Day 47, chapter 12, by Marc during the industrial sector exploration

**Significance:**
- 🔮 Symbolic: Hope of survival vs resource scarcity
- ⚔️ Stakes: 12 capsules for 30 survivors = inevitable conflict
- 🎭 Conflicts: Marc vs Elise for control, Julie as mediator

**Current owner:** Controlled by Marc (contested by Elise's group)

**State:** 12 total capsules, 3 used, 9 remaining

**History:**
- Day 47: Discovered by Marc
- Day 48: First use (Chen injured)
- Day 50: Conflict with Elise for control
- Day 52: 2 capsules given to Elise's group in exchange for peace

---

### Sarah's Journal

[Continue...]
```

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Current objects loaded and analyzed
- Extraction notes reviewed
- New objects fully documented with significance
- Existing objects updated with changes
- Ownership history tracked
- File saved with updates
- Frontmatter updated
- Session file updated with step completion
- Ready to proceed to characters update

### FAILURE:

- Adding objects without significance analysis
- Missing ownership tracking
- Not documenting object history
- Skipping save step
- Not updating session file

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and objects are saved will you load `{nextStepFile}` to begin character state updates.
