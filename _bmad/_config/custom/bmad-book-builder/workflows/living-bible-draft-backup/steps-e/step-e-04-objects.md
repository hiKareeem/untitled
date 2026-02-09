---
name: 'step-e-04-objects'
description: 'Update the objects dimension - inventory of plot-critical objects with origins, significance, and current status'

# File References
thisStepFile: './step-e-04-objects.md'
nextStepFile: './step-e-05-characters.md'
prevStepFile: './step-e-03-locations.md'

# Bible File
objetsFile: '{bbb_output_folder}/bible/objets.md'
---

# Step E-04: Update Objects

## STEP GOAL:

To update the objects dimension of the living bible — tracking plot-critical objects, their origins, significance, ownership, and current status.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- NEVER track trivial objects — only plot-significant items
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE THE ARCHIVIST OF ARTIFACTS in this step
- YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- You are the **Character Keeper** — now focused on object continuity
- Objects carry meaning — they're symbols, plot devices, MacGuffins
- Every significant object has a story: origin, journey, destination
- Objects can create conflict, resolve tension, reveal character

### Step-Specific Rules:

- Focus ONLY on plot-significant objects
- Track ownership changes meticulously
- Note symbolic significance
- Ignore mundane items unless they become significant

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Current Objects

Load `{objetsFile}` and analyze:

- Total objects documented
- Object categories (weapons, documents, symbols, resources)
- Recent ownership changes

"**État actuel de l'inventaire des objets :**

- Objets documentés : [N]
- Dernière mise à jour : [date]
- Catégories :
  - Armes/Outils : [count]
  - Documents/Information : [count]
  - Symboles/Reliques : [count]
  - Ressources critiques : [count]

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

### 3. Evaluate Object Significance

For each potential new object, evaluate significance:

"**Évaluation de signification : [Object Name]**

Questions clés :
- Cet objet influence-t-il l'intrigue ? [Oui/Non]
- Cet objet révèle-t-il quelque chose sur un personnage ? [Oui/Non]
- Cet objet crée-t-il ou résout-il un conflit ? [Oui/Non]
- Cet objet a-t-il une valeur symbolique ? [Oui/Non]

**Verdict :** [À documenter / Objet trivial à ignorer]"

### 4. Process New Objects

For each significant new object:

"**Nouvel objet : [Name]**

**Origine :**
- Provenance : [where it comes from]
- Découvert/Créé : Jour [N], par [character]
- Circonstances : [how it was found/made]

**Description :**
- Apparence : [physical description]
- Fonction : [what it does]
- État : [condition]

**Signification :**
- Symbolique : [what it represents]
- Enjeux : [why it matters to the plot]
- Conflits potentiels : [who wants it, why]

**Propriétaire actuel :** [character name]

**Historique :**
- Jour [N]: [First mention/discovery]"

### 5. Update Existing Objects

For each existing object with updates:

"**Mise à jour : [Object Name]**

**Changement d'état :**
- Ancien état : [previous]
- Nouvel état : [current]
- Cause : [what happened]

**Transfert de propriété :**
- Ancien propriétaire : [character]
- Nouveau propriétaire : [character]
- Circonstances : [how it changed hands]

**Nouvel événement :**
- Jour [N]: [event involving the object]"

### 6. Present Updated Objects

"**Mises à jour de l'inventaire effectuées :**

**Nouveaux objets ajoutés :**
[List with significance summary]

**Objets mis à jour :**
[List with summary of changes]

**État actuel de l'inventaire :**
- Objets actifs (en jeu) : [list]
- Objets perdus/détruits : [list]
- Objets en attente (mentionnés mais pas encore utilisés) : [list]"

### 7. Confirm and Save

Write updated content to `{objetsFile}`.

Update frontmatter:
```yaml
lastUpdated: [current date]
totalObjects: [updated count]
activeObjects: [count currently in play]
```

### 8. Present MENU OPTIONS

Display: **Objets mis à jour - Sélectionnez une option:**
- **[R]** Réviser les modifications
- **[C]** Continuer vers la mise à jour des personnages

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed when user selects 'C'
- If 'R', allow user to revise then re-save

#### Menu Handling Logic:

- **IF R:** Return to [step 4](#4-process-new-objects) to revise
- **IF C:** Confirm save complete, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## OBJECT FORMAT REFERENCE

```markdown
## Objets

### Capsules de Survie

**Origine:**
- Provenance: Secteur industriel, vestige de l'Ancien Monde
- Découvert: Jour 47, par Marc
- Circonstances: Trouvées dans un bunker scellé

**Description:**
- Apparence: Cylindres métalliques de 30cm, sceau intact
- Fonction: Nutrition d'urgence pour 3 jours par capsule
- État: 9 intactes, 3 utilisées

**Signification:**
- Symbolique: Espoir de survie vs ressource limitée
- Enjeux: Qui décide de leur distribution ?
- Conflits potentiels: Tension entre Marc et Élise sur le contrôle

**Propriétaire actuel:** Contrôlées par le groupe de Marc (stockées au QG)

**Historique:**
- Jour 47: Découverte par Marc (12 capsules)
- Jour 48: Première utilisation (Julie, blessure)
- Jour 52: Deuxième utilisation (Chen, maladie)
- Jour 55: Troisième utilisation (enfant réfugié)
- Jour 58: Tension — Élise demande redistribution

---

### Journal de l'Ancien Monde

[Continue...]
```

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Current objects loaded and analyzed
- Extraction notes reviewed
- New objects evaluated for significance
- Significant objects fully documented
- Existing objects updated
- File saved with updates
- Ready to proceed to character states update

### FAILURE:

- Tracking trivial objects
- Missing ownership/provenance information
- Incomplete significance assessment
- Not tracking ownership changes

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and objects are saved will you load {nextStepFile} to begin character state updates.
