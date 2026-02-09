# Workflow Specification: RealityCheck

**Module:** bmad-book-builder
**Status:** Specification — New workflow
**Created:** 2026-01-24
**Priority:** P2 (Specialized Feature — Factual Verification)

---

## Workflow Overview

**Goal:** Verify factual and technical accuracy in story elements

**Description:** Documentaliste (Research & Fact Specialist) analyzes story content for factual inconsistencies, technical inaccuracies, or unrealistic details. Uses web browsing to verify information when needed.

**Workflow Type:** Create-only (verification per chapter or scene)

---

## Why This Workflow Exists

> **🎯 NEW WORKFLOW — Reality Consistency Verification**
>
> Credible stories require factual accuracy. Technical errors (jobs, procedures, tools) or factual errors break reader immersion.
>
> **Example:** "You can't cut down a tree with a hammer" — the kind of error this workflow should detect.
>
> **Capabilities:** Web browsing for validation, research dossiers as references.

---

## Workflow Structure

### Entry Point

```yaml
---
name: reality-check
description: Verify factual and technical accuracy in story
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/reality-check'
---
```

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Select Scope | Choose what to verify (chapter, scene, specific element) |
| 2 | Extract Claims | Identify factual/technical claims to verify |
| 3 | Check References | Consult existing research dossiers |
| 4 | Web Verification | Use web browsing for unknown facts (when needed) |
| 5 | Identify Issues | Flag inaccuracies or inconsistencies |
| 6 | Provide Corrections | Suggest accurate alternatives |

---

## Reality Check Categories

### 1. Technical Accuracy
- Professions/trades — Are procedures correct?
- Tools/equipment — Are they used correctly?
- Technical processes — Is the sequence realistic?

### 2. Factual Accuracy
- Historical facts — Dates, events, figures
- Geographic details — Locations, distances, features
- Scientific facts — Physics, biology, chemistry basics

### 3. Logical Consistency
- Cause and effect — Do actions logically lead to results?
- Time sequences — Are timelines realistic?
- Physical constraints — Do characters respect limits?

---

## Example Issues Detected

```markdown
## Reality Check Report — Chapter 12

### ❌ Issue 1: Technical Inaccuracy
**Location:** Scene where Marc performs surgery
**Problem:** Marc (engineer) performs complex medical procedure without proper training
**Severity:** HIGH — Breaks credibility
**Suggestion:** Either make Marc have medical background, or have him assist actual doctor

### ✅ Verified: Medical Tools
**Location:** Same scene
**Claim:** Use of specific surgical instruments
**Status:** Verified accurate via research
**Source:** Medical reference documentation

### ❌ Issue 2: Physical Impossibility
**Location:** Chase scene on rooftops
**Problem:** Character jumps 15-meter gap (unrealistic for normal human)
**Severity:** MEDIUM — Stretches believability
**Suggestion:** Reduce to 5-6 meters, or add justification (adrenaline, parkour training)
```

---

## Workflow Inputs

### Required Inputs

- Story content (chapter, scene, or excerpt)
- Specific elements to check (optional — can scan entire content)

---

## Workflow Outputs

### Output Format

- [X] Document-producing (reality check report)

### Output Files

- `reality-check/chapter-{XX}-report.md` — Verification report
- `research/dossiers/{topic}-facts.md` — New research dossiers created (if needed)

---

## Agent Integration

### Primary Agent

**Documentaliste** (Research & Fact Specialist)

The Documentaliste has web browsing capabilities and manages research dossiers.

---

## When to Use This Workflow

- **After writing technical scenes** — Medical, legal, engineering, etc.
- **Before final manuscript** — Comprehensive reality check
- **When beta readers flag issues** — Investigate specific concerns
- **During planning** — Verify concepts before writing

---

## Implementation Notes

### Web Browsing Usage:

Use web browsing **only when**:
- Existing research dossiers don't cover the topic
- High-stakes technical claims need verification
- Historical/scientific facts are uncertain

Create new research dossiers when:
- Topic will recur in story
- Complex technical domain is involved
- Multiple facts need tracking

### Severity Levels:

- **HIGH**: Breaks story credibility, must fix
- **MEDIUM**: Stretches believability, should address
- **LOW**: Minor nitpick, optional fix
- **INFO**: Verified accurate, no issue

---

## Integration with Other Workflows

- **Research** — Creates dossiers used by reality-check
- **Review** — Can include reality check as part of comprehensive review
- **Documentaliste agent** — Direct commands for quick fact checks

---

## Example Use Cases

1. **Medical scene verification** — Are procedures, instruments accurate?
2. **Historical fiction check** — Are dates, events, figures correct?
3. **Technical dialogue review** — Would this character actually say this?
4. **Location verification** — Is this place real? Are features accurate?
5. **Procedure validation** — Is this how this profession actually works?

---

## Research Dossier Creation

When new information is verified, create research dossier:

```markdown
# Research Dossier: [Topic]

## Verified Facts
- Fact 1: [Description]
- Fact 2: [Description]
- Fact 3: [Description]

## Sources
- Source 1: [URL or reference]
- Source 2: [URL or reference]

## Story Applications
- Chapter 12: [How this fact appears]
- Chapter 15: [How this fact appears]

## Notes
[Any additional context, warnings, or caveats]
```

---

_This is a specification. Use the create-workflow workflow to build this workflow._
