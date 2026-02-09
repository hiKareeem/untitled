# Review and Edit Procedures

This document provides detailed procedures for reviewing generated characters and editing existing character dossiers.

## Part 1: Review Procedures (Mode B)

### Review Overview

After autonomous generation in Mode B, the author reviews the generated character and can request refinements before finalizing.

---

### Review Presentation Options

**Option F: Full Dossier**
- Display complete dossier content at once
- Best for authors who want to see everything
- Allows comprehensive review before feedback

**Option S: Section by Section**
- Walk through each section sequentially
- Wait for feedback before moving to next
- Best for detailed, methodical review
- Allows targeted feedback per section

**Option H: Highlights**
- Show only key elements and overview
- Best for quick assessment
- Followed by option to dive deeper if needed

**Option A: Approve**
- Skip review and proceed directly to completion
- Best when author is confident or pressed for time

---

### Review Feedback Categories

When author selects **[R] Refine**, present these options:

**[1] Specific Section**
- Author knows exactly what to change
- Targeted, precise edits
- Example: "Change the voice section"

**[2] Overall Feeling**
- Something's off but author isn't sure what
- Requires exploration and diagnosis
- Use Advanced Elicitation to identify root cause

**[3] Add Something**
- New elements to include
- Missing traits, relationships, backstory
- Integration into appropriate section

**[4] Remove Something**
- Elements that no longer fit
- Outdated content, retconned elements
- Careful removal maintaining consistency

**[5] Major Change**
- Fundamental character changes
- May contradict original concept
- Requires explicit confirmation

---

### Refinement Process

For each refinement request:

#### Specific Section Changes

1. **Identify the section**
   - [A] Appearance
   - [P] Personality
   - [D] Desires/Fears
   - [V] Voice
   - [R] Relationships
   - [C] Arc
   - [O] Other

2. **Get specific feedback**
   - "What needs to change in this section?"
   - Listen to author's specific request

3. **Make the update**
   - Read current file
   - Update relevant section
   - Save updated file
   - Confirm: "✅ Updated [section]. Anything else?"

#### Overall Feeling Issues

1. **Explore the problem**
   - "Tell me what feels off"
   - Use open-ended questions
   - Apply Advanced Elicitation techniques

2. **Identify root cause**
   - Is it a voice issue?
   - Psychology problem?
   - Inconsistency somewhere?
   - Missing element?

3. **Propose solution**
   - "I think the issue is [diagnosis]"
   - "Would [proposed change] address it?"

4. **Implement if approved**
   - Make the change
   - Confirm with author

#### Additions

1. **Understand what to add**
   - "What element would you like to add?"
   - Get specifics

2. **Determine placement**
   - Which section does it belong in?
   - How does it connect to existing content?

3. **Integrate carefully**
   - Add to appropriate section
   - Ensure consistency with existing content
   - Update related sections if needed

#### Removals

1. **Identify what to remove**
   - "What doesn't fit anymore?"
   - Get specific details

2. **Check dependencies**
   - Does other content reference this?
   - Will removal create inconsistencies?
   - Alert author if dependencies exist

3. **Remove cleanly**
   - Remove the element
   - Smooth any resulting gaps
   - Verify overall consistency

#### Major Changes

1. **Understand the change**
   - "What fundamental change do you need?"
   - Get full details

2. **Assess impact**
   - Does this contradict original concept?
   - Will it require multiple section updates?
   - Alert author to scope

3. **Get explicit confirmation**
   - "This is substantial. Are you sure?"
   - [Y]es / [N]o

4. **Implement carefully**
   - Make the change
   - Update all affected sections
   - Verify consistency

---

### Review Cycle

After making refinements:

1. **Update dossier** with changes
2. **Return to review options**
3. **Offer to see changes** or continue refining
4. **Repeat until author satisfied**

**Menu after refinements:**
```
**The dossier has been updated.** Would you like to see the changes or continue refining?

**[S]** See changes
**[C]** Continue refining
**[G]** Good to go
```

---

### Final Approval

When author selects **[G]**:

"**Excellent!** Let me finalize **{characterName}**..."

Proceed to completion step.

---

## Part 2: Edit Procedures (Mode E)

### Edit Overview

Edit Mode allows targeted changes to existing character dossiers. It follows a two-step process: Assess → Edit → Complete.

---

### Step 1: Assessment (step-01-assess.md)

**Goal:** Understand what needs to change before making any edits.

#### Change Categories

Present these options to author:

**[S] Specific Section**
- Author knows exactly what to change
- Clear section and specific change identified
- Example: "I want to update the character's age in Basic Info"

**[O] Overall Feeling**
- Something's off but author isn't sure what
- Requires diagnostic work
- Example: "The character feels flat but I don't know why"

**[D] Development Update**
- Story has evolved, character needs to catch up
- Changes driven by story development
- Example: "The story changed, now the character's background doesn't fit"

**[A] Add Something**
- New elements to include
- Example: "I want to add a fear that wasn't there before"

**[R] Remove Something**
- Elements that no longer fit
- Example: "This relationship doesn't work anymore"

**[V] View Full Dossier**
- Review before deciding
- Display complete dossier, then return to options

#### Assessment Process

1. **Load and verify target file**
   - Confirm file exists and is valid
   - Handle missing or invalid files

2. **Display character overview**
   - Location, last updated, role
   - Quick overview (2-3 sentences)
   - Current sections with completion status

3. **Understand change goals**
   - Present change category options
   - Get specific feedback based on category

4. **Summarize change plan**
   - Sections to be modified
   - Specific changes for each section
   - Any additions or removals

