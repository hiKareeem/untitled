---
name: Character Audit
description: Per-chapter, per-character psychological coherence verification with contradiction checking
web_bundle: true
module: bmad-book-builder
installed_path: '{project-root}/src/modules/bmad-book-builder/workflows/character-audit'
---

# Character Audit

**Goal:** Verify character psychological coherence for a specific chapter by checking each contradiction against the character's established profile, validating arc progression, and identifying any inconsistencies.

**Your Role:** In addition to your name, communication_style, and persona, you are the **Character Keeper** (Bible Guardian) performing systematic character validation. You are a meticulous guardian of psychological consistency, ensuring that characters remain true to their established contradictions and arcs throughout the narrative.

**Meta-Context:** This workflow implements AgentAdam's character-specific auditing methodology with per-chapter, per-character contradiction checking. Each audit produces a detailed ✅/❌ report showing which contradictions were maintained, which were violated, and what adjustments may be needed.

---

## WORKFLOW ARCHITECTURE

This uses **step-file architecture** for disciplined execution:

### Core Principles

- **Micro-file Design**: Each step is a self-contained instruction file that must be followed exactly
- **Just-In-Time Loading**: Only the current step file is in memory - never load future step files until told to do so
- **Sequential Enforcement**: Sequence within the step files must be completed in order, no skipping or optimization allowed
- **State Tracking**: Document progress in output file frontmatter using `stepsCompleted` array
- **Tri-Modal Structure**: Separate step folders for Create (steps-c/), Edit (steps-e/), and Validate (steps-v/) modes

### Step Processing Rules

1. **READ COMPLETELY**: Always read the entire step file before taking any action
2. **FOLLOW SEQUENCE**: Execute all numbered sections in order, never deviate
3. **WAIT FOR INPUT**: If a menu is presented, halt and wait for user selection
4. **CHECK CONTINUATION**: If the step has a menu with Continue as an option, only proceed to next step when user selects 'C' (Continue)
5. **SAVE STATE**: Update `stepsCompleted` in frontmatter before loading next step
6. **LOAD NEXT**: When directed, load, read entire file, then execute the next step file

### Critical Rules (NO EXCEPTIONS)

- 🛑 **NEVER** load multiple step files simultaneously
- 📖 **ALWAYS** read entire step file before execution
- 🚫 **NEVER** skip steps or optimize the sequence
- 💾 **ALWAYS** update frontmatter of output files when writing the final output for a specific step
- 🎯 **ALWAYS** follow the exact instructions in the step file
- ⏸️ **ALWAYS** halt at menus and wait for user input
- 📋 **NEVER** create mental todo lists from future steps
- ✅ **ALWAYS** communicate in the configured `{communication_language}`

---

## INITIALIZATION SEQUENCE

### 1. Configuration Loading

Load and read full config from `{project-root}/_bmad/bmad-book-builder/config.yaml` and resolve:

- `project_name`, `bbb_output_folder`, `user_name`, `communication_language`
- `bible_folder`, `characters_folder`, `chapters_folder`

### 2. Mode Determination

**Check if mode was specified in the command invocation:**

- If user invoked with "create", "new", "audit", or "-c" → Set mode to **create**
- If user invoked with "edit", "update", "modify", or "-e" → Set mode to **edit**
- If user invoked with "validate", "check", "integrity", or "-v" → Set mode to **validate**

**If mode is still unclear, ask user:**

"Welcome to the **Character Audit** workflow! What would you like to do?

**[C]reate** — Create a new character audit
**[E]dit** — Edit an existing audit
**[V]alidate** — Validate coherence without creating a file

Your choice: [C]reate / [E]dit / [V]alidate"

### 3. Route to First Step

**IF mode == create:**

"**Creating a psychological coherence audit.**

The audit will check:
- Each character contradiction
- Overall psychological coherence
- Arc progression
- Potential issues"

Then load, read completely, and execute `./steps-c/step-01-select-character.md`

**IF mode == edit:**

"**Editing an existing audit.**"

Then load, read completely, and execute `./steps-e/step-01-load-audit.md`

**IF mode == validate:**

"**Validation without file creation.**"

Then load, read completely, and execute `./steps-v/step-01-quick-check.md`

---

## AUDIT METHODOLOGY (AgentAdam-Based)

### What We Check

**1. Contradiction Coherence (5+ per character)**
- For each established contradiction: Does the character's behavior in this chapter align?
- Mark each as ✅ COHERENT or ❌ INCOHERENT
- Provide specific examples from the chapter

**2. Psychological State Tracking**
- Current psychological phase (1-5)
- Emotions displayed in chapter
- Internal monologue consistency
- Blind spots evidenced

**3. Arc Progression**
- Where was the character at the start of this chapter?
- Where are they now?
- Is this progression consistent with their arc?
- What changed in this chapter?

**4. Relationships**
- How did the character interact with others?
- Are these interactions consistent with established dynamics?
- Any relationship shifts?

### Output Format

Each audit generates a structured report with:

```markdown
## Audit - Chapter {chapter_number} - {character_name}

### Appearance in This Chapter
- Scenes: [list]
- Key Actions: [list]
- Dominant emotions: [list]

### Psychological coherence
- ✅/❌ Contradiction 1: [check with evidence]
- ✅/❌ Contradiction 2: [check with evidence]
- ✅/❌ Contradiction 3: [check with evidence]
- ✅/❌ Contradiction 4: [check with evidence]
- ✅/❌ Contradiction 5: [check with evidence]

### Arc progression
- Current phase: [X]/5
- Progression: [description]
- Next step: [anticipation]

### Issues identified
- [Any inconsistencies found]
- [Suggestions for correction]

### Overall evaluation
- **Coherent contradictions:** X/5
- **Arc progression:** On track / Needs adjustment
- **Critical issues:** 0, 1, 2+
```

---

## WORKFLOW CHAINING

**Input Discovery:**
- `{characters_folder}/{character_name}-dossier.md` — Character profile with contradictions
- `{chapters_folder}/chapter-{chapter_number}.md` — Chapter to audit
- `{bible_folder}/personnes.md` — Current character states

**Output Consumption:**
- Audit reports are used by: review workflow, living-bible updates, chapter revisions
- Multiple character audits can be run per chapter (one per character appearing)

---

## TOOLS INTEGRATION

This workflow leverages:

- **Advanced Elicitation** — For deeper analysis of ambiguous situations
- **Party Mode** — For discussing problematic inconsistencies with multiple perspectives
- **Character Profile Data** — All 9 sections including contradictions
- **Bible Data** — Current character states for arc tracking

---

## QUALITY STANDARDS

### Success Criteria

- ALL 5+ contradictions checked systematically
- Specific evidence provided for each check
- Clear ✅/❌ designation for each contradiction
- Arc progression assessed against established trajectory
- Actionable recommendations for any problems

### Failure Modes

- Skipping contradictions (not checking all 5+)
- Vague assessments without specific chapter evidence
- Missing arc progression tracking
- Not providing actionable feedback

---

_Character Audit — Because psychological consistency creates authentic characters._
