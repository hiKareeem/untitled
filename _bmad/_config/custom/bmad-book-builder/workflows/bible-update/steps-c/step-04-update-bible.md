# Step 04: Update Bible

**Goal:** Write approved extraction to bible files and create extraction record for traceability.

**Duration:** 1-2 minutes

---

## What You'll Do

1. Update 5 bible dimension files with extracted information
2. Create extraction record in `bible/extractions/`
3. Preserve existing formatting and structure
4. Generate summary report of changes made

---

## Process

### A. Update Strategy Overview

**For each dimension file:**
1. Use Grep to find entity sections (`## {Entity Name}`)
2. Use Edit to append new information under entity section
3. If entity doesn't exist, append new section at end of file
4. Update frontmatter (lastUpdated, totalEntries if applicable)

**Preserve formatting:**
- Keep existing markdown structure
- Maintain section hierarchy
- Preserve frontmatter fields
- Don't reformat existing content

**Fallback:**
- If Grep fails or Edit encounters issues → Read full file, reconstruct, Write
- Log fallback usage for debugging

**Complete update procedures for all dimensions:**
- See: `data/references/bible-update-procedures.md`

---

### B. Update Each Dimension File

**Complete update procedures for all dimensions:**
- See: `data/references/bible-update-procedures.md`

**Quick reference per dimension:**

| File | Key Process | First Mention Label |
|------|-------------|---------------------|
| **chronologie.md** | Insert events chronologically (handle flashbacks) | N/A |
| **personnes.md** | Append entries per character | "Première apparition" |
| **lieux.md** | Append usage records per location | "Première mention" |
| **objets.md** | Append status updates per object | "Première mention" |
| **themes.md** | Append progression notes per theme | "Émergence" |

**Tool sequence (all dimensions):**
```
Grep "## {Entity Name}" in {dimension}.md
├─ If found: Edit to append under section
└─ If not found: Edit to append new section at end
```

**Update frontmatter** for each file (lastUpdated, counts)

---

### C. Create Extraction Record

**File:** `{project-root}/bible/extractions/chapitre-{XX}.md`

**Check directory exists:**
```
Use Glob to check: {project-root}/bible/extractions/
If not exists → create directory first (may need Bash mkdir)
```

**Write extraction record:**

Use Write tool (new file) - see complete template in `data/references/bible-update-procedures.md`

**Record includes:**
- Frontmatter (chapter, extractedAt, conflicts, uncertainties, firstMentions)
- Full extraction content
- Validation results (incohérences, extractions incertaines)
- Résolutions appliquées
- Timestamp and approval source

---

### D. Generate Summary Report

After all updates complete, display final summary showing:
- Files updated with counts (chronologie.md, personnes.md, lieux.md, objets.md, themes.md)
- New entities added (with 🆕 indicator)
- Extraction record created
- Conflicts resolved (if any)
- Uncertainties flagged (if any)

**Complete summary format:**
- See: `data/references/bible-update-procedures.md`

---

## Outputs

Final workflow outputs:

```yaml
updated_files:
  - bible/chronologie.md
  - bible/personnes.md
  - bible/lieux.md
  - bible/objets.md
  - bible/themes.md
extraction_record: bible/extractions/chapitre-{XX}.md
summary_report: {text above}
chapter_processed: {XX}
new_entities:
  personnes: [{list}]
  lieux: [{list}]
  objets: [{list}]
  themes: [{list}]
conflicts_resolved: {count}
```

---

## Tools Used

- **Grep** - Find entity sections in bible files
- **Edit** - Append new information to bible files (primary method)
- **Read** - Fallback: read full file if Grep/Edit fails
- **Write** - Create extraction record, fallback for bible updates
- **Glob** - Check if extractions directory exists
- **Bash** (if needed) - Create extractions directory if missing

---

## Success Criteria

- ✅ All 5 bible files updated with new information
- ✅ Existing formatting preserved
- ✅ Frontmatter updated (lastUpdated, counts)
- ✅ Extraction record created with full traceability
- ✅ Summary report generated
- ✅ No file corruption
- ✅ New entities properly added with "Première mention/apparition"

---

## Error Handling

| Error | Handling |
|-------|----------|
| Grep fails to find section | Use Edit to append new section at end |
| Edit fails | Fallback: Read full file, reconstruct, Write |
| Write extraction record fails | Alert user, but bible updates still successful |
| Directory bible/extractions missing | Create directory with Bash mkdir |
| File permission error | Alert user with clear error message |

**Atomicity:**
- Bible updates are separate Edit operations (not atomic across all 5 files)
- If error mid-update → some files updated, some not
- Extraction record logs what was attempted
- User can re-run workflow (will detect previous extraction and warn)

**Rollback:**
- Not automated (rely on git)
- Extraction record provides audit trail
- User can manually revert using git if needed

**Detailed error handling and recovery procedures:**
- See: `data/references/bible-update-procedures.md`

---

## Quality Guidelines

**Preserve Structure:**
- Don't reformat existing content
- Keep markdown hierarchy consistent
- Maintain frontmatter fields

**Chronological Ordering:**
- chronologie.md → chronological order (not narrative)
- Other files → append chronologically (narrative order OK)

**First Mentions:**
- Always mark "Première mention/apparition: Chapitre {XX}"
- Makes bible easy to audit

**Extraction Record:**
- Complete snapshot of extraction
- Include conflicts/uncertainties for future reference
- Timestamped for traceability

---

## Workflow Complete

After this step, workflow is complete. Bible is updated, extraction recorded, user informed.

**Next Actions for User:**
- Review bible files if desired
- Continue with next chapter (will trigger new bible-update)
- Run Character-Audit or Theme-Tracker to analyze bible data

**Complete update procedures and reference material:**
- See: `data/references/bible-update-procedures.md`
