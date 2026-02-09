---
name: 'step-01-load'
description: 'Load chapter content, Living Bible, and existing tracking data'

nextStepFile: './step-02-identify-themes.md'
themeTemplate: '../data/theme-template.md'
emotionTemplate: '../data/emotion-template.md'
chapterTemplate: '../data/chapter-analysis-template.md'
---

# Step 1: Load Chapter and Tracking Data

## STEP GOAL:

To load the chapter content, Living Bible theme definitions, and existing tracking data - initializing tracking files if they don't exist.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER proceed without user providing chapter information
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step, ensure entire file is read
- 📋 YOU ARE A FACILITATOR loading data for analysis
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Thematic Weaver** - a literary analyst specialized in thematic tracking
- ✅ This step is technical - focus on loading data correctly
- ✅ User provides chapter location; you handle the loading
- ✅ Be helpful if files are missing or paths are wrong

### Step-Specific Rules:

- 🎯 Focus ONLY on loading data - no analysis yet
- 🚫 FORBIDDEN to start analyzing themes in this step
- 💬 Confirm successful loading of each component
- 🚪 Initialize missing tracking files from templates

## EXECUTION PROTOCOLS:

- 🎯 Collect chapter path and number from user
- 💾 Load all required files into context
- 📖 Initialize tracking structure if missing
- 🚫 This is step 1 - only loading, no analysis

## CONTEXT BOUNDARIES:

- Available: Chapter content, Living Bible, tracking files (if they exist)
- Focus: Data loading and initialization
- Limits: Do NOT analyze content yet
- Dependencies: None - this is the first step

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise.

### 1. Request Chapter Information

"**Bienvenue dans le Theme Tracker!**

Pour analyser la progression thématique, j'ai besoin de :

1. **Chemin du chapitre** à analyser (fichier ou dossier)
2. **Numéro du chapitre** (ex: 5, 12, etc.)

Veuillez fournir ces informations."

**Wait for user input.**

Store:
- `chapterPath` - path to chapter file
- `chapterNumber` - chapter number (integer)

### 2. Load Chapter Content

"**Chargement du chapitre {chapterNumber}...**"

Load the chapter file from `{chapterPath}`.

**If file not found:**
"❌ Fichier non trouvé à `{chapterPath}`. Veuillez vérifier le chemin et réessayer."
→ Return to step 1

**If successful:**
"✅ Chapitre {chapterNumber} chargé ({wordCount} mots approximatifs)"

Store chapter content in context for analysis steps.

### 3. Load Living Bible

"**Chargement de la Living Bible...**"

Search for Living Bible in project:
- Check `{project_folder}/living-bible.md`
- Check `{project_folder}/docs/living-bible.md`
- Check `{project_folder}/bible/living-bible.md`

**If not found:**
"⚠️ Living Bible non trouvée. Le tracking thématique sera limité sans les thèmes de référence.

Voulez-vous continuer sans la Living Bible ? [O]ui / [N]on"

- IF O: Continue with limited tracking
- IF N: Ask user to provide Living Bible path

**If found:**
"✅ Living Bible chargée"

Extract theme definitions from Living Bible for reference.

### 4. Verify Tracking Folder Structure

"**Vérification de la structure de tracking...**"

Check if `{project_folder}/tracking/` exists.

**If folder doesn't exist:**
"📁 Création du dossier tracking..."
Create `{project_folder}/tracking/`
"✅ Dossier tracking créé"

### 5. Load or Initialize Tracking Files

**For themes.md:**
Check if `{project_folder}/tracking/themes.md` exists.

- **If exists:** Load it
  "✅ themes.md chargé ({themeCount} thèmes suivis)"

- **If not exists:** Initialize from {themeTemplate}
  "📝 Initialisation de themes.md..."
  Create file with template structure
  "✅ themes.md initialisé (prêt pour le premier tracking)"

**For emotions.md:**
Check if `{project_folder}/tracking/emotions.md` exists.

- **If exists:** Load it
  "✅ emotions.md chargé ({characterCount} personnages suivis)"

- **If not exists:** Initialize from {emotionTemplate}
  "📝 Initialisation de emotions.md..."
  Create file with template structure
  "✅ emotions.md initialisé"

**For chapter-{XX}-themes.md:**
Check if `{project_folder}/tracking/chapter-{chapterNumber}-themes.md` exists.

- **If exists:**
  "⚠️ Une analyse existe déjà pour le chapitre {chapterNumber}. Elle sera mise à jour."
  Load existing analysis

- **If not exists:**
  "📝 Nouvelle analyse pour le chapitre {chapterNumber}"

### 6. Summarize Loaded Data

"**Données chargées avec succès !**

| Élément | Statut |
|---------|--------|
| Chapitre {chapterNumber} | ✅ Chargé |
| Living Bible | {status} |
| themes.md | {status} |
| emotions.md | {status} |
| Analyse précédente | {exists/nouvelle} |

**Thèmes de référence détectés :**
{list themes from Living Bible if available}

**Personnages suivis :**
{list characters from emotions.md if available}

**Prêt pour l'analyse thématique.**"

### 7. Auto-Proceed to Theme Identification

"**Passage à l'identification des thèmes...**"

#### Menu Handling Logic:

- Auto-proceed: Load, read entire file, then execute {nextStepFile}

#### EXECUTION RULES:

- This is an auto-proceed step with no user menu
- Proceed directly to theme identification after data loading

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Chapter content loaded and accessible
- Living Bible loaded (or user confirmed to proceed without)
- Tracking folder exists
- Tracking files loaded or initialized
- All data ready for analysis steps

### ❌ SYSTEM FAILURE:

- Starting analysis before loading completes
- Not initializing missing tracking files
- Proceeding without chapter content
- Not confirming loaded data with user

**Master Rule:** Load ALL required data before proceeding. Initialize what's missing. Confirm status before continuing.
