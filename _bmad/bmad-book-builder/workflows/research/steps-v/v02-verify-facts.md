# Step V2: Verify Facts

**Step:** V2 of 4 (Validate Mode)
**Purpose:** Spot-check key facts for accuracy
**Agent:** Documentaliste

---

## What This Step Does

Use web research to independently verify facts from the dossier, checking for accuracy, currency, and contradictions.

---

## Instructions for Documentaliste

### 1. Review Validation Plan

From Step V1, retrieve:
- Validation depth (quick/standard/thorough)
- Focus areas (which sections/facts to prioritize)
- Total fact count
- Dossier content

### 2. Select Facts for Verification

Based on validation depth, determine which facts to verify:

**Quick Validation:**
- Select 3-5 critical facts (focus on story-critical information)
- Prioritize facts marked ⚠️ or with low reliability sources
- Include at least 1 fact from each major category

**Standard Validation:**
- Select 50% of facts across all categories
- Include all facts in focus area (if specified)
- Prioritize facts marked ⚠️, technical details, and story-critical information
- Distribute across categories proportionally

**Thorough Validation:**
- Verify ALL facts in dossier
- Start with focus area, then proceed systematically
- Include all technical details and common misconceptions

### 3. Create Verification Checklist

Present checklist to user before starting:

```markdown
## Fact Verification Checklist

**Validation Depth:** [Quick/Standard/Thorough]
**Total Facts in Dossier:** [N] facts
**Facts to Verify:** [N] facts ([X]% of dossier)

### Facts Selected for Verification

**[Category 1 Name]:** [N] facts to verify
- [ ] Fact 1: [Brief description]
- [ ] Fact 2: [Brief description]

**[Category 2 Name]:** [N] facts to verify
- [ ] Fact 3: [Brief description]
- [ ] Fact 4: [Brief description]

**[Focus Area - if specified]:** [N] facts to verify
- [ ] Fact 5: [Brief description]
- [ ] Fact 6: [Brief description]

**Technical Details:** [N] items to verify
**Common Misconceptions:** [N] items to verify

---

**Ready to begin verification?** [Y]es / [M]odify fact selection
```

### 4. Conduct Independent Verification

For each selected fact:

**a) Retrieve fact from dossier**
- Note the fact description
- Note the original source cited
- Note the reliability rating

**b) Conduct independent web research**
- Search for the fact using different search terms
- Look for alternative sources (not the original source)
- Check multiple sources (aim for 2-3 confirmations)
- Note if information has changed or been updated

**c) Compare findings**
- Does independent research confirm the fact?
- Are there contradictions or updates?
- Is the fact still current?
- Is there additional context missing?

**d) Assess verification result**
```yaml
verification_results:
  - fact: "Fact description"
    original_source: "URL from dossier"
    original_reliability: "High/Medium/Low"
    verification_status: "confirmed/contradicted/outdated/partially_confirmed/cannot_verify"
    verification_sources:
      - url: "Alternative source 1"
        reliability: "High/Medium/Low"
      - url: "Alternative source 2"
        reliability: "High/Medium/Low"
    findings: "What independent research found"
    recommendation: "keep_as_is/update/add_note/flag_for_correction/remove"
    notes: "Additional context or concerns"
```

### 5. Report Verification Progress

After verifying each fact, report status:

```markdown
✅ Verified: [Fact brief description]
- Status: [Confirmed/Contradicted/Outdated/Partial]
- Independent sources: [N] sources checked
- Result: [Summary of findings]
- Recommendation: [Keep/Update/Flag/Remove]
```

### 6. Handle Different Verification Results

**Confirmed Facts:**
```markdown
✅ **CONFIRMED:** [Fact description]
- Original source: [URL] — [Reliability]
- Verification: Confirmed by [N] independent sources
- Status: Accurate and current
- Recommendation: Keep as-is
```

**Contradicted Facts:**
```markdown
⚠️ **CONTRADICTED:** [Fact description]
- Original source: [URL] — [Reliability]
- Contradiction: [What independent sources say instead]
- Independent sources: [List sources]
- Reliability comparison: [Original vs new sources]
- Recommendation: [Update/Flag/Add note explaining contradiction]
```

**Outdated Facts:**
```markdown
⏰ **OUTDATED:** [Fact description]
- Original source: [URL] — [Date]
- Update: [What has changed]
- Current information: [What's accurate now]
- Independent sources: [List sources]
- Recommendation: Update with note about historical context
```

**Partially Confirmed Facts:**
```markdown
⚠️ **PARTIAL:** [Fact description]
- Original source: [URL]
- Confirmation: Part of fact confirmed, part contradicted/uncertain
- Details: [What's confirmed vs. what's not]
- Recommendation: Add qualifier or note about uncertainty
```

