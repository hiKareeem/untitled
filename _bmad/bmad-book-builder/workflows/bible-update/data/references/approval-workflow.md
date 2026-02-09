# Bible Update Approval Workflow

**Purpose:** Reference guide for user approval workflow, decision trees, and conflict resolution patterns.

**Scope:** Step 03 - Approve Changes workflow logic

---

## Decision Logic Flow

### Primary Decision Flag

```yaml
decision_needed = (conflicts.length > 0) OR (uncertain_items.length > 0)
```

### Decision Paths

```
decision_needed?
├─ false (clean extraction)
│  └─ Show summary → Auto-proceed → Step 04
│
└─ true (conflicts/uncertainties exist)
   └─ Show conflicts/uncertainties → AskUserQuestion
      ├─ Proceed → approved_extraction → Step 04
      ├─ Edit → modify → confirm → approved_extraction → Step 04
      └─ Cancel → Exit workflow
```

---

## Path 1: Clean Extraction (Auto-Proceed)

### Condition

- `decision_needed === false`
- No conflicts detected
- No uncertain items
- All extractions clear and confident

### User Display

```markdown
✅ **Extraction Clean**

- No conflicts detected
- All extractions clear and confident
- Continuity validated

Proceeding to update bible automatically...
```

### Action

- Proceed directly to Step 04 (Update Bible)
- No user interaction needed
- Brief informational display only

---

## Path 2: Review Needed (User Checkpoint)

### Condition

- `decision_needed === true`
- Conflicts OR uncertainties exist
- User decision required before proceeding

### Display Format

```markdown
⚠️  **Review Needed**

### Conflicts Detected ({count})

**{Dimension}: {Entity}**
- **Issue:** {conflict description}
- **Chapter says:** {what chapter states}
- **Bible says:** {what existing bible states}
- **Proposed resolution:** {suggested fix}

---

### Uncertain Extractions ({count})

**{Dimension}: {Entity}**
- **Extracted value:** {what was extracted}
- **Uncertainty:** {why uncertain}
- **Suggested:** {flag for manual review after update}

---

### Options

**[P] Proceed** - Accept extraction as-is (proposed resolutions will be applied)
**[E] Edit** - Modify extraction before updating bible
**[C] Cancel** - Abort workflow without making changes

Your choice:
```

---

## User Options

### Option P: Proceed

**User Action:** Accepts extraction with proposed resolutions

**System Actions:**
1. Set `approved_extraction = extraction_data` (unchanged)
2. Note that proposed resolutions are accepted
3. Display: "✅ Extraction approved. Proceeding to update bible..."
4. Continue to Step 04

**When to Use:** User is satisfied with extraction and proposed resolutions

---

### Option E: Edit

**User Action:** Wants to modify extraction before committing

**System Actions:**

1. **Display current extraction** in editable format
2. **Ask user which sections to modify:**
   ```
   What would you like to edit?
   1. Chronology
   2. Characters
   3. Locations
   4. Objects
   5. Themes
   6. Specific conflict resolution
   ```

3. **For selected section:**
   - Show current extraction data
   - Allow user to provide modified version
   - Update `extraction_data` with user edits

4. **Re-validate:**
   - Quick check for obvious errors
   - Confirm: "Updated extraction ready. Proceed to update bible? [Y/n]"

5. **If yes:**
   - Set `approved_extraction = edited_extraction_data`
   - Continue to Step 04

6. **If no:**
   - Return to edit or cancel

**When to Use:** User wants to correct extraction before committing to bible

---

### Option C: Cancel

**User Action:** Aborts workflow entirely

**System Actions:**
1. Display: "❌ Workflow cancelled. No changes made to bible."
2. Exit workflow
3. No files modified
4. Extraction data discarded

**When to Use:** User wants to stop and reconsider, or chapter needs revision

---

## First Mentions Alert

### Purpose

Always highlight new entities being added to bible, even in auto-proceed mode.

### Display Format

```markdown
🆕 **New Entities Detected**

This chapter introduces:
- **Characters:** {list new characters}
- **Locations:** {list new locations}
- **Objects:** {list new objects}
- **Themes:** {list new themes}

These will be added to the bible.
```

### Display Logic

**If `decision_needed === false` (auto-proceed):**
- Show alert + auto-proceed message
- Brief pause (informational only, no user action needed)

**If `decision_needed === true` (conflicts):**
- Include in review section
- User sees as part of approval decision

---

## Extraction Summary Display

### Always Displayed (Both Paths)

