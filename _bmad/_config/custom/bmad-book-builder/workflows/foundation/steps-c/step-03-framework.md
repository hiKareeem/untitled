---
name: 'step-03-framework'
description: 'Select the narrative framework that best serves the story'

# File References
thisStepFile: './step-03-framework.md'
nextStepFile: './step-04-questions.md'
outputFile: '{bbb_output_folder}/chapter-plan-{project_name}.md'
frameworkSummaryFile: '{bbb_output_folder}/framework-summary-{project_name}.md'
frameworkSummaryTemplate: '../data/framework-summary-template.md'

# Framework Data Files
saveTheCatData: '../data/save-the-cat.md'
herosJourneyData: '../data/heros-journey.md'
snowflakeMethodData: '../data/snowflake-method.md'
customFrameworkData: '../data/custom-framework.md'
methodeVareilleData: '../data/vareille-method.md'
psychological5PhaseData: '../data/psychological-5-phase.md'

# Reference Documents
frameworkSelectionGuide: '../data/references/framework-selection-guide.md'

# Tools (optional)
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 3: Framework Selection

## STEP GOAL:

To guide the user in selecting the narrative framework that best serves their story — presenting options clearly, explaining trade-offs, and adapting the recommendation to their experience level and story type.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Story Architect** — a lead narrative designer
- ✅ Frameworks are analytical lenses, NOT prescriptive rules
- ✅ Adapt explanation depth to user expertise level
- ✅ For aspiring writers: educate about frameworks
- ✅ For experienced authors: collaborate as equals
- ✅ Use architectural metaphors (frameworks as blueprints, structure as skeleton)

### Step-Specific Rules:

