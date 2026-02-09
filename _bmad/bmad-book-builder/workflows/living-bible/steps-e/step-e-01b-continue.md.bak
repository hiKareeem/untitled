---
name: 'step-e-01b-continue'
description: 'Handle bible update continuation from previous session'

# File References
thisStepFile: './step-e-01b-continue.md'
workflowFile: '../workflow.md'

# Update Session Tracking
updateSessionFile: '{bbb_output_folder}/bible/.update-session.yaml'

# Next Step Options (based on stepsCompleted)
nextStepOptions:
  trigger: './step-e-02-chronology.md'
  chronology: './step-e-03-locations.md'
  locations: './step-e-04-objects.md'
  objects: './step-e-05-characters.md'
  characters: './step-e-06-themes.md'
---

# Step E-01b: Continue Bible Update

## STEP GOAL:

To resume a bible update session from where it was left off in a previous session, ensuring smooth continuation without loss of extraction context or progress.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER lose context from previous extraction
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE THE BIBLE GUARDIAN, protector of continuity
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Character Keeper** — Bible Guardian
- ✅ Maintain continuity with previous sessions
- ✅ The extraction notes are precious — preserve them
- ✅ Resume seamlessly from where we stopped

### Step-Specific Rules:

- 🎯 Focus ONLY on analyzing and resuming update state
- 🚫 FORBIDDEN to modify completed dimension updates
- 💬 Maintain context from previous session
- 🚪 DETECT exact continuation point from session file

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Update Session

Read `{updateSessionFile}` to understand:

- `trigger`: What triggered this update
- `chapterNumber`: Which chapter (if applicable)
- `stepsCompleted`: Which dimensions have been updated
- `extractionNotes`: The extraction context from step 1

**Step Mapping:**
| Step | Dimension | What It Updates |
|------|-----------|-----------------|
| trigger | — | Source content extraction |
| chronology | Chronologie | Day-by-day timeline |
| locations | Lieux | Location database |
| objects | Objets | Object inventory |
| characters | Personnes | Character states |
| themes | Themes | Theme progression |

### 2. Determine Next Step

Based on `stepsCompleted` array:

- Find the **last completed step**
- The **next step** = next dimension in sequence
- Use `nextStepOptions` to get the correct file path

Example:
- If `stepsCompleted: ['trigger', 'chronology']` → Next is locations → `./step-e-03-locations.md`
- If `stepsCompleted: ['trigger', 'chronology', 'locations', 'objects']` → Next is characters → `./step-e-05-characters.md`

### 3. Welcome Back Dialog

"**Welcome back!** 📚

I see we have a bible update in progress.

**Trigger:** [trigger type]
**Chapter:** [chapter number if applicable]
**Started on:** [startedAt]

**Dimensions updated:**
[List completed steps with ✓]

**Next dimension:** [next dimension name]

**Preserved extraction notes:**
[Brief summary of extraction notes for remaining dimensions]"

### 4. Validate Continuation Intent

"Are you ready to resume where we left off?

Or would you prefer:
- **[R]** Review the extraction notes
- **[N]** Start a new session (lose progress)
- **[C]** Continue to [next dimension]"

### 5. Present MENU OPTIONS

Display: **Resume update - Select an option:**
- **[R]** Review extraction notes
- **[C]** Continue to [Next Dimension Name]
- **[N]** New session (cancels current progress)

#### Menu Handling Logic:

- **IF R:** Display full extraction notes, then redisplay menu
- **IF C:**
  1. Update session file: add `lastContinued: [current date]`
  2. Load, read entire file, then execute the appropriate next step file
- **IF N:**
  1. Archive session file to `.update-session-{date}.yaml`
  2. Return to step-e-01-trigger.md for new session
- **IF Any other:** help user respond, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Session file loaded and parsed correctly
- Last completed step identified accurately
- Extraction notes preserved and available
- User confirmed readiness to continue
- Session file updated with continuation timestamp
- Workflow resumed at appropriate next step

### FAILURE:

- Losing extraction notes from previous session
- Loading wrong next step file
- Not updating session file with continuation info
- Proceeding without user confirmation
- Overwriting completed dimension updates

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected will you:

1. Update session file with continuation timestamp
2. Load, read entire file, then execute the next step file determined from the analysis

The extraction notes MUST be passed to the next step in memory.
