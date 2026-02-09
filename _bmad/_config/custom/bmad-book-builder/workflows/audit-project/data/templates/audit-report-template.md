# Audit Report Template

## Frontmatter Template

```yaml
---
stepsCompleted: ['step-01-load-context', 'step-02-narrative-arc', 'step-03-coherence-check', 'step-04-quality-check', 'step-05-synthesize-reports', 'step-06-generate-report', 'step-07-present-findings']
lastStep: 'step-07-present-findings'
date: '{current_date}'
user_name: '{user_name}'
auditScope: '{auditScope}'
targetChapters: {targetChapters}
chaptersAnalyzed: {count}
overallHealthScore: {score}
narrativeArcHealthScore: {score}
coherenceHealthScore: {score}
qualityHealthScore: {score}
criticalIssuesCount: {count}
majorIssuesCount: {count}
minorIssuesCount: {count}
reportGenerationComplete: true
auditComplete: true
completionDate: '{current_date}'
presentedTo: '{user_name}'
---
```

## Report Header Template

```markdown
# Project Audit Report: {date}

> **Generated:** {date}
> **Auditor:** Continuity Editor (Claude)
> **Scope:** {auditScope} ({chapters_count} chapters, {word_count} words)
> **Report Location:** `{outputFile}`
> **Quick Access:** `{latestAuditLink}`

---

## Executive Summary

### Overall Project Health: {score}/100 — {label}

{Brief paragraph explaining overall project status and what this score means}

### Project Phase Assessment
{Assessment of current project phase based on completeness and quality}

### Critical Issues Requiring Immediate Attention

{Top 3-5 critical issues}

### Immediate Action Items

{Top 3 immediate actions}

---

```

## Health Scores Dashboard Template

```markdown
## Health Scores Dashboard

### Overall Project Health
**Score:** {score}/100 — {label}

### Dimension Health Scores

| Dimension | Health Score | Status | Key Issues |
|-----------|--------------|--------|------------|
| Narrative Arc | {score}/100 | {indicator} | {top 2 issues} |
| Coherence | {score}/100 | {indicator} | {top 2 issues} |
| Quality | {score}/100 | {indicator} | {top 2 issues} |
| Historical Progress | {score}/100 | {indicator} | {trend} |
| Data Currency | {score}/100 | {indicator} | {currency status} |

**Status Indicators:** ✅ Excellent (90-100) | 🟢 Good (75-89) | 🟡 Fair (60-74) | 🟠 Poor (40-59) | 🔴 Critical (0-39)

### Dimension Breakdown

**Narrative Arc Breakdown ({score}/100):**
- Story Structure: {score}/20 — {status}
- Arc Completion: {score}/20 — {status}
- Pacing Quality: {score}/20 — {status}
- Character Arc Progression: {score}/15 — {status}
- Setup/Payoff Validity: {score}/15 — {status}
- Transition Quality: {score}/10 — {status}

**Coherence Breakdown ({score}/100):**
- Character Consistency: {score}/30 — {status}
- Location Accuracy: {score}/20 — {status}
- Object Tracking: {score}/15 — {status}
- Timeline Validation: {score}/20 — {status}
- Plot Hole Absence: {score}/15 — {status}

**Quality Breakdown ({score}/100):**
- Style Consistency: {score}/20 — {status}
- Dialogue Quality: {score}/25 — {status}
- Prose Metrics: {score}/25 — {status}
- Thematic Coherence: {score}/20 — {status}
- Quality Patterns: {score}/10 — {status}

---

```

## Narrative Arc Analysis Section Template

