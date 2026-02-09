---
name: 'step-06-execute'
description: 'Execute the migration plan - create folders, copy files, convert formats'

# File references (ONLY variables used in this step)
nextStepFile: './step-07-detect-gaps.md'
outputFile: '{bbb_output_folder}/bbb-onboarding-plan-{project_name}.md'
executionLog: '{bbb_output_folder}/bbb-onboarding-log-{project_name}.md'
migrationPlanTemplate: './data/migration-plan-template.md'
gapReportTemplate: './data/gap-report-template.md'
---

# Step 6: Execute Migration

## STEP GOAL:

Execute the approved migration plan — create BBB folder structure, copy chapters with BBB frontmatter, convert characters to YAML format.

## MANDATORY EXECUTION RULES:
### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:
- ✅ You are a Migration Specialist — careful and methodical
- ✅ Think SAFETY FIRST — preserve originals
- ✅ Verify before each operation
- ✅ Log everything for transparency

### Step-Specific Rules:
- 🎯 Focus on SAFE execution of the plan
- 🚫 FORBIDDEN to modify original files
- 💬 HYBRID mode — COPY, never move
- 📋 Log all operations to execution log

## EXECUTION PROTOCOLS:
- 🎯 Execute migration steps sequentially
- 💾 Create BBB folders and files
- 📖 Maintain execution log throughout
- ✅ Verify each operation before proceeding

## CONTEXT BOUNDARIES:
- Available: Approved migration plan from step 5
- Focus: Safe and complete execution
- Limits: Only what's in the approved plan
- Dependencies: Requires PROCEED approval from step 5

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Verify Approval

Check that {outputFile} status is "APPROVED FOR EXECUTION".
If not approved: "⚠️ Error: The migration plan has not been approved. Return to step 5."

### 2. Initialize Execution Log

Create execution log at {executionLog} using **execution log template**:
- See: `{workflow_root}/data/templates/execution-log-template.md`
- Fill template variables with project details
- Begin logging migration process

### 3. Create BBB Folder Structure

Create folders in {project_path} according to **BBB structure reference**:
- See: `{workflow_root}/data/references/bbb-folder-structure.md`
- Create all required folders and subfolders
- Verify each folder created successfully

**Log:**
```markdown
### Step 1: BBB Structure Created
- ✅ bbb-output/
- ✅ story-bible/characters/
- ✅ story-bible/themes/
- ✅ story-bible/timeline/
- ✅ chapters/

**Timestamp:** {timestamp}
```

### 4. Migrate Chapters

Follow **migration procedures** for chapter migration:
- See: `{workflow_root}/data/references/migration-procedures.md` (Chapter Migration Procedure)
- Use **chapter frontmatter template**: `{workflow_root}/data/templates/chapter-frontmatter-template.md`

**Subprocess Optimization (Optional):**
- ⚙️ You MAY use subprocess to copy multiple chapters in parallel
- Purpose: Speed up chapter copying for large projects
- Return: List of successfully copied chapters
- Fallback: If subprocess unavailable, copy sequentially

**For each chapter:**
1. Read original chapter content
2. Add BBB frontmatter (using template)
3. Write to `chapters/chapter-{n}.md`
4. Verify write succeeded

**Log:**
```markdown
### Step 2: Chapters Migrated
**Source:** {original_chapters_path}
**Target:** chapters/
**Count:** {count} chapters
**Files:** {list_or_summary}

**Timestamp:** {timestamp}
```

### 5. Migrate Characters

Follow **migration procedures** for character migration:
- See: `{workflow_root}/data/references/migration-procedures.md` (Character Migration Procedure)
- Use **character YAML template**: `{workflow_root}/data/templates/character-yaml-template.md`

**For each character file:**
1. Read original character content
2. Extract information (name, role, description, psychology, contradictions)
3. Convert to YAML format (using template)
4. Write to `story-bible/characters/{name}.yaml`
5. Verify write succeeded

**Log:**
```markdown
### Step 3: Characters Converted
**Source:** {original_characters_path}
**Target:** story-bible/characters/
**Count:** {count} characters
**Format:** Converted from MD to YAML

**Timestamp:** {timestamp}
```

### 6. Migrate Other Content

**Themes:** Convert to YAML if present
**Structure:** Convert if present
**Other:** Process according to mapping

**Log each migration step.**

### 7. Final Verification

Verify:
- [ ] All folders created
- [ ] All chapters copied with frontmatter
- [ ] All characters converted to YAML
- [ ] Original files untouched
- [ ] No data corruption

**If verification fails:**
- Log error details
- Attempt recovery if possible
- If unrecoverable: ABORT and report to user

### 8. Complete Execution Log

Append to {executionLog}:

```markdown
---

## Migration Complete

**Completed:** {completion_timestamp}
**Status:** SUCCESS

**Summary:**
- Folders created: 5
- Chapters migrated: {count}
- Characters converted: {count}
- Other content: {details}

**Verification:** ✅ PASSED

**Original Files:** ✅ PRESERVED (HYBRID MODE)

---

**Ready for BBB gap detection**
```

### 9. Update Migration Plan

Update {outputFile} status:
```yaml
status: "MIGRATION COMPLETE"
completedDate: "{current_date}"
```

### 10. Display Summary and Auto-Proceed

```markdown
**✅ MIGRATION COMPLETE!**

**Operations performed:**
- ✅ BBB structure created
- ✅ {chapters} chapters migrated with frontmatter
- ✅ {characters} characters converted to YAML
- ✅ Additional content migrated

**Your original files:** PRESERVED (hybrid mode)

**Execution log:** {executionLog}

---

**Direction :** step-07-detect-gaps.md
```

Auto-proceed to {nextStepFile}

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- All BBB folders created
- All chapters copied with BBB frontmatter
- All characters converted to YAML
- Execution log maintained throughout
- Original files preserved
- Verification passed
- Auto-proceeded to step 7

### ❌ SYSTEM FAILURE:
- Skipping verification
- Modifying original files
- Not logging operations
- Corruption of data
- Not preserving originals

**Master Rule:** This step MODIFIES the user's project. Every operation must be safe, verified, and logged. NO data loss is acceptable.
