---
name: 'step-04-quality-check'
description: 'Analyze style, dialogue, and prose quality across manuscript'

# Navigation
nextStepFile: './step-05-synthesize-reports.md'
previousStepFile: './step-03-coherence-check.md'

# Output
outputFile: '{bbb_output_folder}/audit/project-audit-{date}.md'
qualityFindings: {}
---

# Step 4: Quality Check

## STEP GOAL:
To analyze prose quality, dialogue effectiveness, style consistency, and thematic coherence across the manuscript to assess writing quality and identify areas for improvement.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Continuity Editor (Claude)** performing quality assessment
- Like a senior editor evaluating prose and dialogue quality
- Quality means serving the story, not imposing arbitrary rules
- You analyze quality now, synthesize previous reports in next step

### Step-Specific Rules:
- Focus ONLY on prose quality, dialogue, style, and thematic coherence
- Analyze across ALL chapters (not individual chapters)
- Identify systemic quality patterns and issues
- Store findings in structured format for report generation
- Auto-proceed to step 5 after quality check complete

## EXECUTION PROTOCOLS:
- Evaluate style consistency and voice across manuscript
- Assess dialogue quality and character voice distinctiveness
- Analyze prose metrics and readability
- Evaluate show vs tell balance
- Assess thematic coherence and progression
- Store all findings in structured format
- Auto-proceed to step 5 after quality check complete

## CONTEXT BOUNDARIES:
- Has access to all loaded chapters from step 1
- Has access to theme tracking from step 1
- Has access to Living Bible themes dimension
- Analysis is read-only — no modifications to any files
- Focus: Quality assessment across manuscript

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Quality Check Phase

"**Analyzing Prose Quality...**

Let me evaluate the writing quality across the manuscript, examining style consistency, dialogue effectiveness, prose mechanics, and thematic coherence.

Quality assessment in progress..."

### 2. Evaluate Style Consistency (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Style Consistency Evaluation" and `data/references/scoring-systems.md` - "Style Consistency (20 points)".

**Assess:**
- Narrative voice consistency across manuscript
- Tone consistency (humorous/serious, dark/light, etc.)
- Style register (sentence patterns, word choice level)
- Identify inappropriate shifts

Store as: `narrative_voice`, `tone_consistency`, `style_register` with descriptions, scores, issues

After evaluation:
"✅ **Style Consistency:** {assessment}"
  - Consistent elements: {list}
  - Issues found: {count}

### 3. Assess Dialogue Quality (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Dialogue Quality Assessment" and `data/references/scoring-systems.md` - "Dialogue Quality (25 points)".

**For each major character, assess:**
- Voice distinctiveness (10 points)
- Dialogue naturalness (7 points)
- Subtext and depth (5 points)
- Dialogue mechanics (3 points)

Store as: `dialogue_voice_distinctiveness`, `dialogue_naturalness`, `dialogue_subtext`, `dialogue_mechanics` with quality assessments and issues

After assessment:
"✅ **Dialogue Quality:** {overall_assessment}"
  - Distinctive voices: {count}/{total} characters
  - Issues found: {count}

### 4. Analyze Prose Metrics (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Prose Metrics Analysis" and `data/references/scoring-systems.md` - "Prose Metrics (25 points)".

**Analyze:**
- Vocabulary variety (6 points)
- Sentence structure variety (6 points)
- Readability (7 points)
- Show vs tell balance (6 points)

Store as: `vocabulary_variety`, `sentence_structure`, `readability`, `show_vs_tell` with scores, issues, examples

After analysis:
"✅ **Prose Metrics:** {overall_assessment}"
  - Vocabulary variety: {score}/10
  - Sentence variety: {score}/10
  - Readability: {score}/10
  - Show vs tell: {score}/10

### 5. Evaluate Thematic Coherence (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Thematic Coherence" and `data/references/scoring-systems.md` - "Thematic Coherence (20 points)".

**IF theme tracking exists:**
- Cross-reference tracked themes with manuscript
- Validate theme presence and progression
- Store as: `theme_presence` with theme_name, presence_score, progression, issues

**IF no theme tracking:**
- Identify themes through manuscript analysis
- Track theme presence and development
- Store as: `identified_themes` with theme_name, presence, development, examples

**Assess:**
- Thematic consistency with story events
- Symbol and motif tracking and effectiveness
- Cross-reference with Living Bible (if exists)

Store as: `thematic_consistency`, `symbols_motifs`, `theme_bible_comparison` with assessments

After evaluation:
"✅ **Thematic Coherence:** {assessment}"
  - Themes identified: {count}
  - Well-developed: {count}
  - Need development: {count}

### 6. Identify Quality Patterns (CORE)

**Reference:** See `data/references/scoring-systems.md` - "Quality Pattern Strength (10 points)".

**Identify:**
- Recurring quality issues across multiple chapters
- Consistent strengths across manuscript
- Developmental trajectory (improvement/decline)

Store as: `recurring_quality_issues`, `quality_strengths`, `quality_trajectory` with assessments and examples

After identification:
"✅ **Quality Patterns:** {assessment}"
  - Recurring issues: {count}
  - Strengths to maintain: {count}

### 7. Compile Quality Health Score (CORE)

**Reference:** See `data/references/scoring-systems.md` - "Quality Scoring" for complete breakdown.

**Calculate Score (0-100):**
- Style consistency: 20 points
- Dialogue quality: 25 points
- Prose metrics: 25 points
- Thematic coherence: 20 points
- Quality pattern strength: 10 points

Store as: `quality_health_score` with score, breakdown, assessment_label

**Assessment Labels:**
- 90-100: Excellent — Consistently high-quality prose
- 75-89: Good — Solid writing with minor issues
- 60-74: Fair — Competent but notable quality concerns
- 40-59: Poor — Significant quality problems
- 0-39: Critical — Major quality failures

After compilation:
"✅ **Quality Health Score:** {score}/100 — {label}"

### 8. Update Output File and Present Summary

**Reference:** See `data/templates/audit-report-template.md` - "Quality Assessment Section Template" for output format.

Update `{outputFile}` frontmatter with quality health score and completion status. Append quality assessment section.

Present quality check summary with:
- Quality Health Score
- Quality breakdown table
- Top 3-5 key quality findings

Auto-proceeding to report synthesis...

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Style consistency evaluated with voice, tone, and register analysis
- Dialogue quality assessed with voice distinctiveness and naturalness
- Prose metrics analyzed with vocabulary, sentence structure, and readability
- Show vs tell balance evaluated
- Thematic coherence assessed with theme tracking and symbol/motif analysis
- Quality patterns identified (recurring issues and strengths)
- Quality health score calculated (0-100)
- Output file updated with quality section
- Key findings identified and summarized

### SYSTEM FAILURE:
- Not evaluating style consistency thoroughly
- Not assessing dialogue quality comprehensively
- Not analyzing prose metrics
- Not evaluating show vs tell balance
- Not assessing thematic coherence
- Not identifying quality patterns
- Not calculating health score
- Not updating output file with findings

**Master Rule:** Quality assessment is essential for identifying writing strengths and weaknesses. Every quality dimension should be examined, every issue noted, all strengths documented. The report synthesis depends on comprehensive quality analysis.
