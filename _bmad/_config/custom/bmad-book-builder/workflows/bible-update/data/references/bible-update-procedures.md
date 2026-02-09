# Bible Update Procedures

**Purpose:** Reference guide for updating all 5 bible dimension files with extracted chapter information.

**Scope:** Step 04 - Update Bible detailed procedures

---

## Update Strategy Overview

### For Each Dimension File

1. **Use Grep** to find entity sections (`## {Entity Name}`)
2. **Use Edit** to append new information under entity section
3. **If entity doesn't exist**, append new section at end of file
4. **Update frontmatter** (lastUpdated, totalEntries if applicable)

### Formatting Preservation

- ✅ Keep existing markdown structure
- ✅ Maintain section hierarchy
- ✅ Preserve frontmatter fields
- ✅ Don't reformat existing content

### Fallback Procedure

**If Grep fails or Edit encounters issues:**
1. Read full file
2. Reconstruct with new content
3. Write complete file
4. Log fallback usage for debugging

---

## Dimension 1: chronologie.md Updates

### File Location

```
{project-root}/bible/chronologie.md
```

### Update Process

1. **Read frontmatter** to get `lastUpdated`
2. **For each timeline event** in `approved_extraction.chronologie`:
   - Find correct chronological position (not narrative order)
   - Insert event in timeline sequence
   - May not be at end if flashback
3. **Update frontmatter:**
   ```yaml
   lastUpdated: {current timestamp}
   ```

### Append Format

```markdown
### Jour {X} - Chapitre {XX}
- {Event description}
- {Duration: X hours/days}
- {Narrative note: flashback/linear/etc if relevant}
```

### Flashback Handling

**If chapter is flashback** (narrative order ≠ chronological):
- Insert in chronological position (not at end)
- Add note: `(Récit: Chapitre {XX})`

**Example:**
```markdown
### Jour 3 - Chapitre 7
- Battle of Troy begins
- Duration: 6 hours
- (Récit: Chapitre 12 - flashback from Day 10 perspective)
```

### Tool Sequence

```
Grep "### Jour {X}" in chronologie.md → find insertion point
Edit chronologie.md → append/insert event
```

---

## Dimension 2: personnes.md Updates

### File Location

```
{project-root}/bible/personnes.md
```

### Update Process

**For each character** in `approved_extraction.personnes`:

1. **Check if character exists:**
   ```
   Grep "## {Character Name}" in personnes.md
   ```

2. **If character exists:**
   - Find character section
   - Append new entry chronologically under character heading

3. **If character new (first mention):**
   - Append new section at end of file

4. **Update frontmatter:**
   ```yaml
   lastUpdated: {timestamp}
   totalCharacters: {count after additions}
   ```

### New Character Format

```markdown
## {Character Name}

**Première apparition:** Chapitre {XX}

### Chapitre {XX}
{character info}
```

### Entry Format (Existing Character)

```markdown
### Chapitre {XX} - Jour {Y}
- **POV:** {Oui/Non}
- **Actions:** {what character does}
- **État psychologique:** {mental/emotional state}
- **Changements:** {character development}
- **Relations:** {relationship changes if any}
```

### Tool Sequence (Per Character)

```
Grep "## {Character Name}" in personnes.md
├─ If found: Edit to append under section
└─ If not found: Edit to append new section at end
```

---

## Dimension 3: lieux.md Updates

### File Location

```
{project-root}/bible/lieux.md
```

### Update Process

**For each location** in `approved_extraction.lieux`:

1. **Check if location exists:**
   ```
   Grep "## {Location Name}" in lieux.md
   ```

2. **If location exists:**
   - Append usage record

3. **If location new (first mention):**
   - Append new section

4. **Update frontmatter**

### New Location Format

```markdown
## {Location Name}

**Première mention:** Chapitre {XX}

**Description:** {location description}

### Chapitre {XX}
{usage info}
```

### Entry Format (Existing Location)

```markdown
### Chapitre {XX} - Jour {Y}
- **Événements:** {what happens here}
- **Ressources:** {resources used if applicable}
- **Personnages présents:** {who was here}
```

### Tool Sequence

```
Grep "## {Location Name}" in lieux.md
└─ Edit to append
```

---

## Dimension 4: objets.md Updates

### File Location

```
{project-root}/bible/objets.md
```

### Update Process

**For each object** in `approved_extraction.objets`:

1. **Check if object exists:**
   ```
   Grep "## {Object Name}" in objets.md
   ```

2. **If object exists:**
   - Append status update

3. **If object new (first mention):**
   - Append new section

4. **Update frontmatter**

### New Object Format

```markdown
## {Object Name}

**Première mention:** Chapitre {XX}

**Signification:** {plot/symbolic importance}

### Chapitre {XX}
{status info}
```

### Entry Format (Existing Object)

```markdown
### Chapitre {XX} - Jour {Y}
- **Statut:** {créé/détruit/perdu/trouvé/utilisé}
- **Changements:** {status changes from previous}
- **Localisation:** {where/who has it}
```

### Tool Sequence

```
Grep "## {Object Name}" in objets.md
└─ Edit to append
```

---

## Dimension 5: themes.md Updates

### File Location

```
{project-root}/bible/themes.md
```

### Update Process

**For each theme** in `approved_extraction.themes`:

1. **Check if theme exists:**
   ```
   Grep "## {Theme Name}" in themes.md
   ```

2. **If theme exists:**
   - Append progression note

3. **If theme new:**
   - Append new section

4. **Update frontmatter**

### New Theme Format

```markdown
## {Theme Name}

**Émergence:** Chapitre {XX}

### Chapitre {XX}
{theme info}
```

