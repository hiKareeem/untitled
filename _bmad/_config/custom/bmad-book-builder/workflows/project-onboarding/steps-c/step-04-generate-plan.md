---
name: 'step-04-generate-plan'
description: 'Generate detailed migration plan document with step-by-step instructions'

# File references (ONLY variables used in this step)
nextStepFile: './step-05-review.md'
outputFile: '{bbb_output_folder}/bbb-onboarding-plan-{project_name}.md'
migrationPlanTemplate: './data/migration-plan-template.md'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 4: Generate Migration Plan

## STEP GOAL:

Create a comprehensive migration plan document that shows the before/after structure, detailed steps, risks, and timeline for the migration.

## MANDATORY EXECUTION RULES:
### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:
- ✅ You are a Migration Specialist — thorough and clear
- ✅ Create actionable, detailed plans
- ✅ Think about safety and rollback
- ✅ Be transparent about risks

### Step-Specific Rules:
- 🎯 Focus on clear, actionable documentation
- 📋 Use the migration plan template
- 💬 Make the plan comprehensive yet readable
- ⚠️ Include honest risk assessment

## EXECUTION PROTOCOLS:
- 🎯 Generate complete migration plan document
- 💾 Overwrite {outputFile} with complete plan
- 📖 Include all sections from template
- 🚫 This is collaborative — present for review

## CONTEXT BOUNDARIES:
- Available: Content detection + mapping from steps 2-3
- Focus: Documentation and planning
- Limits: Plan creation only, no execution
- Dependencies: Requires detection and mapping data

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load All Previous Data

Gather from steps 1-3:
- `project_path`, `project_name`, `project_basename`
- Detected content inventory
- Structure mapping

### 2. Generate Complete Migration Plan

Load {migrationPlanTemplate} and fill in all sections:

**Fill template variables:**
```yaml
---
title: "BBB Migration Plan: {project_name}"
generated: "{current_date}"
project_path: "{project_path}"
author: "{user_name}"
status: "PENDING APPROVAL"
---
```

**Fill all sections:**
1. Executive Summary — What this migration does
2. Detected Content — Everything found in analysis
3. Migration Strategy — HYBRID mode explanation
4. Before/After Structure — Visual comparison
5. Migration Steps — Detailed step-by-step
6. Risks and Warnings — Honest assessment
7. Approval Required — Clear call to action

### 3. Calculate Estimates

**Estimate:**
- Chapter count → Processing time
- Character count → Conversion time
- Complexity level → Overall estimate

**Time estimates:**
- Simple: 15-30 minutes
- Medium: 30-60 minutes
- Complex: 60-90 minutes

### 4. Save Complete Plan

Overwrite {outputFile} with the complete migration plan.

### 5. Display Plan and Menu

```markdown
**✅ Plan de migration généré !**

**Document créé :** {outputFile}

**Contenu du plan :**
- Résumé exécutif
- Contenu détecté ({chapters} chapitres, {characters} personnages)
- Structure avant/après
- Étapes de migration détaillées
- Risques et avertissements
- Estimation du temps : {estimated_time}

---

**Prêt pour la revue ?**

Tapez [C] pour continuer vers la revue du plan.
```

### 6. Present MENU OPTIONS

Display: "**Select :** [P] Party Mode — Débattre le plan avec plusieurs perspectives **[C]** Continuer vers la revue"

#### EXECUTION RULES:
- ALWAYS halt and wait for user input
- ONLY proceed to next step when user selects 'C'

#### Menu Handling Logic:
- IF P: Execute {partyModeWorkflow}, and when finished redisplay menu
- IF C: Load, read entire file, then execute {nextStepFile}
- IF Any other: help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- Complete migration plan generated
- All template sections filled
- Honest risk assessment included
- Time estimates provided
- User can review before proceeding

### ❌ SYSTEM FAILURE:
- Incomplete plan document
- Missing sections from template
- Not including risk assessment
- No time estimates

**Master Rule:** The migration plan is the author's safety net. It must be complete, honest, and actionable.
