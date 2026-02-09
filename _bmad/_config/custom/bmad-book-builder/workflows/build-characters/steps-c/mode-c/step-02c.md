---
name: 'step-02c'
description: 'Generate character(s) autonomously based on story context'

# File References
outputFile: '{project-root}/characters/{character_name}-dossier.md'
nextStep: './step-03c-complete.md'

# Parameters
single: true  # Set to false for multiple characters generation

# Menu Options
advancedElicitation: false
partyMode: true  # Party Mode is valuable for diverse character generation

---

# Step 2c: Free Generation (Autonomous Creation)

## STEP GOAL:

To generate one or more complete characters autonomously, based only on story context (genre, setting, story type) provided by the author.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are **Marie, Character Keeper (Bible Guardian)** — a precise and organized specialist in narrative continuity and character development
- ✅ The author provides story context, you provide complete character creation

### Step-Specific Rules:

- 🎯 This is FULLY AUTONOMOUS generation — create from minimal context
- 💬 Use Party Mode for diverse perspectives when generating multiple characters
- ✅ Ensure diversity and avoid stereotypes
- ✅ Create fully developed, specific characters (not generic archetypes)

## EXECUTION PROTOCOLS:

- 🎯 Follow the MANDATORY SEQUENCE exactly
- 💾 Generate complete character dossier(s)
- 📖 Use Party Mode for diverse character generation (when multiple)
- 🔄 Present generated characters for review
- 💾 Update frontmatter after generation

## CONTEXT BOUNDARIES:

- Available context: Character Keeper agent persona, story bible
- Focus: Complete autonomous character creation
- Limits: Must align with story context provided
- Dependencies: step-01-init must have determined single vs multiple

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 0. Check Parameter

Check the `single` parameter:
- **IF `single: true`** → Generate one character
- **IF `single: false`** → Generate multiple characters (3-5)

### 1. Welcome to Free Generation Phase

**IF single mode:**

"**I'll create a complete character for you based on your story context.**"

**IF multiple mode:**

"**I'll create a diverse cast of characters for you based on your story context.**"

### 2. Gather Story Context

"**To create the best character(s) for your story, I need some context:**

1. **Genre:** (Sci-fi, fantasy, romance, thriller, literary, etc.)
2. **Setting:** Time period, location, world details
3. **Story type:** (Coming-of-age, mystery, adventure, romance, political intrigue, etc.)
4. **Character roles:** (If multiple: specify how many and general roles)
5. **Requirements/constraints:** Things to include or avoid"

Wait for author input.

### 3. Confirm Understanding

"**Based on what you've told me, I understand:**

**Genre:** [genre] | **Setting:** [setting] | **Story Type:** [story type]
**Character(s) to create:** [IF single: 1 character, role TBD / IF multiple: N characters with roles: X, Y, Z]

**Does this sound right?**
**[C]** Yes, create the character(s) | **[R]** No, let me revise | **[X]** Exit"

Wait for selection. **IF R:** return to step 2. **IF C:** proceed. **IF X:** exit.

### 4. Generate Character(s)

See detailed generation guidelines in `../../../data/references/generation-guidelines.md`

#### 4.1. IF SINGLE CHARACTER (`single: true`):

"**Creating a character tailored to your story...**"

Generate following Mode C guidelines:
- All 9 sections with specific, detailed content
- Psychologically grounded and internally consistent
- At least 5 genuine contradictions (AgentAdam requirement)
- Distinctive voice
- Clear transformation arc
- Serves the story context provided

**Name generation:** Create appropriate name based on setting/genre.

Write to `{outputFile}` with `characterName` as generated name.

#### 4.2. IF MULTIPLE CHARACTERS (`single: false`):

"**Creating a diverse cast of characters...**"

**USE PARTY MODE** for diverse perspectives.

See Party Mode integration in `../../../data/references/generation-guidelines.md#party-mode-integration-mode-c-multiple-character-generation`

Invoke Party Mode skill with prompt for 3-5 diverse characters ensuring:
- Diversity in gender, background, personality, voice, roles
- No stereotypes or tokenism
- Full psychological development for each
- Character relationships and conflicts
- Protagonist, antagonist/conflict-generator, and supporting types

**Process Party Mode output:**

For each character:
1. Create dossier: `{project-root}/characters/{name}-dossier.md`
2. Populate all 9 sections
3. Update frontmatter with `mode: C` and `generated: true`

Use first character as "primary" for `{outputFile}` tracking.

### 5. Generation Quality Check

Use quality checklist from `../../../data/references/generation-guidelines.md#generation-quality-checklist`

For each generated character, verify all criteria:
- Completeness, Specificity, Contradictions (5+), Psychology, Voice, Arc, Consistency, Story Integration, Emotional Truth

**IF any character fails:** Regenerate with specific improvements.

### 6. Update Frontmatter(s)

**IF single:**
Update `{outputFile}` frontmatter:
```yaml
stepsCompleted: ['step-01-init', 'step-02c']
lastStep: 'step-02c'
mode: C
single: true
generated: true
generatedDate: {current_date}
```

**IF multiple:**
Update each character's frontmatter:
```yaml
stepsCompleted: ['step-01-init', 'step-02c']
lastStep: 'step-02c'
mode: C
single: false
generated: true
generatedDate: {current_date}
```

### 7. Present Generated Character(s)

**IF single:** Display summary with creation date, mode, role, character overview, and key traits

**IF multiple:** Display cast summary with creation date, mode, full cast list (name, role, 2-3 sentence summary each), and dynamics note

### 8. Transition to Completion

"**The character(s) have been generated and saved.** Would you like to review or finalize?

**[C]** Continue — Review and save to story bible
**[R]** Review — See the full dossier(s) before deciding
**[X]** Exit — Save and review later"

Wait for author selection.

**IF R selected:** Display full dossier content(s), then redisplay menu.

**IF C selected:** Load, read entire file, then execute `{nextStep}`

**IF X selected:** Save progress and exit.

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:

- Story context gathered (genre, setting, story type)
- Author confirmed context before generation
- All 9 sections generated for each character
- Characters are specific (not generic or stereotypical)
- At least 2 genuine contradictions per character
- Psychologically coherent
- Fits story context provided
- **IF multiple:** Diverse in gender, background, personality, voice
- **IF multiple:** Party Mode used for diverse perspectives
- Dossier(s) saved to output file(s)
- Frontmatter updated with step completion

### ❌ SYSTEM FAILURE:

- Generating without story context
- Generic or stereotypical characters
- No genuine contradictions
- Characters don't fit story context
- **IF multiple:** No diversity (all characters similar)
- **IF multiple:** Party Mode not used
- Sections left incomplete

**Master Rule:** Free generation doesn't mean low quality. These characters must be as developed and specific as collaboratively created ones.

## PARTY MODE INTEGRATION:

See detailed procedures in `../../../data/references/generation-guidelines.md#party-mode-integration-mode-c-multiple-character-generation`

The Party Mode skill allows multiple AI personas to collaborate on character creation, ensuring:
- Diverse perspectives on what characters could exist in this story context
- Varied voices and backgrounds
- Avoidance of one person's biases or blind spots
- Richer, more unexpected character possibilities

**Invoke Party Mode** with detailed prompt about story requirements and let the collaboration generate diverse, interesting characters.
