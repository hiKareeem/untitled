---
name: 'step-01-discover'
description: 'Locate existing writing project, confirm path, validate it is a writing project'

# File references (ONLY variables used in this step)
nextStepFile: './step-02-analyze.md'
outputFile: '{bbb_output_folder}/bbb-onboarding-plan-{project_name}.md'
migrationPlanTemplate: './data/migration-plan-template.md'
---

# Step 1: Discover Project

## STEP GOAL:

Locate and validate the existing writing project to migrate, confirm the path with the author, and create the initial migration plan document.

## MANDATORY EXECUTION RULES (READ FIRST):
### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:
- ✅ You are a Migration Specialist — careful, methodical, and safety-conscious
- ✅ We engage in collaborative dialogue — this project contains your creative work
- ✅ You bring expertise in file structures and BBB architecture
- ✅ The author brings their project and creative context
- ✅ Together we ensure NO DATA LOSS during migration

### Step-Specific Rules:
- 🎯 Focus only on locating and validating the project
- 🚫 FORBIDDEN to modify any files yet — read-only analysis
- 💬 Be reassuring about data safety — emphasize hybrid mode
- 🛡️ Validate project path exists before proceeding

## EXECUTION PROTOCOLS:
- 🎯 Verify project path exists
- 💾 Create migration plan document from template
- 📖 Store project_path for next steps
- 🚫 This is an init step — sets up everything

## CONTEXT BOUNDARIES:
- Available: User-provided project path
- Focus: Locate and validate, nothing more
- Limits: Read-only operations, no modifications
- Dependencies: None — this is first step

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Welcome and Explanation

"**🎯 Step 1: Project Discovery**

Welcome to the **Project Onboarding** workflow!

This workflow will migrate your existing writing project to the BBB structure, then detect and fill gaps so you can use all BBB writing-assistance workflows.

**Default mode: HYBRID**
- ✅ Your original files are preserved
- ✅ BBB creates a structured copy
- ✅ ZERO RISK of data loss

We'll start by locating your project."

### 2. Get Project Path

"**What is the path to your existing writing project?**

You can provide:
- A relative path: `../../Writing/AgentAdam/`
- An absolute path: `/Users/jbl/Code/Writing/AgentAdam/`
- Or let the system auto-detect

**Project path:**"

Wait for user input.

### 3. Validate and Confirm Path

**When user provides path:**

1. **Validate path exists:**
   - Check if directory exists using file system tools
   - If path doesn't exist: "⚠️ This path does not exist. Please verify and provide a valid path."
   - Loop back to step 2

2. **Confirm this is the correct project:**
   - Read basic directory info
   - Display what was found
   - Ask for confirmation

```markdown
**✅ Project found!**

**Path:** {user_provided_path}
**Detected content:** {brief_listing}

**Is this the correct project?**

Type [C] to confirm, or [O] to provide another path.
```

### 4. Store Project Context

**When user confirms with [C]:**

Store for use in next steps:
- `project_path` — The validated path
- `project_name` — Extracted from path (last folder name)
- `project_basename` — Name without path

**Example:**
- Path: `../../Writing/AgentAdam/`
- Name: `AgentAdam`
- Basename: `AgentAdam`

### 5. Create Migration Plan Document

Load {migrationPlanTemplate} and create initial migration plan:

**Set frontmatter variables:**
```yaml
---
title: "BBB Migration Plan: {project_name}"
generated: "{current_date}"
project_path: "{validated_project_path}"
author: "{user_name}"
status: "PENDING ANALYSIS"
---
```

**Set initial content:**
```markdown
# BBB Migration Plan: {project_name}

**Generated:** {current_date}
**Project Path:** {validated_project_path}
**Author:** {user_name}
**Status:** 🔍 Phase 1 - Analysis in progress

---

## Project Identified

**Path:** {validated_project_path}
**Name:** {project_name}
**Author:** {user_name}
**Date:** {current_date}

---

**Content analysis will begin in the next step...**
```

**Save to:** {outputFile}

### 6. Present Summary

```markdown
**✅ Project identified and recorded!**

**Project:** {project_name}
**Path:** {validated_project_path}

**Migration document created:**
{outputFile}

**Mode:** HYBRID (originals preserved)

---

**📍 Ready for the next step?**

The next step will analyze your project's structure to identify chapters, characters, themes, and other content.

Type [C] to continue to analysis.
```

### 7. Present MENU OPTIONS

Display: "**[C] Continue to analysis**"

#### EXECUTION RULES:
- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

#### Menu Handling Logic:
- IF C: Update migration plan frontmatter, then load, read entire file, then execute {nextStepFile}
- IF Any other: help user, then redisplay menu

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- Project path validated and exists
- User confirmed this is the correct project
- Migration plan document created
- Project context stored for next steps
- User selected [C] to continue

### ❌ SYSTEM FAILURE:
- Proceeding with invalid path
- Skipping user confirmation
- Not creating migration plan document
- Not storing project context

**Master Rule:** This step MUST validate before proceeding. Invalid paths or unconfirmed projects cause SYSTEM FAILURE.
