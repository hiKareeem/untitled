---
name: 'step-03-map'
description: 'Map detected content types to BBB structure equivalents'

# File references (ONLY variables used in this step)
nextStepFile: './step-04-generate-plan.md'
outputFile: '{bbb_output_folder}/bbb-onboarding-plan-{project_name}.md'
---

# Step 3: Map Content Types

## STEP GOAL:

Map the detected existing content to BBB structure equivalents, creating a clear mapping from "what exists" to "what BBB needs".

## MANDATORY EXECUTION RULES:
### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:
- ✅ You are a Migration Specialist — architectural understanding
- ✅ Map existing structures to BBB standards
- ✅ Preserve semantic meaning
- ✅ Handle non-standard structures gracefully

### Step-Specific Rules:
- 🎯 Focus on mapping, not modifying
- 🚫 FORBIDDEN to create any files yet
- 📋 Document all mappings in migration plan
- 🔄 Think flexibly about structure conversion

## EXECUTION PROTOCOLS:
- 🎯 Map each detected content to BBB equivalent
- 💾 Append mapping to {outputFile}
- 📖 Store mapping for next steps
- 🚫 Auto-proceed after mapping

## CONTEXT BOUNDARIES:
- Available: Detected content from step 2
- Focus: Structure mapping and conversion planning
- Limits: Planning only, no file operations
- Dependencies: Requires content detection from step 2

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Detected Content

Retrieve from step 2:
- `detected_chapters_path` and count
- `detected_characters_path` and count
- `detected_themes` status
- Other detected content

### 2. Map to BBB Structure

Use **BBB Folder Structure** reference for standard mappings:
- See: `{workflow_root}/data/references/bbb-folder-structure.md`

**Mapping Categories:**
- Chapters → `chapters/` (with BBB frontmatter)
- Characters → `story-bible/characters/*.yaml` (convert MD → YAML)
- Themes → `story-bible/themes/themes.yaml`
- Psychology → `story-bible/characters/{id}/psychology.md`
- Structure → `story-bible/structure.md`
- Timeline → `story-bible/timeline/timeline.yaml`

**Handle Non-Standard Structures:**
- Unusual folder names → Map by content analysis
- Combined files → Split into BBB structure
- Scattered content → Consolidate appropriately

### 3. Generate Mapping Document

Create detailed mapping:

```markdown
## Structure Mapping

### Before Structure
{current_directory_tree}

### After Structure (BBB)
{target_directory_tree}

### Content Mapping

#### Chapters
**Source:** {detected_chapters_path}
**Target:** `chapters/chapter-{N}.md`
**Action:** Hybrid copy with BBB frontmatter injection
**Count:** {detected_chapters_count}

#### Characters
**Source:** {detected_characters_path}
**Target:** `story-bible/characters/{name}.yaml`
**Action:** Convert to YAML, validate schema
**Count:** {detected_characters_count}

#### Themes
**Source:** {themes_path}
**Target:** `story-bible/themes/themes.yaml`
**Action:** Restructure as YAML

#### {Other Content}
**Source:** {path}
**Target:** {bbb_target}
**Action:** {conversion_action}
```

### 4. Update Migration Plan

Append mapping to {outputFile}:

```markdown
---

## Mapping Complete

**Mapping Date:** {current_date}

### BBB Structure Target
{bbb_structure_preview}

### Conversion Plan
{detailed_mapping}

---

**Ready to generate the migration plan**
```

### 5. Display Summary and Auto-Proceed

```markdown
**✅ Mapping complete!**

**Target BBB structure identified:**
- story-bible/ — Characters, themes, structure
- chapters/ — Chapters with BBB frontmatter
- bbb-output/ — BBB outputs

---

**Direction :** step-04-generate-plan.md
```

Auto-proceed to {nextStepFile}

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- All detected content mapped to BBB equivalents
- Conversion strategy documented
- Migration plan updated with mapping
- Auto-proceeded to step 4

### ❌ SYSTEM FAILURE:
- Missing mapping for detected content
- Not documenting conversion strategy
- Failing to handle non-standard structures

**Master Rule:** Every detected item MUST have a mapped destination. No content left unmapped.
