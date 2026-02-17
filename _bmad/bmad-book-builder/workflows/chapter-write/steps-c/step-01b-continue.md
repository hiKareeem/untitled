---
name: 'step-01b-continue'
description: 'Resume chapter writing from previous session'

# Output
outputFile: '{bbb_output_folder}/book-1/chapters/chapter-{chapter_number}.md'

# Step routing
workflowFile: '../workflow.md'
nextStepOptions:
  step-01-init: './step-01-init.md'
  step-02-brief: './step-02-brief.md'
  step-03-draft: './step-03-draft.md'
  step-04-review: './step-04-review.md'
  step-05-user-review: './step-05-user-review.md'
  step-06-revise: './step-06-revise.md'
  step-07-finalize: './step-07-finalize.md'
---

# Step 1b: Continue Chapter Writing

## STEP GOAL:

To resume the chapter writing workflow from where it was left off in a previous session.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- You are a **Chapter Writer** resuming work with an author
- Welcome them back and quickly get them oriented
- Show where they left off and what comes next

### Step-Specific Rules:

- Focus ONLY on resumption and routing
- FORBIDDEN to generate new content in this step
- Read stepsCompleted to determine next action
- Present clear status before continuing

## CONTEXT BOUNDARIES:

- User has run this workflow before
- Output file exists with stepsCompleted array
- Need to reload context and route to correct next step

## MANDATORY SEQUENCE

### 1. Welcome Back

"**Welcome back!**

Let me check where we left off with your chapter..."

### 2. Read Workflow State

Load {outputFile} and read frontmatter:
- `chapterNumber`
- `stepsCompleted` array
- `lastStep`
- `draftVersion`
- `status`

### 3. Determine Current State

Analyze stepsCompleted to determine:
- Last completed step
- Next step to load
- Current status (drafting, reviewing, revising)

### 4. Present Status

"**Chapter {chapterNumber} Status**

| Item | Value |
|------|-------|
| Last Step | {lastStep} |
| Steps Completed | {stepsCompleted.length}/7 |
| Draft Version | {draftVersion} |
| Status | {status} |

**Progress:**
- [x] step-01-init (completed)
{for each step in stepsCompleted: [x] or [ ]}

**Next:** {next_step_name}"

### 5. Reload Context (if needed)

If resuming from step-03 or later, reload key context:
- Chapter plan key points
- Style profile highlights
- Brief notes (if completed)
- Draft content (if exists)
- Review findings (if completed)

### 6. Route to Next Step

"Ready to continue with **{next_step_name}**?"

**Select an option:** `[C]` Continue `[R]` Restart from beginning

### MENU HANDLING LOGIC:

- IF C: Load the appropriate next step from {nextStepOptions}
- IF R: Confirm restart, then load step-01-init.md
- IF Any other: Help user, then redisplay menu

**Routing logic:**
```
IF 'step-01-init' in stepsCompleted AND 'step-02-brief' NOT in stepsCompleted:
  → Load step-02-brief.md

IF 'step-02-brief' in stepsCompleted AND 'step-03-draft' NOT in stepsCompleted:
  → Load step-03-draft.md

IF 'step-03-draft' in stepsCompleted AND 'step-04-review' NOT in stepsCompleted:
  → Load step-04-review.md

IF 'step-04-review' in stepsCompleted AND 'step-05-user-review' NOT in stepsCompleted:
  → Load step-05-user-review.md

IF 'step-05-user-review' in stepsCompleted AND status == 'needs-revision':
  → Load step-06-revise.md

IF 'step-06-revise' in stepsCompleted AND status == 'approved':
  → Load step-07-finalize.md

IF 'step-06-revise' in stepsCompleted AND status == 'needs-revision':
  → Load step-05-user-review.md (loop back)
```

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Workflow state read correctly from output file
- Clear status presented to user
- Context reloaded for current phase
- Correct next step loaded

### SYSTEM FAILURE:

- Not reading stepsCompleted correctly
- Routing to wrong step
- Not reloading necessary context
- Starting over without user consent

**Master Rule:** Resume exactly where user left off with full context.
