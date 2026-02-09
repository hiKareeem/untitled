# Bible Dimension Formatting Specifications

## Overview

This document defines the standard formatting specifications for each of the 5 Living Bible dimensions when compiling the complete story bible export.

## Chronologie Section Format

### Section Header Template

```markdown

---

# Chronologie (Timeline)

> **Last Updated:** {lastUpdated}
> **Chapters Tracked:** {lastChapter}

---

```

### Content Processing Rules

- **IF chronologie exists:** Append full content from `bible_chronologie.content`
- **IF chronologie missing:** Append placeholder:

```markdown
*No chronologie data available. The chronologie dimension tracks sequential events, cause-and-effect relationships, and time passage across chapters.*
```

### Metadata Fields

- `lastUpdated`: Date chronologie was last modified
- `lastChapter`: Highest chapter number tracked in chronologie

## Lieux Section Format

### Section Header Template

```markdown

---

# Lieux (Locations)

> **Last Updated:** {lastUpdated}
> **Locations Tracked:** {totalLocations}

---

```

### Content Processing Rules

- **IF lieux exists:** Append full content from `bible_lieux.content`
- **IF lieux missing:** Append placeholder:

```markdown
*No lieux data available. The lieux dimension tracks all story locations, geographic relationships, and location evolution across chapters.*
```

### Metadata Fields

- `lastUpdated`: Date lieux was last modified
- `totalLocations`: Count of unique locations tracked

## Objets Section Format

### Section Header Template

```markdown

---

# Objets (Objects)

> **Last Updated:** {lastUpdated}
> **Objects Tracked:** {totalObjects}

---

```

### Content Processing Rules

- **IF objets exists:** Append full content from `bible_objets.content`
- **IF objets missing:** Append placeholder:

```markdown
*No objets data available. The objets dimension tracks story items (weapons, tools, artifacts), their locations, ownership history, and plot significance.*
```

### Metadata Fields

- `lastUpdated`: Date objets was last modified
- `totalObjects`: Count of unique objects tracked

## Personnes Section Format

### Section Header Template

```markdown

---

# Personnes (Characters)

> **Last Updated:** {lastUpdated}
> **Characters Tracked:** {totalCharacters}

---

```

### Content Processing Rules

- **IF personnes exists:** Append full content from `bible_personnes.content`
- **IF personnes missing:** Append placeholder:

```markdown
*No personnes data available. The personnes dimension tracks character psychological states, relationships, arc progression, and appearance history.*
```

### Metadata Fields

- `lastUpdated`: Date personnes was last modified
- `totalCharacters`: Count of unique characters tracked

## Themes Section Format

### Section Header Template

```markdown

---

# Themes (Thematic)

> **Last Updated:** {lastUpdated}
> **Themes Tracked:** {totalThemes}

---

```

### Content Processing Rules

- **IF themes exists:** Append full content from `bible_themes.content`
- **IF themes missing:** Append placeholder:

```markdown
*No themes data available. The themes dimension tracks central themes, their evolution, symbolic elements, and thematic connections across chapters.*
```

### Metadata Fields

- `lastUpdated`: Date themes was last modified
- `totalThemes`: Count of unique themes tracked

## Character Summaries Section Format

### Section Header Template

```markdown

---

# Character Summaries

> **Source:** Character Dossiers
> **Profiles Included:** {count}

---

```

### Content Processing Rules

- **IF character_summaries exist and not empty:**
  - For each character in `character_summaries`:
    - Create H3 heading with character name: `### {name}`
    - Format as:
      ```markdown
      **Role:** {role}
      **Arc Phase:** {arc_phase}
      **Description:** {description}
      ```
- **IF character_summaries empty or missing:**
  - Append placeholder:
    ```markdown
    *No character summaries available. Individual character dossiers may exist in the characters folder.*
    ```

### Metadata Fields

- `count`: Number of character profile summaries included

## Formatting Standards

### Heading Hierarchy

- **H1 (#)**: Main dimension sections (Chronologie, Lieux, Objets, Personnes, Themes, Character Summaries)
- **H2 (##)**: Subsections within dimensions (from source content)
- **H3 (###)**: Detailed entries (character names, locations, objects, themes)

### Visual Structure

- Use section dividers (`---`) between main dimensions
- Preserve all content from source files (no data loss)
- Apply consistent formatting (bold, lists, tables as appropriate)
- Maintain markdown structure from source files

### Processing Order

Dimensions are formatted in standard order:

1. Chronologie (Timeline)
2. Lieux (Locations)
3. Objets (Objects)
4. Personnes (Characters)
5. Themes (Thematic)
6. Character Summaries (Optional)

## Placeholders

All dimension sections include descriptive placeholders when data is missing. Placeholders explain:

- What the dimension tracks
- How it connects to story development
- Why it may be missing (normal for early story stages)

This ensures complete bible structure even with incomplete data.
