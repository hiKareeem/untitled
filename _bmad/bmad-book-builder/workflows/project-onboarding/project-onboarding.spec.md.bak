# Workflow Specification: Project Onboarding

**Module:** bmad-book-builder
**Status:** Placeholder — To be created via create-workflow workflow
**Created:** 2025-01-24
**Priority:** Normal — To be implemented after style-capture

---

## Workflow Overview

**Goal:** Migrate existing writing projects to BBB structure without data loss

**Description:** Analyze an existing writing project with chapters, characters, themes, and other narrative assets, then generate a migration plan to adopt BBB. The workflow is NON-DESTRUCTIVE — it only analyzes and proposes; the author confirms before any changes.

**Workflow Type:** Create-only (single-session)

**Use Case:** Authors with existing projects (5+ chapters written, character docs, etc.) want to adopt BBB without starting from scratch.

---

## Why This Workflow Exists

> **🎯 PROBLEM SOLVED**
>
> BBB is designed for new projects, but most authors already have projects in progress when they discover BBB.
>
> **Without this workflow:** The author must manually recreate their Story Bible, migrate chapters, etc.
>
> **With this workflow:** BBB analyzes the existing project and proposes a structured, validated migration.

**Real test case:** AgentAdam project in `../../Writing/AgentAdam/` with:
- 10 chapters already written
- Structured annexes (characters, psychology, architecture, themes)
- Existing documentation to convert to BBB format

---

## Workflow Structure

### Entry Point

```yaml
---
name: project-onboarding
description: Migrate existing writing projects to BBB structure
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/project-onboarding'
---
```

### Mode

- [ ] Tri-modal (steps-b/, steps-c/, steps-v/) — **NO, create-only**
- [X] Create-only — Single use, analyze and migrate

---

## Planned Steps

| Step | Name | Goal | Type |
|------|------|------|------|
| 1 | **Discover Project** | Locate project, confirm path, validate it's a writing project | Init |
| 2 | **Analyze Structure** | Scan directories, identify content types (chapters, characters, etc.) | Middle (Simple) |
| 3 | **Map Content Types** | Detect existing structures and map to BBB equivalents | Middle (Simple) |
| 4 | **Generate Migration Plan** | Create detailed step-by-step migration document | Middle (Standard) |
| 5 | **Review with Author** | Present plan, allow adjustments, answer questions | Middle (Standard) |
| 6 | **Execute Migration** | If confirmed, execute the migration plan | Middle (Standard) |
| 7 | **Validate + Detect Gaps** | Verify migration works, detect missing BBB assets | Middle (Simple) |
| 8 | **Complete Foundation** | Launch workflows to fill gaps, ensure project is BBB-ready | Final |

---

## Workflow Inputs

### Required Inputs

**1. Project Path**
- User provides path to existing writing project
- Can be relative or absolute
- Workflow validates directory exists

**2. Project Confirmation**
- User confirms this is the correct project
- Brief description of what workflow found

### Optional Inputs

**3. Migration Preferences**
- Hybrid chapters (copy to BBB, keep original) — DEFAULT
- Move only (remove from original location)
- Reference only (BBB reads from original location)

**4. Scope Selection**
- Full migration (all content) — DEFAULT
- Partial migration (select specific folders/files)

---

## Workflow Outputs

### Output Format

- [X] Document-producing

### Output Files

**1. Migration Plan Document** — `bbb-onboarding-plan-{project-name}.md`

