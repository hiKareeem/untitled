# Step E4: Update Dossier

**Step:** E4 of 4 (Edit Mode)
**Purpose:** Add new findings to existing dossier
**Agent:** Documentaliste

---

## What This Step Does

Integrate new research findings into the existing dossier file, maintaining structure and quality while adding new information.

---

## Instructions for Documentaliste

### 1. Review Update Materials

From Step E3, retrieve:
- New research findings organized by section
- New sources with reliability ratings
- Contradictions resolved
- Original dossier content

### 2. Plan Section Updates

For each section to be modified, determine exact changes:

```markdown
## Update Plan: [Topic Name]

**File:** research/dossiers/[filename].md

### Section-by-Section Updates

**Dossier Metadata:**
- Update "Last Updated" to [current date]
- Update "Source Count" from [old N] to [new N]
- Keep other metadata unchanged

**Overview:**
- [Keep unchanged / Add mention of new aspects / Expand description]

**Key Facts:**
- Add new category: "[Category Name]" with [N] facts
- Expand existing category "[Category]" with [N] facts
- Update fact in "[Category]": [which fact and how]

**Technical Details:**
- Add section for [new technical aspect]
- Expand [existing section] with [new details]

**Common Misconceptions:**
- Add [N] new misconceptions
- Update existing misconception #[N]

**Story Applications:**
- Add [N] new story elements to table
- Update existing row for [element]

**Sources:**
- Add [N] new sources
- Replace broken source #[N] with new source
- Update source #[N] with current URL

**Notes for Author:**
- Add [N] new critical warnings
- Add [N] new recommendations
- Update uncertainty: [which item]
```

### 3. Update Metadata Section

Edit the Dossier Metadata section:

```markdown
## Dossier Metadata
- **Created:** [Keep original date]
- **Last Updated:** [TODAY'S DATE: YYYY-MM-DD]
- **Source Count:** [NEW TOTAL]
- **Story Relevance:** [Update if new story elements added]
- **Reliability:** [Reassess based on aggregate source quality]
```

### 4. Update Overview (If Needed)

If new aspects significantly change dossier scope, update overview:

**Before:**
```markdown
## Overview
Emergency medicine in 1970s France was in a transitional period...
```

**After (if expanded):**
```markdown
## Overview
Emergency medicine in 1970s France was in a transitional period, with modern emergency services being established and advanced medical equipment becoming more widely available. This research supports accurate portrayal of emergency medical and psychiatric emergency procedures...
```

### 5. Update Key Facts Section

Add new facts while maintaining structure and format:

**For new categories:**
```markdown
### Psychiatric Emergency Procedures
- **Fact 1:** [Description]
  - Source: [URL or reference]
  - Verification: ✅ Verified
  - Reliability: High

- **Fact 2:** [Description]
  - Source: [URL or reference]
  - Verification: ✅ Verified
  - Reliability: High
```

**For expanding existing categories:**
- Add new facts at end of category
- Maintain consistent formatting with existing facts
- Keep same indentation and structure

**For updating existing facts:**
- Use Edit tool to replace old fact with updated version
- Add note if fact was updated: "(Updated [date])"
- Keep source history if adding new source

### 6. Update Technical Details (If Applicable)

Add new technical sections or expand existing:

```markdown
## Technical Details

### [Existing Section]
[Existing content...]

### [New Section - if adding]
**[New Technical Aspect]:**
- [Detail 1]
- [Detail 2]
- [Detail 3]
```

### 7. Update Common Misconceptions (If Applicable)

Add new misconceptions following existing format:

```markdown
## Common Misconceptions

[Existing misconceptions...]

- **Misconception [N]:** [What people get wrong]
  - **Reality:** [What's actually true]
  - Source: [Reference]
```

### 8. Update Story Applications Table

Add new story elements or update existing rows:

```markdown
## Story Applications

| Story Element | Chapter/Scene | How Research Applies |
|---------------|---------------|----------------------|
| [Existing entries...] |  |  |
| [New Entry] | Ch. X, Scene Y | [New Application] |
```

### 9. Update Sources Section

Add new sources to the list:

**Maintain numbering:**
```markdown
## Sources

[Existing sources 1-5...]

6. **[New Source Name]** — [URL] — [Reliability: High/Medium/Low]
7. **[New Source Name]** — [URL] — [Reliability: High/Medium/Low]
```

**If replacing broken sources:**
- Mark old source as "(URL no longer accessible - replaced [date])"
- Add replacement source with new number or replace in place

### 10. Update Notes for Author

Add new warnings, recommendations, or update uncertainties:

```markdown
## Notes for Author

**Critical Warnings:**
- [Existing warnings...]
- [New warning from research]

**Areas of Uncertainty:**
- [Existing uncertainties...]
- [New uncertainty OR remove resolved uncertainty]

**Recommendations:**
- [Existing recommendations...]
- [New recommendation]
```

### 11. Execute Dossier Updates

Using the Edit tool, make each planned change:

1. Edit Metadata section (Last Updated, Source Count)
2. Edit Overview (if needed)
3. Edit Key Facts section (add new categories/facts)
4. Edit Technical Details (if applicable)
5. Edit Common Misconceptions (if applicable)
6. Edit Story Applications table
7. Edit Sources section
8. Edit Notes for Author

**Important:** Make edits incrementally, one section at a time, to avoid errors.

### 12. Verify Updates

After all edits complete, read the updated dossier and verify:

- ✅ All planned changes made
- ✅ Metadata updated correctly
- ✅ New facts properly formatted
- ✅ Sources numbered correctly
- ✅ Markdown formatting intact
- ✅ No duplicate content
- ✅ Story applications complete

### 13. Update Research Index (If Exists)

If `research/index.md` exists, update the dossier entry:

```markdown
## Research Dossiers

- **[Topic Name]** — [Updated date] — [New source count] sources
  - File: `dossiers/[filename].md`
  - Scope: [Update scope if changed]
  - Recent Update: [Brief description of what was added]
```

### 14. Present Update Summary

Show user what was changed:

```markdown
## Dossier Updated: [Topic Name]

**File:** research/dossiers/[filename].md

### Changes Made

**Metadata:**
- ✅ Last Updated: [old date] → [new date]
- ✅ Source Count: [old N] → [new N]

**Content Updates:**
- ✅ Added [N] facts in new category "[Category Name]"
- ✅ Expanded [Section] with [N] facts
- ✅ Added [N] new story applications (Chapter 15)
- ✅ Added [N] new sources
- ✅ Updated Notes for Author with [N] warnings

**Before/After:**
- Facts: [old N] → [new N]
- Sources: [old N] → [new N]
- Story Applications: [old N] → [new N]

### Quality Check

✅ All new facts have source citations
✅ Verification symbols used correctly
✅ Reliability ratings assigned
✅ Markdown formatting intact
✅ Story applications linked
✅ Research index updated

---

**Dossier update complete!**

The dossier now includes comprehensive information about [new aspects added].

Would you like to:
- [V]iew updated sections
- [R]un validation on updated dossier (switch to Validate mode)
- [F]inish (update complete)
```

---

## Example Interaction

**Documentaliste:**
"Updating dossier with new research findings...

Making the following edits to: research/dossiers/emergency-medicine-1970s-france.md

1. ✅ Updated Metadata (Last Updated: 2026-01-25, Source Count: 12)
2. ✅ Expanded Overview to mention psychiatric emergency procedures
3. ✅ Added new Key Facts category: "Psychiatric Emergency Procedures" with 9 facts
4. ✅ Expanded Technical Details with psychiatric medication information
5. ✅ Added 1 new Common Misconception about psychiatric procedures
6. ✅ Added Chapter 15 psychiatric scene to Story Applications table
7. ✅ Added 7 new sources to Sources section
8. ✅ Updated Notes for Author with psychiatric procedure warnings

Verifying updates...

---

## Dossier Updated: Emergency Medicine — 1970s France

**File:** research/dossiers/emergency-medicine-1970s-france.md

### Changes Made

**Metadata:**
- ✅ Last Updated: 2026-01-15 → 2026-01-25
- ✅ Source Count: 5 → 12

**Content Updates:**
- ✅ Added 9 facts in new category "Psychiatric Emergency Procedures"
- ✅ Expanded Technical Details with psychiatric medication details
- ✅ Added 1 new common misconception
- ✅ Added Chapter 15 psychiatric scene to Story Applications
- ✅ Added 7 new sources (all High/Medium reliability)
- ✅ Updated Notes for Author with psychiatric procedure warnings

**Before/After:**
- Facts: 11 → 20 facts
- Sources: 5 → 12 sources
- Story Applications: 4 → 5 entries
- Common Misconceptions: 2 → 3 entries

### Quality Check

✅ All new facts have source citations
✅ Verification symbols used correctly (✅ for all verified facts)
✅ Reliability ratings assigned (6 High, 1 Medium)
✅ Markdown formatting intact
✅ Story applications linked to specific chapters
✅ Research index updated

### Key Additions

**New Category:** Psychiatric Emergency Procedures
- Legal procedures for involuntary commitment
- Standard psychiatric medications (Chlorpromazine, Haloperidol)
- Transport protocols for psychiatric patients
- Physician authorization requirements
- Response times for psychiatric consultations

**New Warnings:**
- Psychiatric procedures require legal authorization — can't be portrayed casually
- Use correct French terminology for psychiatric services

---

**Dossier update complete!**

The dossier now includes comprehensive information about psychiatric emergency procedures for Chapter 15's psychiatric scene.

Would you like to:
- [V]iew updated sections
- [R]un validation on updated dossier (switch to Validate mode)
- [F]inish (update complete)"

---

## Success Criteria

✅ **All planned updates executed** correctly in dossier file
✅ **Metadata updated** with current date and source count
✅ **New facts properly formatted** with sources and verification
✅ **Story applications updated** with new story elements
✅ **Sources section complete** with all new sources
✅ **Notes for author updated** with relevant warnings/recommendations
✅ **Research index updated** (if exists)
✅ **Quality verified** — formatting, citations, structure intact
✅ **User confirms update** is complete and accurate

---

## Next Step

Edit mode is complete! The dossier has been successfully updated with new research findings.

**Optional Next Steps:**
- Run Validate mode to verify accuracy of updated dossier
- Create new research dossier (return to workflow.md, select Create mode)
- Exit research workflow

---

## Notes for Documentaliste

- **Use Edit tool exclusively** — never Write (would overwrite entire file)
- **Make incremental edits** — one section at a time for accuracy
- **Preserve existing content** — don't accidentally remove verified facts
- **Maintain formatting consistency** — match existing markdown style
- **Update metadata fields** — Last Updated, Source Count critical
- **Verify after editing** — read updated sections to confirm changes
- **Keep original structure** — don't reorganize unless user requests
- **Document what changed** — user should understand what was added
- **Update research index** — keeps dossier catalog current
- **Quality check before finishing** — ensure all citations, formatting correct