**Cannot Verify:**
```markdown
❓ **CANNOT VERIFY:** [Fact description]
- Original source: [URL or missing]
- Issue: Cannot find independent sources to confirm or deny
- Possible reasons: [Too specific, source unavailable, rare information]
- Recommendation: [Flag for user review / Mark as uncertain / Keep with caveat]
```

### 7. Verify Technical Details

For technical sections, pay special attention to:
- Procedures described step-by-step
- Measurements, quantities, specifications
- Technical terminology
- Time periods and dates
- Legal or regulatory information

```markdown
## Technical Detail Verification: [Procedure/Specification Name]

**Original Description:** [What dossier says]

**Verification:**
- [Step 1 / Detail 1]: ✅ Confirmed / ⚠️ Contradicted / ❓ Cannot verify
- [Step 2 / Detail 2]: ✅ Confirmed / ⚠️ Contradicted / ❓ Cannot verify

**Sources:** [List verification sources]
**Recommendation:** [Keep/Update/Add note]
```

### 8. Verify Common Misconceptions

For misconception items, verify both parts:
- Is the misconception actually common?
- Is the reality/correction accurate?

```markdown
## Misconception Verification: [Misconception topic]

**Misconception stated:** [What dossier says people get wrong]
- Verification: ✅ This is indeed a common misconception / ⚠️ Not actually common

**Reality/correction:** [What dossier says is true]
- Verification: ✅ Correction is accurate / ⚠️ Correction needs update

**Recommendation:** [Keep/Update/Remove]
```

### 9. Track Verification Statistics

Maintain running totals:

```markdown
## Verification Progress

**Facts Verified:** [N] of [N] ([X]%)

**Results Summary:**
- ✅ Confirmed: [N] facts
- ⚠️ Contradicted: [N] facts
- ⏰ Outdated: [N] facts
- ⚠️ Partially Confirmed: [N] facts
- ❓ Cannot Verify: [N] facts

**Issues Found:** [N] facts need attention
```

### 10. Present Verification Summary

After completing all fact verification:

```markdown
## Fact Verification Summary: [Topic Name]

**Verification Scope:**
- Total facts in dossier: [N]
- Facts verified: [N] ([X]%)
- Verification depth: [Quick/Standard/Thorough]

### Verification Results

**✅ Confirmed Facts:** [N] facts
- All information accurate and current
- No action needed

**⚠️ Issues Found:** [N] facts

**Contradicted Facts:** [N]
1. [Fact description] — [Issue summary]
2. [Fact description] — [Issue summary]

**Outdated Facts:** [N]
1. [Fact description] — [Update needed]
2. [Fact description] — [Update needed]

**Partially Confirmed:** [N]
1. [Fact description] — [Details]

**Cannot Verify:** [N]
1. [Fact description] — [Why cannot verify]

### Accuracy Assessment

**Overall Accuracy:** [High/Medium/Low]
- [X]% of verified facts confirmed accurate
- [X]% of verified facts have issues

**Dossier Currency:** [Current/Needs Updates/Outdated]
- Last updated: [Date]
- Information age: [N] days old

**Reliability Assessment:** [High/Medium/Low]
- Based on verification results and source quality

---

**Ready to proceed to source validation?**

[Y]es, check sources next
[R]eview findings (show specific facts)
[M]odify verification (check more facts)
```

---

## Example Interaction

**Documentaliste:**
"Beginning fact verification for Emergency Medicine — 1970s France...

## Fact Verification Checklist

**Validation Depth:** Standard
**Total Facts in Dossier:** 20 facts
**Facts to Verify:** 10 facts (50% of dossier)

### Facts Selected for Verification

**Psychiatric Emergency Procedures (Focus Area):** 9 facts to verify
- [ ] Physician authorization required for involuntary commitment
- [ ] Chlorpromazine standard medication for psychiatric emergencies
- [ ] Haloperidol used for acute agitation
- [ ] Regular ambulance used for cooperative patients
- [ ] Police involvement for violent cases
- [ ] Response time: 30-60 minutes for psychiatric consultation
- [ ] Documentation requirements for psychiatric emergencies
- [ ] Legal procedures: Article 3213-1 regulations
- [ ] Transport protocols differ from medical emergencies

**Emergency Room Equipment:** 1 fact to verify (sample)
- [ ] CT scanners introduced 1971 but not widespread until late 1970s

---

**Ready to begin verification?** [Y]es"

**User:** "Yes"

**Documentaliste:**
"Starting independent verification...

---

✅ Verified: Physician authorization required for involuntary commitment
- Status: Confirmed
- Independent sources: 3 sources (French legal archive, psychiatric care history, medical law reference)
- Result: Confirmed — Article 3213-1 of French public health code required physician certification
- Recommendation: Keep as-is

✅ Verified: Chlorpromazine standard medication
- Status: Confirmed
- Independent sources: 2 sources (pharmaceutical history, medical formulary)
- Result: Confirmed — Chlorpromazine (brand name Largactil in France) was first-line treatment
- Recommendation: Keep, consider adding French brand name

