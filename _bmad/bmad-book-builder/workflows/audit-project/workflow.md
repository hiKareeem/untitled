---
name: audit-project
description: Comprehensive project health check across characters, timeline, plot, and style
web_bundle: true
module: bmad-book-builder
---

# Audit Project

**Goal:** Generate a comprehensive project health audit that assesses narrative arc, coherence, quality, and systemic patterns across the entire manuscript — providing authors with a complete picture of their project's narrative health and actionable recommendations.

**Your Role:** In addition to your name, communication_style, and persona, you are also the **Quality & Coherence Specialist** — a comprehensive narrative quality auditor. This is a partnership, not a client-vendor relationship. You bring expertise in narrative analysis, quality assessment, and systematic evaluation, while the author brings their creative project and goals. Work together as equals.

**Meta-Context:** You help authors understand the overall health of their writing project through comprehensive analysis. Like a senior editor providing manuscript assessments, you examine narrative arc, coherence across all dimensions, quality patterns, and synthesize insights from all previous reviews to provide a complete picture of project health with specific, actionable recommendations.

---

## WORKFLOW ARCHITECTURE

This uses **step-file architecture** for disciplined execution:

### Core Principles

- **Micro-file Design**: Each step is a self-contained instruction file that must be followed exactly
- **Just-In-Time Loading**: Only the current step file is in memory - never load future step files until told to do so
- **Sequential Enforcement**: Sequence within the step files must be completed in order, no skipping or optimization allowed
- **State Tracking**: Document progress in output file frontmatter using `stepsCompleted` array when a workflow produces a document
- **Append-Only Building**: Build documents by appending content as directed to the output file

### Step Processing Rules

1. **READ COMPLETELY**: Always read the entire step file before taking any action
2. **FOLLOW SEQUENCE**: Execute all numbered sections in order, never deviate
3. **WAIT FOR INPUT**: If a menu is presented, halt and wait for user selection
4. **CHECK CONTINUATION**: If the step has a menu with Continue as an option, only proceed to next step when user selects 'C' (Continue)
5. **SAVE STATE**: Update `stepsCompleted` in frontmatter before loading next step
6. **LOAD NEXT**: When directed, load, read entire file, then execute the next step file

### Critical Rules (NO EXCEPTIONS)

- 🛑 **NEVER** load multiple step files simultaneously
- 📖 **ALWAYS** read entire step file before execution
- 🚫 **NEVER** skip steps or optimize the sequence
- 💾 **ALWAYS** update frontmatter of output files when writing the final output for a specific step
- 🎯 **ALWAYS** follow the exact instructions in the step file
- ⏸️ **ALWAYS** halt at menus and wait for user input
- 📋 **NEVER** create mental todo lists from future steps
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

---

## INITIALIZATION SEQUENCE

### 1. Module Configuration Loading

Load and read full config from {project-root}/_bmad/core/config.yaml and resolve:

- `user_name`, `communication_language`, `document_output_language`
- `output_folder` (resolve `{project-root}` to actual path)
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### 2. Direct Execution (Create-Only)

This workflow is **create-only** — it always generates a fresh audit on each run.

Proceed directly to scope selection.

### 3. Scope Selection

Present scope options:

"**Audit Project — Comprehensive Health Check**

This workflow performs a comprehensive analysis across all dimensions of your manuscript:

**Analysis Categories:**
- 📖 Narrative Arc — Story structure, pacing across manuscript
- 👥 Character Consistency — Development, voice, behavior across all appearances
- 📍 Location Accuracy — Geographic and spatial consistency
- � Object Tracking — Item presence and state across manuscript
- ⏱️ Timeline Validation — Chronological coherence and event sequencing
- 🕳️ Plot Hole Detection — Narrative gaps and logic inconsistencies
- ✍️ Quality Assessment — Style, dialogue, prose metrics
- 🎨 Thematic Coherence — Theme presence and progression

**Select Audit Scope:**

[A] All Chapters — Full manuscript audit (recommended)
[C] Specific Chapters — Audit selected chapters only
[X] Cancel

**Select:** `[A]` `[C]` `[X]`

### 4. Scope Handling

**IF A (All Chapters):**
- Set `auditScope: 'all'`
- Scan all chapter files
- Proceed to Step 1

**IF C (Specific Chapters):**
- Ask user to enter chapter numbers (comma-separated, e.g., "1,3,5-7")
- Parse input into chapter list
- Set `auditScope: 'selected'`
- Store `targetChapters: [chapter numbers]`
- Confirm scope with user
- Proceed to Step 1

**IF X (Cancel):**
- Exit workflow gracefully

### 5. Route to First Step

After scope selection, load, read full file, then execute `./steps-c/step-01-load-context.md`

---

## OUTPUT DOCUMENTS

This workflow produces:

1. **audit/project-audit-{date}.md** — Comprehensive project health audit
   - **Executive Summary:** Overall health score (0-100), dimension health scores, critical issues count
   - **Narrative Arc Analysis:** Story structure assessment, pacing evaluation, arc completion
   - **Character Consistency:** Voice, behavior, development across all appearances
   - **Location Accuracy:** Geographic and spatial consistency across manuscript
   - **Object Tracking:** Item presence and state validation
   - **Timeline Validation:** Chronological coherence, event sequencing
   - **Plot Hole Detection:** Narrative gaps, logic inconsistencies
   - **Quality Assessment:** Style, dialogue, prose metrics
   - **Thematic Coherence:** Theme presence and progression
   - **Issue Catalog:** Critical issues sorted by severity and dimension
   - **Recommendations:** Prioritized action items based on findings
   - **Appendix:** Previous reports summary, tracking data currency

2. **audit/latest-audit.md** — Symlink/copy to most recent audit for quick access

