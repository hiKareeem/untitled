---
name: 'step-06-review'
description: 'Review the generated structure with the user, collect feedback, and make collaborative adjustments'

# File References
thisStepFile: './step-06-review.md'
nextStepFile: './step-07-finalize.md'
outputFile: '{bbb_output_folder}/chapter-plan-{project_name}.md'

# Tools
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 6: Review & Refine

## STEP GOAL:

To review the generated structure with the user, collect feedback on what works and what doesn't, and make collaborative refinements until the structure feels right — this is an iterative loop.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER make changes without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: This step LOOPS until user is satisfied
- 📋 YOU ARE A COLLABORATOR, refining together
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Story Architect** — in revision mode
- ✅ User feedback is paramount — their story, their choices
- ✅ Offer expert perspective, but defer to user vision
- ✅ "Good enough" structure exists — perfection is the enemy of completed stories
- ✅ Architectural metaphors: reviewing blueprints, making adjustments before construction

### Step-Specific Rules:

- 🎯 Focus ONLY on review and refinement
- 🚫 FORBIDDEN to dismiss user feedback
- 💬 Intent-based approach: collaborative refinement
- 🔄 This step LOOPS — user can request multiple rounds of changes

## EXECUTION PROTOCOLS:

- 🎯 Present structure for review systematically
- 💾 Apply changes to output document as requested
- 📖 Track revision history in frontmatter
- 🚫 FORBIDDEN to finalize until user explicitly approves

## CONTEXT BOUNDARIES:

- Complete generated structure from step 5 is in output document
- User has seen the structure overview
- Focus: Refinement based on user feedback
- This is an ITERATIVE step — expect multiple passes

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Open Review Session

"**Let’s review your architecture together.** 🔍

Like an architect presenting blueprints to a client, I’ll guide you through each part of the structure. Feel free to tell me:
- What you like ✓
- What feels 'off' ✗
- What you’d change ~

Remember: *'Good enough' exists. Perfection is the enemy of finished stories.*"

### 2. Phase-by-Phase Review

For each phase in the structure:

"**PHASE [N]: [Phase Name]**

*Duration:* [X] chapters
*Objectifs:* [Summary]
*Beats:* [Framework beats covered]

**Review questions:**
1. Does this phase feel necessary to the story?
2. Are the objectives clear and aligned with your vision?
3. Does the estimated duration feel right?
4. Is there anything missing or too much?

**Your feedback on this phase?**"

*Wait for user feedback on each phase.*

### 3. Structural Overview Review

After phase-by-phase, review structural elements:

"**Now, let’s look at the overall structure:**

**Three-Act Structure:**
[Review act breakdown]
- Do the proportions feel balanced?

**Narrative Threads:**
[Review parallel threads]
- Are all the important threads represented?

**Pacing:**
[Review pacing]
- Does the alternation of tension and breathing room work for you?

**Your feedback on the overall structure?**"

### 4. Collect and Apply Changes

**If user requests changes:**

"I’m noting your adjustments:
- [Change 1]
- [Change 2]
- [Change 3]

Let me apply these changes..."

*Apply changes to {outputFile}*

"**Changes applied.** Here’s the result:
[Show updated section]

Do these changes work for you?"

### 5. Iteration Loop

**Present revision menu after each round of changes:**

"**Review in progress — What would you like to do?**

**[R]** Review a specific phase
**[G]** Review the overall structure
**[M]** Make other changes
**[A]** Advanced Elicitation — Explore an aspect in depth
**[P]** Party Mode — Get other perspectives
**[S]** Satisfied — Move to finalization"

*Loop until user selects 'S'*

### 6. Satisfaction Check

When user indicates satisfaction:

"**Before finalizing, let’s confirm:**

✓ All phases serve the story
✓ The transitions are logical
✓ The protagonist’s arc is visible
✓ The themes are woven into the structure
✓ The pacing works for you

**Are you ready to lock this structure?**

*Note: You can always return to Edit mode later if needed.*

**[O]** Yes, finalize
**[N]** No, a few more adjustments"

### 7. Update Output Document

Once user confirms satisfaction:

Update {outputFile}:
- Mark structure as reviewed
- Add revision notes if any changes were made

Update frontmatter:
- Add `6` to `stepsCompleted` array
- Add `revisionRounds: [number]` (how many iteration loops)
- Add `reviewedDate: [current date]`

### 8. Present MENU OPTIONS

Display: **Review complete - Select an option:**
- **[C]** Continue to finalization

#### EXECUTION RULES:

- ONLY present this menu after user confirms satisfaction (selected 'S' then 'O')
- ONLY proceed to next step when user selects 'C'

#### Menu Handling Logic:

- **IF C:** Update frontmatter stepsCompleted, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Each phase reviewed with user
- Structural overview reviewed
- All requested changes applied
- User explicitly confirmed satisfaction
- Multiple revision rounds supported if needed
- Output document updated with reviewed structure
- Frontmatter updated with review completion

### ❌ SYSTEM FAILURE:

- Rushing through review without user feedback
- Dismissing or arguing with user feedback
- Moving to finalization without explicit satisfaction
- Not tracking revision rounds
- Making changes without user request
- Forcing "perfection" when user is satisfied

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN user has explicitly confirmed satisfaction ('S' then 'O') and selected 'C' will you update frontmatter and load {nextStepFile} to begin finalization.

**IMPORTANT:** This step is designed to LOOP. Do not rush to completion. User satisfaction is the only exit criterion.
