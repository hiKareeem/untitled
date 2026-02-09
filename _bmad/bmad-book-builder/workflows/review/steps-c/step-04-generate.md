---
name: 'step-04-generate'
description: 'Generate structured review report from analysis results'

# Navigation
nextStepFile: './step-05-present.md'

# Output
outputFile: '{bbb_output_folder}/review/review-report-{scope}.md'
reportTemplate: '../data/report-template.md'
---

# Step 4: Generate Report

## STEP GOAL:
To compile all analysis results into a structured, actionable review report document that clearly communicates issues, severity, and correction suggestions.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Continuity Editor** compiling findings into an actionable report
- Like a building inspector producing a detailed inspection report
- Your report must be clear, structured, and immediately actionable
- The author should know exactly what to fix and how

### Step-Specific Rules:
- Focus ONLY on compiling and formatting the report
- FORBIDDEN to perform additional analysis in this step
- Follow the report template structure exactly
- Ensure every issue has location reference and suggested fix
- Create resolution tracking checklist for authors

## EXECUTION PROTOCOLS:
- Load analysis results from step 3
- Load report template
- Compile issues by category with full details
- Generate resolution tracking checklist
- Write complete report to output file
- Auto-proceed to step 5 after generation

## CONTEXT BOUNDARIES:
- Has access to all analysis results from step 3
- Report template provides structure
- Output file already created from template (step 1)
- Focus: Report compilation and formatting, not analysis

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

**Reference:** `../data/templates/review-templates.yaml` contains all report templates and formatting guidelines.

### 1. Announce Report Generation

"**Generating Review Report...**

Compiling all analysis findings into a structured, actionable report.
Report generation in progress..."

### 2. Update Report Frontmatter

Update {outputFile} frontmatter with final analysis data:

```yaml
stepsCompleted: ['step-01-init', 'step-02-load', 'step-03-analyze', 'step-04-generate']
lastStep: 'step-04-generate'
date: '{current_date}'
user_name: '{user_name}'
reviewScope: '{reviewScope}'
targetChapters: {target_chapters}
reviewType: 'comprehensive'
issuesFound: {total_issues}
issuesBySeverity:
  critical: {critical_count}
  major: {major_count}
  minor: {minor_count}
reviewQuality: '{quality_assessment}'
bibleDimensionsLoaded: {bible_dimensions}
previousSummariesCount: {previous_summaries}
styleProfileAvailable: {boolean}
```

### 3. Generate Executive Summary
See: Executive Summary Template in review-templates.yaml

### 4-9. Generate Category Sections (1-6)
See: Category Section Template in review-templates.yaml

Apply the category section template for each:
- Category 1: Character Consistency
- Category 2: Location Accuracy
- Category 3: Object Tracking
- Category 4: Timeline Validation
- Category 5: Plot Hole Detection
- Category 6: Quality Issues

### 10. Generate Resolution Tracking
See: Resolution Tracking Template in review-templates.yaml

### 11. Generate Recommendations
See: Recommendations Template in review-templates.yaml

### 12. Write Complete Report

Write all generated sections to {outputFile}, replacing template placeholders.

### 13. Confirm Report Generation

Display:

"**Report Generated Successfully!**

### Report Details

| Item | Value |
|------|-------|
| Output File | {outputFile} |
| Total Issues | {total} |
| Critical | {critical} |
| Major | {major} |
| Minor | {minor} |
| Categories Analyzed | 6 |
{if recurring: | Recurring Issues | {count} 🔴}

### Report Structure

✅ Executive Summary
✅ Category 1: Character Consistency ({count} issues)
✅ Category 2: Location Accuracy ({count} issues)
✅ Category 3: Object Tracking ({count} issues)
✅ Category 4: Timeline Validation ({count} issues)
✅ Category 5: Plot Hole Detection ({count} issues)
✅ Category 6: Quality Issues ({count} issues)
✅ Resolution Tracking Checklist
✅ Prioritized Recommendations

{if no issues: **🎉 Congratulations! Your report shows no issues. Your chapter(s) demonstrate excellent narrative coherence and quality.**}

**Report ready for presentation.**"

**Select:** `[C]` Continue to Presentation

### MENU HANDLING LOGIC:

- IF C: Proceed to load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- All 6 category sections generated with complete issue details
- Every issue includes: description, location, severity, suggested fix
- Resolution tracking checklist generated and organized by severity
- Recommendations section provides prioritized action plan
- Recurring issues flagged if applicable
- Report written to output file successfully

### SYSTEM FAILURE:
- Skipping categories in report generation
- Issues missing location references or suggested fixes
- Resolution tracking not generated
- Recommendations not prioritized by severity
- Report not written to output file

**Master Rule:** The report must be immediately actionable. Every issue needs a specific location reference and a clear, implementable fix suggestion. The resolution tracking checklist enables authors to systematically address all issues.
