---
name: 'step-02-analyze'
description: 'Scan project directories and identify content types (chapters, characters, themes, etc.)'

# File references (ONLY variables used in this step)
nextStepFile: './step-03-map.md'
outputFile: '{bbb_output_folder}/bbb-onboarding-plan-{project_name}.md'
---

# Step 2: Analyze Structure

## STEP GOAL:

Scan the project directory structure to identify and catalog all content types — chapters, characters, themes, locations, and other narrative assets.

## MANDATORY EXECUTION RULES (READ FIRST):
### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:
- ✅ You are a Migration Specialist — methodical and analytical
- ✅ Focus on understanding the project structure
- ✅ Be thorough — every asset counts
- ✅ Take notes on patterns and organization
- ✅ This is READ-ONLY analysis — no modifications

### Step-Specific Rules:
- 🎯 Focus only on scanning and cataloging content
- 🚫 FORBIDDEN to modify any files
- 📋 Document all findings in migration plan
- 🔍 Look for common patterns but stay flexible
- ⚠️ Handle non-standard structures gracefully

## EXECUTION PROTOCOLS:
- 🎯 Scan project directory systematically
- 💾 Append findings to {outputFile}
- 📖 Store detected content for next step
- 🚫 Auto-proceed after analysis (no user input needed)

## CONTEXT BOUNDARIES:
- Available: project_path from step 1
- Focus: Content identification and categorization
- Limits: Read-only scanning, no file modifications
- Dependencies: Requires project_path from step 1

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Project Context

Retrieve project_path from previous step:
- `project_path` — validated path to the project
- `project_name` — extracted from step 1

### 2. Scan Directory Structure

Scan the {project_path} directory systematically:

**Use file system tools to:**
- List all directories and subdirectories
- Identify all markdown (.md) files
- Note any file organization patterns

**Subprocess Optimization (Optional):**
- ⚙️ You MAY use subprocess if the project has many files to scan
- Purpose: Efficiently traverse large directory structures
- Return: Complete directory tree and file listing
- Fallback: If subprocess unavailable, scan in main thread

### 3. Identify Content Types

Based on the scan, categorize content using **detection patterns**:
- See: `{workflow_root}/data/references/content-detection-patterns.md`

**Detection Categories:**
- Chapters, Characters, Themes, Psychology
- Structure, Locations, Timeline, Other Content

Each category has specific patterns for folders, files, and content indicators.

### 4. Generate Content Inventory

Create structured inventory of detected content:

```markdown
## Content Detected

### Chapters
- **Count:** [number]
- **Location:** [path/to/chapters]
- **Files:** [list or summary]
- **Format:** [md/txt/other]

### Characters
- **Count:** [number]
- **Location:** [path/to/characters]
- **Format:** [individual files or combined]

### Themes
- **Status:** [detected/not detected]
- **Location:** [path if found]

### Locations
- **Status:** [detected/not detected]
- **Location:** [path if found]

### Psychology
- **Status:** [detected/not detected]
- **Location:** [path if found]

### Structure
- **Status:** [detected/not detected]
- **Location:** [path if found]

### Other Content
- [List any other significant folders/files]
```

### 5. Update Migration Plan

Append the content inventory to {outputFile}:

**Load {outputFile} and append after the existing content:**

```markdown
---

## Content Analysis Complete

**Scanned:** {project_path}
**Analysis Date:** {current_date}

### Chapter Detection
{chapter_findings}

### Character Detection
{character_findings}

### Theme Detection
{theme_findings}

### Other Content Detected
{other_findings}

---

**Analyse terminée — Prêt pour l'étape suivante**
```

### 6. Store Analysis Results

Store in workflow state for next step:
- `detected_chapters_path` — Where chapters were found
- `detected_chapters_count` — How many chapters
- `detected_characters_path` — Where characters were found
- `detected_characters_count` — How many character files
- `detected_themes` — Theme status
- Other detected content paths

### 7. Display Summary and Auto-Proceed

```markdown
**✅ Analyse terminée !**

**Contenu détecté :**
- Chapitres : {count} fichiers
- Personnages : {count} fichiers
- Thèmes : {status}
- Structure : {status}
- Autre : {other}

---

**Tous les contenus ont été catalogués.**

**Direction :** step-03-map.md
```

**Auto-proceed:** Immediately load, read entire file, then execute {nextStepFile}

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- Complete directory scan performed
- All content types identified and catalogued
- Migration plan updated with findings
- Analysis results stored for next step
- Auto-proceeded to step 3

### ❌ SYSTEM FAILURE:
- Skipping directory scan
- Not documenting findings
- Missing major content types
- Not storing results for next step

**Master Rule:** This is an analysis step — be thorough and complete. Missing content now means migration failures later.