5. **Get author confirmation**
   - "Does this capture your vision?"
   - [C] Yes, make these changes
   - [R] No, let me revise the plan
   - [X] Exit without saving

6. **Store change plan**
   - Update frontmatter with edit tracking
   - Prepare for edit step

---

### Step 2: Edit (step-02-edit.md)

**Goal:** Apply confirmed changes with precision and verification.

#### Edit Process

For each section in the change plan:

**1. Present Current Content**
```
**[Section Name]**

**Current content:**
[Display current content of the section]
```

**2. Present Proposed Change**
```
**Proposed change:**
[Display the specific change from the plan]
```

**3. Confirm Before Applying**
```
**Apply this change?**

**[Y]** Yes — Apply this change
**[S]** Skip — Leave this section as-is for now
**[M]** Modify — I want to adjust the change
**[X]** Exit — Save progress and stop editing
```

**4. Handle Each Option:**
- **Y:** Apply the change and save file
- **S:** Skip this change, move to next section
- **M:** Ask for modification details, then confirm
- **X:** Save progress and exit

#### Consistency Checks

After each applied change:

```
**This change may affect:** [list related sections]

**Would you like to review these sections for consistency?**
**[Y]** Yes — Review affected sections
**[N]** No — Continue to next change
```

**If Y:**
- Present affected sections
- Ask if changes are needed
- Update if requested

**Related Sections Reference:**
- Changing **Personality** may affect: Voice, Arc, Relationships
- Changing **Background** may affect: Psychology, Fears, Arc
- Changing **Desires/Fears** may affect: Arc, Psychology
- Changing **Arc** may affect: Themes, Story Integration
- Changing **Voice** may affect: Personality
- Changing **Relationships** may affect: Arc, Story Integration

---

### Step 3: Completion (step-03-complete.md)

**Goal:** Finalize edits, update story bible, close workflow.

#### Completion Process

1. **Final verification**
   - Verify all edits from step-02 are present
   - Check frontmatter edit tracking is complete
   - Verify no obvious inconsistencies introduced
   - Check all sections are properly formatted

2. **Handle issues if found**
   - Present potential issues
   - Offer to fix or proceed as-is

3. **Finalize frontmatter**
   ```yaml
   ---
   stepsCompleted: [existing array..., 'step-01-assess', 'step-02-edit', 'step-03-complete']
   editComplete: true
   editCompletionDate: {current_date}
   editMode: false
   ---
   ```
   - Preserve existing editSummary for history

4. **Update bible index (if needed)**
   - If character's role changed significantly
   - If character name changed
   - Add to index if not present

5. **Present completion summary**
   ```
   **✅ EDITS COMPLETE!**

   ═══════════════════════════════════════════════════════════
     CHARACTER UPDATED: {characterName}
   ═══════════════════════════════════════════════════════════

     📁 Location: {targetFile}
     📅 Edited: {current_date}
     👤 Edited by: {user_name}

     SECTIONS MODIFIED:
     ✅ [List sections that were edited]

     KEY CHANGES:
     • [Summarize the most significant edits]

     CHARACTER STATUS:
     ✅ Complete and consistent
     ✅ Ready for story use

   ═══════════════════════════════════════════════════════════
   ```

6. **Present next steps options**
   - [E] Edit More
   - [V] Validate
   - [W] Write Chapter
   - [N] New Character
   - [X] Exit

---

## Special Edit Cases

### Major Character Overhaul

When edits fundamentally change the character:

```
**This is a significant change to {characterName}.** Would you like to:

**[1]** Create a new version (keep original as backup)
**[2]** Update in place (overwrite existing)
**[3]** Review the changes more carefully
```

### Character Name Change

When character's name changes:

1. Rename the file: `{project-root}/characters/{new_name}-dossier.md`
2. Update the dossier content with new name
3. Update story bible index
4. Optionally keep old file as backup with `__archived` suffix

### Broken References

When other character dossiers reference this character:

```
⚠️ Other characters reference {characterName} in their relationship sections.

**Would you like me to:**
**[1]** List them so you can update those references
**[2]** Scan the characters directory for all references
**[3]** Proceed without checking references
```

---

## Advanced Elicitation in Review/Edit

### Use Advanced Elicitation when:

**In Review (Mode B):**
- Author says "something's off" but can't identify what
- Need to explore implications of a requested change
- Author wants to understand why something was generated a certain way
- Testing whether a refinement would improve or harm coherence

**In Edit (Mode E):**
- Author has vague sense that "something's wrong"
- Need to explore implications of proposed changes
- Author wants to change something fundamental
- Multiple potential change directions exist

### Example Elicitation Techniques:

**For "something's off":**
> "You mentioned the [trait/element] doesn't feel right. Let's explore that — what does [trait] make you feel? What would you prefer instead, and why?"

**For understanding implications:**
> "Changing [element] would affect [related sections]. Would that still serve your story intent, or should we adjust those too?"

**For fundamental changes:**
> "This change would shift [characterName]'s core from [original] to [new]. Is that the direction you want to go? What would that mean for their arc?"

---

## Best Practices

### For Review:
- Celebrate what works while identifying what needs improvement
- Be specific and actionable in feedback
- Allow multiple review cycles
- Never finalize without author approval

### For Edit:
- Assessment before action — understand before editing
- Confirm every change before applying
- Check consistency impacts
- Track all edits for history
- Preserve what works, change only what's needed

### Master Rule:
Every change must be confirmed before application. Character dossiers are sacred trust — once changed, they become the character's truth.
