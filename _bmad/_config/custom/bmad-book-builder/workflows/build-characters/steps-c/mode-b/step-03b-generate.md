---
name: 'step-03b-generate'
description: 'Generate complete character profile from author concept'

# File References
outputFile: '{project-root}/characters/{character_name}-dossier.md'
nextStep: './step-04b-review.md'

# Menu Options
advancedElicitation: false
partyMode: false

---

# Step 3b: Generate Profile (Autonomous)

## STEP GOAL:

To generate a complete, nuanced character profile from the author's concept, filling in all 9 sections with depth, specificity, and narrative coherence.

## MANDATORY EXECUTION RULES (READ FIRST):

See: `../../../data/procedures/mode-procedures.md#common-execution-rules-all-modes`

### Role Reinforcement:

See: `../../../data/procedures/mode-procedures.md#common-execution-rules-all-modes`

### Step-Specific Rules:

- 🎯 This is GENERATION mode — create fully based on concept
- 💬 Draw on narrative expertise to fill gaps intelligently
- ✅ Generate specific, distinctive details — not generic placeholders
- ✅ Ensure internal consistency and psychological depth
- 🚫 NO user input during generation — this is autonomous

## EXECUTION PROTOCOLS:

- 🎯 Follow the MANDATORY SEQUENCE exactly
- 💾 Generate all 9 sections of the dossier
- 📖 Draw on story bible for context if available
- 🔄 Present complete profile for review
- 💾 Update frontmatter after generation

## CONTEXT BOUNDARIES:

- Available context: Character Keeper agent persona, concept from step-02b, story bible
- Focus: Complete character generation
- Limits: Must align with provided concept
- Dependencies: step-02b-input must have provided concept

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise.

### 1. Prepare for Generation

"**I'm now generating {characterName}'s complete character profile...**"

Retrieve the concept from `{outputFile}` frontmatter (`conceptProvided`).

Check story bible for:
- Existing characters (for relationship potential)
- Genre/tone (for consistency)
- Setting/context (for grounding)

### 2. Generate All Sections

Generate content for all 9 sections of the character dossier.

**PRINCIPLES:**
- Specific over generic (concrete details, not placeholder text)
- Contradictory over consistent (characters are complex)
- Psychologically grounded (motivations make sense)
- Narratively functional (serves story needs)

**SECTION GENERATION:**

Follow the 5-Phase Psychological Framework from `../../../data/references/character-frameworks.md#5-phase-psychological-development-framework`

**2.1. Basic Information**
- Âge, Profession/Statut, Origine sociale

**2.2. Apparence physique**
- Description générale, Particularités physiques, Adaptation à l'histoire

**2.3. Personnalité**
- Traits dominants (3-5), Forces (2-3), Faiblesses (2-3), Contradictions internes (minimum 5 - AgentAdam requirement)

See template in `../../../data/templates/character-templates.yaml#personality_template`

**2.4. Désirs et peurs**
- Ce qu'il veut (conscient), Ce qu'il veut (inconscient), Ses plus grandes peurs, Ses angles morts

**2.5. Contexte et histoire**
- Enfance, Figures clés, Expériences formatrices (2-3), Bagages et blessures

**2.6. Arc de transformation**
- Point de départ, Catalyseurs de changement, Transformation (arc type), Point d'arrivée

See arc types in `../../../data/references/character-frameworks.md#character-arc-types`

**2.7. Compétences et incompétences**
- Compétences utiles (2-3), Incompétences notables (2-3)

**2.8. Relations et connections**
- Avant l'histoire, Dans l'histoire, Dynamique évolutive

**IF story bible has existing characters:** Establish concrete connections.
**IF no other characters exist:** Describe relationship archetypes.

**2.9. Voix et manière d'être**
- Comment il/elle parle, Comment il/elle pense, Tics, habitudes, particularités (2-3)

**2.10. Thèmes explorés**
- Contradictions principales, Question centrale

### 3. Write Complete Dossier

Write all generated content to `{outputFile}`, preserving frontmatter and replacing placeholder sections with generated content.

Ensure format matches template structure with all ## Level 2 headers.

### 4. Update Frontmatter

Update `{outputFile}` frontmatter:

```yaml
stepsCompleted: ['step-01-init', 'step-02b-input', 'step-03b-generate']
lastStep: 'step-03b-generate'
generated: true
generatedDate: {current_date}
```

### 5. Present Generation Summary

"**✅ GENERATION COMPLETE!**"

Display summary:

```
═══════════════════════════════════════════════════════════
  GENERATED: {characterName}
═══════════════════════════════════════════════════════════

  Based on your concept, I've created:

  ✅ Complete 9-section character profile
  ✅ Psychologically grounded personality
  ✅ Distinctive voice and mannerisms
  ✅ Clear transformation arc
  ✅ Meaningful relationships and connections
  ✅ Internal contradictions for depth

  KEY HIGHLIGHTS:
  [3-5 interesting elements from the generated character]

═══════════════════════════════════════════════════════════
```

### 6. Transition to Review

"**The full dossier has been saved.** Would you like to review it?

**[C]** Continue — Review the generated character
**[X]** Exit — Save and review later"

Wait for author selection.

**IF C selected:** Load, read entire file, then execute `{nextStep}`

**IF X selected:** Save progress and exit.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- All 9 sections generated with meaningful content
- Content is specific (not generic placeholders)
- At least 5 genuine contradictions included (AgentAdam requirement)
- Psychology is internally consistent
- Transformation arc is clear and coherent
- Voice is distinctive
- Character aligns with author's concept
- Dossier saved to output file
- Frontmatter updated with step completion

### ❌ SYSTEM FAILURE:

- Generic or placeholder content instead of specific details
- Fewer than 5 genuine contradictions
- Psychology doesn't make sense
- Arc is missing or unclear
- Content contradicts author's concept
- Sections left incomplete

**Master Rule:** Generated characters must be as specific and deep as collaboratively created ones. "Fast" doesn't mean "shallow."

## GENERATION QUALITY STANDARDS:

See: `../../../data/references/character-frameworks.md#quality-standards-reference`

**SPECIFICITY TEST:** Could I swap this character's name for another and have it still work? If yes, it's too generic.

**CONTRADICTION TEST:** Are there at least 5 genuine tensions?

**PSYCHOLOGY TEST:** Do desires, fears, and contradictions form a coherent whole?

**VOICE TEST:** If I removed dialogue tags, would I know this character is speaking?

**ARC TEST:** Is the transformation arc the ONLY way this specific character could change?
