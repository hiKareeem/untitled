# Workflow Specification: LivingBible

**Module:** bmad-book-builder
**Status:** ✅ IMPLEMENTED (13 files, edit-only workflow)
**Created:** 2026-01-24
**Implemented:** 2026-01-24
**Priority:** P1 (Major Gap — Multi-Dimensional Story Tracking)

---

## Workflow Overview

**Goal:** Maintain a living, multi-dimensional story bible that evolves with the narrative

**Description:** Character Keeper (Bible Guardian) manages a comprehensive story bible that tracks chronology, locations, objects, character states, and themes as they evolve throughout the writing process. Unlike static bibles, this is a living document updated after each chapter.

**Workflow Type:** Edit-only (continuous updates throughout writing)

---

## Why This Workflow Exists

> **🎯 MAJOR GAP IDENTIFIED — AgentAdam vs BBB Analysis**
>
> AgentAdam has a **living narrative bible** with multi-dimensional tracking (chronology, locations, objects, characters, themes). BBB only has a basic update workflow.
>
> **Without this workflow, long-term continuity is difficult.** Details get lost and inconsistencies accumulate.
>
> **Reference:** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (section 4)
>
> **Impact:** MEDIUM — Essential for multi-chapter novels with multiple characters
> **Effort:** HIGH — Complex multi-dimensional tracking system

---

## Workflow Structure

### Entry Point

```yaml
---
name: living-bible
description: Maintain living, multi-dimensional story bible
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/living-bible'
---
```

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Select Update Trigger | Choose what event triggers update (chapter written, major event, character transformation) |
| 2 | Update Chronology | Add day-by-day events, timeline progression |
| 3 | Update Locations | Record new locations, resource changes, events per location |
| 4 | Update Objects | Track object inventory, origins, significance |
| 5 | Update Character States | Record current psychological states, relationship changes |
| 6 | Update Theme Progression | Track how themes evolve per chapter |

---

## Multi-Dimensional Tracking System

> **Based on AgentAdam's tracking system (section 4 of the analysis)**

### Dimension 1: Chronology (Timeline)
```markdown
## Chronology

### Day 47
- Morning: Marc explores the industrial sector
- Noon: Discovery of the survival pods
- Afternoon: Confrontation with Elise
- Evening: Council meeting

### Day 48
- [Events continue...]
```

**Purpose:** Track day-by-day progression, verify timing consistency

### Dimension 2: Locations (Locations)
```markdown
## Locations

### Industrial Sector
- Discovered: Day 12
- Resources: Tools, materials, old stockpiles
- Key events:
  - Day 12: First exploration
  - Day 47: Discovery of the pods
  - Day 50: Conflict over control
- Characters present: Marc, Julie, Chen
- Current state: Controlled by Marc's group
```

**Purpose:** Track location inventory, resources, events, occupants

### Dimension 3: Objects (Objects)
```markdown
## Objects

### Survival pods
- Origin: Industrial sector, relic of the Old World
- Discovered: Day 47
- Quantity: 12 pods
- Significance: Symbol of hope vs limited resource = conflict
- Current owner: Controlled by Marc (tension)
- Status: 3 used, 9 remaining
```

**Purpose:** Track plot-critical objects, their status and significance

### Dimension 4: Characters (Character States)
```markdown
## Characters

### Marc
- Current psychological state: Phase 3/5 (Turning Point)
- Current relationships:
  - Elise: High tension (leadership conflict)
  - Julie: Fragile alliance (romantic interest)
  - Chen: Growing doubt (loyalty in question)
- Last appearance: Chapter 12
- Next planned appearance: Chapter 14
- Current arc: Individualism → Collectivism (in progress)

### [Other characters...]
```

**Purpose:** Track character states, relationships, arc progression

### Dimension 5: Themes (Themes)
```markdown
## Themes

### Trust vs Mistrust
- Progression:
- Chapter 1-5: Dominant mistrust (individual survival)
- Chapter 6-10: First openings (need for the group)
- Chapter 11-15: Trust crisis (betrayal or sacrifice)
- Chapter 16-20: Rebuilding (new dynamic)
- Chapter 21-25: Resolution (trust gained or lost)
- Character-theme connections:
  - Marc: Mistrust → trust → ultimate test arc
  - Julie: Naive trust → betrayal → healed mistrust
  - Chen: Pragmatic mistrust → selective trust
- Current chapter: 12 (Phase 3 - Crisis)
```

**Purpose:** Track thematic evolution, character-theme connections

---

## Workflow Inputs

### Required Inputs

- Trigger event type (chapter written, major event, character transformation)
- Chapter number (if chapter written)
- Chapter content (for extracting updates)

---

## Workflow Outputs

### Output Format

- [X] Document-producing (living bible updates)

### Output Files

- `bible/chronology.md` — Day-by-day timeline
- `bible/locations.md` — Location database with resources
- `bible/objects.md` — Object inventory and significance
- `bible/characters.md` — Character state tracking
- `bible/themes.md` — Theme progression mapping

---

## Agent Integration

### Primary Agent

**Character Keeper** (Bible Guardian)

The Character Keeper already exists and is specifically designed as "Bible Guardian" — this workflow gives them the structured framework they need.

---

## Update Triggers

The workflow should be activated when:

1. **After each chapter is written** — Extract all new information from chapter
2. **Major events occur** — Deaths, revelations, location changes
3. **Characters transform** — Psychological breakthroughs, relationship changes
4. **Themes shift** — Thematic progression reaches new phase

---

## Implementation Notes

### Critical Features (from AgentAdam analysis):

1. **Multi-Dimensional Tracking**: 5 simultaneous tracking dimensions
2. **Living Document**: Bible evolves with story, not static
3. **Cross-Referenced**: Each dimension references others (location → characters present, object → significance)
4. **Extractable**: Information can be extracted for audits, reviews, continuity checks
5. **Searchable**: Quick lookup of character states, locations, objects

### File Structure (from AgentAdam):
```
bible/
├── chronologie.md      # Day-by-day timeline
├── lieux.md            # Location database
├── objets.md           # Object inventory
├── personnes.md        # Character states
└── themes.md           # Theme progression
```

---

## When to Use This Workflow

- **After completing each chapter** — Update all dimensions
- **During revision** — Verify continuity, fix inconsistencies
- **Before writing new chapter** — Check current states for reference
- **For manuscript review** — Extract summary for review

---

## Integration with Other Workflows

- **Character-Audit**: Uses `personnes.md` for current states
- **Chapter-Write**: References bible for continuity
- **Review**: Uses bible for comprehensive check
- **Export-Bible**: Compiles all dimensions into single document

---

## Future Enhancements

- Searchable index across all dimensions
- Visualization tools (timeline, relationship maps)
- Change tracking (what changed between chapters)
- Alert system (potential inconsistencies detected)

---

_This specification has been implemented. See `workflow.md` for the implementation._

**Reference Analysis:** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (sections 4, 8)

**Implementation Details:**
- 6 edit steps covering all 5 dimensions
- 5 bible templates for initialization
- Multi-trigger support (chapter, event, transformation, theme shift)
- Cross-reference capability between dimensions
