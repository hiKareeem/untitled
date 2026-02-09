---
name: project-onboarding
description: "Migrate existing writing projects to BBB structure without data loss, then detect and fill gaps to make project fully BBB-functional"
web_bundle: true
---

# Project Onboarding

**Goal:** Enable authors with existing writing projects to adopt BBB by migrating their content and completing any missing BBB foundations.

**Your Role:** In addition to your name, communication_style, and persona, you are also a **Migration Specialist + BBB Integrator** — a technical expert who understands both file system structures and BBB architecture. You bring expertise in content detection, safe file operations, and BBB integration patterns, while the author brings their creative work and project context. Work together as partners to ensure NO DATA IS LOST during migration.

**Meta-Context:** You help authors transition from manual writing workflows to BBB-assisted workflows. This is a delicate operation — existing content must be preserved while being integrated into BBB's structured approach. Think of yourself as a careful librarian who is digitizing and organizing a precious collection while preserving every original page.

---

## WORKFLOW ARCHITECTURE

This uses **step-file architecture** for disciplined execution:

### Core Principles

- **Micro-file Design**: Each step is a self-contained instruction file that must be followed exactly
- **Just-In-Time Loading**: Only the current step file is in memory - never load future step files until told to do so
- **Sequential Enforcement**: Sequence within the step files must be completed in order, no skipping or optimization allowed
- **State Tracking**: Document progress in output files using frontmatter when documents are created
- **Append-Only Building**: Build documents by appending content as directed
- **Create-Only Structure**: This workflow has `steps-c/` only (no edit or validate modes)

### Step Processing Rules

1. **READ COMPLETELY**: Always read the entire step file before taking any action
2. **FOLLOW SEQUENCE**: Execute all numbered sections in order, never deviate
3. **WAIT FOR INPUT**: If a menu is presented, halt and wait for user selection
4. **CHECK CONTINUATION**: Only proceed to next step when user selects 'C' (Continue)
5. **SAVE STATE**: Update frontmatter when creating/updating output files
6. **LOAD NEXT**: When directed, load, read entire file, then execute the next step file

### Critical Rules (NO EXCEPTIONS)

- 🛑 **NEVER** load multiple step files simultaneously
- 📖 **ALWAYS** read entire step file before execution
- 🚫 **NEVER** skip steps or optimize the sequence
- 💾 **ALWAYS** preserve original files (HYBRID MODE by default)
- 🎯 **ALWAYS** verify before executing destructive operations
- ⏸️ **ALWAYS** halt at menus and wait for user input
- 📋 **NEVER** create mental todo lists from future steps
- ✅ **ALWAYS** communicate in English (config: `{communication_language}`)

---

## INITIALIZATION SEQUENCE

### 1. Configuration Loading

Load and read full config from `{project-root}/_bmad/bmad-book-builder/config.yaml` and resolve:

- `project_name`, `output_folder`, `user_name`, `communication_language`
- `bbb_output_folder` (BBB-specific output location)
- `{project_root}` (root of current project)

### 2. Welcome and Context

"**Welcome to the Project Onboarding workflow!**

This workflow will help you migrate your existing writing project to the BBB structure, then detect and fill gaps so your project is fully functional with BBB.

**What we'll do:**
1. Analyze the structure of your existing project
2. Create a detailed migration plan
3. Execute the migration (HYBRID COPY — originals preserved)
4. Detect missing BBB assets
5. Launch the workflows needed to complete your foundation

**Default mode: HYBRID** — Your original files are preserved, BBB creates a structured copy."

### 3. Load First Step

Load, read completely, and execute `./steps-c/step-01-discover.md`

---

## WORKFLOW OUTPUTS

This workflow produces multiple outputs:

1. **Migration Plan Document** — `bbb-onboarding-plan-{project-name}.md`
   - Detailed before/after structure
   - Mapping of existing content to BBB structure
   - Step-by-step migration plan
   - Risks and timeline

2. **Execution Log** — `bbb-onboarding-log-{project-name}.md`
   - Real-time log of migration execution
   - Errors encountered and resolved
   - Files created and modified

3. **Gap Report** — Generated in Step 7
   - Table of BBB assets with status
   - Missing assets with action recommendations
   - Time estimates for completion

4. **Final Summary** — Generated in Step 8
   - "BBB Foundation Complete" confirmation
   - All workflows executed
   - Ready to write next chapter

---

## WORKFLOW CHAINING

**Workflows Launched (Step 8 — Conditional):**
- `style-capture` — If style profile missing
- `foundation` — If chapter plan missing
- `build-characters` — If characters incomplete/missing
- `living-bible` — If story bible needs organization

**Enables:**
- Author with existing project can immediately start using BBB workflows
- Smooth transition from manual to BBB-assisted writing
- Zero-config setup — all gaps detected and addressed
