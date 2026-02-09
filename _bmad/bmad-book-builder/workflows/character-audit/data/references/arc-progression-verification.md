# Arc Progression Verification Framework

## Overview

Arc progression verification tracks where a character starts psychologically in a chapter, where they end, what changed (if anything), and whether this aligns with their established transformation trajectory.

## Core Concept: Character Arc as Journey

A character arc is a psychological journey from Point A to Point B. Each chapter is either:
- **Transformation chapter** — Character changes significantly
- **Maintenance chapter** — Character's state is maintained
- **Regression chapter** — Character moves backward (may be intentional)
- **Setup chapter** — Groundwork is laid for future change

## Verification Process

### Step 1: Load Arc from Character Dossier

Extract the **Arc de transformation** section:

```yaml
arcFromDossier:
  startingPoint: [Starting point]
  catalysts: [Catalysts of change]
  transformation: [Planned transformation]
  endingPoint: [Ending point]
  currentPhase: [Phase actuelle 1-5 if tracked]
```

**Identify Arc Structure Type:**
- 5-Phase psychological structure (if applicable)
- 3-Act structure
- Custom arc
- Not specified

### Step 2: Identify Character State at Chapter Start

**Key Psychological Markers:**
- **Emotional state:** How do they feel?
- **Self-perception:** How do they see themselves?
- **Relationships:** Key relationship states
- **Goals:** What do they want?
- **Obstacles:** What's in their way?

**Phase Marker (if applicable):**
- Phase [X]/5 : Brief description of psychological state

**Evidence Required:**
- Specific text, dialogue, or narration showing state
- Scene references
- Internal monologue or actions that reveal state

**Storage Format:**
```yaml
chapterStart:
  emotionalState: [description]
  selfPerception: [description]
  relationships: [key states]
  goals: [what they want]
  obstacles: [what blocks them]
  phaseMarker: [X]/5 if applicable
  evidence: [chapter references]
```

### Step 3: Identify Character State at Chapter End

**Same Key Markers as Start:**
- Emotional state (has it changed?)
- Self-perception (any shift?)
- Relationships (any evolution?)
- Goals (still want same thing? or changed?)
- Obstacles (new? overcome? still present?)

**Phase Marker (if applicable):**
- Phase [X]/5 : Brief description
- Note if phase has CHANGED from start

**Evidence Required:**
- Specific text, dialogue, or narration showing end state
- Scene references
- Contrast with start state

**Storage Format:**
```yaml
chapterEnd:
  emotionalState: [description]
  selfPerception: [description]
  relationships: [key states]
  goals: [what they want now]
  obstacles: [current state]
  phaseMarker: [X]/5 if applicable
  phaseChange: [yes/no + what changed]
  evidence: [chapter references]
```

### Step 4: Identify the Transformation Moment

**Does transformation occur in this chapter?**

**IF YES — Identify the Moment:**
- **Scene:** Where does it happen?
- **Trigger:** What causes the change?
- **Type:** Breakthrough / Breakdown / Realization / Decision / etc.
- **Before:** State before moment
- **After:** State after moment

**Evidence:** Specific text showing the transformation moment

**IF NO — Note This:**
"This chapter MAINTAINS the psychological state without major transformation. This is valid — not every chapter must have dramatic change."

**Storage Format:**
```yaml
transformation:
  hasTransformation: [true/false]
  moment: [description if true]
  scene: [where it happens]
  trigger: [what causes it]
  type: [breakthrough/breakdown/etc]
  evidence: [chapter references]
```

### Step 5: Assess Arc Progression

**Compare chapter start → chapter end against established arc**

**Alignment Designations:**

✅ **ON TRACK** — Progression coherent with the planned arc
- Character moves in expected direction
- Phase advancement (if applicable) makes sense
- Transformation serves overall arc

⚠️ **SHIFT** — Arc evolves differently (may be valid)
- Character develops in unexpected way
- May indicate natural story evolution
- Discuss with author to verify intention

❌ **REGRESSION** — The character moves backward (justification required)
- Character moves backward in development
- May be intentional (setback, learning moment)
- Requires clear justification

⚪ **NEUTRAL** — No significant progression (maintenance chapter)
- Character state maintained
- No significant change
- Valid for non-transformation chapters

**Phase Progression (if 5-phase structure applies):**
- Start: Phase [X]
- End: Phase [X or X+1 or X-1]
- Assessment: Coherent / Advance too fast / Regression / Stagnation

**Storage Format:**
```yaml
arcProgression:
  alignment: [on track/shift/regression/neutral]
  phaseProgression: [if applicable]
  assessment: [detailed explanation]
  concerns: [any concerns if applicable]
```

### Step 6: Map to Story Context

**Where does this fit in the overall story?**
- Chapter {N} of [total if known]
- Approximately X% through the story
- This chapter is in: [Phase 1-5 if using structure]

**Is this the right time for this progression?**
- ✅ YES — Appropriate for story position
- ⚠️ MAYBE — Could be paced differently
- ❌ NO — Too early / too late / misaligned

**Next Steps Anticipated:**
- Based on this progression, what should come next?
- What groundwork does this lay for future chapters?

## Synthesis Format

**📈 Arc progression summary**

**State at the start of the chapter:**
[summary from chapterStart]

**State at the end of the chapter:**
[summary from chapterEnd]

**Transformation :** [YES / NO]
[If YES: Description of the transformation moment]

**Arc evaluation:** [on track / shift / regression / neutral]
[Detailed assessment]

**Next anticipated step:**
[What should come next based on this progression]

## Common Pitfalls

**AVOID:**
- Missing transformation moments or inventing them
- Not providing clear before/after states
- Not assessing alignment with established arc
- Forgetting that maintenance chapters are valid

**REMEMBER:**
- Not every chapter needs transformation
- Regression can be intentional (setback before growth)
- Arcs can evolve naturally (SHIFT is valid)
- Context and story position matter

## Verification Best Practices

1. **Be Precise** — Clearly identify start and end states
2. **Pinpoint Change** — If transformation occurs, locate the exact moment
3. **Consider Pacing** — Is this the right time in the story for this change?
4. **Think Ahead** — What does this progression set up for future chapters?
5. **Stay Flexible** — Arcs can evolve; SHIFT is not necessarily failure
