---
name: 'step-04-review'
description: 'Multi-agent review of chapter draft by 4 specialized BBB agents'

# Navigation
nextStepFile: './step-05-user-review.md'

# Output
outputFile: '{bbb_output_folder}/chapters/chapter-{chapter_number}.md'

# Agent References (for subprocess calls)
continuityEditorAgent: '{project-root}/_bmad/bmad-book-builder/agents/continuity-editor.yaml'
documentalisteAgent: '{project-root}/_bmad/bmad-book-builder/agents/documentaliste.yaml'
styleCoachAgent: '{project-root}/_bmad/bmad-book-builder/agents/style-coach.yaml'
characterKeeperAgent: '{project-root}/_bmad/bmad-book-builder/agents/character-keeper.yaml'

# Reference Data
antiSlopChecklist: '../data/anti-slop-checklist.md'
multiAgentReviewSpec: '../data/references/multi-agent-review-specification.md'
---

# Step 4: Multi-Agent Review

## STEP GOAL:

To automatically review the chapter draft using 4 specialized BBB agents in parallel, each providing their expert perspective on the chapter quality.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- CRITICAL: Read the complete step file before taking any action
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:

- You are orchestrating a **Multi-Agent Review**
- 4 specialized agents each review from their expertise
- Aggregate findings for the author

### Step-Specific Rules:

- Use **Pattern 4 (Parallel Execution)** for agent reviews
- Each agent returns structured findings, not full content
- Aggregate all findings into a unified review report
- If subprocess unavailable, perform reviews sequentially in main thread
- All review specifications are in `{multiAgentReviewSpec}`

## CONTEXT BOUNDARIES:

- Draft from step-03 is complete and saved
- All context (bible, style, plan, previous chapters) still loaded
- Each agent has their specialized perspective
- Focus: Quality assessment, not revision

## MANDATORY SEQUENCE

**CRITICAL:** Read `{multiAgentReviewSpec}` for complete review specifications before executing.

### 1. Announce Review

Display announcement as specified in `{multiAgentReviewSpec}`:

```
**Initiating Multi-Agent Review...**

Your chapter will be reviewed by 4 specialized agents:
1. **Continuity Editor** — Plan adherence and narrative continuity
2. **Documentaliste** — Factual accuracy verification
3. **Style Coach** — Voice matching and anti-slop detection
4. **Character Keeper** — Bible consistency check

Running reviews...
```

### 2. Execute Parallel Agent Reviews (Pattern 4)

Execute agent reviews per specifications in `{multiAgentReviewSpec}`:

**Pattern 4: Parallel Execution**
- Launch 4 subprocesses simultaneously
- Each subprocess loads the specified agent
- Each returns structured JSON findings
- Parent aggregates all results

**Agent Specifications:**
- Agent 1: Continuity Editor (see spec for analysis focus and return structure)
- Agent 2: Documentaliste (see spec for analysis focus and return structure)
- Agent 3: Style Coach (see spec for analysis focus and return structure)
- Agent 4: Character Keeper (see spec for analysis focus and return structure)

**Fallback Protocol:**
If subprocesses unavailable, perform reviews sequentially in main context as specified in fallback section of `{multiAgentReviewSpec}`.

### 3. Aggregate Review Results

Compile all agent findings into unified report using the format specified in `{multiAgentReviewSpec}`.

**Report Format:**
- Agent status table
- Overall status (PASS / NEEDS REVISION / MAJOR ISSUES)
- Detailed findings by category
- Voice score for Style Coach

### 4. Save Review Results

Append review report to {outputFile} using the format specified in `{multiAgentReviewSpec}`:

```markdown
## Multi-Agent Review

**Date:** {date}
**Overall Status:** {status}

### Agent Results

| Agent | Pass | Issues |
|-------|------|--------|
| Continuity Editor | {pass} | {count} |
| Documentaliste | {pass} | {count} |
| Style Coach | {pass} | {count} |
| Character Keeper | {pass} | {count} |

### Issues to Address
{detailed list}
```

Update frontmatter:
- Add 'step-04-review' to stepsCompleted

### 5. Auto-Proceed to User Review

"**Review complete. Proceeding to user review...**"

→ Automatically load {nextStepFile}

(No menu at this step — auto-proceed to user review)

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- All 4 agents executed their review
- Structured findings returned from each
- Findings aggregated into unified report
- Report saved to output file
- Clear status communicated

### SYSTEM FAILURE:

- Skipping any agent review
- Not aggregating findings properly
- Generic review instead of agent-specific perspectives
- Not saving review results

**Master Rule:** Every review perspective matters. Do not skip agents or combine their findings prematurely.
