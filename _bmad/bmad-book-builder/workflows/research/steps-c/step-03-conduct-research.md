# Step 3: Conduct Research

**Step:** 3 of 6 (Create Mode)
**Purpose:** Web browsing and fact gathering
**Agent:** Documentaliste

---

## What This Step Does

Use web browsing to research the identified queries, gather facts from multiple sources, verify information across sources, and collect source references.

---

## Instructions for Documentaliste

### 1. Review Research Plan

From Step 2, retrieve the research questions and search queries.

### 2. Conduct Web Research

For each aspect in the research plan:

**a) Execute search queries**
- Use web browsing to search for each query
- Open and review multiple sources (aim for 3-5 sources per aspect)
- Prioritize authoritative sources (academic, professional, government)

**b) Gather facts**
- Extract relevant facts that answer the research questions
- Note specific details (dates, names, procedures, terminology)
- Capture quantitative data when available (measurements, timeframes, statistics)
- Document any contradictions between sources

**c) Verify information**
- Cross-check facts across multiple sources
- Note which facts are consistently reported vs. contradicted
- Assess source reliability (academic sources > professional sources > general web)
- Flag information that needs more verification

**d) Collect source references**
- Record URL for each source
- Note source type (academic, professional, government, etc.)
- Capture publication date or last updated date
- Note author/organization if available

### 3. Track Research Progress

After researching each aspect, report progress:

```
✅ Researched: [Aspect name]
- Found [N] facts from [N] sources
- Sources: [list of source types]
- Key findings: [brief summary]
- ⚠️ Contradictions noted: [if any]
```

### 4. Handle Contradictions

When sources contradict each other:
- Document both versions with their respective sources
- Apply reliability priority (academic > professional > general)
- Mark contradictory facts as ⚠️ Needs confirmation
- Note the contradiction for the author to decide

### 5. Determine When Sufficient

After 3-5 sources per aspect, check with user:
- "I've gathered [N] facts about [Aspect] from [N] sources. Should I:
  - [C]ontinue researching this aspect (more sources)
  - [M]ove to next aspect
  - [S]top research (we have enough)"

This prevents over-researching and keeps focus on story needs.

### 6. Collect Images/References (Optional)

If visual references would be helpful:
- Look for diagrams, illustrations, or images
- Capture image URLs
- Note what the image shows
- Add to "Images/References" section later

### 7. Output Research Findings

Organize findings by aspect:

```yaml
research_findings:
  aspect_1:
    facts:
      - fact: "Fact description"
        sources:
          - url: "https://source-url"
            type: "academic/professional/government"
            reliability: "high/medium/low"
            date: "publication date"
        verification: "verified / needs_confirmation / contradicted"
        notes: "additional context"
    contradictions:
      - issue: "What sources disagree on"
        version_a: "Source A says X"
        version_b: "Source B says Y"
        recommended: "Which is more reliable"
  aspect_2:
    facts:
      # ... same structure
```

### 8. Present Summary to User

After completing research, present:

```markdown
## Research Summary: [Topic Name]

### Facts Gathered
- **[Aspect 1]:** [N] facts from [N] sources
- **[Aspect 2]:** [N] facts from [N] sources
- **[Aspect 3]:** [N] facts from [N] sources

**Total:** [N] facts from [N] sources

### Sources Consulted
- [Source 1] — [Type] — [Reliability]
- [Source 2] — [Type] — [Reliability]
- [Source 3] — [Type] — [Reliability]
...

### Contradictions Found
- [Contradiction 1] — [Recommended resolution]
- [Contradiction 2] — [Recommended resolution]

### Key Findings
[Highlight 3-5 most important facts that will impact the story]

Ready to organize findings into dossier structure? [Y]es / [R]esearch more
```

---

## Example Interaction

**Documentaliste:**
"Beginning web research for Emergency Medicine — 1970s France...

---

