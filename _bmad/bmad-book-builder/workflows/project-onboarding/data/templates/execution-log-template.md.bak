# Migration Execution Log Template

This template defines the standard format for migration execution logs.

## Template Structure

```markdown
# BBB Migration Execution Log: {project_name}

**Started:** {current_date}
**Project:** {project_name}
**Path:** {project_path}
**Mode:** HYBRID (originals preserved)

---

## Execution Steps

---

### Step 1: BBB Structure Created
- ✅ bbb-output/
- ✅ story-bible/characters/
- ✅ story-bible/themes/
- ✅ story-bible/timeline/
- ✅ chapters/

**Timestamp:** {timestamp}

### Step 2: Chapters Migrated
**Source:** {original_chapters_path}
**Target:** chapters/
**Count:** {count} chapters
**Files:** {list_or_summary}

**Timestamp:** {timestamp}

### Step 3: Characters Converted
**Source:** {original_characters_path}
**Target:** story-bible/characters/
**Count:** {count} characters
**Format:** Converted from MD to YAML

**Timestamp:** {timestamp}

### Step 4: Other Content Migrated
{additional_migration_details}

**Timestamp:** {timestamp}

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

## Field Descriptions

### Header Fields

**project_name**: Name of the project being migrated
**current_date**: Migration start date (YYYY-MM-DD format)
**project_path**: Full path to the project
**Mode**: Always "HYBRID (originals preserved)"

### Step 1: BBB Structure Created

**Timestamp**: When folder structure was created
**Folders**: List all created folders with checkmarks

### Step 2: Chapters Migrated

**Source**: Original path to chapter files
**Target**: BBB chapters folder path
**Count**: Total number of chapters migrated
**Files**: List of chapter filenames or summary
**Timestamp**: When chapter migration completed

### Step 3: Characters Converted

**Source**: Original path to character files
**Target**: BBB characters folder path
**Count**: Total number of characters converted
**Format**: Note about format conversion (MD → YAML)
**Timestamp**: When character conversion completed

### Step 4: Other Content Migrated

**Details**: Any additional content migrated (themes, structure, etc.)
**Timestamp**: When other content migration completed

### Migration Complete Section

**completion_timestamp**: When migration finished
**Status**: SUCCESS (or FAILURE if issues occurred)
**Summary**: Totals for all migration operations
**Verification**: PASSED (or FAILED if verification issues)
**Original Files**: PRESERVED (confirmation of HYBRID mode)

## Usage Example

```markdown
# BBB Migration Execution Log: AgentAdam

**Started:** 2026-01-25
**Project:** AgentAdam
**Path:** /Users/jane/Writing/AgentAdam
**Mode:** HYBRID (originals preserved)

---

## Execution Steps

---

### Step 1: BBB Structure Created
- ✅ bbb-output/
- ✅ story-bible/characters/
- ✅ story-bible/themes/
- ✅ story-bible/timeline/
- ✅ chapters/

**Timestamp:** 2026-01-25 10:15:30

### Step 2: Chapters Migrated
**Source:** /Users/jane/Writing/AgentAdam/manuscript
**Target:** chapters/
**Count:** 24 chapters
**Files:** chapter-01.md through chapter-24.md

**Timestamp:** 2026-01-25 10:17:45

### Step 3: Characters Converted
**Source:** /Users/jane/Writing/AgentAdam/characters
**Target:** story-bible/characters/
**Count:** 8 characters
**Format:** Converted from MD to YAML

**Timestamp:** 2026-01-25 10:19:20

### Step 4: Other Content Migrated
**Themes:** Converted from themes/thematiques.md to themes.yaml
**Structure:** Migrated structure/plan.md to structure.md

**Timestamp:** 2026-01-25 10:20:15

---

## Migration Complete

**Completed:** 2026-01-25 10:20:15
**Status:** SUCCESS

**Summary:**
- Folders created: 5
- Chapters migrated: 24
- Characters converted: 8
- Other content: 2 items (themes, structure)

**Verification:** ✅ PASSED

**Original Files:** ✅ PRESERVED (HYBRID MODE)

---

**Ready for BBB gap detection**
```

## Error Handling Format

If errors occur during migration, document them:

```markdown
### Step X: {Operation Name}
**Status:** ⚠️ PARTIAL SUCCESS / ❌ FAILED

**Error Details:**
- Error type: {error_type}
- Error message: {error_message}
- Affected files: {list_of_files}

**Recovery Action:**
- {action_taken}

**Timestamp:** {timestamp}
```

## Verification Log Format

Document verification results:

```markdown
### Step X: Verification
**Verification Items:**
- [✅/❌] All folders created
- [✅/❌] All chapters copied with frontmatter
- [✅/❌] All characters converted to YAML
- [✅/❌] Original files untouched
- [✅/❌] No data corruption

**Verification Result:** ✅ PASSED / ❌ FAILED
**Timestamp:** {timestamp}
```

## Best Practices

1. **Timestamp everything** - Record when each step completes
2. **Be specific** - List exact counts, paths, filenames
3. **Document errors** - If something goes wrong, log it clearly
4. **Use checkmarks** - Visual indicators (✅) for success
5. **Confirm preservation** - Always note that originals are preserved
6. **Include summaries** - Totals and overview at the end

## Log File Location

Execution logs are saved to:
```
{bbb_output_folder}/bbb-onboarding-log-{project_name}.md
```

Example:
```
/Users/jane/Writing/AgentAdam/bbb-output/bbb-onboarding-log-AgentAdam.md
```

## Logging Throughout Migration

Maintain the log throughout the entire migration process:
1. **Initialize log** at start (create file with header)
2. **Append to log** after each major step
3. **Document errors** immediately when they occur
4. **Complete log** with final summary after migration
5. **Save log** to BBB output folder

This provides a complete audit trail of the migration process.
