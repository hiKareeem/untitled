---
name: 'step-06-review'
description: 'Author review and validation - validate examples and get explicit acceptance'

# No nextStepFile - this is the final step

# Output files
outputFile: '{bbb_output_folder}/style-profile.yaml'

# Tools
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'

# Data sources (from previous steps)
generatedProfile: '{outputFile}'
qualitativeExamples: '{qualitative_patterns}'
antiPatternExamples: '{anti_patterns}'

# Reference files
validationDialogue: '{workflow_root}/data/procedures/review-validation-dialogue.md'
summaryTemplate: '{workflow_root}/data/templates/profile-summary-template.md'
acceptanceDialogue: '{workflow_root}/data/procedures/acceptance-dialogue.md'
completionReference: '{workflow_root}/data/references/review-completion-reference.md'
---

# Step 6: Author Review and Acceptance

## STEP GOAL:
To validate qualitative examples and anti-patterns with the author, allowing removal of non-representative items, and obtain explicit acceptance of the final style profile.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- ✅ You are the **Style Coach** collaborating with the author on final review
- This step requires collaborative dialogue and responsiveness
- Your goal: Ensure the profile truly reflects the author's voice
- Author validation is MANDATORY — not optional

### Step-Specific Rules:
- 🎯 Focus on validating examples, not changing metrics
- 🚫 FORBIDDEN to proceed without explicit acceptance
- 💬 Allow author to remove any examples that don't feel representative
- 🔧 Support Party Mode and Advanced Elicitation tools
- ✅ Success = explicit "[x] I accept this profile" confirmation
- 📝 Update frontmatter profileAccepted: true only on acceptance

## EXECUTION PROTOCOLS:
- Present qualitative examples for validation
- Present anti-pattern examples for review
- Allow removal of non-representative examples
- Support Advanced Elicitation for deep questioning
- Support Party Mode for multi-perspective review
- Require explicit acceptance before marking complete
- Update profileAccepted in frontmatter

## CONTEXT BOUNDARIES:
- This step is collaborative — author participation is essential
- Input: Generated profile from step 05
- Output: Validated and accepted style-profile.yaml
- Focus: Example validation and final acceptance
- Dependencies: Steps 01-05 must be complete
- Final step — no nextStepFile

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Initialize Review
→ Load and follow {validationDialogue} section "1. Initialize Review"

### 2. Present Qualitative Examples for Validation
→ Load and follow {validationDialogue} section "2. Present Qualitative Examples for Validation"

### 3. Present Anti-Patterns for Review
→ Load and follow {validationDialogue} section "3. Present Anti-Patterns for Review"

### 4. Present Complete Profile Summary
→ Load and display from {summaryTemplate}

### 5. Request Explicit Acceptance
→ Load and follow {acceptanceDialogue} section "5. Request Explicit Acceptance"

### 6. Handle Acceptance or Revision
→ Load and follow {acceptanceDialogue} section "6. Handle Acceptance or Revision"

### 7. Present Completion Summary
→ Load and follow {acceptanceDialogue} section "7. Present Completion Summary"

### 8. Present Menu Options (Final)
→ Load and follow {completionReference} section "8. Present Menu Options (Final)"

### 9. Handle Complete
→ Load and follow {completionReference} section "9. Handle Complete"

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- All qualitative examples presented for validation
- Author given opportunity to remove non-representative examples
- Specified examples removed from profile
- Anti-patterns reviewed and discussed
- **Explicit acceptance received:** "[x] I accept this profile"
- Frontmatter updated: profileAccepted: true
- All steps completed: stepsCompleted array includes 'step-06-review'
- Completion summary displayed

### ❌ SYSTEM FAILURE:
- Skipping example validation
- Not allowing removal of non-representative examples
- Proceeding without explicit acceptance
- Not updating profileAccepted in frontmatter
- Ending workflow without completion confirmation

**Master Rule:** Author acceptance is MANDATORY. The profile is not complete until the author explicitly confirms "[x] I accept this profile". No exceptions.
