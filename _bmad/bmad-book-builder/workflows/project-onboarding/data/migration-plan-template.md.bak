---
title: "BBB Migration Plan: {project_name}"
generated: "{date}"
project_path: "{project_path}"
author: "{user_name}"
status: "PENDING APPROVAL"
---

# BBB Migration Plan: {project_name}

**Generated:** {date}
**Project Path:** {project_path}
**Author:** {user_name}
**Status:** ⏳ PENDING APPROVAL

---

## Executive Summary

This migration will integrate your existing writing project into the BBB structure so you can use all writing-assistance workflows.

---

## Detected Content

### Chapters Found
- **Count:** {chapter_count}
- **Location:** {chapter_location}
- **Format:** {chapter_format}

### Characters Found
- **Count:** {character_count}
- **Location:** {character_location}
- **Format:** {character_format}

### Other Content
- **Themes:** {themes_status}
- **Locations:** {locations_status}
- **Timeline:** {timeline_status}
- **Psychology:** {psychology_status}
- **Structure:** {structure_status}

---

## Migration Strategy

**Mode:** HYBRID (Recommended)
- ✅ Original files preserved in place
- ✅ BBB creates structured copies
- ✅ Zero data loss risk

**Scope:** {scope}
- Full migration (all content)
- Partial migration (selected folders only)

---

## Before Structure

```
{project_name}/
{current_structure_tree}
```

---

## After Structure

```
{project_name}/
├── bbb-output/           # NEW - BBB outputs
├── story-bible/          # NEW - from existing annexes
├── chapters/             # NEW - hybrid copy
├── plans/                # NEW - chapter plans
└── [original folders]    # PRESERVED
{new_structure_tree}
```

---

## Migration Steps

### Step 1: Create BBB Structure
- [ ] Create `bbb-output/` folder
- [ ] Create `story-bible/` with subfolders
- [ ] Create `chapters/` folder
- [ ] Create `plans/` folder

### Step 2: Migrate Characters → Story Bible
**Source:** {character_source}
**Target:** `story-bible/characters/*.yaml`

**Mapping:**
{character_mapping}

### Step 3: Migrate Chapters
**Source:** {chapter_source}
**Target:** `chapters/chapter-{N}.md`

**Action:** Hybrid copy — add BBB frontmatter, preserve content

### Step 4: Migrate Themes
**Source:** {themes_source}
**Target:** `story-bible/themes/themes.yaml`

### Step 5: Optional — Run Style-Capture
**Source:** Existing chapters
**Action:** Run style-capture workflow
**Output:** `bbb-output/style-profile.yaml`

---

## Risks and Warnings

### Data Loss Risk: **LOW**
- Original files preserved (hybrid mode)
- BBB creates new structured copies
- Rollback possible by deleting `bbb-output/`, `story-bible/`, `chapters/`

### Manual Work Required: **MEDIUM**
- Some character attributes may need manual mapping
- Chapter frontmatter may need adjustments
- Review migrated content for accuracy

### Estimated Time: {estimated_time}

---

## Approval Required

**⚠️ IMPORTANT:** This migration will create new folders and files in your project.

**To proceed, confirm:**
- [ ] I have reviewed the migration plan
- [ ] I understand the hybrid mode (originals preserved)
- [ ] I am ready to proceed

**Type "PROCEED" to confirm, or "ABORT" to cancel.**
