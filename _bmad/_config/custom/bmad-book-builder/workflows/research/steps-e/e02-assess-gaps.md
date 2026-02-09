# Step E2: Assess Gaps

**Step:** E2 of 4 (Edit Mode)
**Purpose:** Identify missing or outdated information
**Agent:** Documentaliste

---

## What This Step Does

Analyze the existing dossier to identify gaps, outdated information, or areas needing expansion based on the edit plan from Step E1.

---

## Instructions for Documentaliste

### 1. Review Current Dossier Content

From Step E1, retrieve:
- Complete dossier content
- Edit plan with planned changes
- Update type (add/update/correct/expand)

### 2. Analyze Dossier Sections

For each section in the dossier, assess:

#### **Overview Section**
- Does it accurately reflect current scope?
- Does it mention new story applications?
- Is the description complete?

#### **Key Facts Section**
- Are all categories from edit plan represented?
- Are facts still current and accurate?
- Are there obvious gaps in coverage?
- Do facts answer the research questions from edit plan?

#### **Technical Details Section**
- Are technical specifications complete?
- Are procedures adequately detailed?
- Is terminology comprehensive?

#### **Common Misconceptions Section**
- Are there known misconceptions not covered?
- Are corrections still accurate?

#### **Story Applications Section**
- Are all relevant story elements linked?
- Are new chapters/scenes from edit plan included?
- Are applications specific enough?

#### **Sources Section**
- Are all sources still accessible?
- Are sources current (not outdated)?
- Is source coverage adequate for topic?

### 3. Identify Specific Gaps

Create a detailed gap analysis based on update type:

**For Add New Information:**
```markdown
## Gap Analysis: Information to Add

**New Aspects to Research:**
1. [Aspect 1] — Currently missing
   - Research questions: [List questions]
   - Target section: [Where it will go]

2. [Aspect 2] — Currently missing
   - Research questions: [List questions]
   - Target section: [Where it will go]

**Existing Sections to Expand:**
1. [Section name] — Currently has [N] facts, needs [N] more
   - Gaps: [What's missing]
   - Research questions: [List questions]
```

**For Update Outdated Information:**
```markdown
## Gap Analysis: Information to Update

**Outdated Facts:**
1. [Fact description]
   - Current source: [URL/reference]
   - Date: [When researched]
   - Why outdated: [Reason]
   - New research needed: [What to verify]

2. [Fact description]
   - Current source: [URL/reference]
   - Date: [When researched]
   - Why outdated: [Reason]
   - New research needed: [What to verify]

**Dead or Broken Sources:**
1. [Source name] — [URL] — [Section it supports]
2. [Source name] — [URL] — [Section it supports]
```

**For Correct Errors:**
```markdown
## Gap Analysis: Errors to Correct

**Factual Errors:**
1. [Error description]
   - Current (incorrect) fact: [What dossier says]
   - Correction needed: [What should be researched/verified]
   - Section: [Where it appears]

2. [Error description]
   - Current (incorrect) fact: [What dossier says]
   - Correction needed: [What should be researched/verified]
   - Section: [Where it appears]

**Missing Verification:**
1. [Unverified fact] — Needs source verification
2. [Unverified fact] — Needs source verification
```

**For Expand Scope:**
```markdown
## Gap Analysis: Scope Expansion

**New Aspects to Add:**
1. [New aspect name]
   - Why needed: [Story context]
   - Research questions: [List questions]
   - Related to existing: [Which current sections]
   - Target sections: [Where it will go]

2. [New aspect name]
   - Why needed: [Story context]
   - Research questions: [List questions]
   - Related to existing: [Which current sections]
   - Target sections: [Where it will go]
```

### 4. Generate Research Questions

For each gap identified, create specific research questions:

```markdown
## Research Questions for Gap Filling

**[Aspect/Section Name]:**
1. [Specific question to answer]
2. [Specific question to answer]
3. [Specific question to answer]

**[Aspect/Section Name]:**
1. [Specific question to answer]
2. [Specific question to answer]
```

### 5. Assess Source Needs

Determine how many new sources are needed:

```markdown
## Source Assessment

**Current Sources:** [N] sources
**Source Quality:** [High/Medium/Low based on aggregate]
**Broken/Dead URLs:** [N] sources need replacement

**New Sources Needed:**
- [Aspect 1]: [N] sources (estimated)
- [Aspect 2]: [N] sources (estimated)
- **Total estimated:** [N] new sources

**Target Source Count:** [Current + New] sources
```

### 6. Present Gap Analysis to User

Show complete gap analysis and get confirmation:

