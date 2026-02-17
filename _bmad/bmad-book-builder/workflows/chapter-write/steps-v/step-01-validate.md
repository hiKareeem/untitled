---
name: 'step-01-validate'
description: 'Validate existing chapter against quality criteria'

# Input
chaptersFolder: '{bbb_output_folder}/current-book/chapters/'

# Agent References
continuityEditorAgent: '{project-root}/_bmad/bmad-book-builder/agents/continuity-editor.yaml'
documentalisteAgent: '{project-root}/_bmad/bmad-book-builder/agents/documentaliste.yaml'
styleCoachAgent: '{project-root}/_bmad/bmad-book-builder/agents/style-coach.yaml'
characterKeeperAgent: '{project-root}/_bmad/bmad-book-builder/agents/character-keeper.yaml'
---

# Step 1: Validate Chapter

## STEP GOAL:

To validate an existing chapter against all quality criteria using the 4 BBB specialist agents, without making any modifications.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- This is READ-ONLY validation
- FORBIDDEN to modify chapter content
- Report findings only

### Role Reinforcement:

- You are performing quality assessment
- 4 agents review from their perspectives
- Aggregate findings into validation report

## MANDATORY SEQUENCE

### 1. Select Chapter to Validate

"**Available Chapters:**

{list chapters}

Which chapter would you like to validate?"

### 2. Load Chapter and Context

Load:
- chapter-{N}.md
- chapter-{N}-meta.yaml
- Related bible entries
- Style profile
- Previous chapter summaries

### 3. Run Multi-Agent Validation

Execute the same 4-agent review as step-04-review:

1. **Continuity Editor** — Plan/narrative coherence
2. **Documentaliste** — Factual accuracy
3. **Style Coach** — Voice/anti-slop
4. **Character Keeper** — Bible consistency

### 4. Generate Validation Report

"**Validation Report: Chapter {N}**

**Overall Status:** {PASS / CONCERNS / FAIL}

| Agent | Status | Issues |
|-------|--------|--------|
| Continuity Editor | {status} | {count} |
| Documentaliste | {status} | {count} |
| Style Coach | {status} | Voice: {score}% |
| Character Keeper | {status} | {count} |

### Detailed Findings:

{list all issues found}

### Recommendations:

{list recommended actions if issues found}"

### 5. Offer Next Steps

"**Validation Complete**

Based on findings:
- {PASS}: Chapter meets quality criteria
- {CONCERNS}: Minor issues to consider
- {FAIL}: Recommend running Edit workflow

**Options:**
- Run another validation
- Exit to Edit workflow
- Return to main menu"

(End of Validate workflow)
