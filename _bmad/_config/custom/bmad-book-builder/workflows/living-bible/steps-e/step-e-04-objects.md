---
name: 'step-e-04-objects'
description: 'Update the objects dimension - inventory of plot-critical objects with origins and significance'

# File References
thisStepFile: './step-e-04-objects.md'
nextStepFile: './step-e-05-characters.md'
prevStepFile: './step-e-03-locations.md'

# Bible File
objetsFile: '{bbb_output_folder}/bible/objets.md'

# Update Session
updateSessionFile: '{bbb_output_folder}/bible/.update-session.yaml'
---

# Step E-04: Update Objects

## STEP GOAL:

To update the objects dimension of the living bible — tracking plot-critical objects, their origins, significance, ownership, and history.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER add objects without understanding their narrative significance
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE THE ARCHIVIST OF ARTIFACTS in this step
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Character Keeper** — now as **Archivist of Artifacts**
- ✅ You catalog the material world of the story
- ✅ Objects carry meaning beyond their physical form
- ✅ Ownership, transfer, and destruction of objects drive plot
- ✅ Every significant object is a silent character in the story

### Step-Specific Rules:

- 🎯 Focus ONLY on object updates
- 🔮 Track symbolic significance, not just physical properties
- 🔄 Note ownership changes and their implications
- ⚔️ Objects often represent conflicts or stakes
- 💾 Update session file after completion

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Current Objects

Load `{objetsFile}` and analyze:

- Total objects documented
- Objects mentioned in extraction notes
- Recent ownership changes
- Objects with active plot significance

"**État actuel de l'inventaire des objets :**

- Objets documentés : [N]
- Dernière mise à jour : [date]
- Objets récemment actifs :
  - [Object 1]: [current status/owner]
  - [Object 2]: [current status/owner]

Prêt à mettre à jour l'inventaire."

### 2. Review Extraction Notes (Objects)

From step 1 extraction notes, review object-related items:

"**Mises à jour d'objets détectées :**

**Nouveaux objets :**
[List new objects from extraction]

**Changements d'état :**
[List status changes for existing objects]

**Transferts de propriété :**
[List ownership changes]"

### 3. Process New Objects

For each new object, gather complete information:

"**Nouvel objet détecté : [Name]**

Je dois documenter :
- **Origine :** [where it came from, how it was created/found]
- **Description :** [physical appearance]
- **Découvert/Introduit :** Jour [N], chapitre [X]
- **Signification symbolique :** [what it represents in the story]
- **Enjeux narratifs :** [what conflicts or stakes it creates]
- **Propriétaire actuel :** [who possesses it]
- **État :** [condition, quantity if applicable]"

**Significance Categories:**
- 🔮 Symbolique — Ce que l'objet représente
- ⚔️ Enjeux — Quels conflits il génère
- 🎭 Conflits — Qui le veut et pourquoi

### 4. Update Existing Objects

For each existing object with updates:

"**Mise à jour : [Object Name]**

**Événement :**
- Jour [N]: [what happened to/with this object]
- Personnages impliqués: [names]
- Conséquences: [narrative implications]

**Changements :**
- Propriétaire: [old] → [new] (reason)
- État: [old condition] → [new condition]
- Signification: [any new meaning gained]

**Historique mis à jour :**
[Chronological list of events involving this object]"

### 5. Present Updated Objects

"**Mises à jour des objets effectuées :**

**Nouveaux objets ajoutés :**
| Objet | Propriétaire | Signification |
|-------|--------------|---------------|
[List new objects]

**Objets mis à jour :**
| Objet | Changement | Impact |
|-------|------------|--------|
[List updated objects]

**Inventaire narratif actuel :**
- Objets actifs (impliqués dans l'intrigue) : [list]
- Objets dormants (pas récemment mentionnés) : [list]
- Objets détruits/perdus : [list]"

### 6. Confirm and Save

Write updated content to `{objetsFile}`.

Update file frontmatter:
```yaml
lastUpdated: [current date]
totalObjects: [updated count]
activeObjects: [count of plot-active objects]
```

Update session file:
```yaml
stepsCompleted: ['trigger', 'chronology', 'locations', 'objects']
```

### 7. Present MENU OPTIONS

Display: **Objets mis à jour - Sélectionnez une option:**
- **[R]** Réviser les modifications
- **[C]** Continuer vers la mise à jour des personnages

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed when user selects 'C'
- If 'R', allow user to revise then re-save

#### Menu Handling Logic:

- **IF R:** Return to [step 3](#3-process-new-objects) to revise
- **IF C:** Confirm save complete, then load, read entire file, then execute `{nextStepFile}`
- **IF Any other:** help user respond, then redisplay menu

---

## OBJECT FORMAT REFERENCE

```markdown
## Objets

### Capsules de survie

**Origine:** Secteur industriel, vestige de l'Ancien Monde. Fabriquées avant l'effondrement.

**Description:** Capsules métalliques cylindriques (50cm), contenant rations d'urgence et kit médical.

**Découvert:** Jour 47, chapitre 12, par Marc lors de l'exploration du secteur industriel

**Signification:**
- 🔮 Symbolique: Espoir de survie vs rareté des ressources
- ⚔️ Enjeux: 12 capsules pour 30 survivants = conflit inévitable
- 🎭 Conflits: Marc vs Élise pour le contrôle, Julie comme médiatrice

**Propriétaire actuel:** Contrôlées par Marc (contesté par le groupe d'Élise)

**État:** 12 capsules totales, 3 utilisées, 9 restantes

**Historique:**
- Jour 47: Découverte par Marc
- Jour 48: Première utilisation (Chen blessé)
- Jour 50: Conflit avec Élise pour le contrôle
- Jour 52: 2 capsules données au groupe d'Élise en échange de paix

---

### Journal de Sarah

[Continue...]
```

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Current objects loaded and analyzed
- Extraction notes reviewed
- New objects fully documented with significance
- Existing objects updated with changes
- Ownership history tracked
- File saved with updates
- Frontmatter updated
- Session file updated with step completion
- Ready to proceed to characters update

### FAILURE:

- Adding objects without significance analysis
- Missing ownership tracking
- Not documenting object history
- Skipping save step
- Not updating session file

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and objects are saved will you load `{nextStepFile}` to begin character state updates.
