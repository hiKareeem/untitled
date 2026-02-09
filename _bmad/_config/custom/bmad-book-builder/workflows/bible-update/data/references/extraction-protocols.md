# Bible Dimension Extraction Protocols

**Purpose:** Reference guide for performing multi-dimensional extraction from chapter content and validating continuity with existing bible.

**Scope:** All 5 bible dimensions (chronologie, personnes, lieux, objets, thèmes)

---

## Dimension 1: Chronologie (Timeline)

### What to Extract

| Field | Description | Examples |
|-------|-------------|----------|
| **Jour dans l'histoire** | Day number or timeline marker | "Day 3", "2 weeks later", "Trois jours après" |
| **Ordre narratif vs chronologique** | Narrative structure | Linear, flashback (analepse), mixed timeline |
| **Durée du chapitre** | Time span covered | "2 hours", "3 days", "Une semaine" |
| **Événements clés** | Major timeline events | Battles, meetings, discoveries, deaths |

### Validation Checks

- ✅ Timeline aligns with previous chapters
- ✅ Temporal references consistent with `chronologie.md`
- ✅ Flashbacks properly marked
- ✅ No temporal paradoxes

### Continuity Cross-Checks

**Chronologie ↔ Personnes:**
- Are characters in the right place at the right time?
- Do character actions align with timeline?
- Any time travel or timeline confusion?

**Chronologie ↔ Objets:**
- Objects created/used at consistent times?
- Objects in character possession when should be elsewhere?
- Temporal object inconsistencies?

---

## Dimension 2: Personnes (Characters)

### What to Extract Per Character

| Field | Description | Notes |
|-------|-------------|-------|
| **Présence** | Who appears in chapter | List all characters |
| **Actions** | What they do | Major actions and dialogue |
| **État psychologique** | Mental/emotional state | Especially important for POV characters |
| **POV** | Viewpoint status | Is this character a POV for chapter/scenes? |
| **Changements** | Character development | Decisions, transformations, growth |
| **Relations** | Relationship changes | New or changed relationships with other characters |
| **First mention** | New character check | Use Grep to search entire bible |

### Validation Checks

- ✅ Character state aligns with last known state in `personnes.md`
- ✅ Character locations consistent with chronologie and lieux
- ✅ POV shifts make sense narratively
- ✅ Absences noted (major characters missing)

### Continuity Cross-Checks

**Personnes ↔ Lieux:**
- Do location references match character movements?
- Can character be in location X at time Y given previous position?
- Spatial impossibilities?

**Personnes ↔ Thèmes:**
- Do character actions align with thematic arcs?
- Character behaving out of character for thematic reasons?
- Theme contradictions?

### Absences Significatives

Note when major characters are expected but absent:
- Protagonist missing from chapter
- Supporting character unexplained absence
- Ensemble members missing from group scene

---

## Dimension 3: Lieux (Locations)

### What to Extract Per Location

| Field | Description | Examples |
|-------|-------------|----------|
| **Nom du lieu** | Location name | "Paris", "La cuisine", "Château de Bourbon" |
| **Description** | Physical details | New information only if different from existing |
| **Événements** | What happens here | Plot events, battles, conversations |
| **Ressources** | Resources used/available | Weapons, food, magical items, shelter |
| **First mention** | New location check | Use Grep to search entire bible |

### Validation Checks

- ✅ Location description matches existing `lieux.md`
- ✅ Character movements between locations plausible
- ✅ Spatial consistency maintained (travel time, distances)
- ✅ Geography makes sense

---

## Dimension 4: Objets (Objects)

### What to Extract Per Object

| Field | Description | Examples |
|-------|-------------|----------|
| **Nom de l'objet** | Object name | "Excalibur", "La bague", "Secret documents" |
| **Statut** | Current state | Créé, détruit, perdu, trouvé, utilisé |
| **Changements** | Status changes | How state changed from last known |
| **Signification** | Plot/symbolic importance | Why this object matters to story |
| **First mention** | New object check | Use Grep to search entire bible |

### Validation Checks

- ✅ Object status matches last known state in `objets.md`
- ✅ Object creation/use timeline consistent
- ✅ Object location matches character location
- ✅ No object duplication or contradiction

---

## Dimension 5: Thèmes (Themes)

### What to Extract Per Theme

| Field | Description | Examples |
|-------|-------------|----------|
| **Thèmes avancés** | Existing themes progressing | How theme moves forward in this chapter |
| **Nouveaux thèmes** | Emerging themes | New thematic elements not previously tracked |
| **Connections thématiques** | Links to other elements | How themes connect to character arcs, plot events |

### Validation Checks

- ✅ Theme progression consistent with `themes.md`
- ✅ New themes align with story direction
- ✅ Thematic connections make sense

---

## First Mention Detection Protocol

### Detection Process

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
   - Update existing record

### First Mention Significance

- **New characters** expand cast and relationships
- **New locations** expand story world geography
- **New objects** introduce plot elements or symbols
- **New themes** add thematic depth or direction

---

## Conflict Detection

### What Is a Conflict?

