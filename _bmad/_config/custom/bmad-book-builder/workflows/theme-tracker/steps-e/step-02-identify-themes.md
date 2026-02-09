---
name: 'step-02-identify-themes'
description: 'Detect and document thematic threads present in the chapter'

nextStepFile: './step-03-map-emotions.md'
themeTemplate: '../data/theme-template.md'
---

# Step 2: Identify Themes

## STEP GOAL:

To detect which thematic threads from the Living Bible are present in this chapter and document how they appear.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without understanding the chapter
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step, ensure entire file is read
- 📋 YOU ARE AN ANALYST identifying themes, not inventing them
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Thematic Weaver** - detecting themes with precision
- ✅ Use the Living Bible themes as your reference guide
- ✅ Look for evidence, not assumptions
- ✅ A theme must be demonstrably present, not just implied

### Step-Specific Rules:

- 🎯 Focus ONLY on theme identification - not emotions or arcs yet
- 🚫 FORBIDDEN to invent themes not in the Living Bible
- 🚫 FORBIDDEN to claim a theme is present without textual evidence
- 💬 Approach: Analytical but accessible - explain your reasoning

## EXECUTION PROTOCOLS:

- 🎯 Compare chapter content against Living Bible themes
- 💾 Document each theme found with evidence
- 📖 Categorize by presence level (Strong/Moderate/Background)
- 🚫 Do NOT analyze emotions or character arcs yet

## CONTEXT BOUNDARIES:

- Available: Chapter content, Living Bible themes, existing themes.md
- Focus: Theme detection and documentation
- Limits: Only themes, not emotions or arcs
- Dependencies: Data loaded from step-01

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise.

### 1. Review Available Themes

"**Analyse thématique du chapitre {chapterNumber}**

**Thèmes de référence (Living Bible) :**"

List all themes from the Living Bible that could potentially appear.

For each theme, note:
- Theme name
- Core question
- Key indicators to look for

### 2. Scan Chapter for Theme Presence

For EACH theme in the Living Bible:

**Search the chapter for indicators:**
- Direct mentions of theme concepts
- Situations that embody the theme's tension
- Character actions that relate to the theme
- Dialogue that references theme questions
- Symbolic elements connected to theme

**Document findings:**
- If found: Note specific passages/moments
- If not found: Mark as "Not present in this chapter"

### 3. Classify Theme Presence Levels

For each theme detected, classify its presence:

**Strong Presence:**
- Theme is central to chapter events
- Multiple scenes directly engage with theme
- Character decisions driven by theme tension

**Moderate Presence:**
- Theme appears but isn't central
- One or two clear moments
- Supports other themes or plot

**Background Presence:**
- Theme subtly present
- Referenced indirectly
- Maintains continuity without focus

### 4. Document Theme Findings

"**Thèmes identifiés dans le chapitre {chapterNumber} :**"

For EACH theme found:

```markdown
### [Theme Name]

**Niveau de présence :** [Strong / Moderate / Background]

**Comment il apparaît :**
[Description de comment le thème se manifeste dans ce chapitre]

**Moments clés :**
- [Moment 1 avec référence si possible]
- [Moment 2]

**Citations ou passages révélateurs :**
> "[Quote from chapter that demonstrates theme]"

**Progression depuis le chapitre précédent :**
[Comment le thème a-t-il avancé par rapport au chapitre précédent, si tracking existe]
```

### 5. Identify New Theme Elements

Check if this chapter introduces:
- New aspects of existing themes
- New character connections to themes
- Shifts in theme tension

"**Nouveaux éléments thématiques :**"
- [List any new developments]

### 6. Check for Absent Expected Themes

If a theme was strongly present in recent chapters but absent here:

"**⚠️ Thèmes attendus mais absents :**"
- [Theme name] - was [presence level] in chapter [N-1], not detected here

This isn't necessarily a red flag - themes can rest between chapters. Note for later verification.

### 7. Present Theme Summary

"**Résumé thématique - Chapitre {chapterNumber}**

| Thème | Présence | Moments clés |
|-------|----------|--------------|
| [Theme 1] | Strong | [Brief description] |
| [Theme 2] | Moderate | [Brief description] |
| [Theme 3] | Background | [Brief description] |

**Thèmes non présents ce chapitre :** [list]

**Nouveaux développements :** [list or 'Aucun']

---

Prêt à passer à l'analyse des émotions."

### 8. Present MENU OPTIONS

Display: "**Sélectionnez :** [C] Continuer vers l'analyse émotionnelle"

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

#### Menu Handling Logic:

- IF C: Store theme findings in context, then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All Living Bible themes checked against chapter
- Each detected theme has evidence
- Presence levels appropriately assigned
- New theme elements identified
- Absent expected themes noted
- Summary presented clearly

### ❌ SYSTEM FAILURE:

- Claiming theme presence without evidence
- Inventing themes not in Living Bible
- Skipping themes during analysis
- Not classifying presence levels
- Starting emotional analysis in this step

**Master Rule:** Themes must be DETECTED with evidence, not ASSUMED or INVENTED.