```markdown
## 📋 Extraction Summary - Chapter {XX}

### Extracted Information

**Chronology:**
- {brief summary: day, duration, key events}

**Characters:** {count} characters
- {Character 1}: {brief note}
- {Character 2}: {brief note}
{If first mentions: 🆕 {Character}: First appearance}

**Locations:** {count} locations
- {Location 1}: {brief note}
{If first mentions: 🆕 {Location}: First appearance}

**Objects:** {count} objects
- {Object 1}: {status}
{If first mentions: 🆕 {Object}: First appearance}

**Themes:** {count} themes
- {Theme 1}: {progression note}
{If first mentions: 🆕 {Theme}: First appearance}

---
```

### Purpose

- Give user clear overview of what was extracted
- Show scale of updates coming to bible
- Highlight new entities immediately

---

## Edge Cases and Handling

### Case 1: User Chooses Edit but Provides No Changes

**Detection:** User selects Edit but doesn't modify anything

**Handling:**
```
Ask to confirm: "No changes detected. Proceed with original extraction? [Y/n]"
├─ Yes → Proceed to Step 04 with original extraction
└─ No → Return to edit menu or cancel
```

---

### Case 2: Many First Mentions (10+ New Entities)

**Detection:** Large number of new characters, locations, or objects

**Handling:**
- Group by dimension (don't show individual list if too long)
- Show counts with "(list available on request)"
- Example:
  ```markdown
  🆕 **New Entities Detected**
   - **Characters:** 15 new characters (detailed list available)
   - **Locations:** 3 new locations
  ```

---

### Case 3: Conflicts + First Mentions Together

**Detection:** Both conflicts and new entities exist

**Handling:**
- Show conflicts first (higher priority)
- Show first mentions after conflicts
- Don't bury new entities in conflict details
- Use clear section separation

---

### Case 4: User Unclear on Conflict Resolution

**Detection:** User asks for clarification on proposed resolution

**Handling:**
```
Provide context: Show relevant bible section for comparison

**For location conflicts:**
"Current bible entry for Jean:
From chapitre-03: Jean in London on Day 5
Proposed update: Jean in Paris on Day 5 (from this chapter)

Resolution: Update to Paris (this chapter is more recent)"
```

---

## Output Data Structure

### When Approved

```yaml
approved_extraction: {extraction_data, potentially edited}
user_decision: "proceed" | "edit"
conflicts_accepted: {list of conflict resolutions accepted}
chapter_number: {XX}
```

### When Cancelled

```yaml
user_decision: "cancel"
workflow_status: "aborted"
extraction_discarded: true
```

---

## Tool Usage

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **AskUserQuestion** | Get user decision | Conflict/uncertainty approval |
| Display | Show extraction summary | Always (both paths) |

**Note:** No file operations in approval step (review only)

---

## Communication Guidelines

### Clear Communication Principles

1. **Use emojis for quick visual scanning**
   - ✅ = success/clean
   - ⚠️ = warning/conflict
   - 🆕 = new entity
   - ❓ = uncertain
   - ❌ = error/cancel

2. **Group related information**
   - All conflicts together
   - All uncertainties together
   - All first mentions together

3. **Provide context for conflicts**
   - Don't just say "conflict"
   - Explain what contradicts
   - Show chapter vs bible comparison

4. **Make proposed resolutions actionable**
   - Clear what will happen
   - User understands impact

---

### User Empowerment

- **Transparency:** Make it easy to understand what will change
- **No hiding information:** Show all conflicts and uncertainties
- **Straightforward editing:** Edit option should be clear and simple
- **Always can cancel:** Cancel option always available

---

### Efficiency

- **Auto-proceed when safe:** Don't ask unnecessary questions
- **Concise interface:** Keep approval interface focused
- **Smart defaults:** Proposed resolutions should be sensible

---

## Success Criteria

- ✅ Extraction summary displayed
- ✅ Decision logic correctly applied (auto-proceed vs checkpoint)
- ✅ User decision captured (if checkpoint needed)
- ✅ Approved extraction ready for Step 04
- ✅ First mentions highlighted
- ✅ Clear communication of what will be updated

---

## Workflow Transitions

### From Step 02

**Input:**
```yaml
extraction_data: {structured extraction}
conflicts: [{array of conflict objects}]
uncertain_items: [{array of uncertain item objects}]
first_mentions: [{array of new entities}]
decision_needed: {boolean}
```

### To Step 04

**Output (if approved):**
```yaml
approved_extraction: {final extraction data}
user_decision: "proceed" | "edit"
chapter_number: {XX}
```

**Output (if cancelled):**
- Workflow exits
- No Step 04 execution