A **conflict** is when new extraction contradicts existing bible.

### Conflict Examples

| Type | Example |
|------|---------|
| Location contradiction | Character in Paris (chapter) vs London (bible) on same day |
| Timeline error | Object destroyed in chapter but used later in bible |
| Character contradiction | Personality shift without explanation vs established traits |
| Event contradiction | Timeline event contradicts chronologie.md sequence |

### Conflict Documentation Format

```yaml
conflict:
  dimension: "personnes"
  entity: "Jean"
  issue: "Chapter shows Jean in Paris on Day 5, bible shows him in London on Day 5"
  chapter_says: "Jean in Paris, Day 5"
  bible_says: "Jean in London, Day 5 (from chapitre-03)"
  proposed_resolution: "Update bible - Jean in Paris (this chapter more recent)"
```

### Conflict Resolution Strategy

**Default principle:** Trust new chapter over old bible (chapter is source of truth)

**Exceptions:**
- If chapter is flashback → maintain chronological order
- If chapter is unreliable narrator → flag as uncertain
- If bible entry is more recent → investigate timeline

---

## Uncertain Extractions

### When to Flag as Uncertain

Mark extraction as **uncertain** if:
- Information is ambiguous in chapter
- Multiple interpretations possible
- Cannot confidently determine timeline/location/state
- POV unreliable narrator (subjective information)
- Chapter uses vague references ("days later", "somewhere north")

### Uncertain Item Documentation

```yaml
uncertain_item:
  dimension: "chronologie"
  entity: "Battle timeline"
  reason: "Chapter uses vague time reference 'days later' - unclear exact day number"
  extracted_value: "~Day 7-9"
```

### Handling Uncertainties

- Flag for user review in approval step
- Don't auto-resolve (user decision required)
- Provide context and suggested alternatives if possible

---

## Cross-Dimensional Validation Matrix

| Check | Dimensions | What to Validate |
|-------|------------|------------------|
| Time-Character | Chronologie ↔ Personnes | Characters in right place at right time |
| Character-Location | Personnes ↔ Lieux | Character movements plausible |
| Character-Theme | Personnes ↔ Thèmes | Actions align with arcs |
| Object-Time | Objets ↔ Chronologie | Object timeline consistency |

---

## Extraction Data Structure Template

```markdown
## Chapitre {XX} - Extraction

### Chronologie
- Jour: {day number or marker}
- Ordre: {linear / flashback / mixed}
- Durée: {time span}
- Événements:
  - {event 1}
  - {event 2}

### Personnes présentes
- **{Character 1}** {[FIRST MENTION] if new}
  - POV: {yes/no}
  - Actions: {what they do}
  - État psychologique: {mental state}
  - Changements: {character development}
  - Relations: {relationship changes}

- **{Character 2}** ...

### Absences significatives
- {Character}: {why notable}

### Lieux utilisés
- **{Location 1}** {[FIRST MENTION] if new}
  - Description: {details}
  - Événements: {what happens here}
  - Ressources: {resources used}

### Objets notables
- **{Object 1}** {[FIRST MENTION] if new}
  - Statut: {current state}
  - Changements: {status changes}
  - Signification: {importance}

### Thèmes avancés
- **{Theme 1}** {[FIRST MENTION] if new}
  - Progression: {how chapter advances theme}
  - Connections: {links to plot/characters}

### Incohérences détectées
{If conflicts found:}
- ⚠️ {Conflict description with dimension + proposed resolution}

{If none:}
- ✅ Aucune incohérence détectée

### Extractions incertaines
{If uncertain items:}
- ❓ {Uncertain item description + reason}

{If none:}
- ✅ Toutes les extractions sont claires
```

---

## Decision Logic

```
decision_needed = (conflicts.length > 0) OR (uncertain_items.length > 0)

If decision_needed === true:
    User checkpoint required in Step 03

If decision_needed === false:
    Auto-proceed in Step 03 (just show summary)
```

---

## Quality Guidelines

### Good Extraction Practices

- ✅ **Specific, not vague** - "Day 5" not "a few days later" (unless chapter is vague)
- ✅ **Psychological depth** - Capture mental states for POV characters
- ✅ **Note absences** - Flag missing expected characters
- ✅ **Distinguish orders** - Separate narrative from chronological order
- ✅ **Symbolic awareness** - Identify symbolic significance of objects
- ✅ **Thematic connections** - Link themes to character actions

### Common Pitfalls

- ❌ Hallucinating information not in chapter
- ❌ Over-interpreting ambiguous passages (flag as uncertain instead)
- ❌ Missing major plot events
- ❌ Ignoring continuity errors (must flag conflicts)
- ❌ Assuming without verifying (use Grep for first mentions)

---

## Tool Usage

| Tool | Purpose | When to Use |
|------|---------|-------------|
| **Grep** | Search bible for entity mentions | First mention detection, conflict validation |
| **LLM Analysis** | Extract information, detect conflicts | Primary extraction and validation |
| **Read** | Load chapter and bible files | Context loading |

**Note:** No file writes in extraction phase (read-only analysis)
