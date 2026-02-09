# Logical Consistency Claims Extraction Procedure

## Scan for:
- **Cause-effect relationships:** Actions leading to results
- **Time sequences:** Timelines, travel times, sequence of events
- **Physical constraints:** Physical capabilities, limitations, realistic actions

## For each claim identified:

```yaml
claim_id: "{incremental number starting L001}"
category: "logical"
subcategory: "{cause-effect|time-sequence|physical-constraint}"
priority: "high|medium|low"
claim_text: "{paraphrased or quoted claim}"
location:
  chapter: "{number}"
  scene: "{number}"
  excerpt: "{relevant quote}"
verification_needed: true
dossiers_consulted: []
web_searches: []
status: "pending"
confidence: "unverified"
```

## Priority assignment:
- **HIGH:** Physical impossibilities, major timeline inconsistencies
- **MEDIUM:** Time sequence issues, cause-effect problems
- **LOW:** Minor logical quirks, minor timeline compressions

## Example extractions:
```yaml
claim_id: "L001"
category: "logical"
subcategory: "physical-constraint"
priority: "medium"
claim_text: "Character jumps 15-meter gap between buildings"
location:
  chapter: "8"
  scene: "1"
  excerpt: "He launched himself across the fifteen-meter gap between rooftops..."
status: "pending"
```
