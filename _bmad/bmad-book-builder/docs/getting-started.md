# Getting Started with BMad Book Builder

Welcome to BMad Book Builder (BBB)! This guide will help you get up and running with your novel writing journey.

---

## 🚦 Before You Begin - Installation & Setup

**BBB is a module that runs on the BMAD platform.** Before using BBB, you need to install BMAD first.

### Step 1: Install BMAD (Required)

BBB requires the BMAD CLI to be installed.

**Using npx (recommended):**
```bash
npx bmad-method@alpha install
```

This will launch the interactive BMAD installer. Follow the prompts to:
1. Select your project directory
2. Choose your AI IDE (Claude Code, Cursor, Windsurf, etc.)
3. Configure your preferences (name, language, output folder)

> **❓ What is BMAD?** BMAD (Build Modular AI Devices) is a platform that hosts AI agents and workflows. Think of it like an app store for AI writing assistants. BBB is one of the "apps" you can install.

### Step 2: Download BBB Module

BBB is distributed as a ZIP file from Forgejo. Download it in one of two ways:

**Option A - Download from Release (Recommended):**

1. Go to: https://git.ut0pia.org/jbl/bmad-book-builder/releases
2. Find the latest release (v1.0.1 or later)
3. Click the **"Download ZIP"** button at the bottom of the release notes

**Option B - Download from Repository:**

1. Go to: https://git.ut0pia.org/jbl/bmad-book-builder
2. Click the **"Download ZIP"** button in the repository header

> **💡 Tip:** The release version is recommended as it's tested and stable. Repository ZIP contains the latest development code.

### Step 3: Extract and Install BBB

Once you've downloaded the ZIP file:

1. **Extract the ZIP** to your preferred location:
   - macOS: Double-click the ZIP file
   - Linux: `unzip bmad-book-builder-main.zip`
   - Windows: Right-click → "Extract All"

2. **Note the extracted path** - you'll need it in the next step:
   - Example: `/Users/yourname/Downloads/bmad-book-builder-main`

3. **Re-run the BMAD installer** to add BBB as a custom module:

```bash
npx bmad-method@alpha install
```

4. **When prompted**, select:
   - **"Would you like to install a local custom module?"** → `Yes`
   - **"Enter the path to your custom content folder:"** → Paste the extracted path

Example:
```
? Enter the path to your custom content folder: /Users/yourname/Downloads/bmad-book-builder-main
✓ Confirmed local custom module: BMad Book Builder (BBB)
```

5. **Complete the installation** - BMAD will:
   - Register all BBB agents (8 specialized writing agents)
   - Set up all BBB workflows (17 production-ready workflows)
   - Configure your output folder

### Step 4: Verify Installation

Once installation is complete, you can access BBB agents through your AI IDE (Claude Code, Cursor, etc.):

**In Claude Code:**
- Type `/bmad-help` to see available BBB agents
- Or directly invoke an agent by name

**Available BBB Agents:**
- `story-architect` — Structure and planning
- `character-keeper` — Character development and continuity
- `style-coach` — Voice and style analysis
- `chapter-writer` — Chapter composition
- `continuity-editor` — Quality and coherence
- `thematic-weaver` — Theme tracking
- `rhythm-monitor` — Pacing analysis
- `documentaliste` — Research and fact-checking

> **💡 How to use agents:** In Claude Code, simply type the agent name or workflow trigger in your conversation. The agent will load and present its menu of options.

---

## What This Module Does

BBB provides complete AI-assisted novel development — from raw idea to polished manuscript. Unlike generic AI writing tools that produce robotic "slop," BBB:

- **Learns your authentic voice** — Style capture analyzes your writing samples
- **Uses proven frameworks** — Save the Cat, Hero's Journey, Snowflake Method
- **Tracks everything** — Characters, locations, themes, pacing, continuity
- **Keeps you in control** — AI-assisted, not AI-generated

---

## Installation

If you haven't installed the module yet, follow the steps in the "Before You Begin" section above:

1. Install BMAD CLI: `npx bmad-method@alpha install`
2. Download BBB ZIP from: https://git.ut0pia.org/jbl/bmad-book-builder/releases
3. Extract the ZIP file
4. Re-run BMAD installer and add the extracted folder as a custom module

---

## First Steps

### 1. Start with Your Story Idea

**In Claude Code, type:**
```
story-architect
```

Or use the workflow trigger:
```
/Foundation
```

The Story Architect will welcome you and present a menu:
- **[FO]** Framework Selection — Choose a narrative structure
- **[FD]** Foundation — Create your chapter plan
- **[WS]** Workflow Status — Check your progress

