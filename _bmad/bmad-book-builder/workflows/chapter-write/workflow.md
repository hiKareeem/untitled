---
name: chapter-write
description: Write complete chapters in author's authentic voice with multi-agent review
web_bundle: true
module: bmad-book-builder
installed_path: '{project-root}/src/modules/bmad-book-builder/workflows/chapter-write'
---

# Chapter Write

**Goal:** Write a complete chapter (3000-6000 words) in the author's authentic voice, maintaining continuity with previous chapters and adhering to the story bible.

**Your Role:** In addition to your name, communication_style, and persona, you are also a **Chapter Writer** collaborating with authors. This is a partnership, not a client-vendor relationship. You bring expertise in narrative craft, voice matching, and continuity management, while the author brings their creative vision and story knowledge. Work together as equals.

## WORKFLOW ARCHITECTURE

### Core Principles

- **Micro-file Design**: Each step of the overall goal is a self contained instruction file that you will adhere to 1 file at a time
- **Just-In-Time Loading**: Only 1 current step file will be loaded, read, and executed to completion - never load future step files until told to do so
- **Sequential Enforcement**: Sequence within the step files must be completed in order, no skipping or optimization allowed
- **State Tracking**: Document progress in output file frontmatter using `stepsCompleted` array
- **Append-Only Building**: Build documents by appending content as directed to the output file
- **Multi-Agent Review**: Leverage specialized BBB agents for comprehensive chapter validation

### Step Processing Rules

1. **READ COMPLETELY**: Always read the entire step file before taking any action
2. **FOLLOW SEQUENCE**: Execute all numbered sections in order, never deviate
3. **WAIT FOR INPUT**: If a menu is presented, halt and wait for user selection
4. **CHECK CONTINUATION**: If the step has a menu with Continue as an option, only proceed to next step when user selects 'C' (Continue)
5. **SAVE STATE**: Update `stepsCompleted` in frontmatter before loading next step
6. **LOAD NEXT**: When directed, load, read entire file, then execute the next step file

### Critical Rules (NO EXCEPTIONS)

- NEVER load multiple step files simultaneously
- ALWAYS read entire step file before execution
- NEVER skip steps or optimize the sequence
- ALWAYS update frontmatter of output files when writing the final output for a specific step
- ALWAYS follow the exact instructions in the step file
- ALWAYS halt at menus and wait for user input
- NEVER create mental todo lists from future steps
- If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

---

## TRI-MODAL ROUTING

This workflow supports three modes:

### Create Mode (Default)
Write a new chapter from scratch using the chapter plan and all required inputs.

**Invoke:** Run workflow normally or with `-c` flag
**Entry:** `./steps-c/step-01-init.md`

### Edit Mode
Modify an existing chapter with targeted changes.

**Invoke:** Run workflow with `-e` flag
**Entry:** `./steps-e/step-01-load.md`

### Validate Mode
Validate an existing chapter against quality criteria without modification.

**Invoke:** Run workflow with `-v` flag
**Entry:** `./steps-v/step-01-validate.md`

---

## INITIALIZATION SEQUENCE

### 1. Module Configuration Loading

Load and read full config from {project-root}/_bmad/bmad-book-builder/config.yaml and resolve:

- `project_name`, `bbb_output_folder`, `user_name`, `communication_language`, `document_output_language`
- `bible_folder`, `style_profile_path`, `chapters_folder`

### 2. Mode Detection and Routing

**Check invocation mode:**

- IF `-e` or `--edit` flag present:
  → Load, read full file, then execute `./steps-e/step-01-load.md`

- IF `-v` or `--validate` flag present:
  → Load, read full file, then execute `./steps-v/step-01-validate.md`

- ELSE (default = Create mode):
  → Load, read full file, then execute `./steps-c/step-01-init.md`
