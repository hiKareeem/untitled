# Plot Hole Detection Analysis Procedure

## Analysis Scope
- Contradictions in narrative logic
- Loose ends and unresolved threads
- Unexplained character knowledge or abilities
- Inconsistent cause-and-effect
- Setup without payoff (and vice versa)

## Analysis Process
1. Review chapter plans for intended plot points
2. Extract all plot developments from target chapters
3. Check for logical contradictions
4. Identify unresolved threads
5. Validate character knowledge sources
6. Identify inconsistencies and categorize by severity

## Severity Classification

### Critical
Plot contradiction that breaks story logic

### Major
Significant loose end or unresolved thread

### Minor
Minor plot inconsistency

## Output Format
For each issue found:
```yaml
plot_hole_issues:
  - plot_reference: "Description of plot element"
    issue_description: "Clear description of inconsistency"
    location_reference: "Chapter X, Scene Y"
    severity: "Critical|Major|Minor"
    suggested_fix: "Specific actionable correction"
```

## Progress Update
"✅ **Category 5 Complete:** Plot Hole Detection — {count} issues found"
