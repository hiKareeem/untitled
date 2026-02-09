# Character Update Procedures

## Step-by-Step Character Update Process

This document details the complete procedure for updating the characters dimension during Edit mode.

## 1. Load Current Character States

Load `{bbb_output_folder}/bible/personnes.md` and analyze:

- Total characters documented
- Characters mentioned in extraction notes
- Recent psychological changes
- Active relationship dynamics

**Output Template:**
```markdown
**État actuel de la base des personnages :**

- Personnages documentés : [N]
- Dernière mise à jour : [date]
- Personnages récemment actifs :
  - [Character 1]: Phase [X/5] — [brief state]
  - [Character 2]: Phase [X/5] — [brief state]

Prêt à mettre à jour les états des personnages.
```

## 2. Review Extraction Notes

From step 1 extraction notes, review character-related items:

**Categories to Review:**
- Psychological states (emotions, beliefs)
- Relationship changes (new, modified, ended)
- Arc progression (movement toward transformation)
- New character introductions

**Output Template:**
```markdown
**Mises à jour de personnages détectées :**

**États psychologiques modifiés :**
[List characters with psychological changes]

**Relations modifiées :**
[List relationship changes]

**Progressions d'arc :**
[List characters whose arcs have progressed]
```

## 3. Process Character Updates

For each character with updates, document the changes:

### Character Update Template

```markdown
**Mise à jour : [Character Name]**

**État psychologique :**
- Phase précédente : [X/5] — [description]
- Phase actuelle : [Y/5] — [description]
- Déclencheur du changement : [what caused the shift]

**Émotions dominantes :**
- Avant : [list emotions]
- Après : [list emotions]

**Croyances modifiées :**
- Avant : [belief about self/world/others]
- Après : [new belief]
- Cause : [what changed their mind]

**Relations affectées :**
| Avec | Avant | Après | Cause |
|------|-------|-------|-------|
| [Character] | [state] | [new state] | [reason] |

**Progression d'arc :**
- Arc défini : [character's defined arc, e.g., "Méfiance → Confiance"]
- Position actuelle : [where they are on this journey]
- Prochaine étape prévue : [what needs to happen next]
```

### Processing Rules

1. **One character at a time** - Complete full update before moving to next
2. **Evidence required** - Every psychological change must cite trigger
3. **Track beliefs** - Note shifts in worldview, not just emotions
4. **Document relationships** - Update all affected relationship entries
5. **Map arc progress** - Position character on their transformation journey

## 4. Add New Characters

For each new character introduced:

### New Character Template

```markdown
**Nouveau personnage : [Name]**

**Profil initial :**
- Rôle : [protagonist/antagonist/support/etc.]
- Phase psychologique : [1/5 typically for new characters]
- Émotions dominantes : [initial emotional state]
- Croyances : [core beliefs]

**Relations initiales :**
| Avec | Nature | Intensité |
|------|--------|-----------|
| [Character] | [type] | [low/medium/high] |

**Arc potentiel :**
- Point de départ : [current state]
- Direction probable : [where they might go]
```

### New Character Rules

- Only create with clear evidence from narrative
- Set initial psychological phase appropriately (usually 1/5)
- Document all initial relationships
- Note potential arc trajectory

## 5. Verify Relationship Consistency

Cross-check that relationships are bidirectional and consistent:

### Consistency Check Template

```markdown
**Vérification de cohérence relationnelle :**

Si [A] → [B] est "tension haute"
Alors [B] → [A] devrait refléter cela

**Incohérences détectées :**
[List any asymmetric relationships]

**Résolutions :**
[How inconsistencies were resolved]
```

### Relationship Consistency Rules

1. **Bidirectionality:** If A→B exists, B→A must exist
2. **Intensity match:** Similar intensity levels (allowing some asymmetry)
3. **Nature alignment:** Relationship types should be compatible
4. **Evidence:** Both directions must have narrative support

**Example of Valid Asymmetry:**
- A→B: "Admiration" (high intensity)
- B→A: "Indifference" (low intensity)
- This is valid if supported by narrative (unrequited feelings)

**Example of Invalid Asymmetry:**
- A→B: "Alliance" (active partnership)
- B→A: "Enemy" (active opposition)
- This is invalid — contradicts narrative logic

## 6. Present Updated Characters

Summarize all changes made:

### Update Summary Template

```markdown
**Mises à jour des personnages effectuées :**

**Changements psychologiques :**
| Personnage | Phase avant | Phase après | Déclencheur |
|------------|-------------|-------------|-------------|
[List changes]

**Relations modifiées :**
| De | Vers | Changement |
|----|------|------------|
[List relationship changes]

**Arcs en progression :**
[List characters with arc movement]
```

## 7. Confirm and Save

### Save Procedure

1. Write updated content to `{bbb_output_folder}/bible/personnes.md`
2. Update file frontmatter:
   ```yaml
   lastUpdated: [current date]
   totalCharacters: [updated count]
   charactersInCrisis: [count at phase 3+]
   ```
3. Update session file:
   ```yaml
   stepsCompleted: ['trigger', 'chronology', 'locations', 'objects', 'characters']
   ```
4. Present menu options
5. Wait for user to confirm or revise

## Related References

- **Psychological Phases:** See `character-phases.md`
- **Format Guide:** See `character-format-guide.md`
- **Session Completion:** See `bible-edit-protocols.md`
