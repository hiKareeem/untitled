# Chapter Frontmatter Template

This template defines the standard frontmatter for migrated chapters in BBB structure.

## Template

```yaml
---
chapterNumber: {n}
chapterTitle: "{title_from_content_or_auto}"
createdDate: "{current_date}"
author: "{user_name}"
migrationSource: "{original_path}"
---
```

## Field Descriptions

### chapterNumber
- **Type**: Integer
- **Required**: Yes
- **Description**: Sequential chapter number (1, 2, 3, etc.)
- **Source**: File numbering or sequential assignment

### chapterTitle
- **Type**: String
- **Required**: Yes
- **Description**: Title of the chapter
- **Source**: Extract from first H1 heading in content, or auto-generate "Chapter {n}"

### createdDate
- **Type**: Date (ISO format: YYYY-MM-DD)
- **Required**: Yes
- **Description**: Date the chapter was migrated to BBB
- **Source**: Current date in YYYY-MM-DD format

### author
- **Type**: String
- **Required**: Yes
- **Description**: Author name
- **Source**: User-provided or from config

### migrationSource
- **Type**: String
- **Required**: Yes
- **Description**: Original path to the chapter file before migration
- **Source**: Full path to original chapter file

## Usage Example

Before migration:
```markdown
# The Discovery

John walked into the room and noticed something strange...
```

After migration:
```yaml
---
chapterNumber: 5
chapterTitle: "The Discovery"
createdDate: "2026-01-25"
author: "Jane Smith"
migrationSource: "/Users/jane/writing/project/chapters/chapter-05.md"
---

# The Discovery

John walked into the room and noticed something strange...
```

## Title Extraction Logic

1. **Check for H1 heading** in chapter content
2. **If H1 exists**: Use as chapterTitle
3. **If no H1**: Generate "Chapter {n}" as title
4. **If H1 is "Chapter X"**: Use as-is or extract meaningful title

## File Naming Convention

Migrated chapters should be named:
- `chapter-01.md`
- `chapter-02.md`
- `chapter-03.md`
- etc.

Always use zero-padded two-digit numbers for proper sorting.
