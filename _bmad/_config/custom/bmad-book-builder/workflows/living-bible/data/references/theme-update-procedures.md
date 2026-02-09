# Theme Update Procedures

## Step-by-Step Theme Update Process

This document details the complete procedure for updating the themes dimension during Edit mode.

## 1. Load Current Themes

Load `{bbb_output_folder}/bible/themes.md` and analyze:

- Total themes documented
- Themes mentioned in extraction notes
- Recent thematic progressions
- Active theme carriers

**Output Template:**
```markdown
**État actuel des thèmes :**

- Thèmes documentés : [N]
- Dernière mise à jour : [date]
- Thèmes actifs :
  - [Theme 1]: Phase [X/5] — Porteurs: [characters]
  - [Theme 2]: Phase [X/5] — Porteurs: [characters]

Prêt à mettre à jour la progression thématique.
```

## 2. Review Extraction Notes

From step 1 extraction notes, review theme-related items:

**Categories to Review:**
- Thematic evolutions (phase changes)
- Character-theme connections (new or changed)
- Symbolic manifestations (new or recurring symbols)

**Output Template:**
```markdown
**Mises à jour thématiques détectées :**

**Évolutions thématiques :**
[List themes with phase changes]

**Connexions personnage-thème :**
[List new character-theme connections]

**Manifestations symboliques :**
[List symbolic expressions of themes]
```

## 3. Process Theme Updates

For each theme with updates, document the progression:

### Theme Update Template

```markdown
**Mise à jour : [Theme Name]**

**Progression :**
- Phase précédente : [X/5] — [description]
- Phase actuelle : [Y/5] — [description]
- Événement déclencheur : [what caused the progression]

**Manifestation dans ce chapitre/événement :**
- Type : [Dialogue / Action / Symbole / Décision]
- Description : [how the theme manifested]
- Impact : [narrative consequence]

**Porteurs actuels :**
| Personnage | Rôle thématique | Évolution |
|------------|-----------------|-----------|
| [Name] | [Protagoniste/Antagoniste/Miroir] | [change in relation to theme] |

**Symboles associés :**
- [Symbol]: [significance to this theme]

**Résonances avec autres thèmes :**
- [Other theme]: [Tension / Complémentarité / Écho]
```

### Processing Rules

1. **One theme at a time** - Complete full update for each theme before moving to next
2. **Evidence required** - Every phase change must cite the triggering event
3. **Document all carriers** - Track which characters express or carry each theme
4. **Note symbols** - Record new or recurring symbolic manifestations
5. **Map resonances** - Identify connections with other themes

## 4. Add New Themes

For each new theme identified:

### New Theme Template

```markdown
**Nouveau thème détecté : [Name]**

**Description :** [what this theme explores]

**Phase initiale :** 1/5 (Introduction)

**Première manifestation :**
- Chapitre/Jour : [when it appeared]
- Comment : [how it manifested]

**Porteurs initiaux :**
| Personnage | Rôle | Raison |
|------------|------|--------|
| [Name] | [role] | [why they carry this theme] |

**Potentiel narratif :**
- Direction probable : [how this theme might evolve]
- Conflits potentiels : [with other themes or characters]
```

### New Theme Rules

- Only create new theme with clear evidence from narrative
- Set initial phase to 1/5 (Introduction)
- Identify at least one character carrier
- Note potential conflicts or resonances with existing themes

## 5. Update Theme Resonance Map

Track how themes interact with each other:

### Resonance Map Template

```markdown
**Carte des résonances thématiques mise à jour :**

| Thème A | Thème B | Relation | Exemple |
|---------|---------|----------|---------|
| [Theme] | [Theme] | [Tension/Complémentarité/Écho] | [how they interact] |

**Clusters thématiques identifiés :**
[Groups of related themes that reinforce each other]
```

### Resonance Types

- **Tension:** Themes work at cross-purposes, create conflict
- **Complémentarité:** Themes reinforce each other
- **Écho:** Themes reflect similar ideas in different contexts

## 6. Present Updated Themes

Summarize all changes made:

### Update Summary Template

```markdown
**Mises à jour thématiques effectuées :**

**Progressions :**
| Thème | Phase avant | Phase après | Événement clé |
|-------|-------------|-------------|---------------|
[List changes]

**Nouveaux porteurs :**
| Personnage | Thème | Rôle |
|------------|-------|------|
[List new assignments]

**Carte thématique actuelle :**
- Thèmes en crise (phase 3) : [list]
- Thèmes en résolution (phase 4-5) : [list]
- Thèmes en développement (phase 1-2) : [list]
```

## 7. Confirm and Save

### Save Procedure

1. Write updated content to `{bbb_output_folder}/bible/themes.md`
2. Update file frontmatter:
   ```yaml
   lastUpdated: [current date]
   totalThemes: [updated count]
   themesInCrisis: [count at phase 3]
   ```
3. Update session file:
   ```yaml
   stepsCompleted: ['trigger', 'chronology', 'locations', 'objects', 'characters', 'themes']
   ```
4. Confirm save to user
5. Proceed to final menu

## Related References

- **Phase Definitions:** See `theme-phases.md`
- **Format Guide:** See `theme-format-guide.md`
- **Session Completion:** See `bible-edit-protocols.md`
