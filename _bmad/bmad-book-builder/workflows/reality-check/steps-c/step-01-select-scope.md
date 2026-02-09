---
name: 'step-01-select-scope'
description: 'Select scope for reality check verification'

# Navigation
nextStepFile: './step-02-extract-claims.md'

# Output
outputFile: '{bbb_output_folder}/reality-check/chapter-{scope}-report.md'
bbb_output_folder: '{output_folder}'
chaptersFolder: '{bbb_output_folder}/chapters/'
researchFolder: '{bbb_output_folder}/research/dossiers/'
---

# Step 1: Select Scope

## STEP GOAL:
To determine the scope of the reality check — what content will be verified for factual and technical accuracy.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Documentaliste** beginning a reality check verification
- Like a fact-checker clarifying what needs verification, you establish clear scope
- Proper scope selection ensures thorough, efficient fact-checking
- You guide the author to select the appropriate verification scope

### Step-Specific Rules:
- ALWAYS present the scope selection menu
- FORBIDDEN to proceed without clear scope definition
- Validate scope input and ask for clarification if needed
- Store scope information for use in subsequent steps

## EXECUTION PROTOCOLS:
- Present scope selection menu with clear options
- Collect scope details (chapter number, scene range, element description)
- Validate that content exists for the selected scope
- Initialize output file with scope information
- Wait for user confirmation before proceeding

## CONTEXT BOUNDARIES:
- Has access to `bbb_output_folder` and all subfolder paths from workflow initialization
- Chapter files are read from `chaptersFolder`
- Research dossiers will be accessed from `researchFolder` in later steps
- Output file will be created with scope identifier

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Reality Check Start

"**🔍 Reality Check Verification — Starting**

Let me help you verify the factual and technical accuracy in your story. I'll check for anachronisms, technical errors, factual inconsistencies, and unrealistic details — then provide corrections and build research dossiers for future reference.

First, let's establish what we'll be fact-checking."

### 2. Scan Available Chapters

Scan `{chaptersFolder}` for available chapter files:

**Search for chapter files:**
- Look for: `chapter-{N}.md` pattern
- Collect: Chapter numbers and titles
- Store as: `available_chapters` array

After scanning:
"✅ **Chapters Available:** {list of chapters found}"

**IF no chapters found:**
"⚠️ **No chapters found.** Please write at least one chapter before running a reality check.
You can write chapters using the Chapter Write workflow."

**HALT and suggest running chapter-write workflow first.**

### 3. Present Scope Selection Menu

Display the scope selection menu:

```markdown
## What would you like to fact-check?

  **[C]hapter** — Full chapter verification
  Verify all claims in a single chapter. Most comprehensive option.

  **[S]cene** — Specific scene range
  Focus on particular scenes (e.g., "Chapter 5, scenes 2-4"). Good for targeting technical scenes.

  **[E]lement** — Specific element to verify
  Verify specific topics across chapters (e.g., "medical procedures in Chapter 12"). Good for focused checks.

  **[A]ll Written** — All completed chapters
  Comprehensive reality check across your entire manuscript. Best for pre-publication review.

Your choice: _
```

### 4. Process Scope Selection

Wait for user input. Process based on selection:

#### **[C] CHAPTER - Full Chapter Verification**
Prompt: "Which chapter would you like to verify? Enter chapter number: "

**Validation:**
- Check if chapter exists in `available_chapters`
- IF valid: Store scope as `chapter-{N}`, load chapter file for confirmation
- IF invalid: "⚠️ Chapter {N} not found. Available chapters: {list}. Please enter a valid chapter number."

**After valid selection:**
"✅ **Scope Selected:** Chapter {N} — Full chapter verification
Chapter title: {title}
Word count: {count}

I'll verify all factual and technical claims in this chapter."

#### **[S] SCENE - Specific Scene Range**
Prompt: "Which chapter and scenes? Enter format: 'chapter {N}, scenes {X}-{Y}' or 'chapter {N}, scene {X}'"

