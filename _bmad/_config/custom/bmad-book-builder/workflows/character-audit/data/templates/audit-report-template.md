# Character Audit Report Template

## Report Structure

This template defines the format for character audit reports, following AgentAdam's audit methodology enhanced with BBB's systematic approach.

---

```markdown
# Audit - Chapter {chapter_number} - {character_name}

**Date:** {date}
**Auditor:** Marie, Character Keeper (Bible Guardian)
**Status:** {finalAssessment.overall}

---

## Appearance in This Chapter

**Presence:** {character appears: YES/NO}
**Scenes:** [list of scenes if character appears]
**Key Actions:** [list key actions]
**Dominant Emotions:** [list dominant emotions]

---

## Psychological Coherence

### Contradictions Checked

| # | Contradiction | Type | Result |
|---|---------------|------|--------|
| 1 | [description] | [type] | ✅/❌/⚪ |
| 2 | [description] | [type] | ✅/❌/⚪ |
| 3 | [description] | [type] | ✅/❌/⚪ |
| 4 | [description] | [type] | ✅/❌/⚪ |
| 5 | [description] | [type] | ✅/❌/⚪ |

**Contradictions Coherence Score:** {contradictionsScore}%

**Details of Incoherent Contradictions ❌:**
[If any: List each with detailed explanation and evidence]
[If none: No incoherence detected!]

**Details of Untested Contradictions ⚪:**
[If any: List and explain why not applicable]

### Psychological Dimensions

| Dimension | Result | Notes |
|-----------|--------|-------|
| Emotional State | ✅/⚠️/❌ | [brief] |
| Behavior Patterns | ✅/⚠️/❌ | [brief] |
| Voice Consistency | ✅/⚠️/❌ | [brief] |
| Decision Logic | ✅/⚠️/❌ | [brief] |

**Psychological Assessment:** {psychologicalScore}

---

## Arc Evolution

**State at Chapter Beginning:**
{arcProgression.before}

**State at Chapter End:**
{arcProgression.after}

**Transformation:** {hasTransformation: YES/NO}
{If YES: transformation moment details}

**Arc Progression:** {arcProgression.alignment}
{Detailed assessment}

**Current Phase:** {currentPhase}/5 {if applicable}

**Anticipated Next Step:**
{arcProgression.nextSteps}

---

## Issues Identified

**Problem Criteria:**
- ❌ Incoherent contradiction
- ❌ Incoherent psychological dimension
- ❌ Arc regression
- ⚠️ Significant shift requiring attention

### Issues Detected

**{IF criticalIssues > 0:}**

**HIGH Priority:**
1. [Problem 1 - detailed description]
2. [Problem 2 - detailed description]

**MEDIUM Priority:**
3. [Problem 3 - detailed description]

**{ELSE:}**
✅ **No critical issues detected!**

---

## Recommendations

**{FOR each recommendation in recommendations:}

### [Priority] - [Issue]

**{recommendation.suggestion}**

---

## Overall Assessment

**Contradictions Coherence Score:** {contradictionsScore}%
**Psychological Coherence:** {psychologicalScore}
**Arc Progression:** {arcScore}

**Final Assessment:** {finalAssessment.overall}

{IF excellent:}
✅ **EXCELLENT** — The character is coherent and their evolution is well managed in this chapter.

{IF acceptable:}
⚠️ **ACCEPTABLE** — Some points to improve. See recommendations above.

{IF problematic:}
❌ **PROBLEMATIC** — Significant incoherences have been detected. Revision is recommended.

---

*Audited by BMad Book Builder — Character Audit Workflow*
*Methodology based on AgentAdam*
```

---

## Report Generation Guidelines

### 1. Data Compilation

Gather all data from previous audit steps:

```yaml
allFindings:
  character:
    name: [from step 01]
    slug: [from step 01]
  chapter:
    number: [from step 02]
    file: [from step 02]
    appears: [from step 02]
  contradictions:
    checked: [from step 03]
    coherent: [count]
    incoherent: [count]
    na: [count]
    results: [detailed results]
  psychologicalCoherence:
    overall: [from step 04]
    dimensions: [all 4 ratings]
    issues: [if any]
  arcProgression:
    alignment: [from step 05]
    before: [chapter start state]
    after: [chapter end state]
    transformation: [if applicable]
    nextSteps: [anticipated]
```

### 2. Final Assessment Calculation

**Contradictions Score:**
- Formula: (Coherent / Total Checked) × 100
- Rating: [Score]%
- Assessment:
  - 80-100%: ✅ EXCELLENT
  - 60-79%: ⚠️ ACCEPTABLE
  - < 60%: ❌ PROBLEMATIC

**Psychological Coherence Score:**
- Based on 4 dimensions from step 04
- Count ✅/⚠️/❌ ratings
- Overall: [EXCELLENT / ACCEPTABLE / PROBLEMATIC]

**Arc Progression Score:**
- Based on alignment from step 05
- Rating: [ON TRACK / SHIFT / REGRESSION / NEUTRAL]

**Overall Assessment:**
- If all ✅ or ON TRACK: ✅ **EXCELLENT**
- If any ⚠️ or SHIFT: ⚠️ **ACCEPTABLE**
- If any ❌ or REGRESSION: ❌ **PROBLEMATIC**

### 3. Critical Issues Identification

**Criteria:**
- ❌ Incoherent contradiction
- ❌ Incoherent psychological dimension
- ❌ Arc regression
- ⚠️ Significant shift requiring attention

**Priority Levels:**
- **HIGH:** Multiple ❌ marks or REGRESSION
- **MEDIUM:** Single ❌ or multiple ⚠️
- **LOW:** Minor ⚠️ issues

### 4. Recommendations Generation

**For Incoherent Contradictions:**
- "Review scenes where [contradiction] is violated. Consider: [suggestion]"

**For Problematic Psychological Dimensions:**
- "To improve [dimension]: [concrete suggestion]"

**For Arc Regression:**
- "Arc regression may be justified if: [context]. Otherwise, consider: [alternative]"

**For Excellent Results:**
- "Excellent coherence! Maintain this level for upcoming chapters."

**Storage Format:**
```yaml
recommendations:
  - priority: [high/medium/low]
    issue: [description]
    suggestion: [actionable recommendation]
```

### 5. File Output

**Location:** `{bbb_output_folder}/audits/audit-chapter-{chapter_number}-{character_slug}.md`

**Verification:**
- ✅ Report file created
- ✅ All sections populated
- ✅ All findings included
- ✅ Formatted according to template

### 6. User Summary

Present concise summary with:

- Character and chapter info
- Key scores (contradictions, psychological, arc)
- Overall assessment
- Critical issues count (if any)
- Top 2-3 recommendations
- Next steps options

---

## Master Rule

The audit report is the primary deliverable of this workflow. It must be:
- **Complete** — All findings included
- **Well-formatted** — Clear, professional structure
- **Actionable** — Specific recommendations for improvement
- **Preserved** — Saved as reference for future revisions

Authors will use this report to understand their character's psychological state and make informed revision decisions.
