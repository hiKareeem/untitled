---
name: 'step-03-map-emotions'
description: 'Track character emotional beats throughout the chapter'

nextStepFile: './step-04-analyze-arc.md'
emotionTemplate: '../data/emotion-template.md'
---

# Step 3: Map Emotions

## STEP GOAL:

To track the emotional beats of each character throughout this chapter - their emotional states, triggers, expressions, and impacts on others.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER invent emotions not shown in the text
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step, ensure entire file is read
- 📋 YOU ARE MAPPING observable emotional moments
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Thematic Weaver** - reading emotional subtext with care
- ✅ Emotions must be shown, not assumed
- ✅ Look for triggers (what causes the emotion) and expressions (how it shows)
- ✅ Note impact on other characters

### Step-Specific Rules:

- 🎯 Focus ONLY on emotional beats - not character arc analysis yet
- 🚫 FORBIDDEN to analyze why emotions connect to themes (that's step 4)
- 🚫 FORBIDDEN to assume internal states without textual evidence
- 💬 Approach: Observational - describe what's shown, not interpreted

## EXECUTION PROTOCOLS:

- 🎯 Identify emotional moments for each character
- 💾 Document trigger, expression, and impact
- 📖 Note emotional shifts within the chapter
- 🚫 Do NOT connect to themes yet - that's step 4

## CONTEXT BOUNDARIES:

- Available: Chapter content, existing emotions.md, theme findings from step-02
- Focus: Character emotional states and beats
- Limits: Observation only, no thematic connection yet
- Dependencies: Chapter loaded, themes identified

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise.

### 1. Identify Characters in Chapter

"**Emotional mapping - Chapter {chapterNumber}**

**Characters present in this chapter:**"

List all characters who appear with significant presence (speaking roles, POV, or meaningful actions).

For each character:
- Name
- Role in this chapter (POV, supporting, minor)
- Starting emotional state (if evident)

### 2. Track Emotional Beats Per Character

For EACH significant character:

**Scan the chapter for emotional moments:**
- Direct emotional descriptions ("she felt angry")
- Physical indicators (clenched fists, tears, laughter)
- Dialogue tone and content
- Actions that reveal emotional state
- Reactions to events or other characters

**For each emotional beat found:**

```markdown
### [Character Name]

**Beat 1:**
- **Emotional state:** [Emotion name]
- **Trigger:** [What triggered this emotion]
- **Expression:** [How it's shown - dialogue, action, physical]
- **Impact on others:** [How other characters react or are affected]

**Beat 2:**
- **Emotional state:** [Emotion]
- **Trigger:** [Trigger]
- **Expression:** [How shown]
- **Impact on others:** [Effect]
```

### 3. Map Emotional Trajectory

For characters with multiple beats, note the emotional trajectory:

"**Emotional trajectory in this chapter:**"

- **[Character]:** [Starting state] → [Key shift] → [Ending state]
  - Example: "Distrust → Surprise → Hesitant gratitude"

### 4. Identify Emotional Interactions

Note moments where characters' emotions interact:

"**Key emotional interactions:**"

- [Character A]'s [emotion] triggers [Character B]'s [response]
- Describe the emotional dynamic between characters

### 5. Note Significant Absences

If a major character shows no emotional beats (flat affect):

"**⚠️ Characters without emotional beats:**"
- [Character] - present but emotionally neutral/absent

This could be intentional (character masking emotions) or a potential issue.

### 6. Check Against Previous Chapter

If emotions.md has data from previous chapters:

"**Emotional continuity:**"

For each character:
- Where did they end emotionally last chapter?
- Does this chapter's opening align?
- Any unexplained emotional shifts?

### 7. Present Emotional Summary

"**Emotional summary - Chapter {chapterNumber}**

| Character | Beats | Trajectory | Notes |
|------------|-------|-------------|-------|
| [Char 1] | [count] | [start] → [end] | [key moment] |
| [Char 2] | [count] | [start] → [end] | [key moment] |

**Major interactions:**
- [Summary of key emotional interactions]

**Most significant beats:**
1. [Most impactful emotional moment]
2. [Second most impactful]

---

Ready to analyze development arcs."

### 8. Present MENU OPTIONS

Display: "**Select:** [C] Continue to arc analysis"

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

#### Menu Handling Logic:

- IF C: Store emotional findings in context, then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All significant characters analyzed
- Emotional beats documented with triggers and expressions
- Trajectories mapped for multi-beat characters
- Character interactions noted
- Continuity with previous chapters checked
- Summary clearly presented

### ❌ SYSTEM FAILURE:

- Assuming emotions without textual evidence
- Skipping characters present in chapter
- Connecting emotions to themes (that's step 4)
- Not noting triggers and expressions
- Missing significant emotional moments

**Master Rule:** Emotions must be OBSERVABLE in the text. Map what's shown, not what's assumed.
