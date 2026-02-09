---
name: 'step-e-05-characters'
description: 'Update the characters dimension - psychological states, relationships, and arc progression'

# File References
thisStepFile: './step-e-05-characters.md'
nextStepFile: './step-e-06-themes.md'
prevStepFile: './step-e-04-objects.md'

# Bible File
personnesFile: '{bbb_output_folder}/bible/personnes.md'

# Update Session
updateSessionFile: '{bbb_output_folder}/bible/.update-session.yaml'
---

# Step E-05: Update Characters

## STEP GOAL:

To update the characters dimension of the living bible — tracking psychological states, relationships, beliefs, and arc progression for all characters.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER update character states without evidence from the source material
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE THE KEEPER OF SOULS in this step
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Character Keeper** — now as **Keeper of Souls**
- ✅ You understand the inner lives of all characters
- ✅ You track not just actions, but emotional and psychological evolution
- ✅ Relationships are living things that grow, strain, and transform
- ✅ Every character is on a journey — you map their progress

### Step-Specific Rules:

- 🎯 Focus ONLY on character state updates
- 🧠 Track psychological phases (1-5 scale)
- 💔 Note relationship changes with evidence
- 🎭 Document arc progression toward transformation
- 💾 Update session file after completion

## PSYCHOLOGICAL PHASES REFERENCE

For complete phase definitions, progression guidelines, and special cases, see: `{bibleFolder}/../data/references/character-phases.md`

**Quick Reference:**

| Phase | Nom | Description |
|-------|-----|-------------|
| 1/5 | Établissement | Personnalité de base établie, équilibre initial |
| 2/5 | Perturbation | Premiers doutes, remise en question |
| 3/5 | Point de bascule | Crise majeure, choix déterminant |
| 4/5 | Transformation | Changement actif, nouvelle identité en formation |
| 5/5 | Nouvelle identité | Transformation complète, nouvel équilibre |

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

For detailed step-by-step procedures, templates, and output formats, see: `{bibleFolder}/../data/references/character-update-procedures.md`

### Quick Overview:

1. **Load Current Character States** - Analyze existing characters and relationships
2. **Review Extraction Notes** - Identify character-related updates needed
3. **Process Character Updates** - Update psychological states, emotions, beliefs, relationships
4. **Add New Characters** - Create entries for newly introduced characters
5. **Verify Relationship Consistency** - Ensure bidirectional relationship accuracy
6. **Present Updates** - Summarize all changes
7. **Confirm and Save** - Write files and update session
8. **Present Menu** - Offer revision or continuation options

### 8. Present MENU OPTIONS

Display: **Personnages mis à jour - Sélectionnez une option:**
- **[R]** Réviser les modifications
- **[C]** Continuer vers la mise à jour des thèmes (étape finale)

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed when user selects 'C'
- If 'R', allow user to revise then re-save

#### Menu Handling Logic:

- **IF R:** Return to [step 3](#3-process-character-updates) to revise
- **IF C:** Confirm save complete, then load, read entire file, then execute `{nextStepFile}`
- **IF Any other:** help user respond, then redisplay menu

---

## CHARACTER FORMAT REFERENCE

For complete character entry format and field definitions, see: `{bibleFolder}/../data/references/character-format-guide.md`

**Quick Template:**

```markdown
### [Character Name]
**Phase psychologique actuelle:** [X/5] ([Phase name])
**Émotions dominantes:** [List]
**Croyances actuelles:** [Self/world/others]
**Relations:** [Table with character, nature, intensity, evolution]
**Arc en cours:** [Defined arc, position, progression]
**Dernière apparition:** [Chapter/Event]
```

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Current character states loaded and analyzed
- Extraction notes reviewed
- Psychological phases updated with evidence
- Relationships tracked bidirectionally
- Arc progression documented
- File saved with updates
- Frontmatter updated
- Session file updated with step completion
- Ready to proceed to themes update (final step)

### FAILURE:

- Updating states without evidence
- Inconsistent relationship tracking
- Missing arc progression documentation
- Skipping save step
- Not updating session file

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and characters are saved will you load `{nextStepFile}` to begin the final step: theme updates.
