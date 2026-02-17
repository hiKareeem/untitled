---
name: 'step-02-extract-claims'
description: 'Extract factual and technical claims from content'

# Navigation
nextStepFile: './step-03-check-references.md'
previousStepFile: './step-01-select-scope.md'

# Output
outputFile: '{bbb_output_folder}/reality-check/chapter-{scope}-report.md'
chaptersFolder: '{bbb_output_folder}/current-book/chapters/'
---

# Step 2: Extract Claims

## STEP GOAL:
To systematically extract all factual and technical claims from the target content, categorize them by type and priority, and prepare them for verification.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Documentaliste** performing systematic claim extraction
- Like a researcher cataloging artifacts, you identify and categorize all verifiable claims
- Thorough extraction ensures no factual issues go unnoticed
- You organize claims by priority to focus verification effort efficiently

### Step-Specific Rules:
- Extract ALL claims, not just obvious ones
- Categorize every claim by type (technical/factual/logical) and priority (high/medium/low)
- Include location information (chapter, scene, excerpt) for each claim
- Auto-proceed after extraction and categorization
- FORBIDDEN to skip claims or prioritize during extraction

## EXECUTION PROTOCOLS:
- Read target content thoroughly
- Extract claims in three categories: Technical Accuracy, Factual Accuracy, Logical Consistency
- Assign priority levels based on credibility impact
- Organize claims with location references
- Update output file with extraction summary
- Auto-proceed to reference check