```markdown
# BBB Migration Plan: {Project Name}

**Generated:** {date}
**Project Path:** {path}
**Status:** PENDING APPROVAL

---

## Project Analysis Summary

### Detected Content:
- [X] Chapters: 10 files found
- [X] Characters: 17 files found
- [X] Themes: 2 files found
- [X] Psychology: 5 files found
- [ ] Locations: Not detected
- [ ] Timeline: Not detected

### Structure Assessment:
**Current Structure:**
```
project/
├── 1.1 Premisses/
├── 1.4 Personnages/ (17 files)
├── 2.1 Chapitres/ (10 files)
└── ...
```

**Target BBB Structure:**
```
project/
├── bbb-output/           # NEW
├── story-bible/          # NEW - from existing annexes
├── chapters/             # NEW - hybrid copy from 2.1
├── plans/                # NEW
└── [original folders]    # PRESERVED
```

---

## Migration Steps

### Step 1: Create BBB Structure
- [ ] Create `bbb-output/` folder
- [ ] Create `story-bible/` with subfolders
- [ ] Create `chapters/` folder
- [ ] Create `plans/` folder
- [ ] Create `.bbb/` config folder

### Step 2: Migrate Characters → Story Bible
**Source:** `1.4 Personnages/*.md` (17 files)
**Target:** `story-bible/characters/{character-name}.yaml`

**Mapping:**
| Original | Target | Action |
|----------|--------|--------|
| `personnage-adam.md` | `characters/adam.yaml` | Convert to YAML |
| `personnage-sarah.md` | `characters/sarah.yaml` | Convert to YAML |
| ... | ... | ... |

**Validation:** Confirm character attributes map to BBB schema

### Step 3: Migrate Chapters
**Source:** `2.1 Chapitres/*.md` (10 files)
**Target:** `chapters/chapter-{N}.md`

**Action:** Hybrid copy — add BBB frontmatter to existing chapters
**Preserve:** Original files remain in `2.1 Chapitres/`

### Step 4: Migrate Themes
**Source:** `3.2 Themes/fils-thematiques.md`
**Target:** `story-bible/themes/themes.yaml`

### Step 5: Optional — Run Style-Capture
**Source:** Existing chapters (2.1)
**Action:** Run style-capture workflow to analyze author's voice
**Output:** `bbb-output/style-profile.yaml`

---

## Risks and Warnings

### Data Loss Risk: **LOW**
- Original files preserved
- BBB creates new structured copies
- Rollback possible by deleting `bbb-output/`, `story-bible/`, `chapters/`

### Manual Work Required: **MEDIUM**
- Some character attributes may need manual mapping
- Chapter frontmatter may need adjustments
- Review migrated content for accuracy

### Estimated Time: 30-60 minutes
```
```

**2. Migration Execution Log** — `bbb-onboarding-log-{project-name}.md`
- Real-time log of migration execution
- Errors encountered and resolved
- Files created/modified

**3. (Optional) Style Profile** — Generated if Step 5 executed
- Output from style-capture workflow
- Author's voice profile from existing chapters

---

## Content Type Detection Patterns

### Chapter Detection
Looks for:
- Folders named: `chapters`, `chapitres`, `chapter`, `text`, `manuscript`
- Files named: `chapter-*.md`, `chapitre-*.md`, `ch-*.md`
- Sequential numbering: 01, 02, 03...
- Minimum 3 files to confirm

### Character Detection
Looks for:
- Folders named: `characters`, `personnages`, `chars`, `cast`, `protagonists`
- Files with character names
- Character dossiers with psychology/backstory

### Theme Detection
Looks for:
- Folders named: `themes`, `thematiques`, `motifs`, `ideas`
- Files about themes, symbols, metaphors

### Psychology Detection
Looks for:
- Folders named: `psychology`, `psychologie`, `character-psychology`, `depth`
- Files about character motivations, arcs, emotional states

### Structure Detection
Looks for:
- Files named: `structure`, `architecture`, `outline`, `plan`
- Plot breakdown, beat sheets, scene lists

---

## Gap Detection & Foundation Completion

> **🎯 AUTOMATIC COMPLEMENT — Steps 7-8**
>
> After migration, the project may be incomplete relative to BBB standards.
> These steps detect gaps and propose launching the necessary workflows.

### Step 7: Validate + Detect Gaps

**Objective:** Verify migration succeeded AND detect missing BBB-required assets.

**Validation Checks:**
- [ ] `story-bible/` folder exists and is readable
- [ ] `chapters/` folder exists with migrated chapters
- [ ] Chapter frontmatter is valid BBB format
- [ ] Original files preserved (if hybrid mode)

**Gap Detection — What's Missing?**

| BBB Asset | How to Detect | If Missing → Action |
|-----------|---------------|---------------------|
| **Style Profile** | Check if `bbb-output/style-profile.yaml` exists | → Propose `style-capture` workflow |
| **Story Bible (Complete)** | Check if `story-bible/characters/*.yaml` has 5+ characters | → Propose `build-characters` workflow |
| **Chapter Plan** | Check if `plans/chapter-plan.md` exists | → Propose `foundation` workflow |
| **Locations** | Check if `story-bible/locations/*.yaml` exists | → Note: Optional, can skip |
| **Themes** | Check if `story-bible/themes/themes.yaml` exists | → Note: May have migrated from existing |
| **Timeline** | Check if `story-bible/timeline/timeline.yaml` exists | → Note: Optional, can skip |

**Output of Step 7:** Gap Report

```markdown
# BBB Foundation Gap Report

**Migration Status:** ✅ VALIDATED
**Project:** {Project Name}
**Date:** {date}

---

## Migration Validation

✅ Story Bible structure created
✅ Chapters migrated with frontmatter
✅ Original files preserved (hybrid mode)
✅ All folders accessible by BBB workflows

---

## Detected Gaps

### ❌ Style Profile — MISSING
**Impact:** Chapter-Write cannot maintain your voice
**Recommendation:** Run `style-capture` workflow (uses existing chapters)
**Estimated time:** 15-20 minutes

### ❌ Chapter Plan — MISSING
**Impact:** Cannot write chapter 11+ without structured plan
**Recommendation:** Run `foundation` workflow (analyze existing chapters for structure)
**Estimated time:** 30-45 minutes

### ⚠️ Story Bible — PARTIAL
**Status:** 17 characters detected, but may lack full YAML structure
**Impact:** Character workflows may need manual enrichment
**Recommendation:** Run `build-characters` OR manual review
**Estimated time:** 20-30 minutes

---

## Summary

| Item | Status | Action Needed |
|------|--------|---------------|
| Migration | ✅ Complete | None |
| Style Profile | ❌ Missing | style-capture (15 min) |
| Chapter Plan | ❌ Missing | foundation (30 min) |
| Characters | ⚠️ Partial | build-characters (20 min) |

**Total estimated completion time:** 65 minutes

---

## Next Step

Proceed to **Step 8: Complete Foundation** to address these gaps automatically.
```

### Step 8: Complete Foundation (Launch Missing Workflows)

**Objective:** Guide author through launching missing workflows to complete BBB setup.

**Process:**

1. **Present Gap Report** (from Step 7)
2. **Ask user: "Would you like BBB to help complete these missing assets?"**
   - [A] Yes, launch all recommended workflows
   - [S] Select specific workflows to launch
   - [C] Complete manually later

3. **If A or S selected:**

**For each missing asset:**

| Workflow | Trigger | What happens |
|----------|---------|-------------|
| **style-capture** | Style Profile missing | → Launch workflow with existing chapters as input |
| **foundation** | Chapter Plan missing | → Launch workflow in "analyze existing" mode |
| **build-characters** | Characters partial/missing | → Launch workflow to enrich existing chars |
| **living-bible** | Story Bible incomplete | → Launch to organize/validate bible structure |

**Execution Order (Recommended):**
1. **style-capture** first — Analyzes your voice from existing chapters
2. **foundation** second — Creates structured plan using your style
3. **build-characters** third — Enriches characters in BBB format
4. **living-bible** fourth — Organizes everything into coherent bible

**User Control:**
- User can skip any workflow
- User can pause and resume later
- Each workflow runs independently with its own prompts
- User can return to this step anytime

**Final Output of Step 8:**

```markdown
# BBB Foundation Complete

**Project:** {Project Name}
**Date:** {date}

---

## Migration Summary

✅ **Migration Complete** — All files successfully migrated
✅ **Gaps Addressed** — Missing BBB assets created
✅ **Project Ready** — Full BBB workflow integration enabled

---

## Completed Workflows

| Workflow | Status | Output |
|----------|--------|--------|
| project-onboarding | ✅ Complete | Migration plan executed |
| style-capture | ✅ Complete | `bbb-output/style-profile.yaml` |
| foundation | ✅ Complete | `plans/chapter-plan.md` |
| build-characters | ✅ Complete | `story-bible/characters/*.yaml` |
| living-bible | ✅ Complete | `story-bible/` organized |

---

## Ready to Write!

Your project is now fully integrated with BBB:

✅ **Style Profile** — Chapter-Write will maintain your voice
✅ **Chapter Plan** — Structured roadmap for continuing your story
✅ **Story Bible** — Characters, themes, locations accessible
✅ **Existing Chapters** — Migrated and preserved

**Next step:** Run `chapter-write` to write your next chapter!

---

## Quick Reference

**Available Workflows:**
- `chapter-write` — Write chapter 11+ with full context
- `review` — Validate coherence of any chapter
- `bible-update` — Update story bible after each chapter
- `character-audit` — Check character consistency per chapter

**Documentation:**
- BBB Guide: `{project-root}/_bmad/bmad-book-builder/README.md`
- Project Status: `{bbb_output_folder}/bbb-onboarding-summary.md`
```

---

## Agent Integration

### Primary Agent

**Story Architect** — Analyzes project structure, creates migration plan, detects gaps

### Other Agents Referenced

- **Style Coach** — If style-capture is launched (Step 8, when style profile missing)
- **Character Keeper** — Validates character migration format, used by build-characters
- **Thematic Weaver** — Used by living-bible workflow (Step 8)
- **All BBB agents** — May be invoked through workflows launched in Step 8

### Workflow Chaining (Step 8)

**Workflows that may be auto-launched:**
1. `style-capture` — Analyze author's voice from existing chapters
2. `foundation` — Create structured chapter plan (may use existing content)
3. `build-characters` — Convert/enrich character dossiers to BBB format
4. `living-bible` — Organize and validate complete story bible

---

## Automatic Trigger

> **🎯 TRIGGER**
>
> This workflow is **manual** — the author chooses when to run it.
>
> **Typical entry point:**
> - The author discovers BBB with an ongoing project
> - The author wants to migrate an existing project to BBB
> - Lancement via: `bmad run bmad-book-builder:project-onboarding`
>
> **No automatic trigger** — This is a one-time migration workflow.

---

## When to Use This Workflow

**Use cases:**
1. **New BBB user with existing project** — Author has 5+ chapters written, wants to adopt BBB
2. **Project restructuring** — Author wants to organize existing content with BBB structure
3. **Multi-project consolidation** — Author has multiple projects, wants to standardize on BBB

**When NOT to use:**
- Starting a brand new project → Use `foundation` workflow instead
- Project already uses BBB → Not needed
- Only 1-2 chapters written → Manual setup may be faster

---

## Implementation Notes

### Key Features to Implement

**1. Content Detection Engine**
- Pattern matching for common folder/file names
- Heuristics for content type identification
- Support for multiple languages (English, French, etc.)

**2. Structure Mapper**
- Convert existing hierarchies to BBB flat structure
- Preserve semantic meaning (characters → characters/, etc.)
- Handle non-standard structures gracefully

**3. YAML Converter**
- Convert character docs from Markdown to YAML
- Extract attributes: name, role, psychology, contradictions, etc.
- Validate against BBB character schema

**4. Chapter Frontmatter Injector**
- Add BBB frontmatter to existing chapters
- Preserve original content
- Enable chapter-by-chapter workflow integration

**5. Migration Plan Generator**
- Create human-readable migration document
- Show before/after structure
- List all files affected

**6. Safe Execution**
- Copy/hybrid mode (default) — preserve originals
- Verify each step before proceeding
- Rollback capability

**7. Gap Detection Engine (NEW — Step 7)**
- Scan for BBB-required assets after migration
- Check: style-profile.yaml, chapter-plan.md, story-bible completeness
- Generate comprehensive gap report with recommendations
- Estimate completion time for missing assets

**8. Workflow Launcher (NEW — Step 8)**
- Guide user through launching missing workflows
- Support auto-launch (all recommended) or selective launch
- Launch workflows in optimal order (style → foundation → characters → bible)
- Track workflow completion status
- Generate final "BBB Foundation Complete" summary

### Error Handling

- Invalid project path → Prompt for correct path
- No chapters detected → Warn user, confirm this is a writing project
- File read errors → Log and continue, show summary
- YAML conversion failures → Fallback to manual conversion step

### Test Cases

1. **AgentAdam Project** — Complex multi-folder structure with 10 chapters
2. **Simple Project** — Just chapters folder + character docs
3. **Non-standard Structure** — Unusual naming, scattered files
4. **Empty Project** — New folder with no content yet

---

## Post-Migration Validation

After migration + gap completion (Steps 7-8), verify:

- [ ] BBB workflows can read Story Bible
- [ ] Chapter-Write workflow can access chapters
- [ ] Character Keeper can load characters
- [ ] Original files preserved (if hybrid mode)
- [ ] Gap report generated (Step 7)
- [ ] Missing workflows launched or proposed (Step 8)
- [ ] Style profile exists (style-capture completed or skipped)
- [ ] Chapter plan exists (foundation completed or skipped)
- [ ] Story Bible is complete and organized

---

## Integration with Other Workflows

**Workflows Launched (Step 8 — Conditional):**
- `style-capture` — If style profile missing
- `foundation` — If chapter plan missing
- `build-characters` — If characters incomplete/missing
- `living-bible` — If story bible needs organization

**Outputs Used By:**
- All BBB workflows can now read migrated data
- `chapter-write` — Access to chapters, characters, style, plan
- `review` — Access to story bible for validation
- `bible-update` — Access to existing bible structure

**Enables:**
- Author with existing project can immediately start using BBB workflows
- Smooth transition from manual to BBB-assisted writing
- Zero-config setup — all gaps detected and addressed

---

## Success Metrics

**Successful onboarding =**
1. All content detected and catalogued
2. Migration plan presented clearly
3. Author approves plan
4. Migration executes without errors
5. **Gap report generated (Step 7)**
6. **Missing workflows proposed/launched (Step 8)**
7. BBB workflows can read migrated data
8. Original content preserved (if hybrid mode)
9. **Author can run chapter-write immediately after completion**

**Failure modes:**
- Content detection misses major assets → Enhance patterns
- Migration plan unclear → Improve formatting/examples
- YAML conversion fails → Add fallback/manual step
- Author loses data → **CRITICAL** — ensure hybrid mode default

---

_This is a specification. Use the create-workflow workflow to build this workflow._