**Start the Foundation workflow:**
Type `FD` or `Foundation` and press Enter.

The Foundation workflow will begin. Describe your story concept in your own words. The Story Architect will ask targeted questions to understand:
- Your protagonist and their goals
- The central conflict
- What you want readers to feel
- Themes you want to explore

### 2. Choose Your Framework

BBB supports proven narrative structures:

| Framework | Best For | Description |
|-----------|----------|-------------|
| **Save the Cat** | Plot-driven stories | 15-beat structure used in Hollywood |
| **Hero's Journey** | Character transformation | 12-stage mythic structure |
| **Snowflake Method** | Complex stories | Progressive complexity building |

---

## 📋 Understanding Workflow Dependencies

**Important:** Before you can write your first chapter, BBB needs to gather some essential information about your story. Here's the recommended workflow order:

### Required Workflows (Before Writing)

```
1. Foundation ──────────────→ Creates your chapter plan
     ↓
2. Build Characters ─────────→ Creates detailed character profiles
     ↓
3. Style Capture ─────────────→ Learns your writing voice
     ↓
4. Living Bible (optional) ──→ Creates your story reference (characters, locations, etc.)
     ↓
5. Theme Tracker (optional) ─→ Tracks your thematic threads
     ↓
6. Rhythm Analysis (optional) → Analyzes pacing patterns
     ↓
✅ Ready to write chapters!
```

### What Each Workflow Creates

| Workflow | Creates | Used By |
|----------|---------|---------|
| **Foundation** | `chapter-plan-{project}.md` | Chapter-Write (REQUIRED) |
| **Build Characters** | `character-dossiers/*.md` | Chapter-Write, Character-Audit |
| **Style Capture** | `style-profile.yaml` | Chapter-Write, Review |
| **Living Bible** | 5 tracking files (bible/) | Chapter-Write, Review |
| **Theme Tracker** | `thematic-analysis.md` | Chapter-Write (optional) |
| **Rhythm Analysis** | `rhythm-profile.md` | Chapter-Write (optional) |

### Quick Path vs. Complete Path

**Quick Path (Minimal) - ~2 hours:**
```
Foundation → Build Characters → Style Capture → Chapter Write
```
This gives you everything needed to write your first chapter.

**Complete Path (Recommended) - ~4 hours:**
```
All 6 workflows above → Chapter Write
```
This provides maximum consistency and quality guidance.

> **💡 Tip:** The Foundation workflow will automatically offer to launch Build Characters and Style Capture when you complete it. You can follow these prompts or launch workflows manually as shown above.

---

| Framework | Best For | Description |
|-----------|----------|-------------|
| **Save the Cat** | Plot-driven stories | 15-beat structure used in Hollywood |
| **Hero's Journey** | Character transformation | 12-stage mythic structure |
| **Snowflake Method** | Complex stories | Progressive complexity building |

### 3. Capture Your Voice

Before writing, teach BBB your unique voice:

**Type in Claude Code:**
```
style-coach
```

**Start the Style Capture workflow:**
```
/Style-Capture
```

Provide writing samples (blog posts, short stories, previous chapters). The Style Coach will analyze:
- Your sentence patterns and length distribution
- Your vocabulary preferences
- Your imagery and metaphor style
- Your unique "fingerprint" as a writer

### 4. Build Your Characters

**Type in Claude Code:**
```
character-keeper
```

**Start the Build Characters workflow:**
```
/Build-Characters
```

For each major character, the Character Keeper will help you create:
- Physical description and distinctive traits
- Background and formative experiences
- Psychology (fears, desires, contradictions)
- Voice and speech patterns
- Relationships and arcs

### 5. Write Your First Chapter

**Type in Claude Code:**
```
chapter-writer
```

**Start the Chapter Write workflow:**
```
/Chapter-Write
```

The Chapter Writer will:
- Reference your chapter plan from Foundation
- Match your authentic voice from StyleCapture
- Maintain consistency with your character dossiers
- Produce a complete chapter (3000-6000 words)

### 6. Review and Refine

**Type in Claude Code:**
```
continuity-editor
```

**Start the Review workflow:**
```
/Review
```

The Continuity Editor validates:
- Character consistency (personality, voice, motivation)
- Location accuracy (descriptions match, distances plausible)
- Timeline validation (events in correct order)
- Plot holes or contradictions

---

## Common Use Cases

