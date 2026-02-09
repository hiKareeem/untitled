# BMad Book Builder (BBB)

AI-Assisted Novel Development System

Complete novel writing assistant with proven frameworks, authentic voice preservation, and systematic story tracking.

**Status:** 90% Feature Parity with AgentAdam Methodology

---

## Overview

BMad Book Builder (BBB) is a **production-ready novel development system** that treats creative writing with the rigor of software engineering. Inspired by real-world novel writing methodologies and AgentAdam's systematic approach, BBB provides a professional team of 8 AI agents — Story Architect, Character Keeper, Style Coach, Chapter Writer, Continuity Editor, Thematic Weaver, Rhythm Monitor, and Documentaliste — who collaborate to guide authors from raw premise to finished manuscript while maintaining authentic voice and narrative coherence.

The module's philosophy: **"Everyone deserves a second chance at their story."** BBB removes the barriers that keep people from becoming authors — time, structure, consistency, and self-doubt — by providing systematic, professional-grade assistance at every stage of novel development.

---

## Key Features

### ✨ What's New (v0.9)

**🎯 Quality Assurance System:**
- **Quantitative Style Metrics** — TTR (>0.175), sentence length (20-24 words), complexity ratio (80/20)
- **Automated Audit Chain** — After each chapter: Review → Bible Update → Character Audits → Themes → Rhythm
- **Character-Specific Audits** — Per-chapter, per-character contradiction checking (5+ per character)
- **Pre-Writing Checklist** — 22 verification points before drafting

**📊 Enhanced Framework:**
- **5-Phase Psychological Framework** — Character psychology-driven structure (NEW)
- **Chapter Synopsis System** — Embedded continuity notes in each chapter file
- **Tri-Modal Workflows** — Create/Edit/Validate modes for all major workflows

**🏗️ Architecture:**
- All workflows now support **Create/Edit/Validate** modes
- **Living Bible** with 5 specialized guardian sub-agents
- **Advanced Elicitation** and **Party Mode** for deep exploration

---

## Installation

```bash
bmad install bmad-book-builder
```

---

## Quick Start

**For Thomas (busy professional with a story idea):**
1. Load `/bmad-bmb` to start Morgan, the Module Creation Master
2. Select `[PB]` Create Product Brief OR `[CM]` Create Complete Module
3. Follow **Foundation** workflow (Create mode) to structure your story
4. Run **BuildCharacters** to create detailed psychological profiles (5+ contradictions)
5. Run **StyleCapture** to teach the system your voice with quantitative metrics
6. Write chapters with **ChapterWrite** — includes automated audit chain
7. Complete your novel in weeks, not years

**For detailed documentation, see [docs/](docs/).**

---

## Components

### Agents (8 Specialized Personas)

| Agent | Role | Specialization |
|-------|------|---------------|
| **Story Architect** 🏗️ | Lead Narrative Designer | Structure & frameworks (6 frameworks available) |
| **Character Keeper** 📚 | Bible Guardian | Character psychology, continuity tracking |
| **Style Coach** ✨ | Voice & Style Specialist | Quantitative metrics (TTR, sentence complexity), anti-slop (24 patterns) |
| **Chapter Writer** ✍️ | Content Creator | Authentic voice writing, multi-agent review |
| **Continuity Editor** 🔍 | Quality Specialist | Coherence validation, consistency checks |
| **Thematic Weaver** 🎭 | Theme Tracker | Thematic & emotional progression analysis |
| **Rhythm Monitor** ⏱️ | Pacing Analyst | Tension curves, pacing optimization |
| **Documentaliste** 📖 | Research Specialist | Fact-checking, reality validation |

### Workflows (16 Complete, 8 Tri-Modal)

**Core Tri-Modal Workflows (Create + Edit + Validate):**

| Workflow | Create | Edit | Validate | Description |
|----------|--------|------|----------|-------------|
| **Foundation** | ✅ 8 steps | ✅ 4 steps | ✅ 2 steps | Transform idea → structured chapter plan |
| **Chapter-Write** | ✅ 8 steps | ✅ 3 steps | ✅ 1 step | Write chapters with automated audit chain |
| **Build-Characters** | ✅ 5 steps | ✅ 3 steps | ✅ 1 step | Create character profiles (5+ contradictions) |
| **Living-Bible** | ✅ 3 steps | ✅ 7 steps | ✅ 2 steps | 5-dimensional story tracking |
| **Character-Audit** | ✅ 6 steps | ✅ 1 step | ✅ 1 step | Per-chapter, per-character psychological validation |
| **Research** | ✅ 6 steps | ✅ 4 steps | ✅ 4 steps | Web research & fact verification |

