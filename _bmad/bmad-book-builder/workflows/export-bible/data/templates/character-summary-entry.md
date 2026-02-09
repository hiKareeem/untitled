# Character Summary Entry Template

## Template

For each character in `character_summaries`:

```markdown
### {name}

**Role:** {role}
**Arc Phase:** {arc_phase}
**Description:** {description}
```

## Field Descriptions

- **name**: Character's full name (used as H3 heading)
- **role**: Character's story role (protagonist, antagonist, supporting, etc.)
- **arc_phase**: Current phase of character arc (setup, confrontation, resolution, etc.)
- **description**: Brief character description (first 200 characters from dossier)

## Usage

1. Iterate through `character_summaries` array
2. For each character, create H3 heading with name
3. Format fields as bold labels with values
4. Append to Character Summaries section
5. Display count of profiles formatted in status summary