```markdown
## Narrative Arc Analysis

**Health Score:** {score}/100 — {label}

### Story Structure
{Structure assessment with phases present, arc completion, alignment with plan}

**Narrative Phases Identified:**
- Exposition/Setup: {status} — {location}
- Inciting Incident: {status} — {location}
- Rising Action: {status} — {location}
- Climax: {status} — {location}
- Falling Action: {status} — {location}
- Resolution: {status} — {location}

**Arc Completion:** {percentage}% — {assessment}

### Pacing Assessment
{Overall pacing assessment with chapter-by-chapter pacing notes}

**Pacing Issues:**
- Rushed sections: {count} — {locations}
- Dragging sections: {count} — {locations}
- Pacing inconsistencies: {count} — {locations}

### Character Arc Progression
{Character arc completion assessment with specific character notes}

**Character Arc Status:**
- Complete arcs: {count} characters
- Incomplete arcs: {count} characters
- Stalled arcs: {count} characters

### Setup and Payoff
{Setup/payoff analysis with matched pairs, orphaned setups, unearned payoffs}

**Setup/Payoff Summary:**
- Matched pairs: {count}
- Orphaned setups: {count}
- Unearned payoffs: {count}

### Narrative Transitions
{Transition quality assessment with problematic transitions identified}

**Transition Issues:** {count} problematic transitions

### Key Findings
{Critical findings and recommendations for narrative arc improvement}

---

```

## Coherence Check Section Template

```markdown
## Coherence Check

**Health Score:** {score}/100 — {label}

### Character Consistency
{Character validation results with specific issues by character}

**Characters Validated:** {count}
- Consistent: {count}
- Issues found: {count}

**Issues by Character:**
{List of characters with consistency issues}

### Location Accuracy
{Location validation results with geographic and spatial issues}

**Locations Validated:** {count}
- Consistent: {count}
- Issues found: {count}

**Location Issues:**
{List of locations with accuracy issues}

### Object Tracking
{Object tracking results with presence and state inconsistencies}

**Objects Validated:** {count}
- Consistent: {count}
- Issues found: {count}

**Object Issues:**
{List of objects with tracking issues}

### Timeline Validation
{Timeline validation results with chronological issues}

**Timeline Status:** {assessment}
- Consistent: {status}
- Issues found: {count}

**Timeline Issues:**
{List of timeline inconsistencies}

### Plot Hole Detection
{Plot holes and narrative gaps with severity ratings}

**Issues by Severity:**
- Critical: {count}
- Major: {count}
- Minor: {count}

**Plot Holes and Gaps:**
{List of plot holes and narrative gaps}

### Coherence Issues Summary
{Categorized list of all coherence issues found with severity and chapter references}

---

```

## Quality Assessment Section Template

```markdown
## Quality Assessment

**Health Score:** {score}/100 — {label}

### Style Consistency
{Style assessment with voice, tone, and register analysis}

**Style Elements:**
- Narrative voice: {assessment}
- Tone consistency: {assessment}
- Style register: {assessment}

**Issues found:** {count}

### Dialogue Quality
{Dialogue assessment with voice distinctiveness, naturalness, and subtext analysis}

**Dialogue Assessment:**
- Distinctive voices: {count}/{total} characters
- Naturalness: {assessment}
- Subtext quality: {assessment}
- Mechanics: {assessment}

**Issues found:** {count}

### Prose Metrics
{Prose analysis with vocabulary, sentence structure, readability, and show vs tell}

**Prose Scores:**
- Vocabulary variety: {score}/10
- Sentence variety: {score}/10
- Readability: {score}/10
- Show vs tell: {score}/10

**Issues found:** {count}

### Thematic Coherence
{Theme analysis with presence, progression, and symbol/motif tracking}

**Themes Identified:** {count}
- Well-developed: {count}
- Need development: {count}

**Symbol/Motif Tracking:**
{List of symbols and motifs with effectiveness assessment}

### Quality Patterns
{Recurring issues, strengths, and developmental trajectory}

**Recurring Issues:** {count}
- {Issue 1}
- {Issue 2}
- {Issue 3}

**Strengths to Maintain:** {count}
- {Strength 1}
- {Strength 2}
- {Strength 3}

**Quality Trajectory:** {direction}

### Quality Issues Summary
{Categorized list of all quality issues found with severity and chapter references}

---

```

## Historical Analysis Section Template

