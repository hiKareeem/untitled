# Web Verification Procedure

## Categorize Claims by Stakes

### High-Stakes Claims (Auto-Verify):
- Professional procedures (medical, legal, technical operations)
- Technical tools and equipment usage
- Historical facts critical to plot
- Scientific principles affecting story logic
- Physical impossibilities

### Medium-Stakes Claims (Auto-Verify):
- Historical details not critical to plot
- Geographic details
- Scientific facts not affecting logic
- Technical processes

### Low-Stakes Claims (Ask User):
- Background descriptions
- Minor location details
- Atmospheric elements
- Minor technical mentions

## Search Strategy
- Craft search query based on claim text
- Use specific, factual queries
- Example: "emergency tracheotomy procedure 1970s", "can engineer perform surgery", "Eiffel Tower visibility Montmartre"

## Execute Web Search
```
Search: "{query}"
```

## Analyze Results
- Evaluate source credibility (official sites, academic sources, reputable publications)
- Extract relevant facts
- Determine claim accuracy (verified, contradicted, partially accurate, uncertain)

## Record Verification Result
```yaml
claim_id: "{existing claim}"
web_searches:
  - query: "{search query used}"
    sources:
      - url: "{source URL}"
        title: "{source title}"
        credibility: "{high|medium|low}"
        relevant_fact: "{fact from source}"
    verification_result: "{verified|contradicted|partial|uncertain}"
    confidence: "{high|medium|low}"
    evidence: "{summary of findings}"
status: "verified|contradicted|partial_match|uncertain"
```

## Examples

### Verified
```yaml
claim_id: "F001"
web_searches:
  - query: "emergency medicine 1970s France technology"
    sources:
      - url: "https://www.historyofemergencymedicine.org/timeline/"
        title: "History of Emergency Medicine Timeline"
        credibility: "high"
        relevant_fact: "By the 1970s, emergency departments had cardiac monitors, defibrillators, and basic life support equipment"
    verification_result: "verified"
    confidence: "high"
    evidence: "Multiple sources confirm 1970s hospitals had basic emergency technology including cardiac monitors and defibrillators"
status: "verified"
```

### Contradicted
```yaml
claim_id: "T001"
web_searches:
  - query: "can engineer perform emergency tracheotomy without medical training"
    sources:
      - url: "https://emedicine.medscape.com/article/83522-procedure"
        title: "Cricothyrotomy Procedure - Medscape"
        credibility: "high"
        relevant_fact: "Cricothyrotomy should only be performed by medical professionals or with radio guidance from emergency services due to risk of severing vital structures"
    verification_result: "contradicted"
    confidence: "high"
    evidence: "Medical sources uniformly indicate this procedure requires medical training and anatomical knowledge. Performing without training is extremely dangerous and likely to cause harm."
status: "contradicted"
```

### Partially Accurate
```yaml
claim_id: "F002"
web_searches:
  - query: "CT scanner availability 1970s France hospital"
    sources:
      - url: "https://www.radiologyinfo.org/en/info.cfm?pg=ctscan"
        title: "CT Scan History"
        credibility: "high"
        relevant_fact: "First CT scanner installed in 1971, but not widespread until late 1970s"
    verification_result: "partial"
    confidence: "high"
    evidence: "CT scan technology existed in 1970s but was rare and not standard equipment in most hospitals"
status: "partial_match"
```
