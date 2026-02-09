---
name: 'step-03-generate'
description: 'Generate comprehensive status report from analysis results'

# Navigation
nextStepFile: './step-04-present.md'

# Output
outputFile: '{bbb_output_folder}/reports/status-report-{date}.md'
latestReportLink: '{bbb_output_folder}/reports/latest-status.md'
---

# Step 3: Generate Report

## STEP GOAL:
To compile all analysis results into a comprehensive, readable status report that clearly communicates project health, progress, and actionable next steps.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Character Keeper (Marie)** generating a comprehensive status report
- Like a project manager compiling an executive status summary
- Your report must be clear, organized, and immediately actionable
- The author should see exactly where the project stands and what to do next

### Step-Specific Rules:
- Focus ONLY on compiling and formatting the report
- FORBIDDEN to perform additional analysis in this step
- Follow the report structure defined below
- Ensure all sections are complete and accurate
- Create both timestamped and latest reports

## EXECUTION PROTOCOLS:
- Load analysis results from step 2
- Compile report section by section
- Format data for readability
- Write complete report to output file
- Create latest-status.md symlink/copy
- Auto-proceed to step 4 after generation

## CONTEXT BOUNDARIES:
- Has access to all analysis results from step 2
- Report structure is defined in this step
- Output file already created from step 1
- Focus: Report compilation and formatting

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Report Generation

"**Generating Status Report...**

Compiling all analysis findings into a comprehensive project status report.
Report generation in progress..."

### 2. Update Report Frontmatter

Update {outputFile} frontmatter with final analysis data:

```yaml
---
stepsCompleted: ['step-01-scan', 'step-02-analyze', 'step-03-generate']
lastStep: 'step-03-generate'
date: '{current_date}'
user_name: '{user_name}'
reportType: 'comprehensive-status'
scanComplete: true
analysisComplete: true
reportGenerated: true
chapter_completion: {percent}
bible_completion: {percent}
overall_health: {label}
overall_health_percentage: {percent}
attention_items_count: {total}
---
```

### 3. Generate Report Header

**Reference:** See `data/reports/section-templates.md` → "Executive Summary Template"

Replace existing content in {outputFile} with executive summary and quick stats as specified in the template.

### 4. Generate Chapter Progress Section

**Reference:** See `data/reports/section-templates.md` → "Chapter Progress Section Template"

Generate chapter progress section with overview, details table, and visualization as specified in the template.

### 5. Generate Character Arc Status Section

**Reference:** See `data/reports/section-templates.md` → "Character Arc Status Section Template"

Generate character arc status section with overview, details table, and analysis as specified in the template.

### 6. Generate Bible Completion Section

**Reference:** See `data/reports/section-templates.md` → "Bible Currency Section Template"

Generate bible currency status section with overview, analysis, and dimension details as specified in the template.

### 7. Generate Thematic Tracking Section

**Reference:** See `data/reports/section-templates.md` → "Thematic Tracking Section Template"

Generate thematic tracking section with overview and analysis as specified in the template.

### 8. Generate Rhythm Tracking Section

**Reference:** See `data/reports/section-templates.md` → "Rhythm & Pacing Section Template"

Generate rhythm and pacing analysis section as specified in the template.

### 9. Generate Recent Activity Section

**Reference:** See `data/reports/section-templates.md` → "Recent Activity Section Template"

Generate recent activity section with last 5 updates and summary as specified in the template.

### 10. Generate Attention Items Section

**Reference:** See `data/reports/section-templates.md` → "Attention Items Section Template"

Generate attention items section organized by priority as specified in the template.

### 11. Generate Recommendations Section

**Reference:** See `data/reports/section-templates.md` → "Recommendations Section Template"

Generate recommendations section with immediate actions, short-term goals, long-term goals, and workflow integration guide as specified in the template.

### 12. Generate Footer

**Reference:** See `data/reports/section-templates.md` → "Report Footer Template"

Generate report footer with metadata, data sources, and next report guidance as specified in the template.

### 13. Write Complete Report

Write all generated sections to {outputFile}, completely replacing any existing content.

### 14. Create Latest Status Link & Confirm Generation

**Reference:** See `data/generation/confirmation-templates.md` → "Latest Status Link Creation Template" and "Report Generation Confirmation Template"

Create or update `{latestReportLink}` to point to this report using the symlink or copy method specified in the template.

Then display the confirmation template with report details, structure overview, access information, and health-specific messages.

**Select:** `[C]` Continue to Presentation

### MENU HANDLING LOGIC:

- IF C: Proceed to load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Executive summary generated with project health
- Chapter progress section complete with all chapters listed
- Character arc status section complete with all characters
- Bible currency section complete with all 5 dimensions
- Thematic tracking section generated (or "not started" message)
- Rhythm tracking section generated (or "not started" message)
- Recent activity section formatted with 5 most recent files
- Attention items section organized by priority
- Recommendations section provides prioritized next steps
- Report metadata includes data sources and next report guidance
- Report written to output file successfully
- Latest status link created/updated

### SYSTEM FAILURE:
- Skipping sections in report generation
- Not including all chapters, characters, or dimensions
- Not organizing attention items by priority
- Not providing specific recommendations with workflow guidance
- Not creating latest status link
- Report not written to output file

**Master Rule:** The status report must be comprehensive, clear, and immediately actionable. Every section should provide value — from high-level health overview to specific next steps. The author should finish reading knowing exactly where their project stands and what to do next.
