---
name: 'step-03-analyze'
description: 'Perform sequential analysis of 6 review categories'

# Navigation
nextStepFile: './step-04-generate.md'

# Output
outputFile: '{bbb_output_folder}/review/review-report-{scope}.md'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 3: Analyze

## STEP GOAL:
To perform comprehensive sequential analysis across 6 categories (Character, Location, Object, Timeline, Plot Hole, Quality), identifying issues with severity classification and actionable corrections.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Continuity Editor** performing detailed coherence analysis
- Like a structural engineer examining a building for integrity issues
- You examine the story systematically across multiple dimensions
- Your goal: Find ALL issues, categorize by severity, suggest actionable fixes

### Step-Specific Rules:
- Perform analysis SEQUENTIALLY - one category at a time
- Focus on detection, classification, and correction suggestions
- FORBIDDEN to skip categories or perform parallel analysis
- Use Style Coach as sub-agent ONLY for Category 6 (Quality)
- Party Mode available for alternative perspectives on complex issues

## EXECUTION PROTOCOLS:
- Analyze categories 1-5 as Continuity Editor
- For Category 6 (Quality), decide if Style Coach sub-agent needed
- Classify every issue by severity: Critical/Major/Minor
- Provide specific location references for each issue
- Suggest actionable corrections for each issue
- Store results in structured format for report generation

## CONTEXT BOUNDARIES:
- Has access to ALL loaded context from step 2
- Chapter content, Living Bible 5D, summaries, style profile all available
- Previous reviews available for regression check
- Focus: Issue detection and classification, not report generation

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

**Reference:** `../data/analysis-procedures/` contains detailed procedures for each category.
**Reference:** `../data/classification-rules/severity-classification.md` contains complete severity guidelines.

### 1. Announce Analysis Phase

"**Beginning Comprehensive Analysis...**

I'll now systematically examine your chapter(s) across 6 categories of narrative coherence and quality.

Analysis in progress...
[Progress indicator displayed during analysis]"

### 2. Category 1: Character Consistency
See: `../data/analysis-procedures/character-analysis.md`

### 3. Category 2: Location Accuracy
See: `../data/analysis-procedures/location-analysis.md`

### 4. Category 3: Object Tracking
See: `../data/analysis-procedures/object-analysis.md`

### 5. Category 4: Timeline Validation
See: `../data/analysis-procedures/timeline-analysis.md`

### 6. Category 5: Plot Hole Detection
See: `../data/analysis-procedures/plot-hole-analysis.md`

### 7. Category 6: Quality Issues

**Decision Point: Sub-Agent Usage**

Check if `style_profile` is loaded:
- **IF available (not null):** Consider using Style Coach as sub-agent for deeper quality analysis
- **IF null:** Perform basic quality checks without sub-agent

**Analysis Scope:**
- Repetitive phrasing or patterns
- Dialogue that sounds out of character
- Scenes that lack purpose or tension
- Pacing problems (too fast/slow)
- Show-don't-tell violations
- Weak prose or awkward constructions

**Analysis Process (WITH Style Profile):**

Option A - Use Style Coach sub-agent:
1. Prepare brief context for Style Coach: target chapters, style profile metrics
2. Invoke Style Coach with specific quality focus
3. Receive quality issues report
4. Integrate into overall analysis

Option B - Perform basic checks:
1. Scan for repetitive phrasing patterns
2. Check scene pacing and tension
3. Validate dialogue against character voice
4. Identify weak prose constructions

**Severity Classification:**
- **Critical**: Systemic quality issue affecting multiple scenes (e.g., repetitive dialogue throughout)
- **Major**: Quality issue affecting one scene significantly
- **Minor**: Localized quality issue

**Output Format:**
```yaml
quality_issues:
  - quality_reference: "Description of quality issue"
    issue_description: "Clear description of problem"
    location_reference: "Chapter X, Scene Y"
    severity: "Critical|Major|Minor"
    suggested_fix: "Specific actionable correction"
```

**Progress Update:**
"✅ **Category 6 Complete:** Quality Issues — {count} issues found"

### 8. Compile Analysis Summary

Tally all issues across categories:
```yaml
totalIssues: {sum}
criticalIssues: {count}
majorIssues: {count}
minorIssues: {count}
issuesByCategory:
  character_consistency: {count}
  location_accuracy: {count}
  object_tracking: {count}
  timeline_validation: {count}
  plot_hole_detection: {count}
  quality_issues: {count}
```

### 9. Regression Check (If Previous Reviews Available)

If `previous_reviews` is not empty:
1. Check if any issues from previous reviews recur
2. Note: "Recurring issue from previous review: {issue}"
3. Flag recurring issues for priority attention

### 10. Present Analysis Results

Display:

"**Analysis Complete!**

### Summary

| Metric | Count |
|--------|-------|
| **Total Issues** | {total} |
| **Critical** | {critical} — Must fix before finalizing |
| **Major** | {major} — Should fix before publishing |
| **Minor** | {minor} — Polish before final |

### Issues by Category

| Category | Critical | Major | Minor | Total |
|----------|----------|-------|-------|-------|
| Character Consistency | {count} | {count} | {count} | {total} |
| Location Accuracy | {count} | {count} | {count} | {total} |
| Object Tracking | {count} | {count} | {count} | {total} |
| Timeline Validation | {count} | {count} | {count} | {total} |
| Plot Hole Detection | {count} | {count} | {count} | {total} |
| Quality Issues | {count} | {count} | {count} | {total} |

{regression_note if applicable}

{if no issues: **🎉 Excellent! No issues found. Your chapter(s) demonstrate strong narrative coherence and quality.**}

**Analysis data compiled. Ready to generate report.**"

**Select an Option:** `[P] Party Mode - Alternative Perspectives` `[C]` Continue to Report Generation

### MENU HANDLING LOGIC:

- IF P: Execute {partyModeWorkflow} with context: "Review these {total} issues found across {count} categories. Provide alternative perspectives or suggest additional issues we may have missed.", and when finished redisplay the menu
- IF C: Store all analysis results in memory for step 4, update {outputFile} frontmatter with stepsCompleted: ['step-01-init', 'step-02-load', 'step-03-analyze'], lastStep: 'step-03-analyze', then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- All 6 categories analyzed sequentially
- Every issue categorized by severity (Critical/Major/Minor)
- Specific location references provided for each issue
- Actionable corrections suggested for each issue
- Analysis summary compiled with accurate counts
- Regression check performed if previous reviews available

### SYSTEM FAILURE:
- Skipping categories or analyzing out of sequence
- Not providing severity classification
- Not providing location references
- Not suggesting actionable corrections
- Using parallel sub-processes instead of sequential analysis

**Master Rule:** Sequential analysis is critical for consistency and cost-effectiveness. Each category builds on the same shared context. Every issue must be classified and have an actionable fix suggestion.
