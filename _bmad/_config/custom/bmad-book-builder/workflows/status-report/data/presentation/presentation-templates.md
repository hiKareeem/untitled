# Status Report Presentation Templates
# Reference file for step-04-present

This file contains all presentation templates and displays used in the status report presentation step.

## Executive Summary Display Template

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

## Attention Items Display Template

```markdown
## 🎯 Items Needing Attention

### 🔴 High Priority — Immediate Action

{if high_priority_items:
{for each high priority item:
**{category}: {item}**
- Action: {action}
- Why it matters: {rationale}
- Workflow: {workflow_name}
}

}

{if no_high_priority_items:
✅ No high priority items — your project integrity is solid!
}

### 🟡 Medium Priority — This Week

{if medium_priority_items:
{for each medium priority item:
**{category}: {item}**
- Action: {action}
- Timeline: {target_date}
}

}

{if no_medium_priority_items:
✅ No medium priority items — you're maintaining good project health!
}

### ⚪ Low Priority — When Time Permits

{if low_priority_items:
{for each low priority item:
**{category}: {item}**
- Action: {action}
}

}

{if no_low_priority_items:
✅ No low priority items — excellent project organization!
}
```

## Next Steps Display Template

```markdown
## 🚀 Recommended Next Steps

Based on your project status, here's what I recommend:

### Right Now (Today)

1. **{most_important_action}**
   - Use: {workflow_name}
   - Why: {rationale}
   - Expected outcome: {outcome}

### This Week

{next_2_3_priority_items:
2. **{action}**
   - Use: {workflow_name}
   - Timeline: {target}

3. **{action}**
   - Use: {workflow_name}
   - Timeline: {target}
}

### Ongoing Maintenance

{maintenance_items:
- **{action}** — Frequency: {frequency}
- **{action}** — Frequency: {frequency}
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

## Discussion Facilitation Template

```markdown
## 💬 Discussion & Questions

I'm here to help you understand your project status and plan your next steps. You can:

**Ask questions about:**
- Specific sections of this report
- What certain statuses mean
- Why particular items are flagged
- How to prioritize competing tasks
- Which workflows to run and in what order

**Discuss:**
- Your current writing goals and how they align with this status
- Whether you agree with the priorities identified
- Alternative approaches to addressing items
- How to prevent status issues in future work

**Request:**
- More detail on any section of the report
- Clarification on recommendations
- Additional analysis of specific areas
- Guidance on workflow execution

**What would you like to discuss?**
```

## Completion Summary Template

```markdown
## ✅ Status Report Complete

### Report Location

**Full Report:** `{outputFile}`
**Quick Access:** `{latestReportLink}` (always points to latest report)

### Status Summary

- ✅ Project scanned: All directories checked
- ✅ Data analyzed: Status determined for all categories
- ✅ Report generated: Comprehensive status documentation created
- ✅ Findings presented: Key achievements and attention items highlighted
- ✅ Guidance provided: Prioritized next steps established

### Continuous Monitoring

**Recommended Report Frequency:**
- **Active Writing:** Run status report weekly
- **Revision Phase:** Run status report bi-weekly
- **Between Projects:** Run status report monthly

**When to Re-Run:**
- After completing major milestones (chapter, arc, act)
- Before starting revision phases
- When returning to project after break
- When you feel "lost" or overwhelmed
- Before planning next phase of work

### Status Tracking Over Time

Each report creates a timestamped snapshot. You can:
- Compare reports to see progress over time
- Track how attention items change
- Monitor improvement in project health
- Identify patterns in your workflow

---

**Thank you for using the Status Report workflow!** 📚✨

Maintaining visibility across your project helps you write with confidence. Knowing exactly where everything stands allows you to focus on what matters most — creating great stories.

Check back anytime for an updated status snapshot. Your records are always here when you need them.
```

## Closing Statement Template

```markdown
I'm here whenever you need a status update or have questions about your project. Your records are safe, and I'm always happy to help you understand where things stand.

Happy writing! 📚
```
