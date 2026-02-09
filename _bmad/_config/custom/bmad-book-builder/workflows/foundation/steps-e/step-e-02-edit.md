---
name: 'step-e-02-edit'
description: 'Apply requested edits to the chapter plan collaboratively'

# File References
thisStepFile: './step-e-02-edit.md'
nextStepFile: './step-e-03-complete.md'
outputFile: '{bbb_output_folder}/chapter-plan-{project_name}.md'

# Framework Data (if framework change requested)
saveTheCatData: '../data/save-the-cat.md'
herosJourneyData: '../data/heros-journey.md'
snowflakeMethodData: '../data/snowflake-method.md'
customFrameworkData: '../data/custom-framework.md'
methodeVareilleData: '../data/vareille-method.md'

# Tools
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step E-02: Apply Edits

## STEP GOAL:

To apply the confirmed edit list to the chapter plan, working through each modification collaboratively and ensuring the user approves each change.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER make changes without user confirmation
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: Apply one edit at a time, confirm each
- 📋 YOU ARE A COLLABORATIVE EDITOR
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Story Architect** — in renovation mode
- ✅ Each edit requires user approval before applying
- ✅ Show before/after for significant changes
- ✅ Maintain structural integrity throughout edits

### Step-Specific Rules:

- 🎯 Focus ONLY on applying the confirmed edit list
- 🚫 FORBIDDEN to add unconfirmed edits
- 💬 Collaborative approach: propose, confirm, apply
- 🔄 One edit at a time with confirmation

## EXECUTION PROTOCOLS:

- 🎯 Work through edit list systematically
- 💾 Apply changes to {outputFile} after each confirmation
- 📖 Track which edits are complete
- 🚫 FORBIDDEN to batch changes without individual approval

## CONTEXT BOUNDARIES:

- Edit list from step e-01 is in memory
- Chapter plan file is loaded
- Focus: Applying confirmed edits only

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Confirm Edit List

"**Prêt à appliquer les modifications.** ✏️

**Liste des modifications à effectuer :**
1. [Edit 1]
2. [Edit 2]
3. [Edit 3]
...

Je vais procéder modification par modification. Commençons."

### 2. Apply Each Edit (Loop)

For each edit in the list:

#### A. Show Current State

"**Modification [N]/[Total]: [Edit description]**

**État actuel :**
```
[Current content of section being edited]
```"

#### B. Propose Change

"**Modification proposée :**
```
[Proposed new content]
```

**Différences :**
- [What's changing]
- [Why this change makes sense]

**Approuvez-vous cette modification ?**
- **[O]** Oui, appliquer
- **[M]** Modifier la proposition
- **[S]** Sauter cette modification
- **[A]** Advanced Elicitation — Explorer cette modification"

#### C. Handle Response

**IF O (Approve):**
- Apply the change to {outputFile}
- "✓ Modification appliquée."
- Continue to next edit

**IF M (Modify):**
- "Comment souhaitez-vous modifier la proposition ?"
- Gather user's preferred change
- Present revised proposal
- Return to approval prompt

**IF S (Skip):**
- "Modification sautée."
- Note in edit tracking
- Continue to next edit

**IF A (Advanced Elicitation):**
- Execute {advancedElicitationTask}
- Return to proposal with insights

### 3. Handle Special Edit Types

**Phase Addition:**
- Ask where to insert (before/after which phase)
- Gather phase details (objectives, conflicts, beats)
- Generate phase structure
- Show how it fits in overall structure

**Phase Removal:**
- Show what will be removed
- Explain impact on surrounding phases
- Confirm transitions will still work

**Phase Reordering:**
- Show current order
- Ask for new order
- Show impact on transitions
- Regenerate transition text if needed

**Framework Change:**
- Load new framework data
- Explain how structure will be remapped
- Offer to regenerate phase structure or just relabel beats
- This is a significant change — extra confirmation needed

### 4. Edit Progress Tracking

After each edit, show progress:

"**Progression : [N]/[Total] modifications appliquées**

✓ [Edit 1 - applied]
✓ [Edit 2 - applied]
⏭ [Edit 3 - skipped]
⏳ [Edit 4 - pending]
..."

### 5. Complete All Edits

When all edits are processed:

"**Toutes les modifications ont été traitées !**

**Résumé :**
- ✓ [X] modifications appliquées
- ⏭ [Y] modifications sautées

Souhaitez-vous :
- **[R]** Revoir les modifications appliquées
- **[A]** Ajouter d'autres modifications
- **[C]** Continuer vers la finalisation"

### 6. Present MENU OPTIONS

Display: **Édition complète - Sélectionnez une option:**
- **[R]** Revoir les modifications
- **[A]** Ajouter d'autres modifications (retour à step e-01)
- **[P]** Party Mode — Obtenir des perspectives sur les changements
- **[C]** Continuer vers la complétion

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- Only proceed to next step when user selects 'C'

#### Menu Handling Logic:

- **IF R:** Display summary of all changes made, then redisplay menu
- **IF A:** Load `./step-e-01-assess.md` to add more edits
- **IF P:** Execute {partyModeWorkflow}, then redisplay menu
- **IF C:** Load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Each edit processed individually
- User approved each change before application
- Changes applied correctly to document
- Edit progress tracked throughout
- Skipped edits noted
- All edits processed before proceeding

### ❌ SYSTEM FAILURE:

- Applying changes without user approval
- Batching multiple changes without individual confirmation
- Missing edits from the confirmed list
- Breaking document structure during edits
- Not showing before/after for changes

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN all edits are processed and user selects 'C' will you load {nextStepFile} to complete the edit session.
