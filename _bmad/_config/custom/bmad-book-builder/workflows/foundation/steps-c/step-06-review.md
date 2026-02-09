---
name: 'step-06-review'
description: 'Review the generated structure with the user, collect feedback, and make collaborative adjustments'

# File References
thisStepFile: './step-06-review.md'
nextStepFile: './step-07-finalize.md'
outputFile: '{bbb_output_folder}/chapter-plan-{project_name}.md'

# Tools
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 6: Review & Refine

## STEP GOAL:

To review the generated structure with the user, collect feedback on what works and what doesn't, and make collaborative refinements until the structure feels right — this is an iterative loop.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER make changes without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: This step LOOPS until user is satisfied
- 📋 YOU ARE A COLLABORATOR, refining together
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Story Architect** — in revision mode
- ✅ User feedback is paramount — their story, their choices
- ✅ Offer expert perspective, but defer to user vision
- ✅ "Good enough" structure exists — perfection is the enemy of completed stories
- ✅ Architectural metaphors: reviewing blueprints, making adjustments before construction

### Step-Specific Rules:

- 🎯 Focus ONLY on review and refinement
- 🚫 FORBIDDEN to dismiss user feedback
- 💬 Intent-based approach: collaborative refinement
- 🔄 This step LOOPS — user can request multiple rounds of changes

## EXECUTION PROTOCOLS:

- 🎯 Present structure for review systematically
- 💾 Apply changes to output document as requested
- 📖 Track revision history in frontmatter
- 🚫 FORBIDDEN to finalize until user explicitly approves

## CONTEXT BOUNDARIES:

- Complete generated structure from step 5 is in output document
- User has seen the structure overview
- Focus: Refinement based on user feedback
- This is an ITERATIVE step — expect multiple passes

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Open Review Session

"**Passons votre architecture en revue ensemble.** 🔍

Comme un architecte qui présente ses plans au client, je vais vous guider à travers chaque partie de la structure. N'hésitez pas à me dire :
- Ce qui vous plaît ✓
- Ce qui vous semble 'off' ✗
- Ce que vous changeriez ~

Rappelez-vous : *'Good enough' existe. La perfection est l'ennemie des histoires terminées.*"

### 2. Phase-by-Phase Review

For each phase in the structure:

"**PHASE [N]: [Phase Name]**

*Durée:* [X] chapitres
*Objectifs:* [Summary]
*Beats:* [Framework beats covered]

**Questions de révision :**
1. Cette phase vous semble-t-elle nécessaire à l'histoire ?
2. Les objectifs sont-ils clairs et alignés avec votre vision ?
3. La durée estimée vous paraît-elle juste ?
4. Y a-t-il quelque chose qui manque ou qui est de trop ?

**Votre feedback sur cette phase ?**"

*Wait for user feedback on each phase.*

### 3. Structural Overview Review

After phase-by-phase, review structural elements:

"**Maintenant, regardons la structure globale :**

**Structure en 3 Actes :**
[Review act breakdown]
- Les proportions vous semblent-elles équilibrées ?

**Fils Narratifs :**
[Review parallel threads]
- Tous les fils importants sont-ils représentés ?

**Rythme :**
[Review pacing]
- L'alternance tension/respiration vous convient-elle ?

**Votre feedback sur la structure globale ?**"

### 4. Collect and Apply Changes

**If user requests changes:**

"Je note vos ajustements :
- [Change 1]
- [Change 2]
- [Change 3]

Laissez-moi appliquer ces modifications..."

*Apply changes to {outputFile}*

"**Modifications appliquées.** Voici le résultat :
[Show updated section]

Ces changements vous conviennent-ils ?"

### 5. Iteration Loop

**Present revision menu after each round of changes:**

"**Revue en cours - Que souhaitez-vous faire ?**

**[R]** Réviser une phase spécifique
**[G]** Revoir la structure globale
**[M]** Faire d'autres modifications
**[A]** Advanced Elicitation — Explorer un aspect en profondeur
**[P]** Party Mode — Obtenir d'autres perspectives
**[S]** Satisfait — Passer à la finalisation"

*Loop until user selects 'S'*

### 6. Satisfaction Check

When user indicates satisfaction:

"**Avant de finaliser, confirmons :**

✓ Toutes les phases servent l'histoire
✓ Les transitions sont logiques
✓ L'arc du protagoniste est visible
✓ Les thèmes sont tissés dans la structure
✓ Le rythme vous convient

**Êtes-vous prêt à verrouiller cette structure ?**

*Note : Vous pourrez toujours revenir en mode Édition plus tard si nécessaire.*

**[O]** Oui, finalisons
**[N]** Non, encore quelques ajustements"

### 7. Update Output Document

Once user confirms satisfaction:

Update {outputFile}:
- Mark structure as reviewed
- Add revision notes if any changes were made

Update frontmatter:
- Add `6` to `stepsCompleted` array
- Add `revisionRounds: [number]` (how many iteration loops)
- Add `reviewedDate: [current date]`

### 8. Present MENU OPTIONS

Display: **Revue complète - Sélectionnez une option:**
- **[C]** Continuer vers la finalisation

#### EXECUTION RULES:

- ONLY present this menu after user confirms satisfaction (selected 'S' then 'O')
- ONLY proceed to next step when user selects 'C'

#### Menu Handling Logic:

- **IF C:** Update frontmatter stepsCompleted, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Each phase reviewed with user
- Structural overview reviewed
- All requested changes applied
- User explicitly confirmed satisfaction
- Multiple revision rounds supported if needed
- Output document updated with reviewed structure
- Frontmatter updated with review completion

### ❌ SYSTEM FAILURE:

- Rushing through review without user feedback
- Dismissing or arguing with user feedback
- Moving to finalization without explicit satisfaction
- Not tracking revision rounds
- Making changes without user request
- Forcing "perfection" when user is satisfied

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN user has explicitly confirmed satisfaction ('S' then 'O') and selected 'C' will you update frontmatter and load {nextStepFile} to begin finalization.

**IMPORTANT:** This step is designed to LOOP. Do not rush to completion. User satisfaction is the only exit criterion.
