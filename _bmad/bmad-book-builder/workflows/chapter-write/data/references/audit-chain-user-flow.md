# Audit Chain — User Interaction Flow

**Purpose:** Guide users through the audit chain, which is integrated into the chapter-write workflow as steps 04-06.

**Reference:** See `data/references/automated-audit-chain.md` for complete technical documentation.

---

## Overview

The audit chain is built into the final three steps of the chapter-write workflow. It runs automatically after the draft is complete — no separate invocation needed.

| Step | Name | What Happens |
|------|------|-------------|
| 04 | Self-Review | Style audit against style profile. Findings presented. Author approves fixes. |
| 05 | Audit | Character audit + continuity check. Audit file + thematic analysis created. |
| 06 | Bible Update | Tracking files (themes, emotions, rhythm) + bible files (characters, locations, objects, themes) + project status updated. Chapter locked as v1-complete. |

---

## User Interaction Points

### After Step 04 (Style Audit)

```text
**Style Audit — Chapter {N}**

| # | Check | Result | Notes |
|---|-------|--------|-------|
...

Fixes Required: {count}

Shall I apply fixes? [Y] Yes / [N] No / [S] Selective
```

Author reviews findings and approves fixes before they're applied.

### After Step 05 (Character & Continuity Audit)

If critical issues found:
```text
⚠️ Critical issue: {description}

[F] Fix — Apply recommended correction
[A] Accept — Keep as-is (author decision)
[D] Defer — Flag for future review
```

If no critical issues:
```text
Audit complete. No critical issues. Proceeding to bible updates...
```

### After Step 06 (Bible Update & Finalization)

```text
Chapter {N} — "{title}" — v1-complete

Files created:
- tracking/audits/audit-chapter-{N}.md
- tracking/themes/chapter-{N}-themes.md

Files updated:
- tracking/themes.md, emotions.md, rhythm.md
- bible/characters.md, locations.md, objects.md, themes.md
- project-status.yaml

Ready for the next chapter.
```

---

## Status Storage

Audit status is tracked via:
- **`stepsCompleted` array** in chapter frontmatter — indicates which audit steps are done
- **`tracking/audits/audit-chapter-{N}.md`** — detailed style, character, and continuity findings
- **No separate `auditChain` block** in chapter frontmatter

---

## Running Audits Independently

If needed outside the chapter-write workflow:
- Style audit: Load style-coach agent + style profile
- Character audit: `character-audit -c {chapter_number}`
- Bible update: `living-bible -e`
- Review: `review -c {chapter_number}`
