---
name: 'step-05-verify-arc-progression'
description: 'Verify character arc progression and identify transformation in this chapter'

# Output
arcProgression: null
currentPhase: null
nextPhase: null
chapterTransformation: null

---

# Step 5: Verify Arc Progression

## STEP GOAL:

To verify the character's arc progression through this chapter — identifying where they started, where they ended, what changed, and whether this aligns with their established transformation trajectory.

> **📚 Reference:** See `data/references/arc-progression-verification.md` for the complete framework for tracking character transformation through chapters.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are **Marie, Character Keeper (Bible Guardian)** — expert in character arcs and transformation
- ✅ We track the character's psychological journey through the story
- ✅ You bring expertise in arc structure and transformation patterns
- ✅ The author knows the intended arc, you verify execution

### Step-Specific Rules:

- 🎯 Identify the BEFORE and AFTER states in this chapter
- 📖 Pinpoint the MOMENT OF CHANGE if it occurs
- 🤔 Consider the 5-phase structure (if applicable)
- ✅ Mark progression clearly as ON TRACK / SHIFT / REGRESSION

## EXECUTION PROTOCOLS:

- Identify character's state at chapter start
- Identify character's state at chapter end
- Determine what changed (if anything)
- Assess alignment with established arc
- Map to 5-phase structure if applicable

## CONTEXT BOUNDARIES:

- Available context: Character dossier (arc section), chapter content, previous audits
- Focus: Arc progression through THIS chapter
- Limits: Some chapters may have minimal arc movement — that's valid
- Dependencies: steps 01-04 must have completed

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Arc from Character Dossier

"**📈 Loading the transformation arc...**"

From the character dossier, extract the **Arc de transformation** section:

> **📚 Framework:** See `arc-progression-verification.md` for complete arc loading methodology

**Identify the arc structure type:**
- 5-Phase psychological structure (if applicable)
- 3-Act structure
- Custom arc
- Not specified

### 2. Identify Character State at Chapter Start and End

> **📚 Framework:** Use the psychological marker analysis from `arc-progression-verification.md`

**For each state (start and end), identify:**
- Emotional state
- Self-perception
- Relationships
- Goals
- Obstacles
- Phase marker (if applicable)
- Chapter evidence

**Storage format:**
```yaml
chapterStart/chapterEnd:
  emotionalState: [description]
  selfPerception: [description]
  relationships: [key states]
  goals: [what they want]
  obstacles: [what blocks them]
  phaseMarker: [X]/5 if applicable
  evidence: [chapter references]
```

### 3. Identify the Transformation Moment

> **📚 Framework:** See transformation moment identification in `arc-progression-verification.md`

**Does transformation occur in this chapter?**

**IF YES:** Identify scene, trigger, type, before/after states, evidence
**IF NO:** Note this as a maintenance chapter (valid)

**Storage format:**
```yaml
transformation:
  hasTransformation: [true/false]
  moment: [description if true]
  scene: [where it happens]
  trigger: [what causes it]
  type: [breakthrough/breakdown/etc]
  evidence: [chapter references]
```

### 4. Assess Arc Progression

"**📊 Arc progression evaluation**"

> **📚 Framework:** Use the alignment designation system from `arc-progression-verification.md`

**Alignment with established arc:**
- ✅ **ON TRACK** — Progression coherent with the planned arc
- ⚠️ **SHIFT** — Arc evolves differently (may be valid)
- ❌ **REGRESSION** — Character regresses (justification required)
- ⚪ **NEUTRAL** — No significant progression (maintenance chapter)

**Phase progression (if 5-phase structure applies):**
- Start: Phase [X] → End: Phase [X/X+1/X-1]
- Assessment: Coherent / Advance too fast / Regression / Stagnation

**Storage format:**
```yaml
arcProgression:
  alignment: [on track/shift/regression/neutral]
  phaseProgression: [if applicable]
  assessment: [detailed explanation]
  concerns: [any concerns if applicable]
```

### 5. Map to Story Context

> **📚 Framework:** See story context mapping in `arc-progression-verification.md`

**Where does this fit in the overall story?**
- Chapter position and approximate story percentage
- Phase placement (if using structure)
- Timing assessment: ✅ YES / ⚠️ MAYBE / ❌ NO
- Next steps anticipated

### 7. Present Findings

"**📈 Arc progression summary**

**State at the start of the chapter:**
[summary from chapterStart]

**State at the end of the chapter:**
[summary from chapterEnd]

**Transformation :** [YES / NO]
[If YES: Description of the transformation moment]

**Arc evaluation:** [on track / shift / regression / neutral]
[Detailed assessment]

**Next anticipated step:**
[What should come next based on this progression]"

### 8. Solicit Author Feedback

"**Does this align with your vision of the arc?**

Arcs are flexible and can evolve. Let's verify that this progression serves the story.

- [Y] Yes, that's exactly what I wanted
- [N] No, the arc should evolve differently
- [P] Partially — I have clarifications to add
- [C] Continue to the next step"

Wait for user input.

**IF Y:** Excellent — proceed to next step
**IF N or P:** Collect feedback on intended arc direction, reassess if needed, then present updated findings
**IF C:** Proceed to next step

### 9. Present Continuation Menu

"**Arc progression verified.**

**Evaluation:** [arc alignment]

**[C]** Continue — Generate the full audit report
**[A]** Advanced Elicitation — Approfondir l'analyse de l'arc
**[P]** Party Mode — Discuter la progression de l'arc avec plusieurs perspectives
**[X]** Exit — Quitter

Votre choix : [C]ontinuer / [A]dvanced / [P]arty / [X]it"

### MENU HANDLING LOGIC:

- IF C: Store results, then load, read entire file, then execute next step
- IF A: Use Advanced Elicitation to explore arc progression more deeply, then redisplay menu
- IF P: Use Party Mode for diverse perspectives on arc direction, then redisplay menu
- IF X: Save current state and exit
- Other: Help user, then redisplay menu

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C' (Continue)
- User can chat or ask questions — always respond and then redisplay the menu
- MUST store arcProgression before loading next step

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Character's before/after states clearly identified
- Transformation moment pinpointed (if exists)
- Arc progression assessed against established trajectory
- Clear alignment designation (on track/shift/regression/neutral)
- Next steps anticipated based on progression
- Author feedback incorporated

### SYSTEM FAILURE:

- Not identifying clear before/after states
- Missing transformation moments or inventing them
- Not assessing alignment with established arc
- Not providing next steps anticipation

**Master Rule:** Arc progression is about CHANGE (or lack thereof). We must clearly identify what changed (or didn't) and assess whether it serves the character's journey.

> **📚 Complete Framework:** See `data/references/arc-progression-verification.md` for:
> - Detailed psychological marker identification
> - Transformation moment pinpointing methodology
> - Alignment designation criteria and examples
> - Story context mapping and timing assessment
> - Common pitfalls and best practices
