---
name: 'step-05-update-progression'
description: 'Update tracking files with validated analysis'

nextStepFile: './step-06-verify-consistency.md'
themeTemplate: '../data/theme-template.md'
emotionTemplate: '../data/emotion-template.md'
chapterTemplate: '../data/chapter-analysis-template.md'
---

# Step 5: Update Progression

## STEP GOAL:

To update all tracking files with the user-validated analysis from step 4.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 ONLY execute after user approval in step 4
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step, ensure entire file is read
- 📋 YOU ARE WRITING validated data to persistent files
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Thematic Weaver** - committing analysis to record
- ✅ User has validated - now execute the updates
- ✅ Be precise - these files are the source of truth
- ✅ Preserve existing data while adding new

### Step-Specific Rules:

- 🎯 Focus ONLY on writing validated analysis to files
- 🚫 FORBIDDEN to add anything not in the validated analysis
- 🚫 FORBIDDEN to modify existing data without clear reason
- 💬 Approach: Methodical - update each file systematically

## EXECUTION PROTOCOLS:

- 🎯 Update themes.md with theme progression
- 💾 Update emotions.md with emotional beats
- 📖 Create/update chapter-{XX}-themes.md
- 🚫 Only write what was validated in step 4

## CONTEXT BOUNDARIES:

- Available: Validated analysis from step 4, existing tracking files
- Focus: File updates only
- Limits: Only validated content
- Dependencies: User approval from step 4

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise.

### 1. Confirm Validation Status

"**Mise à jour des fichiers de tracking - Chapitre {chapterNumber}**

✅ Analyse validée par l'utilisateur
📝 Début des mises à jour..."

### 2. Update themes.md

"**Mise à jour de themes.md...**"

For EACH theme with activity in this chapter:

**Load existing theme entry from themes.md**

**Add to Per-Chapter Progression table:**
```markdown
| {chapterNumber} | [Theme Event from analysis] | [Character Impact] | [Next Step] |
```

**Update Progression by Chapter Phase if applicable:**
- Only if this chapter marks a phase transition
- Reference the validated analysis

**Update Character Connections if new insights:**
- Only add, don't remove existing
- New character-theme connections discovered

**Write updated themes.md**

"✅ themes.md mis à jour
   - [N] thèmes avec nouvelles entrées
   - [N] nouvelles connexions personnage-thème"

### 3. Update emotions.md

"**Mise à jour de emotions.md...**"

For EACH character with emotional beats:

**Load existing character entry (or create from {emotionTemplate})**

**Add to Per-Chapter Emotional Beats table:**
```markdown
| {chapterNumber} | [Emotional State] | [Trigger] | [Expression] | [Impact on Others] |
```

**Update Emotional Arc Summary if significant shift:**
- Only if this chapter contains a turning point
- Append to existing summary, don't overwrite

**Write updated emotions.md**

"✅ emotions.md mis à jour
   - [N] personnages avec nouveaux beats
   - [N] trajectoires mises à jour"

### 4. Create/Update Chapter Analysis File

"**Création de chapter-{chapterNumber}-themes.md...**"

**If file doesn't exist:** Create from {chapterTemplate}

**Fill in all sections from validated analysis:**

```markdown
# Chapter {chapterNumber} Thematic Analysis

**Chapter Title:** [if known]
**Analyzed:** [today's date]
**Word Count:** [approximate]

---

## Themes Present

[From step 2 validated findings]

---

## Emotional Beats

[From step 3 validated findings]

---

## Character Development

[From step 4 validated synthesis]

---

## Red Flags

[From step 4 red flag analysis]

---

## Continuity Notes

[From analysis]

---

## Summary

**One-line chapter theme summary:** [from analysis]
**Themes advanced:** [list]
**Themes static:** [list]
**New elements introduced:** [list]
```

**Write chapter-{chapterNumber}-themes.md**

"✅ chapter-{chapterNumber}-themes.md créé/mis à jour"

### 5. Summarize Updates

"**══════════════════════════════════════════════════════════════════**
**MISE À JOUR TERMINÉE**
**══════════════════════════════════════════════════════════════════**

**Fichiers modifiés :**

| Fichier | Action | Détails |
|---------|--------|---------|
| themes.md | Mis à jour | [N] thèmes, [N] entrées ajoutées |
| emotions.md | Mis à jour | [N] personnages, [N] beats ajoutés |
| chapter-{chapterNumber}-themes.md | Créé/Mis à jour | Analyse complète |

**Données persistées avec succès.**

Passage à la vérification de cohérence..."

### 6. Present MENU OPTIONS

Display: "**Sélectionnez :** [C] Continuer vers la vérification"

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed to verification when user selects 'C'

#### Menu Handling Logic:

- IF C: Confirm files saved, then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- themes.md updated with chapter entries
- emotions.md updated with character beats
- chapter-XX-themes.md created/updated
- Only validated content written
- Existing data preserved
- All updates confirmed

### ❌ SYSTEM FAILURE:

- Writing non-validated content
- Overwriting existing data without reason
- Skipping any of the three files
- Not confirming successful writes
- Adding interpretations not in validated analysis

**Master Rule:** Write ONLY what was validated. Preserve existing data. Confirm all updates.
