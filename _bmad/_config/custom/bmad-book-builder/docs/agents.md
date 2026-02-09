# Agents Reference

BMad Book Builder includes 8 specialized agents forming a complete professional writing team at "Second Chance Press."

---

## Story Architect

**Icon:** 🏗️

**Role:** Lead narrative designer specializing in story structure, narrative frameworks, and chapter breakdowns.

**Expertise:**
- Proven narrative frameworks (Save the Cat, Hero's Journey, Snowflake Method)
- Chapter structure and turning points
- Emotional arcs and midpoint analysis
- Targeted questioning to extract story essence

**When to Use:**
- Starting a new novel — use Foundation workflow
- Choosing a narrative framework — use FrameworkSelect
- Restructuring your story

**Key Capabilities:**
- Transforms raw ideas into structured chapter plans
- Applies Hollywood-tested frameworks that actually work
- Identifies weak spots in story structure
- Creates chapter-by-chapter breakdowns with purpose and scenes

**Menu Triggers:**
- `FO` — Framework Select
- `FD` — Foundation
- `WS` — Workflow Status (shared)

**Catchphrase:** *"Every great story is built before it's written."*

---

## Character Keeper

**Icon:** 📚

**Role:** Bible guardian responsible for character profiling, continuity tracking, and maintaining complete story reference documentation.

**Expertise:**
- Character dossiers (psychology, backstory, voice, relationships, arc)
- Story bible maintenance (characters, locations, objects, chronology)
- Continuity validation across long works
- Relationship and timeline tracking

**When to Use:**
- Creating new characters — use BuildCharacters workflow
- After writing chapters — use BibleUpdate workflow
- Needing a reference document — use ExportBible workflow

**Key Capabilities:**
- Creates detailed character profiles from rough concepts
- Tracks every character, location, and object across your manuscript
- Prevents continuity errors before they happen
- Generates complete story bible for reference

**Menu Triggers:**
- `BC` — Build Characters
- `BU` — Bible Update
- `EB` — Export Bible
- `WS` — Workflow Status (shared)

**Memory:** Maintains story bible state across sessions (hasSidecar: true)

**Catchphrase:** *"Characters are the heart, continuity is the heartbeat."*

---

## Style Coach

**Icon:** ✍️

**Role:** Voice & style specialist responsible for capturing the author's unique writing voice and ensuring AI-generated text sounds authentic.

**Expertise:**
- Style analysis (TTR, sentence patterns, vocabulary, imagery)
- Anti-slop detection and enforcement
- Voice matching for authentic text generation
- Writing guidance and improvement

**When to Use:**
- Before writing — use StyleCapture to teach BBB your voice
- Any time you want to verify voice consistency

**Key Capabilities:**
- Analyzes your writing samples to identify your unique fingerprint
- Detects and rejects generic AI "slop"
- Guides Chapter Writer to match your authentic voice
- Helps you sound more like yourself

**Menu Triggers:**
- `SC` — Style Capture
- `WS` — Workflow Status (shared)

**Memory:** Learns and stores your style profile across sessions (hasSidecar: true)

**Catchphrase:** *"Your voice, amplified — not replaced."*

**Anti-Slop Reference:** https://github.com/blader/humanizer

---

## Chapter Writer

**Icon:** 📝

**Role:** Content creator responsible for drafting chapters in the author's authentic voice while maintaining continuity.

**Expertise:**
- Style profile matching (replicates author's voice)
- Bible integration (accurately references characters, locations, objects)
- Continuity maintenance (builds on previous chapters)
- Plan adherence (follows chapter structure from Foundation)

**When to Use:**
- Writing any chapter — use ChapterWrite workflow

**Key Capabilities:**
- Generates complete chapters (3000-6000 words) in your voice
- References all tracking data for consistency
- Accepts revision feedback and iterates
- Delivers publication-ready drafts

**Menu Triggers:**
- `CW` — Chapter Write
- `WS` — Workflow Status (shared)

**Catchphrase:** *"Let's write something authentic."*

---

## Continuity Editor

**Icon:** 🔍

**Role:** Quality & coherence specialist responsible for validating narrative consistency and identifying issues.

**Expertise:**
- Character consistency (personality, voice, motivation)
- Location and object tracking
- Timeline validation
- Plot hole detection

**When to Use:**
- After completing chapters — use Review workflow
- Mid-project health check — use AuditProject workflow
- Any time you suspect continuity problems

**Key Capabilities:**
- Identifies inconsistencies with specific examples
- Categorizes issues by severity (Critical, Major, Minor)
- Provides actionable fixes for each problem
- Runs comprehensive project audits

**Menu Triggers:**
- `RV` — Review
- `AP` — Audit Project
- `WS` — Workflow Status (shared)

**Catchphrase:** *"The details are where the truth lives."*

---

## Thematic Weaver

**Icon:** 🎭

**Role:** Theme & emotion tracker responsible for monitoring thematic threads, emotional arcs, and character development.

**Expertise:**
- Thematic thread tracking (identify, monitor, converge)
- Emotional arc mapping (character feelings across story)
- Character development patterns
- Thematic convergence analysis

**When to Use:**
- After completing chapters — use ThemeTracker workflow
- Analyzing your story's deeper meaning
- Ensuring thematic payoff

**Key Capabilities:**
- Tracks multiple thematic threads across your novel
- Maps character emotional journeys
- Identifies where themes converge or diverge
- Ensures emotional arcs parallel plot arcs

**Menu Triggers:**
- `TT` — Theme Tracker
- `WS` — Workflow Status (shared)

**Memory:** Maintains thematic tracking state across sessions (hasSidecar: true)

**Catchphrase:** *"Themes are the invisible threads that bind."*

---

## Rhythm Monitor

**Icon:** 🎵

**Role:** Pacing analyst responsible for measuring tension curves, action/reflection balance, and chapter patterns.

**Expertise:**
- Tension curve measurement (plot tension per scene/chapter)
- Action/reflection ratio analysis
- Chapter length pattern assessment
- Climax placement validation

**When to Use:**
- After completing chapters — use RhythmAnalysis workflow
- Story feels slow or rushed
- Checking pacing before final revision

**Key Capabilities:**
- Visualizes tension curves to identify flat spots
- Analyzes balance of internal vs. external conflict
- Validates climax placement for maximum impact
- Provides specific pacing recommendations

**Menu Triggers:**
- `RA` — Rhythm Analysis
- `WS` — Workflow Status (shared)

**Catchphrase:** *"Pacing is the pulse of narrative."*

---

## Documentaliste

**Icon:** 📚

**Role:** Research specialist who grounds fiction in reality through web research, fact verification, and organized research dossiers.

**Expertise:**
- Web research and source triangulation
- Research dossier creation and organization
- Fact verification against real-world details
- Anachronism and technical error detection

**When to Use:**
- Before writing — research topics to ensure accuracy
- After writing — verify chapter facts with VerifyChapter
- Building story world — create research dossiers on locations, professions, technology
- Checking consistency — verify bible against real-world facts

**Key Capabilities:**
- Creates organized research dossiers on any topic
- Performs quick factual searches without full dossiers
- Reviews chapters for factual accuracy and anachronisms
- Identifies "golden details" that make fiction feel authentic
- Cross-references story bible against reality

**Menu Triggers:**
- `RD` — Research Dossier (full research workflow)
- `QS` — Quick Search (fast factual lookup)
- `VC` — Verify Chapter (factual accuracy check)
- `VB` — Verify Bible (consistency with reality)
- `RC` — Reality Check (full verification workflow)
- `LD` — List Dossiers (show available research)
- `LR` — Load Research (load dossier into context)

**Memory:** Maintains research dossiers across sessions (hasSidecar: true)

**Catchphrase:** *"Readers forgive invented plots, but never invented facts."*

---

## Collaboration Model

BBB agents work sequentially and collaboratively:

1. **Foundation Phase** — Story Architect, Character Keeper, Style Coach establish foundations
2. **Research Phase** — Documentaliste grounds fiction in reality with verified facts
3. **Production Phase** — Chapter Writer creates content, Continuity Editor validates
4. **Analysis Phase** — Thematic Weaver and Rhythm Monitor provide ongoing feedback

All agents share the "Second Chance Press" identity while maintaining distinct specialties. They reference each other's work naturally and collaborate to serve your story.
