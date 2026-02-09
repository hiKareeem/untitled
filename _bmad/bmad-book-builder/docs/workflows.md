# Workflows Reference

BMad Book Builder includes 12 workflows organized into Core, Feature, and Utility categories.

---

## Core Workflows (Essential)

### Foundation

**Agent:** Story Architect

**Purpose:** Transform raw story idea into structured chapter breakdown

**When to Use:**
- Starting a new novel project
- Restructuring an existing story

**Key Steps:**
1. Gather Story — Extract raw story concept
2. Framework Selection — Choose narrative structure
3. Targeted Questions — Protagonist, conflict, themes, stakes
4. Generate Structure — Apply framework to create breakdown
5. Review & Refine — User adjusts structure
6. Finalize — Lock chapter structure for writing

**Outputs:**
- `chapter-plan.md` — Complete chapter breakdown
- `framework-summary.md` — Framework explanation

---

### ChapterWrite

**Agent:** Chapter Writer

**Purpose:** Write a complete chapter in author's authentic voice

**When to Use:**
- Writing any chapter after Foundation is complete

**Key Steps:**
1. Load Context — Style profile, bible, plan, previous chapters
2. Chapter Brief — Review what this chapter must accomplish
3. Draft — Generate chapter following plan, matching voice
4. Self-Review — Check against plan, bible, style profile
5. User Review — Author reads, provides feedback
6. Revise — Make user-requested changes
7. Finalize — Lock chapter, update tracking

**Inputs:**
- Chapter number and plan
- Style profile (from StyleCapture)
- Story bible (from Character Keeper)

**Outputs:**
- `chapter-{N}.md` — Complete chapter text
- `chapter-{N}-meta.yaml` — Chapter metadata

---

### Review

**Agent:** Continuity Editor

**Purpose:** Validate coherence and quality of chapter(s)

**When to Use:**
- After completing one or more chapters
- Before major revisions

**Key Steps:**
1. Load Content — Chapter(s) for review
2. Load Reference — Bible, previous chapters, plan
3. Validate Coherence — Characters, locations, objects, timeline
4. Identify Issues — Catalog by category and severity
5. Generate Report — Actionable report with fixes
6. Present Findings — Walk through issues
7. Track Resolutions — Allow user to mark fixed

**Outputs:**
- `review-report-{scope}.md` — Detailed coherence report

---

## Feature Workflows (Specialized)

### BuildCharacters

**Agent:** Character Keeper

**Purpose:** Create detailed character profiles

**When to Use:**
- Before Foundation (characters inform structure)
- Anytime you need to develop a new character

**Key Steps:**
1. Character Concept — Get initial idea
2. Physical Description — Appearance, traits
3. Background — History, traumas, formative experiences
4. Psychology — Fears, desires, contradictions
5. Voice — Speech patterns, vocabulary
6. Relationships — Connections to others
7. Arc — Start, end, transformation
8. Generate Dossier — Complete profile

**Outputs:**
- `characters/{name}-dossier.md` — Character profile

---

### StyleCapture

**Agent:** Style Coach

**Purpose:** Analyze and learn author's writing voice

**When to Use:**
- Before writing first chapter
- When voice consistency seems off

**Key Steps:**
1. Collect Samples — Get writing samples
2. Analyze Metrics — TTR, sentence length distribution
3. Identify Patterns — Words, phrases, imagery
4. Detect Anti-Patterns — Slop to avoid
5. Generate Profile — Style profile for Chapter Writer

**Outputs:**
- `style-profile.yaml` — Author's voice profile

**Anti-Slop Resources:**
- https://github.com/blader/humanizer

---

### BibleUpdate

**Agent:** Character Keeper

**Purpose:** Update narrative tracking after chapter completion

**When to Use:**
- After completing each chapter
- Before major story changes

**Key Steps:**
1. Load Chapter — New content
2. Extract Elements — Characters, locations, objects
3. Update Records — Add new, update existing
4. Validate Continuity — Check for inconsistencies
5. Save Bible — Update tracking files

