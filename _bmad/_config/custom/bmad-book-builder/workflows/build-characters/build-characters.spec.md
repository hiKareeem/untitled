# Workflow Specification: BuildCharacters

**Module:** bmad-book-builder
**Status:** Placeholder — To be created via create-workflow workflow
**Created:** 2026-01-24

---

## Workflow Overview

**Goal:** Create detailed character profiles from author's ideas

**Description:** Character Keeper guides author through structured questioning to create complete character dossiers with psychology, backstory, voice, relationships, and arc.

**Workflow Type:** Create-only

---

## Workflow Structure

### Entry Point

```yaml
---
name: build-characters
description: Create detailed character profiles from ideas
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/build-characters'
---
```

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Character Concept | Get initial character idea from author |
| 2 | Physical Description | Appearance, distinctive traits |
| 3 | Background | History, traumas, formative experiences |
| 4 | Psychology | Fears, desires, contradictions, blind spots |
| 5 | Voice | Speech patterns, vocabulary, mannerisms |
| 6 | Relationships | How they connect to other characters |
| 7 | Arc | Where they start, where they end, how they change |
| 8 | Generate Dossier | Compile into complete character profile |

---

## Workflow Inputs

### Required Inputs

- Character concept or idea

---

## Workflow Outputs

### Output Format

- [X] Document-producing

### Output Files

- `characters/{name}-dossier.md` — Complete character profile

---

## Agent Integration

### Primary Agent

Character Keeper

---

_This is a specification. Use the create-workflow workflow to build this workflow._