✅ Researched: Emergency Room Equipment
- Found 8 facts from 4 sources
- Sources: Medical history journal, Emergency medicine association, Hospital archive, Academic research
- Key findings: Cardiac monitors and defibrillators were common; CT scanners introduced 1971 but not widespread
- No contradictions

✅ Researched: Emergency Procedures
- Found 6 facts from 3 sources
- Sources: Medical procedure reference, Academic research, Medical education site
- Key findings: Emergency tracheotomy is last-resort procedure; requires medical training
- ⚠️ Contradictions noted: One source suggests layperson can perform in extreme emergencies; others strongly advise against

✅ Researched: Emergency Medical Services
- Found 5 facts from 4 sources
- Sources: SAMU official site, French medical history, Government archive, Medical association
- Key findings: SAMU established 1968; term "paramedic" is Anglo-Saxon, not used in France
- No contradictions

✅ Researched: Common Misconceptions
- Found 4 facts from 2 sources
- Sources: Medical history blog, Historical fiction research guide
- Key findings: Advanced imaging often anachronistically portrayed; emergency response times often underestimated
- No contradictions

---

## Research Summary: Emergency Medicine — 1970s France

### Facts Gathered
- **Emergency Room Equipment:** 8 facts from 4 sources
- **Emergency Procedures:** 6 facts from 3 sources
- **Emergency Medical Services:** 5 facts from 4 sources
- **Common Misconceptions:** 4 facts from 2 sources

**Total:** 23 facts from 13 sources

### Sources Consulted
1. History of Emergency Medicine — Professional association — High reliability
2. SAMU France Official History — Government/official — High reliability
3. Medscape: Cricothyrotomy Procedure — Medical reference — High reliability
4. NCBI: Mechanical Ventilation History — Academic research — High reliability
5. RadiologyInfo: CT Scan History — Professional/educational — High reliability
6. ... (and 8 more sources)

### Contradictions Found
1. **Emergency tracheotomy by laypeople**
   - Source A: Can be performed in absolute survival situations
   - Source B: Should NEVER be performed without medical training
   - **Recommended:** Follow Source B — procedure is extremely dangerous without training

### Key Findings
1. Dr. Moreau's profession is accurate for 1970s France — emergency medicine was established
2. Emergency room equipment (cardiac monitors, defibrillators) is historically accurate
3. **Critical:** Use SAMU terminology, NOT "paramedics" — this is a key authenticity detail
4. **Critical:** Chapter 12 tracheotomy scene — procedure accurate BUT character must have medical background
5. CT scanners were just introduced (1971) but not widespread — avoid showing them as common

**Ready to organize findings into dossier structure?** [Y]es / [R]esearch more"

---

## Success Criteria

✅ **All research questions addressed** with factual answers
✅ **Multiple sources consulted** (minimum 3 per aspect, ideally 5+)
✅ **Sources are authoritative** (academic/professional/government preferred)
✅ **Facts are verified** across multiple sources when possible
✅ **Contradictions documented** with recommended resolutions
✅ **Source references collected** (URLs, types, reliability)
✅ **User confirms research is sufficient** before proceeding

---

## Next Step

Once research is complete and confirmed, proceed to **Step 4: Organize Findings** where we'll structure the research into categories and prepare for dossier creation.

---

## Notes for Documentaliste

- **Use web browsing extensively** — this is the core research step
- **Aim for 5-10 quality sources** total (not more) — focus on reliability over quantity
- **After 5 sources per aspect,** suggest "sufficient" checkpoint to user
- **Prioritize facts that directly impact story accuracy**
- **Document sources meticulously** — every fact needs a source
- **Flag contradictions** rather than trying to resolve them — let author decide
- **Assess source reliability** and note it for each source
- **Capture specific details** (dates, names, measurements) — these add authenticity
- **Look for terminology** — correct period-specific terms are crucial for authenticity
- **Don't over-research** — stay focused on story needs
