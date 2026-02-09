# Psychological Coherence Analysis Framework

## Overview

Psychological coherence goes beyond individual contradictions to examine the overall consistency of a character's psychology in a chapter. This framework defines the four dimensions that must be assessed.

## Four Dimensions of Psychological Coherence

### 1. Emotional State Analysis

**What to Check:**
- Dominant emotions character experiences in chapter
- Triggers for those emotions
- How emotions change throughout the chapter
- Coherence with current arc phase (Phase X/5)

**Evidence to Gather:**
- Scenes showing emotional state
- Internal monologue if present
- Physical reactions to emotions
- Emotional progression (start → end of chapter)

**Rating Criteria:**
- ✅ COHÉRENT — Emotions correspond to character's arc phase
- ⚠️ DISCORDANT — Emotions seem slightly off or inconsistent
- ❌ INCOHÉRENT — Emotions contradict established psychological state

**Storage Format:**
```yaml
emotionalStateAnalysis:
  dominantEmotions: [list of emotions]
  emotionalProgression: [how emotions change]
  coherenceWithArc: [coherent/discordant/incoherent]
  evidence: [specific chapter examples]
```

### 2. Behavior Patterns Check

**What to Check:**
- Key actions character takes in chapter
- How character responds to situations
- Any unexpected or surprising behaviors
- Alignment with established personality traits

**Evidence to Gather:**
- Specific actions and their context
- Behavior patterns observed
- Comparison with dossier: traits, strengths, weaknesses

**Rating Criteria:**
- ✅ COHÉRENT — Actions match established personality traits
- ⚠️ SURPRENANT mais explicable — Unexpected behavior but justified
- ❌ INCOHÉRENT — Behavior contradicts established personality

**Storage Format:**
```yaml
behaviorPatterns:
  keyActions: [list of key actions]
  personalityMatch: [coherent/surprising/incoherent]
  unexpectedBehaviors: [list if any]
  evidence: [specific chapter examples]
```

### 3. Voice Consistency Check

**What to Check:**
- How character speaks (dialogue patterns)
- How character thinks (internal monologue style)
- Tics, habits, particularities
- Consistency with dossier "Comment il/elle parle" section

**Evidence to Gather:**
- Dialogue examples showing voice
- Internal monologue examples
- Speech patterns (vocabulary, sentence structure, tone)
- Any changes in voice throughout chapter

**Rating Criteria:**
- ✅ COHÉRENT — Voice matches character dossier perfectly
- ⚠️ VARIATIONS mineures — Minor changes acceptable in context
- ❌ INCOHÉRENT — Voice doesn't match established character voice

**Storage Format:**
```yaml
voiceConsistency:
  speechPatterns: [observed in chapter]
  coherenceWithDossier: [coherent/minor variations/incoherent]
  evidence: [specific dialogue examples]
```

### 4. Decision-Making Logic Assessment

**What to Check:**
- What decisions character makes in chapter
- What factors influence those decisions
- Rationality of decisions
- Alignment with desires and fears

**Evidence to Gather:**
- Specific decisions and their context
- Decision-making process if shown
- Comparison with dossier: wants (conscious/unconscious), fears, blind spots

**Rating Criteria:**
- ✅ COHÉRENT — Decisions align with desires/fears
- ⚠️ COMPLEXE — Nuanced decisions that merit discussion
- ❌ INCOHÉRENT — Decisions contradict desires/fears

**Storage Format:**
```yaml
decisionMaking:
  keyDecisions: [list of decisions]
  desireFearAlignment: [coherent/complex/incoherent]
  blindSpotImpact: [if relevant]
  evidence: [specific examples]
```

## Overall Coherence Assessment

### Compilation Matrix

| Dimension | Result | Details |
|-----------|--------|---------|
| État émotionnel | ✅/⚠️/❌ | [brief summary] |
| Patterns de comportement | ✅/⚠️/❌ | [brief summary] |
| Cohérence de la voix | ✅/⚠️/❌ | [brief summary] |
| Logique décisionnelle | ✅/⚠️/❌ | [brief summary] |

### Overall Rating

**✅ EXCELLENTE** — All dimensions are coherent
- Character psychology is consistent throughout chapter
- All four dimensions rated ✅
- Minor ⚠️ acceptable if justified

**⚠️ ACCEPTABLE avec réserves** — Minor issues to monitor
- One or more dimensions rated ⚠️
- No ❌ ratings
- Issues identified but not critical

**❌ PROBLÉMATIQUE** — Significant inconsistencies detected
- One or more dimensions rated ❌
- Requires revision
- Multiple ⚠️ may also indicate problems

### Storage Format

```yaml
psychologicalCoherence:
  overall: [excellent/acceptable/problematic]
  emotionalState: [rating]
  behaviorPatterns: [rating]
  voiceConsistency: [rating]
  decisionMaking: [rating]
  issuesIdentified: [list if any]
```

## Common Pitfalls

**AVOID:**
- Skipping dimensions (must check ALL 4)
- Vague assessments without specific chapter evidence
- Not considering context before marking issues
- Forgetting that character growth may explain changes

**REMEMBER:**
- Context is everything — apparent issues may be justified
- Author feedback is essential for borderline cases
- Psychological coherence allows for growth and change
- Goal is insight, not criticism

## Analysis Best Practices

1. **Be Specific** — Provide concrete chapter evidence for each assessment
2. **Consider Context** — Before marking ❌, ask if there's justification
3. **Look for Patterns** — Are issues isolated or systemic?
4. **Think Developmentally** — Is this change part of character growth?
5. **Stay Constructive** — Feedback should help author improve, not discourage
