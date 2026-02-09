---
name: 'step-04-analyze-arc'
description: 'Analyze character development per theme and present for user validation'

nextStepFile: './step-05-update-progression.md'
---

# Step 4: Analyze Arc + CHECKPOINT

## STEP GOAL:

To connect character development with thematic threads, analyze how characters embody themes, and present the COMPLETE ANALYSIS for user validation before updating tracking files.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 THIS STEP HAS A CHECKPOINT - Do NOT proceed without user approval
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step, ensure entire file is read
- 📋 YOU ARE SYNTHESIZING themes and emotions into character arcs
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Thematic Weaver** - connecting dots between themes and characters
- ✅ This is where analysis becomes insight
- ✅ Show how character emotions relate to thematic threads
- ✅ User validates before any files are modified

### Step-Specific Rules:

- 🎯 Focus on CHARACTER-THEME connections
- 🚫 FORBIDDEN to update any tracking files in this step
- 🚫 FORBIDDEN to proceed without explicit user approval
- 💬 Approach: Synthesize and present clearly for human review

## EXECUTION PROTOCOLS:

- 🎯 Connect emotional beats to thematic threads
- 💾 Prepare analysis summary (DO NOT WRITE TO FILES YET)
- 📖 Present complete analysis for user validation
- 🚫 WAIT for user approval before proceeding

## CONTEXT BOUNDARIES:

- Available: Theme findings (step-02), emotional beats (step-03), existing tracking
- Focus: Character development through thematic lens
- Limits: Analysis only - no file updates
- Dependencies: Steps 01-03 completed

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise.

### 1. Synthesize Themes and Emotions

"**Analyse des arcs de développement - Chapitre {chapterNumber}**

Connexion entre les thèmes identifiés et les beats émotionnels..."

For EACH character with significant emotional beats:

**Connect their emotions to themes:**

```markdown
### [Character Name]

**Position thématique dans ce chapitre :**

**[Theme 1]:**
- Où se situe ce personnage par rapport à ce thème ?
- Comment ses émotions/actions ce chapitre reflètent-elles le thème ?
- Mouvement : [vers/loin de/statique] par rapport à la tension thématique

**[Theme 2]:**
- Position sur ce thème
- Lien avec beats émotionnels
- Mouvement thématique
```

### 2. Identify Character Development Moments

"**Moments de développement clés :**"

For each character, identify if this chapter contains:
- **Turning points:** Major shifts in character position
- **Deepening:** Existing traits intensified
- **Revelation:** New aspects revealed
- **Testing:** Character tested on their values
- **Static:** No development (note if intentional or concerning)

### 3. Map Theme Advancement

"**Avancement des thèmes dans ce chapitre :**"

For EACH theme identified in step-02:

```markdown
### [Theme Name]

**État au début du chapitre :** [Where the theme stood]
**Ce qui se passe :** [How the theme progresses through events]
**État à la fin du chapitre :** [Where the theme now stands]

**Personnages impliqués :**
- [Character]: [Their role in this theme's progression]
- [Character]: [Their role]

**Prochaine étape attendue :**
[What naturally follows from this progression]
```

### 4. Detect Red Flags

"**🚨 Analyse des red flags :**"

Check for potential issues:

- [ ] **Thème mentionné mais pas exploré :**
  [List any themes referenced but not developed]

- [ ] **Position personnage inchangée :**
  [List characters whose thematic position hasn't shifted in many chapters]

- [ ] **Thème abandonné :**
  [List themes that were active but disappeared without resolution]

- [ ] **Incohérence avec chapitres précédents :**
  [List any contradictions detected]

"**Red flags détectés :** [None / List]"

### 5. Prepare Analysis Summary

"**══════════════════════════════════════════════════════════════════**
**ANALYSE COMPLÈTE - CHAPITRE {chapterNumber}**
**══════════════════════════════════════════════════════════════════**"

Present the COMPLETE analysis in one unified view:

```markdown
## Résumé thématique

| Thème | Présence | Progression | Personnages clés |
|-------|----------|-------------|------------------|
| [Theme 1] | [Level] | [Movement] | [Names] |
| [Theme 2] | [Level] | [Movement] | [Names] |

## Résumé émotionnel

| Personnage | Beats | Arc ce chapitre | Lien thématique |
|------------|-------|-----------------|-----------------|
| [Char 1] | [N] | [Summary] | [Theme connection] |
| [Char 2] | [N] | [Summary] | [Theme connection] |

## Développements clés

1. [Most significant development]
2. [Second most significant]
3. [Third if applicable]

## Red Flags

[List or "Aucun détecté"]

## Ce que cette analyse va mettre à jour

**themes.md :** [What will be updated]
**emotions.md :** [What will be updated]
**chapter-{XX}-themes.md :** [Will be created/updated]
```

### 6. CHECKPOINT: User Validation

"**══════════════════════════════════════════════════════════════════**
**🔍 CHECKPOINT - VALIDATION REQUISE**
**══════════════════════════════════════════════════════════════════**

Avant de mettre à jour les fichiers de tracking, veuillez valider cette analyse.

**Questions :**
1. Les thèmes identifiés sont-ils corrects ?
2. Les beats émotionnels reflètent-ils votre intention ?
3. Les connexions personnage-thème sont-elles justes ?
4. Y a-t-il des éléments que j'ai manqués ?
5. Y a-t-il des corrections à apporter ?

**Options :**
- **[A] Approuver** - L'analyse est correcte, procéder à la mise à jour
- **[C] Corriger** - J'ai des corrections à apporter
- **[R] Refaire** - Refaire l'analyse avec de nouvelles instructions"

### 7. Present MENU OPTIONS

Display: "**Validation :** [A] Approuver [C] Corriger [R] Refaire"

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- ONLY proceed to file updates when user selects 'A' (Approve)
- If 'C', collect corrections and revise analysis
- If 'R', return to step-02 with new instructions

#### Menu Handling Logic:

- IF A: User approves - proceed to next step with validated analysis
  Load, read entire file, then execute {nextStepFile}
- IF C: Collect corrections from user, revise the analysis summary, then redisplay checkpoint
- IF R: Ask user for new instructions, then load step-02 to re-analyze
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Themes and emotions synthesized into character arcs
- Development moments identified
- Theme advancement documented
- Red flags detected and reported
- Complete analysis presented clearly
- User explicitly approves before proceeding

### ❌ SYSTEM FAILURE:

- Proceeding without user approval
- Updating files in this step
- Presenting incomplete analysis
- Not checking for red flags
- Skipping the checkpoint

**Master Rule:** THIS IS A CHECKPOINT. User MUST approve before any tracking files are modified.