## CONTEXT BOUNDARIES:
- Reads content from `chaptersFolder` based on scope from Step 1
- Updates `outputFile` with extracted claims
- No external verification in this step (that's Step 3-4)
- Focus: Identification and categorization, not validation

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Claim Extraction Phase

"**📋 Extracting Claims...**

I'm now analyzing the content to identify all factual and technical claims that need verification. This includes:

- **Technical Accuracy:** Professions, tools, procedures, equipment
- **Factual Accuracy:** Historical facts, geographic details, scientific facts
- **Logical Consistency:** Cause-effect, time sequences, physical constraints

I'll categorize each claim by priority so we focus verification effort where it matters most.

Extracting claims from: {scope description}"

### 2. Load Target Content

**Read content based on scope:**

**Chapter scope:** Load `{chaptersFolder}/chapter-{N}.md`, extract chapter title, scenes

**Scene scope:** Load `{chaptersFolder}/chapter-{N}.md`, focus on specified scene range (scenes typically marked with `## Scene {X}` or similar)

**Element scope:** Load specified chapters, scan for content related to the element topic

**All written scope:** Load all completed chapters sequentially, process each chapter's content

### 3. Extract Technical Accuracy Claims

**See:** `data/extraction-procedures/technical-claims.md` for full extraction procedure

**Brief:**
- Scan for profession/trade procedures, tools/equipment usage, technical processes
- Use claim template from reference file
- Assign priority: HIGH (professional procedures), MEDIUM (technical processes), LOW (background details)

### 4. Extract Factual Accuracy Claims

**See:** `data/extraction-procedures/factual-claims.md` for full extraction procedure

**Brief:**
- Scan for historical facts, geographic details, scientific facts, temporal markers
- Use claim template from reference file
- Assign priority: HIGH (historical/scientific facts), MEDIUM (geographic details), LOW (minor mentions)

### 5. Extract Logical Consistency Claims

**See:** `data/extraction-procedures/logical-claims.md` for full extraction procedure

**Brief:**
- Scan for cause-effect relationships, time sequences, physical constraints
- Use claim template from reference file
- Assign priority: HIGH (impossibilities), MEDIUM (sequence issues), LOW (minor quirks)

### 6. Organize and Summarize Extractions

**Count claims by category and priority:**
- Technical claims: {count} (High: {H}, Medium: {M}, Low: {L})
- Factual claims: {count} (High: {H}, Medium: {M}, Low: {L})
- Logical claims: {count} (High: {H}, Medium: {M}, Low: {L})
- **Total claims:** {total}

### 7. Update Output File

**Append to {outputFile}:**

```markdown
## Claims Extracted

### Summary

**Total Claims Extracted:** {total}

| Category | High Priority | Medium Priority | Low Priority | Total |
|----------|---------------|-----------------|--------------|-------|
| Technical Accuracy | {T-H} | {T-M} | {T-L} | {T-total} |
| Factual Accuracy | {F-H} | {F-M} | {F-L} | {F-total} |
| Logical Consistency | {L-H} | {L-M} | {L-L} | {L-total} |
| **TOTAL** | **{H-total}** | **{M-total}** | **{L-total}** | **{total}** |

### Verification Focus

**High-Priority Claims ({H-total}):** Will verify thoroughly with research dossiers and web browsing
**Medium-Priority Claims ({M-total}):** Will verify against research dossiers, web browse if needed
**Low-Priority Claims ({L-total}):** Noted for reference, verified only if obvious issues

---

### Technical Accuracy Claims ({T-total})

{list or table of technical claims with ID, category, location, brief description}

**High Priority:**
- T001: {claim} — Chapter {N}, Scene {M}
- T002: {claim} — Chapter {N}, Scene {M}

**Medium Priority:**
- {claims}

**Low Priority:**
- {claims}

---

### Factual Accuracy Claims ({F-total})

{same structure as technical claims}

---

### Logical Consistency Claims ({L-total})

{same structure as technical claims}

---

## Extraction Complete

All claims have been extracted and categorized. Proceeding to reference check...

---
```

**Update frontmatter:**
```yaml
---
stepsCompleted: ['step-01-select-scope', 'step-02-extract-claims']
lastStep: 'step-02-extract-claims'
claimsExtracted: {total}
highPriorityClaims: {H-total}
mediumPriorityClaims: {M-total}
lowPriorityClaims: {L-total}
extractionComplete: true
---
```

### 8. Present Extraction Summary

Display:

"**✅ Claim Extraction Complete**

### Claims Found: {total}

| Category | High | Medium | Low | Total |
|----------|------|--------|-----|-------|
| Technical | {T-H} | {T-M} | {T-L} | {T-total} |
| Factual | {F-H} | {F-M} | {F-L} | {F-total} |
| Logical | {L-H} | {L-M} | {L-L} | {L-total} |
| **TOTAL** | **{H-total}** | **{M-total}** | **{L-total}** | **{total}** |

### Verification Focus

- **High-Priority ({H-total}):** Thorough verification with dossiers + web browsing
- **Medium-Priority ({M-total}):** Verification against dossiers, web as needed
- **Low-Priority ({L-total}):** Noted, verified if obvious issues found

**Now checking research dossiers for relevant references...**"

### 9. Auto-Proceed to Reference Check

**AUTOMATIC PROCEED:**
Update {outputFile} frontmatter with stepsCompleted: ['step-01-select-scope', 'step-02-extract-claims', 'step-03-check-references'], lastStep: 'step-03-check-references', then load, read entire file, then execute {nextStepFile}

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- All target content read and analyzed
- Technical accuracy claims extracted with locations
- Factual accuracy claims extracted with locations
- Logical consistency claims extracted with locations
- All claims categorized by type and priority
- Claims organized with IDs and metadata
- Output file updated with extraction summary
- Auto-proceed to reference check

### SYSTEM FAILURE:
- Not reading all target content
- Missing claims in any category
- Not assigning priority levels
- Not including location information (chapter, scene, excerpt)
- Not organizing claims systematically
- Skipping low-priority claims

**Master Rule:** Comprehensive claim extraction is essential for thorough reality checking. Every verifiable claim should be identified, categorized, and tracked. Missing a claim now means missing a potential factual error later. Extract everything, let the verification process filter what matters.
