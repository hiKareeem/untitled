# Reference Check Summary Template

## Summary Display Format

Display this after completing the reference check:

```markdown
**✅ Reference Check Complete**

### Dossier Matches Found

**Claims Verified via Dossiers:** {verified_count}
**Claims Needing Web Verification:** {web_count}
**Claims Contradicted by Dossiers:** {contradicted_count} ⚠️
**Partial Matches:** {partial_count}

### Relevant Dossiers Consulted

{list of dossiers that provided matches}

### Verification Status by Priority

| Priority | Verified | Needs Web | Contradicted | Total |
|----------|----------|-----------|--------------|-------|
| High | {H-verified} | {H-web} | {H-contra} | {H-total} |
| Medium | {M-verified} | {M-web} | {M-contra} | {M-total} |
| Low | {L-verified} | {L-web} | {L-contra} | {L-total} |
| **TOTAL** | **{verified}** | **{web}** | **{contra}** | **{total}** |
```

## Breakdown by Priority

- High-priority verified: {count}, needs web: {count}, contradicted: {count}
- Medium-priority verified: {count}, needs web: {count}, contradicted: {count}
- Low-priority verified: {count}, needs web: {count}, contradicted: {count}
