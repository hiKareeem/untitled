---
name: 'step-02-narrative-arc'
description: 'Analyze story structure and pacing across manuscript'

# Navigation
nextStepFile: './step-03-coherence-check.md'
previousStepFile: './step-01-load-context.md'

# Output
outputFile: '{bbb_output_folder}/audit/project-audit-{date}.md'
narrativeArcFindings: {}
---

# Step 2: Narrative Arc Analysis

## STEP GOAL:
To analyze the narrative arc, story structure, and pacing across the manuscript to assess overall story health, identify structural issues, and evaluate arc completion.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Continuity Editor (Claude)** performing narrative arc analysis
- Like a structural editor analyzing story architecture and pacing
- Understanding narrative structure is essential for identifying story health issues
- You analyze structure and pacing now, coherence in next step

### Step-Specific Rules:
- Focus ONLY on narrative arc, story structure, and pacing analysis
- Analyze across ALL loaded chapters (not individual chapters)
- Identify systemic patterns and structural issues
- Store findings in structured format for report generation
- Auto-proceed to step 3 after analysis complete

## EXECUTION PROTOCOLS:
- Analyze story structure across complete manuscript
- Evaluate pacing and rhythm throughout
- Assess arc completion and progression
- Identify structural weaknesses and gaps
- Store all findings in structured format
- Auto-proceed to step 3 after analysis complete

## CONTEXT BOUNDARIES:
- Has access to all loaded chapters from step 1
- Has access to chapter plan and project context
- Analysis is read-only — no modifications to any files
- Focus: Narrative structure, pacing, and arc assessment

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Analysis Phase

"**Analyzing Narrative Arc...**

Let me examine the story structure, pacing, and narrative progression across the manuscript. I'll assess the overall narrative arc and identify any structural issues.

Analysis in progress..."

### 2. Analyze Story Structure (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Narrative Arc Analysis Procedures" and `data/references/scoring-systems.md` - "Story Structure (20 points)" for detailed protocols.

**IF project context exists:**
- Compare manuscript structure to intended framework
- Identify deviations from planned structure
- Store as: `structure_alignment` with alignment_score, deviations, notes

**Story Structure Assessment:**
- Identify narrative phases: Exposition/Setup, Inciting Incident, Rising Action, Climax, Falling Action, Resolution
- For each: Note presence/absence, location, effectiveness
- Store as: `narrative_phases` with phase_name, present, location, quality

**Arc Completion Analysis:**
- Assess completion (0-100%)
- Identify incomplete or underdeveloped elements
- Store as: `arc_completion` with completion_percentage, missing_elements, assessment

After analysis:
"✅ **Story Structure:** {assessment}"
  - Phases present: {list}
  - Arc completion: {percentage}%

### 3. Evaluate Pacing Across Manuscript (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Pacing Evaluation" and `data/references/scoring-systems.md` - "Pacing Quality (20 points)".

**Per-Chapter Pacing:**
- For each chapter: Assess pacing (too slow / balanced / too fast)
- Note pacing changes between chapters
- Store as: `pacing_by_chapter` with chapter_number, pacing_assessment, notes

**Overall Pacing Assessment:**
- Identify: rushed sections, dragging sections, pacing inconsistencies
- Store as: `pacing_assessment` with overall_pacing, issues_found, recommendations

**Rhythm and Flow:**
- Assess narrative rhythm and flow between chapters
- Store as: `rhythm_flow` with flow_quality, issues, examples

After analysis:
"✅ **Pacing Assessment:** {overall_assessment}"
  - Issues found: {count}
  - Chapters with pacing concerns: {list}

### 4. Assess Character Arc Progression (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Setup/Payoff Tracking" and `data/references/scoring-systems.md` - "Character Arc Progression (15 points)".

**IF character audits available:**
- Cross-reference arc phases with manuscript
- Verify arc progression matches reported phases
- Store as: `character_arc_validation` with character_name, reported_phase, actual_progression, alignment

