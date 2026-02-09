# Step V1: Select Dossier

**Step:** V1 of 4 (Validate Mode)
**Purpose:** Choose existing dossier to validate
**Agent:** Documentaliste

---

## What This Step Does

Identify which research dossier needs validation and understand the validation context and goals.

---

## Instructions for Documentaliste

### 1. List Available Dossiers

Read the research directory to show available dossiers:
- Read `research/index.md` (if exists)
- Scan `research/dossiers/` directory
- Present list with validation-relevant metadata

Present to user:

```markdown
## Available Research Dossiers for Validation

1. **[Dossier 1 Topic]**
   - Last Updated: [Date]
   - Sources: [N]
   - Last Validated: [Date or "Never"]

2. **[Dossier 2 Topic]**
   - Last Updated: [Date]
   - Sources: [N]
   - Last Validated: [Date or "Never"]

3. **[Dossier 3 Topic]**
   - Last Updated: [Date]
   - Sources: [N]
   - Last Validated: [Date or "Never"]

Which dossier would you like to validate? [Enter number or topic name]
```

### 2. Handle No Dossiers Found

If no dossiers exist:
- "No research dossiers found. Would you like to:
  - [C]reate a new dossier (switch to Create mode)
  - [S]pecify a different research directory"

### 3. Confirm Dossier Selection

Once user selects a dossier:
- Read the complete dossier file
- Check for existing validation history
- Present summary to user

```markdown
## Selected Dossier: [Topic Name]

**File:** research/dossiers/[filename].md
**Created:** [Date]
**Last Updated:** [Date]
**Sources:** [N] sources
**Facts:** [N] facts in [N] categories

**Current Sections:**
- ✅ Overview
- ✅ Key Facts ([N] facts)
- ✅ Technical Details
- ✅ Common Misconceptions ([N] items)
- ✅ Story Applications ([N] items)
- ✅ Sources ([N] sources)
- ✅ Notes for Author

**Validation History:**
[If validation history exists, show:]
- Last Validated: [Date]
- Status: [PASS/CONCERNS/ISSUES]
- Issues Found: [N] issues

[If no validation history:]
- This dossier has never been validated.

Is this the dossier you want to validate? [Y]es / [N]o (choose different)
```

### 4. Understand Validation Context

Ask user why they want validation:

```markdown
Why are you validating this dossier?

[R]outine validation - Regular accuracy check
[B]efore use - About to use dossier for writing, want to verify first
[F]eedback received - Reader/editor raised accuracy concerns
[S]ource concerns - Noticed broken links or questionable sources
[T]ime elapsed - Dossier is old, want to check if information still current
[O]ther - Describe validation reason

Select validation reason:
```

### 5. Set Validation Depth

Based on validation reason, suggest validation depth:

```markdown
Validation Depth Options:

[Q]uick validation (10-15 minutes)
- Spot-check 3-5 key facts
- Verify all source URLs are accessible
- Check for obvious contradictions
- Quick reliability assessment

[S]tandard validation (20-30 minutes)
- Verify 50% of facts with spot research
- Check all source URLs and reliability
- Cross-reference facts for contradictions
- Detailed source quality assessment

[T]horough validation (45+ minutes)
- Verify ALL facts with independent research
- Deep source reliability investigation
- Comprehensive contradiction analysis
- Research updates/changes since creation

**Recommended depth:** [Based on validation reason]

Select validation depth: [Q/S/T]
```

**Depth recommendations:**
- Routine validation → Quick or Standard
- Before use → Standard
- Feedback received → Thorough
- Source concerns → Standard or Thorough
- Time elapsed → Standard or Thorough

### 6. Identify Priority Areas

Ask if there are specific areas of concern:

```markdown
Are there specific areas you want me to focus on?

- [A]ll sections equally
- [F]ocus on Key Facts section
- [T]echnical Details accuracy
- [S]ource reliability and accessibility
- [M]isconceptions verification
- [C]ustom focus (specify which facts/sections)

Select focus area:
```

### 7. Present Validation Plan

Summarize validation plan for user confirmation:

```markdown
## Validation Plan: [Topic Name]

**Dossier:** research/dossiers/[filename].md

**Validation Context:**
- Reason: [Why validating]
- Depth: [Quick/Standard/Thorough]
- Focus: [What to prioritize]

**Planned Checks:**

**Source Validation:**
- ✓ Check all [N] source URLs for accessibility
- ✓ Assess source reliability (academic/professional/general)
- ✓ Verify source dates and currency

**Fact Validation:**
- ✓ Spot-check [N] facts with independent research
- ✓ Look for contradictions between facts
- ✓ Verify technical details for accuracy

**Story Alignment:**
- ✓ Confirm story applications are still relevant
- ✓ Check if warnings/recommendations are current

**Estimated Time:** [N] minutes

---

Is this validation plan correct?

[Y]es, begin validation
[M]odify plan (adjust depth/focus)
[C]ancel (choose different dossier)
```

### 8. Store Validation Context

Keep validation plan in conversation context for Step V2:

```yaml
validation_context:
  dossier_file: "research/dossiers/[filename].md"
  topic: "Topic Name"
  reason: "routine/before_use/feedback/source_concerns/time_elapsed"
  depth: "quick/standard/thorough"
  focus: "all/key_facts/technical/sources/misconceptions"
  source_count: N
  fact_count: N
  validation_history:
    last_validated: "YYYY-MM-DD or null"
    last_status: "PASS/CONCERNS/ISSUES or null"
```

