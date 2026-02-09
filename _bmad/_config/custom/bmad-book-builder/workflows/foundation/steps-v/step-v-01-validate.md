---
name: 'step-v-01-validate'
description: 'Validate an existing chapter plan against structure, framework, and quality standards'

# File References
thisStepFile: './step-v-01-validate.md'
chapterPlanPattern: '{bbb_output_folder}/chapter-plan*.md'
validationReportFile: '{bbb_output_folder}/validation-report-{project_name}.md'

# Framework Data
saveTheCatData: '../data/save-the-cat.md'
herosJourneyData: '../data/heros-journey.md'
snowflakeMethodData: '../data/snowflake-method.md'
customFrameworkData: '../data/custom-framework.md'
methodeVareilleData: '../data/vareille-method.md'

# Reference to edit mode
editStepFile: '../steps-e/step-e-01-assess.md'
---

# Step V-01: Validate Chapter Plan

## STEP GOAL:

To perform a comprehensive validation of an existing chapter plan, checking structure completeness, framework compliance, character arcs, narrative coherence, and actionability — then providing a detailed report with recommendations.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 This is an ASSESSMENT step — no modifications
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: Run ALL 5 validation checks
- 📋 YOU ARE A QUALITY REVIEWER
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Story Architect** — in inspector mode
- ✅ Be thorough but constructive
- ✅ Identify issues AND suggest solutions
- ✅ Celebrate what works well

### Step-Specific Rules:

- 🎯 Focus ONLY on validation — no modifications
- 🚫 FORBIDDEN to change the document
- 💬 Analytical approach: systematic quality review
- 📊 Generate structured validation report

## EXECUTION PROTOCOLS:

- 🎯 Load and analyze chapter plan systematically
- 💾 Generate validation report
- 📖 Score each validation dimension
- 🚫 FORBIDDEN to modify the source document

## CONTEXT BOUNDARIES:

- User has invoked Validate mode
- Chapter plan exists and needs review
- Focus: Quality assessment only

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Locate and Load Chapter Plan

If chapter plan path was not provided:

"**Mode Validation activé.** 🔍

Quel plan de chapitres souhaitez-vous valider ?"

Look for files matching `{chapterPlanPattern}` and present options.

Load the complete chapter plan file.

### 2. Initialize Validation

"**Validation en cours : [story_title]** 📋

Je vais analyser votre plan selon 5 critères :
1. Complétude structurelle
2. Conformité au framework
3. Arc du personnage
4. Cohérence narrative
5. Actionnabilité

Analyse en cours..."

### 3. Run 5 Validation Checks

#### CHECK 1: Structure Completeness

**Verify presence of:**
- [ ] Story concept (title, logline, premise)
- [ ] Framework selection and rationale
- [ ] Character section (protagonist, antagonist, secondary)
- [ ] World section (setting, rules, atmosphere)
- [ ] Themes & stakes section
- [ ] Phase structure (all phases defined)
- [ ] Phase details (objectives, conflicts, transitions for each)
- [ ] 3-act mapping
- [ ] Parallel narrative threads
- [ ] Pacing analysis

**Score: [X]/10**

**Issues found:**
- [List any missing or incomplete sections]

**Recommendations:**
- [Specific suggestions to address issues]

---

#### CHECK 2: Framework Compliance

Load the appropriate framework data based on `framework` in frontmatter.

**Verify:**
- [ ] All framework beats/stages are mapped to phases
- [ ] Beat placement follows recommended timing
- [ ] No critical beats are missing
- [ ] Framework principles are honored

**Score: [X]/10**

**Framework: [framework name]**

**Beat Coverage:**
| Beat/Stage | Present | Phase | Notes |
|------------|---------|-------|-------|
| [Beat 1] | ✓/✗ | [Phase N] | [any issues] |
| [Beat 2] | ✓/✗ | [Phase N] | [any issues] |
| ... | | | |

**Issues found:**
- [List framework compliance issues]

**Recommendations:**
- [Specific suggestions to improve compliance]

---

#### CHECK 3: Character Arc

**Verify protagonist transformation:**
- [ ] Clear starting state (flaw, lie, want)
- [ ] Visible evolution through phases
- [ ] Transformation arc is tracked
- [ ] End state is different from start
- [ ] Arc connects to theme

**Verify antagonist/opposition:**
- [ ] Clear motivation
- [ ] Present throughout relevant phases
- [ ] Creates meaningful obstacles

**Score: [X]/10**

**Arc Analysis:**
- Start state: [description]
- Midpoint shift: [description]
- End state: [description]
- Transformation clear: Yes/No

**Issues found:**
- [List character arc issues]

