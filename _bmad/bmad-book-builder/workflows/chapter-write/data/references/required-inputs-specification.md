# Chapter Write - Required Inputs Specification

## Overview

The Chapter Write workflow requires **exactly 7 inputs** to be loaded and verified before proceeding. All inputs are MANDATORY - the workflow cannot proceed without complete context.

## Required Inputs

### Input 1: Chapter Plan

**Location:** `{chapterPlanFolder}/chapter-plan-{chapter_number}.md`

**Contains:**
- Scene breakdown for the chapter
- Chapter objectives and goals
- Plot points to address
- Required conflicts
- Thematic beats
- Transformation objectives

**Validation:**
- IF FOUND: "✅ Chapter plan found"
- IF MISSING: "❌ Chapter plan not found. Please run Foundation workflow first."

**Usage:**
- Guides scene-by-scene writing
- Ensures all required plot points are addressed
- Maintains alignment with story structure

---

### Input 2: Style Profile

**Location:** `{styleProfilePath}`

**Contains:**
- Author's quantitative voice metrics:
  - TTR (Type-Token Ratio)
  - Sentence length distribution
  - Sentence complexity ratios
  - Vocabulary patterns
- Author's qualitative preferences:
  - Imagery preferences
  - Dialogue style
  - Narrative distance
  - Show vs tell balance

**Validation:**
- IF FOUND: "✅ Style profile found"
- IF MISSING: "❌ Style profile not found. Please run StyleCapture workflow first."

**Usage:**
- Guides writing to match author's authentic voice
- Sets quality thresholds for revision
- Ensures consistency with established style

---

### Input 3: Story Bible

**Location:** `{storyBiblePath}` (directory with bible-*.md files)

**Contains (5 dimensions):**

1. **Characters**
   - Physical descriptions
   - Personality traits
   - Speech patterns
   - Background and history
   - Relationships

2. **Locations**
   - Physical descriptions
   - Layout and geography
   - Atmosphere and mood
   - Relationship to story

3. **Objects**
   - Important items
   - Symbolic meaning
   - Physical properties

4. **Chronology**
   - Timeline of events
   - Sequences and causality
   - Pacing information

5. **Themes**
   - Central themes
   - Motifs and symbols
   - Thematic arcs

**Validation:**
- IF FOUND: "✅ Story bible found ({N} files)"
- IF MISSING: "❌ Story bible not found. Please ensure bible exists."

**Usage:**
- Ensures consistency across all story elements
- Prevents contradictions
- Maintains narrative continuity

---

### Input 4: Previous Chapter Summaries

**Location:** `{chaptersFolder}/chapter-*-meta.yaml` for chapters 1 to N-1

**Conditional:** Required ONLY if `{chapter_number}` > 1

**Contains:**
- Chapter summaries
- Key plot points from each previous chapter
- Character states at end of each chapter
- Thematic progression
- unresolved threads

**Validation:**
- IF chapter_number > 1 AND ALL FOUND: "✅ Previous chapter summaries found (chapters 1-{N-1})"
- IF chapter_number > 1 AND MISSING ANY: "❌ Missing summaries for chapter(s) [X, Y]. Complete those chapters first."
- IF chapter_number == 1: "✅ First chapter - no previous summaries needed"

**Usage:**
- Maintains narrative continuity
- Prevents contradictions with previous events
- Tracks character arcs and progression
- Ensures proper pacing and rhythm

---

### Input 5: Thematic Context

**Location:** `{thematicContextPath}`

**Contains:**
- Current theme states
- Thematic arcs in progress
- Motif usage patterns
- Symbolic elements
- Emotional arcs
- Theme progression targets

**Validation:**
- IF FOUND: "✅ Thematic context found"
- IF MISSING: "❌ Thematic context not found. Please run Thematic Weaver analysis first."

**Usage:**
- Ensures thematic continuity
- Guides thematic development in chapter
- Prevents thematic contradictions
- Maintains symbolic consistency

---

### Input 6: Rhythm Guidelines

**Location:** `{rhythmGuidelinesPath}`

**Contains:**
- Pacing patterns
- Sentence distribution targets
- Paragraph length patterns
- Scene length targets
- Chapter rhythm goals
- Tension/release patterns

**Validation:**
- IF FOUND: "✅ Rhythm guidelines found"
- IF MISSING: "❌ Rhythm guidelines not found. Please run Rhythm Monitor analysis first."

**Usage:**
- Maintains appropriate pacing
- Ensures rhythm consistency
- Guides sentence and paragraph structure
- Balances tension and release

---

### Input 7: Character Dossiers

**Location:** Derived from Story Bible and Build Characters workflow

**Contains for each character in the chapter:**
- Psychological state (phase 1-5)
- Core contradictions
- Blind spots
- Arc progression
- Current goals and motivations
- Relationships and dynamics

**Validation:**
- Checked as part of Story Bible validation
- Specifically verified in Pre-Writing Checklist

**Usage:**
- Ensures authentic character behavior
- Guides character development
- Maintains psychological consistency
- Tracks character arcs

## Input Discovery Results Table

When all inputs have been discovered, present:

```markdown
## Input Discovery Results

| Input | Status | Path |
|-------|--------|------|
| Chapter Plan | ✅/❌ | {path} |
| Style Profile | ✅/❌ | {path} |
| Story Bible | ✅/❌ | {path} |
| Previous Summaries | ✅/❌ | {count} files |
| Thematic Context | ✅/❌ | {path} |
| Rhythm Guidelines | ✅/❌ | {path} |
```

## Failure Handling

**IF ANY INPUT MISSING:**
- Display discovery results table
- "Cannot proceed - missing required inputs. Please complete the workflows indicated above."
- STOP workflow

**IF ALL INPUTS FOUND:**
- "All required inputs found! Loading context..."
- Proceed to load all inputs

## Master Rule

**ALL 7 inputs are REQUIRED.** Do not proceed without complete context. Missing any input will result in quality issues, inconsistencies, or continuity errors.
