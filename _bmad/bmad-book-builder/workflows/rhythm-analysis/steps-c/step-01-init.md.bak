---
name: Initialization
description: Initialize rhythm analysis and determine the scope
nextStepFile: step-02-load.md
---

# Step 01: Initialization

## Objective

Initialize rhythm analysis and determine the scope (single chapter, range, or full book).

---

## Instructions for the Agent

### 1. Greeting and Context

Briefly introduce yourself as Rex, the Rhythm Monitor:

> "Hey! Rex here, your pacing analyst. I'm going to examine the rhythm of your story - tension, flow, beats. Let's see what's under the hood."

### 2. Load Project Configuration

Check for existence and load:
- `{project-root}/story-bible.md` - for narrative context
- `{project-root}/chapters/` - to list available chapters

> **Reference:** Consult the project context in the story-bible to understand the global narrative frame before defining the scope.

### 3. Determine Analysis Scope

Ask the user what they want to analyze:

**Options:**
1. **Single chapter** - Deep analysis of a specific chapter
2. **Chapter range** - Comparative analysis of multiple chapters
3. **Full book** - Overall pacing overview

```
What are we analyzing today?

1. A specific chapter (detailed analysis)
2. Multiple chapters (comparative analysis)
3. The entire book (overall rhythm overview)

State your choice or the chapter number/title directly.
```

### 4. Validate the Selection

Based on the choice:
- **Single chapter:** Confirm the file exists
- **Range:** List the chapters included
- **Full book:** Confirm total number of chapters

### 5. Initialize Analysis Context

Store in workflow context:
- `scope_type`: single | range | full
- `chapters_to_analyze`: list of chapter files
- `output_filename`: rhythm-chapter-{N}.md | rhythm-chapters-{N}-{M}.md | rhythm-full.md

---

## Validation

Before moving to the next step, confirm:
- [ ] Scope clearly defined
- [ ] Chapters identified and accessible
- [ ] User confirmed the selection

---

## Navigation

**Next step:** [Step 02: Load Content](step-02-load.md)

---

## Technical Notes

- If no chapters exist yet, inform the user and suggest waiting
- For a chapter that was just written (automatic trigger), preselect that chapter
- The story-bible is optional but enriches contextual analysis
