---
name: 'step-e-03-locations'
description: 'Update the locations dimension - location database with resources, events, and occupants'

# File References
thisStepFile: './step-e-03-locations.md'
nextStepFile: './step-e-04-objects.md'
prevStepFile: './step-e-02-chronology.md'

# Bible File
lieuxFile: '{bbb_output_folder}/bible/lieux.md'
---

# Step E-03: Update Locations

## STEP GOAL:

To update the locations dimension of the living bible — adding new locations, updating existing ones with new events, resources, and occupant changes.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- NEVER add locations without complete information
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE THE CARTOGRAPHER in this step
- YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- You are the **Character Keeper** — now focused on spatial continuity
- You map the story's world with precision
- Every location has history, resources, and significance
- Locations are characters too — they evolve with the story

### Step-Specific Rules:

- Focus ONLY on location updates
- Track what happens WHERE
- Note resource changes (depleted, discovered, contested)
- Track who controls/occupies each location

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Current Locations

Load `{lieuxFile}` and analyze:

- Total locations documented
- Recently updated locations
- Locations mentioned in extraction notes

"**Current state of the location database:**

- Locations documented: [N]
- Last updated: [date]
- Recently active locations:
  - [Location 1]: [last event]
  - [Location 2]: [last event]

Ready to update locations."

### 2. Review Extraction Notes (Locations)

From step 1 extraction notes, review location-related items:

"**Detected location updates:**

**New locations:**
[List new locations from extraction]

**Updates to existing locations:**
[List updates for existing locations]

**Events per location:**
[List events that occurred at each location]"

### 3. Process New Locations

For each new location, gather complete information:

"**New location detected: [Name]**

I need to document:
- Description: [physical description]
- Discovered: Day [N], by [character]
- Resources: [what can be found here]
- Dangers: [potential threats]
- Significance: [why this place matters to the story]
- Current state: [current condition]
- Controlled by: [who controls it, if anyone]"

Format and add to locations file.

### 4. Update Existing Locations

For each existing location with updates:

"**Update: [Location Name]**

**New event:**
- Day [N]: [event description]
- Characters involved: [names]
- Consequences: [what changed]

**State changes:**
- Resources: [added/depleted/contested]
- Control: [changed to/remained with]
- Condition: [improved/degraded/destroyed]"

### 5. Present Updated Locations

"**Location updates completed:**

**New locations added:**
[List with brief descriptions]

**Locations updated:**
[List with summary of changes]

**Current narrative map:**
- Active locations (recent scenes): [list]
- Dormant locations (no recent scenes): [list]
- Destroyed/inaccessible locations: [list]"

### 6. Confirm and Save

Write updated content to `{lieuxFile}`.

Update frontmatter:
```yaml
lastUpdated: [current date]
totalLocations: [updated count]
activeLocations: [count of recently used]
```

### 7. Present MENU OPTIONS

Display: **Locations updated - Select an option:**
- **[R]** Review changes
- **[C]** Continue to object updates

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed when user selects 'C'
- If 'R', allow user to revise then re-save

#### Menu Handling Logic:

- **IF R:** Return to [step 3](#3-process-new-locations) to revise
- **IF C:** Confirm save complete, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## LOCATION FORMAT REFERENCE

```markdown
## Locations

### Industrial Sector

**Description:** Vast zone of abandoned warehouses and factories, partially collapsed.

**Discovered:** Day 12, by Marc during a solo exploration

**Resources:**
- Tools (abundant)
- Building materials (moderate)
- Canned food (depleted since Day 35)

**Dangers:**
- Unstable structures
- Wild dogs (eliminated Day 20)

**Key events:**
- Day 12: First exploration by Marc
- Day 20: Confrontation with wild dogs
- Day 35: Food reserves exhausted
- Day 47: Discovery of survival capsules

**Significance:** Symbol of the old world, a source of conflict over resources

**Current state:** Partially secured, exploration ongoing

**Controlled by:** Marc's group (since Day 25)

---

### Fontaine Centrale

[Continue...]
```

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Current locations loaded and analyzed
- Extraction notes reviewed
- New locations fully documented
- Existing locations updated with new events
- File saved with updates
- Frontmatter updated
- Ready to proceed to objects update

### FAILURE:

- Adding incomplete location entries
- Missing event documentation
- Not tracking resource/control changes
- Skipping save step

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and locations are saved will you load {nextStepFile} to begin object updates.
