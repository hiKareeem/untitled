---
name: 'step-e-06-themes'
description: 'Update the themes dimension - thematic evolution and character-theme connections'

# File References
thisStepFile: './step-e-06-themes.md'
prevStepFile: './step-e-05-characters.md'
workflowFile: '../workflow.md'

# Bible File
themesFile: '{bbb_output_folder}/bible/themes.md'
---

# Step E-06: Update Themes (Final Step)

## STEP GOAL:

To update the themes dimension of the living bible — tracking thematic evolution per chapter and character-theme connections. This is the final step of the Living Bible workflow.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- NEVER invent themes — extract them from the story content
- CRITICAL: Read the complete step file before taking any action
- YOU ARE THE THEMATIC WEAVER in this step
- YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- You are the **Character Keeper** — now focused on thematic continuity
- Themes are the soul of the story — its deeper meaning
- Themes manifest through characters, events, symbols
- Track how themes evolve, not just what they are

### Step-Specific Rules:

- Focus on THEMATIC EVOLUTION, not theme identification
- Connect themes to specific characters and events
- Track progression phases per theme
- Note thematic resonance between story elements

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Current Themes

Load `{themesFile}` and analyze:

- Themes being tracked
- Current progression phases
- Character-theme connections
- Recent thematic events

"**État actuel du suivi thématique :**

- Thèmes suivis : [N]
- Dernière mise à jour : [date]

**Aperçu des thèmes :**
| Thème | Phase actuelle | Porteurs principaux | Chapitre clé |
|-------|---------------|---------------------|--------------|
| [Theme 1] | [Phase X/5] | [Characters] | Ch. [N] |
| [Theme 2] | [Phase X/5] | [Characters] | Ch. [N] |
...

Prêt à mettre à jour la progression thématique."

### 2. Review Extraction Notes (Themes)

From step 1 extraction notes, review theme-related items:

"**Évolutions thématiques détectées :**

[List thematic developments from extraction]

**Connexions personnage-thème :**

[List how characters embody/challenge themes]"

### 3. Update Theme Progressions

For each theme with evolution:

"**Évolution thématique : [Theme Name]**

**Phase précédente :** [X/5] - [Phase description]

**Événements thématiques récents :**
- Chapitre [N]: [How theme manifested]
- Impact: [What this means for theme progression]

**Nouvelle phase :** [X/5] - [New phase description]

**Manifestations observées :**
- Dialogue : [Quote or paraphrase illustrating theme]
- Action : [Event that embodies theme]
- Symbole : [Object or image representing theme]

**Porteurs du thème :**
- [Character 1]: [How they carry this theme]
- [Character 2]: [How they carry this theme]"

### 4. Update Character-Theme Connections

"**Connexions personnage-thème mises à jour :**

### [Character Name]

**Thèmes portés :**
| Thème | Rôle | Évolution |
|-------|------|-----------|
| [Theme 1] | Protagoniste | Arc de [X] → [Y] |
| [Theme 2] | Antagoniste | Résiste au changement |

**Événement thématique récent :**
- Chapitre [N]: [How character embodied/challenged theme]"

### 5. Map Thematic Resonance

Identify how themes echo across the story:

"**Résonances thématiques :**

**[Theme 1] ↔ [Theme 2]:**
- Tension : [How these themes create conflict]
- Résolution potentielle : [How they might resolve]

**Patterns observés :**
- Chapitre [N] fait écho au Chapitre [M] via [theme]
- [Symbol/Object] lie [Character A] et [Character B] thématiquement"

### 6. Present Updated Themes

"**Mises à jour thématiques effectuées :**

**Progressions de thèmes :**
[Summary of phase changes]

**Connexions mises à jour :**
[Summary of character-theme updates]

**Résonances cartographiées :**
[Summary of thematic echoes]

**Tableau de synthèse mis à jour :**
| Thème | Phase | Porteurs | Prochaine évolution attendue |
|-------|-------|----------|------------------------------|
| [Theme 1] | [X/5] | [Names] | [Prediction] |
..."

### 7. Confirm and Save

Write updated content to `{themesFile}`.

Update frontmatter:
```yaml
lastUpdated: [current date]
totalThemes: [count]
lastChapter: [chapter number]
```

### 8. Complete Living Bible Update

"**Mise à jour Living Bible terminée !**

**Résumé des mises à jour :**

| Dimension | Éléments mis à jour |
|-----------|---------------------|
| Chronologie | [N] nouveaux événements |
| Lieux | [N] lieux ajoutés/mis à jour |
| Objets | [N] objets ajoutés/mis à jour |
| Personnages | [N] états modifiés |
| Thèmes | [N] progressions enregistrées |

**Fichiers mis à jour :**
- `bible/chronologie.md`
- `bible/lieux.md`
- `bible/objets.md`
- `bible/personnes.md`
- `bible/themes.md`

**Prochaines actions recommandées :**
- [ ] Relire les mises à jour pour cohérence
- [ ] Vérifier les connexions inter-dimensions
- [ ] Planifier le prochain chapitre avec la bible à jour

Votre bible narrative est maintenant à jour. Bonne continuation d'écriture !"

### 9. Present FINAL MENU

Display: **Living Bible mise à jour - Que souhaitez-vous faire ?**
- **[R]** Réviser une dimension spécifique
- **[E]** Exporter un résumé de la bible
- **[Q]** Quitter le workflow

#### Menu Handling Logic:

- **IF R:** Ask which dimension, then return to appropriate step
- **IF E:** Generate a summary document of all 5 dimensions
- **IF Q:** End workflow gracefully

---

## REFERENCE DOCUMENTATION

For detailed theme format and thematic phase definitions, refer to:

- **Theme Format**: `{workflow_root}/data/references/theme-format.md`
- **Thematic Phases**: `{workflow_root}/data/references/thematic-phases.md`

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Current themes loaded
- Extraction notes reviewed
- Theme progressions documented
- Character-theme connections updated
- Thematic resonances mapped
- File saved with updates
- Complete summary provided
- Workflow gracefully concluded

### FAILURE:

- Inventing themes not in the story
- Skipping character-theme connections
- Not mapping progressions
- Incomplete summary

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## WORKFLOW COMPLETION

This is the **final step** of the Living Bible workflow. Upon completion, the user has a fully updated, multi-dimensional story bible ready to support continued writing.
