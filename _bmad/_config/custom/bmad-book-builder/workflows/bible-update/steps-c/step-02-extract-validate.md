# Step 02: Extract & Validate

**Goal:** Perform multi-dimensional extraction from the chapter and validate continuity with existing bible.

**Duration:** 2-4 minutes (depending on chapter complexity)

---

## What You'll Do

1. Extract information across 5 dimensions (chronology, characters, locations, objects, themes)
2. Check for first mentions of new entities
3. Validate continuity with existing bible
4. Detect conflicts and inconsistencies
5. Flag uncertain extractions
6. Determine if user approval needed

---

## Process

### A. Multi-Dimensional Extraction

Extract information for each dimension using LLM analysis of chapter content against existing bible.

**Detailed extraction protocols for each dimension:**
- See: `data/references/extraction-protocols.md` for complete extraction procedures

**Quick reference:**

| Dimension | Key Extracted Fields |
|-----------|---------------------|
| **Chronologie** | Day, timeline order, duration, key events |
| **Personnes** | Presence, actions, psychological state, POV, changes, relations |
| **Lieux** | Name, description, events, resources |
| **Objets** | Name, status, changes, significance |
| **Thèmes** | Progression, new themes, connections |

**Extraction validation checklist:**
- Timeline aligns with previous chapters
- Character state matches last known state
- Location descriptions consistent
- Object status timeline consistent
- Theme progression aligns with story direction

---

### B. First Mention Detection

For each entity extracted (character, location, object, theme):

1. **Use Grep to search ENTIRE bible** (all 5 dimension files):
   ```
   Grep pattern: "{Entity Name}" in bible/*.md
   ```

2. **If NOT found in any bible file:**
   - Mark as "first mention"
   - Flag for special attention in approval step
   - New entities are significant additions to story world

3. **If found:**
   - Cross-reference existing entry
   - Check for consistency

---

### C. Continuity Validation

Perform cross-dimension checks:

**Cross-dimensional validation matrix:**
- See: `data/references/extraction-protocols.md` for complete validation matrix

**Key checks:**
- Chronologie ↔ Personnes: Characters in right place at right time?
- Personnes ↔ Lieux: Character movements plausible?
- Personnes ↔ Thèmes: Actions align with arcs?
- Objets ↔ Chronologie: Object timeline consistent?

---

### D. Conflict Detection

A **conflict** is when new extraction contradicts existing bible.

**Examples:**
- Character location contradiction (Paris vs London on same day)
- Timeline error (object destroyed but used later)
- Character personality shift without explanation
- Event contradicts chronologie.md sequence

**For each conflict detected:**
```yaml
conflict:
  dimension: "personnes"
  entity: "Jean"
  issue: "Chapter shows Jean in Paris on Day 5, bible shows him in London on Day 5"
  chapter_says: "Jean in Paris, Day 5"
  bible_says: "Jean in London, Day 5 (from chapitre-03)"
  proposed_resolution: "Update bible - Jean in Paris (this chapter more recent)"
```

**Detailed conflict examples and resolution strategies:**
- See: `data/references/extraction-protocols.md`

---

### E. Uncertain Extractions

Mark extraction as **uncertain** if:
- Information is ambiguous in chapter
- Multiple interpretations possible
- Cannot confidently determine timeline/location/state
- POV unreliable narrator (subjective information)

**For each uncertain item:**
```yaml
uncertain_item:
  dimension: "chronologie"
  entity: "Battle timeline"
  reason: "Chapter uses vague time reference 'days later' - unclear exact day number"
  extracted_value: "~Day 7-9"
```

---

### F. Build Extraction Data Structure

Compile all extracted information into structured format.

**Complete template and formatting guidelines:**
- See: `data/references/extraction-protocols.md`

**Structure includes:** Chronologie, Personnes présentes, Absences significatives, Lieux utilisés, Objets notables, Thèmes avancés, Incohérences détectées, Extractions incertaines

---

### G. Determine Decision Needed

Calculate if user approval required:

```
decision_needed = (conflicts.length > 0) OR (uncertain_items.length > 0)
```

**If `decision_needed === true`:**
- User checkpoint required in Step 03

**If `decision_needed === false`:**
- Auto-proceed in Step 03 (just show summary)

---

## Outputs (passed to Step 03)

```yaml
extraction_data: {structured markdown above}
conflicts: [{array of conflict objects}]
uncertain_items: [{array of uncertain item objects}]
first_mentions: [{array of new entities with dimension}]
decision_needed: {boolean}
chapter_number: {XX}
```

---

## Tools Used

- **Grep** - Search entire bible for entity mentions (first mention detection)
- **LLM Analysis** - Extract information, detect conflicts, validate continuity
- No file writes (extraction only)

---

## Success Criteria

- ✅ All 5 dimensions extracted
- ✅ First mentions identified
- ✅ Continuity checks performed
- ✅ Conflicts detected and documented (if any)
- ✅ Uncertain items flagged (if any)
- ✅ Decision flag set correctly
- ✅ Extraction data structured and ready for review

---

## Quality Guidelines

**Good Extraction:**
- Specific, not vague ("Day 5" not "a few days later")
- Captures psychological depth for POV characters
- Notes absence of expected characters
- Distinguishes narrative from chronological order

**Avoid:**
- Hallucinating information not in chapter
- Over-interpreting ambiguous passages (flag as uncertain instead)
- Missing major plot events
- Ignoring continuity errors

**Detailed guidelines:** `data/references/extraction-protocols.md`

---

## Next Step

Proceed to **Step 03: Approve Changes** with extraction data and decision flag.
