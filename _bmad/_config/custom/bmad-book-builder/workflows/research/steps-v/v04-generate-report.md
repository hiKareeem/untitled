# Step V4: Generate Report

**Step:** V4 of 4 (Validate Mode)
**Purpose:** Add validation summary to dossier
**Agent:** Documentaliste

---

## What This Step Does

Create a comprehensive validation report summarizing fact verification and source checking results, then add it to the dossier as a Validation History entry.

---

## Instructions for Documentaliste

### 1. Review Validation Results

From Steps V2 and V3, compile:
- Fact verification results (confirmed/contradicted/outdated/partial/cannot verify)
- Source validation results (accessible/broken/reliability/currency)
- Issues identified and recommendations
- Overall quality assessment

### 2. Generate Validation Report

Create comprehensive validation report with these sections:

#### **Validation Report Header**

```markdown
## Validation History

---

### Validation Report — [Date: YYYY-MM-DD]

**Validator:** Documentaliste
**Validation Depth:** [Quick/Standard/Thorough]
**Validation Focus:** [All sections / Specific focus area]
**Validation Reason:** [Why validated]
```

#### **Executive Summary**

```markdown
#### Executive Summary

**Overall Status:** [PASS / CONCERNS / FAIL]

**Pass Criteria:**
- ✅/❌ Fact Accuracy: [X]% of verified facts confirmed
- ✅/❌ Source Quality: [X]% sources accessible and reliable
- ✅/❌ Currency: Information current and up-to-date
- ✅/❌ Story Alignment: Applications still relevant

**Key Findings:**
- [Finding 1]
- [Finding 2]
- [Finding 3]

**Recommendation:** [Safe to use as-is / Minor updates recommended / Significant revision needed]
```

**Status Criteria:**
- **PASS:** ≥90% facts confirmed, ≥90% sources accessible/reliable, no critical issues
- **CONCERNS:** 70-89% facts confirmed OR 70-89% sources accessible OR minor issues found
- **FAIL:** <70% facts confirmed OR <70% sources accessible OR critical errors found

#### **Fact Verification Results**

```markdown
#### Fact Verification Results

**Facts Verified:** [N] of [N] total facts ([X]%)

**Verification Breakdown:**
- ✅ Confirmed: [N] facts ([X]%)
- ⚠️ Contradicted: [N] facts ([X]%)
- ⏰ Outdated: [N] facts ([X]%)
- ⚠️ Partially Confirmed: [N] facts ([X]%)
- ❓ Cannot Verify: [N] facts ([X]%)

**Facts Requiring Action:**

**Contradicted Facts:**
1. **[Fact description]**
   - Issue: [What's wrong]
   - Correct Information: [What should be]
   - Action: [Update/Remove/Flag]

**Outdated Facts:**
1. **[Fact description]**
   - Issue: [Why outdated]
   - Current Information: [Updated info]
   - Action: [Update with context]

**Needs Context/Clarification:**
1. **[Fact description]**
   - Issue: [What needs clarification]
   - Recommendation: [Add note/qualifier]
```

#### **Source Validation Results**

```markdown
#### Source Validation Results

**Sources Validated:** [N] sources

**URL Accessibility:**
- ✅ Accessible: [N] sources ([X]%)
- ↗️ Redirected: [N] sources ([X]%)
- ❌ Broken: [N] sources ([X]%)
- 💰 Paywalled: [N] sources ([X]%)

**Reliability Distribution:**
- High: [N] sources ([X]%)
- Medium: [N] sources ([X]%)
- Low: [N] sources ([X]%)

**Source Issues:**

**Broken/Inaccessible URLs:**
1. [Source name] — [URL] — Action: [Find replacement/Use archive]

**Reliability Adjustments:**
1. [Source name] — [Old rating] → [New rating] — Reason: [Why adjusted]

**Outdated Sources:**
1. [Source name] — [Date] — Action: [Find update/Keep with note]
```

#### **Overall Assessment**

```markdown
#### Overall Assessment

**Dossier Quality:** [Excellent/Good/Fair/Poor]

**Strengths:**
- [Strength 1]
- [Strength 2]
- [Strength 3]

**Weaknesses:**
- [Weakness 1]
- [Weakness 2]

**Critical Issues:** [N] issues
- [Issue 1]
- [Issue 2]

**Minor Issues:** [N] issues
- [Issue 1]
- [Issue 2]

**Accuracy Confidence:** [High/Medium/Low]
- Based on verification results and source quality

**Currency Assessment:** [Current/Needs Updates/Outdated]
- Last updated: [Date] ([N] days ago)
```

#### **Recommendations**