```markdown
## Historical Analysis Synthesis

### Review History
{Aggregated insights from all previous reviews with trends and patterns}

**Previous Reviews Analyzed:** {count}

**Trends:**
- Recurring issues: {count}
- Resolved issues: {count}
- New issues: {count}
- Quality trend: {direction}

### Character Audit Insights
{Synthesized character development data from all audits}

**Characters Audited:** {count}
- Strong progression: {count}
- Needs work: {count}
- Stalled: {count}

**Character Development Trends:**
{Analysis of character arc progression over time}

### Theme Tracking Data
{Theme progression and currency analysis}

**Theme Tracking Status:** {status}
- Themes tracked: {count}
- Currency: {status}
- Underdeveloped themes: {count}

### Rhythm Analysis Data
{Pacing and rhythm insights from tracking}

**Rhythm Tracking Status:** {status}
- Pacing findings: {count}
- Currency: {status}

### Systemic Patterns
{Cross-workflow pattern recognition with systemic issues and strengths}

**Systemic Issues Identified:** {count}
- {Pattern 1}
- {Pattern 2}
- {Pattern 3}

**Strength Patterns Identified:** {count}
- {Pattern 1}
- {Pattern 2}
- {Pattern 3}

### Data Currency Assessment
{Currency status of Living Bible, tracking, and audit data}

**Living Bible Currency:**
- Chronologie: {status}
- Lieux: {status}
- Objets: {status}
- Personnes: {status}
- Themes: {status}

**Tracking Data Currency:**
- Theme Tracking: {status}
- Rhythm Analysis: {status}

**Character Audit Currency:**
{List of characters with audit status}

### Progress Comparison
{Current vs. historical comparison with improvements and persistent concerns}

**Overall Progress:** {direction}
- Significant improvements: {count}
- Persistent concerns: {count}
- New issues: {count}

---

```

## Issue Catalog Template

```markdown
## Issue Catalog

### Critical Issues ({count}) — Must Fix Before Finalizing

{All critical issues from all dimensions}

**Format:**
- **[CRITICAL]** {Issue Title}
  - **Location:** Chapter X, {specific location}
  - **Dimension:** {dimension name}
  - **Description:** {detailed description}
  - **Impact:** {why this matters}
  - **Suggested Fix:** {actionable solution}

### Major Issues ({count}) — Should Fix Before Publishing

{All major issues from all dimensions, same format}

### Minor Issues ({count}) — Polish Before Final

{All minor issues from all dimensions, same format}

### Issues by Dimension

**Narrative Arc Issues:**
{List of all narrative arc issues with severity}

**Coherence Issues:**
- **Character Issues:** {list}
- **Location Issues:** {list}
- **Object Issues:** {list}
- **Timeline Issues:** {list}
- **Plot Holes:** {list}

**Quality Issues:**
- **Style Issues:** {list}
- **Dialogue Issues:** {list}
- **Prose Issues:** {list}
- **Theme Issues:** {list}

---

```

## Recommendations Template

```markdown
## Recommendations

### Priority 1: Critical Actions (Do First)

{Top 3-5 critical issues}

**Format:**
1. **{Action}**
   - Expected Outcome: {result}
   - Estimated Effort: {Low/Medium/High}
   - Impact: {High/Medium/Low}

### Priority 2: Major Improvements (Do Second)

{Top 5-10 major issues, same format}

### Priority 3: Polish and Refine (Do Last)

{Top 5-10 minor issues, same format}

### By Dimension

**Narrative Arc Improvements:**
{Specific recommendations for narrative arc}

**Coherence Improvements:**
- **Character:** {specific recommendation}
- **Location:** {specific recommendation}
- **Object:** {specific recommendation}
- **Timeline:** {specific recommendation}
- **Plot Holes:** {specific recommendation}

**Quality Improvements:**
- **Style:** {specific recommendation}
- **Dialogue:** {specific recommendation}
- **Prose:** {specific recommendation}
- **Themes:** {specific recommendation}

**Data Currency:**
{Specific recommendations for updating Living Bible and tracking}

---

```

## Appendix Template

