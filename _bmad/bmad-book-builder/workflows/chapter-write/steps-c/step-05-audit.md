---
name: 'step-05-audit'
description: 'Character audit, continuity check, and per-chapter thematic analysis'

# Navigation
nextStepFile: './step-06-bible-update.md'

# Output
outputFile: '{bbb_output_folder}/current-book/chapters/chapter-{chapter_number}.md'
auditFile: '{bbb_output_folder}/current-book/tracking/audits/audit-chapter-{chapter_number}.md'
themeAnalysisFile: '{bbb_output_folder}/current-book/tracking/themes/chapter-{chapter_number}-themes.md'

# References
storyBiblePath: '{bbb_output_folder}/bible/'
characterDossiers: '{bbb_output_folder}/characters/'
previousChaptersFolder: '{bbb_output_folder}/current-book/chapters/'
chapterPlan: '{bbb_output_folder}/chapter-plan-*.md'
styleProfilePath: '{style_profile_path}'
lexiconPath: '{bbb_output_folder}/lexicon.md'

# Agent References
continuityEditorAgent: '{project-root}/_bmad/bmad-book-builder/agents/continuity-editor.yaml'
characterKeeperAgent: '{project-root}/_bmad/bmad-book-builder/agents/character-keeper.yaml'
---

# Step 5: Audit (Character + Continuity + Thematic Analysis)

## STEP GOAL:

To validate the chapter against the story bible for character consistency and continuity, then generate the per-chapter thematic analysis. All findings are recorded in the audit file.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- CRITICAL: Read the complete step file before taking any action
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:

- You are performing **Character and Continuity Audits**
- The story bible and character dossiers are the sources of truth
- Flag discrepancies — do not silently fix them

### Step-Specific Rules:

- Check EVERY character appearing in the chapter against their dossier/bible entry
- Check continuity against previous chapters and chapter plan
- Create the audit file with structured findings
- Create the per-chapter thematic analysis file
- Present findings to the author

## CONTEXT BOUNDARIES:

- Draft has been style-audited in step-04
- Story bible, character dossiers, and previous chapters are available
- Focus: Factual consistency, character coherence, thematic cataloging

## MANDATORY SEQUENCE

### 1. Character Audit

For each character appearing in the chapter:

**Check against dossier/bible:**
- Voice/speech register matches lexicon entry
- Mannerisms and physical details consistent
- Psychological state appropriate for current arc phase
- Relationships depicted correctly
- Backstory references accurate
- No contradictions with previous appearances

**Scoring:** Rate each character's coherence out of 10. Flag any item below 7.

### 2. Continuity Check

**Check against previous chapters:**
- Timeline consistency (events in correct order, time gaps logical)
- Object continuity (items in correct locations, states correct)
- Location details consistent with bible
- Character knowledge boundaries (no one knows things they shouldn't)
- Epigraph/rhetoric references match chapter plan

**Check against chapter plan:**
- Key beats from plan present in chapter
- No unplanned divergences (or, if divergences exist, document them)
- POV, location, timeline match plan

### 3. Create Audit File

Write `{auditFile}` with structured findings:

```markdown
# Chapter {chapter_number} Audit

**Chapter:** {chapter_number} — "{title}"
**POV:** {character}
**Date:** {date}
**Draft:** v{version} (post-style-audit revision)
**Auditor:** {method used}

---

## Style Audit

{Results from step-04, carried forward}

## Character Audit

| Character | Role | Coherence | Notes |
|-----------|------|-----------|-------|
| {name} | {POV/Supporting} | {score}/10 | {findings} |

### Detailed Findings
{Per-character breakdown}

## Continuity Check

| Item | Status | Notes |
|------|--------|-------|
| Timeline | ✅/⚠️ | {details} |
| Objects | ✅/⚠️ | {details} |
| Locations | ✅/⚠️ | {details} |
| Knowledge boundaries | ✅/⚠️ | {details} |
| Plan adherence | ✅/⚠️ | {details} |

### Flags for Future Chapters
{Any items that need monitoring going forward}
```

### 4. Create Per-Chapter Thematic Analysis

Write `{themeAnalysisFile}` cataloging:

- **Theme Presence:** Which of the 8 core themes appear, at what intensity (Dominant/Strong/Moderate/Background/Not present)
- **Detailed Thematic Analysis:** Per-theme breakdown with textual evidence
- **Symbolic Register:** New symbols introduced, recurring symbols evolved
- **Cross-Chapter Threads:** Connections to previous and future chapters

### 5. Present Findings

Present a summary of all audit findings to the author.

If critical issues found:
- Present issue with evidence
- Recommend fix
- Wait for author decision: [F] Fix / [A] Accept / [D] Defer

If no critical issues:
"**Audit complete. No critical issues found. Proceeding to bible and tracking updates...**"

### 6. Save and Proceed

Update {outputFile} frontmatter:
- Add 'step-05-audit' to stepsCompleted

→ Automatically load {nextStepFile}

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Every character checked against dossier/bible
- Continuity verified against previous chapters and plan
- Audit file created with structured findings
- Per-chapter thematic analysis created
- Critical issues flagged to author

### SYSTEM FAILURE:

- Skipping characters or continuity checks
- Not creating the audit file
- Silently fixing discrepancies instead of flagging them
- Generic findings without textual evidence

**Master Rule:** The bible is the source of truth. Flag every discrepancy — the author decides what to fix.
