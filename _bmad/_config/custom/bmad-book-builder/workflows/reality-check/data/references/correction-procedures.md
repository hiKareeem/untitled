# Correction Procedures for Step 6

## Research Dossier Recommendation Process

### Identification Criteria

Topics warranting research dossiers must meet these criteria:

**Primary Criteria:**
- Multiple verified facts on same topic (3+ facts)
- High-stakes domain (medical, legal, technical, historical)
- Topic appears in multiple chapters
- Complex subject warranting ongoing reference

### Presentation Template

For each recommended dossier, use this structure:

```markdown
## 📚 Research Dossier Recommendations

Based on this reality check, I recommend creating {count} new research dossiers to build our knowledge base:

### Dossier 1: {Topic}

**Facts to Include:** {count}
**Appears in Chapters:** {list}
**Sample Facts:**
- {fact 1} (verified via {source})
- {fact 2} (verified via {source})

**Why Create This Dossier:**
{justification}

**Create this dossier?** [Y]es / [N]o
```

### Dossier Creation Process

**For each approved dossier:**

1. **Create dossier file** at `{researchFolder}/{topic-name}-facts.md`
2. **Include all verified facts, sources, and story applications**
3. **Update user:** "✅ Created: {dossier-name}"

**Template reference:** See `data/templates/reality-check-templates.yaml` for dossier structure

### Dossier Structure

Brief structure for recommended dossiers:
- dossier_topic, fact_count, chapters_involved
- facts list (claim_id, fact, source)
- justification

## Menu Handling Logic

### User Options

- **IF R:** Offer to show specific sections (HIGH issues, MEDIUM issues, Verified facts, etc.)
- **IF C:** Prompt for dossier topic, create if possible
- **IF Q or other:** Return to Documentaliste menu, exit workflow

### Severity Adjustment Process

**For each issue presented:**

1. Wait for severity confirmation or adjustment
2. **IF user changes severity:** Update issue severity in output file
3. **IF user confirms:** Proceed to next issue

## Final Report Generation

### Output File Updates

**Append final summary to {outputFile}:** See `data/templates/final-report-template.md`

**Update frontmatter:**

```yaml
---
stepsCompleted: ['step-01-select-scope', 'step-02-extract-claims', 'step-03-check-references', 'step-04-web-verification', 'step-05-identify-issues', 'step-06-provide-corrections']
lastStep: 'step-06-provide-corrections'
date: '{current_date}'
user_name: '{user_name}'
scope: '{scope_identifier}'
scopeType: '{scope_type}'
targetChapters: [{list}]
claimsAnalyzed: {total}
issuesFound: {issues}
highSeverityIssues: {H-final}
mediumSeverityIssues: {M-final}
lowSeverityIssues: {L-final}
verifiedClaims: {verified}
dossiersCreated: {count}
dossiersConsulted: {count}
verificationStatus: 'complete'
---
```

### Latest Report Link

**Create or update symlink/copy:**
- Copy `{outputFile}` to `{bbb_output_folder}/reality-check/chapter-{scope}-report-latest.md`
- This provides quick access to most recent reality check

## Correction Approach Recommendations

**Recommended Workflow for Authors:**

1. **Fix HIGH severity issues first** — These affect story credibility
2. **Address MEDIUM severity issues** — These affect reader trust
3. **Polish LOW severity issues** — Optional for perfectionist revision
4. **Use research dossiers** — Reference existing and new dossiers while making corrections

## Next Steps Guidance

### Immediate Actions

1. **Review this report** — Read through all issues and corrections
2. **Plan corrections** — Decide which correction options work best for your story
3. **Make corrections** — Edit your chapters using the recommended fixes
4. **Run follow-up check** — Use this workflow again to verify corrections

### Future Reality Checks

- Run after writing technical scenes
- Run before final manuscript publication
- Run when beta readers flag factual issues

### Documentaliste Services

**Documentaliste is available for:**
- Quick fact searches: `[QS] Quick Search`
- Chapter verification: `[VC] Verify Chapter`
- Research dossier creation: `[RD] Research Dossier`
- Full reality check: `[RC] Reality Check`