```markdown
## Appendix

### Data Currency Status

**Living Bible Dimensions:**
- Chronologie: {status} — {details}
- Lieux: {status} — {details}
- Objets: {status} — {details}
- Personnes: {status} — {details}
- Themes: {status} — {details}

**Tracking Data:**
- Theme Tracking: {status} — {details}
- Rhythm Analysis: {status} — {details}

**Character Audits:**
{List of characters with audit status}

### Previous Reports Summary

**Review Reports:**
{Summary of previous reviews with dates and scopes}

**Character Audits:**
{Summary of character audits with dates and findings}

### Analysis Metadata

**Audit Scope:** {scope}
**Chapters Analyzed:** {count}
**Total Words:** {count}
**Analysis Date:** {date}
**Auditor:** Continuity Editor (Claude)
**Analysis Duration:** {duration if available}

**Report Generated:** {date}
**Report Version:** 1.0

---

*End of Audit Report*
```

## Presentation Summary Template

```markdown
## Presentation Summary

### 📊 EXECUTIVE SUMMARY

**Overall Project Health:** {score}/100 — {label}

{Brief paragraph}

### 🚨 Critical Issues ({count})

{Top 3-5 critical issues}

### ⚡ Immediate Actions

{Top 3 immediate actions}

### 🏥 Health Scores

| Dimension | Score | Status |
|-----------|-------|--------|
| Narrative Arc | {score}/100 | {indicator} |
| Coherence | {score}/100 | {indicator} |
| Quality | {score}/100 | {indicator} |
| Progress | {score}/100 | {indicator} |
| Data Currency | {score}/100 | {indicator} |

### 💪 Strengths ({count})

{List of top 5-10 strengths}

### ⚠️ Issues Requiring Attention

**Critical ({count}):** {summary}
**Major ({count}):** {summary}
**Minor ({count}):** {summary}

### 🎯 Next Steps

1. Address critical issues
2. Tackle major improvements
3. Polish minor issues
4. Update tracking data
5. Re-audit after changes

```

## Issue Entry Template

### Critical Issue Entry

```markdown
- **[CRITICAL]** {Issue Title}
  - **Location:** Chapter {N}, {scene/section if applicable}
  - **Dimension:** {Narrative Arc / Coherence / Quality}
  - **Subcategory:** {specific category}
  - **Description:** {Detailed description of the issue}
  - **Impact:** {Why this is critical and what damage it causes}
  - **Suggested Fix:** {Specific, actionable solution}
  - **Related Issues:** {If applicable, link to related issues}
```

### Major Issue Entry

```markdown
- **[MAJOR]** {Issue Title}
  - **Location:** Chapter {N}, {scene/section if applicable}
  - **Dimension:** {Narrative Arc / Coherence / Quality}
  - **Subcategory:** {specific category}
  - **Description:** {Detailed description of the issue}
  - **Impact:** {Why this matters and how it affects the story}
  - **Suggested Fix:** {Specific, actionable solution}
```

### Minor Issue Entry

```markdown
- **[MINOR]** {Issue Title}
  - **Location:** Chapter {N}, {scene/section if applicable}
  - **Dimension:** {Narrative Arc / Coherence / Quality}
  - **Subcategory:** {specific category}
  - **Description:** {Brief description of the issue}
  - **Suggested Fix:** {Quick fix suggestion}
```

## Completion Message Template

```markdown
**🎯 Audit Workflow Complete**

Thank you for completing the comprehensive project health audit.

Your manuscript has been thoroughly analyzed across {number} dimensions:
- Narrative arc and story structure
- Character, location, object, and timeline coherence
- Style, dialogue, prose quality, and thematic coherence
- Historical patterns and progress trends

**Key Takeaways:**
- Overall health: {score}/100 — {label}
- Critical issues to address: {count}
- Strengths to maintain: {count}

**Remember:** Writing is rewriting. Every issue identified is an opportunity to strengthen your story.

**Report saved:** `{outputFile}`
**Quick access:** `{latestAuditLink}`

Until next time, keep writing.

— Continuity Editor (Claude)
Quality & Coherence Specialist
```
