---
name: 'step-03-coherence-check'
description: 'Check consistency across characters, locations, objects, and timeline'

# Navigation
nextStepFile: './step-04-quality-check.md'
previousStepFile: './step-02-narrative-arc.md'

# Output
outputFile: '{bbb_output_folder}/audit/project-audit-{date}.md'
coherenceFindings: {}
---

# Step 3: Coherence Check

## STEP GOAL:
To perform comprehensive coherence validation across characters, locations, objects, and timeline to identify inconsistencies, continuity errors, and tracking issues across the manuscript.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Continuity Editor (Claude)** performing comprehensive coherence validation
- Like a continuity editor in film/TV ensuring all details match across scenes
- Consistency is credibility — readers notice what doesn't match
- You validate coherence now, quality in next step

### Step-Specific Rules:
- Focus ONLY on coherence validation (characters, locations, objects, timeline)
- Cross-reference manuscript content with Living Bible data
- Identify inconsistencies and continuity errors
- Store findings in structured format for report generation
- Auto-proceed to step 4 after coherence check complete

## EXECUTION PROTOCOLS:
- Validate character consistency across all appearances
- Verify location accuracy and spatial consistency
- Track object presence and state changes
- Validate timeline and chronological sequences
- Identify plot holes and narrative gaps
- Store all findings in structured format
- Auto-proceed to step 4 after coherence check complete

## CONTEXT BOUNDARIES:
- Has access to all loaded chapters from step 1
- Has access to Living Bible dimensions
- Has access to character audits from step 1
- Analysis is read-only — no modifications to any files
- Focus: Coherence and continuity validation

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Coherence Check Phase

"**Performing Coherence Check...**

Let me validate consistency across characters, locations, objects, and timeline throughout the manuscript. I'll cross-reference with the Living Bible to identify any continuity issues.

Coherence validation in progress..."

### 2. Validate Character Consistency (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Character Consistency Checks" and `data/references/scoring-systems.md` - "Character Consistency (30 points)".

**For each major character:**
- Track all appearances across chapters
- Validate: voice, behavior, physical description consistency
- Validate knowledge and memory continuity
- Validate relationship consistency
- Cross-reference with Living Bible (if exists)
- Store as: `character_{name}_coherence` with appearances, voice_consistency, behavior_consistency, description_consistency, issues_found

After validation:
"✅ **Character Consistency:** {count} characters validated"
  - Consistent: {count}
  - Issues found: {count}

### 3. Validate Location Accuracy (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Location Validation" and `data/references/scoring-systems.md` - "Location Accuracy (20 points)".

**For each location:**
- Track all appearances across chapters
- Validate: description consistency, geographic consistency
- Validate spatial and movement accuracy
- Cross-reference with Living Bible (if exists)
- Store as: `location_{name}_coherence` with name, appearances, description_consistency, geographic_consistency, issues_found

After validation:
"✅ **Location Accuracy:** {count} locations validated"
  - Consistent: {count}
  - Issues found: {count}

### 4. Validate Object Tracking (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Object Tracking" and `data/references/scoring-systems.md` - "Object Tracking (15 points)".

**For each significant object:**
- Track all appearances across chapters
- Validate: presence continuity, state changes
- Validate special/magical object rules
- Cross-reference with Living Bible (if exists)
- Store as: `object_{name}_coherence` with name, appearances, presence_consistency, state_changes, issues_found

After validation:
"✅ **Object Tracking:** {count} objects validated"
  - Consistent: {count}
  - Issues found: {count}

### 5. Validate Timeline and Chronology (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Timeline Validation" and `data/references/scoring-systems.md` - "Timeline Validation (20 points)".

**For each major event:**
- Track temporal placement across manuscript
- Validate: sequence, duration, timing
- Validate flashback/flashforward handling
- Cross-reference with Living Bible (if exists)
- Store as: `event_sequence_coherence` with event, temporal_placement, sequence_issues

After validation:
"✅ **Timeline Validation:** {assessment}"
  - Consistent: {status}
  - Issues found: {count}

### 6. Detect Plot Holes and Narrative Gaps (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Plot Hole Detection" and `data/references/scoring-systems.md` - "Plot Hole Absence (15 points)".

**Identify:**
- Missing information critical to plot
- Unresolved plot threads
- Logic gaps and contradictions
- Cause/effect violations
- Dropped storylines
- Unanswered questions

Store as: `narrative_gaps`, `logic_inconsistencies`, `unresolved_elements` with descriptions, locations, severity

After detection:
"✅ **Plot Hole Detection:** {count} issues found"
  - Critical: {count}
  - Major: {count}
  - Minor: {count}

### 7. Compile Coherence Health Score (CORE)

**Reference:** See `data/references/scoring-systems.md` - "Coherence Scoring" for complete breakdown.

**Calculate Score (0-100):**
- Character consistency: 30 points
- Location accuracy: 20 points
- Object tracking: 15 points
- Timeline validation: 20 points
- Plot hole absence: 15 points

Store as: `coherence_health_score` with score, breakdown, assessment_label

**Assessment Labels:**
- 90-100: Excellent — Minimal coherence issues
- 75-89: Good — Minor inconsistencies
- 60-74: Fair — Notable coherence problems
- 40-59: Poor — Significant continuity errors
- 0-39: Critical — Major coherence failures

After compilation:
"✅ **Coherence Health Score:** {score}/100 — {label}"

### 8. Update Output File and Present Summary

**Reference:** See `data/templates/audit-report-template.md` - "Coherence Check Section Template" for output format.

Update `{outputFile}` frontmatter with coherence health score and completion status. Append coherence check section.

Present coherence check summary with:
- Coherence Health Score
- Coherence breakdown table
- Critical issues found

Auto-proceeding to quality analysis...

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Character consistency validated across all appearances
- Location accuracy verified with geographic and spatial checks
- Object tracking validated with presence and state checks
- Timeline validated with sequence and timing checks
- Plot holes and narrative gaps identified
- Coherence health score calculated (0-100)
- Output file updated with coherence section
- Critical issues identified and prioritized

### SYSTEM FAILURE:
- Not validating character consistency thoroughly
- Not checking location accuracy
- Not tracking object continuity
- Not validating timeline
- Not detecting plot holes
- Not calculating health score
- Not updating output file with findings

**Master Rule:** Coherence validation is critical for narrative credibility. Every dimension should be checked, every inconsistency noted, all continuity errors documented. The quality check depends on ensuring coherence first.
