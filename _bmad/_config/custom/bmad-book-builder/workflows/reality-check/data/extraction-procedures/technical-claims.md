# Technical Accuracy Claims Extraction Procedure

## Scan for:
- **Profession/trade procedures:** Medical, legal, engineering, technical operations
- **Tools/equipment usage:** Specific tools, instruments, machinery
- **Technical processes:** Sequences, operations, systems

## For each claim identified:

```yaml
claim_id: "{incremental number starting T001}"
category: "technical"
subcategory: "{profession-procedure|tool-usage|technical-process|system-operation}"
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
- **HIGH:** Professional procedures (medical, legal, technical), tool usage, technical operations
- **MEDIUM:** Technical processes, system operations
- **LOW:** Background technical details, minor equipment mentions

## Example extractions:
```yaml
claim_id: "T001"
category: "technical"
subcategory: "profession-procedure"
priority: "high"
claim_text: "Engineer performs emergency tracheotomy with pocket knife"
location:
  chapter: "12"
  scene: "3"
  excerpt: "Marc whipped out his pocket knife and made an incision in the patient's throat..."
status: "pending"
```
