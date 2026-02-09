---
name: 'step-07-detect-gaps'
description: 'Validate migration and detect missing BBB assets that need to be created'

# File references (ONLY variables used in this step)
nextStepFile: './step-08-complete-foundation.md'
outputFile: '{bbb_output_folder}/bbb-onboarding-plan-{project_name}.md'
gapReportFile: '{bbb_output_folder}/bbb-gap-report-{project_name}.md'
gapReportTemplate: './data/gap-report-template.md'
---

# Step 7: Validate + Detect Gaps

## STEP GOAL:

Verify that the migration succeeded and detect which BBB-required assets are missing, generating a comprehensive gap report.

## MANDATORY EXECUTION RULES:
### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:
- ✅ You are a Migration Specialist — thorough validation
- ✅ Check everything systematically
- ✅ Be honest about gaps found
- ✅ Think holistically about BBB completeness

### Step-Specific Rules:
- 🎯 Focus on validation and gap detection
- 📋 Be comprehensive — check all BBB assets
- 💬 Generate actionable gap report
- ⚠️ Don't assume anything — verify everything

## EXECUTION PROTOCOLS:
- 🎯 Verify migration success first
- 📋 Check all BBB-required assets
- 💾 Generate gap report document
- 📖 Store gap data for next step

## CONTEXT BOUNDARIES:
- Available: Migrated BBB structure from step 6
- Focus: Validation and gap identification
- Limits: Detection only, no gap filling yet
- Dependencies: Requires completed migration from step 6

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Verify Migration Success

Check that migration completed:
- {outputFile} status is "MIGRATION COMPLETE"
- {executionLog} shows success
- BBB folders exist in project

**If migration incomplete:** "⚠️ Error: The migration is not complete. Check step 6."

### 2. Initialize Gap Detection

Load {gapReportTemplate} for structure.

Check BBB-required assets using **Gap Detection Criteria**:
- See: `{workflow_root}/data/references/gap-detection-criteria.md`

**Required Assets:**
1. Style Profile — `bbb-output/style-profile.yaml`
2. Chapter Plan — `plans/chapter-plan.md`
3. Characters — `story-bible/characters/*.yaml` (completeness)
4. Story Bible — Overall organization
5. Locations — `story-bible/locations/` (optional)
6. Timeline — `story-bible/timeline/` (optional)

### 3. Check Each BBB Asset

**Subprocess Optimization (Optional):**
- ⚙️ You MAY use subprocess to check multiple assets in parallel
- Purpose: Faster gap detection across many files
- Return: Status of all checked assets
- Fallback: If subprocess unavailable, check sequentially

**For each asset:**
1. Check if file/folder exists
2. If exists, verify completeness (using criteria from reference)
3. Determine status: COMPLETE, PARTIAL, or MISSING
4. Calculate time estimate to fix
5. Identify action needed (workflow or manual)

See **Gap Detection Criteria** for detailed status definitions and time estimates.

### 4. Generate Gap Report

Create {gapReportFile} from template:

**Fill template with detected gaps:**
```markdown
---
title: "BBB Foundation Gap Report: {project_name}"
generated: "{current_date}"
project_path: "{project_path}"
migration_status: "MIGRATION COMPLETE"
---
```

**Fill the gaps table:**
| BBB Asset | Status | Missing? | Action Needed | Time Estimate |
|-----------|--------|----------|---------------|---------------|
| **Style Profile** | {style_status} | {style_missing} | Run style-capture workflow | {style_time} |
| **Chapter Plan** | {plan_status} | {plan_missing} | Run foundation workflow | {plan_time} |
| **Characters** | {chars_status} | {chars_missing} | Run build-characters or manual | {chars_time} |
| **Story Bible** | {bible_status} | {bible_missing} | Run living-bible or manual | {bible_time} |

**Fill detailed analysis for each gap.**

**Calculate totals:**
- Total gaps detected
- Total estimated time

### 5. Determine BBB Readiness

**Assess overall BBB foundation completeness** (using criteria from reference):

**If 0-1 gaps:**
- BBB Readiness: HIGH
- Recommendation: Optional improvements - can proceed with minimal gaps

**If 2-3 gaps:**
- BBB Readiness: MEDIUM
- Recommendation: Address gaps before full workflow usage

**If 4+ gaps:**
- BBB Readiness: LOW
- Recommendation: Complete foundation before writing

See **Gap Detection Criteria** for detailed readiness level definitions.

### 6. Update Migration Plan

Append gap summary to {outputFile}:

```markdown
---

## Gap Detection Complete

**Detection Date:** {current_date}
**Gap Report:** {gapReportFile}

**Gaps Detected:** {total_gaps}
**Estimated Completion Time:** {total_time}
**BBB Readiness:** {readiness}

**Next Step:** Complete Foundation (address gaps)
```

### 7. Display Summary and Auto-Proceed

```markdown
**✅ Validation complete — Gaps detected**

**Migration Status:** ✅ SUCCESS

**Gaps detected:**
- {gap_summary}

**Estimated time to complete:** {total_time}

**BBB Readiness :** {readiness}

---

**Rapport complet :** {gapReportFile}

**Direction :** step-08-complete-foundation.md
```

Auto-proceed to {nextStepFile}

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- Migration validation completed
- All BBB assets checked systematically
- Comprehensive gap report generated
- Time estimates provided
- BBB readiness assessed
- Auto-proceeded to step 8

### ❌ SYSTEM FAILURE:
- Skipping validation
- Not checking all BBB assets
- Incomplete gap report
- Missing time estimates
- Not assessing BBB readiness

**Master Rule:** Gap detection is the foundation for successful BBB usage. Missing gaps now means broken workflows later. Be thorough.