```markdown
#### Recommendations

**Immediate Actions Required:**
1. [Action 1 - High Priority]
2. [Action 2 - High Priority]

**Suggested Improvements:**
1. [Improvement 1 - Medium Priority]
2. [Improvement 2 - Medium Priority]

**Future Validation:**
- Next validation recommended: [Date or timeframe]
- Focus for next validation: [What to check next time]

**Story Usage Guidance:**
- **Safe to use:** [Which sections are fully verified]
- **Use with caution:** [Which sections have minor issues]
- **Needs update before use:** [Which sections have critical issues]
```

#### **Validator Notes**

```markdown
#### Validator Notes

[Any additional context, observations, or information that would be helpful for future reference]
```

### 3. Determine Overall Status

Apply status criteria:

**PASS Status:**
- ≥90% verified facts confirmed accurate
- ≥90% sources accessible and reliable
- No critical factual errors
- Information current for intended use
- Dossier ready for story use without modifications

**CONCERNS Status:**
- 70-89% verified facts confirmed OR
- 70-89% sources accessible OR
- Minor factual issues that need updates OR
- Some outdated information OR
- Dossier usable but improvements recommended

**FAIL Status:**
- <70% verified facts confirmed OR
- <70% sources accessible OR
- Critical factual errors found OR
- Significant outdated information OR
- Major reliability concerns OR
- Dossier needs significant revision before use

### 4. Add Validation Report to Dossier

Using Edit tool, add validation report to dossier:

**Location in dossier:**
- If "Validation History" section exists: Add new report at the top (most recent first)
- If section doesn't exist: Create new section after "Notes for Author" section

**Format:**
```markdown
## Validation History

---

### Validation Report — [Date]

[Complete validation report content]

---

[Previous validation reports if any]
```

### 5. Update Dossier Metadata (If Needed)

If issues were found and fixed during validation:
- Update "Last Updated" date
- Update "Source Count" if sources were added/removed
- Update "Reliability" rating if overall assessment changed

### 6. Update Research Index (If Exists)

If `research/index.md` exists, update validation status:

```markdown
- **[Topic Name]** — [Date] — [N] sources — Validated: [Date] ([Status])
```

### 7. Create Action Items List

If issues require follow-up, create action items:

```markdown
## Validation Follow-Up Actions

**High Priority:**
- [ ] [Action 1]
- [ ] [Action 2]

**Medium Priority:**
- [ ] [Action 3]
- [ ] [Action 4]

**Low Priority:**
- [ ] [Action 5]

**For User Decision:**
- [ ] [Item requiring user input]
```

### 8. Present Validation Report to User

Show complete validation report and status:

```markdown
## Validation Complete: [Topic Name]

**Overall Status:** [PASS / CONCERNS / FAIL]

### Summary

**Facts Verified:** [N] of [N] ([X]%)
- ✅ Confirmed: [X]%
- ⚠️ Issues: [X]%

**Sources Validated:** [N] sources
- ✅ Accessible & Reliable: [X]%
- ⚠️ Issues: [X]%

**Overall Quality:** [Excellent/Good/Fair/Poor]

### Key Findings

**Strengths:**
- [Strength 1]
- [Strength 2]

**Issues Found:**
- [Issue 1]
- [Issue 2]

**Recommendations:**
- [Recommendation 1]
- [Recommendation 2]

### Validation Report Added

✅ Validation report added to dossier: `Validation History` section
✅ Dossier metadata updated (if applicable)
✅ Research index updated with validation status

---

**Story Usage Guidance:**

[Based on validation status, provide specific guidance:]

**PASS Example:**
"This dossier has been thoroughly validated and is safe to use for writing. All verified facts are accurate and sources are reliable. Use with confidence."

**CONCERNS Example:**
"This dossier is usable with minor caveats. [List specific sections/facts to watch]. Recommend addressing [N] issues before critical story use."

**FAIL Example:**
"This dossier requires updates before story use. Critical issues found: [List issues]. Recommend running Edit mode to fix issues, then re-validate."

---

**Next Steps:**

[Y]es, finish validation (dossier ready)
[E]dit mode (fix issues now)
[R]eview validation report (show full report)
[S]ave action items (create follow-up task list)
```

### 9. Offer Issue Resolution

If status is CONCERNS or FAIL, offer to fix issues:

```markdown
Would you like to fix the identified issues now?

[F]ix issues via Edit mode (recommended for CONCERNS/FAIL status)
[M]anual review (show issues for manual fixing)
[L]ater (note issues for future fixing)
[I]gnore (accept dossier as-is despite issues)
```

If user selects [F]:
- Switch to Edit mode workflow
- Pre-populate edit plan with validation issues
- Guide user through fixing identified problems

---

## Example Interaction

