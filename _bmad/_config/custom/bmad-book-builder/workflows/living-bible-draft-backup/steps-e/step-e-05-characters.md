---
name: 'step-e-05-characters'
description: 'Update the character states dimension - psychological states, relationships, and arc progression'

# File References
thisStepFile: './step-e-05-characters.md'
nextStepFile: './step-e-06-themes.md'
prevStepFile: './step-e-04-objects.md'

# Bible File
personnesFile: '{bbb_output_folder}/bible/personnes.md'

# Related Files
characterDossiersPattern: '{bbb_output_folder}/character-dossiers/*.md'
---

# Step E-05: Update Character States

## STEP GOAL:

To update the character states dimension of the living bible — tracking current psychological states, relationship dynamics, and arc progression for all active characters.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- NEVER update character states without evidence from source content
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE THE KEEPER OF SOULS in this step
- YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- You are the **Character Keeper** — guardian of character continuity
- Characters are living beings with evolving psychologies
- Relationships shift, grow, fracture — track every change
- Arc progression must be organic, not sudden jumps

### Step-Specific Rules:

- Focus on CHARACTER STATES (current snapshot), not full biographies
- Track psychological evolution, not just actions
- Map relationship dynamics between characters
- Note arc phase progression

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Current Character States

Load `{personnesFile}` and analyze:

- Characters being tracked
- Current psychological phases
- Recent relationship changes
- Arc progressions

"**État actuel du suivi des personnages :**

- Personnages suivis : [N]
- Dernière mise à jour : [date]

**Aperçu rapide :**
| Personnage | Phase psychologique | Arc | Dernière apparition |
|------------|--------------------|----|---------------------|
| [Name 1] | [Phase X/5] | [Arc name] | Chapitre [N] |
| [Name 2] | [Phase X/5] | [Arc name] | Chapitre [N] |
...

Prêt à mettre à jour les états."

### 2. Review Extraction Notes (Characters)

From step 1 extraction notes, review character-related items:

"**Mises à jour de personnages détectées :**

**États psychologiques modifiés :**
[List characters with psychological changes]

**Relations modifiées :**
[List relationship changes between characters]

**Progressions d'arc :**
[List arc phase changes]"

### 3. Update Psychological States

For each character with psychological changes:

"**Mise à jour psychologique : [Character Name]**

**État précédent :**
- Phase : [X/5] ([phase name])
- État émotionnel : [description]
- Croyances dominantes : [beliefs]

**Déclencheur du changement :**
- Événement : [what happened]
- Impact : [how it affected them]

**Nouvel état :**
- Phase : [X/5] ([phase name])
- État émotionnel : [new description]
- Croyances modifiées : [updated beliefs]

**Manifestation comportementale :**
- Avant : [how they acted]
- Maintenant : [how they act now]"

### 4. Update Relationships

For each relationship change:

"**Mise à jour relationnelle : [Character A] ↔ [Character B]**

**État précédent :**
- Nature : [type of relationship]
- Intensité : [low/medium/high]
- Dynamique : [description]

**Événement déclencheur :**
- Jour [N]: [what happened between them]

**Nouvel état :**
- Nature : [updated type]
- Intensité : [updated level]
- Dynamique : [new description]
- Tension/Harmonie : [current state]"

### 5. Update Arc Progression

For each arc progression:

"**Progression d'arc : [Character Name]**

**Arc :** [Arc name, e.g., "Individualisme → Collectivisme"]

**Phase précédente :** [X/5]
- [Description of previous phase]

**Événement de progression :**
- Jour [N]: [pivotal moment]

**Nouvelle phase :** [X+1/5]
- [Description of new phase]

**Indicateurs observés :**
- [Behavioral evidence 1]
- [Behavioral evidence 2]
- [Behavioral evidence 3]

**Prochaine phase attendue :** [X+2/5]
- Déclencheur probable : [what might cause next progression]"

### 6. Present Updated Character States

"**Mises à jour des personnages effectuées :**

**États psychologiques modifiés :**
[Summary for each character]

**Relations modifiées :**
[Summary of relationship changes]

**Arcs progressés :**
[Summary of arc changes]

**Tableau de synthèse mis à jour :**
| Personnage | Phase | Arc | Relations clés | Dernier changement |
|------------|-------|-----|----------------|-------------------|
| [Name 1] | [X/5] | [Arc] | [Key relations] | [Last change] |
..."

### 7. Confirm and Save

Write updated content to `{personnesFile}`.

Update frontmatter:
```yaml
lastUpdated: [current date]
totalCharacters: [count]
lastChapter: [chapter number]
```

### 8. Present MENU OPTIONS

Display: **Personnages mis à jour - Sélectionnez une option:**
- **[R]** Réviser les modifications
- **[C]** Continuer vers la mise à jour des thèmes

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed when user selects 'C'
- If 'R', allow user to revise then re-save

#### Menu Handling Logic:

- **IF R:** Return to [step 3](#3-update-psychological-states) to revise
- **IF C:** Confirm save complete, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## REFERENCE DOCUMENTATION

For detailed character state format and psychological phase definitions, refer to:

- **Character State Format**: `{workflow_root}/data/references/character-state-format.md`
- **Psychological Phases**: `{workflow_root}/data/references/psychological-phases.md`

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Current character states loaded
- Extraction notes reviewed
- Psychological changes documented with evidence
- Relationships updated with dynamics
- Arc progressions tracked
- File saved with updates
- Ready to proceed to themes update

### FAILURE:

- Updating states without evidence
- Skipping relationship dynamics
- Jumping arc phases without events
- Not tracking all affected characters

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and character states are saved will you load {nextStepFile} to begin theme updates.