**Examples:** "chapter 5, scenes 2-4" → Verify scenes 2, 3, and 4 in chapter 5

**Validation:**
- Extract chapter number and scene range
- Check if chapter exists
- IF valid: Store scope as `chapter-{N}-scenes-{X}-{Y}`, load chapter file to confirm scene boundaries
- IF invalid: "⚠️ Invalid format or chapter not found. Please use the format 'chapter {N}, scenes {X}-{Y}'"

**After valid selection:**
"✅ **Scope Selected:** Chapter {N}, Scene(s) {X}-{Y}
Chapter title: {title}
Scene range: {description}

I'll verify claims within these specific scenes."

#### **[E] ELEMENT - Specific Element**
Prompt: "Which element would you like to verify? Describe the specific element, chapter, and topic."

**Analysis:**
- Parse description to identify: target chapters, topic/theme, specific claims to verify

**Prompt for clarification if needed:**
"I understand you want to verify '{element}'. Let me confirm:
- **Chapters:** {list or 'all mentioned'}
- **Focus:** {topic/theme}
- **Specific claims:** {identified claims or 'will scan for relevant claims'}

Is this correct? [Y]es / [N]o — provide different description"

**After confirmation:**
"✅ **Scope Selected:** Element Verification
Topic: {element}
Chapters: {list}
Focus: {description}

I'll scan the specified chapters for claims related to this topic."

#### **[A] ALL WRITTEN - All Completed Chapters**
**Validation:**
- Count chapters with complete status
- IF no complete chapters: "⚠️ No completed chapters found. Only chapters with 'complete' status will be verified."

**IF complete chapters exist:**
"✅ **Scope Selected:** All Completed Chapters
Chapters to verify: {count}
List: {chapter numbers}

This will be a comprehensive reality check across your entire manuscript."

### 5. Create Output Directory and Initialize File

**Create directory:**
Check if `{bbb_output_folder}/reality-check/` exists:
- IF EXISTS: Proceed
- IF NOT EXISTS: Create directory

**Initialize output file:**
Create initial output file at `{outputFile}` with frontmatter (see `data/templates/reality-check-templates.yaml` for output file structure):

```yaml
---
stepsCompleted: ['step-01-select-scope']
lastStep: 'step-01-select-scope'
date: '{current_date}'
user_name: '{user_name}'
scope: '{scope_identifier}'
scopeType: '{chapter|scene|element|all}'
targetChapters: [{list}]
verificationStatus: 'in-progress'
---
```

Add initial header and scope section (see template for full structure).

### 6. Present Scope Confirmation and Proceed

Display:

"**✅ Scope Confirmed**

Reality check will verify:
- **Scope:** {scope description}
- **Chapters:** {list}
- **Estimated claims:** {estimate based on scope size}

I'll now extract factual and technical claims from the specified content, then verify them against research dossiers and web sources.

**Select:** `[C]` Continue to Claim Extraction"

### MENU HANDLING LOGIC:

- IF C: Update {outputFile} frontmatter with stepsCompleted: ['step-01-select-scope', 'step-02-extract-claims'], lastStep: 'step-02-extract-claims', then load, read entire file, then execute {nextStepFile}
- IF Any other input: Treat as scope change request — return to scope selection menu

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Scope selection menu presented clearly
- User input collected and validated
- Target chapters identified and confirmed to exist
- Output directory created
- Output file initialized with scope information in frontmatter
- User confirms scope and proceeds to next step

### SYSTEM FAILURE:
- Not presenting scope selection menu
- Proceeding without clear scope definition
- Not validating that target content exists
- Not initializing output file properly
- Not storing scope information for subsequent steps

**Master Rule:** Clear scope definition is the foundation of effective reality checking. The verification quality depends on understanding exactly what content is being checked. Never proceed without explicit scope confirmation.
