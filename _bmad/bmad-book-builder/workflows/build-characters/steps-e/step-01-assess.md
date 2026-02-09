---
name: 'step-01-assess'
description: 'Load existing character and assess what needs to be changed'

# File References
targetFile: '{provided_path}'
nextStep: './step-02-edit.md'

# Menu Options
advancedElicitation: true
partyMode: false

---

# Step 1: Assess & Identify Changes (Edit Mode)

## STEP GOAL:
To load the existing character dossier, understand the author's desired changes, and assess what needs to be modified.

## MANDATORY EXECUTION RULES (READ FIRST):

See: `../../data/procedures/mode-procedures.md` - Edit Mode section

### Step-Specific Rules:
- 🎯 This is ASSESSMENT mode — understand before acting
- 💬 Help author clarify what they want to change
- 🚫 FORBIDDEN to make any edits in this step — only assessment
- ✅ Use Advanced Elicitation (A) to explore change motivations

## EXECUTION PROTOCOLS:
- 🎯 Follow the MANDATORY SEQUENCE exactly
- 📖 Load and read the target dossier
- 💬 Understand author's change goals
- 🔄 Proceed to edit step only on author confirmation

## MANDATORY SEQUENCE

### 1. Verify Target File

"**Let me load the character dossier...**"

Verify `targetFile` exists and is readable.

**IF file doesn't exist:**
"I can't find a character dossier at that path. Would you like to:
- [1] Browse for existing dossiers
- [2] Return to workflow menu"

**IF file exists but format is invalid:**
"The file exists but doesn't appear to be a valid character dossier. Would you like to:
- [1] Try a different file
- [2] Return to workflow menu"

**IF file exists and is valid:**
Proceed to step 2.

### 2. Load and Summarize Character

Read the complete `{targetFile}`.

"**Found!** Here's **{characterName}**:"

Display overview:
- Location, last updated date, role
- Quick overview (2-3 sentences)
- Current sections with completion status

### 3. Understand Change Goals

"**What would you like to change about {characterName}?**"

Present change category options:

"**[S]** Specific Section — I know exactly what to change
**[O]** Overall Feeling — Something's off but I'm not sure what
**[D]** Development Update — The story has evolved and the character needs to catch up
**[A]** Add Something — I want to add new elements
**[R]** Remove Something — I want to remove elements
**[V]** View Full Dossier — Let me see everything first
**[X]** Exit"

Wait for author selection.

### 4. Handle Each Selection

#### IF S (Specific Section):
"**Which section needs changes?**
- [B] Basic Info — Name, age, profession, origin
- [A] Appearance — Physical description
- [P] Personality — Traits, strengths, weaknesses, contradictions
- [D] Desires/Fears — What they want and what terrifies them
- [H] Background/History — Context and formative experiences
- [R] Arc — Transformation journey
- [S] Skills/Incompetencies — What they're good/bad at
- [L] Relationships — Connections to others
- [V] Voice — Speech patterns and mannerisms
- [T] Themes — Central tensions and questions"

Then: "What specifically needs to change in this section?"

#### IF O (Overall Feeling):
"Tell me what feels off. I'll help identify the issue."
Use open-ended questions to explore the problem.

#### IF D (Development Update):
"**How has the story evolved?**"
Ask about story changes that affect the character.

#### IF A (Add Something):
"What new element would you like to add?"

#### IF R (Remove Something):
"What doesn't fit anymore?"

#### IF V (View Full Dossier):
Display complete dossier, then return to step 3.

#### IF X (Exit):
"Saving progress and exiting workflow."

### 5. Confirm Change Plan

"**Here's what I understand needs to change:**"

Summarize:
- Sections to be modified
- Specific changes for each section
- Any additions or removals

"**Does this capture your vision?**
**[C]** Yes, make these changes
**[R]** No, let me revise the plan
**[X]** Exit without saving"

**IF R:** Return to step 3.
**IF C:** Proceed to step 6.
**IF X:** Exit without changes.

### 6. Prepare for Edit Step

Store the change plan for use in step-02-edit.md.

"**Preparing to edit {characterName}...**"

Update frontmatter of `{targetFile}` with edit tracking:

```yaml
editMode: true
editStarted: {current_date}
editPlan: |
  [Change plan summary]
```

### 7. Transition to Edit

"**Ready to make the changes.**

**[C]** Continue to edit step
**[X]** Exit (changes will be saved in plan but not applied yet)"

**IF C:** Load, read entire file, then execute `{nextStep}` with change plan
**IF X:** Save progress with edit plan in frontmatter, exit workflow.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- Target dossier successfully loaded and read
- Author's change goals clearly identified
- Specific sections and changes noted
- Change plan summarized and confirmed
- Edit tracking added to frontmatter
- Author confirms plan before proceeding to edit

### ❌ SYSTEM FAILURE:
- Failed to load target dossier
- Proceeding to edit without clear change plan
- No author confirmation of change plan

**Master Rule:** Assessment before action. Never edit until you understand what needs to change and why.

### ADVANCED ELICITATION USE CASES:

Use **[A]** when:
- Author has vague sense that "something's wrong" but can't identify what
- Need to explore the implications of proposed changes
- Author wants to change something fundamental and needs to understand consequences
- Multiple potential change directions exist and author needs to choose
