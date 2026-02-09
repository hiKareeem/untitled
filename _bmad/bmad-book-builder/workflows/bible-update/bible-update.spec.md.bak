# Workflow Specification: BibleUpdate

**Module:** bmad-book-builder
**Status:** Specification — Enhanced with AgentAdam analysis
**Created:** 2026-01-24
**Updated:** 2026-01-24
**Priority:** P2 (Standard Feature — Bible Maintenance)

---

## Workflow Overview

**Goal:** Update story bible after chapter completion

**Description:** Character Keeper extracts new information from completed chapters and updates the story bible — characters, locations, objects, timeline, and thematic progression.

**Workflow Type:** Edit-only (continuous updates)

---

## Relationship to Living-Bible Workflow

> **📌 IMPORTANT NOTE**
>
> This **Bible-Update** workflow is a **simplified version** of **Living-Bible**.
>
> **Bible-Update**: Automatic extraction from written chapters
> **Living-Bible**: Full multi-dimensional system with structured tracking
>
> For new projects, **prefer Living-Bible** which offers more depth.
> Bible-Update is useful for quick updates after writing.

---

## Workflow Structure

### Entry Point

```yaml
---
name: bible-update
description: Update story bible after each chapter
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/bible-update'
---
```

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Load Chapter | Load completed chapter content |
| 2 | Extract Chronology | Identify timeline events, day progression |
| 3 | Extract Characters | Track character appearances, states, relationship changes |
| 4 | Extract Locations | Record locations used, resources, events |
| 5 | Extract Objects | Track plot-critical objects, status changes |
| 6 | Extract Themes | Identify thematic advancement in chapter |
| 7 | Validate Continuity | Check for inconsistencies with existing bible |
| 8 | Update Bible | Save all extracted information to bible files |

---

## Extraction Template (per Chapter)

> **Based on the AgentAdam multi-dimensional tracking methodology**

```markdown
## Chapter XX - Extraction

### Chronology
- Day in story: [X]
- Key events: [list]

### Characters present
- [Character 1]: [Actions, psychological state, changes]
- [Character 2]: [Actions, psychological state, changes]

### Locations used
- [Location 1]: [Description, resources used, events]
- [Location 2]: [Description, resources used, events]

### Notable objects
- [Object 1]: [Status, changes, significance]
- [Object 2]: [Status, changes, significance]

### Themes advanced
- [Theme 1]: [How this chapter advances the theme]
- [Theme 2]: [How this chapter advances the theme]

### Inconsistencies detected
- [Any continuity issues found during extraction]
```

---

## Workflow Inputs

### Required Inputs

- Completed chapter content
- Current story bible (for cross-reference)

---

## Workflow Outputs

### Output Format

- [X] Data update
- [X] Document-producing (extraction summary)

### Output Files

- `bible/chronology.md` — Updated timeline
- `bible/characters.md` — Updated character states
- `bible/locations.md` — Updated location records
- `bible/objects.md` — Updated object inventory
- `bible/themes.md` — Updated thematic progression
- `bible/extract-chapter-{XX}.md` — Extraction record for chapter

---

## Agent Integration

### Primary Agent

**Character Keeper** (Bible Guardian)

The Character Keeper is specifically designed as the bible manager.

---

## When to Use This Workflow

- **After completing each chapter** — Extract all new information
- **During revision** — Update bible with changes
- **For continuity checks** — Verify information is tracked correctly

**For comprehensive tracking**, use the **Living-Bible** workflow instead.

---

## Implementation Notes

### Cross-Reference Checks:

When updating one section, verify:
- **Chronology → Characters**: Are characters in the right place at the right time?
- **Characters → Locations**: Do location references match character movements?
- **Characters → Themes**: Do character actions align with thematic arcs?
- **Objects → Chronology**: Are objects created/used at consistent times?

---

## Integration with Other Workflows

- **Living-Bible** — Comprehensive multi-dimensional tracking (preferred)
- **Chapter-Write** — Should trigger bible-update after completion
- **Character-Audit** — Uses bible for character state verification
- **Theme-Tracker** — Integrates with thematic progression

---

_This is a specification. Use the create-workflow workflow to build this workflow._

**Reference Analysis:** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (sections 4, 8)
