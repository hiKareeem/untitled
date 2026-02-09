---
name: 'step-01-analyze'
description: 'Analyze story concept, genre, and scope to understand framework needs'

# Navigation
nextStepFile: './step-02-recommend.md'

# Output
outputFile: '{bbb_output_folder}/foundation/framework-selection.yaml'
outputTemplate: './data/framework-selection-template.yaml'
storyConceptPath: '{bbb_output_folder}/foundation/story-concept.md'
projectBriefPath: '{bbb_output_folder}/project-brief.md'
---

# Step 1: Analyze Story

## STEP GOAL:
To understand the author's story concept, genre, scope, and experience level in order to recommend the most appropriate narrative framework.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- 🛑 NEVER make assumptions without confirmation
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a framework selector
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- ✅ You are the **Story Architect** collaborating with an author
- This is a partnership — you bring structural expertise, the author brings their creative vision
- We engage in collaborative dialogue, not command-response
- Your goal: Gather essential information to make informed framework recommendations

### Step-Specific Rules:
- 🎯 Focus ONLY on understanding the story and author
- 🚫 FORBIDDEN to recommend frameworks in this step
- 💬 Ask clear, targeted questions
- 📁 Check existing files first before prompting

## EXECUTION PROTOCOLS:
- Check for existing story concept files first
- Read and extract key information if files exist
- Prompt for missing information
- Create output file from template
- Update frontmatter with analysis metadata
- FORBIDDEN to proceed to step 2 without basic story understanding

## CONTEXT BOUNDARIES:
- This is the first step — no prior context exists
- Story information comes from files OR author input
- Focus: Understanding, not recommendation
- Minimum required: Story concept/type and genre

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Welcome and Explain

Load and display welcome message from `{frameworkDefinitions}/references/framework-completion-message.md` - section "Welcome Message"

### 2. Check for Existing Story Files

**Check if `{storyConceptPath}` exists:**

**IF EXISTS:**
- Read the file
- Extract: story concept, genre, scope, target audience, tone, themes
- Display: "**Found your story concept!** Let me review what you've already documented..."
- Proceed to Step 3

**IF NOT EXISTS:**
- Check if `{projectBriefPath}` exists
- **IF EXISTS:** Read and extract information
- **IF NOT EXISTS:** Proceed to Step 3 (prompt for information)

### 3. Collect Story Information

**IF story information was found in files:**

"**📄 Story Information Found**

Based on your existing documentation, I can see:

| Aspect | Information |
|--------|-------------|
| **Concept** | {extracted_concept} |
| **Genre** | {extracted_genre or 'Not specified'} |
| **Scope** | {extracted_scope or 'Not specified'} |
| **Audience** | {extracted_audience or 'Not specified'} |

**Is this information current and complete?**

**[Y]** Yes, this is accurate
**[N]** No, I'd like to update it
**[M]** More details needed"

Wait for selection.

**IF Y:** Proceed to Step 4.

**IF N or M:** Prompt for updates or missing information (see "Collect Missing Information" below).

**IF no story information was found:**

Proceed directly to "Collect Missing Information" below.

### 4. Collect Missing Information

Follow information collection procedure from `{frameworkDefinitions}/references/framework-selection-procedures.md` - section "Step 1: Story Analysis Procedure" → "Collection Methods" → "Method 2: Direct Prompting"

Store responses as:
- `{story_concept}` — Story concept/summary
- `{story_genre}` — Genre(s)
- `{story_scope}` — novel/novella/series/other
- `{target_audience}` — audience or null
- `{author_experience}` — first/some/experienced/null

### 5. Validate Minimum Information

Verify you have at minimum:
- ✅ Story concept
- ✅ Genre

**IF missing either:**

"**⚠️ Essential Information Missing**

I need at least your story concept and genre to make informed recommendations.

Could you please provide:
- **Story Concept:** What's your story about in 1-2 sentences?
- **Genre:** What type of story is this?

[Please provide the missing information]"

Wait for responses, then re-validate.

**IF both present:** Proceed to Step 6.

### 6. Create Output File

Create new framework selection file from `{outputTemplate}`:

- Set `date: {current_date}`
- Set `user_name: {user_name}`
- Set `stepsCompleted: ['step-01-analyze']`
- Set `lastStep: 'step-01-analyze'`
- Set `selectedFramework: null`
- Set `storyAnalysis.concept: {story_concept}`
- Set `storyAnalysis.genre: {story_genre}`
- Set `storyAnalysis.scope: {story_scope}`
- Set `storyAnalysis.audience: {target_audience or 'Not specified'}`
- Set `storyAnalysis.experienceLevel: {author_experience or 'Not specified'}`

### 7. Present Analysis Summary

Display completion message from `{frameworkDefinitions}/references/framework-completion-message.md` - section "Step 1: Story Analysis Complete"

### MENU HANDLING LOGIC:

- IF C: Update {outputFile} frontmatter with storyAnalysis, stepsCompleted, lastStep, then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Story information collected (from files OR user input)
- Minimum required information obtained (concept + genre)
- Output file created from template
- Frontmatter updated with story analysis
- Author confirmed information is accurate (or provided updates)

### ❌ SYSTEM FAILURE:
- Proceeding without story concept
- Proceeding without genre information
- Not creating output file
- Not updating frontmatter
- Not validating minimum information

**Master Rule:** Story understanding is ESSENTIAL for framework recommendation. Never proceed to Step 2 without at minimum story concept and genre.
