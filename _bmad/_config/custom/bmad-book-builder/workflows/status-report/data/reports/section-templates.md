# Status Report Section Templates
# Reference file for step-03-generate and step-04-present

This file contains all report section templates used in the status report workflow.

## Executive Summary Template

```markdown
## Executive Summary

### Project Health: {label} ({percent}%)

| Component | Status | Details |
|-----------|--------|---------|
| **Chapter Progress** | {chapter_percent}% | {complete}/{total} chapters complete |
| **Bible Currency** | {bible_percent}% | {uptodate}/5 dimensions up to date |
| **Character Tracking** | {char_status} | {char_count} characters with arc data |
| **Theme/Rhythm Tracking** | {track_status} | {details} |

### Quick Stats

| Metric | Value |
|--------|-------|
| **Total Chapters** | {total_planned} |
| **Complete Chapters** | {complete} ({percent}%) |
| **Draft Chapters** | {draft} |
| **Planned Chapters** | {planned} |
| **Total Words** | {words:,} |
| **Last Complete Chapter** | {last_complete} |
| **Characters Tracked** | {char_count} |
| **Items Needing Attention** | {attention_total} |

---
```

## Chapter Progress Section Template

```markdown
## Chapter Progress

### Overview

| Status | Count | Percentage |
|--------|-------|------------|
| ✅ **Complete** | {complete} | {complete_percent}% |
| 🟡 **In Draft** | {draft} | {draft_percent}% |
| ⚪ **Planned** | {planned} | {planned_percent}% |

### Chapter Details

| Chapter | Title | Status | Words | Last Modified |
|---------|-------|--------|-------|---------------|
{for each chapter:
| {number} | {title} | {status_icon} {status} | {words:,} | {date} |
}

### Progress Visualization

```
{visual progress bar showing completion}
Example: [████████████████░░░░░░░░] 60% Complete
```

{if completion_percentage < 50:
### ⚠️ Progress Alert

You're in early stages. Consider focusing on completing core chapters before expanding tracking.
}

{if completion_percentage > 50 and completion_percentage < 80:
### 📈 Making Good Progress

You're past the halfway point. Keep momentum going on remaining chapters.
}

{if completion_percentage >= 80:
### 🎯 Almost There

You're in final stages. Focus on completing remaining chapters and polishing.
}

---
```

## Character Arc Status Section Template

```markdown
## Character Arc Status

### Overview

{character_count} characters tracked with arc progression data.

### Character Details

| Character | Arc Progress | Last Audited | Status |
|-----------|--------------|--------------|--------|
{for each character:
| {name} | {arc_phase} ({percent}%) | {audit_date} | {status_icon} |
}

### Arc Analysis

{if all_characters_on_track:
### ✅ Character Arcs On Track

All characters are progressing as expected. Arc phases align with story completion.
}

{if some_characters_behind:
### ⚠️ Arc Alignment Check

The following characters may need attention:
- {list of characters whose arc phase is ahead of story completion}
}

{if no_audits_completed:
### 📋 Audit Recommendation

Consider running Character Audit workflows to validate character consistency and arc progression.
}

---
```

## Bible Currency Section Template

```markdown
## Bible Currency Status

### Overview

| Dimension | Status | Coverage | Last Updated |
|-----------|--------|----------|--------------|
{for each dimension:
| **{name}** | {status_icon} {status} | {coverage} | {date} |
}

### Currency Analysis

{if all_dimensions_up_to_date:
### ✅ Bible Fully Current

All 5 dimensions are up to date through Chapter {last_complete}. Your story bible is in excellent shape.
}

{if some_dimensions_partial:
### 🟡 Update Recommended

The following dimensions need updating:
- {list of partial dimensions}

**Recommendation:** Run Bible Update workflow for these dimensions to incorporate latest chapter content.
}

{if some_dimensions_missing:
### ⚪ Missing Dimensions

The following dimensions haven't been created yet:
- {list of missing dimensions}

**Recommendation:** Create these dimensions to establish complete story reference documentation.
}

### Dimension Details

{for each dimension:
#### {name}

**Status:** {status}
**Coverage:** {coverage}
**Last Modified:** {date}

{if status == 'partial':
This dimension covers chapters through {coverage}, but your last complete chapter is {last_complete}. Update needed.
}

{if status == 'missing':
This dimension hasn't been created yet. Essential for tracking {dimension_purpose}.
}

}

---
```

## Thematic Tracking Section Template

