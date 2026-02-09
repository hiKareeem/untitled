# Multi-Agent Review Specification

## Overview

The chapter draft undergoes automated review by 4 specialized BBB agents in parallel. Each agent provides their expert perspective on chapter quality, returning structured findings that are aggregated into a unified review report.

## Review Architecture

### Pattern 4: Parallel Execution

All 4 agents are launched simultaneously as subprocesses, each analyzing the draft from their specialized perspective. Each returns structured JSON findings to the parent process for aggregation.

**Fallback:** If subprocess execution is unavailable, perform reviews sequentially in the main context thread.

---

## Agent Specifications

### Agent 1: Continuity Editor

**Agent File:** `{project-root}/_bmad/bmad-book-builder/agents/continuity-editor.yaml`

**Input:**
- Chapter plan
- Previous chapter summaries
- Draft content

**Responsibilities:**
- Verify plan adherence (all scenes present, all plot points addressed)
- Check narrative continuity with previous chapters
- Identify timeline inconsistencies
- Find logical gaps in narrative flow
- Ensure chapter connects properly to previous and next chapters

**Analysis Focus:**
- Does each planned scene appear in draft?
- Are plot points from plan addressed?
- Does draft align with previous chapter events?
- Are there timeline inconsistencies?
- Are there logical gaps in narrative flow?

**Return Structure:**
```json
{
  "agent": "Continuity Editor",
  "pass": true/false,
  "planAdherence": {
    "scenesComplete": ["scene1", "scene2"],
    "scenesMissing": [],
    "plotPointsAddressed": ["point1"],
    "plotPointsMissing": []
  },
  "continuityIssues": [
    {
      "location": "paragraph X",
      "issue": "description",
      "severity": "high/medium/low"
    }
  ],
  "warnings": [],
  "summary": "Brief assessment"
}
```

---

### Agent 2: Documentaliste

**Agent File:** `{project-root}/_bmad/bmad-book-builder/agents/documentaliste.yaml`

**Input:**
- Draft content
- Bible factual entries
- (Optional) Web browsing for fact verification

**Responsibilities:**
- Verify factual accuracy of technical/professional details
- Check real-world references
- Ensure procedures are described accurately
- Validate technical details
- Cross-reference facts with external sources if needed

**Analysis Focus:**
- Are professional procedures described accurately?
- Are technical details correct?
- Are real-world references accurate?
- Use web-browsing if needed to verify facts

**Return Structure:**
```json
{
  "agent": "Documentaliste",
  "pass": true/false,
  "factsChecked": [
    {
      "fact": "description",
      "status": "verified/unverified/incorrect",
      "source": "if checked"
    }
  ],
  "factualIssues": [
    {
      "location": "paragraph X",
      "claim": "what was claimed",
      "issue": "why incorrect",
      "correction": "suggested fix"
    }
  ],
  "warnings": [],
  "summary": "Brief assessment"
}
```

---

### Agent 3: Style Coach

**Agent File:** `{project-root}/_bmad/bmad-book-builder/agents/style-coach.yaml`

**Input:**
- Style profile
- Draft content
- Anti-slop checklist (`../data/anti-slop-checklist.md`)

**Responsibilities:**
- Verify voice matching against author's style profile
- Detect AI-generated patterns (slop)
- Check quantitative metrics (TTR, sentence length, complexity)
- Ensure vocabulary patterns match author
- Verify dialogue style consistency
- Check imagery preference adherence

**Analysis Focus:**
- TTR (Type-Token Ratio) compared to profile
- Sentence length distribution vs profile
- Vocabulary match with author's patterns
- All 24 anti-slop patterns checked
- Dialogue style consistency
- Imagery preference adherence

**Return Structure:**
```json
{
  "agent": "Style Coach",
  "pass": true/false,
  "voiceScore": 85,
  "metrics": {
    "ttrMatch": "within range/outside range",
    "sentenceLengthMatch": "good/needs adjustment",
    "vocabularyMatch": "strong/moderate/weak"
  },
  "slopPatterns": [
    {
      "pattern": "pattern name",
      "location": "paragraph X",
      "example": "the text",
      "fix": "suggested revision"
    }
  ],
  "styleIssues": [],
  "warnings": [],
  "summary": "Brief assessment"
}
```

