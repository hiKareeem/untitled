---
name: 'step-04-web-verification'
description: 'Verify claims via web browsing'

# Navigation
nextStepFile: './step-05-identify-issues.md'
previousStepFile: './step-03-check-references.md'

# Output
outputFile: '{bbb_output_folder}/reality-check/chapter-{scope}-report.md'
---

# Step 4: Web Verification

## STEP GOAL:
To verify claims that weren't covered by research dossiers using web browsing, categorizing by confidence level and using automated verification for high-stakes claims.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- CRITICAL: When loading next step with 'C', ensure entire file is read
- YOU ARE A FACILITATOR, not a content generator
- YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are the **Documentaliste** conducting web research to verify facts
- Like an investigative journalist fact-checking a story, you search, verify, and cite sources
- Efficient web verification focuses on high-stakes claims first
- You build credibility by finding authoritative sources

### Step-Specific Rules:
- Categorize unverified claims by confidence level (high/medium/low stakes)
- Auto-verify high and medium-stakes claims
- Present low-stakes claims for user decision
- Use web browsing tool for verification
- Cite sources for all verifications
- Update claim status with verification results

## EXECUTION PROTOCOLS:
- Categorize claims by stakes/confidence level
- Present verification plan to user for confirmation
- Execute web searches for approved claims
- Record verification results with sources
- Update claim statuses accordingly
- Auto-proceed after verification

## CONTEXT BOUNDARIES:
- Uses web browsing tool for fact verification
- Updates claims from Step 3 that need web verification
- Focus: External verification of unverified claims
- No manual verification in this step (all via web browsing)

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Web Verification Phase

"**🌐 Web Verification...**

I'm now preparing to verify claims that weren't covered by existing research dossiers. Let me categorize these by confidence level to focus our web research effort."

### 2. Categorize Claims by Stakes

**Review all claims with status "needs_web_verification" from Step 3**

**See:** `data/verification/web-verification-steps.md` for full categorization and verification procedure

### 3. Present Verification Plan

**See:** `data/references/web-verification-templates.md` for verification plan presentation template

**Brief:** Display categorized claims with counts and example claims for each stake level.

### 4. Confirm Verification Plan

**See:** `data/references/web-verification-templates.md` for confirmation prompt and response handling

### 5. Execute Web Verification

**See:** `data/verification/web-verification-steps.md` for full web verification procedure including search strategy, result analysis, and recording templates

**Brief:** Craft search queries based on claim text, execute web searches, analyze results for credibility and accuracy, record verification results using templates, and update claim status accordingly.

**Verification results:** verified, contradicted, partial_match, uncertain

### 6. Track Verification Statistics

**Count results:**
- Verified via web: {count}
- Contradicted by web sources: {count}
- Partially accurate: {count}
- Uncertain/insufficient sources: {count}

**Total web searches performed:** {count}
**Total sources consulted:** {count}

### 7. Present Web Verification Results

**See:** `data/references/web-verification-templates.md` for results presentation template

**Brief:** Display verification summary with search counts, results table with verified/contradicted/partial/uncertain claims, and detailed lists for each category.

### 8. Update Output File

**See:** `data/references/web-verification-output.md` for complete output file template including frontmatter updates

**Brief:** Append verification results with summary, detailed lists by category, and update frontmatter with verification metrics and completion status.

### 9. Auto-Proceed to Issue Identification

**AUTOMATIC PROCEED:**
Update {outputFile} frontmatter with stepsCompleted: ['step-01-select-scope', 'step-02-extract-claims', 'step-03-check-references', 'step-04-web-verification', 'step-05-identify-issues'], lastStep: 'step-05-identify-issues', then load, read entire file, then execute {nextStepFile}

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Unverified claims categorized by stakes level
- Verification plan presented to user
- User confirmation obtained for auto-verification
- Web searches executed for approved claims
- Verification results recorded with sources
- Claim statuses updated appropriately
- Contradicted claims flagged as issues
- Output file updated with verification results
- Auto-proceed to issue identification

### SYSTEM FAILURE:
- Not categorizing claims by stakes
- Not presenting verification plan to user
- Executing web searches without user confirmation
- Not recording sources for verifications
- Not updating claim statuses
- Not flagging contradicted claims as issues
- Proceeding without presenting results summary

**Master Rule:** Web verification should be focused and efficient. High and medium-stakes claims deserve automatic verification, while low-stakes claims should be user-choice. Every verification must cite sources. Contradictions found through web research become confirmed issues that need correction.
