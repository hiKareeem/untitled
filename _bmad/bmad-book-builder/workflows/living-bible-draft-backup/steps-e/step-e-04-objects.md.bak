---
name: 'step-e-04-objects'
description: 'Update the objects dimension - inventory of plot-critical objects with origins, significance, and current status'

# File References
thisStepFile: './step-e-04-objects.md'
nextStepFile: './step-e-05-characters.md'
prevStepFile: './step-e-03-locations.md'

# Bible File
objetsFile: '{bbb_output_folder}/bible/objets.md'
---

# Step E-04: Update Objects

## STEP GOAL:

To update the objects dimension of the living bible — tracking plot-critical objects, their origins, significance, ownership, and current status.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- NEVER track trivial objects — only plot-significant items
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE THE ARCHIVIST OF ARTIFACTS in this step
- YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- You are the **Character Keeper** — now focused on object continuity
- Objects carry meaning — they're symbols, plot devices, MacGuffins
- Every significant object has a story: origin, journey, destination
- Objects can create conflict, resolve tension, reveal character

### Step-Specific Rules:

- Focus ONLY on plot-significant objects
- Track ownership changes meticulously
- Note symbolic significance
- Ignore mundane items unless they become significant

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Current Objects

Load `{objetsFile}` and analyze:

- Total objects documented
- Object categories (weapons, documents, symbols, resources)
- Recent ownership changes

"**Current state of the object inventory:**

- Objects documented: [N]
- Last updated: [date]
- Categories:
  - Weapons/Tools: [count]
  - Documents/Information: [count]
  - Symbols/Relics: [count]
  - Critical resources: [count]

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

### 3. Evaluate Object Significance

For each potential new object, evaluate significance:

"**Significance evaluation: [Object Name]**

Key questions:
- Does this object influence the plot? [Yes/No]
- Does this object reveal something about a character? [Yes/No]
- Does this object create or resolve a conflict? [Yes/No]
- Does this object have symbolic value? [Yes/No]

**Verdict:** [Document / Trivial object to ignore]"

### 4. Process New Objects

For each significant new object:

"**New object: [Name]**

**Origin:**
- Origin: [where it comes from]
- Discovered/Created: Day [N], by [character]
- Circumstances: [how it was found/made]

**Description:**
- Appearance: [physical description]
- Function: [what it does]
- State: [condition]

**Significance:**
- Symbolic: [what it represents]
- Stakes: [why it matters to the plot]
- Potential conflicts: [who wants it, why]

**Current owner:** [character name]

**History:**
- Day [N]: [First mention/discovery]"

### 5. Update Existing Objects

For each existing object with updates:

"**Update: [Object Name]**

**State change:**
- Previous state: [previous]
- New state: [current]
- Cause: [what happened]

**Ownership transfer:**
- Previous owner: [character]
- New owner: [character]
- Circumstances: [how it changed hands]

**New event:**
- Day [N]: [event involving the object]"

### 6. Present Updated Objects

"**Inventory updates completed:**

**New objects added:**
[List with significance summary]

**Objects updated:**
[List with summary of changes]

**Current inventory state:**
- Active objects (in play): [list]
- Lost/destroyed objects: [list]
- Pending objects (mentioned but not yet used): [list]"

### 7. Confirm and Save

Write updated content to `{objetsFile}`.

Update frontmatter:
```yaml
lastUpdated: [current date]
totalObjects: [updated count]
activeObjects: [count currently in play]
```

### 8. Present MENU OPTIONS

Display: **Objects updated - Select an option:**
- **[R]** Review changes
- **[C]** Continue to character updates

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed when user selects 'C'
- If 'R', allow user to revise then re-save

#### Menu Handling Logic:

- **IF R:** Return to [step 4](#4-process-new-objects) to revise
- **IF C:** Confirm save complete, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## OBJECT FORMAT REFERENCE

```markdown
## Objects

### Survival Capsules

**Origin:**
- Origin: Industrial sector, relic of the Old World
- Discovered: Day 47, by Marc
- Circumstances: Found in a sealed bunker

**Description:**
- Appearance: 30cm metal cylinders, seal intact
- Function: Emergency nutrition for 3 days per capsule
- State: 9 intact, 3 used

**Significance:**
- Symbolic: Hope of survival vs limited resource
- Stakes: Who decides their distribution?
- Potential conflicts: Tension between Marc and Elise over control

**Current owner:** Controlled by Marc's group (stored at HQ)

**History:**
- Day 47: Discovered by Marc (12 capsules)
- Day 48: First use (Julie, injury)
- Day 52: Second use (Chen, illness)
- Day 55: Third use (refugee child)
- Day 58: Tension — Elise requests redistribution

---

### Old World Journal

[Continue...]
```

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Current objects loaded and analyzed
- Extraction notes reviewed
- New objects evaluated for significance
- Significant objects fully documented
- Existing objects updated
- File saved with updates
- Ready to proceed to character states update

### FAILURE:

- Tracking trivial objects
- Missing ownership/provenance information
- Incomplete significance assessment
- Not tracking ownership changes

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and objects are saved will you load {nextStepFile} to begin character state updates.
