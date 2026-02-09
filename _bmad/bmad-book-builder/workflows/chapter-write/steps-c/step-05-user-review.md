---
name: 'step-05-user-review'
description: 'Present chapter and review findings to author for approval or revision requests'

# Navigation
nextStepApprove: './step-07-finalize.md'
nextStepRevise: './step-06-revise.md'

# Output
outputFile: '{bbb_output_folder}/chapters/chapter-{chapter_number}.md'
---

# Step 5: User Review

## STEP GOAL:

To present the chapter draft and multi-agent review findings to the author, collecting their feedback for either approval or revision.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- You are presenting work for **author review**
- The author has final say on their chapter
- Be helpful in explaining findings, not defensive

### Step-Specific Rules:

- Focus ONLY on presenting and collecting feedback
- FORBIDDEN to make changes in this step
- Author decides: approve, revise, or provide specific feedback
- This is a decision point that may loop back to revision

## CONTEXT BOUNDARIES:

- Draft complete from step-03
- Review findings complete from step-04
- Author sees everything and decides next action
- This step may repeat after revisions

## MANDATORY SEQUENCE

### 1. Present Chapter for Review

"**Chapter {chapter_number} Ready for Your Review**

The draft is complete and has been reviewed by our specialist agents. Please review the chapter and the findings below.

---

## Your Chapter

{Present full chapter text or offer to display sections}

---

**Word Count:** {count}
**Draft Version:** {version}"

### 2. Present Review Summary

"## Review Findings

| Agent | Status | Summary |
|-------|--------|---------|
| Continuity Editor | {status} | {summary} |
| Documentaliste | {status} | {summary} |
| Style Coach | {status} | Voice: {score}% |
| Character Keeper | {status} | {summary} |

**Issues Requiring Attention:** {count}

{If issues exist, list them with brief descriptions}"

### 3. Gather Author Feedback

"## Your Feedback

Please review the chapter and let me know:

**[A] Approve** — Chapter is ready for finalization
**[R] Revise** — I have changes to request

If you choose Revise, please describe what you'd like changed:
- Specific passages to rewrite
- Tone or pacing adjustments
- Character voice corrections
- Any other modifications

You can also ask questions about the review findings."

Wait for author response.

### 4. Process Author Decision

**IF [A] Approve:**
"**Chapter Approved!**

Proceeding to finalization where we'll:
- Lock the chapter text
- Generate the chapter metadata (summary, key points)
- Update project tracking

Ready to finalize?"

Update frontmatter:
- Add 'step-05-user-review' to stepsCompleted
- Set status: 'approved'

→ Load {nextStepApprove}

**IF [R] Revise:**
"**Revision Requested**

I've noted your feedback:
{summarize author's revision requests}

I'll now revise the chapter based on your requests and return for another review.

Proceeding to revision..."

Update frontmatter:
- Set status: 'needs-revision'
- Store revision requests

→ Load {nextStepRevise}

**IF questions or other input:**
Answer the author's questions, provide clarification, then redisplay the menu:

**Select an option:** `[A]` Approve `[R]` Revise

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Chapter and findings clearly presented
- Author feedback collected
- Clear routing based on decision
- Revision requests captured accurately

### SYSTEM FAILURE:

- Making changes without author request
- Proceeding without explicit approval
- Not capturing revision requests properly
- Ignoring author questions

**Master Rule:** The author decides. Present, listen, then act on their decision.
