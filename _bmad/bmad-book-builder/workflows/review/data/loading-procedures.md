# Context Loading Procedures

## Loading Announcement

"**Loading Reference Context...**

I'll now load all available reference files to establish a comprehensive knowledge base for the review. This ensures consistent analysis across all 6 categories.

Loading in progress..."

## Target Chapter Content Loading (CORE)

For each chapter in {targetChapters}:
- Read full chapter text from `{chaptersFolder}/chapter-{N}.md`
- Read chapter metadata from `{chaptersFolder}/chapter-{N}-meta.yaml` if available
- Store as: `chapter_{N}_content`, `chapter_{N}_meta`, `chapter_{N}_summary`

After loading:
"✅ **Target Chapters Loaded:** {count} chapters"
  - Chapters: {list}
  - Total words: {sum}
  - Last chapter: {number/title}

## Chapter Plans Loading (CORE)

Read chapter plan for each target chapter from `{foundationFolder}/chapter-plan-{N}.md`:
- Extract: chapter goals, scene breakdown, key plot points
- Store as: `plan_{N}_goals`, `plan_{N}_scenes`, `plan_{N}_keypoints`

"✅ **Chapter Plans Loaded:** {count} plans"
  - Plans cover: {list}

## Living Bible Loading (CORE - 5 Dimensions)

### Dimension 1: Chronologie (Timeline)
Search: `{bibleFolder}/chronologie.md`
- IF FOUND: Load timeline, events, sequences
- IF MISSING: Note "Timeline dimension not available"
- Store as: `bible_timeline` (or `null` if missing)

### Dimension 2: Lieux (Locations)
Search: `{bibleFolder}/lieux.md`
- IF FOUND: Load locations, descriptions, connections
- IF MISSING: Note "Locations dimension not available"
- Store as: `bible_locations` (or `null` if missing)

### Dimension 3: Objets (Objects)
Search: `{bibleFolder}/objets.md`
- IF FOUND: Load objects, properties, histories
- IF MISSING: Note "Objects dimension not available"
- Store as: `bible_objects` (or `null` if missing)

### Dimension 4: Personnes (Characters)
Search: `{bibleFolder}/personnes.md`
- IF FOUND: Load characters, traits, relationships
- IF MISSING: Note "Characters dimension not available"
- Store as: `bible_characters` (or `null` if missing)

### Dimension 5: Themes (Thematic)
Search: `{bibleFolder}/themes.md`
- IF FOUND: Load themes, motifs, arcs
- IF MISSING: Note "Themes dimension not available"
- Store as: `bible_themes` (or `null` if missing)

"✅ **Living Bible Loaded:** {count}/5 dimensions"
  - Available: {list of available dimensions}
  - Missing: {list of missing dimensions}

## Previous Chapter Summaries Loading (CORE)

Identify chapters BEFORE first target chapter.
Load summaries from `{chaptersFolder}/chapter-{N}-meta.yaml` for all prior chapters:
- Extract: `summary` and `keyPoints` from each
- Store as: `previous_summaries` array

"✅ **Previous Summaries Loaded:** {count} chapters"
  - Chapters: {list}
  - Purpose: Narrative coherence verification

## Style Profile Loading (STRONGLY RECOMMENDED)

Search: `{styleProfilePath}`
- IF FOUND:
  - Load: TTR metrics, sentence length patterns, qualitative traits
  - Store as: `style_profile`
  - "✅ **Style Profile Loaded:** Full metrics available"
- IF MISSING:
  - Note "Style profile not available - quality category limited"
  - Store as: `style_profile: null`
  - "⚠️ **Style Profile Missing:** Quality category will use basic checks only"

## Character Dossiers Loading (OPTIONAL)

Search: `{charactersFolder}/` for psychology files
- IF FOUND:
  - Load all available character psychology/contradiction files
  - Store as: `character_dossiers` (character → data map)
  - "✅ **Character Dossiers Loaded:** {count} characters"
- IF MISSING:
  - Note "Character dossiers not available"
  - Store as: `character_dossiers: {}`

## Thematic Tracking Loading (OPTIONAL)

Search: `{thematicAnalysisPath}`
- IF FOUND:
  - Load: themes, progression, patterns
  - Store as: `thematic_tracking`
  - "✅ **Thematic Tracking Loaded:** Thematic coherence checks enhanced"
- IF MISSING:
  - Note "Thematic tracking not available"
  - Store as: `thematic_tracking: null`

## Previous Reviews Loading (OPTIONAL)

Search: `{reviewReportsFolder}/review-report-*.md`
- IF FOUND:
  - Load all previous review reports
  - Extract: resolved issues, recurring problems
  - Store as: `previous_reviews` array
  - "✅ **Previous Reviews Loaded:** {count} reports - regression check available"
- IF MISSING:
  - Note "No previous reviews found"
  - Store as: `previous_reviews: []`

## Review Quality Assessment

Based on loaded files, determine review quality:

### Complete Quality
- All core files loaded (chapters, plans, Living Bible 5D, previous summaries)
- Style profile loaded
- Character dossiers loaded

### Standard Quality
- All core files loaded
- Style profile loaded

### Limited Quality
- Missing critical core files (e.g., partial Living Bible)
- Or missing style profile

Store as `reviewQuality` in output frontmatter.

## Context Summary Template

"**Context Loading Complete!**

### Review Scope
| Item | Value |
|------|-------|
| Scope | {reviewScope} |
| Target Chapters | {targetChapters} |
| Total Words | {word_count} |

### Core Reference Files
| File | Status | Details |
|------|--------|---------|
| Target Chapters | ✅ | {count} chapters, {words} words |
| Chapter Plans | ✅ | {count} plans |
| Living Bible | ✅/⚠️ | {count}/5 dimensions: {list} |
| Previous Summaries | ✅ | {count} chapters |

### Enhancements
| File | Status | Details |
|------|--------|---------|
| Style Profile | ✅/⚠️ | {status} |
| Character Dossiers | ✅/⚠️ | {count} characters |
| Thematic Tracking | ✅/⚠️ | {status} |
| Previous Reviews | ✅/⚠️ | {count} reports |

### Review Quality Assessment
**Overall Quality: {quality_assessment}**

{quality_notes}

**Ready to proceed to comprehensive analysis.**"

**Select:** `[C]` Continue to Analysis