**Recommendations:**
- [Specific suggestions to strengthen arcs]

---

#### CHECK 4: Narrative Coherence

**Verify:**
- [ ] Parallel threads are tracked consistently
- [ ] Stakes escalate appropriately
- [ ] Transitions between phases are logical
- [ ] Tone is consistent (or intentionally varied)
- [ ] Themes are woven throughout
- [ ] No plot holes or contradictions

**Score: [X]/10**

**Thread Analysis:**
| Thread | Phases Active | Consistent | Notes |
|--------|---------------|------------|-------|
| [A] | [X, Y, Z] | ✓/✗ | |
| [B] | [X, Y, Z] | ✓/✗ | |

**Escalation Check:**
- Phase 1 → 2: [Stakes increase described]
- Phase 2 → 3: [Stakes increase described]
- ...

**Issues found:**
- [List coherence issues]

**Recommendations:**
- [Specific suggestions to improve coherence]

---

#### CHECK 5: Actionability

**Verify the plan is ready for writing:**
- [ ] Each phase has enough detail to start writing
- [ ] Key scenes are identified (not just vague descriptions)
- [ ] Character voices/actions are suggested
- [ ] Emotional beats are clear
- [ ] Author could write Chapter 1 from this plan

**Score: [X]/10**

**Readiness Assessment:**
- Detail level: [Sparse / Adequate / Rich]
- Scene clarity: [Vague / Clear / Vivid]
- Writing-ready: Yes / Needs more detail

**Issues found:**
- [List actionability issues]

**Recommendations:**
- [Specific suggestions to improve actionability]

---

### 4. Generate Overall Score

**Calculate overall validation score:**

| Check | Score | Weight | Weighted |
|-------|-------|--------|----------|
| Structure Completeness | /10 | 20% | |
| Framework Compliance | /10 | 20% | |
| Character Arc | /10 | 25% | |
| Narrative Coherence | /10 | 20% | |
| Actionability | /10 | 15% | |
| **TOTAL** | | | **/10** |

**Overall Rating:**
- 9-10: ⭐⭐⭐⭐⭐ Excellent — Ready to write
- 7-8: ⭐⭐⭐⭐ Good — Minor improvements suggested
- 5-6: ⭐⭐⭐ Adequate — Some work needed
- 3-4: ⭐⭐ Needs Work — Significant gaps
- 1-2: ⭐ Incomplete — Major revision needed

### 5. Present Validation Report

"**Rapport de Validation : [story_title]** 📊

**Score Global : [X]/10** [star rating]

**Résumé :**
[2-3 sentence summary of overall quality]

**Points Forts :**
- [Strength 1]
- [Strength 2]
- [Strength 3]

**Points à Améliorer :**
- [Issue 1] — [Brief recommendation]
- [Issue 2] — [Brief recommendation]
- [Issue 3] — [Brief recommendation]

**Verdict :**
[PRÊT À ÉCRIRE / QUELQUES AJUSTEMENTS RECOMMANDÉS / RÉVISION NÉCESSAIRE]"

### 6. Save Validation Report

Create {validationReportFile} with complete validation details:

```markdown
---
title: Validation Report
story_title: [title]
validated_date: [current date]
overall_score: [X]/10
verdict: [READY / ADJUSTMENTS / REVISION]
---

# Rapport de Validation : [story_title]

[Complete validation report with all 5 checks detailed]
```

### 7. Present MENU OPTIONS

Display: **Validation terminée - Sélectionnez une option:**
- **[D]** Voir le rapport détaillé
- **[E]** Passer en mode Édition pour corriger les problèmes
- **[T]** Terminer

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- Route based on user choice

#### Menu Handling Logic:

- **IF D:** Display full validation report, then redisplay menu
- **IF E:** Load {editStepFile} to enter edit mode
- **IF T:** Proceed to closing message
- **IF Any other:** help user respond, then redisplay menu

### 8. Closing Message

"**Validation terminée.** ✓

Votre rapport de validation est sauvegardé à :
`{validationReportFile}`

**Prochaines étapes suggérées :**
[Based on verdict - specific recommendations]

Bonne continuation avec votre histoire !"

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All 5 validation checks completed
- Each check has score, issues, recommendations
- Overall score calculated correctly
- Report is constructive (not just critical)
- Validation report saved
- Clear next steps based on verdict

### ❌ SYSTEM FAILURE:

- Skipping any of the 5 checks
- Modifying the source document
- Being overly critical without recommendations
- Not generating validation report
- Giving inaccurate scores

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

This is a STANDALONE validation step. The session completes when user selects 'T', or transitions to Edit Mode if 'E' selected.
