---
name: 'step-06-generate-report'
description: 'Compile all findings into comprehensive audit report'

# Navigation
nextStepFile: './step-07-present-findings.md'
previousStepFile: './step-05-synthesize-reports.md'

# Output
outputFile: '{bbb_output_folder}/audit/project-audit-{date}.md'
auditReportComplete: false
---

# Step 6: Generate Audit Report

## STEP GOAL:
To compile all analysis findings into a comprehensive, well-structured audit report with health scores, detailed issue catalogs, prioritized recommendations, and executive summary — providing a complete picture of project narrative health.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Continuity Editor (Claude)** compiling comprehensive audit report
- Like a senior editor producing final manuscript assessment
- Clear, actionable reporting is essential for author understanding
- You compile report now, present findings in final step

### Step-Specific Rules:
- Compile ALL findings from previous steps into unified report
- Calculate overall project health score
- Generate executive summary with key insights
- Create prioritized issue catalog with actionable recommendations
- Format report for clarity and actionability
- Auto-proceed to step 7 after report generation complete

## EXECUTION PROTOCOLS:
- Compile all analysis sections into cohesive report
- Calculate overall project health score from dimension scores
- Generate executive summary with top priorities
- Create comprehensive issue catalog sorted by severity
- Generate prioritized recommendations with action items
- Add appendix with data currency and historical context
- Store complete report in output file
- Auto-proceed to step 7 after report generation complete

## CONTEXT BOUNDARIES:
- Has access to all analysis findings from steps 2-5
- Has access to all health scores calculated in previous steps
- Has access to output file with accumulated sections
- Compiles and reorganizes content for final report
- Focus: Report compilation and organization

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Report Generation Phase

"**Generating Audit Report...**

Let me compile all analysis findings into a comprehensive project health report with executive summary, health scores, detailed analysis, and prioritized recommendations.

Report generation in progress..."

### 2. Calculate Overall Project Health Score (CORE)

**Reference:** See `data/references/scoring-systems.md` - "Overall Project Health Calculation" section.

**Weighted Average Formula:**
- Narrative Arc Health Score: 25%
- Coherence Health Score: 30%
- Quality Health Score: 25%
- Historical Progress: 10%
- Data Currency: 10%

Store as: `overall_project_health_score` with score (0-100), breakdown, assessment_label

**Assessment Labels:**
- 90-100: Excellent — Ready for final polish
- 75-89: Good — Minor improvements needed
- 60-74: Fair — Notable issues requiring attention
- 40-59: Poor — Substantial work required
- 0-39: Critical — Comprehensive revision needed

After calculation:
"✅ **Overall Project Health Score:** {score}/100 — {label}"

### 3. Generate Executive Summary (CORE)

**Reference:** See `data/templates/audit-report-template.md` - "Executive Summary Template" section.

**Generate:**
- High-level overview with project status and health score
- Top 5 critical findings with descriptions, locations, severity, impact
- Top 3 immediate action items with descriptions, expected impact, estimated effort

Store as: `executive_summary` with overview, critical_findings, immediate_actions

After generation:
"✅ **Executive Summary:** Generated with {count} critical findings and {count} immediate actions"

### 4. Compile Detailed Analysis Sections (CORE)

**Reference:** See `data/templates/audit-report-template.md` for complete report structure.

**Reorganize output file into final structure:**
1. Executive Summary (new)
2. Health Scores Dashboard (new)
3. Narrative Arc Analysis (from step 2)
4. Coherence Check (from step 3)
5. Quality Assessment (from step 4)
6. Historical Analysis Synthesis (from step 5)
7. Issue Catalog (new)
8. Recommendations (new)
9. Appendix (new)

After compilation:
"✅ **Detailed Analysis:** All sections compiled and organized"

### 5. Create Health Scores Dashboard (CORE)

**Reference:** See `data/templates/audit-report-template.md` - "Health Scores Dashboard Template" section.

**Create dashboard with:**
- Overall project health score
- Dimension health scores table
- Complete dimension breakdowns for all three main dimensions

After creation:
"✅ **Health Scores Dashboard:** Created with all dimension breakdowns"

### 6. Generate Issue Catalog (CORE)

**Reference:** See `data/templates/audit-report-template.md` - "Issue Catalog Template" section.

**Generate catalog with:**
- Critical issues (must fix before finalizing)
- Major issues (should fix before publishing)
- Minor issues (polish before final)
- Issues by dimension

**Issue entry format:**
- **[CRITICAL/MAJOR/MINOR]** {Issue Title}
  - Location: Chapter X, {specific location}
  - Dimension: {dimension name}
  - Description: {detailed description}
  - Impact: {why this matters}
  - Suggested Fix: {actionable solution}

After generation:
"✅ **Issue Catalog:** Generated with {critical} critical, {major} major, {minor} minor issues"

### 7. Generate Prioritized Recommendations (CORE)

**Reference:** See `data/templates/audit-report-template.md` - "Recommendations Template" section.

**Generate recommendations with:**
- Priority 1: Critical actions (do first)
- Priority 2: Major improvements (do second)
- Priority 3: Polish and refine (do last)
- Recommendations by dimension

**Format:**
1. **{Action}**
   - Expected Outcome: {result}
   - Estimated Effort: {Low/Medium/High}
   - Impact: {High/Medium/Low}

After generation:
"✅ **Recommendations:** Generated with {priority_1} critical, {priority_2} major, {priority_3} polish actions"

### 8. Generate Appendix (CORE)

**Reference:** See `data/templates/audit-report-template.md` - "Appendix Template" section.

**Generate appendix with:**
- Data currency status (Living Bible, tracking, character audits)
- Previous reports summary
- Analysis metadata

After generation:
"✅ **Appendix:** Generated with data currency, historical summary, and metadata"

### 9. Update Output File with Complete Report

**Reference:** See `data/templates/audit-report-template.md` for complete report structure.

Update `{outputFile}` with complete report including:
1. Frontmatter (updated with all final data)
2. Header
3. Executive Summary
4. Health Scores Dashboard
5. All analysis sections (steps 2-5)
6. Issue Catalog
7. Recommendations
8. Appendix

### 10. Create Latest Audit Link

Create symlink or copy to `audit/latest-audit.md` for quick access.

### 11. Present Report Generation Summary

Display report statistics and structure confirmation.

Auto-proceeding to findings presentation...

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Overall project health score calculated (0-100)
- Executive summary generated with top findings and immediate actions
- Health scores dashboard created with all dimension breakdowns
- Comprehensive issue catalog generated with all issues sorted by severity
- Prioritized recommendations generated with critical/major/polish actions
- Appendix generated with data currency and historical summary
- Output file updated with complete, well-structured report
- Latest audit link created for quick access
- All statistics and metadata accurate

### SYSTEM FAILURE:
- Not calculating overall health score
- Not generating executive summary
- Not creating health scores dashboard
- Not generating comprehensive issue catalog
- Not creating prioritized recommendations
- Not generating appendix
- Not organizing report properly
- Not creating latest audit link

**Master Rule:** Report generation is the culmination of all analysis work. Every finding should be included, every issue cataloged, all recommendations prioritized. The final report must be clear, actionable, and comprehensive. Author depends on this report for understanding project health and next steps.
