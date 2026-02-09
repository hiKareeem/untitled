# Research Organization Framework

## Overview

This document defines the standard categorization system for organizing research findings in the research workflow.

## Standard Categories

### Key Facts
The core factual information, organized by sub-category based on the research topic.

**Sub-category examples:**
- For professions: Daily routines, qualifications, equipment, terminology
- For locations: Geography, climate, culture, landmarks, transportation
- For historical periods: Political climate, social norms, technology, cost of living
- For technical domains: Procedures, specifications, safety requirements, terminology

### Technical Details
Specific technical information that requires precise documentation:
- Procedures (step-by-step processes)
- Specifications (measurements, capacities, tolerances)
- Technical terminology with definitions
- Quantitative data and statistics
- Safety requirements or warnings

### Common Misconceptions
What people commonly get wrong versus reality:
- Misconception description
- Reality (what's actually true)
- Source reference
- Why this matters for the story

### Story Applications
How facts connect to specific story elements:
- Story element (character, location, plot point)
- Chapter/Scene reference
- Application description

### Sources
Organized list of all sources with reliability ratings:
- Source name and URL/reference
- Source type (academic/professional/government)
- Reliability rating (High/Medium/Low)

## Example Category Organization

```yaml
key_facts:
  emergency_room_equipment:
    - "Cardiac monitors and defibrillators were common"
    - "CT scanners introduced 1971 but not widespread"
    - "Mechanical ventilators were available"
  emergency_medical_services:
    - "SAMU established in 1968"
    - "Term 'paramedic' is Anglo-Saxon; French use 'infirmier urgentiste'"
    - "Response times: 10-15 minutes in urban areas"

technical_details:
  procedures:
    - "Cricothyrotomy: Last-resort airway procedure"
    - "Requires medical training or radio guidance"
    - "Risks: severing vital structures, bleeding, airway obstruction"

common_misconceptions:
  - "Misconception: Paramedics in 1970s France"
  - "Reality: SAMU with 'infirmier urgentiste'"
```

## Fact Metadata Requirements

Each fact must include:
- **Source citation** — Which source(s) support this fact
- **Verification status** — ✅ Verified or ⚠️ Needs confirmation
- **Reliability rating** — High/Medium/Low based on source quality
- **Notes** — Additional context, caveats, or warnings

## Critical Facts Identification

Flag facts that are **critical for story accuracy:**
- Facts that impact plot points
- Facts that affect character authenticity
- Facts that influence scene descriptions
- Facts that correct common misconceptions

## Areas of Uncertainty

Note any facts that:
- Have conflicting sources
- Come from low-reliability sources
- Lack sufficient verification
- Are minor details that don't affect the story

These go in "Notes for Author" as areas of uncertainty.
