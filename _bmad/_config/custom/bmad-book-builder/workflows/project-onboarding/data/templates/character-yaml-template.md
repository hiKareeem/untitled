# Character YAML Template

This template defines the standard YAML format for migrated characters in BBB structure.

## Template

```yaml
---
name: "{character_name}"
role: "{role}"
archetype: "{archetype}"

description: |
  {description}

psychology: |
  {psychology_if_present}

contradictions:
  - {contradiction_1}
  - {contradiction_2}

relationships: []
  # To be populated later

notes: |
  Migrated from: {original_file}
  Migration date: {current_date}
---
```

## Field Descriptions

### name
- **Type**: String
- **Required**: Yes
- **Description**: Character's full name
- **Source**: Character file name or content

### role
- **Type**: String
- **Required**: Yes
- **Description**: Character's role in the story
- **Examples**: Protagonist, Antagonist, Mentor, Sidekick, Love Interest

### archetype
- **Type**: String
- **Required**: Yes
- **Description**: Character archetype (if known)
- **Examples**: The Hero, The Shadow, The Wise Old Man, The Trickster

### description
- **Type**: Multiline string (using pipe |)
- **Required**: Yes
- **Description**: Physical description, background, and general character information
- **Source**: Extracted from original character file

### psychology
- **Type**: Multiline string (using pipe |)
- **Required**: No (but recommended)
- **Description**: Character's psychology, motivations, fears, desires, internal conflicts
- **Source**: Extracted from original file or dedicated psychology section
- **Default**: Leave blank or "Not yet defined" if not present

### contradictions
- **Type**: List of strings
- **Required**: No
- **Description**: Character contradictions, flaws, or conflicts
- **Source**: Extracted from original character file
- **Format**: YAML list with dash prefix
- **Default**: Empty list [] if not present

### relationships
- **Type**: List
- **Required**: Yes (but can be empty initially)
- **Description**: Relationships to other characters
- **Default**: Empty list with comment "# To be populated later"
- **Note**: Populated later through build-characters workflow

### notes
- **Type**: Multiline string (using pipe |)
- **Required**: Yes
- **Description**: Migration notes and metadata
- **Content**: Original file path and migration date

## Usage Examples

### Example 1: Complete Character

```yaml
---
name: "Sarah Connor"
role: "Protagonist"
archetype: "The Warrior"

description: |
  A fierce woman who discovers she is the mother of humanity's future savior.
  Strong-willed, resourceful, and increasingly tactical as she faces threats.

psychology: |
  Motivated by protection of her son and the future of humanity.
  Struggles with disbelief transitioning to acceptance and then to action.
  Internal conflict: peaceful life vs. destiny as a warrior.

contradictions:
  - Ordinary waitress vs. destined warrior
  - Desire for peace vs. necessity of violence
  - Trust issues vs. need for allies

relationships: []
  # To be populated later

notes: |
  Migrated from: /project/characters/sarah.md
  Migration date: 2026-01-25
---
```

### Example 2: Minimal Character

```yaml
---
name: "John Doe"
role: "Minor Character"
archetype: "Unknown"

description: |
  A minor character who appears in chapter 3.
  Basic description only.

psychology: |
  Not yet defined

contradictions: []

relationships: []
  # To be populated later

notes: |
  Migrated from: /project/characters/john.md
  Migration date: 2026-01-25
---
```

## Migration Process

1. **Read original character file**
2. **Extract information**:
   - Name (usually file name or first heading)
   - Role/Archetype (if specified)
   - Description (main content)
   - Psychology (if present in separate section)
   - Contradictions (if listed)
3. **Map to YAML structure**
4. **Validate YAML syntax**
5. **Write to** `story-bible/characters/{name}.yaml`
6. **Verify write succeeded**

## Handling Missing Fields

### If psychology is not present:
```yaml
psychology: |
  Not yet defined
```

### If contradictions are not present:
```yaml
contradictions: []
```

### If archetype is not present:
```yaml
archetype: "Unknown"
```

### If role is unclear:
```yaml
role: "Supporting Character"
```

## YAML Formatting Rules

1. **Use pipe (|) for multiline strings** - preserves line breaks
2. **Indent with 2 spaces** - standard YAML indentation
3. **Use dashes (-) for list items** - standard YAML list format
4. **Quotes around strings** - optional but recommended for consistency
5. **Empty lists** - use [] with comment about future population

## File Naming

Character YAML files should be named:
- `{character-name}.yaml`
- Use lowercase with hyphens for spaces
- Examples: `sarah-connor.yaml`, `john-smith.yaml`

## Validation Checklist

After migration, verify:
- [ ] File is valid YAML (can be parsed)
- [ ] All required fields present (name, role, description, notes)
- [ ] Multiline fields use pipe (|) syntax
- [ ] Lists use proper YAML format
- [ ] File name matches character name (normalized)
- [ ] Original content preserved in description/psychology
