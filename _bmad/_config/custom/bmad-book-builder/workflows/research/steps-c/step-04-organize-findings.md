# Step 4: Organize Findings

**Step:** 4 of 6 (Create Mode)
**Purpose:** Structure research into categories and prepare for dossier creation
**Agent:** Documentaliste

---

## What This Step Does

Organize the gathered research facts into logical categories, group related facts together, identify key themes, and prepare the structure for the research dossier.

---

## Instructions for Documentaliste

### 1. Review Research Findings

From Step 3, retrieve all gathered facts with their sources and verification status.

### 2. Organize Facts into Categories

Group facts into logical categories based on the dossier template structure.

> See: `data/references/research-organization-framework.md` for complete category definitions and examples.

**Standard Categories:**
- **Key Facts** — The core factual information, organized by sub-category
- **Technical Details** — Specific technical information (procedures, specifications, measurements)
- **Common Misconceptions** — What people get wrong vs. reality
- **Story Applications** — How facts connect to specific story elements
- **Sources** — Organized list of all sources with reliability ratings

### 3. Identify Fact Categories

Within "Key Facts," create sub-categories that group related information.

> See: `data/references/research-organization-framework.md` for detailed sub-category examples by topic type.

### 4. Add Metadata for Each Fact

For each fact, ensure you have:
- **Source citation** — Which source(s) support this fact
- **Verification status** — ✅ Verified or ⚠️ Needs confirmation
- **Reliability rating** — High/Medium/Low based on source quality
- **Notes** — Additional context, caveats, or warnings

### 5. Create Story Applications Table

Review the story connection from Step 1 and create specific applications.

> See: `data/references/story-applications-framework.md` for complete guidance on creating story applications.

**Story Applications Table:**
| Story Element | Chapter/Scene | How Research Applies |
|---------------|---------------|----------------------|
| Dr. Moreau profession | Ch. 5, 8, 12, 15 | Emergency physician role accurate |
| Emergency room equipment | Ch. 5, Scene 2 | Cardiac monitors verified |
| Emergency tracheotomy | Ch. 12, Scene 3 | Procedure accurate; character needs medical background |

### 6. Identify Critical Facts

Flag facts that are **critical for story accuracy:**
- Facts that impact plot points
- Facts that affect character authenticity
- Facts that influence scene descriptions
- Facts that correct common misconceptions

Mark these clearly — they're the most important for the author.

### 7. Identify Areas of Uncertainty

Note any facts that:
- Have conflicting sources
- Come from low-reliability sources
- Lack sufficient verification
- Are minor details that don't affect the story

These go in "Notes for Author" as areas of uncertainty.

### 8. Present Organization to User

Show how the research will be organized in the dossier:

```markdown
## Dossier Structure: [Topic Name]

### Key Facts

**[Category 1]** ([N] facts)
- Fact 1
- Fact 2
- Fact 3

**[Category 2]** ([N] facts)
- Fact 1
- Fact 2
- Fact 3

### Technical Details
[If applicable] - [N] technical points

### Common Misconceptions
[N] misconceptions documented

### Story Applications
[N] story connections identified

### Sources
[N] sources (High: [N], Medium: [N], Low: [N])

### Critical Facts for Story Accuracy
1. [Critical fact 1] — [Why it matters]
2. [Critical fact 2] — [Why it matters]
3. [Critical fact 3] — [Why it matters]

### Areas of Uncertainty
- [Uncertainty 1]
- [Uncertainty 2]

Does this organization work? [Y]es / [M]odify
```

### 9. Allow User Modification

If user selects [M]odify:
- Ask which categories need adjustment
- Add or remove categories as needed
- Re-fact facts into different groupings
- Re-present organization for confirmation

### 10. Output Organized Structure

Store in conversation context using the defined YAML format.

> See: `data/references/organized-research-output-format.md` for complete YAML structure specification.

---

## Example Interaction

**Documentaliste:**
"Organizing research findings for Emergency Medicine — 1970s France...

---

## Dossier Structure: Emergency Medicine — 1970s France

### Key Facts

**Emergency Room Equipment** (3 facts)
- Cardiac monitors and defibrillators were common in 1970s French hospitals
- CT scanners introduced in 1971 but not widespread until late 1970s
- Basic ventilators and mechanical ventilation were available

**Emergency Medical Services** (3 facts)
- SAMU (Service d'Aide Médicale Urgente) established in 1968
- Term "paramedic" is Anglo-Saxon; French use "infirmier urgentiste"
- Response times: 10-15 minutes in urban Paris

**Hospital Operations** (2 facts)
- Emergency medicine was recognized specialty in 1970s France
- Hospital hierarchy included emergency physicians, surgeons, specialists

### Technical Details

**Emergency Procedures** (3 points)
- Cricothyrotomy: Last-resort airway obstruction procedure
- Requires medical training or radio guidance from emergency services
- Risks: severing vital structures, bleeding, airway obstruction

**Response Specifications** (1 point)
- SAMU response: 10-15 minutes (urban areas); Hospital arrival: 20-30 minutes

### Common Misconceptions
2 misconceptions documented
- "Paramedics" in 1970s France (reality: SAMU with infirmier urgentiste)
- Advanced imaging readily available (reality: CT just introduced, not widespread)

### Story Applications
4 story connections identified
- Dr. Moreau profession → Ch. 5, 8, 12, 15
- Emergency room equipment → Ch. 5, Scene 2
- Emergency tracheotomy → Ch. 12, Scene 3
- Emergency response → Ch. 8, Scene 1

### Sources
5 sources (High: 5, Medium: 0, Low: 0)
- History of Emergency Medicine (Professional association)
- SAMU France Official (Government/official)
- Medscape: Cricothyrotomy (Medical reference)
- NCBI: Mechanical Ventilation (Academic)
- RadiologyInfo: CT Scan History (Professional)

### Critical Facts for Story Accuracy
1. **Use SAMU terminology, not "paramedics"** — Critical for authenticity in Ch. 8
2. **Chapter 12 tracheotomy requires medical background** — Character authenticity issue
3. **CT scanners not widespread** — Avoid anachronism in equipment descriptions

### Areas of Uncertainty
- Specific equipment models in 1970s French hospitals (minor detail)
- Exact response times for SAMU (10-15 minutes acceptable for story)

**Does this organization work?** [Y]es / [M]odify"

---

## Success Criteria

✅ **Facts organized into logical categories** that match dossier template
✅ **Key facts grouped by sub-category** for easy navigation
✅ **Each fact has source citation** and verification status
✅ **Story applications identified** for relevant story elements
✅ **Critical facts flagged** that impact story accuracy
✅ **Areas of uncertainty noted** for author awareness
✅ **User confirms organization** before proceeding

---

## Next Step

Once organization is confirmed, proceed to **Step 5: Build Dossier** where we'll create the formatted research dossier document.

---

## Notes for Documentaliste

- **Organize for usability** — author should be able to quickly find facts
- **Group related facts** — similar information should be together
- **Use descriptive category names** — clear and intuitive
- **Flag critical facts** — these are the most important for story accuracy
- **Note uncertainties** — transparency builds trust
- **Connect to story elements** — show how research applies to the story
- **Keep author's needs in mind** — what will they reference while writing?
- **Maintain source linkage** — every fact must trace back to its source
