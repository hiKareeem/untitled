---
name: 'step-04-self-review'
description: 'Style audit of chapter draft using style profile, apply fixes'

# Navigation
nextStepFile: './step-05-audit.md'

# Output
outputFile: '{bbb_output_folder}/chapters/chapter-{chapter_number}.md'

# Reference
antiSlopChecklist: '../data/anti-slop-checklist.md'
styleProfilePath: '{style_profile_path}'

# Agent References
styleCoachAgent: '{project-root}/_bmad/bmad-book-builder/agents/style-coach.yaml'
---

# Step 4: Self-Review (Style Audit)

## STEP GOAL:

To audit the chapter draft against the author's style profile, identify deviations, and apply targeted fixes while preserving the author's voice.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- CRITICAL: Read the complete step file before taking any action
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:

- You are performing a **Style Audit** against the author's established voice
- The style profile is the source of truth for voice characteristics
- Fixes must preserve voice — never flatten it toward generic AI prose

### Step-Specific Rules:

- Audit against ALL checks in the style profile (see checklist below)
- Use frontier model consultation when available for deeper analysis
- Present findings to author before applying fixes
- Only apply fixes the author approves
- Anti-slop checklist is a hard constraint — zero tolerance

## CONTEXT BOUNDARIES:

- Draft from step-03 is complete and saved
- Style profile loaded during step-01
- Focus: Voice consistency and style compliance, not content

## MANDATORY SEQUENCE

### 1. Run Style Audit

Execute the following checks against the style profile:

| # | Check | What to Measure |
|---|-------|-----------------|
| 1 | Negation-before-assertion count | Target per chapter from style profile (note: POV-specific overrides may apply) |
| 2 | Fragment/paratactic % | Target range from style profile |
| 3 | Bimodal paragraphs | Dense blocks alternating with single-line punches |
| 4 | Em dashes | Signature usage — parenthetical, pivotal, listing |
| 5 | Italics (payoff words) | Used for emphasis on thematically load-bearing words |
| 6 | Dialogue ratio | Target range from style profile |
| 7 | Sensory hierarchy | Must follow profile order (e.g., Sound > Temperature > Tactile > Visual > Taste) |
| 8 | Emotion via physical sensation | Named emotions must be physicalized — NEVER tell directly |
| 9 | Anti-slop | Run full `{antiSlopChecklist}` — zero tolerance |
| 10 | Metaphor domain | POV-specific metaphor domains from style profile (no cross-contamination) |
| 11 | Dialogue tags | Only "said" and action beats — no "whispered," "muttered," etc. |
| 12 | Avg sentence length | Target from style profile |

**Frontier Model Consultation (when available):**
- Send chapter + style profile to frontier model for independent audit
- Compare frontier findings with self-audit
- Flag any discrepancies

### 2. Present Findings

Present audit results to the author:

```
**Style Audit — Chapter {chapter_number}**

| # | Check | Result | Notes |
|---|-------|--------|-------|
| 1 | ... | ✅/⚠️ | ... |
...

**Fixes Required:** {count}
**Fixes Recommended:** {count}

Shall I apply fixes? [Y] Yes / [N] No / [S] Selective
```

Wait for author response.

### 3. Apply Approved Fixes

For each approved fix:

1. **Locate the passage** — exact line reference
2. **Draft the fix** — maintain voice, don't flatten
3. **Present before/after** — show the author what changed
4. **Apply** — edit the file

Re-run anti-slop check on all fixed passages.

### 4. Save and Present for Author Review

Update {outputFile} frontmatter:
- Add 'step-04-self-review' to stepsCompleted

"**Style audit complete. Draft is ready for author review.**

The chapter has been drafted and style-audited. Please review the draft, provide any line-level edits or comments, and confirm when ready to proceed to character/continuity audit.

**Select an option:** `[C]` Continue to Audit `[E]` Edit Mode (apply specific changes first)"

### MENU HANDLING LOGIC:

- IF C: Load, read entire file, then execute {nextStepFile}
- IF E: Wait for author's line-level edits, apply them, then redisplay menu
- IF Any other: Help user, then redisplay menu

**CRITICAL: Do NOT auto-proceed. The author MUST review the draft before the audit runs.**

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- All 12 checks executed against style profile
- Findings presented clearly with line references
- Author approved fixes before application
- Anti-slop re-checked on all modified passages
- Voice preserved in all fixes

### SYSTEM FAILURE:

- Skipping checks or using generic criteria instead of style profile
- Applying fixes without author approval
- Introducing AI patterns in fixes
- Flattening voice toward generic prose

**Master Rule:** The style profile is the source of truth. Every fix must make the prose MORE like the author's voice, never less.
