# Reference Checking Procedure

## Full Matching Procedure

**For each claim from Step 2:**

### Step 1: Extract Keywords
- Extract keywords from claim text
- Example: "emergency tracheotomy" → keywords: ["emergency", "tracheotomy", "medical", "surgery", "procedure"]

### Step 2: Search Dossiers
Search dossier titles and content for keyword matches

**Match Criteria:**
- **Direct match:** Dossier title directly addresses claim topic
- **Keyword match:** Dossier contains relevant keywords
- **Category match:** Dossier covers claim category (e.g., medical, historical, technical)

### Step 3: Process Matching Dossiers
For each matching dossier:
- Read dossier content
- Extract relevant facts
- Match claim to specific facts in dossier

### Step 4: Update Claim Status
```yaml
claim_id: "{existing claim}"
dossiers_consulted: ["{dossier-name-1}", "{dossier-name-2}"]
dossier_matches:
  - dossier: "{dossier-name}"
    fact_id: "{fact identifier from dossier}"
    relevance: "direct|partial|related"
    verification_result: "{verified|contradicted|partial_match|not_found}"
status: "verified_via_dossier|needs_web_verification|contradicted_by_dossier"
confidence: "{high|medium|low}"
```

## Verification Result Categories

- **verified_via_dossier:** Claim matches dossier fact(s) exactly or closely
- **needs_web_verification:** Claim not addressed in any dossier
- **contradicted_by_dossier:** Claim contradicts dossier fact(s) → FLAG AS ISSUE
- **partial_match:** Claim partially addressed but needs clarification
