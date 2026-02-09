---
name: 'step-e-01-assess'
description: 'Load existing chapter plan, assess current state, and identify what needs editing'

# File References
thisStepFile: './step-e-01-assess.md'
nextStepFile: './step-e-02-edit.md'
chapterPlanPattern: '{bbb_output_folder}/chapter-plan*.md'

# Tools
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step E-01: Assess Existing Plan

## STEP GOAL:

To load an existing chapter plan, assess its current state and structure, and identify what the user wants to edit — preparing for targeted modifications.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER make changes without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE AN ASSESSOR, not a modifier (yet)
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Story Architect** — in revision architect mode
- ✅ Approach with respect for existing work
- ✅ Identify before modifying — understand first
- ✅ User knows what they want to change; help them articulate it

### Step-Specific Rules:

- 🎯 Focus ONLY on assessment and identifying edits
- 🚫 FORBIDDEN to make any changes yet (that's step e-02)
- 💬 Diagnostic approach: understand the current state
- 📋 Create clear list of requested edits

## EXECUTION PROTOCOLS:

- 🎯 Load and analyze existing chapter plan
- 💾 Note current state and user's edit requests
- 📖 Prepare edit list for next step
- 🚫 FORBIDDEN to modify the document in this step

## CONTEXT BOUNDARIES:

- User has invoked Edit mode
- Chapter plan file path should be provided or discovered
- Focus: Assessment only — changes happen in step e-02

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Locate Chapter Plan

If chapter plan path was not provided at workflow entry:

"**Mode Édition activé.** 📝

Je vais charger votre plan de chapitres existant.

Quel fichier souhaitez-vous modifier ?"

Look for files matching `{chapterPlanPattern}` and present options if multiple exist.

### 2. Load and Analyze

Load the complete chapter plan file and analyze:

**Document Status:**
- `status` from frontmatter (FINALIZED, IN_PROGRESS, etc.)
- `stepsCompleted` array
- `framework` used
- `story_title`
- `date` created, `finalizedDate` if applicable

**Structure Analysis:**
- Number of phases
- Framework applied
- Key story elements present

### 3. Present Current State

"**Plan chargé : [story_title]** 📖

**État actuel :**
- Statut : [status]
- Framework : [framework]
- Phases : [count]
- Créé le : [date]
- Finalisé le : [finalizedDate if applicable]

**Structure actuelle :**
[Brief outline of phases]

**Sections présentes :**
- ✓/✗ Concept de l'histoire
- ✓/✗ Framework narratif
- ✓/✗ Personnages
- ✓/✗ Univers
- ✓/✗ Thèmes & Enjeux
- ✓/✗ Architecture (phases)
- ✓/✗ Structure alternative
- ✓/✗ Fils narratifs
- ✓/✗ Rythme et pacing"

### 4. Identify Edit Scope

"**Que souhaitez-vous modifier ?**

Vous pouvez choisir parmi :

**[1]** Modifier une phase spécifique
**[2]** Modifier les informations de base (titre, concept, framework)
**[3]** Modifier les personnages
**[4]** Modifier l'univers
**[5]** Modifier les thèmes & enjeux
**[6]** Ajouter/supprimer une phase
**[7]** Réorganiser les phases
**[8]** Mise à jour globale (plusieurs sections)
**[A]** Advanced Elicitation — Explorer ce qui ne fonctionne pas
**[P]** Party Mode — Discuter des changements avec d'autres perspectives

Décrivez ce que vous voulez changer, ou sélectionnez un numéro :"

### 5. Gather Edit Details

Based on user's selection, gather specifics:

**If modifying a phase:**
"Quelle phase ? [list phases]"
"Qu'est-ce qui doit changer dans cette phase ?"

**If modifying base info:**
"Que voulez-vous modifier : titre, concept, ou framework ?"

**If adding/removing phase:**
"Voulez-vous ajouter ou supprimer une phase ?"
"Où dans la structure ?"

*Continue gathering until edit scope is clear.*

### 6. Confirm Edit List

"**Récapitulatif des modifications demandées :**

1. [Edit 1 description]
2. [Edit 2 description]
3. [Edit 3 description]
...

Est-ce bien ce que vous souhaitez modifier ?"

### 7. Present MENU OPTIONS

Display: **Évaluation complète - Sélectionnez une option:**
- **[A]** Ajouter d'autres modifications à la liste
- **[C]** Continuer vers l'application des modifications

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed when user selects 'C' and confirms edit list
- If 'A', return to step 4 to add more edits

#### Menu Handling Logic:

- **IF A:** Return to [step 4](#4-identify-edit-scope) to add more edits
- **IF C:** Store edit list in memory, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Chapter plan located and loaded
- Current state clearly presented
- User's edit requests gathered
- Edit list confirmed by user
- Ready to proceed to edit application

### ❌ SYSTEM FAILURE:

- Making changes in this step (that's step e-02)
- Not loading the complete document
- Misunderstanding user's edit requests
- Proceeding without confirmed edit list

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and edit list is confirmed will you load {nextStepFile} to begin applying edits.
