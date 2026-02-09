# Review Completion Reference

## 8. Present Menu Options (Final)

Display: "**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Complete Workflow"

### Execution Rules:
- ALWAYS halt and wait for user input after presenting menu
- User selects final action

### Menu Handling Logic:
- IF A: Execute {advancedElicitationTask} for deep exploration of any aspect of the profile, and when finished redisplay the menu
- IF P: Execute {partyModeWorkflow} to simulate reader perspectives on the profile, and when finished redisplay the menu
- IF C: Display completion message and mark workflow complete
- IF Any other: help user respond then redisplay menu options

## 9. Handle Complete

When user selects C:

Display:

"**✅ Style Capture Workflow Complete**

**Profile Location:** {outputFile}
**Status:** profileAccepted: true
**Generated:** {date}

Thank you for using Style Capture. Your writing voice is now preserved and ready for Chapter-Write."

**END OF WORKFLOW** — No next step

---

## System Success/Failure Metrics

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
