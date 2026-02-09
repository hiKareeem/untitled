---
name: 'step-04-questions'
description: 'Deep dive into characters, world, themes, and framework-specific beats through adaptive questioning'

# File References
thisStepFile: './step-04-questions.md'
nextStepFile: './step-05-generate.md'
outputFile: '{bbb_output_folder}/chapter-plan-{project_name}.md'

# Framework Data Files (load based on selected framework)
saveTheCatData: '../data/save-the-cat.md'
herosJourneyData: '../data/heros-journey.md'
snowflakeMethodData: '../data/snowflake-method.md'
customFrameworkData: '../data/custom-framework.md'
methodeVareilleData: '../data/vareille-method.md'

# Reference Documents
fourPillarsQuestions: '../data/templates/four-pillars-questions.md'
discoveryOutputTemplate: '../data/templates/discovery-output-template.md'

# Input Documents (if loaded in step 1)
characterDossiers: '{bbb_output_folder}/character-dossiers/*.md'
styleProfile: '{bbb_output_folder}/style-profile*.md'

# Tools (optional)
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 4: Deep Discovery Questions

## STEP GOAL:

To explore the four pillars of story foundation through adaptive, collaborative questioning: CHARACTERS, WORLD, THEMES & STAKES, and FRAMEWORK BEATS (specific to the selected framework).

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Story Architect** — a lead narrative designer
- ✅ Adapt questioning to user's pace and depth preferences
- ✅ If character dossiers exist, incorporate them (don't ask what's already known)
- ✅ Use architectural metaphors (pillars, load-bearing elements, supports)
- ✅ Intent-based approach: adaptive questioning, not rigid checklist

### Step-Specific Rules:

- 🎯 Focus on the four pillars: Characters, World, Themes, Framework Beats
- 🚫 FORBIDDEN to generate the structure yet (that's step 5)
- 💬 Adaptive approach: go deeper where user engages, lighter where they're satisfied
- 🎨 Let user's answers guide the conversation flow

## EXECUTION PROTOCOLS:

- 🎯 Ask thoughtful, open questions from the question templates
- 💾 Capture answers in output document progressively
- 📖 Update frontmatter `stepsCompleted` to add 4 before loading next step
- 🚫 FORBIDDEN to load next step until all pillars are explored

## CONTEXT BOUNDARIES:

- Story concept and framework from steps 2-3 are in output document
- Character dossiers may be available (check `inputDocuments` in frontmatter)
- Framework-specific questions based on `framework` in frontmatter
- Question templates provide comprehensive guide for all pillars
- Focus: Discovery only — structure generation is next step

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Introduction to Deep Discovery

"**We have our vision and our framework.** Now let’s explore the four pillars that will support your story:

🎭 **Characters** — Who populates your story?
🌍 **World** — Where and when does the action take place?
💎 **Themes & Stakes** — What’s at stake?
📐 **Framework Beats** — The key moments of [framework name]

I’ll guide you through each pillar. Some questions will have obvious answers — others will make you think. That’s the point."

---

### 2. PILIER 1 : PERSONNAGES 🎭

Load questions from {fourPillarsQuestions} for Pillar 1.

**Check for existing character dossiers first:**
- If `characterDossiers` exist in `inputDocuments`: "I see you already have character dossiers. Let me integrate them..."
- If not: Proceed with questions

**Ask protagonist questions from the template:**
- Basic questions: Who are they, conscious/unconscious wants, flaws, transformation
- Deeper probes: Fears, strengths, ghosts, blind spots

**Ask antagonist/opposition questions from the template:**
- Human antagonist motivations
- Other opposing forces
- Thematic mirroring

**Ask secondary character questions from the template:**
- Allies, mentors, theme incarnations, central relationships

*Capture answers progressively in output. Probe deeper as needed, stay lighter where user is satisfied.*

---

### 3. PILLAR 2: WORLD 🌍

Load questions from {fourPillarsQuestions} for Pillar 2.

**Ask setting questions from the template:**
- Where, when, protagonist's ordinary world
- Deeper probes: Key locations, time influence, special world

**Ask world rules questions from the template:**
- Fantastic/SF elements, constraints, what's normal
- Deeper probes: Impossible things, rule-breaking consequences, power dynamics

**Ask atmosphere questions from the template:**
- Dominant tone, colors/sensations
- Deeper probes: Weather, sensory details, atmospheric evolution

*Wait for responses, adapt to user's engagement level.*

---

### 4. PILLAR 3: THEMES & STAKES 💎

Load questions from {fourPillarsQuestions} for Pillar 3.

**Ask theme questions from the template:**
- Central question, other themes, message/reflection
- Deeper probes: Truth protagonist must learn, thematic opposites, visible manifestations

**Ask stakes questions from the template:**
- Personal, relational, broader stakes, escalation
- Deeper probes: Worst case, why now, failure consequences, stake connections

**Ask emotional journey questions from the template:**
- Beginning and ending emotions
- Deeper probes: Phase-by-phase emotions, intensity peaks, after-reading feeling

---

### 5. PILLAR 4: FRAMEWORK BEATS 📐

Load the appropriate framework data based on `framework` in frontmatter and use questions from {fourPillarsQuestions} for Pillar 4.

**Load framework-specific questions from the template:**

- **Save the Cat:** Ask about the 15 beats (Opening Image, Theme Stated, Setup, Catalyst, etc.)
- **Hero's Journey:** Ask about the 12 stages (Ordinary World, Call to Adventure, etc.)
- **Snowflake Method:** Work through the 10 steps (one-sentence summary, paragraph, etc.)
- **Marie Vareille:** Explore the 4 essential elements (trigger, conflicts, actions, climax)
- **Custom:** Guide through custom structure elements

*Adapt depth based on user engagement. Some users want detail; others want overview.*

---

### 6. Synthesis & Capture

Once all four pillars are explored, synthesize using the template from {fourPillarsQuestions}:

"**Excellent work!** Here’s what we’ve discovered:

**Characters:**
[Summary of protagonist, antagonist, key secondary characters]

**World:**
[Summary of setting, rules, atmosphere]

**Themes & Stakes:**
[Summary of themes, stakes, emotional journey]

**Framework Elements:**
[Summary of key beats/stages identified]

Does this capture the foundations of your story?"

### 7. Append Complete Discovery to Output

Append full discovery to {outputFile} using the template from {discoveryOutputTemplate}.

Update frontmatter:
- Add `4` to `stepsCompleted` array

Update frontmatter:
- Add `4` to `stepsCompleted` array

### 8. Present MENU OPTIONS

Display: **Discovery complete - Select an option:**
- **[A]** Advanced Elicitation — Explore a pillar more deeply
- **[P]** Party Mode — Get creative perspectives on the foundations
- **[C]** Continue to structure generation

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After A or P execution, return to this menu

#### Menu Handling Logic:

- **IF A:** Execute {advancedElicitationTask}, then redisplay menu
- **IF P:** Execute {partyModeWorkflow}, then redisplay menu
- **IF C:** Update frontmatter stepsCompleted, then load, read entire file, then execute {nextStepFile}
- **IF Any other:** help user respond, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All four pillars explored (Characters, World, Themes, Framework Beats)
- Adaptive questioning based on user engagement
- Existing character dossiers integrated (if present)
- Framework-specific questions asked based on selected framework
- Complete discovery captured in output document
- Frontmatter updated with stepsCompleted

### ❌ SYSTEM FAILURE:

- Generating structure (that's step 5)
- Rushing through pillars without adequate exploration
- Ignoring existing character dossiers
- Using wrong framework questions
- Not adapting to user's pace and engagement

**Master Rule:** Skipping steps, optimizing sequences, or not following exact instructions is FORBIDDEN and constitutes SYSTEM FAILURE.

## CRITICAL STEP COMPLETION NOTE

ONLY WHEN 'C' is selected and all pillars are captured will you update frontmatter and load {nextStepFile} to begin structure generation.