**Use Case 1: "I have an idea but don't know where to start"**
→ Type `story-architect` then `Foundation`. Story Architect will structure your idea into a chapter-by-chapter plan.

**Use Case 2: "I'm stuck on Chapter 5"**
→ Type `chapter-writer` then `Chapter-Write`. The Writer will continue from where you are, maintaining all continuity.

**Use Case 3: "I think I have a continuity problem"**
→ Type `continuity-editor` then `Review`. Continuity Editor will identify specific issues and suggest fixes.

**Use Case 4: "I want to check my pacing"**
→ Type `rhythm-monitor` then `Rhythm-Analysis`. Rhythm Monitor will show tension curves and identify flat spots.

**Use Case 5: "I need to research historical facts"**
→ Type `documentaliste` then `Research`.

---

## 📚 Complete Workflow Reference

BBB includes 17 production-ready workflows. Here's how to invoke each one in Claude Code:

### Core Workflows (With Dedicated Agents)

| Workflow | Agent Name | Menu Trigger | Description |
|----------|------------|--------------|-------------|
| **Foundation** | `story-architect` | `/Foundation` or `FD` | Create chapter plan from story idea |
| **Chapter-Write** | `chapter-writer` | `/Chapter-Write` or `CW` | Write complete chapters in your voice |
| **Build Characters** | `character-keeper` | `/Build-Characters` or `BC` | Create detailed character profiles |
| **Style Capture** | `style-coach` | `/Style-Capture` or `SC` | Analyze and learn your writing voice |
| **Review** | `continuity-editor` | `/Review` or `RV` | Validate coherence and consistency |

### Standalone Workflows

These workflows are invoked through their parent agents:

| Workflow | Parent Agent | Trigger | Description |
|----------|--------------|---------|-------------|
| **Living Bible** | `character-keeper` | `/Living-Bible` | Create/update 5-dimensional story tracking |
| **Bible Update** | `character-keeper` | `/Bible-Update` | Update story bible after chapters |
| **Theme Tracker** | `thematic-weaver` | `/Theme-Tracker` | Track thematic progression |
| **Rhythm Analysis** | `rhythm-monitor` | `/Rhythm-Analysis` | Analyze pacing and tension |
| **Research** | `documentaliste` | `/Research` | Web research and fact verification |
| **Reality Check** | `documentaliste` | `/Reality-Check` | Ground fiction in reality |
| **Audit Project** | `continuity-editor` | `/Audit-Project` | Full project health check |
| **Status Report** | `story-architect` | `/Status-Report` | Generate project status overview |
| **Export Bible** | `character-keeper` | `/Export-Bible` | Export complete story bible |
| **Framework Select** | `story-architect` | `/Framework-Select` or `FO` | Choose narrative framework |
| **Project Onboarding** | `story-architect` | `/Project-Onboarding` | Migrate existing projects to BBB |

### Quick Reference Card

```
STORY DEVELOPMENT:
├─ Foundation           → story-architect (FD)
├─ Build Characters     → character-keeper (BC)
├─ Style Capture        → style-coach (SC)
└─ Framework Select     → story-architect (FO)

WRITING & REVIEW:
├─ Chapter Write        → chapter-writer (CW)
├─ Review               → continuity-editor (RV)
└─ Character Audit      → character-keeper (CA)

TRACKING & ANALYSIS:
├─ Living Bible         → character-keeper
├─ Bible Update         → character-keeper
├─ Theme Tracker        → thematic-weaver
└─ Rhythm Analysis      → rhythm-monitor

RESEARCH & VERIFICATION:
├─ Research             → documentaliste
├─ Reality Check        → documentaliste
└─ Documentaliste       → documentaliste (agent)

PROJECT MANAGEMENT:
├─ Status Report        → story-architect
├─ Audit Project        → continuity-editor
├─ Export Bible         → character-keeper
└─ Project Onboarding   → story-architect
```

> **💡 Tip:** Type the agent name (e.g., `story-architect`) to load the agent, then use the menu trigger (e.g., `FD`) to run a specific workflow. You can also use fuzzy matching—type `Foundation` or even just `Fou` instead of the trigger.

---

- Check out the [Agents Reference](agents.md) to meet your "Second Chance Press" team
- Browse the [Workflows Reference](workflows.md) to see what you can do
- See [Examples](examples.md) for real-world usage

---

## Need Help?

If you run into issues:
1. Check the troubleshooting section in examples.md
2. Review your module configuration
3. Consult the broader BMAD documentation

---

**Remember:** Everyone deserves a second chance at their story. BBB is here to help you finally write that book.