⚠️ **OUTDATED:** Haloperidol for acute agitation
- Original source: Medical formulary archive — Medium reliability
- Update: Haloperidol was available but not first-line until late 1970s; became standard in 1980s
- Current information: In early-mid 1970s, chlorpromazine was more common; haloperidol gaining use
- Independent sources: Pharmaceutical history database, Academic research on antipsychotic timeline
- Recommendation: Update with note: "Haloperidol was available but becoming standard; chlorpromazine more common in early-mid 1970s"

✅ Verified: Regular ambulance for cooperative patients
- Status: Confirmed
- Independent sources: 2 sources (SAMU operations, medical transport history)
- Result: Confirmed — standard ambulance used unless patient violent
- Recommendation: Keep as-is

✅ Verified: Police involvement for violent cases
- Status: Confirmed
- Independent sources: 2 sources (Police procedures, psychiatric transport protocols)
- Result: Confirmed — Police assisted with violent or dangerous patients
- Recommendation: Keep as-is

⏰ **NEEDS CONTEXT:** Response time 30-60 minutes
- Original source: Psychiatric services history
- Verification: Confirmed BUT needs clarification
- Finding: 30-60 minutes was typical, but could be longer in rural areas or overnight
- Recommendation: Add note: "in urban areas during regular hours; could be longer in rural areas or overnight"

✅ Verified: Documentation requirements
- Status: Confirmed
- Independent sources: 2 sources (Legal archive, medical procedures manual)
- Result: Confirmed — Detailed documentation required for involuntary commitment
- Recommendation: Keep as-is

✅ Verified: Article 3213-1 legal procedures
- Status: Confirmed
- Independent sources: 2 sources (French legal database, public health law archive)
- Result: Confirmed — Article 3213-1 governed involuntary psychiatric commitment in 1970s
- Recommendation: Keep as-is

✅ Verified: Transport protocols differ from medical emergencies
- Status: Confirmed
- Independent sources: 2 sources (Emergency services manual, psychiatric care protocols)
- Result: Confirmed — Different protocols, equipment, and personnel training
- Recommendation: Keep as-is

✅ Verified: CT scanners introduced 1971 but not widespread
- Status: Confirmed
- Independent sources: 3 sources (Radiology history, Medical technology timeline, Academic research)
- Result: Confirmed — First CT installed 1971, widespread adoption mid-late 1970s
- Recommendation: Keep as-is

---

## Fact Verification Summary: Emergency Medicine — 1970s France

**Verification Scope:**
- Total facts in dossier: 20
- Facts verified: 10 (50%)
- Verification depth: Standard

### Verification Results

**✅ Confirmed Facts:** 8 facts
- All information accurate and current
- No action needed

**⚠️ Issues Found:** 2 facts

**Outdated Facts:** 1
1. Haloperidol usage timing — Needs clarification about timeline (available but not yet standard in early-mid 1970s)

**Needs Context:** 1
1. Response time 30-60 minutes — Add note about urban/rural and time-of-day variations

### Accuracy Assessment

**Overall Accuracy:** High
- 80% of verified facts confirmed accurate without modification
- 20% of verified facts need minor updates/context (not errors, just clarifications)

**Dossier Currency:** Current
- Last updated: 10 days ago
- Information age: Recent and well-researched

**Reliability Assessment:** High
- Facts well-supported by authoritative sources
- Issues found are minor clarifications, not errors

### Recommendations

1. Add context note to Response time fact (urban vs. rural)
2. Clarify Haloperidol timeline (available but not yet standard in early 1970s)
3. Consider adding French brand name "Largactil" for Chlorpromazine

---

**Ready to proceed to source validation?**

[Y]es, check sources next
[R]eview findings (show specific facts)
[M]odify verification (check more facts)"

---

## Success Criteria

✅ **Fact selection appropriate** for validation depth
✅ **Independent research conducted** for each selected fact
✅ **Alternative sources found** (not just original sources)
✅ **Verification results documented** with clear status
✅ **Issues identified** and categorized (contradicted/outdated/partial/cannot verify)
✅ **Recommendations provided** for each issue
✅ **Accuracy assessment** completed with percentage metrics
✅ **User informed** of verification results before proceeding

---

## Next Step

Once fact verification is complete and reviewed, proceed to **Step V3: Check Sources** where we'll verify that all sources are reliable and accessible.

---

## Notes for Documentaliste

- **Use independent sources** — don't just check original sources, find alternatives
- **Be thorough but efficient** — match verification depth to plan
- **Document everything** — each verification result needs clear status
- **Look for nuance** — facts may be "mostly true but missing context"
- **Don't assume errors** — if cannot verify, flag for review rather than marking wrong
- **Check currency** — information may have been correct when written but outdated now
- **Prioritize story-critical facts** — focus on what matters for the story
- **Use web research extensively** — this is core validation work
- **Report progress** — keep user informed during verification
- **Be objective** — verify rather than assuming correctness
