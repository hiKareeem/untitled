# Issues Identified Output Template for Step 5

## Output Format

**Append to {outputFile}:**

```markdown
## Issues Identified

### Issue Summary

**Total Issues Found:** {total}

| Severity | Technical | Factual | Logical | Total |
|----------|-----------|---------|---------|-------|
| **HIGH** | {H-tech} | {H-fact} | {H-logic} | {H-total} |
| **MEDIUM** | {M-tech} | {M-fact} | {M-logic} | {M-total} |
| **LOW** | {L-tech} | {L-fact} | {L-logic} | {L-total} |
| **TOTAL** | **{tech}** | **{fact}** | **{logic}** | **{total}** |

---

## HIGH Severity Issues ({H-total})

> **Must Fix:** These issues break story credibility and will definitely be noticed by readers.

{list each HIGH severity issue with full details: location, claim, problem, evidence, severity, corrections, impact}

---

## MEDIUM Severity Issues ({M-total})

> **Should Address:** These issues stretch believability and some readers will notice.

{same structure as HIGH issues}

---

## LOW Severity Issues ({L-total})

> **Optional Polish:** These are minor nitpicks for perfectionist revision.

{same structure as HIGH issues, but shorter}

---

## Verified Facts

Claims that were verified as accurate through research dossiers or web verification.

{list verified facts by category with sources and verification notes}

---

## Verification Statistics

**Total Claims Analyzed:** {total_claims}
**Issues Found:** {total_issues} (HIGH: {H-total}, MEDIUM: {M-total}, LOW: {L-total})
**Verified Accurate:** {total_verified}
**Partially Accurate/Needs Clarification:** {partial_count}

**Verification Sources:**
- Research Dossiers Consulted: {dossier_count}
- Web Searches Performed: {search_count}
- Web Sources Consulted: {source_count}

---

## Issue Identification Complete

All issues have been identified with severity assessments and correction suggestions. Ready to present findings and recommendations.

---
```

## Frontmatter Updates

**Update {outputFile} frontmatter:**

```yaml
---
stepsCompleted: ['step-01-select-scope', 'step-02-extract-claims', 'step-03-check-references', 'step-04-web-verification', 'step-05-identify-issues']
lastStep: 'step-05-identify-issues'
issuesFound: {total}
highSeverityIssues: {H-total}
mediumSeverityIssues: {M-total}
lowSeverityIssues: {L-total}
verifiedClaims: {total_verified}
issueIdentificationComplete: true
---
```