### Entry Format (Existing Theme)

```markdown
### Chapitre {XX}
- **Progression:** {how chapter advances theme}
- **Connections:** {links to characters/plot}
- **Symboles:** {symbolic elements if any}
```

### Tool Sequence

```
Grep "## {Theme Name}" in themes.md
└─ Edit to append
```

---

## Extraction Record Creation

### File Location

```
{project-root}/bible/extractions/chapitre-{XX}.md
```

### Directory Check

```
Use Glob to check: {project-root}/bible/extractions/
If not exists → create directory first (may need Bash mkdir)
```

### Record Template

```markdown
---
chapter: {XX}
extractedAt: {ISO timestamp}
conflicts: {count}
uncertainties: {count}
firstMentions:
  personnes: [{list}]
  lieux: [{list}]
  objets: [{list}}
  themes: [{list}]
---

# Extraction - Chapitre {XX}

{Copy entire approved_extraction content here}

## Informations Extraites

### Chronologie
{chronologie data}

### Personnes présentes
{personnes data}

### Absences significatives
{absences if any}

### Lieux utilisés
{lieux data}

### Objets notables
{objets data}

### Thèmes avancés
{themes data}

## Validation

### Incohérences détectées
{conflicts if any, else "✅ Aucune"}

### Extractions incertaines
{uncertainties if any, else "✅ Toutes claires"}

## Résolutions Appliquées

{If conflicts were resolved:}
{For each conflict:}
- **{Dimension} - {Entity}:** {resolution applied}

{If no conflicts:}
Aucun conflit à résoudre.

---

**Record créé:** {timestamp}
**Extraction approuvée par:** {user or "auto-approved (no conflicts)"}
```

---

## Summary Report Format

### Display After All Updates Complete

```markdown
✅ **Bible Updated Successfully - Chapitre {XX}**

### Fichiers Mis à Jour

**chronologie.md**
- {N} événement(s) ajouté(s)
- Timeline jour {X} → jour {Y}

**personnes.md**
- {N} personnage(s) mis à jour
- 🆕 {N} nouveau(x) personnage(s): {list if any}
- Total personnages: {count}

**lieux.md**
- {N} lieu(x) mis à jour
- 🆕 {N} nouveau(x) lieu(x): {list if any}
- Total lieux: {count}

**objets.md**
- {N} objet(s) mis à jour
- 🆕 {N} nouvel(s) objet(s): {list if any}
- Total objets: {count}

**themes.md**
- {N} thème(s) progressé(s)
- 🆕 {N} nouveau(x) thème(s): {list if any}
- Total thèmes: {count}

### Extraction Record

📄 **Record créé:** `bible/extractions/chapitre-{XX}.md`

{If conflicts resolved:}
### Conflits Résolus ({count})
{List conflicts resolved}

{If uncertainties:}
### ⚠️ Éléments Incertains ({count})
{List uncertainties for user awareness}

---

**Bible maintenant à jour jusqu'au Chapitre {XX}**
```

---

## Tool Usage Summary

| Tool | Purpose | Usage Pattern |
|------|---------|---------------|
| **Grep** | Find entity sections in bible files | Primary search method |
| **Edit** | Append new information to bible files | Primary update method |
| **Read** | Fallback: read full file if Grep/Edit fails | Recovery mechanism |
| **Write** | Create extraction record, fallback for bible updates | Recovery mechanism |
| **Glob** | Check if extractions directory exists | Directory validation |
| **Bash** | Create extractions directory if missing | Directory creation |

---

## Error Handling Matrix

| Error | Detection | Handling |
|-------|-----------|----------|
| Grep fails to find section | Grep returns no results | Use Edit to append new section at end |
| Edit fails | Edit tool error | Fallback: Read full file, reconstruct, Write |
| Write extraction record fails | Write tool error | Alert user, but bible updates still successful |
| Directory bible/extractions missing | Glob returns empty | Create directory with Bash mkdir |
| File permission error | Read/Write tool error | Alert user with clear error message |

---

## Atomicity and Rollback

### Atomicity

**Note:** Bible updates are separate Edit operations (not atomic across all 5 files)

**Implications:**
- If error mid-update → some files updated, some not
- Extraction record logs what was attempted
- User can re-run workflow (will detect previous extraction and warn)

### Rollback

**Not automated** - rely on git

**Recovery:**
- Extraction record provides audit trail
- User can manually revert using git if needed
- Previous extraction check prevents accidental overwrite

---

## Quality Guidelines

### Preserve Structure

- ✅ Don't reformat existing content
- ✅ Keep markdown hierarchy consistent
- ✅ Maintain frontmatter fields
- ✅ Respect existing section organization

### Chronological Ordering

**chronologie.md:**
- Chronological order (not narrative)
- Insert flashbacks in correct timeline position

**Other files:**
- Append chronologically (narrative order OK)
- Chapter-based organization

### First Mentions

**Always mark:**
```markdown
**Première mention:** Chapitre {XX}
**Première apparition:** Chapitre {XX}
**Émergence:** Chapitre {XX}
```

**Purpose:** Makes bible easy to audit and trace

### Extraction Record

**Complete snapshot:**
- Full extraction data
- Conflicts/uncertainties for future reference
- Timestamped for traceability
- Approval source (user or auto)

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

## Final Outputs

### Workflow Outputs

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

### Workflow Completion

After this step, workflow is complete. Bible is updated, extraction recorded, user informed.

**Next Actions for User:**
- Review bible files if desired
- Continue with next chapter (will trigger new bible-update)
- Run Character-Audit or Theme-Tracker to analyze bible data
