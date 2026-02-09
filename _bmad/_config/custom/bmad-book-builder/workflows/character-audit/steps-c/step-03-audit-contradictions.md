---
name: 'step-03-audit-contradictions'
description: 'Check each contradiction against character behavior in the chapter'

# Output
contradictionsChecked: []
contradictionsResults: []

# Audit Data
chapterContent: null
characterContradictions: []
---

# Step 3: Audit Contradictions

## STEP GOAL:

To systematically check each of the character's established contradictions against their behavior in this chapter, marking each as ✅ COHÉRENT or ❌ INCOHÉRENT with specific evidence.

> **📚 Reference:** See `data/references/contradiction-audit-framework.md` for the complete methodology based on AgentAdam's approach to character psychology auditing.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are **Marie, Character Keeper (Bible Guardian)** — expert in psychological consistency
- ✅ We systematically verify each contradiction with evidence from the chapter
- ✅ You bring expertise in character psychology and narrative analysis
- ✅ The author provides creative context, you provide structural validation

### Step-Specific Rules:

- 🎯 Check EVERY contradiction in the character's profile (minimum 5)
- 📖 Provide SPECIFIC chapter evidence for each check
- ✅ Use ✅/❌ format for clear designation
- 🤔 When in doubt, discuss with author before marking

## EXECUTION PROTOCOLS:

- Load character contradictions from dossier
- Load chapter content
- For each contradiction: analyze chapter behavior, check coherence, mark result
- Store results for report generation
- Present findings to user for confirmation

## CONTEXT BOUNDARIES:

- Available context: Character dossier, chapter content
- Focus: Contradiction-by-contradiction verification
- Limits: Only mark as incoherent with clear evidence
- Dependencies: steps 01-02 must have selected character and chapter

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Contradictions from Character Dossier

"**📋 Chargement des contradictions de {selectedCharacterName}...**"

From the character dossier, extract the **Contradictions internes** section:

Store as `characterContradictions` array:
```yaml
contradictions:
  - type: [Valeurs vs Actions / Image de soi vs Réalité / etc.]
    description: [full description]
    examples: [story examples if available]
```

**Verify minimum 5 contradictions:**
- IF < 5: "⚠️ Attention : Seulement [N] contradictions identifiées. La norme AgentAdam recommande 5+ contradictions pour une profondeur psychologique complète."
- Proceed anyway but note this in audit

### 2. Load Chapter Content

"**📖 Analyse du Chapitre {selectedChapterNumber}...**"

Load full chapter content from `{selectedChapterFile}`

Identify:
- All scenes involving `{selectedCharacterName}`
- Key actions taken by the character
- Dialogue spoken by the character
- Internal monologue (if present)
- Decisions made
- Emotional responses

### 3. Systematic Contradiction Checking

"**🔍 Vérification systématique des contradictions**

Je vais maintenant vérifier chacune des [N] contradictions de {selectedCharacterName} contre son comportement dans ce chapitre."

For EACH contradiction in `characterContradictions`:

> **📚 Framework:** Use the systematic verification process from `contradiction-audit-framework.md`
> - Check each contradiction individually with ✅/❌/⚪ designation
> - Provide specific chapter evidence for each assessment
> - Consider context before marking incoherent

**Analysis format for each contradiction:**
- Description: [from dossier]
- Chapter behavior: [what character does/says/thinks]
- Coherence check: [alignment with contradiction]
- Conclusion: ✅ COHÉRENT / ❌ INCOHÉRENT / ⚪ NON APPLICABLE
- Evidence: [specific chapter references]

**Work through EACH contradiction systematically:**
> See `contradiction-audit-framework.md` for rating criteria and evidence standards

### 4. Compile Results

"**📊 Résultats de l'audit des contradictions**

| Contradiction | Type | Résultat |
|--------------|------|----------|
| 1. [description] | [Type] | ✅/❌/⚪ |
| 2. [description] | [Type] | ✅/❌/⚪ |
| 3. [description] | [Type] | ✅/❌/⚪ |
| 4. [description] | [Type] | ✅/❌/⚪ |
| 5. [description] | [Type] | ✅/❌/⚪ |

**Synthèse :**
- ✅ Cohérentes : [X]/[N]
- ❌ Incohérentes : [Y]/[N]
- ⚪ Non applicables : [Z]/[N]"

**Store results for report:**
```yaml
contradictionsChecked: [N]
contradictionsCoherent: [X]
contradictionsIncoherent: [Y]
contradictionsNA: [Z]
contradictionsResults:
  - contradiction: [description]
    type: [type]
    result: [coherent/incoherent/na]
    evidence: [specific chapter evidence]
    analysis: [brief explanation]
```

### 5. Present Findings

"**🔍 Analyse détaillée**

**Contradictions COHÉRENTES ✅ :**
- [List each with brief explanation]

**Contradictions INCOHÉRENTES ❌ :**
- [List each with explanation of the problem]
- [If none: "Aucune incohérence détectée !"]

**Contradictions NON TESTÉES ⚪ :**
- [List contradictions not relevant to this chapter]

**Problèmes potentiels :**
- [If any incoherent: Discuss what this means for character consistency]
- [If none: "La cohérence psychologique est maintenue dans ce chapitre."]"

### 6. Solicit Author Feedback

"**Avez-vous des observations à ajouter ?**

Parfois un comportement apparemment incohérent a une justification contextuelle que j'ai pu manquer.

- [Y] Oui, j'ai des précisions à apporter
- [N] Non, l'analyse est correcte
- [C] Continuer vers l'étape suivante"

Wait for user input.

**IF Y:**
"Quelles précisions souhaitez-vous ajouter ?"
Collect additional context, reconsider specific contradictions if needed, then re-present findings.

**IF N or C:**
Proceed to next step.

### 7. Present Continuation Menu

"**Audit des contradictions terminé.**

**Résultat global :** [X]/[N] contradictions cohérentes

**[C]** Continuer — Vérifier la cohérence psychologique globale
**[A]** Advanced Elicitation — Approfondir l'analyse des contradictions
**[P]** Party Mode — Obtenir d'autres perspectives sur les incohérences
**[X]** Exit — Quitter

Votre choix : [C]ontinuer / [A]dvanced / [P]arty / [X]it"

### MENU HANDLING LOGIC:

- IF C: Store results, then load, read entire file, then execute next step
- IF A: Use Advanced Elicitation to explore contradictions more deeply, then redisplay menu
- IF P: Use Party Mode for diverse perspectives on problematic contradictions, then redisplay menu
- IF X: Save current state and exit
- Other: Help user, then redisplay menu

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C' (Continue)
- User can chat or ask questions — always respond and then redisplay the menu
- MUST store contradictionsResults before loading next step

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- ALL contradictions checked systematically (minimum 5)
- Specific chapter evidence provided for each check
- Clear ✅/❌/⚪ designation for each contradiction
- Results compiled and stored
- Author feedback solicited and incorporated

### SYSTEM FAILURE:

- Skipping contradictions (not checking all)
- Vague assessments without specific evidence
- Not marking results clearly
- Not storing results for report generation

**Master Rule:** EVERY contradiction must be checked with SPECIFIC evidence from the chapter. This is the foundation of psychological consistency auditing.

> **📚 Complete Methodology:** See `data/references/contradiction-audit-framework.md` for:
> - Detailed contradiction types and patterns
> - Evidence standards and rating criteria
> - Scoring formulas and best practices
> - Common pitfalls to avoid
