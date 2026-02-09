# Initialization Procedures

## Welcome Message

"**Welcome to the Review workflow!**

I'm your Continuity Editor, and I'll help you validate the coherence and quality of your chapter(s). I'll check for:

- **Character Consistency** — Personality, voice, motivations, descriptions
- **Location Accuracy** — Descriptions, geography, setting details
- **Object Tracking** — Items, weapons, tools, possession timeline
- **Timeline Validation** — Event order, time passage, cause-and-effect
- **Plot Hole Detection** — Narrative logic, loose ends, contradictions
- **Quality Issues** — Repetition, dialogue, scene purpose, pacing

Let's get started by determining the scope of your review."

## Scope Selection Options

"**What would you like to review?**

**[S]** Single Chapter — Review one specific chapter
**[M]** Multiple Chapters — Review a range of chapters
**[F]** Full Manuscript — Review all completed chapters

Please select: [S]ingle / [M]ultiple / [F]ull"

## Scope Gathering Procedures

### Single Scope
"Which chapter would you like to review? Please provide the chapter number (e.g., 3):"
Store as `{target_chapters}` (single number array).

### Multiple Scope
"Which chapter range would you like to review? Please provide start and end (e.g., 3-7):"
Store as `{target_chapters}` (array of numbers in range).

### Full Scope
Scan {chaptersFolder} for all chapter files. Store as `{target_chapters}` (all chapter numbers found).

### Scope Confirmation
"**Review Scope Confirmed:**
- Scope: {review_scope}
- Target Chapters: {target_chapters}"

## File Detection Procedures

### Core Required Files

#### Chapter Plan Detection
Search: `{foundationFolder}/chapter-plan-*.md`
- IF FOUND: "✅ Chapter plans found"
- IF MISSING: "❌ Chapter plans not found. Please run Foundation workflow first."

#### Living Bible Detection
Search: `{bibleFolder}/` for:
  - `chronologie.md` (Timeline)
  - `lieux.md` (Locations)
  - `objets.md` (Objects)
  - `personnes.md` (Characters)
  - `themes.md` (Themes)

Count found files:
- IF 5 FOUND: "✅ Living Bible complete (all 5 dimensions)"
- IF 1-4 FOUND: "⚠️ Living Bible partial ({count}/5 dimensions found: {list})"
- IF 0 FOUND: "❌ Living Bible not found. This is critical for thorough review."

#### Previous Chapter Summaries Detection
Search: `{chaptersFolder}/chapter-*-meta.yaml` for chapters BEFORE first target chapter
- IF FOUND: "✅ Previous chapter summaries found ({count} chapters)"
- IF NONE: "⚠️ No previous chapter summaries found. Narrative coherence verification will be limited."

### Strongly Recommended Files

#### Style Profile Detection
Search: `{styleProfilePath}`
- IF FOUND: "✅ Style profile found (quality metrics available)"
- IF MISSING: "⚠️ Style profile not found. Quality category will be limited."

### Optional Files

#### Character Dossiers Detection
Search: `{bbb_output_folder}/characters/` for psychology files
- IF FOUND: "✅ Character dossiers found ({count} characters)"
- IF MISSING: "Note: Character dossiers not found (optional enhancement)"

#### Thematic Tracking Detection
Search: `{bbb_output_folder}/thematic-analysis.md`
- IF FOUND: "✅ Thematic tracking found"
- IF MISSING: "Note: Thematic tracking not found (optional enhancement)"

#### Previous Reviews Detection
Search: `{bbb_output_folder}/review/review-report-*.md`
- IF FOUND: "✅ Previous reviews found ({count} reports)"
- IF MISSING: "Note: No previous reviews (optional for regression check)"

## File Discovery Results Template

"**File Discovery Results**

### Core Required Files

| File | Status | Notes |
|------|--------|-------|
| Chapter Plans | ✅/❌ | {status} |
| Living Bible (5D) | ✅/⚠️/❌ | {count}/5 dimensions |
| Previous Summaries | ✅/⚠️ | {status} |

### Strongly Recommended

| File | Status | Notes |
|------|--------|-------|
| Style Profile | ✅/⚠️ | {status} |

### Optional Enhancements

| File | Status | Notes |
|------|--------|-------|
| Character Dossiers | ✅/⚠️ | {status} |
| Thematic Tracking | ✅/⚠️ | {status} |
| Previous Reviews | ✅/⚠️ | {status} |

**Review Quality Assessment:**
- Complete: All core + strongly recommended files found
- Standard: All core files found
- Limited: Missing critical files (recommend completion first)"

## Missing Living Bible Handling

"**Living Bible Incomplete**

The Living Bible is critical for thorough review. I can help you create the missing dimensions.

Would you like to:
**[C]** Create missing Living Bible dimensions now
**[P]** Proceed with available files (review quality will be limited)

Please select: [C]reate / [P]roceed"

### Create Option Response
"Please run the Living Bible workflow first to create the missing dimensions:
```
create living-bible
```

Then return to this review workflow."

→ STOP workflow

### Proceed Option Response
"Proceeding with available files. Review quality will be limited by missing Living Bible dimensions."
→ Continue to next step

## Output File Initialization

Create new review report file from {reportTemplate}:

- Set `scope: {review_scope}`
- Set `targetChapters: {target_chapters}`
- Set `date: {current_date}`
- Set `user_name: {user_name}`
- Set `reviewType: 'comprehensive'`
- Set `stepsCompleted: ['step-01-init']`
- Set `lastStep: 'step-01-init'`
- Initialize `reviewQuality: 'unknown'` (will be updated in step 2)
- Initialize `issuesFound: 0`
- Initialize counters to 0

## Initialization Summary Template

"**Initialization Complete!**

| Item | Value |
|------|-------|
| Review Scope | {review_scope} |
| Target Chapters | {target_chapters} |
| Living Bible | {count}/5 dimensions |
| Style Profile | {status} |
| Previous Summaries | {count} chapters |
| Review Quality | {quality_assessment} |

**Ready to proceed to context loading.**"

**Select:** `[C]` Continue to Load Context
