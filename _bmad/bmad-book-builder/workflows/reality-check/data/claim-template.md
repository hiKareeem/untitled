# Claim Template

## Claim Structure

Each extracted claim follows this format:

```yaml
claim_id: "{number}"
category: "technical|factual|logical"
subcategory: "{specific type}"
priority: "high|medium|low"
claim_text: "{exact text or paraphrased claim}"
location:
  chapter: "{number}"
  scene: "{number or range}"
  excerpt: "{relevant quote}"
verification_needed: true
dossiers_consulted: []
web_searches: []
status: "pending|verified|issue_found"
confidence: "high|medium|low"
```

## Claim Categories

### Technical Accuracy Claims

**Subcategories:**
- `profession-procedure` — Professional/trade procedures
- `tool-usage` — Tools and equipment usage
- `technical-process` — Technical sequences and operations
- `system-operation` — Systems and their operation

**Example:**
```yaml
claim_id: "001"
category: "technical"
subcategory: "profession-procedure"
priority: "high"
claim_text: "Marc performs emergency tracheotomy with pocket knife"
location:
  chapter: "12"
  scene: "3"
  excerpt: "Marc whipped out his pocket knife and made an incision in the patient's throat..."
verification_needed: true
status: "pending"
```

### Factual Accuracy Claims

**Subcategories:**
- `historical-fact` — Historical dates, events, figures
- `geographic-detail` — Locations, distances, features
- `scientific-fact` — Physics, biology, chemistry
- `temporal-marker` — Time periods, eras, dates

**Example:**
```yaml
claim_id: "002"
category: "factual"
subcategory: "historical-fact"
priority: "high"
claim_text: "Emergency medicine techniques in 1970s France"
location:
  chapter: "5"
  scene: "2"
  excerpt: "The emergency room was equipped with the latest 1970s technology..."
verification_needed: true
status: "pending"
```

### Logical Consistency Claims

**Subcategories:**
- `cause-effect` — Actions leading to results
- `time-sequence` — Timeline realism
- `physical-constraint` — Physical limits respected

**Example:**
```yaml
claim_id: "003"
category: "logical"
subcategory: "physical-constraint"
priority: "medium"
claim_text: "Character jumps 15-meter gap between buildings"
location:
  chapter: "8"
  scene: "1"
  excerpt: "He launched himself across the fifteen-meter gap between rooftops..."
verification_needed: true
status: "pending"
```

## Priority Levels

**High Priority:**
- Professional procedures (medical, legal, technical)
- Tools/equipment usage
- Historical facts
- Scientific principles
- Physical impossibilities

**Medium Priority:**
- Geographic details
- Technical processes
- Timeline sequences
- Cause-and-effect chains

**Low Priority:**
- Background descriptions
- Atmospheric details
- Minor narrative elements
