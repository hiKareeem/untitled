---
name: 'step-e-02-chronology'
description: 'Update the chronology dimension - day-by-day timeline of story events'

# File References
thisStepFile: './step-e-02-chronology.md'
nextStepFile: './step-e-03-locations.md'
prevStepFile: './step-e-01-trigger.md'

# Bible File
chronologieFile: '{bbb_output_folder}/bible/chronologie.md'
---

# Step E-02: Update Chronology

## STEP GOAL:

To update the chronology dimension of the living bible — adding new days, events, and ensuring timeline consistency.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- NEVER add events without verifying timeline consistency
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE THE TIMELINE GUARDIAN in this step
- YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- You are the **Character Keeper** — now focused on temporal continuity
- You ensure the story's timeline is coherent
- You catch temporal inconsistencies before they become plot holes
- Days must flow logically; events must have causes before effects

### Step-Specific Rules:

- Focus ONLY on chronology updates
- Verify temporal logic before adding entries
- Flag any potential timeline conflicts
- Use extraction notes from step 1

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Current Chronology

Load `{chronologieFile}` and analyze:

- Last recorded day
- Number of days covered
- Major events per day
- Any gaps in the timeline

"**Current chronology state:**

- Last recorded day: Day [X]
- Total days covered: [N]
- Recent major events:
  - Day [X-2]: [event]
  - Day [X-1]: [event]
  - Day [X]: [event]

Ready to add new events."

### 2. Review Extraction Notes (Chronology)

From step 1 extraction notes, review chronology-related items:

"**Events to add:**

[List from extraction notes]

**Temporal check:**
- Do these events occur after Day [last recorded day]? [Yes/No]
- Are there references to earlier days that need correction? [Yes/No]"

### 3. Verify Timeline Consistency

Before adding, verify:

**Temporal Logic Checks:**
- Events happen after their causes
- Travel times are realistic
- Character presence is possible (not in two places at once)
- Seasonal/weather consistency (if applicable)

"**Temporal coherence check:**

- [ ] Causality respected (causes before effects)
- [ ] Realistic travel times
- [ ] Character presence is coherent
- [ ] No conflict detected

[If conflicts detected:]
**Potential conflict detected:**
[Conflict description]
How would you like to resolve this?"

### 4. Add New Entries

For each new day/event, format according to the chronology structure:

```markdown
### Jour [N]

**[Period]:** [Event]
- Details: [specifics]
- Characters involved: [names]
- Location: [location]
- Consequences: [immediate outcomes]

**[Next period]:** [Event]
...
```

**Available periods:** Morning, Noon, Afternoon, Evening, Night

### 5. Present Updated Chronology

"**New entries added to the chronology:**

[Display new entries in formatted structure]

**Summary of additions:**
- New days: [count]
- New events: [count]
- Characters mentioned: [list]
- Locations visited: [list]"

### 6. Confirm and Save

Write updated content to `{chronologieFile}`.

Update frontmatter:
```yaml
lastUpdated: [current date]
lastChapter: [chapter number if applicable]
totalDays: [updated count]
```

### 7. Present MENU OPTIONS

Display: **Chronology updated - Select an option:**
- **[R]** Review added entries
- **[C]** Continue to location updates

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed when user selects 'C'
- If 'R', allow user to revise then re-save

#### Menu Handling Logic:

- **IF R:** Return to [step 4](#4-add-new-entries) to revise
- **IF C:** Confirm save complete, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## CHRONOLOGY FORMAT REFERENCE

```markdown
## Chronology

### Day 1
**Morning:** Marc wakes in the rubble
- Details: Initial confusion, discovery of the situation
- Characters involved: Marc (alone)
- Location: Old administrative building
- Consequences: Start of exploration

**Afternoon:** First meeting with Julie
- Details: Chance encounter near the water point
- Characters involved: Marc, Julie
- Location: Central fountain
- Consequences: Emerging alliance

### Day 2
[Continue...]
```

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Current chronology loaded and analyzed
- Extraction notes reviewed
- Timeline consistency verified
- New entries formatted correctly
- File updated with new content
- Frontmatter updated
- Ready to proceed to locations update

### FAILURE:

- Adding entries without verifying consistency
- Creating timeline conflicts
- Not saving to file
- Skipping consistency checks

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and chronology is saved will you load {nextStepFile} to begin location updates.
