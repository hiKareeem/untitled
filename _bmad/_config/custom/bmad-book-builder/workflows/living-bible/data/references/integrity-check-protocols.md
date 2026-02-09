# Integrity Check Protocols

## Bible Dimension Integrity Checks

This document defines the five categories of cross-dimensional integrity checks for the living bible validation system.

## Check Categories

### Category 1: Temporal Coherence (Chronologie)

**Purpose:** Ensure events happen in logical, consistent sequence

**Checks:**
- Events happen after their causes
- Travel times are realistic
- No character in two places at once (same day/time)
- Weather/season consistency maintained

**Cross-Reference:**
- Chronologie events vs character presence in Personnes
- Travel times between Lieux entries
- Cause-effect ordering across dimensions

### Category 2: Spatial Coherence (Lieux)

**Purpose:** Ensure location references are accurate and consistent

**Checks:**
- Referenced locations exist in lieux.md
- Location states match what happened there
- Resource changes are tracked
- Control/ownership is consistent

**Cross-Reference:**
- Locations mentioned in Chronologie exist in Lieux
- Character locations in Personnes match Chronologie events
- Resource states in Lieux match object usage in Objets

### Category 3: Object Coherence (Objets)

**Purpose:** Ensure object existence and state consistency

**Checks:**
- Referenced objects exist in objets.md
- Object locations match where characters left them
- Ownership transfers are documented
- Object states (destroyed, used) are consistent

**Cross-Reference:**
- Objects mentioned in Chronologie exist in Objets
- Object ownership matches character in Personnes
- Object locations match Lieux

### Category 4: Character Coherence (Personnes)

**Purpose:** Ensure character states and relationships are consistent

**Checks:**
- Referenced characters exist in personnes.md
- Psychological phases progress logically (no skipping)
- Relationships are bidirectional
- Character presence matches chronology

**Cross-Reference:**
- Characters in Chronologie exist in Personnes
- Relationship A→B matches B→A
- Psychological phase progression is logical
- Character arcs match their actions in Chronologie

### Category 5: Thematic Coherence (Thèmes)

**Purpose:** Ensure theme tracking is accurate and consistent

**Checks:**
- Theme carriers match character states
- Theme phases progress (not regressing without reason)
- Symbols are used consistently
- Resonances make narrative sense

**Cross-Reference:**
- Theme carriers match characters' current states
- Theme events in Chronologie reflect theme phases
- Theme phases progress logically
- Symbols used consistently

## Issue Severity Levels

### CRITIQUE
- Breaks narrative continuity
- Creates plot holes
- Makes story impossible to follow
- Must be fixed before continuing

**Examples:**
- Character appears in two places simultaneously
- Event happens before its cause
- Object used after being destroyed
- Character skips psychological phases

### AVERTISSEMENT
- Minor inconsistency
- Could confuse readers
- Should be addressed

**Examples:**
- Travel time slightly unrealistic
- Minor relationship asymmetry
- Symbol used inconsistently
- Theme phase unclear

### MINEUR
- Small detail discrepancy
- Doesn't impact comprehension
- Can be ignored if not critical

**Examples:**
- Weather detail inconsistent
- Minor resource count discrepancy
- Relationship intensity slightly off

## Validation Output Template

For each check category, produce:

```markdown
**[Category Name] Coherence Check:**

Vérifications effectuées: [N]
Issues détectées: [N]

[If issues found:]
⚠️ Issue #1: [Brief description]
   - Chronologie dit: [X]
   - Mais: [Y]
   - Suggestion: [how to resolve]
   - Sévérité: [CRITIQUE/AVERTISSEMENT/MINEUR]

Issue #2: [Brief description]
   [...]
```

## Party Mode for Complex Issues

When CRITIQUE issues are found OR user requests discussion:

### Party Mode Participants

- **Timeline Guardian** — perspective temporelle
  - Focus: Event sequencing, cause-effect, travel times
  - Role: Ensures time flows logically

- **Cartographer** — perspective spatiale
  - Focus: Location states, resource tracking, geography
  - Role: Ensures spaces make sense

- **Archivist** — perspective matérielle
  - Focus: Objects, ownership, state changes
  - Role: Ensures items are tracked

- **Keeper of Souls** — perspective psychologique
  - Focus: Character states, relationships, arcs
  - Role: Ensures people behave consistently

- **Thematic Weaver** — perspective sémantique
  - Focus: Themes, symbols, resonances
  - Role: Ensures deeper meanings cohere

### Party Mode Process

1. Present each complex issue to all perspectives
2. Each guardian analyzes from their viewpoint
3. Discussion of potential resolutions
4. Consensus on recommended fix
5. Document resolution approach

## Related References

- **Validation Procedures:** See `validation-protocols.md`
- **Step Implementation:** See `step-v-02-integrity.md`
- **Menu Options:** See `bible-edit-protocols.md`