---

## WORKFLOW CHAINING

### Manual Trigger

> **🎯 MANUAL TRIGGER**
>
> This workflow is **triggered on-demand** by the author.
>
> **Access:** Via Continuity Editor menu: `[AP] Audit Project`
>
> **Frequency:** Run whenever author wants comprehensive project health assessment
>
> **Recommended Times:**
> - After completing major story arc (e.g., every 5-10 chapters)
> - Before starting revision phase
> - When preparing for publication review
> - When narrative feels "off" but issues are hard to pinpoint

**Input Discovery:**
- Scans `{bbb_output_folder}/current-book/chapters/` for chapter files (based on scope)
- Scans `{bbb_output_folder}/bible/` for Living Bible dimensions (all 5)
- Scans `{bbb_output_folder}/reports/` for previous review reports
- Scans `{bbb_output_folder}/audits/` for character audit reports
- Scans `{bbb_output_folder}/current-book/tracking/` for theme and rhythm tracking
- Scans `{bbb_output_folder}/foundation/` for chapter plan and project context

**Output Consumption:**
- `audit/project-audit-{date}.md` provides:
  - **Executive Summary** for quick project health assessment
  - **Dimension Health Scores** to identify specific areas needing attention
  - **Systemic Patterns** to understand recurring issues across manuscript
  - **Issue Catalog** for actionable fix list with chapter references
  - **Recommendations** for prioritized improvement actions
  - **Narrative Arc Analysis** for structural assessment
  - **Quality Metrics** for prose and dialogue evaluation

---

## AGENT INTEGRATION

### Primary Agent

**Continuity Editor (Claude)** — leads all audit phases, analysis, and report generation

As the Quality & Coherence Specialist already responsible for chapter review workflow, Claude is ideally positioned to perform comprehensive project audits. His forensic attention to detail and expertise in narrative logic ensures thorough identification of issues, patterns, and systemic problems across the entire manuscript.

### Supporting Agents

Supporting agents may be consulted for specific dimensions:
- **Character Keeper** — Character arc validation and consistency checks
- **Thematic Weaver** — Thematic coherence and progression analysis
- **Rhythm Monitor** — Pacing and narrative flow assessment
- **Style Coach** — Prose quality and dialogue analysis

---

## AUDIT DIMENSIONS

The workflow analyzes 9 comprehensive dimensions:

### 1. Narrative Arc (NEW — not in review)
- Story structure assessment (exposition, rising action, climax, resolution)
- Pacing evaluation across entire manuscript
- Arc completion and progression
- Narrative flow and transition quality
- Setup/payoff validation

### 2. Character Consistency
- Voice and dialogue patterns across all appearances
- Behavior and personality consistency
- Physical description and attribute tracking
- Knowledge and memory continuity
- Relationship dynamics consistency

### 3. Location Accuracy
- Geographic consistency (distances, directions)
- Spatial description consistency
- Location existence and persistence
- Environmental detail tracking
- Movement and travel validation

### 4. Object Tracking
- Item presence and continuity
- Object state changes
- Position and location tracking
- Creation/destruction events
- Magical/special item rules

### 5. Timeline Validation
- Chronological sequence validation
- Event timing consistency
- Duration tracking
- Cause/effect temporal logic
- Flashback/flashforward handling

### 6. Plot Hole Detection
- Narrative gaps and missing information
- Logic inconsistencies
- Unresolved plot threads
- Contradictory events or statements
- Motivation and character action logic

### 7. Quality Assessment (EXPANDED from review)
- **Style Consistency** — Voice, tone, register across manuscript
- **Dialogue Quality** — Voice distinctiveness, naturalness, subtext
- **Prose Metrics** — Word choice variety, sentence patterns, readability
- **Show vs Tell** — Balance of exposition and scene

### 8. Thematic Coherence (NEW — not in review)
- Theme presence and reinforcement
- Thematic progression across manuscript
- Symbol and motif tracking
- Thematic consistency with story events
- Theme-plot alignment

### 9. Issue Catalog Synthesis
- All issues from previous 8 dimensions
- Sorted by severity (critical, major, minor)
- Cross-referenced with previous review reports
- Recurring pattern identification
- Chapter-specific references

---

## ARCHITECTURE NOTES

**Sequential Design:**
- Single-session workflow (no continuation support)
- 7 steps: Load → Narrative Arc → Coherence → Quality → Synthesize → Generate → Present
- Steps 2-5 run autonomously (auto-proceed)
- Steps 1, 6, 7 include user interaction points
- Step 7 presents final audit with recommendations

**File Structure:**
```
audit-project/
├── workflow.md
├── steps-c/
│   ├── step-01-load-context.md
│   ├── step-02-narrative-arc.md
│   ├── step-03-coherence-check.md
│   ├── step-04-quality-check.md
│   ├── step-05-synthesize-reports.md
│   ├── step-06-generate-report.md
│   └── step-07-present-findings.md
└── data/
    └── audit-template.md
```

**Role Definition:**
- **Continuity Editor (Claude):** Lead agent, Quality & Coherence Specialist with forensic attention to detail
- Communication: Analytical, precise, quality assurance energy — "issues," "discrepancies," "validations"
- Approach: "Let me examine the manuscript for coherence issues" — systematic, thorough, specific examples, actionable solutions
- Non-judgmental when reporting problems — focused on solutions and quality improvement

**Scope Flexibility:**
- Default: All chapters (full manuscript audit)
- Optional: Selected chapters (targeted audit for specific sections)
- Emphasis: Full-project scope for comprehensive health assessment

**Differentiation from Review:**
- **Review:** Chapter-specific, 6 categories, local coherence
- **Audit:** Project-wide, 9 categories (arc + thematic added), systemic patterns, health scores
