---
name: 'step-04b-review'
description: 'Present generated character for author review and refinement'

# File References
outputFile: '{project-root}/characters/{character_name}-dossier.md'
nextStep: './step-05b-complete.md'

# Menu Options
advancedElicitation: true
partyMode: false

---

# Step 4b: Review & Refine (Autonomous)

## STEP GOAL:

To present the generated character to the author for review, allow for refinements and adjustments, and ensure satisfaction before finalizing.

## MANDATORY EXECUTION RULES (READ FIRST):

See: `../../../data/procedures/mode-procedures.md#common-execution-rules-all-modes`

### Step-Specific Rules:

- 🎯 This is REVIEW mode — present what was generated, gather feedback
- 💬 Author can approve or request specific refinements
- 🚫 FORBIDDEN to regenerate everything without request
- ✅ Use Advanced Elicitation (A) to explore refinement directions

## EXECUTION PROTOCOLS:

See: `../../../data/procedures/mode-procedures.md#common-execution-rules-all-modes`

- 🎯 Follow the MANDATORY SEQUENCE exactly
- 📖 Present generated dossier for review
- 💬 Gather specific feedback on what works and what doesn't
- 💾 Make targeted refinements as requested
- 🔄 Proceed to completion only on author approval

## CONTEXT BOUNDARIES:

- Available context: Character Keeper agent persona, complete generated dossier
- Focus: Review and refinement
- Limits: Targeted changes only, not wholesale regeneration
- Dependencies: step-03b-generate must have completed dossier

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Welcome to Review Phase

"**Voici votre personnage!** 📖

I've generated **{characterName}** based on your concept. Let me walk you through what I created, then you can tell me what works and what needs adjustment."

### 2. Present Character Overview

Read `{outputFile}` and present a concise overview:

"**{characterName} — Overview:**
**Role:** [story role] | **Age:** [age] | **Profession:** [profession]
**Key Personality Traits:** [3-5 main traits]
**Core Desire:** [conscious want] | **Deeper Need:** [unconscious need]
**Core Fear:** [terror]
**Voice:** [speech pattern description]
**Arc Type:** [Growth/Fall/Flat/Transformation]

Would you like to see the full dossier, or should I go section by section?"

Wait for author response.

### 3. Review Options

"**How would you like to review?**
**[F]** Full Dossier — Show me everything at once
**[S]** Section by Section — Walk through each part
**[H]** Highlights — Show me the key elements only
**[A]** Approve — This looks good, let's finalize"

Wait for author selection.

### 4. Present Based on Selection

**IF F:** Display complete `{outputFile}` content, then proceed to step 5.
**IF S:** Walk through each section, wait for feedback before moving to next.
**IF H:** Display key highlights, then proceed to step 5.
**IF A:** Skip to step 6 (Finalize).

### 5. Gather Refinement Requests

"**What do you think?**
**[G]** Good to go — I'm satisfied
**[R]** Refine — I need some changes
**[X]** Exit — Save and review later"

**IF G:** Proceed to step 6.
**IF X:** Save progress and exit.
**IF R:** Proceed to refinement process.

### 6. Refinement Process (IF R selected)

"**What would you like to refine?**
**[1]** Specific section — I'll tell you which part
**[2]** Overall feeling — Something's off but I'm not sure what
**[3]** Add something — I want to include an element that's missing
**[4]** Remove something — This doesn't fit
**[5]** Major change — I want to change something fundamental"

**Handle each case:**

**IF 1 (Specific section):**
"Which section? [A] Appearance / [P] Personality / [D] Desires/Fears / [V] Voice / [R] Relationships / [C] Arc / [O] Other"
Then: "What needs to change in [section]?" Make the update.

**IF 2 (Overall feeling):**
"Tell me what feels off. I'll help identify the issue."
Use Advanced Elicitation to explore, then propose and make changes.

**IF 3 (Add something):**
"What element would you like to add?"
Get specifics, integrate into appropriate section.

**IF 4 (Remove something):**
"What doesn't fit?"
Remove or adjust the requested element.

**IF 5 (Major change):**
"What fundamental change do you need?"
If contradicts original concept: "This is substantial. Are you sure? [Y]es / [N]o"
Then make the change.

### 7. Update Dossier with Refinements

For each refinement:
1. Read current `{outputFile}`
2. Update relevant section(s)
3. Save updated file
4. Confirm: "✅ Updated [section]. Anything else?"

### 8. Repeat Review Cycle

After making refinements, return to step 3 (Review Options):

"**The dossier has been updated.** Would you like to see the changes or continue refining?
**[S]** See changes
**[C]** Continue refining
**[G]** Good to go"

Wait for selection and proceed accordingly.

### 9. Final Approval

When author selects **[G]**:

"**Excellent!** Let me finalize **{characterName}**..."
Proceed to step 10.

### 10. Update Frontmatter

Update `{outputFile}` frontmatter:

```yaml
stepsCompleted: ['step-01-init', 'step-02b-input', 'step-03b-generate', 'step-04b-review']
lastStep: 'step-04b-review'
reviewed: true
approved: true
reviewDate: {current_date}
```

### 11. Transition to Completion

"**{characterName}** is approved! Ready to save to the story bible?
**[C]** Continue — Save to bible and complete workflow
**[A]** Advanced Elicitation — Final exploration or refinements
**[X]** Exit — Save progress and leave"

**IF C:** Load, read entire file, then execute `{nextStep}`
**IF A:** Use Advanced Elicitation for final explorations, then redisplay menu.
**IF X:** Save progress and exit.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- Author has seen the generated character (full or section-by-section)
- Author has opportunity to request refinements
- All requested refinements are implemented
- Author explicitly approves the character
- Dossier reflects author's vision
- Frontmatter updated with review and approval
- Proceeding to completion with author consent

### ❌ SYSTEM FAILURE:

- Author hasn't seen the character before proceeding
- No opportunity for refinement offered
- Refinement requests not implemented
- Proceeding to completion without explicit approval

**Master Rule:** Even in autonomous mode, the author must have final say. A character isn't complete until the author says it's complete.

### ADVANCED ELICITATION USE CASES:

Use **[A]** when:
- Author says "something's off" but can't identify what
- Need to explore implications of a requested change
- Author wants to understand why something was generated a certain way
- Testing whether a refinement would improve or harm coherence

Example: "You mentioned the [trait] doesn't feel right. Let's explore that — what does [trait] make you feel? What would you prefer instead, and why?"
