# Character Consistency Analysis Procedure

## Analysis Scope
- Personality remains consistent throughout
- Voice and dialogue patterns match established character
- Motivations align with established traits
- Physical descriptions are consistent
- Emotional reactions fit character psychology

## Analysis Process
1. Load all character entries from `bible_characters`
2. Compare each character across target chapters
3. Check character dossiers if available for deeper validation
4. Cross-reference with previous summaries for established behavior
5. Identify inconsistencies and categorize by severity

## Severity Classification

### Critical
Character completely breaks established personality (e.g., pacifist suddenly violent without explanation)

### Major
Minor personality drift or inconsistent dialogue pattern

### Minor
Minor physical description inconsistency

## Output Format
For each issue found:
```yaml
character_issues:
  - character_name: "Name"
    issue_description: "Clear description of inconsistency"
    location_reference: "Chapter X, Scene Y"
    severity: "Critical|Major|Minor"
    suggested_fix: "Specific actionable correction"
```

## Progress Update
"✅ **Category 1 Complete:** Character Consistency — {count} issues found"
