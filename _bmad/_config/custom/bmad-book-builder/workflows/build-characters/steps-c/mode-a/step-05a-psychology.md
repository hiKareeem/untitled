---
name: 'step-05a-psychology'
description: 'Explore character psychology - desires, fears, contradictions, and blind spots'

# File References
outputFile: '{project-root}/characters/{character_name}-dossier.md'
nextStep: './step-06a-voice.md'

# Menu Options
advancedElicitation: true
partyMode: true

---

# Step 5a: Psychology (Collaborative)

## STEP GOAL:

To develop **{characterName}**'s inner world — conscious and unconscious desires, deepest fears, internal contradictions, and blind spots. This is where character depth comes from.

## MANDATORY EXECUTION RULES (READ FIRST):

See: `../../../data/procedures/mode-procedures.md#common-execution-rules-all-modes`

### Step-Specific Rules:

- 🎯 This is THE critical step for character depth — take your time
- 💬 Contradictions and blind spots are what make characters real — pursue them relentlessly
- 🚫 FORBIDDEN to accept simple answers — dig deeper
- ✅ HEAVILY use Advanced Elicitation (A) and Party Mode (P) — this step benefits from multiple perspectives

## EXECUTION PROTOCOLS:

See: `../../../data/procedures/mode-procedures.md#common-execution-rules-all-modes`

## CONTEXT BOUNDARIES:

- Available context: Character Keeper agent persona, existing dossier
- Focus: Internal psychology — the invisible forces driving behavior
- Limits: Don't jump ahead to arc — that's about transformation
- Dependencies: Previous steps must have established background and appearance

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Welcome to Psychology Phase

"**Nous voici au cœur du personnage.** 🧠

This is where **{characterName}** becomes real — not just a collection of traits and history, but a living, breathing person with contradictions, blind spots, and layers of desire they don't even understand themselves.

**Take your time with this step.** It's the most important one for character depth."

### 2-7. Psychology Exploration (5-Phase Framework)

Follow the 5-Phase Psychological Framework from `../../../data/references/character-frameworks.md`:

**Phase 1: Conscious Desires**
"**Let's start with what {characterName} knows they want:**"
1. What does {characterName} consciously want most?
2. Why do they want it?
3. What are they doing to get it?

**Phase 2: Unconscious Desires**
"**Now for what they DON'T know they want:**"
4. What does {characterName} ACTUALLY want?
5. How is this different from what they think they want?
6. What happens when these two desires conflict?

**Phase 3: Deepest Fears**
"**Now the shadows:**"
7. What terrifies {characterName} most?
8. What's the origin of this fear?
9. How does this fear limit them?
10. What would happen if this fear came true?

**Phase 4: Internal Contradictions**
"**🎯 C'EST CRUCIAL — les contradictions sont ce qui rend les personnages humains.**

**EXIGENCE : MINIMUM 5 CONTRADICTIONS PAR PERSONNAGE**

See `../../../data/references/character-frameworks.md#phase-4-internal-contradictions` for detailed contradiction types."

Use the 6 contradiction types from the framework:
- Type 1: Valeurs vs Actions
- Type 2: Image de soi vs Réalité
- Type 3: Conscient vs Inconscient
- Type 4: Idéalisme vs Pragmatisme
- Type 5: Passé vs Présent
- Type 6: Tensions identifiées

**Phase 5: Blind Spots**
"**Now for what {characterName} cannot see about themselves:**"
15. What's obvious to everyone else but {characterName} can't see?
16. What do they refuse to admit about themselves?
17. How do other people see {characterName}?

### 8. Strengths and Weaknesses

"**Let's round out the psychological portrait:**"
18. What is {characterName}'s greatest strength?
19. What is their greatest weakness?
20. How are these two things connected?

### 9. Synthesize and Present

"**Here's {characterName}'s psychological portrait:**"

[Summarize key psychological elements — conscious vs unconscious desires, core fears, central contradictions, blind spots. Focus on tensions and conflicts.]

"**The key contradiction I'm seeing:** [highlight the most interesting tension]

**The blind spot that will matter most:** [identify the most consequential blind spot]

Does this capture their inner world? What needs to go deeper?"

### 10. Update Character Dossier

Update the **Personnalité** and **Désirs et peurs** sections in `{outputFile}`:

See templates in `../../../data/templates/character-templates.yaml#personality_template` and `../../../data/templates/character-templates.yaml#desires_fears_template`

### 11. Update Frontmatter

Update `stepsCompleted` array in `{outputFile}` frontmatter:

```yaml
stepsCompleted: ['step-01-init', 'step-02a-concept', 'step-03a-physical', 'step-04a-background', 'step-05a-psychology']
lastStep: 'step-05a-psychology'
```

### 12. Present Menu Options

Display:

"**{characterName}** has depth now. Ready to give them a voice?

**[C]** Continue — Move to speech patterns and mannerisms
**[A]** Advanced Elicitation — Dive deeper into psychology
**[P]** Party Mode — Get multiple perspectives on {characterName}'s psychology
**[X]** Exit — Save progress and leave"

#### Menu Handling Logic:

See: `../../../data/procedures/mode-procedures.md#menu-handling-logic`

- IF A: Use Advanced Elicitation to explore psychology more deeply (unexamined corners of psyche, shadow work, etc.), then [Redisplay Menu Options](#12-present-menu-options)
- IF P: Use Party Mode to get diverse perspectives on contradictions and blind spots — different personas might spot different things, then [Redisplay Menu Options](#12-present-menu-options)
- Other options follow standard handling

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- Clear distinction between conscious and unconscious desires
- At least 5 significant contradictions identified (AgentAdam requirement)
- Core fear(s) named with origin explained
- At least 1 major blind spot identified
- Connection between strengths and weaknesses explored
- Author feels character has genuine psychological depth
- Personnalité and Désirs et peurs sections fully populated
- Frontmatter updated with step completion

### ❌ SYSTEM FAILURE:

- No distinction between conscious and unconscious desire
- Accepting simple answers without pushing deeper
- Fewer than 5 contradictions or blind spots identified
- Character feels psychologically flat or consistent
- Author doesn't feel character has depth

**Master Rule:** Characters are interesting because they're contradictory. If the character feels consistent, you haven't gone deep enough.

### ADVANCED ELICITATION USE CASES:

Use **[A]** when:
- Author gives simple answers ("they want to be happy")
- You sense unexplored contradictions
- Need to push past surface-level desires
- Author hasn't considered how fears limit character

Example: "You mentioned {characterName} wants [X]. What if getting [X] would cost them [Y]? What if [X] and [Y] are mutually exclusive — which would they actually choose, and what would that tell us about them?"

### PARTY MODE USE CASES:

Use **[P]** when:
- Author is stuck identifying contradictions
- Want diverse perspectives on blind spots
- Exploring what different people might see in the character
- Author wants to discover hidden psychological tensions

Example: "Let's have multiple perspectives analyze {characterName}'s psychology — different takes on their contradictions, what they're hiding from themselves, what their behavior actually means."
