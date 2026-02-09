# Step 01: Load Context

**Goal:** Load the completed chapter and existing bible files to prepare for extraction.

**Duration:** 1-2 minutes

---

## What You'll Do

1. Identify which chapter to analyze (auto-detect or user-provided)
2. Load chapter content
3. Load all 5 bible dimension files
4. Check for previous extraction of this chapter
5. Validate that all prerequisites are met

---

## Process

### A. Identify Chapter

**If `chapter_path` provided:**
- Use the provided path directly
- Extract chapter number from filename (e.g., `chapitre-05.md` → 5)

**If `chapter_number` provided:**
- Construct path: `{project-root}/chapters/chapitre-{XX}.md`
- Verify file exists

**If neither provided (auto-detect):**
- Use Glob to find all chapters: `{project-root}/chapters/chapitre-*.md`
- Sort by filename to find highest number
- Use most recent chapter as default
- Confirm with user: "Analyzing Chapitre {XX}. Correct? [Y/n]"

### B. Load Chapter Content

Use Read tool:
```
Read {project-root}/chapters/chapitre-{XX}.md
```

**Validate:**
- File exists and is readable
- Content is not empty
- Chapter appears complete (has expected structure)

**Error handling:**
- File not found → Ask user for correct path
- File empty or corrupted → Error: "Chapter file is unreadable. Please verify file integrity."
- Chapter appears incomplete → Warning, but proceed (user may want to extract partial)

### C. Load Bible Files

Load all 5 dimension files using Read tool:

1. `{project-root}/bible/chronologie.md`
2. `{project-root}/bible/personnes.md`
3. `{project-root}/bible/lieux.md`
4. `{project-root}/bible/objets.md`
5. `{project-root}/bible/themes.md`

**Validate:**
- All 5 files exist
- Files have expected structure (frontmatter + sections)

**Error handling:**
- Any file missing → **STOP** with error:
  ```
  ❌ Story bible not found.

  Expected structure:
  {project-root}/bible/
    ├── chronologie.md
    ├── personnes.md
    ├── lieux.md
    ├── objets.md
    └── themes.md

  Please run Foundation workflow first to create bible structure.
  ```

### D. Check Previous Extraction

Check if extraction record already exists:

Use Glob:
```
{project-root}/bible/extractions/chapitre-{XX}.md
```

**If exists:**
- Read the previous extraction
- Display warning:
  ```
  ⚠️  Previous extraction found for Chapitre {XX}

  Last extracted: {timestamp from frontmatter}

  This will re-extract and may overwrite changes.
  Continue? [Y/n]
  ```
- If user says no → Abort workflow
- If user says yes → Store previous_extraction for reference

**If not exists:**
- Set `previous_extraction = null`
- Proceed normally

### E. Prepare Context Summary

Display loaded context:

```markdown
📚 Context Loaded - Chapitre {XX}

**Chapter:**
- Path: {full path}
- Word count: ~{approximate word count}
- Structure: {brief note on sections/scenes if obvious}

**Bible Status:**
- Chronologie: {number of existing events/entries}
- Personnes: {number of existing characters}
- Lieux: {number of existing locations}
- Objets: {number of existing objects}
- Thèmes: {number of existing themes}

**Previous Extraction:**
{If exists: summary of what was previously extracted}
{If not: "First extraction for this chapter"}

✅ Ready for extraction
```

---

## Outputs (passed to Step 02)

Store the following in workflow context:

```yaml
chapter_number: {XX}
chapter_content: {full chapter text}
chapter_path: {absolute path}
bible_data:
  chronologie: {content of chronologie.md}
  personnes: {content of personnes.md}
  lieux: {content of lieux.md}
  objets: {content of objets.md}
  themes: {content of themes.md}
previous_extraction: {content if exists, null otherwise}
project_root: {detected project root path}
```

---

## Tools Used

- **Glob** - Find chapter files, check for previous extraction
- **Read** - Load chapter and bible files
- **AskUserQuestion** (if needed) - Confirm chapter, handle previous extraction warning

---

## Success Criteria

- ✅ Chapter identified and loaded
- ✅ Chapter number determined
- ✅ All 5 bible files loaded successfully
- ✅ Previous extraction checked (and handled if exists)
- ✅ Context summary displayed
- ✅ Ready to proceed to extraction

---

## Error Cases

| Error | Handling |
|-------|----------|
| Chapter not found | Ask user for correct path, retry |
| Bible files missing | STOP - require Foundation workflow |
| Chapter empty/corrupted | Error message, cannot proceed |
| Previous extraction exists | Warn user, get confirmation to continue |
| Ambiguous chapter number | Ask user to specify |

---

## Next Step

Proceed to **Step 02: Extract & Validate** with loaded context.
