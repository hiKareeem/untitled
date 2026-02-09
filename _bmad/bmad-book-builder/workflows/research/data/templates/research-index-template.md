# Research Index Template

## Template Overview

This template defines the structure for the research index that tracks all research dossiers in a project.

## Index Header

```markdown
# Research Index

> Master index of all research dossiers for this project
> Last Updated: [Date]
```

## Dossier Summary

```markdown
## Dossier Summary

**Total Dossiers:** [N]
**Total Sources:** [N]
**Latest Dossier:** [Topic Name] ([Date])
```

## All Dossiers Section

Organize dossiers by category/topic area:

```markdown
## All Dossiers

### [Category/Topic Area]

1. **[Dossier Name]**
   - **File:** `research/dossiers/{filename}.md`
   - **Created:** [Date]
   - **Last Updated:** [Date]
   - **Source Count:** [N]
   - **Reliability:** [High/Medium/Low]
   - **Story Relevance:** [Brief description]
   - **Key Facts:** [N] facts across [N] categories

2. **[Dossier Name]**
   - **File:** `research/dossiers/{filename}.md`
   - **Created:** [Date]
   - **Last Updated:** [Date]
   - **Source Count:** [N]
   - **Reliability:** [High/Medium/Low]
   - **Story Relevance:** [Brief description]
   - **Key Facts:** [N] facts across [N] categories

### [Another Category]
[... more dossiers in same format]
```

## Dossiers by Story Element Section

Organize dossiers by their relevance to story elements:

```markdown
## Dossiers by Story Element

### Characters
- [Dossier relevant to Character X] — [Brief note]
- [Dossier relevant to Character Y] — [Brief note]

### Chapters
- **Chapter 5:** [Dossier 1], [Dossier 2], [Dossier 3]
- **Chapter 8:** [Dossier 1], [Dossier 4]
- **Chapter 12:** [Dossier 1], [Dossier 5]

### Locations
- [Dossier relevant to Location X] — [Brief note]
- [Dossier relevant to Location Y] — [Brief note]

### Themes/Topics
- [Dossier relevant to Theme X] — [Brief note]
- [Dossier relevant to Topic Y] — [Brief note]
```

## Index Legend

```markdown
## Index Legend

- **Reliability:**
  - High: Academic/professional/government sources
  - Medium: Mixed sources or general references
  - Low: Limited sources or casual references

- **Source Count:** Number of unique sources cited in dossier

- **Key Facts:** Total number of verified facts across all categories
```

## Organization Guidelines

When organizing dossiers in the index:

1. **By Topic Area** — Group related subjects (Medical, Historical, Technical, Location, etc.)
2. **By Story Element** — Cross-reference by characters, chapters, locations
3. **Alphabetically** — Within each group, sort alphabetically
4. **Update Regularly** — Keep index current with each new dossier
5. **Be Consistent** — Use the same format for all dossier entries

## Index Maintenance

- Update when: A new dossier is created or an existing one is significantly updated
- Verify: All file paths are correct and dossiers exist
- Check: Story relevance connections are accurate
- Review: Category groupings still make sense as dossier count grows
