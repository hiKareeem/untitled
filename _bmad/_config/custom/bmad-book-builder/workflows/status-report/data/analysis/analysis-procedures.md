# Analysis Procedures
# Reference file for step-02-analyze

This file contains detailed analysis procedures for determining status classifications, currency assessments, and identifying items needing attention.

## Chapter Status Analysis Procedure

**For each planned chapter:**

### Determine Status Logic

```
IF file_exists: true AND status_field: 'complete'
  → Status: Complete

ELSE IF file_exists: true AND (status_field != 'complete' OR no status field)
  → Status: In Draft

ELSE IF file_exists: false
  → Status: Planned
```

### Calculate Chapter Metrics

1. **Total chapters:** Count of `total_planned`
2. **Complete chapters:** Count of chapters with status: Complete
3. **Draft chapters:** Count of chapters with status: In Draft
4. **Planned chapters:** Count of chapters with status: Planned
5. **Total words:** Sum of all `word_counts` from existing chapters
6. **Completion percentage:** `(count_complete / total_planned) × 100`

### Identify Last Complete Chapter

Find highest chapter number with status: Complete

Store as: `last_complete_chapter`

### Store Analysis Results

```yaml
chapter_analysis:
  total_chapters: {total}
  complete: {count}
  in_draft: {count}
  planned: {count}
  completion_percentage: {percent}
  total_words: {words}
  last_complete_chapter: {number}
  chapters: [
    { number, title, status, word_count, modified_date }
  ]
```

---

## Character Arc Status Analysis Procedure

**For each character dossier:**

### Determine Arc Progression

1. Extract arc phase from `arc_phase` field (e.g., "Phase 3/5")
2. Parse current phase (3) and total phases (5)
3. Calculate arc percentage: `(current_phase / total_phases) × 100`

### Cross-Reference Audit Status

1. Check if audit report exists for this character (from scan data)
2. IF audit exists:
   - Get audit date
   - Note as "Last audited: {date}"
3. IF no audit:
   - Note as "No audit completed"

### Store Analysis Results

```yaml
character_analysis:
  total_characters: {count}
  characters: [
    {
      name: {name}
      arc_phase: {phase}
      arc_percentage: {percent}
      last_audited: {date or 'Never'}
      dossier_exists: true
    }
  ]
```

---

## Bible Currency Analysis Procedure

**For each Living Bible dimension:**

### Determine Currency Status Logic

**IF dimension exists:**
1. Compare dimension's `last_chapter_marker` with `last_complete_chapter`
2. Compare dimension's `modified_date` with last complete chapter's date
3. Determine status:

```
IF dimension covers up to last complete chapter
  → Status: Up to date

ELSE IF dimension covers fewer chapters OR modified before last chapter
  → Status: Partial (needs update)
```

4. Store chapter coverage: "Up to Chapter X"

**IF dimension doesn't exist:**
- Status: Missing

### Calculate Bible Metrics

1. **Total dimensions:** 5
2. **Dimensions up to date:** Count of dimensions with status: Up to date
3. **Dimensions partial:** Count of dimensions with status: Partial
4. **Dimensions missing:** Count of dimensions with status: Missing
5. **Bible completion percentage:** `(uptodate / 5) × 100`

### Store Analysis Results

```yaml
bible_analysis:
  total_dimensions: 5
  up_to_date: {count}
  partial: {count}
  missing: {count}
  completion_percentage: {percent}
  dimensions: [
    {
      name: {dimension_name}
      status: {up_to_date|partial|missing}
      chapter_coverage: {coverage or 'N/A'}
      modified_date: {date}
    }
  ]
```

---

## Thematic Tracking Analysis Procedure

**IF theme tracking data exists:**

### For each tracked theme:

1. Extract theme name, progression phase, status
2. Parse phase: "Phase 3/5" → current: 3, total: 5
3. Categorize status: "On track", "Needs attention", "Behind", etc.

### Store Analysis Results

```yaml
theme_analysis:
  tracking_exists: true
  total_themes: {count}
  themes: [
    {
      name: {theme_name}
      progression: {phase}
      status: {on_track|needs_attention|behind}
    }
  ]
```

**IF theme tracking doesn't exist:**

```yaml
theme_analysis:
  tracking_exists: false
  status: "Not started"
```

---

## Rhythm Tracking Analysis Procedure

**IF rhythm tracking exists:**

```yaml
rhythm_analysis:
  tracking_exists: true
  last_updated: {date}
  status: "Active"
```

**IF rhythm tracking doesn't exist:**

