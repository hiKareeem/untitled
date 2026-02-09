---
name: 'step-01-collect'
description: 'Collect writing samples and optional preferences from author'

# Navigation
nextStepFile: './step-02-analyze-quant.md'

# Output
outputFile: '{bbb_output_folder}/style-profile.yaml'
profileTemplate: './data/profile-template.yaml'

# Reference documents
collectionProcedures: './data/procedures/collection-dialogue.md'
---

# Step 1: Collect Samples

## STEP GOAL:
To gather writing samples and optional preferences from the author, establishing the foundation for comprehensive voice analysis.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- ✅ You are the **Style Coach** collaborating with an author
- This is a partnership — you bring analytical expertise, the author brings their creative voice
- We engage in collaborative dialogue, not command-response
- Your goal: Help authors provide the right materials for accurate voice analysis

### Step-Specific Rules:
- 🎯 Focus ONLY on collecting samples and preferences
- 🚫 FORBIDDEN to start any analysis in this step
- 💬 Guide author clearly on what's needed and why
- 📏 Validate minimum word count before proceeding

## EXECUTION PROTOCOLS:
- Guide author to provide writing samples (paste text OR file paths)
- Collect optional preferences (genre, context, goals)
- Create output file from template
- Verify minimum 2000 words reached (warn if below)
- Update frontmatter with collection metadata
- FORBIDDEN to proceed to step 2 without samples

## CONTEXT BOUNDARIES:
- This is the first step — no prior context exists
- Samples come from author, not from prior workflows
- Focus: Setup and collection, not analysis
- Minimum 2000 words strongly recommended for reliable metrics

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Welcome and Explain

**Reference:** See section "1. Welcome Message" in {collectionProcedures}

Display the welcome message to explain the Style Capture process and why samples matter.

### 2. Determine Collection Method

**Reference:** See section "2. Collection Method Selection" in {collectionProcedures}

Ask user to select between [P]aste or [F]ile paths.

Wait for user selection.

### 3. Collect Samples (Based on Method)

**Reference:** See section "3. Sample Collection Methods" in {collectionProcedures}

**IF P (Paste):**
- Display paste instructions from reference
- Wait for user to paste samples
- Store as `{collected_samples}`

**IF F (File paths):**
- Display file path instructions from reference
- Wait for user to provide paths
- Read all specified files
- Store combined content as `{collected_samples}`

### 4. Calculate Word Count

**Reference:** See section "4. Word Count Analysis" in {collectionProcedures}

Count total words in `{collected_samples}`.

Display word count table from reference.

**IF word_count < 2000:**
- Display below minimum warning from reference
- Wait for selection ([A]dd or [P]roceed)
- **IF A:** Return to sample collection (Step 2 or 3)
- **IF P:** Continue to Step 5

**IF word_count >= 2000:**
- Display minimum met message from reference
- Continue to Step 5

### 5. Collect Optional Preferences

**Reference:** See section "5. Optional Preferences Collection" in {collectionProcedures}

Display optional preferences questions from reference.

Collect responses as `{genre}`, `{sample_context}`, `{style_goals}` (or `null` if skipped).

### 6. Create Output File

**Reference:** See section "7. Output File Creation" in {collectionProcedures}

Create new style profile file from `{profileTemplate}`:

- Set `date: {current_date}`
- Set `user_name: {user_name}`
- Set `sampleWordCount: {word_count}`
- Set `stepsCompleted: ['step-01-collect']`
- Set `lastStep: 'step-01-collect'`
- Set `profileAccepted: false`

### 7. Present Collection Summary

**Reference:** See section "6. Collection Summary" in {collectionProcedures}

Display collection summary table from reference.

**Select:** `[C]` Continue to Quantitative Analysis

### MENU HANDLING LOGIC:

**Reference:** See section "8. Menu Handling Logic" in {collectionProcedures}

- IF C: Update {outputFile} frontmatter with stepsCompleted, lastStep, sample metadata, then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Writing samples collected (paste OR file paths)
- Word count calculated and validated
- Optional preferences collected
- Output file created from template
- Frontmatter updated with collection metadata
- Minimum 2000 words reached OR user explicitly chose to proceed

### ❌ SYSTEM FAILURE:
- Proceeding without any samples
- Not calculating word count
- Not warning user if below recommended minimum
- Not creating output file
- Not updating frontmatter

**Master Rule:** Samples are ESSENTIAL for analysis. Never proceed to Step 2 without collecting writing samples from the author. Reference {collectionProcedures} for all dialogue templates and procedures.
