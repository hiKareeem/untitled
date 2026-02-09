---
name: 'step-06-generate-report'
description: 'Generate comprehensive audit report with all findings and recommendations'

# Output
auditReport: null
auditFile: null

# Report Data Collection
allFindings: {}
finalAssessment: null
recommendations: []
---

# Step 6: Generate Report

## STEP GOAL:

To compile all audit findings into a comprehensive, formatted report following AgentAdam's audit format, providing actionable insights and recommendations.

> **📚 Reference:** See `data/templates/audit-report-template.md` for the complete report structure and `data/references/` frameworks for methodology details.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are **Marie, Character Keeper (Bible Guardian)** — producing professional audit reports
- ✅ The report is a deliverable that will inform future revisions
- ✅ You bring expertise in synthesizing complex psychological data
- ✅ The author reviews the report for final approval

### Step-Specific Rules:

- 📄 Generate a complete, well-formatted markdown report
- 📊 Include ALL findings from previous steps
- ✅ Use clear ✅/❌ format throughout
- 💡 Provide actionable recommendations

## EXECUTION PROTOCOLS:

- Compile all data from previous steps
- Format according to AgentAdam audit template
- Calculate final assessment scores
- Generate recommendations based on findings
- Write report to audit file
- Present summary to user

## CONTEXT BOUNDARIES:

- Available context: All data from steps 01-05
- Focus: Report compilation and formatting
- Limits: Report only what was analyzed — no new analysis
- Dependencies: steps 01-05 must have completed

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Compile All Findings and Calculate Assessment

"**📋 Compilation de toutes les découvertes et calcul de l'évaluation...**"

> **📚 Template:** See `audit-report-template.md` for complete data compilation and assessment calculation methodology

**Gather data from all previous steps:**
- Character info (step 01)
- Chapter info (step 02)
- Contradictions results (step 03)
- Psychological coherence (step 04)
- Arc progression (step 05)

**Calculate final assessment:**
> Use the scoring formulas and rating criteria from `audit-report-template.md`

**Scores:**
- Contradictions: (Coherent / Total Checked) × 100
- Psychological: Based on 4 dimensions
- Arc: Based on alignment designation
- Overall: Combine all three scores

**Storage format:**
```yaml
finalAssessment:
  contradictionsScore: [X]%
  psychologicalScore: [rating]
  arcScore: [rating]
  overall: [excellent/acceptable/problematic]
  criticalIssues: [count]
  issuesList: [detailed list]
```

### 2. Generate Recommendations

"**💡 Génération des recommandations...**"

> **📚 Template:** Use the recommendation generation guidelines from `audit-report-template.md`

**Based on findings, generate specific recommendations:**
- For incoherent contradictions: scene-specific suggestions
- For problematic psychological dimensions: concrete improvements
- For arc regression: justification or alternatives
- For excellent results: maintenance guidance

**Storage format:**
```yaml
recommendations:
  - priority: [high/medium/low]
    issue: [description]
    suggestion: [actionable recommendation]
```

### 3. Generate Report File

"**📄 Génération du rapport d'audit...**"

> **📚 Template:** Use the complete report structure from `audit-report-template.md`

**Create the audit report file at `{auditFile}`:**
- Follow the exact template format
- Include all sections: Apparition, Cohérence Psychologique, Évolution de l'Arc, Problèmes, Recommandations, Évaluation Globale
- Populate with data from previous steps
- Ensure all findings are included

### 4. Write Report to File and Present Summary

**Write the complete report to:**
`{bbb_output_folder}/audits/audit-chapter-{chapter_number}-{selectedCharacterSlug}.md`

**Verify file creation:**
- ✅ Report file created
- ✅ All sections populated
- ✅ All findings included

**Present summary to user:**
> Use the summary presentation format from `audit-report-template.md`

"**✅ Rapport d'audit généré !**

**Fichier :** `audit-chapter-{chapter_number}-{selectedCharacterSlug}.md`
**Emplacement :** `{bbb_output_folder}/audits/`

---

## 📊 Résumé de l'audit

**Personnage :** {selectedCharacterName}
**Chapitre :** {selectedChapterNumber}

**Contradictions vérifiées :** {totalChecked}
- ✅ Cohérentes : {coherent}/{totalChecked}
- ❌ Incohérentes : {incoherent}/{totalChecked}

**Cohérence psychologique :** {psychologicalScore}
**Progression de l'arc :** {arcScore}

**Évaluation finale :** {finalAssessment.overall}

{IF criticalIssues > 0:}
**⚠️ Problèmes identifiés :** {criticalIssues}
Voir le rapport complet pour les détails.

{ELSE:}
**✅ Aucun problème critique !**

---

## Recommandations Rapides

{Top 2-3 recommendations brief}

---

**Que souhaitez-vous faire ?**

- **[V]**oir le rapport complet
- **[R]**éviser le chapitre (si problèmes détectés)
- **[A]**utre audit (autre personnage/chapitre)
- **[X]** Exit

Votre choix : [V]iew / [R]evise / [A]nother / [X]it"

### MENU HANDLING LOGIC:

- IF V: Display the full report content, then redisplay menu
- IF R: Suggest using chapter-write workflow in edit mode with specific guidance from audit
- IF A: Ask what to audit next, restart workflow from step 01
- IF X: Save final state and exit workflow
- Other: Help user, then redisplay menu

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- User can chat or ask questions — always respond and then redisplay the menu
- Report is FINAL交付品 — should be preserved

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- All findings compiled from previous steps
- Report formatted according to AgentAdam template
- Final assessment calculated with clear criteria
- Recommendations generated based on findings
- Report file written to disk
- Summary presented to user

### SYSTEM FAILURE:

- Missing findings from previous steps
- Report not formatted correctly
- No final assessment calculated
- Report file not written
- Summary not presented

**Master Rule:** The audit report is the primary deliverable of this workflow. It must be complete, well-formatted, and actionable. Authors will use this report to understand their character's psychological state and make informed revision decisions.

> **📚 Complete Template and Guidelines:** See `data/templates/audit-report-template.md` for:
> - Complete report structure and formatting
> - Data compilation methodology
> - Assessment calculation formulas
> - Critical issue identification criteria
> - Recommendation generation guidelines
> - File output verification standards
