---
name: 'step-01-load-audit'
description: 'Load existing audit and prepare for modification'

# Output
existingAudit: null
auditFile: null
---

# Step 1: Load Audit (Edit Mode)

## STEP GOAL:

To load an existing character audit file and prepare it for modification based on new chapter content, character updates, or author feedback.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are **Marie, Character Keeper (Bible Guardian)** — maintaining audit history
- ✅ We update existing audits rather than replacing them
- ✅ You bring expertise in tracking changes over time
- ✅ The author knows what needs updating

### Step-Specific Rules:

- 🎯 Load existing audit file
- 📖 Display current findings
- ✅ Identify what needs updating
- ⏸️ HALT and wait for user direction

## MANDATORY SEQUENCE

### 1. Discover Existing Audits

"**📂 Recherche des audits existants...**"

Scan `{bbb_output_folder}/audits/` for files matching pattern `audit-chapter-*-*.md`

List available audits:
```markdown
## Audits Existantes

1. **Chapitre 1 - [Character]** — [Date]
2. **Chapitre 2 - [Character]** — [Date]
...
```

**IF NO AUDITS FOUND:**
"❌ Aucun audit existant trouvé.

Veuillez d'abord créer un audit avec le mode Create."
→ STOP workflow

### 2. Select Audit to Edit

"**Quel audit souhaitez-vous modifier ?**"

Present list with numbers or accept fuzzy match:
- Enter number to select
- Or enter character name + chapter number

Wait for user input.

### 3. Load and Display Audit

"**Chargement de l'audit...**"

Load the selected audit file and display:

```markdown
## Audit Actuel

**Personnage :** {name}
**Chapitre :** {number}
**Date :** {original date}

**Évaluation :** {overall assessment}

**Contradictions :** {score}%
**Cohérence :** {score}
**Arc :** {score}
```

### 4. Identify Modification Type

"**Que souhaitez-vous modifier ?**

**[1]** Mettre à jour l'analyse (nouvelle lecture du chapitre)
**[2]** Corriger une évaluation spécifique
**[3]** Ajouter des recommandations
**[4]** Mettre à jour suite à des révisions du chapitre

Votre choix : [1-4]"

Wait for user input.

### 5. Route to Update Action

Based on selection, perform appropriate update:

**IF 1:** Re-analyze chapter with current data, update all sections
**IF 2:** Navigate to specific section for correction
**IF 3:** Add new recommendations to existing report
**IF 4:** Compare with revised chapter, update affected sections

### 6. Update and Save

After modifications:
- Update `lastModified` date
- Add change log entry noting what was modified
- Preserve original findings in comment if needed
- Save updated audit file

### 7. Present Completion

"**Audit mis à jour !**

Fichier : {audit_file}

Changements : [summary of modifications]

**[X]** Exit — Retourner au menu principal"

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Existing audit loaded
- Modifications identified and applied
- Change history documented
- File saved with updates

### SYSTEM FAILURE:
- No existing audits found
- Selected file cannot be loaded
- Modifications not saved

**Master Rule:** Edit mode preserves audit history. Always document what changed and why.
