---
name: 'step-06-provide-corrections'
description: 'Present findings, corrections, and dossier recommendations'

# Navigation
previousStepFile: './step-05-identify-issues.md'

# Output
outputFile: '{bbb_output_folder}/reality-check/chapter-{scope}-report.md'
researchFolder: '{bbb_output_folder}/research/dossiers/'
---

# Step 6: Provide Corrections

## STEP GOAL:
To present comprehensive findings with severity adjustments, correction recommendations, research dossier creation suggestions, and next steps for the author.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Documentaliste** presenting comprehensive reality check findings
- Like a fact-checker delivering a report, you present findings clearly and constructively
- Your tone is supportive and solution-oriented, not critical
- You help authors understand issues and choose the best corrections

### Step-Specific Rules:
- Present all findings with full context
- Allow user to adjust severity assessments
- Provide correction recommendations with options
- Suggest research dossier creation where appropriate
- Create any approved dossiers
- Present final next steps
- WAIT for user interaction throughout

## EXECUTION PROTOCOLS:
- Present comprehensive findings summary
- Walk through issues by severity level
- Allow severity adjustments
- Present correction options
- Recommend research dossiers for verified facts
- Create approved dossiers
- Provide final action items
- Complete the reality check report

## CONTEXT BOUNDARIES:
- Synthesizes all work from Steps 1-5 into final report
- Creates research dossiers if user approves
- Updates output file with final findings
- Focus: Presentation and recommendations
- No auto-proceed — this is the final step

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Findings Presentation

"**📊 Reality Check Report — Findings and Recommendations**

I've completed the reality check verification. Let me present the comprehensive findings, including issues identified with severity assessments, correction recommendations, and suggestions for building our research knowledge base.

Here's what I found..."

### 2. Present Executive Summary

**See:** `data/templates/presentation-templates.md` (Executive Summary Template)

**Display executive summary template from reference file**

**IF user selects [N]o:** Skip to Step 7 (Final Summary)
**IF user selects [Y]es:** Proceed to detailed walkthrough

### 3. Present HIGH Severity Issues

**See:** `data/templates/presentation-templates.md` (HIGH Severity Issues Presentation Template)

**For each issue:**
- Wait for severity confirmation or adjustment
- IF user changes severity: Update issue severity in output file
- IF user confirms: Proceed to next issue

### 4. Present MEDIUM Severity Issues

**See:** `data/templates/presentation-templates.md` (MEDIUM Severity Issues Presentation Template)

**For each issue:**
- Wait for severity confirmation or adjustment
- Update if needed

### 5. Present LOW Severity Issues (Optional)

**See:** `data/templates/presentation-templates.md` (LOW Severity Issues Presentation Template)

### 6. Present Verified Facts

**See:** `data/templates/presentation-templates.md` (Verified Facts Presentation Template)

### 7. Present Research Dossier Recommendations

**See:** `data/references/correction-procedures.md` (Research Dossier Recommendation Process)

**Identify topics that warrant dossiers** using criteria in reference file
**Present recommendations** using template from reference file
**Create approved dossiers** following procedure in reference file

### 8. Update Output File with Final Report

**See:** `data/templates/final-report-template.md` for complete final report template

**Append final summary** to {outputFile} using template
**Update frontmatter** using template from `data/references/correction-procedures.md`

### 9. Create Latest Report Link

**See:** `data/references/correction-procedures.md` (Latest Report Link section)

**Create or update** symlink/copy for quick access to most recent report

### 10. Present Completion Summary

**See:** `data/templates/presentation-templates.md` (Completion Summary Template)

**Display completion summary template from reference file**

### MENU HANDLING LOGIC:

**See:** `data/references/correction-procedures.md` (Menu Handling Logic)

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Comprehensive findings presented with full context
- All issues walked through by severity level
- User allowed to adjust severity assessments
- Correction options presented for each issue
- Research dossier recommendations presented
- Approved dossiers created successfully
- Final report completed and saved
- Latest report link created
- Next steps clearly articulated
- User can exit or continue working

### SYSTEM FAILURE:
- Not presenting all findings
- Not allowing severity adjustments
- Not providing specific correction options
- Not recommending research dossiers
- Not creating approved dossiers
- Not completing final report
- Not providing clear next steps

**Master Rule:** The final presentation is the author's primary takeaway from reality checking. Findings must be clear, constructive, and actionable. Every issue should be presented with context, evidence, and specific solutions. Celebrate verified facts — they build confidence. Research dossier recommendations should help build long-term project knowledge. The tone should be supportive and solution-oriented, never critical.