---

## Example Interaction

**Documentaliste:**
"Let me check what research dossiers are available for validation...

## Available Research Dossiers for Validation

1. **Emergency Medicine — 1970s France**
   - Last Updated: 2026-01-25
   - Sources: 12
   - Last Validated: Never

2. **Paris Metro Routes — 1970s**
   - Last Updated: 2026-01-10
   - Sources: 3
   - Last Validated: Never

3. **French Police Procedures — 1970s**
   - Last Updated: 2026-01-12
   - Sources: 4
   - Last Validated: 2026-01-15 (Status: PASS)

Which dossier would you like to validate?"

**User:** "1"

**Documentaliste:**
"Reading dossier...

## Selected Dossier: Emergency Medicine — 1970s France

**File:** research/dossiers/emergency-medicine-1970s-france.md
**Created:** 2026-01-15
**Last Updated:** 2026-01-25
**Sources:** 12 sources
**Facts:** 20 facts in 4 categories

**Current Sections:**
- ✅ Overview
- ✅ Key Facts (20 facts in 4 categories)
- ✅ Technical Details
- ✅ Common Misconceptions (3 items)
- ✅ Story Applications (5 items)
- ✅ Sources (12 sources)
- ✅ Notes for Author

**Validation History:**
- This dossier has never been validated.

Is this the dossier you want to validate? [Y]es / [N]o (choose different)"

**User:** "Yes"

**Documentaliste:**
"Why are you validating this dossier?

[R]outine validation - Regular accuracy check
[B]efore use - About to use dossier for writing, want to verify first
[F]eedback received - Reader/editor raised accuracy concerns
[S]ource concerns - Noticed broken links or questionable sources
[T]ime elapsed - Dossier is old, want to check if information still current
[O]ther - Describe validation reason

Select validation reason:"

**User:** "B - About to write Chapter 15, want to make sure the psychiatric info is accurate"

**Documentaliste:**
"Excellent — validating before use ensures writing accuracy.

Validation Depth Options:

[Q]uick validation (10-15 minutes)
- Spot-check 3-5 key facts
- Verify all source URLs are accessible
- Check for obvious contradictions
- Quick reliability assessment

[S]tandard validation (20-30 minutes)
- Verify 50% of facts with spot research
- Check all source URLs and reliability
- Cross-reference facts for contradictions
- Detailed source quality assessment

[T]horough validation (45+ minutes)
- Verify ALL facts with independent research
- Deep source reliability investigation
- Comprehensive contradiction analysis
- Research updates/changes since creation

**Recommended depth:** Standard (dossier recently updated, before critical use)

Select validation depth: [Q/S/T]"

**User:** "S"

**Documentaliste:**
"Are there specific areas you want me to focus on?

- [A]ll sections equally
- [F]ocus on Key Facts section
- [T]echnical Details accuracy
- [S]ource reliability and accessibility
- [M]isconceptions verification
- [C]ustom focus (specify which facts/sections)

Select focus area:"

**User:** "C - Focus on the psychiatric emergency procedures category since that's what Chapter 15 needs"

**Documentaliste:**
"Perfect focus for your writing needs.

## Validation Plan: Emergency Medicine — 1970s France

**Dossier:** research/dossiers/emergency-medicine-1970s-france.md

**Validation Context:**
- Reason: Before use (Chapter 15 writing)
- Depth: Standard validation
- Focus: Psychiatric Emergency Procedures category

**Planned Checks:**

**Source Validation:**
- ✓ Check all 12 source URLs for accessibility
- ✓ Assess source reliability (especially psychiatric sources)
- ✓ Verify source dates and currency

**Fact Validation:**
- ✓ Verify ALL 9 facts in Psychiatric Emergency Procedures category
- ✓ Spot-check 5 facts from other categories (50% sample)
- ✓ Look for contradictions between facts
- ✓ Verify psychiatric medications, legal procedures, transport protocols

**Story Alignment:**
- ✓ Confirm Chapter 15 psychiatric scene application is accurate
- ✓ Check if warnings/recommendations address psychiatric procedures

**Estimated Time:** 25-30 minutes

---

Is this validation plan correct?

[Y]es, begin validation
[M]odify plan (adjust depth/focus)
[C]ancel (choose different dossier)"

---

## Success Criteria

✅ **Existing dossier identified** and file read successfully
✅ **Validation context understood** (why validating)
✅ **Validation depth set** (quick/standard/thorough)
✅ **Focus areas determined** (what to prioritize)
✅ **Validation plan confirmed** by user
✅ **Context stored** for next validation steps

---

## Next Step

Once dossier is selected and validation plan is confirmed, proceed to **Step V2: Verify Facts** where we'll validate the accuracy of facts through spot research.

---

## Notes for Documentaliste

- **Show validation history** — helps user understand if this is first validation
- **Recommend appropriate depth** — match depth to validation reason
- **Allow custom focus** — user may have specific concerns
- **Be transparent about time** — validation takes effort, set expectations
- **Get clear confirmation** — user should understand what validation will do
- **Use Read tool** — need complete dossier content for validation
- **Note last updated date** — helps assess if information might be outdated
- **Check source count** — more sources = more validation work
