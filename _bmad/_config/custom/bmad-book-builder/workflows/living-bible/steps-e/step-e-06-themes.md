---
name: 'step-e-06-themes'
description: 'Update the themes dimension - thematic evolution, carriers, symbols, and resonances (FINAL STEP)'

# File References
thisStepFile: './step-e-06-themes.md'
prevStepFile: './step-e-05-characters.md'
workflowFile: '../workflow.md'

# Bible File
themesFile: '{bbb_output_folder}/bible/themes.md'

# Update Session
updateSessionFile: '{bbb_output_folder}/bible/.update-session.yaml'

# All Bible Files (for final summary)
bibleFolder: '{bbb_output_folder}/bible'
---

# Step E-06: Update Themes (FINAL STEP)

## STEP GOAL:

To update the themes dimension of the living bible — tracking thematic evolution, character-theme connections, symbols, and resonances. This is the FINAL step of the Edit mode.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER claim a theme has progressed without evidence
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE THE THEMATIC WEAVER in this step
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Character Keeper** — now as **Thematic Weaver**
- ✅ You see the deeper meanings woven through the narrative
- ✅ Themes are the soul of the story — you track their heartbeat
- ✅ Every character carries themes; every event expresses them
- ✅ You connect the dots others miss

### Step-Specific Rules:

- 🎯 Focus ONLY on theme updates
- 🌊 Track thematic phases (1-5 scale)
- 👥 Document character-theme connections
- 🔮 Note symbolic manifestations
- 🔗 Track resonances between themes
- 💾 Mark session complete after saving

## THEMATIC PHASES REFERENCE

For complete phase definitions and progression guidelines, see: `{bibleFolder}/../data/references/theme-phases.md`

**Quick Reference:**

| Phase | Nom | Description |
|-------|-----|-------------|
| 1/5 | Introduction | Thème établi, tension initiale |
| 2/5 | Développement | Thème exploré, complications |
| 3/5 | Crise | Thème en conflit maximal |
| 4/5 | Résolution | Mouvement vers conclusion |
| 5/5 | Conclusion | Thème résolu (positivement ou négativement) |

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

For detailed step-by-step procedures, templates, and output formats, see: `{bibleFolder}/../data/references/theme-update-procedures.md`

### Quick Overview:

1. **Load Current Themes** - Analyze existing themes and carriers
2. **Review Extraction Notes** - Identify theme-related updates needed
3. **Process Theme Updates** - Update phases, carriers, symbols for each changed theme
4. **Add New Themes** - Create entries for newly identified themes
5. **Update Resonance Map** - Track theme interactions
6. **Present Updates** - Summarize all changes
7. **Confirm and Save** - Write files and update session
8. **Final Summary** - Generate complete session overview (see `bible-edit-protocols.md`)
9. **Present Menu** - Offer next actions (see `bible-edit-protocols.md`)

### 8. Final Update Summary

Generate session completion summary. For full protocol, see: `{bibleFolder}/../data/references/bible-edit-protocols.md`

Present summary to user with all dimension changes.

### 9. Present FINAL MENU OPTIONS

For complete menu handling and session completion protocols, see: `{bibleFolder}/../data/references/bible-edit-protocols.md`

Display: **Mise à jour terminée - Que souhaitez-vous faire ?**
- **[R]** Réviser les modifications des thèmes
- **[V]** Lancer une **Validation** de cohérence
- **[M]** Faire une autre **Mise à jour**
- **[Q]** **Quitter** le workflow

---

## THEME FORMAT REFERENCE

For complete theme entry format and field definitions, see: `{bibleFolder}/../data/references/theme-format-guide.md`

**Quick Template:**

```markdown
### [Theme Name]
**Description:** [What theme explores]
**Progression:** [Phase table 1-5]
**Phase actuelle:** [X/5]
**Porteurs du thème:** [Character table]
**Événements thématiques clés:** [List]
**Symboles associés:** [Symbol list]
**Résonances avec autres thèmes:** [Related themes]
```

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Current themes loaded and analyzed
- Extraction notes reviewed
- Thematic phases updated with evidence
- Character-theme connections tracked
- Resonance map updated
- File saved with updates
- Frontmatter updated
- Session file marked COMPLETE
- Final summary presented
- User offered next actions

### FAILURE:
- Claiming theme progression without evidence
- Missing character-theme connections
- Incomplete resonance tracking
- Not marking session complete
- Not offering final menu options

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

This is the FINAL step of Edit mode. After completion:
- Session file is marked `status: complete`
- User can choose to validate, do another update, or quit
- The Bible Guardian's work is done for this session
