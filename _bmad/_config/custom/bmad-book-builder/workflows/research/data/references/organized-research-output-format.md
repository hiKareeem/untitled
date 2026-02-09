# Organized Research Output Format

## Overview

This document defines the YAML structure for storing organized research findings in the research workflow.

## Output Structure

The organized research is stored in conversation context using this YAML format:

```yaml
organized_research:
  key_facts:
    category_1:
      - fact: "Fact description"
        source: "Source URL or reference"
        verification: "verified"
        reliability: "high"
        notes: "Additional context, caveats, or warnings"
      - fact: "Another fact description"
        source: "Source URL or reference"
        verification: "verified"
        reliability: "medium"
        notes: "Additional context"
    category_2:
      - fact: "Fact in second category"
        source: "Source URL or reference"
        verification: "needs-confirmation"
        reliability: "low"
        notes: "Caveats about this fact"

  technical_details:
    procedures:
      - "Procedure description with key points"
      - "Another procedure"
    specifications:
      - "Specification 1: value and units"
      - "Specification 2: value and units"
    terminology:
      - term: "Technical term"
        definition: "Clear definition"

  common_misconceptions:
    - misconception: "Common misunderstanding"
      reality: "What's actually true"
      source: "Source reference"

  story_applications:
    - element: "Story element name"
      chapter: "Ch. X, Scene Y"
      application: "How research applies to this element"
    - element: "Another story element"
      chapter: "Ch. X, Scene Y"
      application: "How research applies"

  sources:
    - name: "Source Name"
      url: "https://example.com/source"
      type: "academic"
      reliability: "high"
    - name: "Another Source"
      url: "https://example.com/another"
      type: "professional"
      reliability: "medium"

  critical_facts:
    - fact: "Critical fact description"
      importance: "Why this matters for story accuracy"
      chapter: "Ch. X, Scene Y (if applicable)"

  areas_of_uncertainty:
    - "Description of uncertainty or conflicting information"
    - "Another area needing further research"
```

## Field Definitions

### key_facts
Core factual information organized by category:
- **fact**: The factual statement
- **source**: Where this fact comes from (URL or reference)
- **verification**: Either "verified" or "needs-confirmation"
- **reliability**: Either "high", "medium", or "low"
- **notes**: Additional context, caveats, warnings, or explanations

### technical_details
Technical information for specialized topics:
- **procedures**: Step-by-step processes or methodologies
- **specifications**: Measurements, capacities, tolerances, etc.
- **terminology**: Technical terms with definitions

### common_misconceptions
Misconceptions and their corrections:
- **misconception**: What people commonly get wrong
- **reality**: What's actually true
- **source**: Reference supporting the reality

### story_applications
Connections between research and story elements:
- **element**: Character, location, plot point, scene, etc.
- **chapter**: Specific chapter/scene reference
- **application**: How the research applies to this element

### sources
All sources cited in the research:
- **name**: Source name or title
- **url**: Full URL or citation reference
- **type**: Either "academic", "professional", "government", or "general"
- **reliability**: Either "high", "medium", or "low"

### critical_facts
Facts that are critical for story accuracy:
- **fact**: The critical fact
- **importance**: Why it matters for the story
- **chapter**: Specific chapter/scene if applicable

### areas_of_uncertainty
Facts or topics that need more research:
- Free-form text describing the uncertainty
- Include conflicting information if applicable
- Note whether this affects the story significantly

## Usage Notes

1. **Maintain Source Linkage** — Every fact must trace back to its source
2. **Use Consistent Formatting** — Follow the YAML structure exactly
3. **Complete Metadata** — Fill all applicable fields for each entry
4. **Update Regularly** — Modify as new information is discovered
5. **Flag Issues** — Use verification and reliability fields to indicate quality
