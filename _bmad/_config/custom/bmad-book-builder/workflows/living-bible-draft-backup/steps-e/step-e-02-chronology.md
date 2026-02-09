---
name: 'step-e-02-chronology'
description: 'Update the chronology dimension - day-by-day timeline of story events'

# File References
thisStepFile: './step-e-02-chronology.md'
nextStepFile: './step-e-03-locations.md'
prevStepFile: './step-e-01-trigger.md'

# Bible File
chronologieFile: '{bbb_output_folder}/bible/chronologie.md'
---

# Step E-02: Update Chronology

## STEP GOAL:

To update the chronology dimension of the living bible — adding new days, events, and ensuring timeline consistency.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- NEVER add events without verifying timeline consistency
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE THE TIMELINE GUARDIAN in this step
- YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- You are the **Character Keeper** — now focused on temporal continuity
- You ensure the story's timeline is coherent
- You catch temporal inconsistencies before they become plot holes
- Days must flow logically; events must have causes before effects

### Step-Specific Rules:

- Focus ONLY on chronology updates
- Verify temporal logic before adding entries
- Flag any potential timeline conflicts
- Use extraction notes from step 1

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Current Chronology

Load `{chronologieFile}` and analyze:

- Last recorded day
- Number of days covered
- Major events per day
- Any gaps in the timeline

"**État actuel de la chronologie :**

- Dernier jour enregistré : Jour [X]
- Total jours couverts : [N]
- Événements majeurs récents :
  - Jour [X-2]: [event]
  - Jour [X-1]: [event]
  - Jour [X]: [event]

Prêt à ajouter les nouveaux événements."

### 2. Review Extraction Notes (Chronology)

From step 1 extraction notes, review chronology-related items:

"**Événements à ajouter :**

[List from extraction notes]

**Vérification temporelle :**
- Ces événements se situent-ils après le Jour [last recorded day] ? [Oui/Non]
- Y a-t-il des références à des jours antérieurs à corriger ? [Oui/Non]"

### 3. Verify Timeline Consistency

Before adding, verify:

**Temporal Logic Checks:**
- Events happen after their causes
- Travel times are realistic
- Character presence is possible (not in two places at once)
- Seasonal/weather consistency (if applicable)

"**Vérification de cohérence temporelle :**

- [ ] Causalité respectée (causes avant effets)
- [ ] Temps de déplacement réalistes
- [ ] Présence des personnages cohérente
- [ ] Aucun conflit détecté

[If conflicts detected:]
**Conflit potentiel détecté :**
[Description du conflit]
Comment souhaitez-vous résoudre ceci ?"

### 4. Add New Entries

For each new day/event, format according to the chronology structure:

```markdown
### Jour [N]

**[Période]:** [Événement]
- Détails: [specifics]
- Personnages impliqués: [names]
- Lieu: [location]
- Conséquences: [immediate outcomes]

**[Next période]:** [Événement]
...
```

**Périodes disponibles:** Matin, Midi, Après-midi, Soir, Nuit

### 5. Present Updated Chronology

"**Nouvelles entrées ajoutées à la chronologie :**

[Display new entries in formatted structure]

**Résumé des ajouts :**
- Nouveaux jours : [count]
- Nouveaux événements : [count]
- Personnages mentionnés : [list]
- Lieux visités : [list]"

### 6. Confirm and Save

Write updated content to `{chronologieFile}`.

Update frontmatter:
```yaml
lastUpdated: [current date]
lastChapter: [chapter number if applicable]
totalDays: [updated count]
```

### 7. Present MENU OPTIONS

Display: **Chronologie mise à jour - Sélectionnez une option:**
- **[R]** Réviser les entrées ajoutées
- **[C]** Continuer vers la mise à jour des lieux

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed when user selects 'C'
- If 'R', allow user to revise then re-save

#### Menu Handling Logic:

- **IF R:** Return to [step 4](#4-add-new-entries) to revise
- **IF C:** Confirm save complete, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## CHRONOLOGY FORMAT REFERENCE

```markdown
## Chronologie

### Jour 1
**Matin:** Réveil de Marc dans les décombres
- Détails: Confusion initiale, découverte de la situation
- Personnages impliqués: Marc (seul)
- Lieu: Ancien bâtiment administratif
- Conséquences: Début de l'exploration

**Après-midi:** Première rencontre avec Julie
- Détails: Rencontre fortuite près du point d'eau
- Personnages impliqués: Marc, Julie
- Lieu: Fontaine centrale
- Conséquences: Alliance naissante

### Jour 2
[Continue...]
```

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Current chronology loaded and analyzed
- Extraction notes reviewed
- Timeline consistency verified
- New entries formatted correctly
- File updated with new content
- Frontmatter updated
- Ready to proceed to locations update

### FAILURE:

- Adding entries without verifying consistency
- Creating timeline conflicts
- Not saving to file
- Skipping consistency checks

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and chronology is saved will you load {nextStepFile} to begin location updates.
