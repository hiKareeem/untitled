---
name: Load Content
description: Load selected chapter content and prepare data
nextStepFile: step-03-analyze.md
---

# Step 02: Load Content

## Objective

Load the selected chapter content and prepare data for analysis.

---

## Instructions for the Agent

### 1. Load Chapter Files

For each chapter in `chapters_to_analyze`:

```
Reading files...
```

Use the Read tool to load:
- The full chapter content
- Metadata (if present in frontmatter)

### 2. Extract Basic Metrics

For each chapter, calculate:

| Metric | Description |
|----------|-------------|
| `word_count` | Total word count |
| `paragraph_count` | Number of paragraphs |
| `scene_count` | Number of scenes (delimited by `---` or `###`) |
| `dialogue_ratio` | Percentage of dialogue vs narration |
| `avg_sentence_length` | Average sentence length |

> **Reference:** See `data/references/pacing-analysis-framework.md` for detailed metric definitions and calculation methods.

### 3. Identify Scenes

Parse the chapter to identify:
- Scene delimiters (separators, section headings)
- The start and end of each scene
- Characters present per scene

Data structure:
```
scenes:
  - id: 1
    title: {title_or_description}
    start_line: {n}
    end_line: {n}
    word_count: {n}
    characters: [{list}]
    location: {location}
```

### 4. Load Supplemental Context (if available)

Try to load:
- `story-bible.md` - Expected narrative structure
- Previous chapters (for comparison if scope = single)
- Previous `analysis/rhythm-*.md` files (for trends)

### 5. Confirm Loading

Display a summary:

```
Content loaded for analysis:

📖 Chapter {N}: "{title}"
   - {word_count} words
   - {scene_count} scenes identified
   - {paragraph_count} paragraphs
   - Dialogue ratio: {percentage}%

Ready for rhythm analysis.
```

---

## Validation

Before continuing:
- [ ] All chapters loaded successfully
- [ ] Basic metrics calculated
- [ ] Scenes identified and delimited
- [ ] Supplemental context loaded (if available)

---

## Navigation

**Previous step:** [Step 01: Init](step-01-init.md)
**Next step:** [Step 03: Analyze](step-03-analyze.md)

---

## Error Handling

- **File not found:** Return to Step 01 to reselect
- **Empty file:** Notify and offer to skip or wait
- **Unexpected format:** Try to parse as best as possible, report anomalies