```markdown
## Thematic Tracking

### Overview

{if theme_tracking_exists:
{theme_count} themes tracked with progression data.

| Theme | Progression | Status |
|-------|-------------|--------|
{for each theme:
| {name} | {phase} | {status_icon} {status} |
}

### Theme Analysis

{if all_themes_on_track:
### ✅ Thematic Development On Track

All themes are progressing as expected. Good alignment with story completion.
}

{if some_themes_need_attention:
### ⚠️ Themes Needing Attention

The following themes may need review:
- {list of themes with 'needs_attention' or 'behind' status}

**Recommendation:** Review theme progression and consider reinforcing in upcoming chapters.
}

}

{if no_theme_tracking:
### 📋 Thematic Tracking Not Started

No theme tracking data found.

**Recommendation:** Consider running Theme Tracker workflow to monitor thematic development across your narrative.
}

---
```

## Rhythm & Pacing Section Template

```markdown
## Rhythm & Pacing Analysis

### Status

{if rhythm_tracking_exists:
### ✅ Rhythm Tracking Active

**Last Updated:** {date}

Rhythm and pacing analysis is being tracked. Use Rhythm Analysis workflow for detailed pacing reports.

**Next Steps:**
- Review latest rhythm analysis for pacing patterns
- Compare pacing across completed chapters
- Identify and address pacing inconsistencies
}

{if no_rhythm_tracking:
### 📋 Rhythm Tracking Not Started

No rhythm or pacing tracking data found.

**Recommendation:** Consider running Rhythm Analysis workflow to monitor narrative pacing and rhythm patterns.

**Benefits:**
- Identify pacing inconsistencies
- Track tension curves across scenes
- Validate rhythm matches story beats
}

---
```

## Recent Activity Section Template

```markdown
## Recent Activity

### Last 5 Updates

| Date | File | Type | Description |
|------|------|------|-------------|
{for each recent file:
| {date} | {file_name} | {type} | {description} |
}

### Activity Summary

{analysis of recent activity:
- "Most recent work focused on {focus_area}"
- "{count} files updated in the last {timeframe}"
- "Activity concentrated on {category}"
}

---
```

## Attention Items Section Template

```markdown
## Items Needing Attention

### 🔴 High Priority ({count})

{if high_priority_items:
These items require immediate attention to maintain project integrity and consistency.

{for each high priority item:
- **{category}:** {item}
  - Action: {action}
  - Why: {rationale}
}

}

{if no_high_priority_items:
✅ No high priority items. Great work keeping your project in good shape!
}

### 🟡 Medium Priority ({count})

{if medium_priority_items:
These items are important for project quality and should be addressed soon.

{for each medium priority item:
- **{category}:** {item}
  - Action: {action}
  - Why: {rationale}
}

}

{if no_medium_priority_items:
✅ No medium priority items.
}

### ⚪ Low Priority ({count})

{if low_priority_items:
These items are nice-to-have improvements but not urgent.

{for each low priority item:
- **{category}:** {item}
  - Action: {action}
  - Why: {rationale}
}

}

{if no_low_priority_items:
✅ No low priority items.
}

---
```

## Recommendations Section Template

```markdown
## Recommendations

Based on your project status, here are prioritized next steps:

### Immediate Actions (This Week)

{top 3 high-priority items with specific actions:
1. **{action}** — {item}
   - Workflow to use: {workflow_name}
   - Expected outcome: {outcome}

2. **{action}** — {item}
   - Workflow to use: {workflow_name}
   - Expected outcome: {outcome}

3. **{action}** — {item}
   - Workflow to use: {workflow_name}
   - Expected outcome: {outcome}
}

### Short-Term Goals (This Month)

{next 3 medium-priority items with timeline:
1. **{action}** — {item}
   - Target: {timeline}

2. **{action}** — {item}
   - Target: {timeline}

3. **{action}** — {item}
   - Target: {timeline}
}

### Long-Term Goals (Ongoing)

{ongoing maintenance items:
1. **{action}** — {item}
   - Frequency: {frequency}

2. **{action}** — {item}
   - Frequency: {frequency}
}

### Workflow Integration Guide

Based on your current status, recommended workflow sequence:

{prioritized workflow recommendations:
1. **{workflow}** — {reason}
2. **{workflow}** — {reason}
3. **{workflow}** — {reason}
}

---
```

## Report Footer Template

