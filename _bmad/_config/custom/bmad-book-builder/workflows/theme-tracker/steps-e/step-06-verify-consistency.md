---
name: 'step-06-verify-consistency'
description: 'Verify thematic coherence with previous chapters and report findings'
---

# Step 6: Verify Consistency (Final)

## STEP GOAL:

To verify that the thematic tracking remains coherent across chapters and provide a final report with any red flags or concerns.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 THIS IS THE FINAL STEP - provide comprehensive verification
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE VERIFYING coherence and flagging concerns
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Thematic Weaver** - ensuring narrative coherence
- ✅ Compare this chapter's tracking against the full history
- ✅ Flag issues but don't alarm - some may be intentional
- ✅ Provide actionable insights, not just problems

### Step-Specific Rules:

- 🎯 Focus on CROSS-CHAPTER coherence
- 🚫 FORBIDDEN to modify any files in this step
- 💬 Approach: Quality assurance with constructive feedback

## EXECUTION PROTOCOLS:

- 🎯 Load all tracking files for comparison
- 💾 Generate verification report (display only, don't save separately)
- 📖 Identify patterns, concerns, and recommendations
- 🚫 This is read-only verification

## CONTEXT BOUNDARIES:

- Available: All tracking files, chapter analysis files
- Focus: Coherence verification
- Limits: Analysis and reporting only
- Dependencies: Steps 01-05 completed

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise.

### 1. Load Tracking History

"**Vérification de cohérence - Post Chapitre {chapterNumber}**

Chargement de l'historique de tracking..."

Load:
- themes.md (full file)
- emotions.md (full file)
- Previous chapter-XX-themes.md files (if they exist)

### 2. Verify Theme Continuity

"**Vérification de la continuité thématique...**"

For EACH theme in themes.md:

**Check progression logic:**
- Does the Per-Chapter Progression table show logical flow?
- Are there unexplained gaps (chapters where theme should appear but doesn't)?
- Does the progression match the Progression by Chapter Phase?

**Flag issues:**
- 🟡 **Attention :** [Theme] hasn't appeared in [N] chapters
- 🔴 **Problème :** [Theme] progression contradicts phase plan
- ✅ **OK :** [Theme] tracking is coherent

### 3. Verify Character Emotional Arcs

"**Vérification des arcs émotionnels...**"

For EACH character in emotions.md:

**Check emotional continuity:**
- Do chapter-to-chapter emotional states make sense?
- Are there unexplained emotional jumps?
- Does the Per-Chapter Beats table show growth/change?

**Flag issues:**
- 🟡 **Attention :** [Character] shows no emotional change in [N] chapters
- 🔴 **Problème :** [Character] emotional state inconsistent (was X, suddenly Y)
- ✅ **OK :** [Character] arc is coherent

### 4. Cross-Reference Themes and Characters

"**Vérification des connexions personnage-thème...**"

Check Character Connections in themes.md against actual chapter data:
- Are claimed connections supported by chapter analyses?
- Are there characters engaging with themes not listed in connections?

**Flag issues:**
- 🟡 **Attention :** [Character] engages with [Theme] but not listed in connections
- ✅ **OK :** Connections match chapter evidence

### 5. Compile Red Flags Summary

"**══════════════════════════════════════════════════════════════════**
**RAPPORT DE VÉRIFICATION - Chapitre {chapterNumber}**
**══════════════════════════════════════════════════════════════════**"

**Organize by severity:**

```markdown
## 🔴 Problèmes à traiter

[List critical issues that likely need addressing]
- [Issue 1 with explanation]
- [Issue 2 with explanation]

Or: "Aucun problème critique détecté."

## 🟡 Points d'attention

[List items that might need attention but aren't critical]
- [Item 1 with context]
- [Item 2 with context]

Or: "Aucun point d'attention particulier."

## ✅ Vérifications réussies

- Continuité thématique : [OK / N issues]
- Arcs émotionnels : [OK / N issues]
- Connexions personnage-thème : [OK / N issues]
```

### 6. Provide Recommendations

"**Recommandations pour les prochains chapitres :**"

Based on the analysis:

1. **Thèmes à développer :**
   - [Theme] is due for progression based on phase plan
   - [Theme] hasn't had focus recently

2. **Personnages à surveiller :**
   - [Character] arc needs movement
   - [Character] emotional state needs resolution

3. **Questions ouvertes :**
   - [Question raised by the narrative that should be addressed]

### 7. Present Final Summary

"**══════════════════════════════════════════════════════════════════**
**ANALYSE THÉMATIQUE TERMINÉE - Chapitre {chapterNumber}**
**══════════════════════════════════════════════════════════════════**

**Résumé de l'analyse :**

| Métrique | Valeur |
|----------|--------|
| Thèmes suivis | [N] |
| Thèmes actifs ce chapitre | [N] |
| Personnages suivis | [N] |
| Beats émotionnels ce chapitre | [N] |
| Red flags détectés | [N] |

**Fichiers mis à jour :**
- ✅ tracking/themes.md
- ✅ tracking/emotions.md
- ✅ tracking/chapter-{chapterNumber}-themes.md

**Santé thématique globale :** [Excellente / Bonne / À surveiller / Préoccupante]

---

**Le suivi thématique du chapitre {chapterNumber} est terminé.**

Pour analyser le prochain chapitre, relancez le workflow theme-tracker."

### 8. Workflow Complete

This is the FINAL STEP. No menu needed.

The workflow is complete. User can:
- Review the tracking files
- Run the workflow again for the next chapter
- Address any red flags raised

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All tracking files verified for coherence
- Theme continuity checked
- Character arcs verified
- Red flags clearly categorized
- Recommendations provided
- Final summary presented
- Workflow completes cleanly

### ❌ SYSTEM FAILURE:

- Not checking all tracking files
- Missing coherence issues
- Not providing recommendations
- Leaving workflow in incomplete state
- Modifying files in this step

**Master Rule:** Verify thoroughly. Report clearly. Complete cleanly.
