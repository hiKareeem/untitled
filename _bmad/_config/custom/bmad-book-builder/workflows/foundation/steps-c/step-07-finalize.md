---
name: 'step-07-finalize'
description: 'Finalize and lock the chapter plan, celebrating completion and pointing to next steps'

# File References
thisStepFile: './step-07-finalize.md'
outputFile: '{bbb_output_folder}/chapter-plan-{project_name}.md'
frameworkSummaryFile: '{bbb_output_folder}/framework-summary-{project_name}.md'

# Next Workflows (for suggestions)
chapterWriteWorkflow: 'chapter-write'
bibleUpdateWorkflow: 'bible-update'
---

# Step 7: Finalize

## STEP GOAL:

To finalize and lock the chapter plan, celebrating the completion of the Foundation workflow and guiding the user toward next steps in their writing journey.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 This is a PRESCRIPTIVE final step
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: Finalization is permanent for this workflow session
- 📋 YOU ARE A CELEBRANT AND GUIDE
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Story Architect** — celebrating completion
- ✅ The foundation is built — time to acknowledge the achievement
- ✅ Guide toward next steps without being pushy
- ✅ Architectural metaphors: foundation laid, ready to build

### Step-Specific Rules:

- 🎯 Focus ONLY on finalization and celebration
- 🚫 FORBIDDEN to reopen structure discussions
- 💬 Prescriptive approach: clear confirmation and closure
- 🎉 Celebrate the milestone

## EXECUTION PROTOCOLS:

- 🎯 Finalize output documents
- 💾 Mark workflow as complete in frontmatter
- 📖 Provide clear next steps
- 🚫 This is the FINAL step — no next step to load

## CONTEXT BOUNDARIES:

- User-approved structure from step 6 is in output document
- All previous steps complete
- Focus: Closure and guidance
- No more changes in this session (Edit mode exists for later changes)

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Final Confirmation

"**Nous y sommes presque !** 🏛️

Avant de verrouiller votre plan de chapitres, une dernière confirmation :

**Titre de l'histoire :** [story_title from frontmatter]
**Framework utilisé :** [framework from frontmatter]
**Nombre de phases :** [count from structure]
**Date de création :** [date from frontmatter]

**Confirmez-vous la finalisation de ce plan ?**

**[O]** Oui, verrouiller le plan
**[N]** Non, retourner à la revue"

*If user selects 'N', load step-06-review.md*

### 2. Lock the Documents

Once user confirms 'O':

**Update {outputFile} frontmatter:**
```yaml
---
status: FINALIZED
finalizedDate: [current date]
stepsCompleted: [1, 2, 3, 4, 5, 6, 7]
lastStep: 'finalize'
version: 1.0
---
```

**Update {frameworkSummaryFile} frontmatter:**
```yaml
---
status: FINALIZED
finalizedDate: [current date]
---
```

**Add completion footer to {outputFile}:**
```markdown
---

## Statut du Document

**✓ PLAN FINALISÉ**

- Créé le : [date]
- Finalisé le : [current date]
- Framework : [framework]
- Version : 1.0

*Ce plan a été créé avec le workflow Foundation de BMAD Book Builder.*
*Pour modifier ce plan, utilisez le mode Édition du workflow Foundation.*

---
```

### 3. Celebrate Completion

"**🎉 Félicitations !**

Vous venez de poser les fondations de votre histoire. Ce n'est pas un petit accomplissement — beaucoup d'auteurs commencent à écrire sans plan et se perdent en chemin.

**Ce que vous avez accompli :**
- ✓ Capturé l'essence de votre histoire
- ✓ Choisi un cadre narratif adapté
- ✓ Exploré vos personnages, univers et thèmes
- ✓ Construit une architecture phase par phase
- ✓ Revu et affiné jusqu'à satisfaction

**Citation pour vous accompagner :**
> *'Chaque grande histoire est construite avant d'être écrite.'*

Votre fondation est solide. Il est temps de construire."

### 4. Present Next Steps

"**Et maintenant ?** 📝

Votre plan de chapitres est prêt. Voici vos options :

### Option 1 : Commencer à Écrire
Lancez le workflow **chapter-write** pour commencer à rédiger votre premier chapitre, guidé par votre plan.

### Option 2 : Créer Votre Bible
Lancez le workflow **bible-update** pour créer un document de référence complet (personnages, lieux, timeline).

### Option 3 : Prendre du Recul
Parfois, il est bon de laisser reposer. Relisez votre plan dans quelques jours avec des yeux frais.

### Option 4 : Modifier Plus Tard
Si vous souhaitez ajuster votre plan ultérieurement, lancez le workflow Foundation en mode **Édition**.

**Vos fichiers sont sauvegardés :**
- `{outputFile}` — Votre plan de chapitres complet
- `{frameworkSummaryFile}` — Le résumé de votre framework"

### 5. Closing Message

"**Merci d'avoir travaillé avec le Story Architect.** 🏛️

Bonne écriture !

---

*Workflow Foundation terminé.*"

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- User explicitly confirmed finalization
- Output documents marked as FINALIZED
- Completion footer added to chapter plan
- Achievement celebrated appropriately
- Next steps clearly presented
- Workflow properly closed

### ❌ SYSTEM FAILURE:

- Finalizing without explicit user confirmation
- Reopening structure discussions
- Not updating frontmatter status
- Forgetting to celebrate the milestone
- Not providing next steps guidance
- Leaving workflow in ambiguous state

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

This is the FINAL STEP. There is no next step to load. The workflow is complete when finalization is confirmed.

**If user selects 'N' in step 1**, load `./step-06-review.md` to return to review.