**Outputs:**
- `bible/characters.yaml` — Updated characters
- `bible/locations.yaml` — Updated locations
- `bible/objects.yaml` — Updated objects
- `bible/timeline.yaml` — Updated chronology

---

### ThemeTracker

**Agent:** Thematic Weaver

**Purpose:** Track thematic and emotional progression

**When to Use:**
- After completing chapters
- Analyzing story depth

**Key Steps:**
1. Load Chapter — Content to analyze
2. Identify Themes — Detect thread presence
3. Map Emotions — Track emotional beats
4. Analyze Arc — Character development
5. Update Tracking — Update tracking files

**Outputs:**
- `tracking/themes.yaml` — Thematic progression
- `tracking/emotions.yaml` — Emotional arc data

---

### RhythmAnalysis

**Agent:** Rhythm Monitor

**Purpose:** Analyze pacing and tension

**When to Use:**
- Story feels slow or rushed
- Before final revision

**Key Steps:**
1. Load Chapter(s) — Content to analyze
2. Measure Tension — Plot tension curve
3. Analyze Balance — Action/reflection ratio
4. Check Patterns — Length, climax placement
5. Generate Report — Pacing report with recommendations

**Outputs:**
- `analysis/rhythm-{scope}.md` — Pacing analysis

---

### AuditProject

**Agent:** Continuity Editor

**Purpose:** Comprehensive project health check

**When to Use:**
- Mid-project health check
- Before final revision
- When reviewing complete manuscript

**Key Steps:**
1. Load All Chapters — Complete manuscript
2. Run Coherence Check — Full validation
3. Run Quality Check — Style, voice, prose
4. Compile Issues — All problems catalogued
5. Generate Audit Report — Complete health report

**Outputs:**
- `audit/project-audit.md` — Complete audit report

---

## Utility Workflows (Support)

### StatusReport

**Agent:** Any (shared command)

**Purpose:** Show current project state

**When to Use:**
- Anytime you want a progress overview

**Outputs:**
- Progress display (chapters, word count, tracking status)

---

### ExportBible

**Agent:** Character Keeper

**Purpose:** Generate formatted story bible

**When to Use:**
- Need reference document
- Before sharing story with collaborators

**Outputs:**
- `bible/complete-bible.md` — Formatted reference

---

### FrameworkSelect

**Agent:** Story Architect

**Purpose:** Choose narrative framework for structure

**When to Use:**
- Before Foundation workflow
- When considering structural changes

**Key Steps:**
1. Analyze Story — Type, genre, scope
2. Recommend Framework — Suggest appropriate options
3. Explain Options — What each offers
4. User Selection — Author chooses
5. Configure — Set up for Foundation

**Outputs:**
- `framework-selection.yaml` — Selected framework

---

## Workflow Integration

```
┌─────────────────────────────────────────────────────────────────────┐
│  NEW PROJECT                                                         │
├─────────────────────────────────────────────────────────────────────┤
│  1. FrameworkSelect → Choose structure                               │
│  2. BuildCharacters → Create character dossiers                     │
│  3. StyleCapture → Learn author's voice                              │
│  4. Foundation → Generate chapter plan                              │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────────┐ │
│  │  ITERATIVE CHAPTER LOOP (repeat for each chapter)              │ │
│  ├─────────────────────────────────────────────────────────────────┤ │
│  │                                                                 │ │
│  │  5. ChapterWrite → Generate chapter                             │ │
│  │  6. BibleUpdate → Update tracking                               │ │
│  │  7. ThemeTracker → Track themes/emotions                        │ │
│  │  8. RhythmAnalysis → Check pacing                              │ │
│  │  9. Review → Validate coherence                                │ │
│  │                                                                 │ │
│  └─────────────────────────────────────────────────────────────────┘ │
│                                                                      │
│  PERIODIC CHECKS:                                                    │
│  • StatusReport → Progress overview                                 │
│  • AuditProject → Complete health check                             │
│  • ExportBible → Generate reference document                        │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```
