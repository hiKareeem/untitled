# Automated Audit Chain Reference
# Used by chapter-write step-07-finalize for quality assurance

> **🎯 AUTOMATION CHAIN — Based on the AgentAdam vs BBB analysis**
>
> AgentAdam uses an automatic audit system after each chapter to ensure coherence. BBB now implements an automatic audit chain that triggers Review → Living Bible Update → Character Audits → Thematic Tracking → Rhythm Analysis.
>
> **Reference:** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (sections 5, 7, 8)

## Chain Sequence

### Step 1: Review (CRITICAL)
**Coherence validation before bible update**

**Action:** Execute Review workflow for this chapter

**Failure Handling:**
- ⚠️ Review detected critical issues
- The audit chain is PAUSED
- Options: Correct / Ignore / Defer

**Success:** Continue to Step 2

### Step 2: Living Bible Update
**Update of the 5 dimensions**

**Dimensions updated:**
- Chronology: Add chapter events
- Locations: Update location states
- Objects: Update introduced/modified objects
- Characters: Update psychological states
- Themes: Record thematic progression

**Action:** Execute Living Bible Edit mode for this chapter

### Step 3: Character Audits
**Audits of characters present in the chapter**

**Process:**
1. Identify characters present (from synopsis)
2. For each character:
   - Contradiction checks (5+ per character)
   - Overall psychological coherence
   - Arc progression

**Action:** For EACH character → Execute character-audit workflow (Create mode)

### Step 4: Thematic Tracking
**Update thematic progression**

**Tracked:**
- Themes addressed: [list]
- Progression phase: [1-5]
- Theme carriers: [which characters]
- Resonances: [symbolic connections]

**Action:** Execute theme-tracker workflow (if available) or update themes.md

### Step 5: Rhythm Analysis (OPTIONNEL)
**Chapter pacing analysis**

**Analyzed:**
- Tension curve
- Action/reflection balance
- Sentence length variation
- Narrative flow

**Action:** Ask user Y/N, then execute rhythm-analysis workflow if yes

## User Options

### [A] Automatic Chain
Execute all 5 steps in sequence
- Step 1 runs first (CRITICAL)
- Steps 2-4 run automatically
- Step 5 requires user confirmation

### [S] Selective Chain
User chooses which steps to execute (1-5, comma-separated)
Execute only selected steps in order

### [D] Defer
Skip audits now (NOT RECOMMENDED)
**Risks:**
- Inconsistencies in future chapters
- Bible out of sync
- Inconsistent characters

**Manual execution later:**
- Review: `review -c {chapter_number}`
- Living Bible: `living-bible -e`
- Character Audit: `character-audit -c`

## Chain Completion Output

```
✅ Audit chain complete!

Steps executed: [list of completed steps]
Steps skipped: [list of skipped steps, if any]

Results summary:
- Review: ✅/❌ [result]
- Living Bible: ✅/❌ [result]
- Character Audits: [N] audits created
- Thematic Tracking: ✅/❌ [result if executed]
- Rhythm Analysis: ✅/❌ [result if executed]

Files created/updated:
- [List audit files created]
- [List bible files updated]
- [List tracking files updated]
```

## Status Storage (Chapter Frontmatter)

```yaml
auditChain:
  review: completed/skipped/failed
  bibleUpdate: completed/skipped
  characterAudits: completed/skipped/partial
  thematicTracking: completed/skipped
  rhythmAnalysis: completed/skipped
  lastChainDate: {date}
```
