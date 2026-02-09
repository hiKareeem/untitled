# Validation Mode Protocols

## Final Menu Options (Validation Mode)

After completing integrity validation, present this menu to the user:

```
Validation terminée - Que souhaitez-vous faire ?

[R] Relancer la validation (après corrections)
[P] Lancer Party Mode pour discuter d'une issue
[M] Passer en mode Mise à jour pour corriger
[E] Exporter le rapport de validation
[Q] Quitter le workflow
```

### Menu Execution Rules

- ALWAYS halt and wait for user input
- This is the FINAL step of Validate mode — no automatic progression

### Menu Handling Logic

**[R] Relancer:** Re-run validation from beginning
- Action: Return to step 1 (Temporal Coherence Check)
- Use case: User has made corrections and wants to verify

**[P] Party Mode:** Discuss specific issue with multiple perspectives
- Action: Invoke Party Mode with specified issue
- Participants: Timeline Guardian, Cartographer, Archivist, Keeper of Souls, Thematic Weaver
- After discussion: Redisplay menu

**[M] Mise à jour:** Transition to Edit mode to fix issues
- Action: Display "Passage en mode Mise à jour..."
- Load: `../steps-e/step-e-01-trigger.md`
- Begin update workflow to correct identified issues

**[E] Exporter:** Generate validation report file
- Action: Create markdown report at `{bibleFolder}/validation-report-{date}.md`
- Report contents:
  - Executive summary
  - All issues by category
  - Severity breakdown
  - Recommended fixes
  - Party Mode discussions (if any)
- After export: Redisplay menu

**[Q] Quitter:** Exit workflow
- Action: Display "Validation terminée. À bientôt, gardien des histoires !"
- Terminate session

**Any other input:** Help user understand options, then redisplay menu

## Validation Report Template

When user selects [E] Export, generate:

```markdown
# Rapport de Validation - Bible Narrative

**Date:** [YYYY-MM-DD HH:MM]
**Projet:** [Project name]
**Fichiers analysés:** [list all bible files]

---

## Résumé Exécutif

| Catégorie | Vérifications | Issues | Statut |
|-----------|---------------|--------|--------|
| Temporelle | [N] | [N] | ✅/⚠️/❌ |
| Spatiale | [N] | [N] | ✅/⚠️/❌ |
| Objets | [N] | [N] | ✅/⚠️/❌ |
| Personnages | [N] | [N] | ✅/⚠️/❌ |
| Thématique | [N] | [N] | ✅/⚠️/❌ |

**Statut global:** [✅ VALIDE / ⚠️ AVERTISSEMENTS / ❌ ISSUES CRITIQUES]

---

## Issues Critiques

[Issues that must be fixed]

### Issue #1: [Title]
- **Catégorie:** [Temporal/Spatial/Object/Character/Thematic]
- **Description:** [Detailed description]
- **Evidence:**
  - [Dimension A] states: [X]
  - [Dimension B] states: [Y]
- **Suggestion:** [How to fix]
- **Impact:** [What breaks if not fixed]

---

## Avertissements

[Issues that should be addressed]

[Same format as above]

---

## Issues Mineures

[Optional fixes]

[Same format as above]

---

## Recommandations

1. **Priorité immédiate:** [Critical issues to fix first]
2. **À surveiller:** [Warnings to monitor]
3. **Améliorations suggérées:** [Optional enhancements]

---

## Party Mode Discussions

[If Party Mode was invoked]

### Discussion: [Issue Title]
**Participants:** Timeline Guardian, Cartographer, Archivist, Keeper of Souls, Thematic Weaver

**Perspectives:**
- **Timeline Guardian:** [Their view]
- **Cartographer:** [Their view]
- **Archivist:** [Their view]
- **Keeper of Souls:** [Their view]
- **Thematic Weaver:** [Their view]

**Résolution recommandée:** [Consensus solution]

---

*Généré par le Bible Guardian - Système de Validation Living Bible*
```

## Transition Protocols

### From Validation to Edit Mode

When user selects [M] to fix issues:

1. Display transition message: "Passage en mode Mise à jour..."
2. Preserve validation context:
   - Attach validation report to session
   - Flag issues as "to be resolved"
3. Load Edit mode trigger step
4. Begin extraction with validation context

### Re-validation After Corrections

When user selects [R] after making corrections:

1. Clear previous validation results
2. Re-run all 5 coherence checks
3. Compare with previous results:
   - Highlight resolved issues
   - Flag any new issues
   - Note unchanged issues
4. Generate updated report

## Success Criteria

Validation mode is successful when:

**User knows the state of their bible:**
- Clear verdict (VALID/AVERTISSEMENTS/ISSUES CRITIQUES)
- All issues documented with severity
- Recommended fixes provided

**Clear path forward:**
- Options presented for each possible action
- Transitions to other modes work smoothly
- Reports can be exported for reference

**Quality assurance:**
- All 5 check categories executed
- No issues ignored without user consent
- Party Mode available for complex cases

## Related References

- **Integrity Check Definitions:** See `integrity-check-protocols.md`
- **Step Implementation:** See `step-v-02-integrity.md`
- **Edit Mode Protocols:** See `bible-edit-protocols.md`