```markdown
## Gap Analysis Summary: [Topic Name]

**Update Type:** [Type]

### Information Gaps Identified

**Missing Information:**
- [Gap 1]
- [Gap 2]
- [Gap 3]

**Outdated Information:**
- [Item 1]
- [Item 2]

**Errors to Correct:**
- [Error 1]
- [Error 2]

**Broken Sources:**
- [Source 1]
- [Source 2]

### Research Required

**Research Questions:** [N] questions across [N] aspects
**New Sources Needed:** Approximately [N] sources
**Sections to Modify:** [List sections]

### Estimated Scope

**Research Time:** [Light/Moderate/Extensive]
**Complexity:** [Low/Medium/High]

---

**Does this gap analysis look accurate?**

[Y]es, proceed to research
[M]odify gaps (add/remove items)
[R]eview dossier again (re-read sections)
```

### 7. Allow Gap Adjustment

If user selects [M]odify:
- Ask which gaps to add/remove/modify
- Update gap analysis
- Re-present for confirmation

If user selects [R]eview:
- Show specific dossier sections user wants to review
- Update gap analysis based on review
- Re-present for confirmation

### 8. Store Gap Analysis

Keep gap analysis in conversation context for Step E3:

```yaml
gap_analysis:
  missing_information:
    - aspect: "Aspect name"
      research_questions:
        - "Question 1"
        - "Question 2"
      target_section: "Section name"
  outdated_information:
    - fact: "Fact description"
      current_source: "URL"
      verification_needed: "What to verify"
  errors_to_correct:
    - error: "Error description"
      current_incorrect: "What dossier says"
      correction_needed: "What to research"
      section: "Section name"
  broken_sources:
    - source: "Source name"
      url: "URL"
      section: "Section it supports"
  new_sources_needed: 3
```

---

## Example Interaction

**Documentaliste:**
"Analyzing dossier for gaps based on edit plan...

---

## Gap Analysis: Emergency Medicine — 1970s France

**Update Type:** Add new information

### Information Gaps Identified

**Missing Information:**
- Psychiatric emergency protocols in 1970s France
- Legal procedures for involuntary psychiatric commitment
- Medications available for psychiatric emergencies in 1970s
- Psychiatric ward operations in French hospitals

**Current Coverage:**
- ✅ Emergency room equipment (8 facts)
- ✅ Emergency procedures (6 facts)
- ✅ Emergency medical services (5 facts)
- ❌ Psychiatric emergency procedures (0 facts) — **GAP IDENTIFIED**

### Research Required

**Research Questions:** 6 questions across 1 new aspect

**Psychiatric Emergency Procedures:**
1. What were standard protocols for handling psychiatric emergencies in 1970s French hospitals?
2. What legal procedures existed for involuntary psychiatric commitment?
3. What medications were available for psychiatric emergencies?
4. How did emergency physicians interact with psychiatric services?
5. What were response times for psychiatric consultations?
6. What documentation was required for psychiatric emergencies?

**New Sources Needed:** Approximately 3-4 sources
- Legal sources (psychiatric commitment laws)
- Medical sources (protocols, medications)
- Historical sources (1970s French psychiatric care)

**Sections to Modify:**
- Key Facts (add new category: Psychiatric Emergency Procedures)
- Story Applications (add Chapter 15 psychiatric scene)
- Sources (add 3-4 new sources)
- Dossier Metadata (update Last Updated, Source Count)

### Estimated Scope

**Research Time:** Moderate (3-4 sources, new aspect)
**Complexity:** Medium (legal + medical research)

---

**Does this gap analysis look accurate?**

[Y]es, proceed to research
[M]odify gaps (add/remove items)
[R]eview dossier again (re-read sections)"

**User:** "Yes, looks good. One addition — also research how psychiatric patients were transported to hospitals."

**Documentaliste:**
"Excellent addition! Updating gap analysis...

**Added Research Question:**
7. How were psychiatric patients transported to hospitals in 1970s France? (Emergency ambulance vs. specialized transport)

**Updated Research Questions:** 7 questions across 1 new aspect

Ready to proceed? [Y]es / [M]ore modifications"

---

## Success Criteria

✅ **Dossier thoroughly analyzed** section by section
✅ **Specific gaps identified** with clear descriptions
✅ **Research questions generated** for each gap
✅ **Source needs estimated** (how many new sources required)
✅ **Sections to modify listed** clearly
✅ **User confirms gap analysis** before proceeding to research

---

## Next Step

Once gap analysis is complete and confirmed, proceed to **Step E3: Gather New Info** where we'll conduct web research to fill the identified gaps.

---

## Notes for Documentaliste

- **Be thorough** — analyze every section of the dossier
- **Be specific** — vague gaps lead to unfocused research
- **Generate clear research questions** — these guide the research in Step E3
- **Estimate source needs realistically** — helps user understand scope
- **Consider story context** — gaps should align with story needs
- **Check source accessibility** — dead URLs are common gaps
- **Get user buy-in** — user should agree with what's missing
- **Allow modifications** — user may identify gaps you missed
- **Document everything** — gap analysis drives the rest of Edit mode
