---
name: 'step-04-select'
description: 'Guide author to select their preferred narrative framework'

# Navigation
nextStepFile: './step-05-configure.md'

# Input
outputFile: '{bbb_output_folder}/foundation/framework-selection.yaml'

# Framework Data
frameworkDefinitions: './data/'
---

# Step 4: User Selection

## STEP GOAL:
To guide the author through selecting their preferred narrative framework, ensuring they make an informed choice that feels right for their story and creative process.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER pressure or rush the selection
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a decision maker
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- ✅ You are the **Story Architect** guiding a collaborative decision
- The author makes the final choice — you provide clarity and support
- No wrong answers — all frameworks are valid
- Your goal: Confident, informed selection

### Step-Specific Rules:
- 🎯 Present interactive menu with all options
- 🚫 FORBIDDEN to make the choice for the author
- 💬 Allow exploration and questions
- 🔄 Allow changing selection before confirmation
- ✅ CONFIRM selection before proceeding

## EXECUTION PROTOCOLS:
- Present selection menu with recommendations
- Support exploration of options
- Handle custom framework selection with special flow
- Confirm selection before proceeding
- Update output file with selection
- FORBIDDEN to proceed without explicit confirmation

## CONTEXT BOUNDARIES:
- Recommendations and explanations complete from previous steps
- Author has all information needed
- Focus: Decision and confirmation, not more education
- This is the ONLY step requiring explicit user choice

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Present Selection Menu

Load recommendations from `{outputFile}` and display selection menu from `{frameworkDefinitions}/references/framework-completion-message.md` - section "Framework Selection Menu"

Wait for user selection.

### 2. Handle Initial Selection

**IF S (Save the Cat):**
- Confirm choice: "**You selected: Save the Cat**
{Brief confirmation of what this offers}
Is this correct? [Y] Yes / [N] No, let me reconsider"

**IF H (Hero's Journey):**
- Confirm choice: "**You selected: Hero's Journey**
{Brief confirmation of what this offers}
Is this correct? [Y] Yes / [N] No, let me reconsider"

**IF N (Snowflake Method):**
- Confirm choice: "**You selected: Snowflake Method**
{Brief confirmation of what this offers}
Is this correct? [Y] Yes / [N] No, let me reconsider"

**IF C (Custom Framework):**
- Proceed to Custom Framework Flow (see below)

**IF ? (Help/Explain More):**
- "What would you like to know more about?"
  - "[S] - More about Save the Cat"
  - "[H] - More about Hero's Journey"
  - "[N] - More about Snowflake Method"
  - "[C] - More about Custom Framework"
  - "[M] - Return to main menu"
- Provide requested information, then return to main menu

### 3. Handle Confirmation

**IF Y (Yes, confirmed):**
- Store selection as `{selected_framework}`
- Proceed to Step 4

**IF N (No, reconsider):**
- Return to main menu (Step 1)
- Allow new selection

### 4. Custom Framework Flow

Follow custom framework procedure from `{frameworkDefinitions}/references/framework-selection-procedures.md` - section "Step 4: Selection Procedure" → "Custom Framework Flow"

Load custom framework prompt from `{frameworkDefinitions}/references/framework-completion-message.md` - section "Custom Framework Prompt"

### 5. Final Confirmation

Before proceeding to configuration, confirm one final time:

"**✅ Selection Confirmed**

You've selected: **{selected_framework}**

{For standard frameworks: Brief reminder of what this provides}
{For custom: Brief summary of their approach}

**Ready to configure?**

**[C]** Yes, configure this framework
**[R]** No, I want to reconsider"

Wait for final confirmation.

**IF C:**
- Proceed to Step 6

**IF R:**
- Return to main menu (Step 1)

### 6. Update Output File

Update `{outputFile}`:

- Set `stepsCompleted: ['step-01-analyze', 'step-02-recommend', 'step-03-explain', 'step-04-select']`
- Set `lastStep: 'step-04-select'`
- Set `selectedFramework: {selected_framework}`

**IF custom:**
- Set `customFramework.description: {custom_description}`

### 7. Present Selection Summary

Display completion message from `{frameworkDefinitions}/references/framework-completion-message.md` - section "Step 4: Framework Selection Complete"

### MENU HANDLING LOGIC:

- IF C: Update {outputFile} frontmatter with selectedFramework, customFramework (if applicable), stepsCompleted, lastStep, then load, read entire file, then execute {nextStepFile}
- IF R: "No problem! Let's return to the selection menu." → Return to Step 1
- IF ?: "What questions do you have before we proceed?" → Answer, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Selection presented with clear menu
- Author made informed choice
- Selection confirmed (not assumed)
- Custom framework flow handled properly if selected
- Output file updated with selection
- Final confirmation obtained before proceeding

### ❌ SYSTEM FAILURE:
- Making selection for the author
- Proceeding without explicit confirmation
- Not handling custom framework properly
- Not updating output file
- Skipping confirmation steps

**Master Rule:** The author MUST make an explicit, confirmed choice. Never assume or proceed without clear confirmation. This is their story, their choice.
