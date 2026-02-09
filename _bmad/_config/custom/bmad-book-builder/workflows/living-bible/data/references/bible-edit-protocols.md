# Bible Edit Protocols

## Final Menu Options (Edit Mode)

After completing all dimension updates in Edit mode, present this menu to the user:

```
Mise à jour terminée - Que souhaitez-vous faire ?

[R] Réviser les modifications des thèmes
[V] Lancer une Validation de cohérence
[M] Faire une autre Mise à jour
[Q] Quitter le workflow
```

### Menu Execution Rules

- ALWAYS halt and wait for user input
- This is the FINAL step of Edit mode — no automatic progression

### Menu Handling Logic

**[R] Réviser:** Return to theme update processing to revise changes
- Action: Return to step 3 (Process Theme Updates)
- User can make additional changes before final save

**[V] Validation:** Transition to Validate mode
- Action: Display "Passage en mode Validation..."
- Load: `../steps-v/step-v-01-load.md`
- Begin integrity checking workflow

**[M] Mise à jour:** Start new edit session
- Action: Display "Nouvelle session de mise à jour..."
- Load: `./step-e-01-trigger.md`
- Begin new extraction and update cycle

**[Q] Quitter:** Exit workflow
- Action: Display closing message: "La Bible Narrative est à jour. À bientôt, gardien des histoires !"
- Terminate session

**Any other input:** Help user understand options, then redisplay menu

## Session Completion Protocol

### Update Session File

When Edit mode completes successfully, update the session file:

```yaml
status: complete
stepsCompleted:
  - trigger
  - chronology
  - locations
  - objects
  - characters
  - themes
completedAt: [current datetime ISO 8601]
```

Location: `{bbb_output_folder}/bible/.update-session.yaml`

### Final Update Summary

Generate a comprehensive summary of all changes:

```markdown
**✅ MISE À JOUR DE LA BIBLE TERMINÉE**

**Récapitulatif de cette session :**

| Dimension | Modifications |
|-----------|--------------|
| Chronologie | [summary of changes] |
| Lieux | [summary of changes] |
| Objets | [summary of changes] |
| Personnages | [summary of changes] |
| Thèmes | [summary of changes] |

**Bible narrative mise à jour avec succès !**

Tous les fichiers ont été sauvegardés dans {bibleFolder}/

*La mémoire de votre histoire est à jour. Rien n'a été oublié.*
```

## File Update Protocols

### Frontmatter Updates

Each dimension file should have its frontmatter updated:

```yaml
lastUpdated: [current date YYYY-MM-DD]
total[Dimension]s: [updated count]
[dimension]InCrisis: [count at phase 3, if applicable]
```

Example for themes:
```yaml
lastUpdated: 2025-01-15
totalThemes: 12
themesInCrisis: 3
```

### Save Verification

Before marking step complete:
1. Verify file write was successful
2. Confirm frontmatter updated
3. Check session file updated
4. Present summary to user
5. Only then mark complete and offer menu options

## Related References

- **Dimension-Specific Procedures:** See individual dimension reference files
- **Validation Mode:** See `validation-protocols.md`
- **Session Management:** See workflow-level session documentation
