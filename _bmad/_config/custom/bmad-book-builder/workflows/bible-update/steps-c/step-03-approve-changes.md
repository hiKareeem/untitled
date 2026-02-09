# Step 03: Approve Changes

**Goal:** Present extraction results and get user approval if conflicts detected, otherwise auto-proceed.

**Duration:** 0-2 minutes (0 if auto-proceed, 2 if user review needed)

---

## What You'll Do

1. Check the `decision_needed` flag from Step 02
2. Display extraction summary
3. If conflicts/uncertainties exist, present to user for approval
4. If clean, auto-proceed with confirmation message
5. Handle user decisions (proceed / edit / cancel)

---

## Process

### A. Display Extraction Summary

**Always show** (regardless of decision_needed):

```markdown
## 📋 Extraction Summary - Chapitre {XX}

### Informations Extraites

**Chronologie:**
- {brief summary: day, duration, key events}

**Personnes:** {count} characters
- {Character 1}: {brief note}
{If first mentions: 🆕 {Character}: First appearance}

**Lieux:** {count} locations
- {Location 1}: {brief note}
{If first mentions: 🆕 {Location}: First appearance}

**Objets:** {count} objects
- {Object 1}: {status}
{If first mentions: 🆕 {Object}: First appearance}

**Thèmes:** {count} themes
- {Theme 1}: {progression note}
{If first mentions: 🆕 {Theme}: First appearance}
```

---

### B. Check Decision Flag

#### Path 1: Clean Extraction (decision_needed === false)

**No conflicts and no uncertainties** → Auto-proceed

Display:
```markdown
✅ **Extraction Clean**

- No conflicts detected
- All extractions clear and confident
- Continuity validated

Proceeding to update bible automatically...
```

**Action:** Proceed directly to Step 04 (Update Bible)
**No user interaction needed**

---

#### Path 2: Conflicts/Uncertainties Detected (decision_needed === true)

**Conflicts OR uncertainties exist** → User checkpoint required

**Complete decision tree and user options:**
- See: `data/references/approval-workflow.md` for detailed workflow

Display full conflict/uncertainty details:

```markdown
⚠️  **Review Needed**

### Conflicts Detected ({count})

{For each conflict:}
**{Dimension}: {Entity}**
- **Issue:** {conflict description}
- **Chapter says:** {what chapter states}
- **Bible says:** {what existing bible states}
- **Proposed resolution:** {suggested fix}

---

### Uncertain Extractions ({count})

{For each uncertain item:}
**{Dimension}: {Entity}**
- **Extracted value:** {what was extracted}
- **Uncertainty:** {why uncertain}

---

### Options

**[P] Proceed** - Accept extraction as-is (proposed resolutions will be applied)
**[E] Edit** - Modify extraction before updating bible
**[C] Cancel** - Abort workflow without making changes
```

**Use AskUserQuestion** to get user decision.

---

### C. Handle User Decision

**Detailed handling for each option:**
- See: `data/references/approval-workflow.md` for complete procedures

#### Option P: Proceed

User accepts extraction with proposed resolutions.

**Action:**
- Set `approved_extraction = extraction_data` (unchanged)
- Display: "✅ Extraction approved. Proceeding to update bible..."
- Continue to Step 04

#### Option E: Edit

User wants to modify extraction before committing.

**Action:**
- Display current extraction_data
- Allow user to provide modified version
- Update `extraction_data` with user edits
- Confirm: "Updated extraction ready. Proceed to update bible? [Y/n]"
- If yes → Set `approved_extraction = edited_extraction_data`, continue to Step 04

#### Option C: Cancel

User aborts workflow.

**Action:**
- Display: "❌ Workflow cancelled. No changes made to bible."
- Exit workflow
- No files modified

---

### D. First Mentions Alert

If any first mentions detected (new characters, locations, objects, themes):

**Always alert user** (even if auto-proceeding):

```markdown
🆕 **New Entities Detected**

This chapter introduces:
- **Personnes:** {list new characters}
- **Lieux:** {list new locations}
- **Objets:** {list new objects}
- **Thèmes:** {list new themes}

These will be added to the bible.
```

**Display logic:**
- If `decision_needed === false`: Show alert + auto-proceed message
- If `decision_needed === true`: Include in review section

---

## Outputs (passed to Step 04)

```yaml
approved_extraction: {extraction_data, potentially edited}
user_decision: "proceed" | "edit" | "cancel"
conflicts_accepted: {list of conflict resolutions accepted}
chapter_number: {XX}
```

**If user_decision === "cancel":**
- Workflow exits, no Step 04

---

## Tools Used

- **AskUserQuestion** - Get user decision if conflicts/uncertainties
- No file operations (review only)

---

## Success Criteria

- ✅ Extraction summary displayed
- ✅ Decision logic correctly applied (auto-proceed vs checkpoint)
- ✅ User decision captured (if checkpoint needed)
- ✅ Approved extraction ready for Step 04
- ✅ First mentions highlighted
- ✅ Clear communication of what will be updated

---

## Edge Cases

| Case | Handling |
|------|----------|
| User chooses Edit but provides no changes | Ask to confirm: proceed with original or cancel |
| Many first mentions (10+ new entities) | Group by dimension, don't overwhelm display |
| Conflicts + first mentions | Show both clearly, don't bury new entities |
| User unclear on conflict resolution | Provide context: show relevant bible section |

**Detailed edge case handling:**
- See: `data/references/approval-workflow.md`

---

## Next Step

**If approved:** Proceed to **Step 04: Update Bible**
**If cancelled:** Exit workflow

---

## Quick Reference

**Decision Logic:**
```
decision_needed = (conflicts > 0) OR (uncertainties > 0)

false → Auto-proceed to Step 04
true → User review → [P]roceed / [E]dit / [C]ancel
```

**Complete approval workflow reference:**
- `data/references/approval-workflow.md`
