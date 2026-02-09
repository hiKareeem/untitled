---
name: 'step-06-revise'
description: 'Apply author-requested revisions to the chapter draft'

# Navigation
nextStepFile: './step-05-user-review.md'

# Output
outputFile: '{bbb_output_folder}/chapters/chapter-{chapter_number}.md'

# Reference
antiSlopChecklist: '../data/anti-slop-checklist.md'

# Tasks
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 6: Revise Chapter

## STEP GOAL:

To apply the author's requested revisions to the chapter draft while maintaining voice consistency and avoiding the introduction of new issues.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- CRITICAL: Read the complete step file before taking any action
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- You are a **Chapter Writer** making targeted revisions
- Honor the author's specific requests
- Maintain the established voice while making changes

### Step-Specific Rules:

- Focus ONLY on the requested revisions
- FORBIDDEN to make unrequested changes
- Re-apply anti-slop checking to revised sections
- Preserve author's voice in all revisions

## CONTEXT BOUNDARIES:

- Author's revision requests from step-05
- Original draft available
- Style profile for voice consistency
- Focus: Targeted changes, not wholesale rewrite

## MANDATORY SEQUENCE

### 1. Review Revision Requests

Present the revision requests from the author:

"**Revision Requests for Chapter {chapter_number}**

You requested the following changes:

{list each revision request with location if specified}

I'll address each of these while maintaining your voice and style."

### 2. Process Each Revision

For each revision request:

1. **Locate the passage** — Find the exact text to revise
2. **Understand the intent** — What does the author want changed?
3. **Draft the revision** — Write new text matching author's voice
4. **Anti-slop check** — Verify no AI patterns introduced
5. **Present the change** — Show before/after

"**Revision {N}:**

**Original:**
> {original text}

**Revised:**
> {revised text}

**Changes made:** {brief description}"

### 3. Apply All Revisions

Once all revisions are drafted:

"**All Revisions Applied**

| Revision | Location | Status |
|----------|----------|--------|
| {request 1} | {location} | ✅ Applied |
| {request 2} | {location} | ✅ Applied |
| ... | ... | ... |

**Anti-Slop Check:** {passed/issues found}

The chapter has been updated with your requested changes."

### 4. Re-check Affected Sections

Run a quick anti-slop check on revised sections:

IF slop patterns detected in revisions:
"**Note:** I detected some AI patterns in the revised sections. I've adjusted them to match your voice:
{list adjustments}"

IF no issues:
"Revised sections maintain your authentic voice."

### 5. Save Revised Draft

Update {outputFile} with the revised content:

```markdown
## Draft v{version+1} (Revised)

{updated chapter content}

---
_Revised: {date}_
_Changes: {count} revisions applied_
```

Update frontmatter:
- Add 'step-06-revise' to stepsCompleted
- Increment draftVersion

### 6. Present Menu

"**Revisions Complete**

Draft version {version} is ready for your review.

Would you like to review the revised chapter?"

**Select an option:** `[A]` Advanced Elicitation `[P]` Party Mode `[C]` Continue to Review

### MENU HANDLING LOGIC:

- IF A: Execute {advancedElicitationTask}, then redisplay menu
- IF P: Execute {partyModeWorkflow}, then redisplay menu
- IF C: Update {outputFile} frontmatter, then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- All requested revisions applied
- Voice consistency maintained
- Anti-slop checked on revised sections
- Before/after shown for each change
- Draft version incremented

### SYSTEM FAILURE:

- Making unrequested changes
- Breaking voice consistency
- Introducing AI patterns in revisions
- Not tracking draft version

**Master Rule:** Only change what was requested. Preserve the author's voice in every revision.
