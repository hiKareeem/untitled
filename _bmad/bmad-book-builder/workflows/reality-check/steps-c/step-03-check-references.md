---
name: 'step-03-check-references'
description: 'Check claims against existing research dossiers'

# Navigation
nextStepFile: './step-04-web-verification.md'
previousStepFile: './step-02-extract-claims.md'

# Output
outputFile: '{bbb_output_folder}/reality-check/chapter-{scope}-report.md'
researchFolder: '{bbb_output_folder}/research/dossiers/'
---

# Step 3: Check References

## STEP GOAL:
To cross-reference extracted claims against existing research dossiers, identify matches, and determine which claims require web verification.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Documentaliste** consulting existing research knowledge
- Like a librarian checking reference materials before new research, you leverage existing dossiers
- Efficient reference checking avoids redundant web searches
- You build on previous research while identifying gaps

### Step-Specific Rules:
- Scan ALL research dossiers in the research folder
- Match claims to dossiers by keywords and topics
- Allow user to specify additional dossiers
- Update claim status based on dossier matches
- Auto-proceed after reference check

## EXECUTION PROTOCOLS:
- Scan research dossier directory for available files
- Match extracted claims to dossiers by topic keywords
- Read relevant dossiers to verify claims
- Allow user input for additional dossiers
- Update claim status and document matches
- Auto-proceed to web verification

## CONTEXT BOUNDARIES:
- Reads research dossiers from `researchFolder`
- Updates claims extracted in Step 2 with dossier references
- No web browsing in this step (that's Step 4)
- Focus: Leveraging existing research, identifying gaps

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Reference Check Phase

"**📚 Checking Research Dossiers...**

I'm now consulting existing research dossiers to verify claims against previously researched facts. This avoids redundant web searches and leverages our growing knowledge base.

Let me scan the research library..."

### 2. Scan Research Dossier Directory

**Check if research folder exists:**
- IF `{researchFolder}` does not exist: "⚠️ No research dossiers found (folder doesn't exist yet). All claims will proceed to web verification."
- Proceed to Step 4

**IF research folder exists:**
- Scan for `.md` files in `{researchFolder}/`
- Collect: Dossier file names, titles, topics
- Store as: `available_dossiers` array

After scanning:
"✅ **Research Dossiers Found:** {count}
- {list of dossier titles or file names}"

**IF no dossiers found:**
"⚠️ No research dossiers found. All claims will proceed to web verification."
- Proceed to Step 4

### 3. Match Claims to Dossiers

**See:** `data/verification/reference-checking.md` for full matching procedure

**For each claim from Step 2:**
- Extract keywords from claim text
- Search dossier titles and content for keyword matches
- For matching dossiers: read content, extract relevant facts, match claim to specific facts
- Update claim status using template from reference file

### 4. Present Reference Check Summary

**Count results by verification status and priority**

**See:** `data/references/reference-check-summary.md` for summary template

Display the complete summary with:
- Claims verified via dossiers
- Claims needing web verification
- Claims contradicted by dossiers (these become issues)
- Claims with partial matches
- Breakdown by priority level

### 5. Allow Additional Dossier Specification

**Prompt:**
"Any additional research dossiers to consult? (or press Enter to continue to web verification)

Enter dossier name(s) separated by commas, or press Enter to proceed: "

**IF user provides dossier names:**
- Verify each dossier exists
- IF exists: Add to consultation list, check against remaining claims
- IF not found: "⚠️ Dossier '{name}' not found. Available dossiers: {list}"

**Recount results after additional consultation:**
"**After Additional Consultation:**
Claims Verified via Dossiers: {new_verified_count}
Claims Needing Web Verification: {new_web_count}"

### 6. Update Output File

**See:** `data/references/reference-check-output.md` for output template and frontmatter format

Append reference check results to {outputFile} including:
- Dossiers consulted
- Verification results table
- Results by priority
- Verified claims list
- Claims needing web verification
- Contradicted claims (issues)
- Partial matches

Update frontmatter with completion status

### 7. Auto-Proceed to Web Verification

**AUTOMATIC PROCEED:**
Update {outputFile} frontmatter with stepsCompleted: ['step-01-select-scope', 'step-02-extract-claims', 'step-03-check-references', 'step-04-web-verification'], lastStep: 'step-04-web-verification', then load, read entire file, then execute {nextStepFile}

---

## SYSTEM SUCCESS/FAILURE METRICS

**See:** `data/references/reference-check-metrics.md` for complete success/failure criteria

### Key Success Indicators:
- All research dossiers scanned and matched
- Claims updated with verification status
- Contradictions flagged as issues
- Output file updated with complete results
- Auto-proceed to web verification

### Critical Failure Conditions:
- Skipping dossier scanning or matching
- Not updating claim statuses
- Missing contradiction flags
- Proceeding without user summary
