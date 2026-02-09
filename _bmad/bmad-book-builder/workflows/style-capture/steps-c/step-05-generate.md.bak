---
name: 'step-05-generate'
description: 'Generate comprehensive style profile in YAML format'

# Navigation
nextStepFile: './step-06-review.md'

# Output files
outputFile: '{bbb_output_folder}/style-profile.yaml'
profileTemplate: './data/profile-template.yaml'

# Data sources (from previous steps)
quantitativeMetrics: '{quantitative_metrics}'
qualitativePatterns: '{qualitative_patterns}'
antiPatterns: '{anti_patterns}'
metadata: '{date}, {user_name}, {sample_count}, {word_count}'
optionalInputs: '{genre}, {sample_context}, {style_goals}'

# Reference documents
templatesReference: './data/templates/style-profile-templates.yaml'
---

# Step 5: Generate Style Profile

## STEP GOAL:
To compile all quantitative metrics, qualitative patterns, and anti-patterns into a comprehensive YAML style profile for use by Chapter-Write and Review workflows.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- ✅ You are the **Style Coach** compiling the comprehensive style profile
- This step requires precise YAML formatting
- Your goal: Create a structured, consumable profile for other workflows
- Follow the exact template structure — no improvisation

### Step-Specific Rules:
- 🎯 Follow the {templatesReference} structure EXACTLY
- 🚫 FORBIDDEN to deviate from the template format
- 📝 Prescriptive instructions — exact structure required
- ✅ Validate YAML syntax before saving
- 💾 Output file will be consumed by Chapter-Write and Review workflows

## EXECUTION PROTOCOLS:
- Load the profile template
- Populate all sections with data from previous steps
- Add recommendations section based on findings
- Add additional-insights section if applicable (temporal tracking, genre context)
- Validate YAML before saving
- Display summary and auto-proceed to review

## CONTEXT BOUNDARIES:
- This step runs autonomously — no user interaction required
- Input: All data from steps 02-04
- Output: Complete style-profile.yaml file
- Focus: Precise YAML structure for workflow consumption
- Dependencies: Steps 01-04 must be complete
- Reference: {templatesReference} for complete structure

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Initialize Profile Generation

Display: "**📝 Generating Style Profile...**"

### 2. Load Template and Structure

**Reference:** See "Complete Profile Template" and "Complete File Structure" sections in {templatesReference}

Load {profileTemplate} to understand the exact structure.

The structure MUST follow the format specified in {templatesReference}.

### 3. Populate Frontmatter

**Reference:** See "Frontmatter Section" in {templatesReference}

Create/update frontmatter section following the exact template.

```yaml
---
stepsCompleted: ['step-01-collect', 'step-02-analyze-quant', 'step-03-analyze-qual', 'step-04-detect-antipatterns', 'step-05-generate']
lastStep: 'step-05-generate'
date: {current_date}
user_name: {user_name}
sampleWordCount: {word_count}
profileAccepted: false
---
```

### 4. Populate Header Section

**Reference:** See "Header Section" in {templatesReference}

Follow template format exactly.

Add optional metadata if provided:
- **Genre:** {genre} (if provided)
- **Sample Context:** {sample_context} (if provided)
- **Style Goals:** {style_goals} (if provided)

### 5. Populate Quantitative Metrics Section

**Reference:** See "Quantitative Metrics Template" in {templatesReference}

Use data from {quantitative_metrics} (step 02): TTR, Sentence Length, Complexity Ratio, Paragraph Variation. Follow exact template format.

### 6. Populate Qualitative Patterns Section

**Reference:** See "Qualitative Patterns Template" in {templatesReference}

Use data from {qualitative_patterns} (step 03): Favorite Words, Characteristic Phrases, Imagery Themes, Transition Patterns. Include validation note.

### 7. Populate Anti-Patterns Section

**Reference:** See "Anti-Patterns Template" in {templatesReference}

Use data from {anti_patterns} (step 04): Excessive Adverbs, Passive Voice, Cliches, Generic Dialogue, Slop Patterns. Use appropriate template for each category. Include Humanizer reference.

### 8. Generate Recommendations Section

**Reference:** See "Recommendations Template" in {templatesReference}

Create recommendations: Style Preservation (summarize 3-5 voice characteristics, use templates), Quality Improvements (list 3-5 from anti-pattern findings, use priority templates)

### 9. Add Additional Insights (Conditional)

**Reference:** See "Additional Insights Template" in {templatesReference}

**IF genre provided:** Add genre-context analysis. **IF samples span time periods:** Add temporal tracking. **IF neither:** Omit section.

### 10. Validate YAML Syntax

**Reference:** See "Usage Notes" in {templatesReference}

Before saving, validate:

**Check:**
- YAML frontmatter is properly formatted
- All `{placeholders}` have been replaced with actual data
- List items are properly indented
- No unclosed quotes or brackets
- No markdown syntax conflicts with YAML

**Fix any errors before proceeding.**

### 11. Write Profile File

Write the complete YAML document to {outputFile}.

**CRITICAL:** This is the consumable output for Chapter-Write and Review workflows.

### 12. Display Generation Summary

Display:

"**📝 Style Profile Generated**

**Location:** {outputFile}

**Profile Contents:**
- Quantitative Metrics: TTR, sentence length, complexity, paragraph variation
- Qualitative Patterns: {count} favorite words, {count} phrases, {count} imagery themes, {count} transitions
- Anti-Patterns: Adverb patterns, passive voice, cliches, dialogue issues, slop
- Recommendations: Style preservation guidance and quality improvements

**Next:** Author review step — validate examples and accept profile.

**Important:** You will review all examples in the next step and can remove any that don't feel representative of your voice."

### 13. Auto-Proceed to Review

Display: "**Proceeding to Author Review...**"

#### Menu Handling Logic:
- After displaying summary, immediately load, read entire file, then execute {nextStepFile}

#### EXECUTION RULES:
- This is a prescriptive generation step with no user choices
- Proceed directly to review step after profile complete

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Profile template structure followed EXACTLY (per {templatesReference})
- All sections populated with data from previous steps
- YAML syntax validated before saving
- File written successfully to {outputFile}
- Frontmatter properly updated
- Summary displayed to user
- Proceeded to step 06 without error

### ❌ SYSTEM FAILURE:
- Deviating from template structure
- Leaving placeholders unfilled
- YAML syntax errors in output file
- Not validating before saving
- Not writing to correct output path
- Missing sections or data

**Master Rule:** The style profile is the consumable output for other workflows. Precise YAML structure is CRITICAL. Any deviation breaks workflow integration. Reference {templatesReference} for exact structure.