---

### Agent 4: Character Keeper

**Agent File:** `{project-root}/_bmad/bmad-book-builder/agents/character-keeper.yaml`

**Input:**
- Story bible
- Draft content

**Responsibilities:**
- Verify bible consistency for all story elements
- Check character behaviors match definitions
- Ensure character dialogue matches voice patterns
- Verify locations described accurately
- Check objects/items used correctly
- Validate relationships portrayed accurately
- Identify contradictions with established facts

**Analysis Focus:**
- Character behaviors match bible definitions
- Character dialogue matches their voice patterns
- Locations described accurately per bible
- Objects/items used correctly
- Relationships portrayed accurately
- No contradictions with established facts

**Return Structure:**
```json
{
  "agent": "Character Keeper",
  "pass": true/false,
  "charactersChecked": ["char1", "char2"],
  "locationsChecked": ["loc1"],
  "inconsistencies": [
    {
      "entity": "Character Name",
      "location": "paragraph X",
      "issue": "description",
      "bibleReference": "what bible says"
    }
  ],
  "warnings": [],
  "summary": "Brief assessment"
}
```

---

## Result Aggregation

### Unified Review Report Format

```markdown
## Multi-Agent Review

**Date:** {date}
**Overall Status:** {PASS / NEEDS REVISION / MAJOR ISSUES}

### Agent Results

| Agent | Pass | Issues |
|-------|------|--------|
| Continuity Editor | {pass} | {count} |
| Documentaliste | {pass} | {count} |
| Style Coach | {pass} | {count} |
| Character Keeper | {pass} | {count} |

### Issues to Address

**Continuity:**
{list issues if any}

**Factual Accuracy:**
{list issues if any}

**Style & Voice:**
- Voice Match: {score}%
- Slop Patterns Found: {count}
{list patterns if any}

**Bible Consistency:**
{list inconsistencies if any}
```

### Overall Status Determination

- **PASS**: All agents return pass=true, 0-2 minor issues total
- **NEEDS REVISION**: 1-2 agents return pass=false, or 3-5 issues total
- **MAJOR ISSUES**: 3+ agents return pass=false, or 6+ issues total, or any high-severity issues

---

## Review Process Flow

### 1. Announcement

Display to user:

```
**Initiating Multi-Agent Review...**

Your chapter will be reviewed by 4 specialized agents:
1. **Continuity Editor** — Plan adherence and narrative continuity
2. **Documentaliste** — Factual accuracy verification
3. **Style Coach** — Voice matching and anti-slop detection
4. **Character Keeper** — Bible consistency check

Running reviews...
```

### 2. Parallel Execution

Launch all 4 subprocesses simultaneously. Each subprocess:
1. Loads the specified agent
2. Analyzes the draft content
3. Returns structured findings to parent

### 3. Aggregation

When all subprocesses complete:
1. Compile findings into unified report
2. Calculate overall status
3. Format results for display

### 4. Results Display

Show the unified review report to the user with:
- Agent status table
- Detailed findings by category
- Overall assessment

### 5. Auto-Proceed

After displaying results, automatically proceed to step-05-user-review without menu interaction.

---

## Fallback Protocol (Sequential Execution)

If subprocess execution is unavailable:

1. **Sequential Reviews**
   - Load Continuity Editor perspective, analyze, record findings
   - Load Documentaliste perspective, analyze, record findings
   - Load Style Coach perspective, analyze, record findings
   - Load Character Keeper perspective, analyze, record findings

2. **Same Output Format**
   - Aggregate findings identically to parallel execution
   - Generate same unified review report
   - Display results in same format

3. **Performance Note**
   - Inform user if running in sequential mode
   - "Running reviews in sequential mode (parallel unavailable)..."

---

## Success Metrics

### SUCCESS

- All 4 agents executed their review
- Structured findings returned from each
- Findings aggregated into unified report
- Report saved to output file
- Clear status communicated

### SYSTEM FAILURE

- Skipping any agent review
- Not aggregating findings properly
- Generic review instead of agent-specific perspectives
- Not saving review results

---

## Master Rule

**Every review perspective matters.** Do not skip agents or combine their findings prematurely. Each agent provides a unique, critical perspective on chapter quality.