```markdown
---

## Report Metadata

**Report Generated:** {current_date} at {current_time}
**Reporter:** Character Keeper (Marie) 📚
**Project:** {project_name}
**Report Type:** Comprehensive Status Report
**Report ID:** status-report-{date}

### Data Sources

This report synthesized data from:
- Chapter files and metadata in `{chaptersFolder}/`
- Character dossiers in `{charactersFolder}/`
- Living Bible dimensions in `{bibleFolder}/`
- Character audit reports in `{auditsFolder}/`
- Tracking data in `{trackingFolder}/`

### Next Status Report

Run Status Report workflow again to get an updated snapshot. Recommended frequency:
- **Active writing:** Weekly
- **Revision phase:** Bi-weekly
- **Between projects:** Monthly

---

_This report was generated by the Status Report workflow of the bmad-book-builder module. For questions or clarification, consult your Character Keeper agent._
```

## Presentation Summary Template

```markdown
## 📊 Project Status Summary

**Report Date:** {date}
**Project:** {project_name}
**Reporter:** Marie, Character Keeper 📚

### Overall Project Health: {label} ({percent}%)

| Component | Status | Details |
|-----------|--------|---------|
| **Chapter Progress** | {chapter_percent}% | {complete}/{total} chapters complete |
| **Bible Currency** | {bible_percent}% | {uptodate}/5 dimensions up to date |
| **Character Tracking** | {char_status} | {char_count} characters tracked |
| **Theme/Rhythm Tracking** | {track_status} | {details} |

### Quick Stats

- **Total Chapters:** {total_planned}
- **Complete:** {complete} | **In Draft:** {draft} | **Planned:** {planned}
- **Total Words:** {words:,}
- **Last Complete Chapter:** {last_complete}
- **Characters Tracked:** {char_count}
- **Items Needing Attention:** {attention_total}
```

## Key Achievements Template

```markdown
## 🎉 Key Achievements

{analyze report for positive achievements:

**Chapter Progress:**
{if completion_percentage > 0:
- ✅ You've completed {complete} chapters ({words:,} words!)
{if completion_percentage > 50:
- ✅ More than halfway through your manuscript!
}
{if completion_percentage > 75:
- ✅ In the home stretch — final stretch ahead!
}
}

**Bible Management:**
{if bible_completion > 0:
- ✅ {uptodate}/5 dimensions maintained
{if bible_completion == 100:
- ✅ All dimensions current — excellent reference documentation!
}
}

**Character Work:**
{if char_count > 0:
- ✅ Tracking {char_count} characters with arc data
{if all_characters_on_track:
- ✅ All character arcs progressing as expected
}
}

**Tracking Systems:**
{if theme_tracking_exists:
- ✅ Thematic tracking established
}
{if rhythm_tracking_exists:
- ✅ Rhythm analysis active
}
}

### Project Momentum

{assess momentum based on recent activity:
{if recent_activity_shows_consistent_work:
**Strong Momentum:** You've been consistently working across multiple areas. Keep it up!
}

{if recent_activity_limited:
**Building Momentum:** Focus on completing current chapter to maintain progress.
}

{if recent_activity_show_gaps:
**Restarting Momentum:** Recent activity shows you're getting back into the flow. Great!
}
}
```

## Workflow Guidance Template

```markdown
## 📚 Workflow Guidance

Based on your current status, here are the workflows that would be most valuable:

### Recommended Workflows

{analyze status and recommend workflows:

{if bible_dimensions_need_update:
**1. Bible Update**
- Priority: High
- Which dimensions: {list}
- Why: Ensures your reference documentation stays current with latest chapters
- Trigger: Use `[BU]` from my menu
}

{if chapters_need_completion:
**2. Chapter Write**
- Priority: High
- Which chapters: {list of planned chapters}
- Why: Continue making progress on your manuscript
- Trigger: Chapter workflow from Story Architect
}

{if characters_need_audit:
**3. Character Audit**
- Priority: Medium
- Which characters: {list}
- Why: Validate character consistency and arc progression
- Trigger: Character Audit workflow
}

{if themes_need_tracking:
**4. Theme Tracker**
- Priority: Medium
- Why: Monitor thematic development across your narrative
- Trigger: Theme Tracker workflow
}

{if rhythm_not_tracked:
**5. Rhythm Analysis**
- Priority: Low
- Why: Understand pacing patterns and identify inconsistencies
- Trigger: Rhythm Analysis workflow
}
}

### My Available Workflows

As your Character Keeper, I can help you with:
- **[BC] Build Characters** — Create comprehensive character dossiers
- **[BU] Bible Update** — Update story bible from latest chapters
- **[EB] Export Bible** — Export formatted story bible
- **[RC] Review Continuity** — Chapter-by-chapter continuity review
- **[SB] Search Bible** — Search story bible for specific information
- **[SR] Status Report** — Generate this status report

Just ask me to run any of these workflows!
```