- 🎯 Focus ONLY on framework selection
- 🚫 FORBIDDEN to start applying framework details yet (that's step 4)
- 💬 Prescriptive approach: structured selection process
- 🏗️ Emphasize that frameworks serve creativity, not the reverse

## EXECUTION PROTOCOLS:

- 🎯 Load and understand all framework options
- 💾 Record framework choice in output document
- 📖 Update frontmatter `stepsCompleted` to add 3 before loading next step
- 🚫 FORBIDDEN to load next step until framework is selected

## CONTEXT BOUNDARIES:

- Story concept from step 2 is available in output document
- All framework data files are available for reference
- Framework selection guide provides comprehensive framework information
- Focus: Framework selection only
- Dependencies: Step 2 (concept) must be complete

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Introduce Framework Concept

"**Maintenant que nous avons capturé l'essence de votre histoire**, choisissons un cadre narratif pour structurer votre récit.

Un framework n'est pas une prison — c'est une **lentille analytique** qui nous aide à voir la structure naturelle de votre histoire. Comme un architecte choisit un style (gothique, moderne, minimaliste) pour guider sa conception, nous allons choisir un cadre qui s'harmonise avec votre vision.

**Philosophie clé :** La structure sert la créativité, jamais l'inverse."

### 2. Present Framework Options

**IMPORTANT: Assess user expertise level FIRST and adapt presentation depth accordingly.**

Load {frameworkSelectionGuide} and present frameworks based on user experience level.

**For NEW writers (first novel, unfamiliar with frameworks):**

Present the three beginner-friendly frameworks from the guide:
- Save the Cat — Structure Hollywood
- Méthode Marie Vareille — Approche Pragmatique
- Structure 5 Phases Psychologiques — NOUVEAU

Provide option to see all frameworks: **[VOIR TOUS]** or **[ALL]**

Provide option to learn about frameworks: **[APPRENDRE]**

**For EXPERIENCED writers (familiar with narrative structure):**

Present all six frameworks with full details from the guide:
- Save the Cat (Blake Snyder)
- Voyage du Héros (Joseph Campbell)
- Méthode Snowflake (Randy Ingermanson)
- Méthode Marie Vareille
- Structure Personnalisée
- Structure 5 Phases Psychologiques (NOUVEAU — AgentAdam-Based)

**If user selects [APPRENDRE]:**

Load and present educational content from {frameworkSelectionGuide}:
- Why use a framework?
- Can I change my mind?
- Framework as architectural style

### 3. Make Personalized Recommendation

Based on the story concept from step 2 and the framework selection guide, provide a recommendation:

"**Pour votre histoire** — *[story title/logline reminder]* — **je recommanderais :**

**[Framework name]** parce que [specific reason based on their story and the guide's recommendations].

[If user seems new to frameworks:]
> 💡 *Si c'est votre premier roman, je vous conseille de commencer avec Save the Cat ou Marie Vareille — leurs structures claires vous guideront sans vous submerger.*

[If story has mythic/transformative elements:]
> 💡 *Votre récit a des éléments de transformation profonde qui s'alignent naturellement avec le Voyage du Héros.*

Cela dit, c'est **votre histoire** — choisissez ce qui résonne avec vous."

### 4. Capture Selection

**For NEW writers (simplified presentation):**

"**Quel framework vous attire ?** Tapez le numéro ou le nom :

**[1]** Save the Cat — Structure Hollywood simple
**[2]** Marie Vareille — Approche pragmatique française
**[3]** 5 Phases Psychologiques — Méthode innovante
**[VOIR TOUS]** ou **[ALL]** — Voir les 6 frameworks complets
**[APPRENDRE]** — En savoir plus sur les frameworks

**If user selects [VOIR TOUS] or [ALL]:**
Display the full 6-framework presentation from the guide, then return to selection prompt.

**For EXPERIENCED writers (full presentation):**

"**Quel framework souhaitez-vous utiliser ?**

**Options rapides :**
- Tapez **[1-6]** pour choisir directement
- Tapez **[détails X]** pour en savoir plus sur le framework X
- Tapez le **nom du framework** (ex: "Save the Cat", "Snowflake")

**If user asks for details:**
Load the corresponding data file and present key information from the framework selection guide.

**Once user selects (any mode):**

"**Excellent choix !** Nous utiliserons **[Framework Name]** comme cadre pour structurer votre histoire.

*Rappel : Ce framework est un guide, pas une cage. Si quelque chose ne fonctionne pas pour votre histoire, nous l'adapterons.*"

### 5. Append to Output Document

Append framework selection to {outputFile}:

```markdown
## Framework Narratif

### Framework Sélectionné
[Framework name]

### Pourquoi Ce Framework
[User's reason or your recommendation reason]

### Principes Clés du Framework
[3-5 key principles from the framework data]

---
```

Update frontmatter:
- `framework: [framework-name]`
- Add `3` to `stepsCompleted` array

### 6. Create Framework Summary Document

Copy template from {frameworkSummaryTemplate} to {frameworkSummaryFile} and populate with:
- Framework name and principles
- Why this framework was chosen
- How it will apply to this story

### 7. Present MENU OPTIONS

Display: **Framework sélectionné - Sélectionnez une option:**
- **[A]** Advanced Elicitation — Explorer le framework plus en profondeur
- **[P]** Party Mode — Discuter du choix avec d'autres perspectives
- **[C]** Continuer vers les questions détaillées (personnages, univers, thèmes)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After A or P execution, return to this menu

#### Menu Handling Logic:

- **IF A:** Execute {advancedElicitationTask} to explore framework deeply, then redisplay menu
- **IF P:** Execute {partyModeWorkflow} for multi-perspective discussion, then redisplay menu
- **IF C:** Update frontmatter stepsCompleted, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Frameworks presented clearly at appropriate depth for user experience
- Personalized recommendation based on story concept and guide
- User made informed selection
- Framework choice recorded in output document
- Framework summary document created
- Frontmatter updated with framework and stepsCompleted

### ❌ SYSTEM FAILURE:

- Forcing a framework on the user
- Starting to apply framework details (that's step 4)
- Not explaining frameworks adequately for user's experience level
- Moving on without clear framework selection
- Creating framework summary before selection is confirmed

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and framework is chosen will you update frontmatter and load {nextStepFile} to begin detailed questioning.
