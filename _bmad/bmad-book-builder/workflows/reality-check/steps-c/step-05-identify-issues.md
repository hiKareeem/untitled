---
name: 'step-05-identify-issues'
description: 'Identify and categorize issues found during verification'

# Navigation
nextStepFile: './step-06-provide-corrections.md'
previousStepFile: './step-04-web-verification.md'

# Output
outputFile: '{bbb_output_folder}/reality-check/chapter-{scope}-report.md'
---

# Step 5: Identify Issues

## STEP GOAL:
To synthesize all verification results, identify issues with severity assessments, and prepare a comprehensive list of problems and corrections for user review.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Documentaliste** synthesizing verification results into actionable issues
- Like a senior editor presenting fact-check findings, you organize problems by severity
- Clear issue identification helps authors prioritize corrections
- You present problems with specific, actionable corrections

### Step-Specific Rules:
- Collect all issues from dossier contradictions and web verifications
- Assess severity based on credibility impact
- Prepare specific corrections for each issue
- Organize issues by severity for easy prioritization
- Auto-proceed after issue identification

## EXECUTION PROTOCOLS:
- Compile all contradicted claims from previous steps
- Assess severity (HIGH/MEDIUM/LOW) based on predefined criteria
- Develop specific corrections for each issue
- Organize issues by severity level
- Prepare comprehensive issue list
- Auto-proceed to corrections step

## CONTEXT BOUNDARIES:
- Synthesizes results from Steps 3 (dossier contradictions) and 4 (web verifications)
- Updates output file with issue catalog
- Focus: Problem identification and correction preparation
- No user interaction in this step (that's Step 6)

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Issue Identification Phase

"**🔍 Identifying Issues...**

I'm now synthesizing all verification results to identify factual and technical issues. Let me compile the problems found, assess their severity, and prepare specific corrections."

### 2. Compile All Issues

**See:** `data/procedures/issue-identification.md` for complete issue compilation process

**Collect from:**
- Step 3 (Reference Check): Claims contradicted by research dossiers
- Step 4 (Web Verification): Claims contradicted by web sources

**Use issue template from:** `data/issue-template.md`

### 3. Assess Severity

**See:** `data/references/severity-classification.md` for complete severity assessment criteria

**Quick reference:**
- **HIGH:** Breaks credibility, factual impossibility, readers will definitely notice
- **MEDIUM:** Stretches believability, minor inaccuracies, some might notice
- **LOW:** Minor nitpicks, polish-level, doesn't affect credibility
- **INFO:** Verified accurate, builds confidence

### 4. Develop Corrections

**See:** `data/references/correction-development.md` for complete correction guidelines

**Quick reference:** Be specific, offer 2-3 options, respect story context, minimize disruption

### 5. Organize Issues by Severity

**See:** `data/procedures/issue-identification.md` for complete organization strategy

**Sort:** HIGH → MEDIUM → LOW, grouped by category, ordered by chapter/scene

### 6. Prepare Verified Facts Summary

**See:** `data/procedures/issue-identification.md` for verified facts compilation process

### 7. Update Output File

**See:** `data/templates/issues-identified-template.md` for complete output format

**Key elements:**
- Issue summary table by severity and category
- Detailed issue lists (HIGH, MEDIUM, LOW)
- Verified facts summary
- Verification statistics
- Frontmatter updates with completion status

### 8. Present Issue Summary

Display:

"**✅ Issue Identification Complete**

### Issues Found: {total}

**Must Fix (HIGH):** {H-total}
- Technical: {H-tech} | Factual: {H-fact} | Logical: {H-logic}

**Should Address (MEDIUM):** {M-total}
- Technical: {M-tech} | Factual: {M-fact} | Logical: {M-logic}

**Optional Polish (LOW):** {L-total}
- Technical: {L-tech} | Factual: {L-fact} | Logical: {L-logic}

### Verified Accurate: {verified}

Claims confirmed correct through research dossiers and web verification.

### Most Critical Issues

{list of 2-3 most severe issues with brief descriptions}

**Now preparing comprehensive corrections and recommendations...**""

### 9. Auto-Proceed to Corrections

**AUTOMATIC PROCEED:**
Update {outputFile} frontmatter with stepsCompleted: ['step-01-select-scope', 'step-02-extract-claims', 'step-03-check-references', 'step-04-web-verification', 'step-05-identify-issues', 'step-06-provide-corrections'], lastStep: 'step-06-provide-corrections', then load, read entire file, then execute {nextStepFile}

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- All issues from dossier contradictions and web verifications compiled
- Severity assessments applied based on credibility impact criteria
- Specific corrections prepared for each issue
- Issues organized by severity for prioritization
- Verified facts summarized separately
- Output file updated with comprehensive issue catalog
- Clear statistics presented
- Auto-proceed to corrections step

### SYSTEM FAILURE:
- Not compiling all issues from previous steps
- Not assessing severity for each issue
- Not preparing specific corrections
- Not organizing issues by severity
- Missing verified facts summary
- Not providing actionable recommendations
- Proceeding without presenting summary

**Master Rule:** Clear issue identification with severity assessment and specific corrections is the core value of reality checking. Every problem found must be presented with context, evidence, severity, and actionable solutions. Issues must be organized by severity so authors can prioritize fixes. Verified facts should be celebrated — they build confidence in the story's accuracy.
