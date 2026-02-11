# Chapter Finalization Procedures

> **Note:** These procedures are executed as part of step-06-bible-update.
> The chapter is locked as `v1-complete` after all tracking and bible updates are done.

## 1. Chapter Locking Procedure

**Action:** Update chapter frontmatter to lock the chapter

**Frontmatter Updates:**
- Set `status: v1-complete`
- Set `lastStep: 'step-06-bible-update'`
- Ensure `stepsCompleted` includes all 6 steps

**Statistics to Report:**
- Word Count
- Draft Versions
- Audit Status

---

## 2. Synopsis Generation

**Purpose:** Embed a quick reference for continuity checking at the top of the chapter content.

**Based on:** AgentAdam methodology for chapter continuity
**Reference:** `_bmad-output/bmb-creations/analysis/agentadam-vs-bbb-comparison.md`

**Insert Location:** At the TOP of chapter content (right after frontmatter, BEFORE chapter title)

**Synopsis Template:**

```html
<!--
📋 SYNOPSIS - Chapter {chapter_number}

SYNOPSIS: {one_sentence_summary_of_what_happens}

This chapter explores {primary_character}'s {contradiction_type} contradiction through {central_conflict_description}.
{brief_description_of_the_core_conflict_and_its_significance}

**Phase:** {psychological_phase_1_to_5}
**Themes:** {theme_1}, {theme_2}
**Characters present:** {character_list}
**Location:** {where_this_takes_place}

**Key events:**
- {key_event_1}
- {key_event_2}
- {key_event_3}

**Consequences:**
- {what_changes_as_a_result_of_this_chapter}

**Continuity notes for future chapters:**
- {important_detail_1}
- {character_state_change_1}
- {plot_development_1}

**Bible update needed:**
- Chronology: {what_happened_when}
- Locations: {any_location_changes}
- Objects: {objects_introduced_or_removed}
- Characters: {character_state_updates}
- Themes: {thematic_progression}

-->
```

---

## 3. Chapter Summary Generation (CRITICAL)

**Purpose:** Generate comprehensive summary for future chapter continuity and book-level analysis.

**Summary Format:** 2-3 paragraphs

**Content Requirements:**
- Main events of the chapter
- Character developments
- Key decisions or turning points
- How the chapter ends (state of affairs)

**Critical Uses:**
- Writing future chapters (continuity)
- Book-level analysis without reading full text
- Tracking story progression

---

## 4. Key Points Extraction

**Identify and categorize:**

### Key Plot Points:
- Major events that advance the story
- Decisions with consequences
- Revelations or discoveries

### Characters Appearing:
- List all characters who appear
- Note significant character moments

### Locations Used:
- All locations featured in chapter
- Any new locations introduced

### New Elements (Divergences from Plan):
- Anything that emerged during writing not in original plan
- New characters, locations, objects introduced
- Plot variations from plan

---

## 5. Metadata File Generation

**Template Reference:** See `data/metadata-template.yaml` for complete schema

**Fill in Template Structure:**
- Chapter metadata (number, title, word count, POV, timeline)
- Summary (from Section 3)
- Key points (from Section 4)
- Characters, locations, new elements
- Review results (when available)
- Date and author information

---

## 6. Project Tracking Update

**Update** `project-status.yaml`:

```yaml
chapters:
  chapter_{N}:
    title: "{title}"
    status: v1-complete
    pov: "{character}"
    wordCount: {count}
    completedDate: {date}
    metaFile: chapter-{N}-meta.yaml
    mode: {PRESSURE|TEXTURE}
```

Update `completedCount`, `totalWords`, and `lastUpdated`.

---

## 7. Completion Summary

**Present to User:**

```text
Chapter {chapter_number} Complete! 🎉

Final Chapter:
- File: `chapter-{chapter_number}.md`
- Words: {count}
- Status: v1-complete

Metadata Generated:
- File: `chapter-{chapter_number}-meta.yaml`
- Summary: {word count} words
- Key Points: {count}
- Characters: {count}
- Locations: {count}

Project Updated:
- Chapters complete: {total}
- Total words: {running total}

---

Summary Preview:

> {first paragraph of summary}

---

Your chapter is ready! The metadata will help maintain continuity in future chapters.
```

---

## 8. Final Confirmation

**Present to User:**

```text
Chapter Writing Complete

All files saved:
- ✅ `chapter-{N}.md` (final)
- ✅ `chapter-{N}-meta.yaml` (summary + metadata)
- ✅ Project tracking updated

What's Next?
- Write another chapter: Run chapter-write workflow again
- Review the book: Run review workflow
- Continue developing: Return to Foundation workflow

Thank you for writing with me!
```

---

## Success Metrics

**SUCCESS:**
- Chapter text locked with final status
- Comprehensive summary generated
- All key points extracted accurately
- Metadata file created with complete schema
- Project tracking updated
- Clear completion confirmation

**FAILURE:**
- Incomplete summary (missing key events)
- Missing key points or characters
- Not tracking new elements/divergences
- Not updating project tracking
- Leaving status as 'draft'

**Master Rule:** The summary MUST be accurate and complete — future chapters depend on it for continuity.
