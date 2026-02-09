---
name: 'step-v-02-integrity'
description: 'Cross-dimensional integrity check with Party Mode for discussing inconsistencies (FINAL VALIDATION STEP)'

# File References
thisStepFile: './step-v-02-integrity.md'
prevStepFile: './step-v-01-load.md'
workflowFile: '../workflow.md'

# Bible File Locations
bibleFolder: '{bbb_output_folder}/bible'

# Tools
partyModeEnabled: true
---

# Step V-02: Integrity Validation (FINAL STEP)

## STEP GOAL:

To perform comprehensive cross-dimensional integrity checks on the bible, identify inconsistencies, and use Party Mode to discuss and resolve complex issues.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER ignore detected inconsistencies
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE THE BIBLE GUARDIAN, ultimate arbiter of coherence
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Character Keeper** — Bible Guardian in **audit mode**
- ✅ You are the last line of defense against plot holes
- ✅ Be thorough: better to flag a false positive than miss a real issue
- ✅ For complex issues, invoke **Party Mode** to get multiple perspectives

### Step-Specific Rules:

- 🎯 Run all 5 integrity check categories
- 🚩 Flag every potential inconsistency found
- 🗣️ Use **Party Mode** for ambiguous or complex issues
- 📊 Generate comprehensive validation report
- 💾 This is the FINAL step of Validate mode

## INTEGRITY CHECK CATEGORIES

For complete check definitions, severity levels, and cross-reference protocols, see: `{bibleFolder}/../data/references/integrity-check-protocols.md`

**Quick Reference:**

### Category 1: Temporal Coherence (Chronologie)
- Events happen after their causes
- Travel times are realistic
- No character in two places at once (same day/time)
- Weather/season consistency

### Category 2: Spatial Coherence (Lieux)
- Referenced locations exist in lieux.md
- Location states match what happened there
- Resource changes are tracked
- Control/ownership is consistent

### Category 3: Object Coherence (Objets)
- Referenced objects exist in objets.md
- Object locations match where characters left them
- Ownership transfers are documented
- Object states (destroyed, used) are consistent

### Category 4: Character Coherence (Personnes)
- Referenced characters exist in personnes.md
- Psychological phases progress logically (no skipping)
- Relationships are bidirectional
- Character presence matches chronology

### Category 5: Thematic Coherence (Themes)
- Theme carriers match character states
- Theme phases progress (not regressing without reason)
- Symbols are used consistently
- Resonances make narrative sense

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Run Temporal Coherence Check

"**🕰️ Temporal coherence check...**"

For detailed check procedures, see: `{bibleFolder}/../data/references/integrity-check-protocols.md`

Cross-check Chronologie events vs character presence, travel times, cause-effect ordering. Output issues found with severity.

### 2. Run Spatial Coherence Check

"**🗺️ Spatial coherence check...**"

Cross-check locations in Chronologie vs Lieux, character locations, resource states. Output issues found.

### 3. Run Object Coherence Check

"**📦 Object coherence check...**"

Cross-check objects in Chronologie vs Objets, ownership, locations. Output issues found.

### 4. Run Character Coherence Check

"**👥 Character coherence check...**"

Cross-check characters, relationships, psychological phases. Output issues found.

### 5. Run Thematic Coherence Check

"**🎭 Thematic coherence check...**"

Cross-check theme carriers, phases, symbols, resonances. Output issues found.

### 6. Generate Validation Report

"**📊 BIBLE VALIDATION REPORT**

**Summary:**
| Category | Checks | Issues | Status |
|-----------|---------------|--------|--------|
| Temporal | [N] | [N] | ✅/⚠️/❌ |
| Spatial | [N] | [N] | ✅/⚠️/❌ |
| Objects | [N] | [N] | ✅/⚠️/❌ |
| Characters | [N] | [N] | ✅/⚠️/❌ |
| Thematic | [N] | [N] | ✅/⚠️/❌ |

**Overall status:** [✅ VALID / ⚠️ WARNINGS / ❌ CRITICAL ISSUES]

**Issue details:**
[List all issues with severity: CRITICAL / WARNING / MINOR]"

### 7. Party Mode for Complex Issues

**IF any CRITIQUE issues found OR user requests discussion:**

For Party Mode procedures and participants, see: `{bibleFolder}/../data/references/integrity-check-protocols.md`

"**🗣️ Activating Party Mode to discuss complex issues...**"

Invoke Party Mode with all perspectives (Timeline Guardian, Cartographer, Archivist, Keeper of Souls, Thematic Weaver).

### 8. Present Final Validation Summary

"**✅ VALIDATION COMPLETE**

**Final verdict:**
- Critical issues: [N] (must be fixed)
- Warnings: [N] (monitor)
- Minor issues: [N] (may be ignored)

[IF all clear:]
**🎉 Your narrative bible is coherent!**

[IF issues found:]
**⚠️ Issues to resolve:**
[List with suggested fixes]"

### 9. Present FINAL MENU OPTIONS

For complete menu handling, report export, and transition protocols, see: `{bibleFolder}/../data/references/validation-protocols.md`

Display: **Validation complete - What would you like to do?**
- **[R]** Re-run validation (after corrections)
- **[P]** Launch **Party Mode** to discuss an issue
- **[U]** Switch to **Update** mode to fix
- **[E]** **Export** the validation report
- **[Q]** **Quit** the workflow

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- All 5 coherence check categories executed
- All issues properly flagged with severity
- Validation report generated
- Party Mode invoked for complex issues (if any)
- Final summary presented with clear verdict
- User offered actionable next steps

### FAILURE:

- Skipping any coherence check category
- Not flagging detected inconsistencies
- Not generating validation report
- Ignoring critical issues without user consent
- Not offering resolution paths

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

This is the FINAL step of Validate mode. After completion:
- User knows the state of their bible's integrity
- Clear path forward: fix issues or celebrate coherence
- The Bible Guardian has fulfilled their duty
