---
name: 'step-e-03-complete'
description: 'Complete the edit session, save changes, and offer validation'

# File References
thisStepFile: './step-e-03-complete.md'
outputFile: '{bbb_output_folder}/chapter-plan-{project_name}.md'
validateStepFile: '../steps-v/step-v-01-validate.md'
---

# Step E-03: Complete Edit Session

## STEP GOAL:

To complete the edit session, update document metadata, save all changes, and offer the user the option to validate the modified structure.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 This is a COMPLETION step
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: Ensure all changes are properly saved
- 📋 YOU ARE A FINALIZER
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Story Architect** — completing renovation
- ✅ Ensure changes are saved and documented
- ✅ Offer quality assurance (validation)
- ✅ Provide clear next steps

### Step-Specific Rules:

- 🎯 Focus ONLY on completion and saving
- 🚫 FORBIDDEN to make additional edits
- 💬 Prescriptive approach: save and document
- 🎉 Acknowledge the work done

## EXECUTION PROTOCOLS:

- 🎯 Update document metadata
- 💾 Ensure all changes are saved
- 📖 Document edit session in frontmatter
- 🔍 Offer validation as next step

## CONTEXT BOUNDARIES:

- All edits from step e-02 have been applied
- Document is in modified state
- Focus: Finalization and quality assurance options

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Update Document Metadata

Update {outputFile} frontmatter:

```yaml
---
# Add/update these fields
lastEditDate: [current date]
editHistory:
  - date: [current date]
    changes: [brief summary of edits made]
version: [increment version number, e.g., 1.0 → 1.1]
status: EDITED  # or maintain FINALIZED if minor edits
---
```

### 2. Add Edit Session Note

If significant edits were made, add a note to the document:

```markdown
---

## Historique des Modifications

### [current date]
- [Edit 1 summary]
- [Edit 2 summary]
- [Edit 3 summary]

---
```

### 3. Save Confirmation

"**Modifications sauvegardées !** 💾

**Résumé de la session d'édition :**
- Document : [story_title]
- Version : [new version number]
- Modifications appliquées : [count]
- Date : [current date]

Votre plan de chapitres a été mis à jour avec succès."

### 4. Offer Validation

"**Souhaitez-vous valider votre plan modifié ?**

La validation vérifiera :
- ✓ Complétude de la structure (phases, transitions)
- ✓ Conformité au framework ([framework name])
- ✓ Arc du personnage (transformation trackée)
- ✓ Cohérence narrative (fils narratifs, enjeux)
- ✓ Niveau de détail (actionnabilité)

**[V]** Valider le plan maintenant
**[L]** Terminer sans validation (vous pourrez valider plus tard)"

### 5. Present MENU OPTIONS

Display: **Session d'édition terminée - Sélectionnez une option:**
- **[V]** Valider le plan modifié
- **[L]** Terminer la session

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- Route based on user choice

#### Menu Handling Logic:

- **IF V:** Load, read entire file, then execute {validateStepFile} to validate the plan
- **IF L:** Proceed to closing message (step 6)
- **IF Any other:** help user respond, then redisplay menu

### 6. Closing Message

"**Session d'édition terminée.** ✓

Votre plan de chapitres modifié est sauvegardé à :
`{outputFile}`

**Prochaines options :**
- Lancez **Foundation -v** pour valider le plan
- Lancez **Foundation -e** pour d'autres modifications
- Lancez **chapter-write** pour commencer à écrire

Bonne continuation !"

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Document metadata updated (version, editDate)
- Edit history documented
- Changes confirmed as saved
- Validation option offered
- Clear next steps provided
- Session properly closed

### ❌ SYSTEM FAILURE:

- Not updating version number
- Not documenting edit history
- Making additional edits (that was step e-02)
- Not offering validation option
- Leaving session in ambiguous state

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

This is the FINAL STEP of Edit Mode. The session is complete when user selects 'L', or transitions to Validate Mode if 'V' selected.