**Additional Create-Mode Workflows:**

| Workflow | Steps | Description |
|----------|-------|-------------|
| **Review** | ✅ 5 steps | Validate coherence, consistency, quality |
| **Style-Capture** | ✅ 6 steps | Analyze author's voice (TTR, metrics) |
| **Bible-Update** | ✅ 4 steps | Update Living Bible dimensions |
| **Theme-Tracker** | ✅ 6 steps (Edit) | Track thematic progression |
| **Rhythm-Analysis** | ✅ 4 steps | Analyze pacing and tension |
| **Audit-Project** | ✅ 7 steps | Full project health check |
| **Status-Report** | ✅ 4 steps | Generate project status |
| **Export-Bible** | ✅ 4 steps | Export complete story bible |
| **Reality-Check** | ✅ 6 steps | Ground fiction in reality |
| **Framework-Select** | ✅ 5 steps | Choose narrative framework |
| **Project-Onboarding** | ✅ 8 steps | Initial project setup |

**Total: 17 production-ready workflows**

---

## Narrative Frameworks (6 Available)

1. **Save the Cat** (Blake Snyder) — Commercial structure, 15 beats
2. **Hero's Journey** (Joseph Campbell) — Mythic 12-stage structure
3. **Snowflake Method** (Randy Ingermanson) — Progressive complexity
4. **Méthode de Marie ** — Pragmatic French approach
5. **Custom Structure** — Your own framework
6. **🆕 5-Phase Psychological** — Character psychology-driven structure (AgentAdam-based)

---

## Quality Assurance System

### Quantitative Style Metrics
- **TTR (Type-Token Ratio)** — Target: > 0.175 for vocabulary diversity
- **Sentence Length** — Target: 20-24 words average
- **Complexity Ratio** — Target: 80% complex/compound, 20% simple
- **Show vs Tell** — Estimated showing percentage
- **Paragraph Variation** — Rhythm analysis

### Automated Audit Chain
After each chapter completion:
1. **Review** — Validate coherence (blocks if critical issues)
2. **Living Bible Update** — Update 5 dimensions (chronologie, lieux, objets, personnes, themes)
3. **Character Audits** — Audit each character present in chapter
4. **Thematic Tracking** — Update theme progression
5. **Rhythm Analysis** — Analyze pacing (optional)

### Character-Specific Audits
- **5+ Contradictions** per character checked systematically
- **4 Psychological Dimensions**: emotional state, behavior patterns, voice consistency, decision logic
- **Arc Progression**: before/after states, transformation moments, next steps
- **✅/❌ Format**: Clear designation with specific chapter evidence

---

## Module Structure

```
bmad-book-builder/
├── module.yaml
├── README.md
├── TODO.md
├── docs/
│   ├── getting-started.md
│   ├── agents.md
│   ├── workflows.md
│   └── examples.md
├── agents/
│   ├── story-architect.yaml
│   ├── character-keeper.yaml + sidecar/
│   ├── style-coach.yaml + sidecar/
│   ├── chapter-writer.yaml
│   ├── continuity-editor.yaml
│   ├── thematic-weaver.yaml + sidecar/
│   ├── rhythm-monitor.yaml
│   └── documentaliste.yaml + sidecar/
└── workflows/
    ├── foundation/          ✅ TRI-MODAL (8+4+2 steps)
    ├── chapter-write/       ✅ TRI-MODAL (8+3+1 steps)
    ├── living-bible/        ✅ TRI-MODAL (3+7+2 steps)
    ├── build-characters/    ✅ TRI-MODAL (5+3+1 steps)
    ├── character-audit/     ✅ TRI-MODAL (6+1+1 steps)
    ├── research/            ✅ TRI-MODAL (6+4+4 steps)
    ├── review/              ✅ CREATE (5 steps)
    ├── style-capture/       ✅ CREATE (6 steps)
    ├── bible-update/        ✅ CREATE (4 steps)
    ├── theme-tracker/       ✅ EDIT (6 steps)
    ├── rhythm-analysis/     ✅ CREATE (4 steps)
    ├── audit-project/       ✅ CREATE (7 steps)
    ├── status-report/       ✅ CREATE (4 steps)
    ├── export-bible/        ✅ CREATE (4 steps)
    ├── framework-select/    ✅ CREATE (5 steps)
    ├── project-onboarding/  ✅ CREATE (8 steps)
    └── reality-check/       ✅ CREATE (6 steps)
```

