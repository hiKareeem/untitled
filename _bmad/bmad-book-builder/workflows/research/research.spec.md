# Workflow Specification: Research

**Module:** bmad-book-builder
**Status:** Specification — New workflow
**Created:** 2026-01-24
**Priority:** P2 (Specialized Feature — Research Management)

---

## Workflow Overview

**Goal:** Create and manage research dossiers for story topics

**Description:** Documentaliste (Research & Fact Specialist) guides author through creating comprehensive research dossiers on topics relevant to their story — professions, locations, historical periods, technical domains, etc.

**Workflow Type:** Create/Edit/Validate (tri-modal)

---

## Why This Workflow Exists

> **🎯 NEW WORKFLOW — Research documentation management**
>
> Credible novels require research. Organized research dossiers let authors verify facts quickly and maintain coherence.
>
> **This workflow centralizes research** so it can be reused across the entire project.

---

## Workflow Structure

### Entry Point

```yaml
---
name: research
description: Create and manage research dossiers
web_bundle: true
installed_path: '{project-root}/_bmad/bmad-book-builder/workflows/research'
---
```

---

## Planned Steps

### Create Mode
| Step | Name | Goal |
|------|------|------|
| 1 | Identify Topic | Choose research topic (profession, location, era, etc.) |
| 2 | Define Scope | Specify what aspects to research |
| 3 | Web Research | Use web browsing to gather information |
| 4 | Organize Facts | Structure findings into dossier format |
| 5 | Create Dossier | Generate organized research document |
| 6 | Link to Story | Note how research applies to story elements |

### Edit Mode
| Step | Name | Goal |
|------|------|------|
| 1 | Select Dossier | Choose existing dossier to update |
| 2 | Assess Gaps | Identify missing or outdated information |
| 3 | Gather New Info | Research additional details |
| 4 | Update Dossier | Add new findings to existing dossier |

### Validate Mode
| Step | Name | Goal |
|------|------|------|
| 1 | Select Dossier | Choose dossier to validate |
| 2 | Verify Facts | Check accuracy of key facts |
| 3 | Check Sources | Verify sources are reliable |
| 4 | Generate Report | Produce validation summary |

---

## Research Dossier Structure

```markdown
# Research Dossier: [Topic Name]

## Dossier Metadata
- **Created:** [Date]
- **Last Updated:** [Date]
- **Source Count:** [Number of sources]
- **Story Relevance:** [How this connects to story]

## Overview
[Brief description of topic and why it matters to the story]

## Key Facts

### Fact Category 1
- **Fact 1:** [Description]
  - Source: [URL or reference]
  - Verification: ✅ Verified / ⚠️ Needs confirmation
- **Fact 2:** [Description]
  - Source: [URL or reference]
  - Verification: ✅ Verified / ⚠️ Needs confirmation

### Fact Category 2
[... same format ...]

## Technical Details (if applicable)
[Specific technical information relevant to story]

## Common Misconceptions
- **Misconception 1:** [What people get wrong]
  - **Reality:** [What's actually true]
- **Misconception 2:** [What people get wrong]
  - **Reality:** [What's actually true]

## Story Applications
| Story Element | Chapter/Scene | How Research Applies |
|---------------|---------------|----------------------|
| [Character profession] | Ch. 12, 15 | [Specific usage] |
| [Location detail] | Ch. 8 | [Specific usage] |

## Sources
1. **Source Name** — URL or reference — [Reliability rating]
2. **Source Name** — URL or reference — [Reliability rating]

## Images/References
[Links to images, diagrams, or other visual references]

## Notes for Author
[Any reminders, warnings, or special considerations]
```

---

## Example Research Dossier

```markdown
# Research Dossier: Emergency Medicine — 1970s

## Overview
Medical procedures and knowledge relevant to story set in 1970s hospital. Critical for scenes involving emergency treatment.

## Key Facts

### Diagnostic Tools (1970s)
- **X-ray:** Available, but slower than modern — 30+ minute development
  - Source: Medical history archives
  - Verification: ✅ Verified
- **CT Scan:** Introduced 1972, very rare in hospitals
  - Source: Radiology history journal
  - Verification: ✅ Verified
- **MRI:** Not invented until 1977 — NOT AVAILABLE
  - Source: Medical imaging history
  - Verification: ✅ Verified

### Emergency Procedures (1970s)
- **CPR:** Just becoming standard (introduced 1960s)
  - Source: American Heart Association archives
  - Verification: ✅ Verified
- **Defibrillators:** Bulky, less effective than modern
  - Source: Medical equipment history
  - Verification: ✅ Verified

## Common Misconceptions
- **Misconception:** Doctors could instantly diagnose conditions
  - **Reality:** 1970s diagnosis was slower, less precise
- **Misconception:** All modern drugs existed
  - **Reality:** Many common drugs (Prozac, etc.) not yet invented

## Story Applications
| Story Element | Chapter/Scene | Usage |
|---------------|---------------|-------|
| Dr. Marc's diagnosis | Ch. 12 | Must use 1970s-appropriate methods |
| Emergency scene | Ch. 15 | No CT scan, use X-ray only |

## Sources
1. "History of Emergency Medicine" — Journal of Medical History — High reliability
2. "Medical Technology Timeline" — Medical Museum — High reliability
```

---

## Workflow Inputs

### Required Inputs (Create Mode)
- Research topic
- Scope of research needed

### Required Inputs (Edit Mode)
- Existing dossier to update

### Required Inputs (Validate Mode)
- Dossier to validate

---

## Workflow Outputs

### Output Format

- [X] Document-producing (research dossiers)

### Output Files

- `research/dossiers/{topic-name}.md` — Research dossier document
- `research/index.md` — Index of all research dossiers

---

## Agent Integration

### Primary Agent

**Documentaliste** (Research & Fact Specialist)

The Documentaliste has web browsing capabilities and specializes in research management.

---

## Research Topics by Category

### Professional Domains
- Medical professions
- Legal procedures
- Engineering disciplines
- Military operations
- Academic fields

### Historical Periods
- Time-specific technology
- Period-appropriate language
- Social norms and customs
- Political context

### Geographic Locations
- Climate and weather
- Physical geography
- Cultural specifics
- Local customs

### Technical Domains
- Weapons and combat
- Vehicles and transportation
- Computers and technology
- Tools and equipment

---

## When to Use This Workflow

- **During planning** — Research key topics before writing
- **When writing technical scenes** — Create dossiers for accuracy
- **During revision** — Verify facts with existing dossiers
- **When beta readers flag issues** — Research to address concerns

---

## Implementation Notes

### Web Browsing Strategy:

1. **Start with broad overview** — Get general understanding
2. **Identify reliable sources** — Academic, official, expert sources
3. **Cross-reference facts** — Verify across multiple sources
4. **Document sources** — Keep URLs for later verification

### Dossier Organization:

- Use descriptive filenames (e.g., `emergency-medicine-1970s.md`)
- Create index.md linking all dossiers
- Tag dossiers by category for easy filtering

---

## Integration with Other Workflows

- **Reality-Check** — Uses research dossiers for verification
- **Documentaliste agent** — Direct commands for quick research
- **Foundation** — Can trigger research for worldbuilding
- **Chapter-Write** — Reference research during writing

---

## Example Use Cases

1. **Historical fiction** — Research period details (clothing, speech, events)
2. **Medical drama** — Research procedures, equipment, limitations
3. **Technical thriller** — Research technology, hacking, engineering
4. **Legal drama** — Research legal procedures, courtroom dynamics
5. **Military fiction** — Research tactics, equipment, hierarchy

---

_This is a specification. Use the create-workflow workflow to build this workflow._
