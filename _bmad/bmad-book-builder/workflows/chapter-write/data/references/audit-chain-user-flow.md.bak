# Automated Audit Chain - User Interaction Flow

**Purpose:** Guide users through the automated audit chain execution options.

**Reference:** See `data/references/automated-audit-chain.md` for complete technical documentation.

---

## Introduction to User

```text
🔗 Automated Audit Chain

To ensure your novel's coherence, I will now automatically trigger a series of quality audits.

The audit chain:
1. Review — Coherence validation (CRITICAL)
2. Living Bible Update — Update the 5 dimensions
3. Character Audits — Audit per character present
4. Thematic Tracking — Update thematic progression
5. Rhythm Analysis — Pacing analysis (optional)
```

---

## User Choice Prompt

```text
How would you like to proceed?

[A] Automatic — Run the full chain (RECOMMENDED)
[S] Selective — Choose which steps to run
[D] Defer — Skip audits for now (NOT RECOMMENDED)

Your choice: [A]utomatic / [S]elective / [D]efer
```

---

## Option A: Automatic Execution

**User Message:**
```text
Running the automatic audit chain...
```

**Procedure:**
1. Load automated-audit-chain.md reference
2. Execute automatic chain sequence:
   - Step 1: Review → If fails, pause and ask [C]orrect/[I]gnore/[D]efer
   - Step 2: Living Bible Update
   - Step 3: Character Audits (for each character in chapter)
   - Step 4: Thematic Tracking
   - Step 5: Ask Y/N for Rhythm Analysis

---

## Option S: Selective Execution

**User Message:**
```text
Choose the steps to run:

[1] Review (Recommended)
[2] Living Bible Update (Recommended)
[3] Character Audits (Recommended)
[4] Thematic Tracking
[5] Rhythm Analysis

Enter the step numbers to run (comma-separated):
```

**Procedure:**
- Execute only selected steps in order (1-5)

---

## Option D: Defer Execution

**User Message:**
```text
⏸️ Audit chain deferred

The audits will not be executed now.

⚠️ IMPORTANT: Without audits, you risk:
- Inconsistencies in future chapters
- Bible out of sync
- Inconsistent characters

You can run the audits manually later:
- Review : `review -c {chapter_number}`
- Living Bible : `living-bible -e`
- Character Audit : `character-audit -c`

Do you really want to defer? [Y] Yes / [N] Cancel and run the chain
```

**Procedure:**
- Wait for user confirmation
- If confirmed, skip audit chain
- If N cancelled, proceed to automatic execution

---

## Chain Completion Summary

**User Message:**
```text
✅ Audit chain complete!

Steps executed: [list of completed steps]
Steps skipped: [list of skipped steps, if any]

Results summary:
- Review : ✅/❌ [result]
- Living Bible : ✅/❌ [result]
- Character Audits: [N] audits created
- Thematic Tracking : ✅/❌ [result if executed]
- Rhythm Analysis : ✅/❌ [result if executed]

Files created/updated:
- [List audit files created]
- [List bible files updated]
- [List tracking files updated]
```

---

## Chain Status Storage

**Store in Chapter Frontmatter:**

```yaml
auditChain:
  review: completed/skipped/failed
  bibleUpdate: completed/skipped
  characterAudits: completed/skipped/partial
  thematicTracking: completed/skipped
  rhythmAnalysis: completed/skipped
  lastChainDate: {date}
```

---

## Audit Chain Steps Reference

**Step 1: Review** (CRITICAL)
- Validates consistency
- If fails: Pause for user decision

**Step 2: Living Bible Update**
- Updates 5 dimensions
- Chronology, Locations, Objects, Characters, Themes

**Step 3: Character Audits**
- One audit per character present in chapter
- Tracks character development

**Step 4: Thematic Tracking**
- Updates thematic progression
- Monitors theme evolution

**Step 5: Rhythm Analysis** (Optional)
- Analyzes chapter pacing
- Flow and rhythm assessment
