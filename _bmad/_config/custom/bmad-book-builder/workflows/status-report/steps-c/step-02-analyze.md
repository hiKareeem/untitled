---
name: 'step-02-analyze'
description: 'Analyze scan data and determine status for all categories'

# Navigation
nextStepFile: './step-03-generate.md'

# Output
outputFile: '{bbb_output_folder}/reports/status-report-{date}.md'
---

# Step 2: Analyze Data

## STEP GOAL:
To analyze the raw scan data from Step 1 and determine status classifications, currency assessments, and identify items needing attention across all categories.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Character Keeper (Marie)** analyzing scanned data to determine status
- Like an auditor reviewing collected records to assess their currency and completeness
- Your analysis reveals patterns, identifies gaps, and highlights what needs attention
- You transform raw data into actionable insights

### Step-Specific Rules:
- Focus ONLY on analyzing scan data and determining status
- FORBIDDEN to generate the final report in this step
- Apply consistent status logic across all categories
- Identify items that need attention
- Store analysis results in structured format

## EXECUTION PROTOCOLS:
- Analyze each category systematically
- Apply status determination logic consistently
- Calculate completion percentages
- Identify gaps and attention items
- Store all analysis results for report generation
- Auto-proceed to step 3 after analysis complete

## CONTEXT BOUNDARIES:
- Has access to all scan data from step 1
- No external file reading needed — analysis is based on collected data
- Focus: Status determination and pattern recognition, not report generation

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Analysis Phase

"**Analyzing Scan Data...**

Now I'll examine the collected data to determine status classifications, identify currency gaps, and highlight items needing attention.

Analysis in progress..."

### 2. Analyze Chapter Status

**Reference:** See `data/analysis/analysis-procedures.md` → "Chapter Status Analysis Procedure"

**For each planned chapter:**
- Determine status (Complete/Draft/Planned)
- Calculate chapter metrics
- Identify last complete chapter
- Store analysis results

**Progress Update:**
"✅ **Chapter Status Analyzed:** {percent}% complete ({complete}/{total} chapters)"

### 3. Analyze Character Arc Status

**Reference:** See `data/analysis/analysis-procedures.md` → "Character Arc Status Analysis Procedure"

**For each character dossier:**
- Determine arc progression
- Cross-reference audit status
- Store analysis results

**Progress Update:**
"✅ **Character Arcs Analyzed:** {count} characters tracked"

### 4. Analyze Bible Currency

**Reference:** See `data/analysis/analysis-procedures.md` → "Bible Currency Analysis Procedure"

**For each Living Bible dimension:**
- Determine currency status
- Calculate bible metrics
- Store analysis results

**Progress Update:**
"✅ **Bible Currency Analyzed:** {count}/5 dimensions up to date"

### 5. Analyze Thematic Tracking

**Reference:** See `data/analysis/analysis-procedures.md` → "Thematic Tracking Analysis Procedure"

**IF theme tracking data exists:**
- For each theme: extract name, progression, status
- Store analysis results

**IF theme tracking doesn't exist:**
- Store as not started

**Progress Update:**
"✅ **Thematic Tracking Analyzed:** {status}"

### 6. Analyze Rhythm Tracking

**Reference:** See `data/analysis/analysis-procedures.md` → "Rhythm Tracking Analysis Procedure"

**IF rhythm tracking exists:**
- Store as active with last updated date

**IF rhythm tracking doesn't exist:**
- Store as not started

**Progress Update:**
"✅ **Rhythm Tracking Analyzed:** {status}"

### 7. Calculate Project Health

**Reference:** See `data/analysis/analysis-procedures.md` → "Project Health Calculation Procedure"

**Calculate overall health:**
- Apply weighted components (chapters 50%, bible 30%, characters 10%, tracking 10%)
- Determine health label (Excellent/Good/Fair/Needs Attention/Early Stage)
- Store health analysis

**Progress Update:**
"✅ **Project Health Calculated:** {label} ({percent}%)"

### 8. Identify Attention Items

**Reference:** See `data/analysis/analysis-procedures.md` → "Attention Items Identification Procedure"

**Generate prioritized list:**
- High priority: Bible gaps, character inconsistencies
- Medium priority: Draft chapters, missing audits, theme issues
- Low priority: Optional tracking, documentation

**Store attention items:**
```yaml
attention_items:
  high_priority: [...]
  medium_priority: [...]
  low_priority: [...]
```

**Progress Update:**
"✅ **Attention Items Identified:** {high} high, {medium} medium, {low} low priority"

### 9. Synthesize Recent Activity

**Reference:** See `data/analysis/analysis-procedures.md` → "Recent Activity Synthesis Procedure"

**Format recent activity for report:**
- Determine file type (Chapter, Bible, Audit, Tracking, Character)
- Format date as readable
- Create brief description from file name

**Progress Update:**
"✅ **Recent Activity Formatted:** 5 recent items"

### 10. Update Output Frontmatter

**Reference:** See `data/analysis/analysis-procedures.md` → "Output Frontmatter Update Procedure"

Update {outputFile} frontmatter with analysis results as specified in reference procedures.

### 11. Present Analysis Summary

**Reference:** See `data/analysis/analysis-procedures.md` → "Analysis Summary Presentation Procedure"

Display project health overview and attention items summary as specified in reference procedures.

**Select:** `[C]` Continue to Report Generation

### MENU HANDLING LOGIC:

- IF C: Store all analysis results for step 3, update {outputFile} frontmatter with stepsCompleted: ['step-01-scan', 'step-02-analyze', 'step-03-generate'], lastStep: 'step-03-generate', then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Chapter status determined for all planned chapters (Complete/Draft/Planned)
- Character arc phases extracted and analyzed
- Bible currency assessed for all 5 dimensions
- Thematic and rhythm tracking status determined
- Project health calculated with weighted components
- Attention items identified and prioritized
- Recent activity formatted for report
- Output frontmatter updated with analysis summary

### SYSTEM FAILURE:
- Not determining status for all chapters
- Not assessing bible currency against last complete chapter
- Not calculating project health
- Not identifying attention items
- Not formatting recent activity

**Master Rule:** Analysis transforms raw scan data into actionable insights. Every item should be classified, every gap identified, priorities established. The report generation phase depends on complete, structured analysis results.
