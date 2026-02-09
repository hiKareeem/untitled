---
name: 'step-05-review'
description: 'Present migration plan to author, allow adjustments, and obtain final approval'

# File references (ONLY variables used in this step)
nextStepFile: './step-06-execute.md'
outputFile: '{bbb_output_folder}/bbb-onboarding-plan-{project_name}.md'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
---

# Step 5: Review with Author

## STEP GOAL:

Present the migration plan to the author, allow questions and adjustments, and obtain explicit approval (PROCEED) or cancellation (ABORT) before execution.

## MANDATORY EXECUTION RULES:
### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:
- ✅ You are a Migration Specialist — careful and consultative
- ✅ This is a QUALITY GATE — execution depends on approval
- ✅ Be patient and thorough in explanations
- ✅ Author MUST understand before proceeding

### Step-Specific Rules:
- 🎯 Focus on understanding and consent
- 🚫 FORBIDDEN to proceed without explicit PROCEED
- 💬 Allow questions and adjustments
- ⚠️ This is the LAST CHANCE to abort safely

## EXECUTION PROTOCOLS:
- 🎯 Present plan clearly and completely
- 💾 Allow plan modifications if requested
- 📖 Obtain explicit PROCEED or ABORT
- 🚫 Only proceed with PROCEED confirmation

## CONTEXT BOUNDARIES:
- Available: Complete migration plan from step 4
- Focus: Author understanding and approval
- Limits: Review only, no execution
- Dependencies: Requires complete migration plan

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Migration Plan

Load {outputFile} completely to present to author.

### 2. Present Executive Summary

```markdown
**🎯 REVUE DU PLAN DE MIGRATION**

Bonjour {user_name} ! Voici le plan de migration pour votre projet **{project_name}**.

---

## Résumé

Votre projet contient :
- {chapters} chapitres
- {characters} personnages
- {other_content}

**La migration va :**
1. Créer la structure BBB dans votre projet
2. Copier vos chapitres avec frontmatter BBB (mode HYBRIDE)
3. Convertir vos personnages au format YAML BBB
4. Migrer vos thèmes et autres contenus

**Mode : HYBRIDE**
- ✅ Vos fichiers originaux sont PRÉSERVÉS
- ✅ BBB crée une copie structurée
- ✅ ZÉRO RISQUE de perte de données

**Estimation :** {estimated_time}
```

### 3. Present Before/After Structure

```markdown
## Structure Avant

{current_structure_tree}

## Structure Après (BBB)

{target_structure_tree}
```

See **BBB Folder Structure** reference for detailed layout:
`{workflow_root}/data/references/bbb-folder-structure.md`

### 4. Present Migration Steps

Present summary from migration plan:
- Step 1: Créer la structure BBB
- Step 2: Migrer les personnages
- Step 3: Migrer les chapitres
- Step 4: Migrer les thèmes et autres contenus

For detailed procedures, see **Migration Procedures** reference:
`{workflow_root}/data/references/migration-procedures.md`

### 5. Present Risks and Warnings

```markdown
## ⚠️ Risques et Avertissements

**Risque de perte de données : FAIBLE**
- Mode hybride = originals préservés
- Rollback possible

**Travail manuel requis : MOYEN**
- Certains attributs de personnages peuvent nécessiter ajustement
- Revoir le contenu migré pour précision

**Estimation du temps :** {estimated_time}
```

### 6. Offer Review Options

```markdown
---

## Options de Revue

**[A]** Advanced Elicitation — Explorer les implications plus profondément
**[P]** Party Mode — Débattre le plan avec plusieurs perspectives
**[M]** Modifier le plan — Proposer des changements
**[C]** Continuer — Approuver et exécuter la migration
**[X]** Annuler — Arrêter le workflow (pas de modifications)

**Votre choix ?**
```

### 7. Handle User Input

**IF A:** Execute {advancedElicitationTask}, then redisplay menu

**IF P:** Execute {partyModeWorkflow}, then redisplay menu

**IF M:** Allow user to propose changes
- Collect requested changes
- Discuss implications
- Update plan if appropriate
- Redisplay menu

**IF X:** Abort workflow
```markdown
**⚠️ WORKFLOW ANNULÉ**

Aucune modification n'a été faite à votre projet.

Merci d'avoir exploré BBB. Vous pouvez relancer ce workflow à tout moment.
```
END workflow

**IF C:** Obtain FINAL APPROVAL
```markdown
**⚠️ DERNIÈRE CONFIRMATION**

Vous allez approuver l'exécution de la migration.

Ce qui va se passer :
- ✅ Création des dossiers BBB
- ✅ Copie hybride de vos fichiers
- ✅ Conversion des personnages en YAML
- ✅ Ajout de frontmatter BBB aux chapitres

**VOS FICHIERS ORIGINAUX SERONT PRÉSERVÉS**

Tapez **PROCEED** pour confirmer et exécuter,
ou **ABORT** pour annuler.
```

Wait for explicit "PROCEED" confirmation.

**If PROCEED confirmed:**
- Update migration plan status to "APPROVED"
- Proceed to step 6

**If ABORT:**
- Return to menu above

### 8. Final Approval and Menu

**When PROCEED confirmed:**

Update {outputFile} frontmatter:
```yaml
status: "APPROVED FOR EXECUTION"
approvedDate: "{current_date}"
```

```markdown
**✅ PLAN APPROUVÉ**

La migration va maintenant être exécutée.

Tapez [C] pour commencer l'exécution.
```

### 9. Present MENU OPTIONS

Display: "**[C]** Exécuter la migration"

#### EXECUTION RULES:
- ALWAYS halt and wait for user input
- ONLY proceed to execution when user selects 'C'

#### Menu Handling Logic:
- IF C: Update plan status, then load, read entire file, then execute {nextStepFile}
- IF Any other: help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- Migration plan presented clearly
- Author had opportunity to review and ask questions
- Party mode and advanced elicitation available
- Explicit PROCEED confirmation obtained
- Plan status updated to APPROVED

### ❌ SYSTEM FAILURE:
- Proceeding without explicit approval
- Not offering review opportunities
- Skipping final confirmation step
- Not handling ABORT properly

**Master Rule:** This is the CRITICAL QUALITY GATE. NO execution happens without EXPLICIT user PROCEED confirmation.
