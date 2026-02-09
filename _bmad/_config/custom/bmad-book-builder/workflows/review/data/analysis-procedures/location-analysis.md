# Location Accuracy Analysis Procedure

## Analysis Scope
- Descriptions match across mentions
- Distances and geography are plausible
- Setting details remain consistent
- Transitions between locations are logical

## Analysis Process
1. Load all location entries from `bible_locations`
2. Track each location mention across target chapters
3. Validate description consistency
4. Check geographical plausibility
5. Identify inconsistencies and categorize by severity

## Severity Classification

### Critical
Location changes fundamental properties without explanation (e.g., small village becomes city)

### Major
Description inconsistent or geography implausible

### Minor
Minor detail inconsistency

## Output Format
For each issue found:
```yaml
location_issues:
  - location_name: "Name"
    issue_description: "Clear description of inconsistency"
    location_reference: "Chapter X, Scene Y"
    severity: "Critical|Major|Minor"
    suggested_fix: "Specific actionable correction"
```

## Progress Update
"✅ **Category 2 Complete:** Location Accuracy — {count} issues found"