---

## Documentation

For detailed user guides and documentation, see the **[docs/](docs/)** folder:
- [Getting Started](docs/getting-started.md)
- [Agents Reference](docs/agents.md)
- [Workflows Reference](docs/workflows.md)
- [Examples](docs/examples.md)

---

## Development Status

This module is **production-ready** with comprehensive workflow implementation.

**Completed:**
- [x] Agents: 8/8 agents implemented
- [x] Workflows: 17/17 workflows production-ready
  - [x] 6 tri-modal workflows (Foundation, Chapter-Write, Build-Characters, Living-Bible, Character-Audit, Research)
  - [x] 11 create-mode workflows (Review, Style-Capture, Bible-Update, Theme-Tracker, Rhythm-Analysis, Audit-Project, Status-Report, Export-Bible, Reality-Check, Framework-Select, Project-Onboarding)
- [x] Quality System: Quantitative metrics (TTR, sentence length, complexity ratio), automated audit chain, character audits
- [x] Frameworks: 6 frameworks available including 5-phase psychological
- [x] Documentation: Complete

**Fully Functional Features:**
- ✅ Complete novel creation pipeline (Foundation → Build Characters → Style Capture → Chapter Write)
- ✅ Automated audit chain after each chapter (Review → Bible Update → Character Audits → Theme Tracking → Rhythm Analysis)
- ✅ Quantitative style metrics with TTR calculation
- ✅ Living Bible with 5-dimensional tracking
- ✅ Multi-modal editing (Create/Edit/Validate) for core workflows
- ✅ Research and fact verification workflows

See TODO.md for detailed status.

---

## AgentAdam Parity

BBB has achieved **90% feature parity** with AgentAdam's mature novel writing methodology while maintaining superior architectural advantages:

**BBB Exclusive Advantages:**
- **Multi-Agent Architecture** (8 personas vs single agent)
- **Tri-Modal Workflows** (Create/Edit/Validate vs single-mode)
- **Sub-Agent Personas** (5 specialized Bible guardians)
- **Party Mode Integration** (multi-perspective analysis)
- **Advanced Elicitation** (systematic deep-dive)

**Parity Achieved:**
- ✅ Psychological depth (5+ contradictions per character)
- ✅ Quantitative style metrics (TTR, sentence length, complexity)
- ✅ Character-specific auditing (✅/❌ format with evidence)
- ✅ Living story bible (5-dimensional tracking)
- ✅ 5-phase psychological structure
- ✅ Automated audit chain
- ✅ Chapter synopsis system

**Reference:** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md`

---

## "Second Chance Press"

BBB agents embody a boutique publishing house philosophy where everyone deserves a second chance at their story. Each agent is a senior editor with a specialty, working together to help writers succeed. The publishing house theme provides narrative unity while allowing each agent distinct expertise.

**Agent Catchphrases:**
- Story Architect: *"Every great story is built before it's written."*
- Character Keeper: *"Characters are the heart, continuity is the heartbeat."*
- Style Coach: *"Your voice, amplified — not replaced."*
- Chapter Writer: *"Let's write something authentic."*
- Continuity Editor: *"The details are where the truth lives."*
- Thematic Weaver: *"Themes are the invisible threads that bind."*
- Rhythm Monitor: *"Pacing is the pulse of narrative."*
- Documentaliste: *"Readers forgive invented plots, but never invented facts."*

---

## Version History

- **v0.9** (2026-01-24) — 90% AgentAdam parity, automated audit chain, character audits, quantitative metrics
- **v0.7** (Initial) — Core workflows and agents

---

## Author

Created via BMAD Module workflow by Jean-Baptiste

---

## License

Part of the BMAD framework.
