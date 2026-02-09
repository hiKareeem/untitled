# Object Tracking Analysis Procedure

## Analysis Scope
- Items don't appear/disappear without explanation
- Weapons, tools, items are tracked properly
- Timeline of object possession is logical
- Object properties remain consistent

## Analysis Process
1. Load all object entries from `bible_objects`
2. Track each object across target chapters
3. Validate possession timeline
4. Check for unexplained appearances/disappearances
5. Identify inconsistencies and categorize by severity

## Severity Classification

### Critical
Plot-critical object appears/disappears without explanation

### Major
Important object not tracked consistently

### Minor
Minor object inconsistency

## Output Format
For each issue found:
```yaml
object_issues:
  - object_name: "Name"
    issue_description: "Clear description of inconsistency"
    location_reference: "Chapter X, Scene Y"
    severity: "Critical|Major|Minor"
    suggested_fix: "Specific actionable correction"
```

## Progress Update
"✅ **Category 3 Complete:** Object Tracking — {count} issues found"
