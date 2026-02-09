# Chapter Write Execution Modes

## Overview

The Chapter Write workflow offers two execution modes to balance speed and quality assurance. Users choose between Quick Start (fast) and Full Review (thorough) during initialization.

---

## Mode Selection

Present this choice to the user after all required inputs are discovered and validated:

```
**All required inputs found!** ✅

How would you like to proceed?

**[Q] Quick Start** — Start writing immediately (recommended for experienced writers)
**[F] Full Review** — Complete pre-writing checklist for maximum quality assurance

**What's the difference?**
- **Quick Start**: Skip directly to chapter brief, start writing faster (~5 min)
- **Full Review**: Verify 22 pre-writing checkpoints for quality (~15 min)

**Select your preferred mode:** `[Q]` Quick Start or `[F]` Full Review
```

Wait for user selection. Store as `{execution_mode}` (values: 'quick', 'full').

---

## Mode 1: Quick Start

**Best for:** Experienced writers, subsequent chapters, when context is well-established

**Process:**
- Skip pre-writing checklist verification
- Proceed directly to step 6 (Create Output File)
- Then continue to step-02-brief

**Time savings:** ~10 minutes

**Quality assurance:**
- Relies on author's familiarity with context
- Assumes previous quality checks are still valid
- Recommended for chapters 2+ when first chapter was successful

**Status Display:**
```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ **Initialization complete — Quick Start mode**

All contexts are loaded. Ready for the chapter brief!

| Item | Value |
|------|-------|
| Chapter | {chapter_number} |
| Title | {chapter_title} |
| Target Words | 3000-6000 |
| Mode | Quick Start |
| Context Files | 7/7 loaded ✅ |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Mode 2: Full Review

**Best for:** First chapter, complex chapters, after major story changes, quality-critical work

**Process:**
- Complete step 5 (Load All Inputs)
- Execute step 5.5 (Pre-Writing Checklist with 22 verification points)
- Only proceed to brief after all checkpoints verified

**Time investment:** ~15 minutes

**Quality assurance:**
- Systematic verification of all context elements
- Identifies missing or incomplete information
- Prevents quality issues before writing begins
- Especially valuable for complex chapters with multiple characters

**Status Display:**
```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ **Initialization complete — Full Review**

All contexts are loaded. Comprehensive preparation complete!

| Item | Value |
|------|-------|
| Chapter | {chapter_number} |
| Title | {chapter_title} |
| Target Words | 3000-6000 |
| Mode | Full Review |
| Context Files | 7/7 loaded ✅ |
| Checkpoints | 22/22 verified ✅ |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Mode Comparison

| Aspect | Quick Start | Full Review |
|--------|-------------|-------------|
| **Time** | ~5 minutes | ~15 minutes |
| **Checkpoints** | 7 (input validation) | 22 (input + prep + quality) |
| **Best for** | Experienced writers, subsequent chapters | First chapter, complex scenes |
| **Risk** | Lower (assumes established quality) | Minimal (systematic verification) |
| **Recommendation** | Chapters 2+ | Chapter 1, critical scenes |

---

## Pre-Writing Checklist (Full Review Only)

The Full Review mode includes a comprehensive 22-point checklist across 4 categories:

### Category 1: Context Files Loaded (7 items)
- Chapter Plan
- Story Bible (all 5 dimensions)
- Character Dossiers
- Style Profile
- Previous Chapters
- Thematic Context
- Rhythm Guidelines

### Category 2: Chapter Brief Preparation (7 items)
- Chapter goal established
- Characters present identified
- Setting confirmed
- Scene-by-scene breakdown ready
- Key conflicts planned
- Thematic beats identified
- Transformation objectives set

### Category 3: Psychological Preparation (4 items)
- Each character's psychological state noted
- Which contradictions will be tested
- What blind spots may be relevant
- Arc progression tracked

### Category 4: Quality Thresholds (4 items)
- TTR target identified (> 0.175)
- Sentence length target (20-24 words average)
- Complexity target (80% complex/compound, 20% simple)
- Show vs Tell intentions

**Full checklist specification:** See `pre-writing-checklist.md`

---

## Completion Message (Both Modes)

After mode-specific processing, present:

```markdown
Ready to proceed to chapter brief?

**Select an option:** `[C]` Continue to Brief
```

## Menu Handling Logic

- **IF C:** Update {outputFile} frontmatter, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** Help user, then redisplay menu
