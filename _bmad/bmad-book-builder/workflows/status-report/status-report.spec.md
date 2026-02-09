# Workflow Specification: StatusReport

**Module:** bmad-book-builder
**Status:** Specification — Corrected (Agent assigned)
**Created:** 2026-01-24
**Updated:** 2026-01-24
**Priority:** P2 (Utility Feature — Project Overview)

---

## Workflow Overview

**Goal:** Generate comprehensive project status report

**Description:** Character Keeper compiles a complete overview of project progress — chapters written, word counts, character dossiers created, tracking status, and identifies next steps to keep the project moving forward.

**Workflow Type:** Create-only (report generation)

---

## Why This Workflow Exists

> **🎯 PROJECT STATUS REPORT**
>
> Long-form writing projects need a high-level view to track progress. Status-Report provides a comprehensive dashboard of project status.
>
> **Integrated with Character Keeper** — The bible guardian is best positioned to know the overall project state.

---

## Workflow Structure

### Entry Point

```yaml
---
name: status-report
description: Generate comprehensive project status report
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/status-report'
---
```

---

## Planned Steps

| Step | Name | Goal |
|------|------|------|
| 1 | Gather Metrics | Count chapters, words, characters, tracking files |
| 2 | Check Bible Status | Verify story bible completeness |
| 3 | Analyze Progress | Compare against plan/outline |
| 4 | Identify Gaps | Find missing elements (characters, themes, etc.) |
| 5 | Suggest Next Steps | Recommend what to work on next |
| 6 | Generate Report | Create comprehensive status document |

---

## Status Report Structure

```markdown
# Project Status Report — [Project Name]
**Generated:** [Date]

## Executive Summary
- Total chapters: [X] / [Y] planned ([Z]% complete)
- Total word count: [XXX,XXX] words
- Project phase: [Foundation / Writing / Revision / Finalization]

## Chapter Progression
| Chapter | Status | Word Count | Last Updated |
|---------|--------|------------|--------------|
| 1 | ✅ Complete | 4,500 | 2026-01-20 |
| 2 | ✅ Complete | 5,200 | 2026-01-22 |
| 3 | 🟡 In Draft | 3,100 | 2026-01-24 |
| 4 | ⚪ Planned | - | - |

## Character Dossiers
| Character | Status | Arc Progress | Audits Complete |
|-----------|--------|--------------|-----------------|
| Marc | ✅ Complete | Phase 3/5 | Ch. 1-12 |
| Julie | ✅ Complete | Phase 2/5 | Ch. 1-10 |
| Chen | 🟡 In Progress | Phase 2/5 | Ch. 1-8 |

## Story Bible Status
- ✅ Chronology: Up to date through Chapter 12
- ✅ Characters: All characters tracked
- 🟡 Locations: 3/5 locations documented
- ⚪ Objects: Not started

## Thematic Tracking
| Theme | Progression | Status |
|-------|-------------|--------|
| Trust vs Distrust | Phase 3/5 | On track |
| Individualism vs Collectivism | Phase 2/5 | Needs attention |
| Survival vs Sacrifice | Phase 1/5 | Just started |

## Recent Activity
- [Latest actions taken]

## Identified Gaps
- [Missing elements that need attention]

## Recommended Next Steps
1. [Priority 1 action]
2. [Priority 2 action]
3. [Priority 3 action]
```

---

## Workflow Inputs

### Required Inputs

- Project context (scan project files)
- Chapter plan (from Foundation workflow)

---

## Workflow Outputs

### Output Format

- [X] Document-producing (status report)
- [X] Display summary (show to user)

### Output Files

- `reports/status-[date].md` — Complete status report
- `reports/latest-status.md` — Always contains latest report

---

## Agent Integration

### Primary Agent

**Character Keeper** (Bible Guardian)

The Character Keeper manages the story bible and is best positioned to provide a complete project overview.

### Menu Command

Add to Character Keeper menu:
```
[SR] Status Report — Generate comprehensive project status
```

---

## When to Use This Workflow

- **Weekly project review** — Check overall progress
- **After completing major milestones** — Chapter 5, 10, 15, etc.
- **When feeling lost** — Get clarity on what to work on next
- **Before planning sessions** — Know where you are before planning where to go
- **Project kickoff** — Establish baseline (will show mostly zeros)

---

## Implementation Notes

### Scan Locations:

The workflow should scan:
- `chapters/` — For chapter files and metadata
- `characters/` — For character dossiers
- `bible/` — For story bible status
- `audits/` — For character audit completion
- `tracking/` — For theme and rhythm tracking

### Progress Calculation:

- **Chapter completion:** Files marked as complete vs planned
- **Word count:** Sum of all chapter word counts
- **Bible completeness:** Which sections exist and are up-to-date
- **Character arc progress:** From character dossiers

---

## Integration with Other Workflows

This workflow provides overview data that complements:
- **Foundation** — Shows how many chapters planned vs written
- **Build-Characters** — Shows which character dossiers are complete
- **Bible-Update** — Uses bible status for report
- **Audit-Project** — More detailed audit vs this high-level overview

---

_This is a specification. Use the create-workflow workflow to build this workflow._

**Agent Assignment:** Character Keeper (Bible Guardian)
**Menu Command:** SR → Status Report
