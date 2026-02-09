# Reference Check Output Template

## Output File Format

**Append to {outputFile}:**

```markdown
## Reference Check Results

### Dossiers Consulted

**Available Research Dossiers:** {total_dossiers}
**Dossiers with Relevant Matches:** {matched_dossiers}

{list of consulted dossiers with match counts}

### Verification Results

| Result | Count | Percentage |
|--------|-------|------------|
| ✅ Verified via Dossier | {verified} | {verified%} |
| 🔍 Needs Web Verification | {web} | {web%} |
| ❌ Contradicted by Dossier | {contradicted} | {contra%} |
| 📝 Partial Match | {partial} | {partial%} |
| **TOTAL** | **{total}** | **100%** |

### Results by Priority

**High-Priority Claims:** Verified: {H-verified} | Need Web: {H-web} | Contradicted: {H-contra}
**Medium-Priority Claims:** Verified: {M-verified} | Need Web: {M-web} | Contradicted: {M-contra}
**Low-Priority Claims:** Verified: {L-verified} | Need Web: {L-web} | Contradicted: {L-contra}

---

### Verified Claims ({verified})

{list of claims verified via dossiers}

---

### Claims Needing Web Verification ({web})

{list of claims requiring web browsing, organized by category}

---

### Contradicted Claims ({contradicted}) ⚠️

{list of claims contradicted by dossiers — these become issues}

---

### Partial Matches ({partial})

{list of claims with partial matches}

---

## Reference Check Complete

Proceeding to web verification for {web} claims...

---
```

## Output File Frontmatter Update

```yaml
---
stepsCompleted: ['step-01-select-scope', 'step-02-extract-claims', 'step-03-check-references']
lastStep: 'step-03-check-references'
claimsVerified: {verified}
claimsNeedWeb: {web}
claimsContradicted: {contradicted}
referenceCheckComplete: true
---
```
