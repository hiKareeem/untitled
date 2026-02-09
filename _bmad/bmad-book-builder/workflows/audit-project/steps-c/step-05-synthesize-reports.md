---
name: 'step-05-synthesize-reports'
description: 'Aggregate insights from previous reports and tracking data'

# Navigation
nextStepFile: './step-06-generate-report.md'
previousStepFile: './step-04-quality-check.md'

# Output
outputFile: '{bbb_output_folder}/audit/project-audit-{date}.md'
synthesisFindings: {}
---

# Step 5: Synthesize Previous Reports

## STEP GOAL:
To aggregate insights from all previous review reports, character audits, and tracking data to identify recurring patterns, systemic issues, and track progress over time — providing a historical context for current audit findings.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Continuity Editor (Claude)** synthesizing historical analysis data
- Like a lead editor compiling insights from multiple review rounds
- Understanding patterns over time reveals systemic issues
- You synthesize now, generate final report in next step

### Step-Specific Rules:
- Focus ONLY on aggregating and analyzing previous reports
- Identify recurring patterns and systemic issues
- Track issue resolution and recurrence
- Compare current findings with historical data
- Store synthesis in structured format for report generation
- Auto-proceed to step 6 after synthesis complete

## EXECUTION PROTOCOLS:
- Aggregate findings from all previous review reports
- Synthesize character audit insights
- Incorporate theme and rhythm tracking data
- Identify recurring patterns and systemic issues
- Track issue resolution status
- Compare current audit with historical data
- Store all synthesis in structured format
- Auto-proceed to step 6 after synthesis complete

## CONTEXT BOUNDARIES:
- Has access to all previous review reports from step 1
- Has access to character audit reports from step 1
- Has access to theme and rhythm tracking from step 1
- Has access to current audit findings from steps 2-4
- Analysis is read-only — no modifications to any files
- Focus: Historical pattern analysis and synthesis

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Synthesis Phase

"**Synthesizing Previous Reports...**

Let me aggregate insights from all previous reviews, character audits, and tracking data to identify recurring patterns, systemic issues, and track progress over time.

Synthesis in progress..."

### 2. Aggregate Review Report Insights (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Historical Analysis" section.

**IF previous reviews exist:**
- Extract key findings, issues, severity from each review
- Track issue types and frequencies
- Identify: recurring issues, resolved issues, new issues
- Track quality trends over time
- Store as: `review_history_analysis` with total_reviews, recurring_issues, resolved_issues, new_issues, trends

**IF no previous reviews:**
- Note "No previous review reports — this is baseline audit"
- Store as: `review_history_analysis: {baseline_audit: true}`

After aggregation:
"✅ **Review History:** {count} reviews analyzed"
  - Recurring issues: {count}
  - Resolved issues: {count}
  - New issues: {count}
  - Quality trend: {direction}

### 3. Synthesize Character Audit Insights (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Character Audit Synthesis" section.

**IF character audits exist:**
- Extract arc phase, issues, recommendations from each audit
- Track character arc progression over time
- Identify development patterns and recurring issues
- Compare with current coherence check
- Store as: `character_audit_synthesis` with character_name, audit_history, arc_progression, recurring_issues

**IF no character audits:**
- Note "No character audits — character analysis based on manuscript only"
- Store as: `character_audit_synthesis: {no_audits: true}`

After synthesis:
"✅ **Character Audits:** {count} characters audited"
  - Strong progression: {count}
  - Needs work: {count}
  - Stalled: {count}

### 4. Incorporate Theme Tracking Data (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Theme Progression Analysis" section.

**IF theme tracking exists:**
- Extract theme phases and progression
- Compare with current thematic coherence findings
- Validate theme presence and progression
- Assess currency of tracking
- Store as: `theme_tracking_synthesis` with themes_tracked, progression_validation, underdeveloped_themes

**IF no theme tracking:**
- Note "No theme tracking — themes identified from manuscript analysis"
- Store as: `theme_tracking_synthesis: {no_tracking: true}`

After incorporation:
"✅ **Theme Tracking:** {status}"
  - Themes tracked: {count}
  - Currency: {status}

### 5. Incorporate Rhythm Analysis Data (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Rhythm and Pacing Insights" section.

**IF rhythm analysis exists:**
- Extract pacing findings and rhythm patterns
- Compare with current narrative arc pacing assessment
- Validate pacing consistency
- Assess currency of tracking
- Store as: `rhythm_tracking_synthesis` with pacing_findings, validation, issues_alignment

**IF no rhythm analysis:**
- Note "No rhythm tracking — pacing based on manuscript analysis only"
- Store as: `rhythm_tracking_synthesis: {no_tracking: true}`

After incorporation:
"✅ **Rhythm Analysis:** {status}"
  - Pacing findings: {count}
  - Currency: {status}

### 6. Identify Systemic Patterns (CORE)

**Reference:** See `data/references/audit-procedures.md` - "Systemic Pattern Recognition" section.

**Identify:**
- Issues appearing across multiple analysis dimensions
- Workflow alignment issues and contradictions
- Consistent strengths across all dimensions

Store as: `systemic_patterns`, `workflow_alignment`, `strength_patterns` with pattern_name, appears_in, severity, examples

After identification:
"✅ **Systemic Patterns:** {count} patterns identified"
  - Systemic issues: {count}
  - Strengths: {count}

### 7. Tracking Data Currency Assessment (CORE)

**Reference:** See `data/references/scoring-systems.md` - "Data Currency Scoring" section.

**Assess currency:**
- Living Bible dimensions (5 dimensions)
- Tracking data (themes, rhythm)
- Character audits

Store as: `bible_currency`, `tracking_currency`, `audit_currency` with currency_status, last_updated, coverage

After assessment:
"✅ **Data Currency:** Bible {bible_status}, Tracking {tracking_status}, Audits {audit_status}"

### 8. Compare Current vs. Historical (CORE)

**Reference:** See `data/references/scoring-systems.md` - "Historical Progress Scoring" section.

**Compare:**
- Overall improvement or decline
- Dimension-by-dimension changes
- Issue resolution (resolved, persistent, new)

Store as: `overall_progress`, `dimension_comparison`, `issue_resolution_tracking` with direction, changes, trends

After comparison:
"✅ **Progress Assessment:** {overall_direction}"
  - Significant improvements: {count}
  - Persistent concerns: {count}
  - New issues: {count}"

### 9. Update Output File and Present Summary

**Reference:** See `data/templates/audit-report-template.md` - "Historical Analysis Section Template" for output format.

Update `{outputFile}` frontmatter with synthesis completion status. Append historical analysis synthesis section.

Present synthesis summary with:
- Historical data processed table
- Top 3-5 synthesis findings
- Systemic patterns identified
- Progress assessment

Auto-proceeding to report generation...

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- All previous review reports aggregated and analyzed
- Character audit insights synthesized with progression tracking
- Theme tracking data incorporated and validated
- Rhythm analysis data incorporated and validated
- Systemic patterns identified across workflows
- Data currency assessed for all sources
- Current vs. historical comparison completed
- Output file updated with synthesis section
- Key findings and trends identified

### SYSTEM FAILURE:
- Not aggregating all previous review reports
- Not synthesizing character audit insights
- Not incorporating tracking data
- Not identifying systemic patterns
- Not assessing data currency
- Not comparing current vs. historical
- Not updating output file with synthesis

**Master Rule:** Report synthesis is crucial for understanding patterns over time. Every previous report should be analyzed, every pattern identified, all trends documented. The final report depends on comprehensive historical context.
