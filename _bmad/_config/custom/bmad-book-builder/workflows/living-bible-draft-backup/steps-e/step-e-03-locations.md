---
name: 'step-e-03-locations'
description: 'Update the locations dimension - location database with resources, events, and occupants'

# File References
thisStepFile: './step-e-03-locations.md'
nextStepFile: './step-e-04-objects.md'
prevStepFile: './step-e-02-chronology.md'

# Bible File
lieuxFile: '{bbb_output_folder}/bible/lieux.md'
---

# Step E-03: Update Locations

## STEP GOAL:

To update the locations dimension of the living bible — adding new locations, updating existing ones with new events, resources, and occupant changes.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- NEVER add locations without complete information
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE THE CARTOGRAPHER in this step
- YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- You are the **Character Keeper** — now focused on spatial continuity
- You map the story's world with precision
- Every location has history, resources, and significance
- Locations are characters too — they evolve with the story

### Step-Specific Rules:

- Focus ONLY on location updates
- Track what happens WHERE
- Note resource changes (depleted, discovered, contested)
- Track who controls/occupies each location

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Current Locations

Load `{lieuxFile}` and analyze:

- Total locations documented
- Recently updated locations
- Locations mentioned in extraction notes

"**État actuel de la base de lieux :**

- Lieux documentés : [N]
- Dernière mise à jour : [date]
- Lieux récemment actifs :
  - [Location 1]: [last event]
  - [Location 2]: [last event]

Prêt à mettre à jour les lieux."

### 2. Review Extraction Notes (Locations)

From step 1 extraction notes, review location-related items:

"**Mises à jour de lieux détectées :**

**Nouveaux lieux :**
[List new locations from extraction]

**Mises à jour de lieux existants :**
[List updates for existing locations]

**Événements par lieu :**
[List events that occurred at each location]"

### 3. Process New Locations

For each new location, gather complete information:

"**Nouveau lieu détecté : [Name]**

Je dois documenter :
- Description : [physical description]
- Découvert : Jour [N], par [character]
- Ressources : [what can be found here]
- Dangers : [potential threats]
- Signification : [why this place matters to the story]
- État actuel : [current condition]
- Contrôlé par : [who controls it, if anyone]"

Format and add to locations file.

### 4. Update Existing Locations

For each existing location with updates:

"**Mise à jour : [Location Name]**

**Nouvel événement :**
- Jour [N]: [event description]
- Personnages impliqués: [names]
- Conséquences: [what changed]

**Changements d'état :**
- Ressources: [added/depleted/contested]
- Contrôle: [changed to/remained with]
- Condition: [improved/degraded/destroyed]"

### 5. Present Updated Locations

"**Mises à jour des lieux effectuées :**

**Nouveaux lieux ajoutés :**
[List with brief descriptions]

**Lieux mis à jour :**
[List with summary of changes]

**Carte narrative actuelle :**
- Lieux actifs (scènes récentes) : [list]
- Lieux dormants (pas de scènes récentes) : [list]
- Lieux détruits/inaccessibles : [list]"

### 6. Confirm and Save

Write updated content to `{lieuxFile}`.

Update frontmatter:
```yaml
lastUpdated: [current date]
totalLocations: [updated count]
activeLocations: [count of recently used]
```

### 7. Present MENU OPTIONS

Display: **Lieux mis à jour - Sélectionnez une option:**
- **[R]** Réviser les modifications
- **[C]** Continuer vers la mise à jour des objets

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed when user selects 'C'
- If 'R', allow user to revise then re-save

#### Menu Handling Logic:

- **IF R:** Return to [step 3](#3-process-new-locations) to revise
- **IF C:** Confirm save complete, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## LOCATION FORMAT REFERENCE

```markdown
## Lieux

### Secteur Industriel

**Description:** Vaste zone d'entrepôts et d'usines abandonnés, partiellement effondrés.

**Découvert:** Jour 12, par Marc lors d'une exploration solo

**Ressources:**
- Outils (abondants)
- Matériaux de construction (modérés)
- Nourriture en conserve (épuisée depuis Jour 35)

**Dangers:**
- Structures instables
- Chiens sauvages (éliminés Jour 20)

**Événements clés:**
- Jour 12: Première exploration par Marc
- Jour 20: Confrontation avec les chiens sauvages
- Jour 35: Épuisement des réserves de nourriture
- Jour 47: Découverte des capsules de survie

**Signification:** Symbole de l'ancien monde, source de conflit pour les ressources

**État actuel:** Partiellement sécurisé, exploration en cours

**Contrôlé par:** Groupe de Marc (depuis Jour 25)

---

### Fontaine Centrale

[Continue...]
```

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Current locations loaded and analyzed
- Extraction notes reviewed
- New locations fully documented
- Existing locations updated with new events
- File saved with updates
- Frontmatter updated
- Ready to proceed to objects update

### FAILURE:

- Adding incomplete location entries
- Missing event documentation
- Not tracking resource/control changes
- Skipping save step

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and locations are saved will you load {nextStepFile} to begin object updates.
