---
name: Report
description: Generate the rhythm analysis report
nextStepFile: null
---

# Step 04: Report

## Objective

Generate the rhythm analysis report and save it in the analysis folder.

---

## Instructions for the Agent

### 1. Prepare the Output Folder

Check/create the folder:
```
{project-root}/analysis/
```

### 2. Generate the Report

Use the `data/templates/report-template.md` template and fill it with analysis data.

**Sections to complete:**
1. Executive Summary - Summary and overall score
2. Pacing Analysis - Scene table and distribution
3. Tension Curve - ASCII visualization and key beats
4. Transitions Analysis - Table and score
5. Beat Mapping - Identified beats with functions
6. Flow Assessment - Flow evaluation
7. Action/Reflection Balance - Ratio and assessment
8. Recommendations - Critical, major, minor issues
9. Comparison - Metrics vs book average (if applicable)

> **Reference:** Evaluation criteria for each section are defined in the reference documents:
> - `data/references/pacing-analysis-framework.md` - for sections 2 and 7
> - `data/references/tension-mapping-procedures.md` - for section 3
> - `data/references/transition-analysis-guide.md` - for section 4
> - `data/references/beat-mapping-system.md` - for section 5
> - `data/references/flow-assessment-criteria.md` - for section 6

### 3. Determine the File Name

Based on scope:
- **Single chapter:** `rhythm-chapter-{N}.md`
- **Range:** `rhythm-chapters-{N}-to-{M}.md`
- **Full book:** `rhythm-full-{date}.md`

### 4. Write the Report

Use the Write tool to save:
```
{project-root}/analysis/{filename}
```

### 5. Display the Summary

Present key findings to the user:

```
═══════════════════════════════════════════════════════
     RHYTHM REPORT - Chapter {N}: "{title}"
═══════════════════════════════════════════════════════

📊 SCORE GLOBAL: {score}/10 - {health_status}

┌─────────────────────────────────────────────────────┐
│ MÉTRIQUES CLÉS                                      │
├─────────────────────────────────────────────────────┤
│ Pacing:      {score}/10  {bar}                      │
│ Tension:     {score}/10  {bar}                      │
│ Transitions: {score}/10  {bar}                      │
│ Flow:        {score}/10  {bar}                      │
└─────────────────────────────────────────────────────┘

🔴 CRITICAL ISSUES: {count}
{list_critical_issues}

🟡 POINTS OF ATTENTION: {count}
{list_important_issues}

🟢 STRENGTHS:
{list_strengths}

📁 Full report: analysis/{filename}
═══════════════════════════════════════════════════════
```

### 6. Action Recommendations

Based on findings, propose next steps:

**If critical issues:**
```
⚠️ I recommend addressing critical issues before continuing.
Would you like me to detail the suggested corrections?
```

**If healthy:**
```
✓ The rhythm of this chapter is solid!
Some minor adjustments are suggested in the full report.
```

**If scope = full book:**
```
Overall pacing overview complete.
Chapters {X, Y, Z} deserve special attention.
```

### 7. Suggest Related Workflows

```
Suggested workflows:
- [RA] Analyze another chapter
- [RE] Review - Full chapter revision
- [CW] Chapter-Write - Continue writing
```

---

## Final Validation

- [ ] Report generated and saved
- [ ] Summary displayed to the user
- [ ] Clear recommendations provided
- [ ] Next steps proposed

---

## Navigation

**Previous step:** [Step 03: Analyze](step-03-analyze.md)
**End of workflow**

---

## Output Produced

```
analysis/
└── rhythm-{scope}.md    # Full rhythm analysis report
```

---

## Closing Notes

- The report is self-contained and can be referenced later
- Scores are comparable across chapters to track trends
- Critical issues should be tracked to resolution
- This workflow can be re-run after changes to verify improvements
