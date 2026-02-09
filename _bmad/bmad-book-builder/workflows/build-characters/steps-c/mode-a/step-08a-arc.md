---
name: 'step-08a-arc'
description: 'Map character transformation arc - starting point, catalysts, and evolution'

# File References
outputFile: '{project-root}/characters/{character_name}-dossier.md'
nextStep: './step-09a-polish.md'

# Menu Options
advancedElicitation: true
partyMode: false

---

# Step 8a: Arc of Transformation (Collaborative)

## STEP GOAL:

To map **{characterName}**'s transformation arc — where they start, what catalyzes change, how they evolve, and where they end up. This is the skeleton of their story.

## MANDATORY EXECUTION RULES (READ FIRST):

See: `../../../data/procedures/mode-procedures.md#common-execution-rules-all-modes`

### Step-Specific Rules:

- 🎯 Arc connects all previous elements — this is where it comes together
- 💬 Transformation must be earned — no epiphanies without preparation
- 🚫 FORBIDDEN to create an arc that contradicts established character
- ✅ Use Advanced Elicitation (A) to explore the arc deeply

## EXECUTION PROTOCOLS:

See: `../../../data/procedures/mode-procedures.md#common-execution-rules-all-modes`

- 🎯 Follow the MANDATORY SEQUENCE exactly
- 💾 Update output file with author's responses
- 📖 Track progress in frontmatter `stepsCompleted`
- 🔄 Reference previous steps for consistency
- 🔄 Proceed to next step only when author selects 'C'

## CONTEXT BOUNDARIES:

- Available context: Character Keeper agent persona, complete existing dossier
- Focus: Through-line of transformation — how story changes the character
- Limits: Must be consistent with established psychology, desires, and fears
- Dependencies: All previous steps must be complete (psychology, relationships, etc.)

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Welcome to Arc Phase

"**We're at the climax.** 🎯

Everything we've explored — **{characterName}**'s psychology, history, relationships, desires, fears — all of it leads here. The arc is the story's spine: who they are, what breaks them open, who they become.

This step will reveal whether everything we've built is coherent."

### 2-6. Arc Development

"**Let's establish where {characterName} begins:**"

1. When the story starts, what does {characterName} believe about themselves?
2. What's their emotional state?
3. What are they WRONG about?
4. What's their flaw or misapprehension?

Wait for responses.

"**Something needs to happen to crack {characterName} open:**"

5. What inciting incident or disruption forces {characterName} to engage?
6. Why can't they ignore this?
7. What do they WANT to do (vs what they NEED to do)?
8. What do they FEAR will happen?

Wait for responses.

"**Now for the middle — the struggle, the setbacks, the incremental shifts:**"

9. What does {characterName} face that challenges their beliefs?
10. What do they resist changing?
11. What breaks them open?
12. What do they have to give up?

Wait for responses.

"**Every arc has a moment when there's no going back:**"

13. What's {characterName}'s point of no return?
14. What choice do they make that defines who they're becoming?
15. What does this choice cost them?

Wait for responses.

"**Let's establish where {characterName} ends up:**"

16. When the story ends, what does {characterName} believe now?
17. What have they learned?
18. What's different about how they move through the world?
19. What's still unresolved?

Wait for responses.

### 7. Arc Consistency Check

"**Critical question — does this fit the character we've built?**"

20. How does this arc fulfill {characterName}'s unconscious desire?
21. How does this arc force them to confront their deepest fear?
22. How does this arc resolve or transform their key contradictions?

Wait for responses.

### 8. Arc Type Selection

"**One last thing — what KIND of arc is this?**"

See arc types in `../../../data/references/character-frameworks.md#character-arc-types`

"**[A]** Growth Arc — {characterName} overcomes their flaw and becomes a better version of themselves

**[B]** Fall Arc — {characterName} descends into their flaw and is destroyed by it

**[C]** Flat Arc — {characterName} already has the truth and transforms the world around them

**[D]** Transformation Arc — {characterName} becomes something fundamentally different

**[E]** Complex Arc — A combination or subversion of the above"

Wait for response.

### 9. Synthesize and Present

"**Here's {characterName}'s transformation arc:**"

[Create a clear arc summary — starting state → catalysts → struggles → point of no return → ending state. Highlight the emotional truth of the transformation.]

"**The arc type:** [name it]

**Does this track?** Does it feel true to the character we've built? Any contradictions?"

### 10. Update Character Dossier

Update the **Transformation arc** section in `{outputFile}`:

See template in `../../../data/templates/character-templates.yaml#arc_template`

### 11. Update Frontmatter

Update `stepsCompleted` array in `{outputFile}` frontmatter:

```yaml
stepsCompleted: ['step-01-init', 'step-02a-concept', 'step-03a-physical', 'step-04a-background', 'step-05a-psychology', 'step-06a-voice', 'step-07a-relationships', 'step-08a-arc']
lastStep: 'step-08a-arc'
```

### 12. Present Menu Options

Display:

"**{characterName}** has an arc now. Ready for final polish?

**[C]** Continue — Final polish and review
**[A]** Advanced Elicitation — Dive deeper into the arc
**[X]** Exit — Save progress and leave"

#### Menu Handling Logic:

See: `../../../data/procedures/mode-procedures.md#menu-handling-logic`

- IF A: Use Advanced Elicitation to explore arc more deeply (alternative paths, what if scenarios, testing the arc's integrity), then [Redisplay Menu Options](#12-present-menu-options)
- Other options follow standard handling

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- Clear starting point established (who they are, what they believe)
- Catalyst of change identified
- Journey of struggle and resistance mapped
- Point of no return defined
- Clear ending point (how they've changed)
- Arc is consistent with established psychology
- Arc type identified and fits the transformation
- Arc de transformation section fully populated
- Frontmatter updated with step completion

### ❌ SYSTEM FAILURE:

- Arc doesn't connect to established character (psychology, desires, fears)
- Transformation is unearned (no struggle, no resistance)
- No clear starting or ending point
- Arc is generic rather than specific to this character

**Master Rule:** The arc must be the ONLY way this specific character could transform. If it could apply to anyone, it's not specific enough.

### ADVANCED ELICITATION USE CASES:

Use **[A]** when:
- Arc feels generic or predictable
- Transformation seems unearned
- You want to explore alternative arc paths
- Need to test the arc's emotional integrity

Example: "What if {characterName} made a different choice at [moment]? What would THAT arc look like? Why is the actual arc the RIGHT one for them?"
