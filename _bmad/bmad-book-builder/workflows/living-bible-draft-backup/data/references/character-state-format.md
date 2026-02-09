# Character State Format Reference

This document provides the standard format for character state entries in the living bible.

## Template Structure

```markdown
### [Character Name]

**Current psychological state:**
- Phase: [X/5] ([Phase name])
- Emotional state: [Emotional state description]
- Dominant beliefs: "[Core belief]"
- Internal contradictions: [Internal conflicts]

**Current relationships:**
| Character | Relationship | Intensity | Dynamics |
|------------|--------|-----------|-----------|
| [Name 1] | [Relationship type] | [Intensity] | [Dynamic description] |
| [Name 2] | [Relationship type] | [Intensity] | [Dynamic description] |

**Current arc:** [Arc name, e.g., "Individualism → Collectivism"]
- Current phase: [X/5] ([Phase name])
- Progression: [Progress status]
- Next step: [Next step description]

**Appearances:**
- Last appearance: Chapter [N]
- Next planned appearance: Chapter [N]

**Recent history:**
- Chapter [N]: [Event description] (Phase change if applicable)
- Chapter [N]: [Event description] (consolidation/change)
```

## Example

```markdown
### Marc

**Current psychological state:**
- Phase: 3/5 (Turning Point)
- Emotional state: Growing doubt, fear of failure
- Dominant beliefs: "I must control everything to protect others"
- Internal contradictions: Wants to protect but suffocates

**Current relationships:**
| Character | Relationship | Intensity | Dynamics |
|------------|--------|-----------|-----------|
| Elise | Rival/Ally | High | Leadership tension |
| Julie | Romantic interest | Medium | Fragile alliance |
| Chen | Subordinate | Declining | Loyalty questioned |

**Current arc:** Individualism → Collectivism
- Current phase: 3/5 (Control crisis)
- Progression: In progress (first doubts)
- Next step: Forced letting go

**Appearances:**
- Last appearance: Chapter 12
- Next planned appearance: Chapter 14

**Recent history:**
- Chapter 10: Confrontation with Elise (Phase 2→3)
- Chapter 12: Doubts about his decisions (consolidation Phase 3)
```

## Field Definitions

### Psychological State
- **Phase (X/5)**: Current position in psychological arc (see Psychological Phases Reference)
- **Emotional state**: Brief description of current emotional state
- **Dominant beliefs**: Core belief system driving character behavior
- **Internal contradictions**: Internal conflicts creating tension

### Relationships Table
- **Character**: Related character name
- **Relationship**: Type of relationship (rival, ally, romantic, subordinate, etc.)
- **Intensity**: Low/Medium/High intensity level
- **Dynamics**: Description of relationship dynamics

### Arc Progression
- **Current arc**: Name of character arc (typically "From → To" format)
- **Current phase**: Current phase number/name
- **Progression**: Status of progression
- **Next step**: Expected next development

### Appearances
- **Last appearance**: Last chapter where character appeared
- **Next planned appearance**: Next planned appearance (if known)

### Recent History
- **Chapter [N]**: Chapter number and event description
- Note phase changes in parentheses
