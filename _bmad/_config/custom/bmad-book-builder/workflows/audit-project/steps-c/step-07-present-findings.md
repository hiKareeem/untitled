---
name: 'step-07-present-findings'
description: 'Present audit summary and recommendations to author'

# Navigation
previousStepFile: './step-06-generate-report.md'
finalStep: true

# Output
outputFile: '{bbb_output_folder}/audit/project-audit-{date}.md'
latestAuditLink: '{bbb_output_folder}/audit/latest-audit.md'
---

# Step 7: Present Findings

## STEP GOAL:
To present the audit findings in a clear, actionable format that helps authors understand their project's narrative health and provides specific next steps for improvement.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Continuity Editor (Claude)** presenting comprehensive audit findings
- Like a senior editor walking through manuscript assessment with author
- Clear presentation is essential for author understanding and action
- You present findings now, then complete workflow

### Step-Specific Rules:
- Present findings in clear, organized format
- Highlight critical issues requiring immediate attention
- Provide actionable next steps with priorities
- Balance honesty with encouragement
- Offer follow-up options
- Wait for user acknowledgment before completing

## EXECUTION PROTOCOLS:
- Display executive summary with top findings
- Present health scores with context and interpretation
- Highlight critical and major issues
- Provide prioritized next steps
- Encourage author by noting strengths
- Offer follow-up workflow options
- Wait for user acknowledgment

## CONTEXT BOUNDARIES:
- Has access to complete audit report from step 6
- Has access to all health scores and findings
- Presents summary with option to view full report
- Focus: Clear, actionable presentation

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Presentation Phase

"**Presenting Audit Findings...**

Let me walk you through the comprehensive project health assessment. I'll highlight the key findings, health scores, critical issues, and recommended next steps.

Preparing presentation..."

### 2. Display Audit Header

**Reference:** See `data/templates/audit-report-template.md` - "Presentation Summary Template" section.

Display audit header with date, auditor, scope, report location, and quick access link.

### 3. Present Executive Summary

**Reference:** See `data/templates/audit-report-template.md` - "Presentation Summary Template" section.

Display:
- Overall project health score with explanation
- Project phase assessment
- Top 3-5 critical issues
- Top 3 immediate actions

### 4. Present Health Scores Dashboard

**Reference:** See `data/templates/audit-report-template.md` - "Health Scores Dashboard Template" section.

Display:
- Dimension health scores table
- Complete dimension breakdowns for all three main dimensions
- Status indicators (Excellent/Good/Fair/Poor/Critical)

### 5. Highlight Strengths

Display:
- 5-10 significant strengths across all dimensions
- What's working well
- Advice on maintaining strengths

### 6. Present Critical and Major Issues

Display:
- All critical issues with details (location, dimension, impact, fix)
- Top 5-10 major issues with same format
- Note about minor issues count

### 7. Present Prioritized Recommendations

**Reference:** See `data/templates/audit-report-template.md` - "Recommendations Template" section.

Display:
- Priority 1: Critical actions (3-5 items)
- Priority 2: Major improvements (5-10 items)
- Priority 3: Polish and refine (5-10 items)
- Recommendations by dimension

### 8. Provide Next Steps and Options

Display:
- Recommended workflow (5 steps)
- Immediate actions for this week and this month
- Checkboxes for action items

### 9. Offer Encouragement

Display encouraging message acknowledging:
- Hard work and progress
- Specific strengths to celebrate
- Normal revision phase
- Confidence in author's ability
- Reminder that writing is rewriting

### 10. Present Follow-Up Options

Display:
- Workflows that can help (address issues, update data, track progress)
- Recommended next session based on audit findings

### 11. Provide Full Report Access

**Reference:** See `data/templates/audit-report-template.md` - "Presentation Summary Template" section.

Display:
- Complete report location and quick access link
- Full report contents overview
- How to use the full report

### 12. Final Menu and Completion

**Reference:** See `data/templates/audit-report-template.md` - "Completion Message Template" section.

Display final menu with options: [V] View Full Report, [R] Re-run Audit, [Q] Quit, [?] Help

**Menu Handling:**
- **V (View)**: Display message with report location and preview
- **R (Re-run)**: Display message about making changes first
- **Q (Quit)**: Display completion message (see template), update output file frontmatter with completion status
- **? (Help)**: Provide guidance based on audit findings

**IF Q (Quit) selected:** Update `{outputFile}` frontmatter with auditComplete: true, completionDate, presentedTo

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Executive summary presented with top findings
- Health scores dashboard displayed with all dimensions
- Project strengths highlighted and celebrated
- Critical and major issues presented clearly
- Prioritized recommendations provided
- Next steps and workflow options offered
- Encouragement and support provided to author
- Full report access information provided
- Follow-up menu presented and handled
- Completion message displayed (for Quit)

### SYSTEM FAILURE:
- Not presenting executive summary
- Not displaying health scores
- Not highlighting strengths
- Not presenting issues clearly
- Not providing recommendations
- Not offering next steps
- Not providing encouragement
- Not presenting follow-up options

**Master Rule:** Presentation is the final touchpoint with the author. Findings must be clear, actionable, and balanced. Celebrate strengths while being honest about issues. Provide hope and specific next steps. Author should leave with clear understanding of project health and concrete actions to take.
