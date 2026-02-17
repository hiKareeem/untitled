# Chapter Write - Required Inputs Specification

## Overview

The Chapter Write workflow requires **exactly 7 inputs** to be loaded and verified before proceeding. All inputs are MANDATORY - the workflow cannot proceed without complete context.

## Required Inputs

### Input 1: Chapter Plan

**Location:** `{chapterPlanPath}` (single file containing all chapters)

**Contains:**
- Scene breakdown for ALL chapters (extract the relevant chapter's section)
- Chapter objectives and goals
- Plot points to address
- Required conflicts
- Thematic beats
- Transformation objectives
- Epigraph assignments
- In-chapter rhetoric references

**Validation:**
- IF FOUND: "✅ Chapter plan found (Ch {chapter_number} details extracted)"
- IF MISSING: "❌ Chapter plan not found at {chapterPlanPath}."

**Usage:**
- Guides scene-by-scene writing
- Ensures all required plot points are addressed
- Maintains alignment with story structure
- Extract ONLY the section for the target chapter number

---

### Input 2: Style Profile

**Location:** `{styleProfilePath}` (YAML format)

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
- Full POV Register with per-character voice notes
- AEGIS Full Style Exemption section
- Meta-Narrative Framing reference

**Validation:**
- IF FOUND: "✅ Style profile found"
- IF MISSING: "❌ Style profile not found. Please run StyleCapture workflow first."

**Usage:**
- Guides writing to match author's authentic voice
- Sets quality thresholds for revision
- Ensures consistency with established style

---

### Input 3: Story Bible

**Location:** `{storyBiblePath}` (directory with 5 .md files: characters, locations, objects, chronology, themes)

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

**Location:** `{thematicContextPath}` (primary: bible/themes.md)

**Additional sources (load if available):**
- Per-chapter thematic analysis: `{bbb_output_folder}/current-book/tracking/chapter-{N}-themes.md` (for previous chapters)
- Cumulative themes tracking: `{bbb_output_folder}/current-book/tracking/themes.md`

**Contains:**
- 8 central themes with definitions and progression
- Thematic arcs in progress
- Motif usage patterns and symbol tables
- Per-chapter theme presence tracking
- Thematic resistances and trilogy arcs

**Validation:**
- IF bible/themes.md FOUND: "✅ Thematic context found"
- IF bible/themes.md MISSING: "⚠️ Primary thematic context (bible/themes.md) not found — check tracking/themes.md as fallback"

**Usage:**
- Ensures thematic continuity
- Guides thematic development in chapter
- Prevents thematic contradictions
- Maintains symbolic consistency

---

### Input 6: Rhythm Guidelines

**Location:** `{rhythmGuidelinesPath}` (primary: tracking/rhythm.md)

**Additional sources (load if available):**
- Rhythm dashboard: `{bbb_output_folder}/current-book/tracking/rhythm-dashboard.md`
- Rhythm baseline: `{bbb_output_folder}/analysis/rhythm-baseline.md`

**Contains:**
- Per-chapter rhythm metrics (flow, tension, action/reflection ratio, fragment %)
- TEXTURE subtypes per chapter
- Pacing patterns and sentence distribution targets
- Phase-level rhythm health
- Tension/release patterns

**Validation:**
- IF tracking/rhythm.md FOUND: "✅ Rhythm guidelines found"
- IF tracking/rhythm.md MISSING: "⚠️ Primary rhythm file not found — check tracking/rhythm-dashboard.md or analysis/rhythm-baseline.md as fallback"

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
| Chapter Plan | ✅/❌ | book-1/chapter-plan-book-1.md (Ch {N} details extracted) |
| Style Profile | ✅/❌ | style-profile.yaml |
| Story Bible | ✅/❌ | bible/ ({N} files: locations, characters, themes, objects, chronology) |
| Previous Summaries | ✅/❌ | {count} meta.yaml files (Prologue–Ch {N-1}) |
| Thematic Context | ✅/⚠️/❌ | bible/themes.md — tracking/themes.md covers partial |
| Rhythm Guidelines | ✅/⚠️/❌ | tracking/rhythm.md |
| Character Dossier | ✅/❌ | characters/{name}-dossier.md |
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
