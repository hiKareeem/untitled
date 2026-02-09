---
name: 'step-e-01-trigger'
description: 'Select update trigger and load chapter content for bible updates'

# File References
thisStepFile: './step-e-01-trigger.md'
nextStepFile: './step-e-02-chronology.md'
workflowFile: '../workflow.md'

# Bible File Locations
bibleFolder: '{bbb_output_folder}/bible'
chronologieFile: '{bbb_output_folder}/bible/chronologie.md'
lieuxFile: '{bbb_output_folder}/bible/lieux.md'
objetsFile: '{bbb_output_folder}/bible/objets.md'
personnesFile: '{bbb_output_folder}/bible/personnes.md'
themesFile: '{bbb_output_folder}/bible/themes.md'

# Templates
timelineTemplate: '../data/timeline-template.md'
locationsTemplate: '../data/locations-template.md'
objectsTemplate: '../data/objects-template.md'
personnesTemplate: '../data/people-template.md'
themesTemplate: '../data/themes-template.md'

# Input Discovery
chapterPattern: '{bbb_output_folder}/chapters/chapter-*.md'
chapterPlanPattern: '{bbb_output_folder}/chapter-plan*.md'
---

# Step E-01: Select Update Trigger

## STEP GOAL:

To identify what event triggered this bible update, load the relevant source content (chapter, event description), and prepare for multi-dimensional updates.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- NEVER make updates without understanding the source content
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE THE BIBLE GUARDIAN, keeper of continuity
- YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- You are the **Character Keeper** — Bible Guardian
- You protect the story's continuity across all dimensions
- You catch details others miss
- You maintain the living memory of the story

### Step-Specific Rules:

- Focus ONLY on trigger selection and content loading
- FORBIDDEN to start updating bible files yet (that's steps 2-6)
- Diagnostic approach: understand what happened before recording
- Create extraction checklist for subsequent steps

## EXECUTION PROTOCOLS:

- Load and analyze source content (chapter or event description)
- Extract key information for each dimension
- Prepare update notes for steps 2-6
- FORBIDDEN to modify bible files in this step

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Check Bible Folder Existence

First, check if the bible folder and files exist:

- Look for folder at `{bibleFolder}`
- If folder doesn't exist: Create it
- For each bible file (chronologie, lieux, objets, personnes, themes):
  - If file doesn't exist: Copy from corresponding template
  - If file exists: Note current state for updates

### 2. Select Update Trigger

"**Quel événement déclenche cette mise à jour ?**

**[1]** Chapitre terminé — J'ai fini d'écrire un chapitre
**[2]** Événement majeur — Mort, révélation, changement de lieu important
**[3]** Transformation de personnage — Percée psychologique, changement relationnel
**[4]** Évolution thématique — Le thème a atteint une nouvelle phase
**[5]** Mise à jour complète — Vérifier et mettre à jour toutes les dimensions

Sélectionnez le déclencheur :"

### 3. Load Source Content

**IF trigger == 1 (Chapitre terminé):**

"Quel chapitre venez-vous de terminer ?"

- Look for chapters matching `{chapterPattern}`
- List available chapters if multiple
- Load the specified chapter completely
- Extract: chapter number, day(s) covered, locations visited, objects mentioned, characters present, themes touched

**IF trigger == 2 (Événement majeur):**

"Décrivez l'événement majeur qui s'est produit :
- Quoi : [description de l'événement]
- Quand : [jour/moment dans la chronologie]
- Où : [lieu]
- Qui : [personnages impliqués]
- Impact : [conséquences immédiates]"

**IF trigger == 3 (Transformation personnage):**

"Décrivez la transformation du personnage :
- Qui : [nom du personnage]
- Avant : [état précédent]
- Déclencheur : [ce qui a causé le changement]
- Après : [nouvel état]
- Impact relationnel : [comment cela affecte les autres]"

**IF trigger == 4 (Évolution thématique):**

"Décrivez l'évolution thématique :
- Thème : [nom du thème]
- Phase précédente : [description]
- Nouvelle phase : [description]
- Manifestation : [comment cela se manifeste dans l'histoire]
- Personnages concernés : [qui porte ce thème]"

**IF trigger == 5 (Mise à jour complète):**

"Mode mise à jour complète activé. Je vais passer en revue chaque dimension.

Avez-vous un chapitre spécifique à analyser, ou souhaitez-vous une révision générale ?"

### 4. Extract Update Notes

Based on source content, create extraction notes for each dimension:

"**Extraction des mises à jour potentielles :**

**Chronologie:**
- [ ] Jour(s) à ajouter : [list]
- [ ] Événements à enregistrer : [list]

**Lieux:**
- [ ] Nouveaux lieux : [list]
- [ ] Mises à jour de lieux existants : [list]
- [ ] Événements par lieu : [list]

**Objets:**
- [ ] Nouveaux objets : [list]
- [ ] Changements d'état d'objets : [list]
- [ ] Transferts de propriété : [list]

**Personnages:**
- [ ] États psychologiques modifiés : [list]
- [ ] Relations modifiées : [list]
- [ ] Progressions d'arc : [list]

**Thèmes:**
- [ ] Évolutions thématiques : [list]
- [ ] Connexions personnage-thème : [list]"

### 5. Confirm Extraction

"**Récapitulatif des mises à jour détectées :**

[Display extraction notes]

Ces informations vous semblent-elles complètes ? Voulez-vous ajouter ou corriger quelque chose ?"

### 6. Present MENU OPTIONS

Display: **Extraction terminée - Sélectionnez une option:**
- **[A]** Ajouter des informations manquantes
- **[C]** Continuer vers la mise à jour de la chronologie

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed when user selects 'C'
- If 'A', return to step 4 to add more information

#### Menu Handling Logic:

- **IF A:** Return to [step 4](#4-extract-update-notes) to add more
- **IF C:** Store extraction notes in memory, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Bible folder and files exist (created if missing)
- Trigger type identified
- Source content loaded and analyzed
- Extraction notes created for all 5 dimensions
- User confirmed extraction completeness
- Ready to proceed to chronology update

### FAILURE:

- Starting to update bible files (that's steps 2-6)
- Not loading source content completely
- Missing extraction for any dimension
- Proceeding without user confirmation

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and extraction is confirmed will you load {nextStepFile} to begin chronology updates.
