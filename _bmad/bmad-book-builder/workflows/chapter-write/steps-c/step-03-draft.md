---
name: 'step-03-draft'
description: 'Generate the complete chapter draft following plan, voice, and continuity'

# Navigation
nextStepFile: './step-04-self-review.md'

# Output
outputFile: '{bbb_output_folder}/current-book/chapters/chapter-{chapter_number}.md'

# Reference
antiSlopChecklist: '../data/anti-slop-checklist.md'
---

# Step 3: Draft Chapter

## STEP GOAL:

To generate a complete chapter draft (3000-6000 words) that follows the chapter plan, matches the author's voice from the style profile, and maintains continuity with the story bible and previous chapters.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- CRITICAL: Read the complete step file before taking any action
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:

- You are a **Chapter Writer** generating prose in the author's voice
- This is creative generation guided by plan and style
- Match the author's patterns, not generic AI prose

### Step-Specific Rules:

- Focus ONLY on generating the chapter content
- FORBIDDEN to skip anti-slop enforcement during generation
- Generate scene by scene following the plan
- Apply style profile patterns throughout

## CONTEXT BOUNDARIES:

- Chapter plan provides scene structure
- Style profile provides voice patterns
- Story bible provides character/location details
- Previous summaries provide continuity context
- Brief notes provide author's specific requests

## MANDATORY SEQUENCE

### 1. Prepare for Generation

Review key context before writing:

"**Preparing to draft Chapter {chapter_number}...**

**Style Profile Active:**
- Sentence length: {pattern}
- Vocabulary: {traits}
- Imagery: {preferences}
- Dialogue style: {pattern}

**Anti-Slop Patterns to Avoid:**
- No significance inflation
- No AI vocabulary (testament, landscape, showcasing)
- No copula avoidance (use 'is' and 'has' naturally)
- No rule of three unless author uses it
- Match author's punctuation patterns

**Beginning draft generation...**"

### 2. Generate Chapter Content

Generate the complete chapter following this approach:

**For each scene in the plan:**

1. **Set the scene** — Match author's scene-setting patterns
2. **Character action** — Use bible-accurate character behaviors
3. **Dialogue** — Match author's dialogue style from profile
4. **Internal thought** — If POV character, use their voice
5. **Transition** — Connect to next scene naturally

**While generating, continuously apply:**
- Style profile vocabulary patterns
- Sentence length distribution from profile
- Author's imagery preferences
- Bible-accurate details
- Continuity from previous chapters

**Word count target:** 3000-6000 words

### 3. Anti-Slop Self-Check During Generation

As you write, actively avoid:

**Content Patterns:**
- No "pivotal moments" or "marking a new era"
- No vague attributions ("experts say")
- No formulaic challenges ("despite X, they persevered")

**Language Patterns:**
- Use author's vocabulary, not AI-typical words
- Use "is" and "has" naturally, not "serves as" or "boasts"
- Vary list lengths (no constant rule of three)

**Style Patterns:**
- Match author's em-dash usage (not overuse)
- Match author's formatting patterns
- No chatbot artifacts in narrative

### 4. Present Draft

Once complete, present the draft:

"**Draft Complete: Chapter {chapter_number}**

**Word Count:** {actual count}
**Scenes:** {count}

---

{Full chapter text}

---

**Generation Notes:**
- Voice matching: Applied {X} patterns from style profile
- Bible references: {Y} character/location details included
- Continuity: Referenced {Z} elements from previous chapters"

### 5. Save Draft to Output

Append the complete chapter draft to {outputFile}:

```markdown
## Draft v{version}

{chapter content}

---
_Draft generated: {date}_
_Word count: {count}_
```

Update frontmatter:
- Add 'step-03-draft' to stepsCompleted
- Set draftVersion: {version}

### 6. Auto-Proceed to Self-Review

"**Draft saved. Proceeding to style audit...**"

→ Automatically load {nextStepFile}

(No stop at this step — draft flows directly into style audit. The author review stop comes after step-04.)

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- Complete chapter generated (3000-6000 words)
- Style profile patterns applied throughout
- Bible-accurate character/location details
- Continuity maintained with previous chapters
- Anti-slop patterns actively avoided
- Draft saved to output file

### SYSTEM FAILURE:

- Generating less than 3000 words
- Using generic AI prose instead of author's voice
- Ignoring style profile patterns
- Bible-inaccurate details
- Not applying anti-slop during generation

**Master Rule:** Every sentence should sound like the author wrote it, not like AI.
