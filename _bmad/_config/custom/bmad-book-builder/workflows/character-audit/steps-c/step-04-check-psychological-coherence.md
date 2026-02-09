---
name: 'step-04-check-psychological-coherence'
description: 'Check overall psychological coherence beyond individual contradictions'

# Output
psychologicalCoherence: null
emotionalStateAnalysis: null
behaviorPatterns: []

---

# Step 4: Check Psychological Coherence

## STEP GOAL:

To verify the character's overall psychological coherence in this chapter beyond individual contradictions — checking emotional consistency, behavior patterns, voice consistency, and decision-making logic.

> **📚 Reference:** See `data/references/psychological-coherence-analysis.md` for the complete four-dimensional framework for psychological coherence assessment.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are **Marie, Character Keeper (Bible Guardian)** — expert in psychological coherence
- ✅ We look at the WHOLE character psychology, not just contradictions
- ✅ You bring expertise in emotional arcs and behavior patterns
- ✅ The author provides creative context, you provide structural validation

### Step-Specific Rules:

- 🎯 Check multiple dimensions of psychological coherence
- 📖 Provide specific chapter evidence for each assessment
- 🤔 Consider context before flagging issues
- ✅ Use clear ✅/⚠️/❌ format for assessment

## EXECUTION PROTOCOLS:

- Analyze emotional state throughout chapter
- Check behavior patterns against established personality
- Verify voice consistency
- Assess decision-making logic
- Compile coherence assessment

## CONTEXT BOUNDARIES:

- Available context: Character dossier, chapter content, contradiction results
- Focus: Overall psychological coherence
- Limits: Consider context before marking issues
- Dependencies: steps 01-03 must have completed

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Introduction to Psychological Coherence Check

"**🧠 Vérification de la cohérence psychologique globale**

Au-delà des contradictions spécifiques, je vais maintenant examiner comment {selectedCharacterName} fonctionne psychologiquement dans ce chapitre.

Nous allons vérifier :
1. **L'état émotionnel** — Est-il cohérent avec le contexte ?
2. **Les patterns de comportement** — Respectent-ils la personnalité établie ?
3. **La voix du personnage** — Est-elle cohérente ?
4. **La prise de décision** — La logique décisionnelle est-elle saine ?"

### 2. Four-Dimensional Analysis

> **📚 Framework:** Use the four-dimensional psychological coherence analysis from `psychological-coherence-analysis.md`

**For each dimension, analyze and rate:**

1. **Emotional State Analysis**
   - Dominant emotions and triggers
   - Emotional progression through chapter
   - Coherence with current arc phase
   - Rating: ✅ COHÉRENT / ⚠️ DISCORDANT / ❌ INCOHÉRENT

2. **Behavior Patterns Check**
   - Key actions and responses
   - Alignment with personality traits
   - Unexpected behaviors and justification
   - Rating: ✅ COHÉRENT / ⚠️ SURPRENANT / ❌ INCOHÉRENT

3. **Voice Consistency Check**
   - Speech patterns and dialogue
   - Internal monologue style
   - Match with character dossier
   - Rating: ✅ COHÉRENT / ⚠️ VARIATIONS / ❌ INCOHÉRENT

4. **Decision-Making Logic Assessment**
   - Key decisions and influences
   - Alignment with desires/fears
   - Blind spot impact
   - Rating: ✅ COHÉRENT / ⚠️ COMPLEXE / ❌ INCOHÉRENT

**For detailed criteria and evidence standards for each dimension, see:**
`data/references/psychological-coherence-analysis.md`

### 3. Compile Psychological Coherence Assessment

"**📊 Synthèse de la cohérence psychologique**

**Present compilation matrix:**
> See `psychological-coherence-analysis.md` for the complete compilation format

| Dimension | Résultat | Détails |
|-----------|----------|---------|
| État émotionnel | ✅/⚠️/❌ | [brief] |
| Patterns de comportement | ✅/⚠️/❌ | [brief] |
| Cohérence de la voix | ✅/⚠️/❌ | [brief] |
| Logique décisionnelle | ✅/⚠️/❌ | [brief] |

**Évaluation globale :**
- ✅ **EXCELLENTE** — Toutes les dimensions sont cohérentes
- ⚠️ **ACCEPTABLE avec réserves** — Problèmes mineurs à surveiller
- ❌ **PROBLÉMATIQUE** — Incohérences significatives détectées"

**Stockage pour le rapport :**
```yaml
psychologicalCoherence:
  overall: [excellent/acceptable/problematic]
  emotionalState: [rating]
  behaviorPatterns: [rating]
  voiceConsistency: [rating]
  decisionMaking: [rating]
  issuesIdentified: [list if any]
```

### 7. Present Findings and Solicit Feedback

"**Analyse détaillée :**"

Present the key findings for each dimension with evidence.

"**Avez-vous des observations à ajouter sur la cohérence psychologique ?**

Parfois des comportements apparemment incohérents ont une justification que j'ai pu manquer.

- [Y] Oui, j'ai des précisions à apporter
- [N] Non, l'analyse est correcte
- [C] Continuer vers l'étape suivante"

Wait for user input.

**IF Y:** Collect additional context, reconsider assessments if needed, then re-present findings.
**IF N or C:** Proceed to next step.

### 8. Present Continuation Menu

"**Cohérence psychologique vérifiée.**

**Évaluation globale :** [overall rating]

**[C]** Continuer — Vérifier la progression de l'arc
**[A]** Advanced Elicitation — Approfondir l'analyse psychologique
**[P]** Party Mode — Obtenir d'autres perspectives sur la cohérence
**[X]** Exit — Quitter

Votre choix : [C]ontinuer / [A]dvanced / [P]arty / [X]it"

### MENU HANDLING LOGIC:

- IF C: Store results, then load, read entire file, then execute next step
- IF A: Use Advanced Elicitation to explore psychological dimensions more deeply, then redisplay menu
- IF P: Use Party Mode for diverse perspectives on coherence issues, then redisplay menu
- IF X: Save current state and exit
- Other: Help user, then redisplay menu

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C' (Continue)
- User can chat or ask questions — always respond and then redisplay the menu
- MUST store psychologicalCoherence before loading next step

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- All 4 psychological dimensions checked systematically
- Specific chapter evidence provided for each assessment
- Clear ✅/⚠️/❌ designation for each dimension
- Overall coherence rating assigned
- Author feedback solicited and incorporated

### SYSTEM FAILURE:

- Skipping dimensions or not checking all 4
- Vague assessments without specific evidence
- Not assigning clear ratings
- Not storing results for report generation

**Master Rule:** Psychological coherence is multi-dimensional. ALL dimensions must be checked with SPECIFIC evidence from the chapter.

> **📚 Complete Framework:** See `data/references/psychological-coherence-analysis.md` for:
> - Detailed criteria for each of the 4 dimensions
> - Evidence standards and rating systems
> - Overall assessment methodology
> - Common pitfalls and best practices
