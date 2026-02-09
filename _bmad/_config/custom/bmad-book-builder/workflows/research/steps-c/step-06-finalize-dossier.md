# Step 6: Finalize Dossier

**Step:** 6 of 6 (Create Mode)
**Purpose:** Save the dossier file and update the research index
**Agent:** Documentaliste

---

## What This Step Does

Save the completed research dossier to the dossiers directory, create or update the research index, and confirm successful completion.

---

## Instructions for Documentaliste

### 1. Verify Dossiers Directory

Ensure the dossiers directory exists:
- Check if `research/dossiers/` directory exists
- If not, create it with proper parent directories

### 2. Save Dossier File

Write the dossier content to the file:
- **Path:** `research/dossiers/{filename}.md`
- **Content:** The complete dossier from Step 5
- **Encoding:** UTF-8

Confirm file was saved successfully:
```markdown
✅ Dossier saved: research/dossiers/{filename}.md
- Word count: [N] words
- File size: [N] KB
- Created: [Date]
```

### 3. Load or Create Research Index

Check if research index exists:
- **If `research/index.md` exists:** Load current index content
- **If not exists:** Create new index with header

### 4. Update Research Index

Add the new dossier to the index.

> See: `data/templates/research-index-template.md` for complete index structure and organization guidelines.

The index includes:
- Dossier Summary (total counts, latest update)
- All Dossiers (organized by category/topic area)
- Dossiers by Story Element (cross-referenced by characters, chapters, locations)
- Index Legend (explaining reliability ratings and terms)

### 5. Organize Dossiers in Index

Group dossiers logically:
- **By topic area** (Medical, Historical, Technical, Location, etc.)
- **By story element** (Characters, Chapters, Locations)
- **Alphabetically** within each group

### 6. Save Updated Index

Write the updated index to `research/index.md`

Confirm index was updated:
```markdown
✅ Research index updated: research/index.md
- Total dossiers: [N]
- Last updated: [Date]
```

### 7. Present Completion Summary

Show the user what was accomplished.

> See: `data/templates/completion-summary-template.md` for complete completion summary structure.

The summary includes:
- Dossier Created (name, location, word count)
- What's Included (facts, sources, applications, misconceptions)
- Story Impact (specific story elements supported)
- Next Steps (how to use the dossier)
- Quick Actions (edit, create, validate, return)

---

## Example Interaction

**Documentaliste:**
"Finalizing research dossier for Emergency Medicine — 1970s France...

---

✅ Verifying directory structure...
✅ Directory research/dossiers/ exists

✅ Saving dossier file...
✅ Dossier saved: research/dossiers/emergency-medicine-1970s-france.md
   - Word count: 1,247 words
   - File size: 8.2 KB
   - Created: 2026-01-25

✅ Loading research index...
✅ Index found: research/index.md
   - Current dossiers: 2

✅ Updating research index...
✅ Index updated: research/index.md
   - Total dossiers: 3
   - Last updated: 2026-01-25

---

[Present completion summary using template structure]

**What would you like to do next?**"

---

## Success Criteria

✅ **Dossier file saved** to `research/dossiers/{filename}.md`
✅ **File content is complete** and properly formatted
✅ **Research index updated** with new dossier entry
✅ **Index is well-organized** and easy to navigate
✅ **Completion summary presented** to user
✅ **Next steps offered** (edit, create, validate, exit)

---

## Workflow Completion

After completing this step:

1. **Ask user what's next:**
   - Edit this dossier (switch to Edit mode)
   - Create another dossier (restart Create mode)
   - Validate this dossier (switch to Validate mode)
   - Exit workflow

2. **If user wants to continue:**
   - Follow the appropriate mode (Edit/Create/Validate)
   - Maintain context of current work

3. **If user exits:**
   - Confirm workflow completion
   - Remind user where to find the dossier
   - Note that dossier can be edited/validated later

---

## Notes for Documentaliste

- **Always verify directory structure** before saving files
- **Use UTF-8 encoding** for markdown files
- **Maintain index consistency** — update all relevant sections
- **Organize index logically** — group by topic and story elements
- **Provide file paths** — user needs to know where to find the dossier
- **Summarize key findings** — reinforce the value of the research
- **Offer next actions** — keep the workflow moving
- **Celebrate completion** — creating a research dossier is significant work
- **Remind about Edit mode** — dossiers can be updated as story evolves
- **Keep index current** — it's the user's roadmap to their research
