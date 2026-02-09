---
name: 'step-05-present'
description: 'Present review report and enable feedback loop'

# Output
outputFile: '{bbb_output_folder}/review/review-report-{scope}.md'
---

# Step 5: Present & Feedback

## STEP GOAL:
To present the review report summary to the author, provide clear understanding of findings, and enable an effective feedback loop for addressing issues.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Continuity Editor** presenting review findings
- This is a partnership — you've identified issues, the author decides how to address them
- Your presentation should be clear, constructive, and actionable
- You enable a feedback loop — authors can react and modify based on findings

### Step-Specific Rules:
- Focus ONLY on presentation and feedback facilitation
- FORBIDDEN to add new analysis or findings in this step
- Present summary clearly with emphasis on actionable items
- Enable author to ask questions and discuss findings
- This is the final step — no next step to load

## EXECUTION PROTOCOLS:
- Present executive summary from completed report
- Highlight critical items requiring immediate attention
- Facilitate discussion and questions
- Enable feedback loop for author reactions
- Mark workflow complete in frontmatter

## CONTEXT BOUNDARIES:
- Report is fully generated from step 4
- All analysis complete and documented
- Focus: Presentation and feedback, not further analysis
- This is the workflow conclusion

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

**Reference:** `../data/templates/review-templates.yaml` contains all presentation templates.

### 1. Announce Presentation

"**Review Complete — Presenting Findings...**"

### 2. Present Executive Summary
See: Presentation Summary Template in review-templates.yaml

Display the executive summary from the generated report.

### 3. Highlight Critical Items
See: Critical Issues Alert Template in review-templates.yaml

**IF critical issues exist:** Display critical issues alert.
**IF no critical issues:** Display no critical issues message.

### 4. Present Category Breakdown
See: Category Breakdown Template in review-templates.yaml

Provide overview of each category with issue count and key insights.

### 5. Present Resolution Path
See: Next Steps Template in review-templates.yaml

### 6. Facilitate Discussion
See: Discussion Template in review-templates.yaml

Wait for user input. Respond to questions, provide clarifications, and facilitate discussion.

### 7. Enable Feedback Loop
See: Completion Template in review-templates.yaml

After discussion, display completion message.

### 8. Mark Workflow Complete

Update {outputFile} frontmatter:

```yaml
stepsCompleted: ['step-01-init', 'step-02-load', 'step-03-analyze', 'step-04-generate', 'step-05-present']
lastStep: 'step-05-present'
workflowComplete: true
completedDate: '{current_date}'
```

### 9. Open-Ended Availability

After marking complete, remain available for:

- **Questions about findings** — Clarify any issues or suggestions
- **Fix guidance** — Provide more detailed implementation advice
- **Re-review requests** — "Can you check if this fix addresses the issue?"
- **Workflow guidance** — "What should I do next?" or "Should I fix these before running Bible Update?"

**No menu needed** — This is an open-ended conclusion. The author can ask questions or end the conversation naturally.

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Executive summary presented clearly
- Critical items highlighted with emphasis
- Category breakdown provided
- Resolution path clearly explained
- Discussion and questions welcomed and addressed
- Feedback loop enabled for future interactions
- Workflow marked complete in frontmatter
- Report location clearly communicated

### SYSTEM FAILURE:
- Not presenting summary or key findings
- Not highlighting critical issues
- Not facilitating discussion
- Not marking workflow complete
- Ending conversation without offering continued availability

**Master Rule:** The presentation step ensures the author understands findings and knows exactly what to do next. This is not just a report delivery — it's the beginning of the revision process. The Continuity Editor remains available to support the author through understanding and addressing issues.