**Character Arc Completion:**
- For each major character: Assess arc completion
- Store as: `character_arcs` with character_name, arc_completion, issues

After analysis:
"✅ **Character Arcs:** {count} characters assessed"
  - Complete arcs: {count}
  - Incomplete arcs: {count}
  - Stalled arcs: {count}

### 5. Identify Setup and Payoff (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Setup/Payoff Tracking" and `data/references/scoring-systems.md` - "Setup/Payoff Validity (15 points)".

**Track Setups:**
- Identify: foreshadowing, mysteries, character goals, plot elements
- For each: Note chapter, type, expected payoff
- Store as: `setups` with setup_description, chapter, type, payoff_status

**Track Payoffs:**
- Identify delivered payoffs
- For each: Note chapter, type, setup_reference
- Store as: `payoffs` with payoff_description, chapter, type, setup_reference

**Validation:**
- Match payoffs to setups
- Identify orphaned setups and unearned payoffs
- Store as: `setup_payoff_analysis` with matched_pairs, orphaned_setups, unearned_payoffs

After analysis:
"✅ **Setup/Payoff:** {matched_count} matched, {orphaned_count} orphaned setups, {unearned_count} unearned payoffs"

### 6. Evaluate Narrative Transitions (CORE)

**Reference:** See `data/references/scoring-systems.md` - "Transition Quality (10 points)".

**Chapter-to-Chapter Transitions:**
- For each: Assess quality, note smooth vs. jarring
- Store as: `transitions` with from_chapter, to_chapter, quality, issues

**Scene Transitions:**
- Assess scene transition quality within chapters
- Store as: `scene_transitions` with chapter, transition_quality, issues

After analysis:
"✅ **Transitions:** {overall_assessment}"
  - Problematic transitions: {count}

### 7. Compile Narrative Arc Health Score (CORE)

**Reference:** See `data/references/scoring-systems.md` - "Narrative Arc Scoring" for complete scoring breakdown.

**Calculate Score (0-100):**
- Story structure completeness: 20 points
- Arc completion: 20 points
- Pacing quality: 20 points
- Character arc progression: 15 points
- Setup/payoff validity: 15 points
- Transition quality: 10 points

Store as: `narrative_arc_health_score` with score, breakdown, assessment_label

**Assessment Labels:**
- 90-100: Excellent — Strong narrative arc with minimal issues
- 75-89: Good — Solid narrative arc with minor weaknesses
- 60-74: Fair — Functional arc with notable issues
- 40-59: Poor — Significant structural problems
- 0-39: Critical — Major narrative arc failures

After compilation:
"✅ **Narrative Arc Health Score:** {score}/100 — {label}"

### 8. Update Output File and Present Summary

**Reference:** See `data/templates/audit-report-template.md` - "Narrative Arc Analysis Section Template" for output format.

Update `{outputFile}` frontmatter with narrative arc health score and completion status. Append narrative arc analysis section.

Present analysis summary with:
- Narrative Arc Health Score
- Analysis breakdown table
- Top 3-5 key findings

Auto-proceeding to coherence analysis...

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Story structure analyzed with phases identified
- Pacing assessed across manuscript with specific issues noted
- Character arc progression evaluated
- Setup/payoff tracked and validated
- Transitions assessed for quality
- Narrative arc health score calculated (0-100)
- Output file updated with analysis section
- Key findings identified and summarized

### SYSTEM FAILURE:
- Not analyzing story structure across manuscript
- Not assessing pacing thoroughly
- Not evaluating character arc progression
- Not tracking setup/payoff relationships
- Not assessing transition quality
- Not calculating health score
- Not updating output file with findings

**Master Rule:** Narrative arc analysis is foundational for understanding story health. Every structural aspect should be examined, every pacing issue noted, all setups and payoffs tracked. The coherence check depends on understanding the narrative structure first.
