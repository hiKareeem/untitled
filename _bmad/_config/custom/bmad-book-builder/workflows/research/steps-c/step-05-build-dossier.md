# Step 5: Build Dossier

**Step:** 5 of 6 (Create Mode)
**Purpose:** Create the formatted research dossier document
**Agent:** Documentaliste

---

## What This Step Does

Using the organized research findings, create a complete, properly formatted research dossier following the dossier template structure.

---

## Instructions for Documentaliste

### 1. Review Organized Research

From Step 4, retrieve the organized research structure with all facts, sources, and metadata.

### 2. Build Dossier Sections

Create each section of the dossier following the template structure.

> See: `data/templates/dossier-structure-template.md` for complete dossier template with all sections and formatting requirements.

The template includes:
- Dossier Header and Metadata
- Overview
- Key Facts (with sub-categories)
- Technical Details
- Common Misconceptions
- Story Applications
- Sources
- Images/References (if applicable)
- Notes for Author

### 3. Generate Dossier Filename

Create a filename that is:
- Descriptive but concise
- Uses kebab-case (lowercase with hyphens)
- Uniquely identifies the topic

> See: `data/templates/dossier-structure-template.md` for filename guidelines.

**Examples:**
- `emergency-medicine-1970s-france.md`
- `surgical-instruments-basic-procedures.md`
- `paris-metro-1970s-routes.md`

### 4. Present Dossier Preview

Show the user a preview of the complete dossier:

```markdown
## Dossier Preview

**Filename:** research/dossiers/[filename].md

**Word count:** [N] words
**Facts:** [N] facts in [N] categories
**Sources:** [N] sources

[Show first 50-100 lines of dossier]

---

**Preview complete. Ready to finalize?**

[Y]es, save dossier
[M]odify content
[R]eview full dossier
```

### 5. Allow Modifications

If user selects [M]odify:
- Ask what needs to be changed (add facts, reorganize, clarify sections)
- Make requested changes
- Re-present preview for confirmation

If user selects [R]eview:
- Show the complete dossier content
- Allow navigation to specific sections
- Return to finalize option after review

### 6. Store Dossier Content

Keep the complete dossier content in conversation context for Step 6:

```yaml
dossier_content: |
  # Research Dossier: [Topic Name]

  ## Dossier Metadata
  ...

dossier_filename: "filename.md"
```

---

## Example Interaction

**Documentaliste:**
"Building research dossier for Emergency Medicine — 1970s France...

---

## Dossier Preview

**Filename:** research/dossiers/emergency-medicine-1970s-france.md

**Word count:** 1,247 words
**Facts:** 11 facts in 3 categories
**Sources:** 5 sources

[Show first 50-100 lines of formatted dossier following template structure]

---

**Preview complete. Ready to finalize?**

[Y]es, save dossier
[M]odify content
[R]eview full dossier"

---

## Success Criteria

✅ **Dossier follows template structure** with all required sections
✅ **All facts included** with proper formatting and source citations
✅ **Metadata complete** (Created, Last Updated, Source Count, Reliability)
✅ **Story applications table** links research to specific story elements
✅ **Sources listed** with reliability ratings
✅ **Notes for author** include warnings and recommendations
✅ **Filename is descriptive** and uses kebab-case format
✅ **User approves dossier** before finalizing

---

## Next Step

Once dossier is built and approved, proceed to **Step 6: Finalize Dossier** where we'll save the file and update the research index.

---

## Notes for Documentaliste

- **Follow the template exactly** — consistency is important for dossiers
- **Use proper markdown formatting** — headers, lists, tables, links
- **Include all metadata fields** — completeness matters
- **Link facts to sources** — every fact must have a source citation
- **Use verification symbols** — ✅ for verified, ⚠️ for needs confirmation
- **Make it author-friendly** — clear, organized, easy to navigate
- **Highlight critical information** — what the author MUST know
- **Keep it concise but complete** — include all relevant information without fluff
- **Get user approval** before saving — this is their research dossier