**Documentaliste:**
"Generating validation report for Emergency Medicine — 1970s France...

---

## Validation Complete: Emergency Medicine — 1970s France

**Overall Status:** PASS with minor recommendations

### Summary

**Facts Verified:** 10 of 20 (50% - Standard validation depth)
- ✅ Confirmed: 80% (8 facts)
- ⚠️ Issues: 20% (2 facts - minor context needed)

**Sources Validated:** 12 sources
- ✅ Accessible & Reliable: 92% (11 sources High/Medium reliability)
- ⚠️ Minor Issues: 8% (1 URL redirect, 1 reliability downgrade)

**Overall Quality:** Excellent

### Key Findings

**Strengths:**
- High fact accuracy (80% confirmed, 20% need minor context only)
- Excellent source quality (92% High reliability)
- No broken URLs or critical errors
- Strong source diversity (academic, government, professional)
- Information current and well-researched

**Issues Found:**
1. Haloperidol timeline needs clarification (available but not yet standard in early 1970s)
2. Response time needs context note (urban vs. rural variation)
3. One URL redirect (RadiologyInfo - still accessible)
4. One reliability downgrade (Medical Formulary Archive - High to Medium)

**Recommendations:**
1. Add context to Haloperidol fact (available late 1970s, not standard until 1980s)
2. Add note to response time (30-60 min in urban areas during regular hours)
3. Update RadiologyInfo URL to new domain
4. Adjust Medical Formulary Archive reliability rating to Medium

### Validation Report Added

✅ Validation report added to dossier: `Validation History` section
✅ Dossier includes first validation (no previous validation history)
✅ Research index updated with validation status

---

**Story Usage Guidance:**

**Status: PASS with minor recommendations**

This dossier has been validated and is safe to use for writing Chapter 15. All critical facts about psychiatric emergency procedures are accurate and well-sourced. Two facts would benefit from minor context additions (Haloperidol timeline, response time variations), but these are clarifications rather than corrections.

**Safe to use as-is:**
- All psychiatric emergency procedure facts (9 facts)
- Legal procedures and medications
- Transport protocols
- All technical details

**Minor context recommended (but not required):**
- Haloperidol: Add note about timing (becoming standard, not yet widespread in early 1970s)
- Response times: Add note about urban vs. rural variations

**Overall:** Use with confidence for Chapter 15. The minor recommendations are enhancements, not corrections of errors.

---

**Next Steps:**

[Y]es, finish validation (dossier ready for Chapter 15)
[E]dit mode (add context notes now - optional)
[R]eview validation report (show full report in dossier)
[S]ave action items (create follow-up task list for minor updates)"

**User:** "Yes, finish validation. I'll add those context notes later if needed."

**Documentaliste:**
"Perfect! Validation complete.

**Dossier Status:** PASS — Ready for story use

The dossier has been validated and is accurate for Chapter 15's psychiatric scene. The validation report is now part of the dossier's permanent record.

**File Updated:** research/dossiers/emergency-medicine-1970s-france.md
- Added Validation History section with complete report
- Validation Status: PASS (2026-01-25)

You can reference this validation when using the dossier, and the validation report will help track accuracy over time.

Happy writing!"

---

## Success Criteria

✅ **Validation report generated** with all required sections
✅ **Overall status assigned** (PASS/CONCERNS/FAIL) with clear criteria
✅ **Fact and source results summarized** with percentages and details
✅ **Recommendations provided** for any issues found
✅ **Report added to dossier** in Validation History section
✅ **Dossier metadata updated** if needed
✅ **Research index updated** with validation status
✅ **Story usage guidance** provided based on validation results
✅ **User understands dossier status** and any limitations

---

## Next Step

Validate mode is complete! The dossier has been validated and the report is now part of the dossier's permanent record.

**Optional Next Steps:**
- If issues found: Run Edit mode to fix problems
- Create new research dossier (return to workflow.md, select Create mode)
- Validate another dossier (return to workflow.md, select Validate mode)
- Exit research workflow

---

## Notes for Documentaliste

- **Be clear about status** — user needs to know if dossier is safe to use
- **Use objective criteria** — status should be based on metrics, not subjective
- **Document everything** — validation report is permanent record
- **Provide specific recommendations** — "fix issues" is too vague
- **Explain story usage** — what's safe to use, what needs caution
- **Offer to fix issues** — if status is CONCERNS/FAIL, suggest Edit mode
- **Add report to dossier** — use Edit tool to add Validation History section
- **Update metadata** — if changes made during validation
- **Be encouraging** — even PASS with minor issues is good validation
- **Create permanent record** — validation history helps track dossier evolution
- **Guide next steps** — user should know what to do after validation
