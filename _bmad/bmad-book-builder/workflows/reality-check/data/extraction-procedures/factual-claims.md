# Factual Accuracy Claims Extraction Procedure

## Scan for:
- **Historical facts:** Dates, events, historical figures, time periods
- **Geographic details:** Locations, distances, geographic features, place names
- **Scientific facts:** Physics, biology, chemistry, scientific principles
- **Temporal markers:** Years, decades, eras, specific dates

## For each claim identified:

```yaml
claim_id: "{incremental number starting F001}"
category: "factual"
subcategory: "{historical-fact|geographic-detail|scientific-fact|temporal-marker}"
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
- **HIGH:** Historical facts, scientific facts, specific dates/time periods
- **MEDIUM:** Geographic details, locations
- **LOW:** Minor geographic mentions, background temporal references

## Example extractions:
```yaml
claim_id: "F001"
category: "factual"
subcategory: "historical-fact"
priority: "high"
claim_text: "Emergency medicine techniques in 1970s France"
location:
  chapter: "5"
  scene: "2"
  excerpt: "The emergency room was equipped with the latest 1970s technology..."
status: "pending"
```
