# Web Verification Output File Template

## Output File Content

Append to {outputFile}:

```markdown
## Web Verification Results

### Verification Summary

**Web Searches Performed:** {searches}
**Sources Consulted:** {sources}
**Claims Verified:** {verified_new}
**Claims Contradicted:** {contradicted_new}
**Partial Matches:** {partial}
**Uncertain:** {uncertain}

---

### Newly Verified Claims ({verified_new})

{detailed list with sources and findings}

---

### Claims Contradicted by Web Sources ({contradicted_new}) ⚠️

{detailed list with sources and findings — these become issues}

---

### Partial Matches ({partial})

{detailed list with notes for clarification}

---

### Uncertain Claims ({uncertain})

{list with notes about insufficient sources}

---

## Web Verification Complete

All possible claims have been verified via web research. Proceeding to issue identification...

---
```

## Frontmatter Updates

Update frontmatter:

```yaml
---
stepsCompleted: ['step-01-select-scope', 'step-02-extract-claims', 'step-03-check-references', 'step-04-web-verification']
lastStep: 'step-04-web-verification'
webSearchesPerformed: {searches}
sourcesConsulted: {sources}
newlyVerified: {verified_new}
newlyContradicted: {contradicted_new}
webVerificationComplete: true
---
```

## Auto-Proceed Frontmatter

For auto-proceed to next step, update frontmatter:

```yaml
---
stepsCompleted: ['step-01-select-scope', 'step-02-extract-claims', 'step-03-check-references', 'step-04-web-verification', 'step-05-identify-issues']
lastStep: 'step-05-identify-issues'
---
```
