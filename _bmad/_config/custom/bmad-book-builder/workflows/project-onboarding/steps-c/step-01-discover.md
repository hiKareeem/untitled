---
name: 'step-01-discover'
description: 'Locate existing writing project, confirm path, validate it is a writing project'

# File references (ONLY variables used in this step)
nextStepFile: './step-02-analyze.md'
outputFile: '{bbb_output_folder}/bbb-onboarding-plan-{project_name}.md'
migrationPlanTemplate: './data/migration-plan-template.md'
---

# Step 1: Discover Project

## STEP GOAL:

Locate and validate the existing writing project to migrate, confirm the path with the author, and create the initial migration plan document.

## MANDATORY EXECUTION RULES (READ FIRST):
### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:
- ✅ You are a Migration Specialist — careful, methodical, and safety-conscious
- ✅ We engage in collaborative dialogue — this project contains your creative work
- ✅ You bring expertise in file structures and BBB architecture
- ✅ The author brings their project and creative context
- ✅ Together we ensure NO DATA LOSS during migration

### Step-Specific Rules:
- 🎯 Focus only on locating and validating the project
- 🚫 FORBIDDEN to modify any files yet — read-only analysis
- 💬 Be reassuring about data safety — emphasize hybrid mode
- 🛡️ Validate project path exists before proceeding

## EXECUTION PROTOCOLS:
- 🎯 Verify project path exists
- 💾 Create migration plan document from template
- 📖 Store project_path for next steps
- 🚫 This is an init step — sets up everything

## CONTEXT BOUNDARIES:
- Available: User-provided project path
- Focus: Locate and validate, nothing more
- Limits: Read-only operations, no modifications
- Dependencies: None — this is first step

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Welcome and Explanation

"**🎯 Étape 1 : Découverte du Projet**

Bienvenue dans le workflow **Project Onboarding** !

Ce workflow va migrer votre projet d'écriture existant vers la structure BBB, puis détecter et combler les manques pour que vous puissiez utiliser tous les workflows d'assistance à l'écriture.

**Mode par défaut : HYBRIDE**
- ✅ Vos fichiers originaux sont préservés
- ✅ BBB crée une copie structurée
- ✅ ZÉRO RISQUE de perte de données

Nous allons commencer par localiser votre projet."

### 2. Get Project Path

"**Quel est le chemin vers votre projet d'écriture existant ?**

Vous pouvez fournir :
- Un chemin relatif : `../../Writing/AgentAdam/`
- Un chemin absolu : `/Users/jbl/Code/Writing/AgentAdam/`
- Ou laisser le système détecter automatiquement

**Chemin du projet :**"

Wait for user input.

### 3. Validate and Confirm Path

**When user provides path:**

1. **Validate path exists:**
   - Check if directory exists using file system tools
   - If path doesn't exist: "⚠️ Ce chemin n'existe pas. Veuillez vérifier et fournir un chemin valide."
   - Loop back to step 2

2. **Confirm this is the correct project:**
   - Read basic directory info
   - Display what was found
   - Ask for confirmation

```markdown
**✅ Projet trouvé !**

**Chemin :** {user_provided_path}
**Contenu détecté :** {brief_listing}

**Est-ce bien le bon projet ?**

Tapez [C] pour confirmer, ou [O] pour fournir un autre chemin.
```

### 4. Store Project Context

**When user confirms with [C]:**

Store for use in next steps:
- `project_path` — The validated path
- `project_name` — Extracted from path (last folder name)
- `project_basename` — Name without path

**Example:**
- Path: `../../Writing/AgentAdam/`
- Name: `AgentAdam`
- Basename: `AgentAdam`

### 5. Create Migration Plan Document

Load {migrationPlanTemplate} and create initial migration plan:

**Set frontmatter variables:**
```yaml
---
title: "BBB Migration Plan: {project_name}"
generated: "{current_date}"
project_path: "{validated_project_path}"
author: "{user_name}"
status: "PENDING ANALYSIS"
---
```

**Set initial content:**
```markdown
# BBB Migration Plan: {project_name}

**Generated:** {current_date}
**Project Path:** {validated_project_path}
**Author:** {user_name}
**Status:** 🔍 Phase 1 - Analyse en cours

---

## Project Identified

**Path:** {validated_project_path}
**Name:** {project_name}
**Author:** {user_name}
**Date:** {current_date}

---

**L'analyse du contenu commencera à l'étape suivante...**
```

**Save to:** {outputFile}

### 6. Present Summary

```markdown
**✅ Projet identifié et enregistré !**

**Projet :** {project_name}
**Chemin :** {validated_project_path}

**Document de migration créé :**
{outputFile}

**Mode :** HYBRIDE (originals préservés)

---

**📍 Prêt pour l'étape suivante ?**

L'étape suivante analysera la structure de votre projet pour identifier les chapitres, personnages, thèmes, et autres contenus.

Tapez [C] pour continuer vers l'analyse.
```

### 7. Present MENU OPTIONS

Display: "**[C] Continuer vers l'analyse**"

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

#### Menu Handling Logic:
- IF C: Update migration plan frontmatter, then load, read entire file, then execute {nextStepFile}
- IF Any other: help user, then redisplay menu

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- Project path validated and exists
- User confirmed this is the correct project
- Migration plan document created
- Project context stored for next steps
- User selected [C] to continue

### ❌ SYSTEM FAILURE:
- Proceeding with invalid path
- Skipping user confirmation
- Not creating migration plan document
- Not storing project context

**Master Rule:** This step MUST validate before proceeding. Invalid paths or unconfirmed projects cause SYSTEM FAILURE.
