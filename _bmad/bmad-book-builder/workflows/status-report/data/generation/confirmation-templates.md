# Report Generation Confirmation Templates
# Reference file for step-03-generate

This file contains templates for confirming successful report generation.

## Report Generation Confirmation Template

```markdown
**Report Generated Successfully!**

### Report Details

| Item | Value |
|------|-------|
| Output File | {outputFile} |
| Latest Link | {latestReportLink} |
| Project Health | {label} ({percent}%) |
| Chapter Completion | {chapter_percent}% |
| Bible Currency | {bible_percent}% |
| Attention Items | {total} items |

### Report Structure

✅ Executive Summary
✅ Chapter Progress ({complete}/{total} chapters)
✅ Character Arc Status ({char_count} characters)
✅ Bible Currency ({uptodate}/5 dimensions)
✅ Thematic Tracking ({status})
✅ Rhythm & Pacing Analysis ({status})
✅ Recent Activity (5 updates)
✅ Items Needing Attention ({total} items)
✅ Prioritized Recommendations
✅ Report Metadata

### Access Your Report

**Full Report:** `{outputFile}`
**Quick Access:** `{latestReportLink}` (always latest)

{if overall_health == 'Excellent':
**🎉 Excellent!** Your project is in great shape. Keep up the fantastic work!
}

{if overall_health == 'Good':
**✅ Good Progress!** Your project is on track. Address the attention items to maintain momentum.
}

{if overall_health == 'Fair':
**📊 Fair Progress.** You're making progress but have some gaps to address. Focus on high-priority items.
}

{if overall_health in ['Needs Attention', 'Early Stage']:
**⚠️ Attention Needed.** Your project needs focus on key areas. Start with high-priority recommendations.
}

**Report ready for presentation.**

**Select:** `[C]` Continue to Presentation
```

## Latest Status Link Creation Template

**Option A: Symlink (Unix/Mac)**
```bash
ln -sf {outputFile} {latestReportLink}
```

**Option B: Copy**
- Copy content from {outputFile} to {latestReportLink}

This ensures `latest-status.md` always points to the most recent report.
