---
name: 'step-02-edit'
description: 'Apply specific edits to character dossier'

# File References
targetFile: '{provided_path}'
nextStep: './step-03-complete.md'

# Menu Options
advancedElicitation: true
partyMode: false

---

# Step 2: Apply Edits (Edit Mode)

## STEP GOAL:
To apply the confirmed changes to the character dossier, maintaining consistency and ensuring all edits serve the story.

## MANDATORY EXECUTION RULES (READ FIRST):

See: `../../data/procedures/mode-procedures.md` - Edit Mode section

### Step-Specific Rules:
- 🎯 This is EDIT mode — apply changes with precision
- 💬 Verify each change before applying
- 🚫 FORBIDDEN to make unconfirmed changes
- ✅ Use Advanced Elicitation (A) to explore implications

## EXECUTION PROTOCOLS:
- 🎯 Follow the MANDATORY SEQUENCE exactly
- 📖 Load target dossier and change plan
- 💬 Apply changes one section at a time with confirmation
- 💾 Save after each confirmed change
- 🔄 Track all edits for review

## MANDATORY SEQUENCE

### 1. Load Change Plan

"**Let me load the change plan...**"

Read `{targetFile}` frontmatter to retrieve `editPlan`.

Display the change plan:

"**Changes to make to {characterName}:**
[Display the edit plan from step-01]"

### 2. Process Changes Section by Section

For each section in the change plan:

#### 2.1. Present Current Content

"**[Section Name]**

**Current content:**
[Display current content of the section]"

#### 2.2. Present Proposed Change

"**Proposed change:**
[Display the specific change from the plan]"

#### 2.3. Confirm Before Applying

"**Apply this change?**

**[Y]** Yes — Apply this change
**[S]** Skip — Leave this section as-is for now
**[M]** Modify — I want to adjust the change
**[X]** Exit — Save progress and stop editing"

**IF Y:** Apply the change and save file
**IF S:** Skip this change, move to next section
**IF M:** Ask for modification details, then confirm
**IF X:** Save progress and exit

### 3. Check for Consistency Impact

After each applied change, check if it affects other sections:

"**This change may affect: [list related sections].**

Would you like to review these sections for consistency?
**[Y]** Yes — Review affected sections
**[N]** No — Continue to next change"

**IF Y:** Present affected sections and ask if changes are needed.

### 4. Complete All Changes

Repeat step 2 for all sections in the change plan.

### 5. Review All Changes

"**All changes applied. Here's what was modified:**

[List all changes made]

**Would you like to:**
**[V]** View full updated dossier
**[A]** Adjust any changes
**[C]** Confirm and complete
**[X]** Exit without finalizing"

#### Menu Handling Logic:
- IF V: Display complete updated dossier
- IF A: Return to step 2 for specific adjustment
- IF C: Proceed to step 6
- IF X: Save progress and exit

### 6. Final Confirmation

"**Final review of changes to {characterName}:**

[Summary of all changes]

**These changes will be saved permanently. Confirm?**
**[Y]** Yes — Save and complete
**[N]** No — Make adjustments"

**IF Y:** Proceed to step 7.
**IF N:** Return to step 2.

### 7. Update Frontmatter

Update `{targetFile}` frontmatter:

```yaml
editMode: true
editStarted: {edit_start_date}
editCompleted: {current_date}
editPlan: |
  [Original plan]
editApplied: true
editSummary: |
  [Summary of changes applied]
```

### 8. Transition to Completion

"**Edits complete!**

**[C]** Continue — Complete edit workflow
**[X]** Exit — Save and leave"

**IF C:** Load, read entire file, then execute `{nextStep}`
**IF X:** Save progress and exit workflow.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- All planned changes presented for confirmation
- Changes applied only with explicit approval
- Consistency impacts identified and addressed
- File saved after each confirmed change
- Frontmatter updated with edit tracking
- Author has clear record of all changes

### ❌ SYSTEM FAILURE:
- Changes applied without confirmation
- No consistency checks performed
- File not saved after changes
- No edit tracking in frontmatter

**Master Rule:** Every change must be confirmed before application. Edits are sacred — once applied, they become the character's truth.

### ADVANCED ELICITATION USE CASES:

Use **[A]** when:
- Author requests a change with unclear implications
- Need to explore how a change affects character coherence
- Author wants to understand the ripple effects of an edit
- Multiple change options exist

Example: "You mentioned changing [element]. This would affect [related sections]. Would that still serve your story intent, or should we adjust?"
