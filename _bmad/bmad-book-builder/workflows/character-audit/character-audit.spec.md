# Workflow Specification: CharacterAudit

**Module:** bmad-book-builder
**Status:** Specification — To be created via create-workflow workflow
**Created:** 2026-01-24
**Priority:** P0 (Critical Gap — Feature Parity with AgentAdam)

---

## Workflow Overview

**Goal:** Verify character psychological coherence after each chapter

**Description:** Continuity Editor performs character-specific audits to check that character behavior in each chapter aligns with their established psychological profile, contradictions, and arc progression. Each audit produces a pass/fail report for every contradiction.

**Workflow Type:** Create-only (per-chapter audit)

---

## Why This Workflow Exists

> **🎯 CRITICAL GAP IDENTIFIED — AgentAdam vs BBB analysis**
>
> AgentAdam has a per-character audit system that verifies psychological coherence chapter by chapter. BBB currently only has general continuity checks.
>
> **Without this workflow, characters can become inconsistent.** The contradictions established in profiles are not verified in the writing.
>
> **Reference:** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (section 5)
>
> **Impact:** HIGH — Ensures long-term character quality and coherence
> **Effort:** MEDIUM — Structured workflow with consistent checks

---

## Workflow Structure

### Entry Point

```yaml
---
name: character-audit
description: Verify character psychological coherence after each chapter
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/character-audit'
---
```

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Select Chapter & Character | Choose which chapter and character to audit |
| 2 | Load Character Profile | Read the character's complete dossier |
| 3 | Extract Chapter Behavior | Identify what character does/thinks/feels in chapter |
| 4 | Check Contradictions | **Verify each contradiction (5+) against behavior** |
| 5 | Verify Arc Progression | Check if character is progressing through their arc |
| 6 | Generate Audit Report | Create pass/fail report with ✅/❌ for each contradiction |

---

## Character-Specific Audit Template

> **Based on AgentAdam's audit system (section 5 of the analysis)**

```markdown
## Audit - Chapter XX - [Character Name]

### Appearance in This Chapter
- Scenes: [list of scenes]
- Key Actions: [what they do]
- Dominant emotions: [what they feel]

### Psychological coherence — Contradiction checks
- ✅/❌ Contradiction 1 (Values vs Actions): [check against behavior] — COHERENT/INCOHERENT
- ✅/❌ Contradiction 2 (Self-image vs Reality): [check against behavior] — COHERENT/INCOHERENT
- ✅/❌ Contradiction 3 (Conscious vs Unconscious): [check against behavior] — COHERENT/INCOHERENT
- ✅/❌ Contradiction 4 (Idealism vs Pragmatism): [check against behavior] — COHERENT/INCOHERENT
- ✅/❌ Contradiction 5 (Past vs Present): [check against behavior] — COHERENT/INCOHERENT
- ✅/❌ Contradiction 6+ (others): [check against behavior] — COHERENT/INCOHERENT

### Arc progression
- Current phase: [X]/5
- Progression: [description of how they changed]
- Next step: [anticipation for next chapter]

### Issues identified
- [Any inconsistencies found]
- [Suggestions for correction]

### Coherence score
- Score: [X]/5 coherent contradictions
- Status: ✅ PASS / ❌ FAIL / ⚠️ WARN
```

---

## Workflow Inputs

### Required Inputs

- Chapter number to audit
- Character name to audit
- Chapter text (or reference to chapter file)
- Character dossier (already exists in `characters/`)

---

## Workflow Outputs

### Output Format

- [X] Document-producing (audit reports)

### Output Files

- `tracking/audits/audit-chapter-{N}.md` — **Single consolidated audit file per chapter** containing all character audits, summary table, and coherence scores. All characters appearing in the chapter are audited in one document (batch mode is the default). This file is the canonical record of character coherence for the chapter.

> **Rationale:** A single file per chapter is easier to reference, diff, and review than per-character splits. The summary table at the bottom provides the at-a-glance view; the per-character sections above it provide the detail.

---

## Agent Integration

### Primary Agent

**Continuity Editor** (Quality & Coherence Specialist)

The Continuity Editor already exists and has general continuity checking capabilities. This workflow gives them a structured, character-specific framework.

---

## Implementation Notes

### Critical Features (from AgentAdam analysis):

1. **Consolidated Audit File**: All characters audited in a single `tracking/audits/audit-chapter-{N}.md` file per chapter, with a summary table at the end
2. **Contradiction Checking**: EVERY contradiction (5+) from the character profile must be checked
3. **Pass/Fail System**: ✅/❌ for clear status tracking
4. **Arc Progression Tracking**: Verify characters are actually changing according to their arc
5. **Problem Identification**: Specific suggestions when incoherence is detected

### Example from AgentAdam (section 5 of analysis):
```markdown
## Audit - Chapter 12 - Marc

### Psychological Coherence
- ✅ Contradiction Values vs Actions: Marc hesitates before making a pragmatic decision — COHERENT
- ❌ Contradiction Individualism vs Collectivism: Marc acts too alone without justification — INCOHERENT
- ✅ Contradiction Idealism vs Pragmatism: Marc compromises his ideals — COHERENT

### Issues Identified
- Marc makes a decision without consulting the group (in conflict with his evolution toward collectivism)
- Suggestion: Add a deliberation scene or show his internal conflict
```

---

## When to Use This Workflow

- **After each chapter is written** — Run audit for each character appearing in chapter
- **During revision** — Re-run audits to verify corrections
- **Before final manuscript** — Comprehensive audit of all chapters

---

## Automatic Trigger

> **🎯 AUTOMATIC TRIGGER**
>
> This workflow is **automatically triggered** by the **Chapter-Write** workflow after each chapter is finalized.
>
> **When:** After Step 7 (Finalize) of Chapter-Write
> **Condition:** For each character present in the chapter
> **Mode:** The user can choose to run immediately or defer

**This ensures character coherence is systematically verified after each chapter.**

---

## Future Enhancements

- ~~Batch mode: Audit all characters in a chapter at once~~ *(Now default behavior)*
- Cross-chapter analysis: Identify patterns across multiple chapters
- Metric tracking: Character coherence score over entire manuscript

---

_This is a specification. Use the create-workflow workflow to build this workflow._

**Reference Analysis:** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md` (sections 2, 5, 9, 10)
