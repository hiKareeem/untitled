---
name: 'step-02-brief'
description: 'Review chapter plan and confirm direction before drafting'

# Navigation
nextStepFile: './step-03-draft.md'

# Output
outputFile: '{bbb_output_folder}/current-book/chapters/chapter-{chapter_number}.md'

# Context (loaded in step-01)
chapterPlanFile: '{bbb_output_folder}/foundation/chapter-plan-{chapter_number}.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 2: Chapter Brief

## STEP GOAL:

To review what this chapter must accomplish based on the chapter plan, note any divergences from previous chapters, and confirm direction with the author before drafting.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- You are a **Chapter Writer** preparing to draft with an author
- Review the plan together to ensure alignment
- This is the last checkpoint before drafting begins

### Step-Specific Rules:

- Focus ONLY on reviewing and confirming the chapter brief
- FORBIDDEN to start writing chapter content in this step
- Identify any divergences from plan in previous chapters
- Get explicit author approval before proceeding to draft

## CONTEXT BOUNDARIES:

- All 7 inputs loaded in step-01
- Chapter plan provides the roadmap
- Previous chapter summaries may reveal divergences
- Focus: Alignment and confirmation, not creation

## MANDATORY SEQUENCE

### 1. Present Chapter Plan Summary

From the loaded chapter plan, present:

"**Chapter {chapter_number}: {title}**

**Scene Breakdown:**
{list scenes from plan with brief descriptions}

**Key Goals for This Chapter:**
- {goal 1 from plan}
- {goal 2 from plan}
- {goal 3 from plan}

**Characters Appearing:**
{list from plan}

**Location(s):**
{list from plan}

**Emotional Arc:**
{describe the emotional journey}

**Target Word Count:** 3000-6000 words"

### 2. Check for Divergences from Previous Chapters

IF chapter_number > 1:

Review previous chapter summaries for:
- Plot points that diverged from original plan
- New elements introduced
- Character developments not in original plan
- Timeline adjustments

IF divergences found:
"**Note: Previous Chapters Diverged from Plan**

The following changes occurred in earlier chapters that may affect this one:
- Chapter {X}: {divergence description}
- Chapter {Y}: {divergence description}

Should we adjust this chapter's plan accordingly?"

IF no divergences:
"Previous chapters followed the plan closely. No adjustments needed."

### 3. Confirm Key Points

"**Before we draft, let's confirm:**

1. **POV Character:** {character} — Is this correct?
2. **Timeline:** {when in story} — Any adjustments?
3. **Main Conflict:** {conflict from plan} — Still accurate?
4. **Resolution:** {how chapter ends} — Any changes?

**Style Reminders (from your profile):**
- Sentence length: {pattern from style profile}
- Vocabulary: {key traits}
- Imagery: {preferences}
- Avoid: {anti-slop patterns to watch}"

### 4. Gather Author Notes

"**Any additional notes for this chapter?**

You can add:
- Specific phrases or lines to include
- Mood or atmosphere details
- Particular scenes to emphasize
- Anything else to keep in mind

Or say 'ready' to proceed with the plan as-is."

Wait for author input. Store any notes.

### 5. Confirm Direction

"**Chapter Brief Complete**

| Element | Value |
|---------|-------|
| Chapter | {number}: {title} |
| POV | {character} |
| Scenes | {count} |
| Word Target | 3000-6000 |
| Divergences | {noted/none} |
| Author Notes | {yes/no} |

Ready to proceed to drafting?"

### 6. Update Output and Present Menu

Append brief notes to {outputFile}:
```markdown
## Chapter Brief

**Plan Confirmed:** {date}
**Divergences Noted:** {list or "None"}
**Author Notes:** {notes or "None"}
```

Update frontmatter: add 'step-02-brief' to stepsCompleted

**Select an option:** `[A]` Advanced Elicitation `[P]` Party Mode `[C]` Continue to Draft

### MENU HANDLING LOGIC:

- IF A: Execute {advancedElicitationTask}, then redisplay menu
- IF P: Execute {partyModeWorkflow}, then redisplay menu
- IF C: Update {outputFile} frontmatter, then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Chapter plan presented clearly
- Divergences from previous chapters identified
- Key points confirmed with author
- Additional notes gathered (if any)
- Brief documented in output file
- Author explicitly approves direction

### SYSTEM FAILURE:

- Skipping plan review
- Not checking for divergences
- Proceeding without author confirmation
- Not documenting the brief

**Master Rule:** Never start drafting without explicit author approval of the brief.
