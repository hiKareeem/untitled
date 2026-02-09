---
name: 'step-01-validate'
description: 'Validate character dossier against quality standards'

# File References
targetFile: '{provided_path}'

# Menu Options
advancedElicitation: false
partyMode: false

---

# Character Validation

## STEP GOAL:
To validate a character dossier against quality standards, identifying strengths, weaknesses, and areas for improvement.

## MANDATORY EXECUTION RULES (READ FIRST):

See: `../../data/procedures/mode-procedures.md` - Validate Mode section

### Step-Specific Rules:
- 🎯 This is VALIDATION mode — assess against standards
- 💬 Be constructive — identify both strengths and weaknesses
- ✅ Provide actionable feedback
- 🚫 NOT an edit workflow — only validation

## EXECUTION PROTOCOLS:
- 🎯 Follow the MANDATORY SEQUENCE exactly
- 📖 Load and read target dossier
- 📊 Assess against all quality standards (see `../../data/references/character-frameworks.md`)
- 💬 Provide validation report with scores
- 🔄 Offer options for addressing issues

## MANDATORY SEQUENCE

### 1. Load Target Dossier

"**Let me load the character dossier for validation...**"

Verify `{targetFile}` exists and is readable.

**IF file doesn't exist:**
"I can't find a character dossier at that path. Please verify the path and try again."

End validation workflow.

**IF file exists and is valid:**
Proceed to step 2.

### 2. Initial Assessment

"**Found!** Validating **{characterName}**..."

Extract character name from frontmatter or file header.

### 3. Run Validation Checks

See quality standards in `../../data/references/character-frameworks.md`

**Sections to check:**
- Basic Information
- Physical appearance
- Personality
- Desires and fears
- Arc de transformation (or Contexte et histoire)
- Skills and weaknesses
- Relationships and connections
- Voice and mannerisms
- Themes explored

**Quality checks:**
- Completeness: [X]/9 sections complete
- Specificity: PASS/NEEDS WORK/FAIL
- Contradictions: Number and quality assessed
- Psychology: Coherence evaluated
- Voice: Distinctiveness evaluated
- Arc: Clarity and necessity evaluated
- Consistency: Internal alignment evaluated
- Story Integration: Story-serving role evaluated
- Emotional Truth: Authenticity evaluated

### 4. Calculate Overall Score

**Calculate:**
- Completeness: [X]/9
- Quality Checks: [X]/9 passed

**Overall Rating:**
- **9/9 + 8-9/9** = ⭐⭐⭐⭐⭐ EXCELLENT
- **8-9/9 + 6-7/9** = ⭐⭐⭐⭐ GOOD
- **7-8/9 + 5-6/9** = ⭐⭐⭐ ADEQUATE
- **6-7/9 + 3-4/9** = ⭐⭐ NEEDS WORK
- **<6/9 or <3/9** = ⭐ INCOMPLETE

### 5. Generate Validation Report

"**✅ Validation Complete!**"

Display report with:
- File location and validation date
- Overall rating (stars)
- Completeness score
- Quality checks with comments
- Strengths (3-5 items)
- Areas for improvement (prioritized)

### 6. Provide Recommendations

Based on validation results:
- **⭐⭐⭐⭐⭐ or ⭐⭐⭐⭐:** Character is excellent/solid
- **⭐⭐⭐:** Character has room for growth
- **⭐⭐ or ⭐:** Character needs more development

### 7. Present Next Steps Options

"**What would you like to do next?**

**[E]** Edit — Address the issues identified
**[R]** Re-validate — Run validation again after changes
**[N]** New Character — Validate a different character
**[X]** Exit — Complete validation"

#### Menu Handling Logic:
- IF E: Load `../steps-e/step-01-assess.md` with `{targetFile}` as target
- IF R: Reload this validation step
- IF N: Prompt for new character path
- IF X: Present completion message and end workflow

### 8. Completion Message (IF X selected)

"**Validation complete!** ✅

**{characterName}** received a rating of ⭐ [X/5 STARS].

**Summary:**
[Brief recap of key findings]

Use this feedback to guide further character development. Consistent validation ensures your story bible maintains high quality standards.

Come back anytime to validate other characters or re-validate after making changes.

**Happy writing!** ✍️"

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- All 9 quality checks performed
- Specific, actionable feedback provided
- Overall score calculated correctly
- Strengths and weaknesses both identified
- Recommendations are prioritized and helpful
- Author has clear path forward if issues exist

### ❌ SYSTEM FAILURE:
- Skipped quality checks
- Generic feedback without specifics
- No actionable recommendations
- Score calculation errors

**Master Rule:** Validation should be diagnostic, not judgmental. The goal is improvement, not criticism.
