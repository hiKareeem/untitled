# Workflow Specification: ThemeTracker

**Module:** bmad-book-builder
**Status:** Specification — Enhanced with AgentAdam analysis
**Created:** 2026-01-24
**Updated:** 2026-01-24
**Priority:** P2 (Standard Feature — Thematic Depth)

---

## Workflow Overview

**Goal:** Track thematic and emotional progression throughout narrative

**Description:** Thematic Weaver analyzes chapters for thematic thread presence, emotional beats, and character development moments. Maintains comprehensive tracking of how themes evolve from introduction to resolution.

**Workflow Type:** Edit-only (continuous tracking)

---

## Why This Workflow Exists

> **🎯 COMPLEMENT TO AGENTADAM VS BBB ANALYSIS**
>
> AgentAdam has a thematic tracking system with explicit chapter-by-chapter progression and character-theme connections. BBB should offer the same capability.
>
> **Without thematic tracking, themes become blurry** and lose their emotional impact.
>
> **Reference:** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (sections 8, 10)
>
> **Impact:** MEDIUM — Essential for thematic novels
> **Effort:** MEDIUM — Structured tracking system

---

## Workflow Structure

### Entry Point

```yaml
---
name: theme-tracker
description: Track thematic and emotional progression
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/theme-tracker'
---
```

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Load Chapter | Load chapter content |
| 2 | Identify Themes | Detect which thematic threads are present |
| 3 | Map Emotions | Track character emotional beats |
| 4 | Analyze Arc | Map character development per theme |
| 5 | Update Progression | Document how themes advanced in this chapter |
| 6 | Verify Consistency | Check thematic coherence with previous chapters |

---

## Theme Structure (from AgentAdam analysis)

```markdown
## Theme: [Theme Name] — e.g., "Trust vs Distrust"

### Core Question
[The central question this theme explores]

### Tension
[Opposing forces that create the theme]

### Progression by Chapter Phase
- **Chapter 1-5**: [Introduction phase — how theme is introduced]
- **Chapter 6-10**: [Exploration phase — how theme is tested]
- **Chapter 11-15**: [Deepening phase — crisis point for theme]
- **Chapter 16-20**: [Resolution phase — how theme resolves]
- **Chapter 21-25**: [Final state — where theme ends]

### Character Connections
- **Character 1**: [How they embody theme, their arc]
- **Character 2**: [How they embody theme, their arc]
- **Character 3**: [How they embody theme, their arc]

### Per-Chapter Progression
| Chapter | Theme Event | Character Impact | Next Step |
|---------|-------------|------------------|-----------|
| 1 | Theme introduced | Initial positions | Setup for chapter 2 |
| 2 | First test | Complications | Setup for chapter 3 |
| ... | ... | ... | ... |
```

---

## Example from AgentAdam

```markdown
## Theme: Trust vs Distrust

### Progression
- Chapter 1-5: Dominant distrust (individual survival)
- Chapter 6-10: First openings (need for the group)
- Chapter 11-15: Trust crisis (betrayal or sacrifice)
- Chapter 16-20: Reconstruction (new dynamics)
- Chapter 21-25: Resolution (trust won or lost)

### Character Connections
- Marc: Arc from distrust → trust → ultimate test
- Julie: Naive trust → betrayal → healed distrust
- Chen: Pragmatic distrust → selective trust
```

---

## Workflow Inputs

### Required Inputs

- Chapter content
- Current thematic tracking data

---

## Workflow Outputs

### Output Format

- [X] Data update
- [X] Document-producing (theme tracking)

### Output Files

- `tracking/themes.md` — Complete theme tracking with progression
- `tracking/emotions.md` — Emotional arc data per character
- `tracking/chapter-{XX}-themes.md` — Theme analysis per chapter

---

## Agent Integration

### Primary Agent

**Thematic Weaver** (Theme & Emotion Tracker)

Specializes in tracking themes and emotions throughout the narrative.

---

## When to Use This Workflow

- **After each chapter** — Update theme progression
- **During Foundation** — Establish main themes and their arcs
- **During revision** — Verify thematic consistency
- **Before final manuscript** — Ensure all themes resolve

---

## Automatic Trigger

> **🎯 AUTOMATIC TRIGGER**
>
> This workflow is **automatically triggered** by the **Chapter-Write** workflow after each chapter is finalized.
>
> **When:** After Step 7 (Finalize) of Chapter-Write
> **Condition:** Always triggered (each chapter advances themes)
> **Mode:** The user can choose to run immediately or defer

**This ensures that thematic progression is systematically tracked throughout the entire story.**

---

## Implementation Notes

### Thematic Depth Indicators:

A well-tracked theme should have:
1. **Clear question** — What is this theme really about?
2. **Opposing forces** — What creates the tension?
3. **Character connections** — Who embodies which side?
4. **Progression** — How does it evolve from start to finish?
5. **Resolution** — Does it resolve (and how)?

### Red Flags:

- ❌ Theme mentioned but never explored
- ❌ Character positions on theme never change
- ❌ Theme introduced but dropped
- ❌ No clear resolution (unless deliberate ambiguity)

---

## Integration with Other Workflows

- **Foundation** — Initial theme identification
- **Living-Bible** — Theme progression is one dimension
- **Bible-Update** — Extracts thematic info from chapters
- **Character-Audit** — Verify character thematic consistency

---

_This is a specification. Use the create-workflow workflow to build this workflow._

**Reference Analysis:** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (section 8)
