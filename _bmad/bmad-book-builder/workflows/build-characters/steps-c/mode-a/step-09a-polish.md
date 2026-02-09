---
name: 'step-09a-polish'
description: 'Final polish and review - ensure consistency, depth, and story readiness'

# File References
outputFile: '{project-root}/characters/{character_name}-dossier.md'
nextStep: './step-10a-complete.md'

# Menu Options
advancedElicitation: true
partyMode: false

---

# Step 9a: Final Polish (Collaborative)

## STEP GOAL:

To review **{characterName}** as a complete whole, identify gaps or inconsistencies, ensure depth and authenticity, and polish the character dossier for story use.

## MANDATORY EXECUTION RULES (READ FIRST):

See: `../../../data/procedures/mode-procedures.md#common-execution-rules-all-modes`

### Step-Specific Rules:

- 🎯 This is a REVIEW step — focus on quality, consistency, and completeness
- 💬 Celebrate what works — but don't shy from pointing out gaps
- 🚫 FORBIDDEN to add new content without author collaboration
- ✅ Use Advanced Elicitation (A) to explore gaps and inconsistencies

## EXECUTION PROTOCOLS:

See: `../../../data/procedures/mode-procedures.md#common-execution-rules-all-modes`

- 🎯 Follow the MANDATORY SEQUENCE exactly
- 💾 Update output file with any refinements
- 📖 Track progress in frontmatter `stepsCompleted`
- 🔄 Review ALL sections of the dossier
- 🔄 Proceed to next step only when author selects 'C'

## CONTEXT BOUNDARIES:

- Available context: Character Keeper agent persona, complete existing dossier, story bible
- Focus: Holistic review — how everything works together
- Limits: Don't add new dimensions — refine what exists
- Dependencies: All previous steps must be complete

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Welcome to Polish Phase

"**Here we are.** ✨

**{characterName}** is now fully developed. Let's review them as a whole and make sure everything is coherent, deep, and ready for the story.

This is our chance to catch inconsistencies, fill gaps, and polish the rough edges."

### 2. Load Complete Dossier

"**Let me read through the complete dossier...**"

Read the entire `{outputFile}` file to review all sections.

### 3-6. Quality Checks

Perform all quality checks from `../../../data/references/character-frameworks.md#quality-standards-reference`:

**Consistency Check (3-8):**
"**First, let's check for consistency:**
1. Voice and Psychology: Does speech pattern reflect psychology?
2. Background and Arc: Does transformation grow from background?
3. Desires and Fears: Are conscious/unconscious desires in tension?
4. Appearance and Self-Image: How does appearance reflect or contradict self-image?"

**Depth Check (5-8):**
"**Now let's check for depth:**
5. Contradictions: At least 5 genuine contradictions?
6. Blind Spots: Meaningful blind spots?
7. Specificity: Is every section specific to THIS character?
8. Stereotype Check: More than an archetype?"

**Story Integration Check (9-12):**
"**Now for how they serve the story:**
9. Role Clarity: Is their story role clear?
10. Conflict Generator: What tensions do they create/embody?
11. Arc Necessity: Is this arc essential to the story?
12. Relationships: Are relationships meaningful and story-driving?"

**Readiness Check (13-16):**
"**Finally, is {characterName} ready to be used in a story?**
13. Chapter Readiness: Would Chapter Writer have everything needed?
14. Voice Recognition: Would you know them without dialogue tags?
15. Emotional Truth: Does this character feel emotionally authentic?
16. Gaps: What's missing? What questions remain?"

Wait for responses to each check. Note any issues.

### 7. Present Review Findings

"**Here's my assessment of {characterName}:**"

**✅ STRENGTHS:**
[List 3-5 things that work particularly well — distinctive voice, interesting contradictions, strong arc, etc.]

**⚠️ AREAS FOR POLISH:**
[List any inconsistencies, gaps, or areas needing refinement]

**🔍 QUESTIONS:**
[Any remaining questions or uncertainties about the character]

"**Would you like to address any of these areas?** Or is {characterName} ready as-is?"

Wait for author response.

### 8. Refinement (If Needed)

**IF author wants to refine:**

Work through each identified issue one by one. For each:
- Identify the issue: "You mentioned [issue]. Let's explore that."
- Ask guiding questions: Use Advanced Elicitation techniques
- Update dossier: Make changes to `{outputFile}` as author provides input

**IF author is satisfied:**

"**{characterName}** is polished and ready!"

### 9. Complete Thematic Section

Ensure the **Themes explored** section in `{outputFile}` is populated:

See template in `../../../data/templates/character-templates.yaml#themes_template`

### 10. Update Frontmatter

Update `stepsCompleted` array in `{outputFile}` frontmatter:

```yaml
stepsCompleted: ['step-01-init', 'step-02a-concept', 'step-03a-physical', 'step-04a-background', 'step-05a-psychology', 'step-06a-voice', 'step-07a-relationships', 'step-08a-arc', 'step-09a-polish']
lastStep: 'step-09a-polish'
```

### 11. Present Menu Options

Display:

"**{characterName}** is complete! 🎉

Ready to finalize and save to the story bible?

**[C]** Continue — Save to story bible and complete workflow
**[A]** Advanced Elicitation — Final refinements or explorations
**[X]** Exit — Save progress and leave"

#### Menu Handling Logic:

See: `../../../data/procedures/mode-procedures.md#menu-handling-logic`

- IF A: Use Advanced Elicitation for any final refinements, then [Redisplay Menu Options](#11-present-menu-options)
- Other options follow standard handling

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- All consistency checks passed (voice matches psychology, arc grows from background, etc.)
- At least 5 genuine contradictions identified (AgentAdam requirement)
- Meaningful blind spots noted
- Character is specific, not generic or stereotypical
- Story role is clear
- Arc is essential to the story
- Character feels emotionally authentic
- Author cares about the character
- All sections complete and populated
- Themes explored section completed
- Frontmatter updated with step completion

### ❌ SYSTEM FAILURE:

- Inconsistencies between sections (voice doesn't match psychology, etc.)
- Fewer than 5 genuine contradictions
- Generic or stereotypical elements
- Gaps that prevent story use
- Author doesn't feel connected to character

**Master Rule:** A character is ready when they feel like a real person who could surprise you. If everything about them is predictable, keep working.

### ADVANCED ELICITATION USE CASES:

Use **[A]** when:
- Author is stuck on how to resolve an inconsistency
- Need to deepen a contradiction or blind spot
- Want to explore alternative arc possibilities
- Testing character's emotional authenticity

Example: "You mentioned {characterName} [contradiction]. Let's explore this — when would each side emerge? What would force them to choose one over the other?"
