---
name: 'step-05-review'
description: 'Present migration plan to author, allow adjustments, and obtain final approval'

# File references (ONLY variables used in this step)
nextStepFile: './step-06-execute.md'
outputFile: '{bbb_output_folder}/bbb-onboarding-plan-{project_name}.md'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
---

# Step 5: Review with Author

## STEP GOAL:

Present the migration plan to the author, allow questions and adjustments, and obtain explicit approval (PROCEED) or cancellation (ABORT) before execution.

## MANDATORY EXECUTION RULES:
### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:
- ✅ You are a Migration Specialist — careful and consultative
- ✅ This is a QUALITY GATE — execution depends on approval
- ✅ Be patient and thorough in explanations
- ✅ Author MUST understand before proceeding

### Step-Specific Rules:
- 🎯 Focus on understanding and consent
- 🚫 FORBIDDEN to proceed without explicit PROCEED
- 💬 Allow questions and adjustments
- ⚠️ This is the LAST CHANCE to abort safely

## EXECUTION PROTOCOLS:
- 🎯 Present plan clearly and completely
- 💾 Allow plan modifications if requested
- 📖 Obtain explicit PROCEED or ABORT
- 🚫 Only proceed with PROCEED confirmation

## CONTEXT BOUNDARIES:
- Available: Complete migration plan from step 4
- Focus: Author understanding and approval
- Limits: Review only, no execution
- Dependencies: Requires complete migration plan

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Migration Plan

Load {outputFile} completely to present to author.

### 2. Present Executive Summary

```markdown
**🎯 MIGRATION PLAN REVIEW**

Hello {user_name}! Here is the migration plan for your project **{project_name}**.

---

## Summary

Your project contains:
- {chapters} chapters
- {characters} characters
- {other_content}

**The migration will:**
1. Create the BBB structure in your project
2. Copy your chapters with BBB frontmatter (HYBRID mode)
3. Convert your characters to BBB YAML format
4. Migrate your themes and other content

**Mode: HYBRID**
- ✅ Your original files are PRESERVED
- ✅ BBB creates a structured copy
- ✅ ZERO RISK of data loss

**Estimate:** {estimated_time}
```

### 3. Present Before/After Structure

```markdown
## Before Structure

{current_structure_tree}

## After Structure (BBB)

{target_structure_tree}
```

See **BBB Folder Structure** reference for detailed layout:
`{workflow_root}/data/references/bbb-folder-structure.md`

### 4. Present Migration Steps

Present summary from migration plan:
- Step 1: Create the BBB structure
- Step 2: Migrate characters
- Step 3: Migrate chapters
- Step 4: Migrate themes and other content

For detailed procedures, see **Migration Procedures** reference:
`{workflow_root}/data/references/migration-procedures.md`

### 5. Present Risks and Warnings

```markdown
## ⚠️ Risks and Warnings

**Data loss risk: LOW**
- Hybrid mode = originals preserved
- Rollback possible

**Manual work required: MEDIUM**
- Some character attributes may need adjustment
- Review migrated content for accuracy

**Estimated time:** {estimated_time}
```

### 6. Offer Review Options

```markdown
---

## Review Options

**[A]** Advanced Elicitation — Explore implications more deeply
**[P]** Party Mode — Debate the plan with multiple perspectives
**[M]** Modify the plan — Propose changes
**[C]** Continue — Approve and execute the migration
**[X]** Cancel — Stop the workflow (no changes)

**Your choice?**
```

### 7. Handle User Input

**IF A:** Execute {advancedElicitationTask}, then redisplay menu

**IF P:** Execute {partyModeWorkflow}, then redisplay menu

**IF M:** Allow user to propose changes
- Collect requested changes
- Discuss implications
- Update plan if appropriate
- Redisplay menu

**IF X:** Abort workflow
```markdown
**⚠️ WORKFLOW CANCELED**

No changes were made to your project.

Thank you for exploring BBB. You can rerun this workflow anytime.
```
END workflow

**IF C:** Obtain FINAL APPROVAL
```markdown
**⚠️ FINAL CONFIRMATION**

You are about to approve the migration execution.

What will happen:
- ✅ Creation of BBB folders
- ✅ Hybrid copy of your files
- ✅ Conversion of characters to YAML
- ✅ Adding BBB frontmatter to chapters

**YOUR ORIGINAL FILES WILL BE PRESERVED**

Type **PROCEED** to confirm and execute,
or **ABORT** to cancel.
```

Wait for explicit "PROCEED" confirmation.

**If PROCEED confirmed:**
- Update migration plan status to "APPROVED"
- Proceed to step 6

**If ABORT:**
- Return to menu above

### 8. Final Approval and Menu

**When PROCEED confirmed:**

Update {outputFile} frontmatter:
```yaml
status: "APPROVED FOR EXECUTION"
approvedDate: "{current_date}"
```

```markdown
**✅ PLAN APPROVED**

The migration will now be executed.

Type [C] to begin execution.
```

### 9. Present MENU OPTIONS

Display: "**[C]** Execute migration"

#### EXECUTION RULES:
- ALWAYS halt and wait for user input
- ONLY proceed to execution when user selects 'C'

#### Menu Handling Logic:
- IF C: Update plan status, then load, read entire file, then execute {nextStepFile}
- IF Any other: help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- Migration plan presented clearly
- Author had opportunity to review and ask questions
- Party mode and advanced elicitation available
- Explicit PROCEED confirmation obtained
- Plan status updated to APPROVED

### ❌ SYSTEM FAILURE:
- Proceeding without explicit approval
- Not offering review opportunities
- Skipping final confirmation step
- Not handling ABORT properly

**Master Rule:** This is the CRITICAL QUALITY GATE. NO execution happens without EXPLICIT user PROCEED confirmation.