```yaml
rhythm_analysis:
  tracking_exists: false
  status: "Not started"
```

---

## Project Health Calculation Procedure

### Overall Completion Calculation

**Weighted components:**
- Chapter completion: 50% weight
- Bible currency: 30% weight
- Character tracking: 10% weight
- Theme/rhythm tracking: 10% weight

### Calculate Overall Health

```
overall_health = (chapter_completion × 0.5) +
                 (bible_completion × 0.3) +
                 (character_tracking × 0.1) +
                 (tracking_status × 0.1)
```

**Where:**
- `character_tracking`:
  - 100% if any characters tracked
  - 50% if partial tracking
  - 0% if none

- `tracking_status`:
  - 100% if both themes and rhythm tracked
  - 50% if one tracked
  - 0% if none tracked

### Determine Health Label

```
90-100%  → Excellent
70-89%   → Good
50-69%   → Fair
30-49%   → Needs Attention
0-29%    → Early Stage
```

### Store Health Analysis

```yaml
health_analysis:
  overall_percentage: {percent}
  overall_label: {label}
  chapter_completion: {percent}
  bible_currency: {percent}
  character_tracking: {percent}
  theme_rhythm_tracking: {percent}
```

---

## Attention Items Identification Procedure

**Generate prioritized list of items needing attention:**

### High Priority (Critical)

Items that threaten project integrity:

- Bible dimensions marked as "Partial" or "Missing"
- Characters with arc phase ahead of last complete chapter (potential inconsistency)
- Significant gaps in story continuity

**Format:**
```yaml
- category: "Bible Currency"
  item: "Chronologie dimension missing"
  action: "Create chronologie dimension and populate with chapter markers"
  priority: "high"
```

### Medium Priority (Important)

Items that affect project quality:

- Draft chapters that haven't been completed
- Characters without audit reports
- Theme tracking marked as "Needs attention" or "Behind"

**Format:**
```yaml
- category: "Character Development"
  item: "Protagonist character not audited"
  action: "Run Character Audit workflow for protagonist"
  priority: "medium"
```

### Low Priority (Nice to have)

Items that improve project organization:

- Rhythm tracking not started
- Missing optional tracking
- Documentation improvements

**Format:**
```yaml
- category: "Tracking Systems"
  item: "Rhythm analysis not started"
  action: "Consider running Rhythm Analysis workflow"
  priority: "low"
```

### Store Attention Items

```yaml
attention_items:
  high_priority: [
    { category, item, action, priority }
  ]
  medium_priority: [
    { category, item, action, priority }
  ]
  low_priority: [
    { category, item, action, priority }
  ]
```

---

## Recent Activity Synthesis Procedure

**Format recent activity for report:**

### For each of the 5 recent files:

1. Determine file type:
   - Chapter → "Chapter"
   - Bible dimension → "Bible"
   - Audit → "Audit"
   - Tracking → "Tracking"
   - Character → "Character"

2. Format date as readable (e.g., "2026-01-24")

3. Create brief description from file name:
   - `chapter-5.md` → "Chapter 5 content"
   - `chronologie.md` → "Timeline updates"
   - `character-audit-protagonist.md` → "Protagonist audit"

### Store Formatted Activity

```yaml
recent_activity_formatted: [
  {
    file: {file_name}
    type: {type}
    date: {readable_date}
    description: {brief}
  }
]
```

---

## Output Frontmatter Update Procedure

**Update {outputFile} frontmatter with analysis results:**

```yaml
stepsCompleted: ['step-01-scan', 'step-02-analyze']
lastStep: 'step-02-analyze'
analysisComplete: true
chapter_completion: {percent}
bible_completion: {percent}
overall_health: {label}
attention_items_count: {total}
```

---

## Analysis Summary Presentation Procedure

### Project Health Overview Table

| Metric | Status |
|--------|--------|
| **Overall Health** | {label} ({percent}%) |
| **Chapter Completion** | {chapter_percent}% ({complete}/{total} chapters) |
| **Bible Currency** | {bible_percent}% ({uptodate}/5 dimensions) |
| **Character Tracking** | {char_count} characters with arc data |
| **Theme/Rhythm Tracking** | {status} |

### Items Needing Attention Table

| Priority | Count | Category |
|----------|-------|----------|
| **High** | {count} | {categories} |
| **Medium** | {count} | {categories} |
| **Low** | {count} | {categories} |

### Summary of Key Findings

Generate 2-3 bullet points highlighting:
- Most significant achievement
- Most critical gap
- Overall trajectory
