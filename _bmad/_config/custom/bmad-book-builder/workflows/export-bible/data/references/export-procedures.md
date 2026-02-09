# Bible Export Formatting Procedures

## Overview

This document outlines the step-by-step procedures for formatting and structuring bible data sections during the export process.

## Formatting Phase Protocol

### Preparation

Before formatting begins, ensure:

1. All 5 bible dimensions have been loaded (step-01-load complete)
2. Output file has been initialized with frontmatter
3. Raw content is stored from source files
4. Metadata (lastUpdated, counts) has been extracted

### Formatting Sequence

Follow this exact sequence for consistent results:

1. **Chronologie Section** - Timeline and events
2. **Lieux Section** - Locations and geography
3. **Objets Section** - Objects and artifacts
4. **Personnes Section** - Characters and relationships
5. **Themes Section** - Thematic elements
6. **Character Summaries Section** - Optional character profiles

### Section Formatting Steps

For each dimension section:

#### Step 1: Create Section Header

- Add section divider (`---`)
- Add H1 heading with dimension name (English + French)
- Add metadata blockquote with last updated date and entity counts
- Add section divider (`---`)

#### Step 2: Process Content

- Check if dimension data exists in loaded data
- If exists: Append complete content from source
- If missing: Append descriptive placeholder
- Preserve all original markdown formatting

#### Step 3: Confirm Completion

- Log section formatted
- Count words if data present
- Note placeholder if data missing

## Output File Management

### Frontmatter Updates

After formatting all sections, update output file frontmatter:

```yaml
stepsCompleted: ['step-01-load', 'step-02-format']
lastStep: 'step-02-format'
date: '{current_date}'
user_name: '{user_name}'
project_name: '{project_name}'
exportType: 'complete-bible'
bibleDimensionsLoaded: {count}
characterSummariesLoaded: {count}
formattingComplete: true
```

### Content Appending

- All formatting is additive - append to existing output file
- Do not overwrite previously formatted sections
- Maintain order: each new section added after previous sections
- Final structure: frontmatter → chronologie → lieux → objets → personnes → themes → character_summaries

## Quality Assurance

### Completeness Checks

After formatting:

- [ ] All 5 dimensions have been processed
- [ ] Each dimension has section header with metadata
- [ ] Placeholders added for missing dimensions
- [ ] All source content preserved (no data loss)
- [ ] Consistent heading structure applied
- [ ] Section dividers between all main sections

### Formatting Validation

Check for:

- Consistent H1/H2/H3 heading usage
- Proper markdown syntax throughout
- Metadata blockquotes correctly formatted
- No truncated content
- All character summaries formatted uniformly

## Status Reporting

### Section Status Indicators

Use these indicators for each section:

- **✅** = Section formatted with content
- **⚠️** = Section has placeholder (missing data)
- **❌** = Section failed to format

### Summary Table Format

After formatting complete, present:

```markdown
### Bible Sections Formatted

| Section | Status | Word Count |
|---------|--------|------------|
| Chronologie | ✅/⚠️ | {count} |
| Lieux | ✅/⚠️ | {count} |
| Objets | ✅/⚠️ | {count} |
| Personnes | ✅/⚠️ | {count} |
| Themes | ✅/⚠️ | {count} |
| Character Summaries | ✅/⚠️ | {count} profiles |

**Total Word Count:** {total_words}
```

## Error Handling

### Missing Source Files

If a dimension source file is missing:

1. Store empty content with exists: false flag
2. Add descriptive placeholder explaining dimension purpose
3. Continue with next dimension
4. Note missing dimensions in final summary

### Malformed Content

If dimension content has formatting issues:

1. Preserve original content as-is
2. Do not attempt to fix formatting in this step
3. Note formatting issues in status summary
4. Source content can be corrected and bible re-exported

### Metadata Extraction Failures

If frontmatter metadata cannot be extracted:

1. Proceed with content formatting
2. Use placeholder values: "Unknown" for dates, 0 for counts
3. Note metadata issues in status summary

## Success Criteria

Formatting phase is successful when:

- All 5 dimensions have section headers in output file
- All existing content preserved (no data loss)
- Missing dimensions have descriptive placeholders
- Output file frontmatter updated with formatting status
- Section order follows standard sequence
- Word counts calculated for each dimension
- Status summary presented to user

## Next Steps

After formatting complete:

1. Present formatting summary with status table
2. Offer option to continue to cross-referencing (step-03)
3. Update frontmatter with step-03 in stepsCompleted array
4. Load and execute step-03-crossref.md
