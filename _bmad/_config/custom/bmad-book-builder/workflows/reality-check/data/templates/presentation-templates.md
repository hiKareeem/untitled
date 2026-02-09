# Presentation Templates for Step 6

## Executive Summary Template

```markdown
## 📋 Executive Summary

**Scope:** {scope description}
**Chapters Verified:** {list}
**Date:** {current_date}

### Overall Assessment

| Metric | Count | Status |
|--------|-------|--------|
| **Claims Analyzed** | {total} | ✅ |
| **Issues Found** | {issues} | ⚠️ |
| **Verified Accurate** | {verified} | ✅ |
| **HIGH Severity** | {H-total} | 🔴 Must Fix |
| **MEDIUM Severity** | {M-total} | 🟡 Should Address |
| **LOW Severity** | {L-total} | 🟢 Optional |

### Key Findings

**🔴 Critical Issues (Must Fix):**
{list of HIGH severity issues with brief descriptions}

**🟡 Important Issues (Should Address):**
{list of top MEDIUM severity issues}

**✅ Strengths (Verified Accurate):**
{list of interesting or important verified facts}

### Research Knowledge Base

**New Research Dossiers Recommended:** {count}
{list of suggested dossiers with topics}

**Existing Dossiers Used:** {count}
{list of dossiers that provided verifications}

---

Proceed to detailed findings? [Y]es / [N]o (see summary only)
```

## HIGH Severity Issues Presentation Template

```markdown
## 🔴 HIGH Severity Issues ({H-total})

> **Must Fix:** These issues break story credibility and will definitely be noticed by readers.

### Issue I001: {Title}

**Location:** Chapter {N}, Scene {M}
**Category:** {technical|factual|logical}

**The Claim:**
> "{excerpt from story}"

**The Problem:**
{detailed explanation with evidence}

**Why This Matters:**
{impact on story credibility and reader trust}

**Correction Options:**

**1. {Recommended approach}**
- **What to change:** {specific change}
- **How it affects the story:** {impact}
- **Effort required:** {high|medium|low}

**2. {Alternative approach}**
- **What to change:** {specific change}
- **How it affects the story:** {impact}
- **Effort required:** {high|medium|low}

**3. {Another alternative if applicable}**
- **What to change:** {specific change}
- **How it affects the story:** {impact}
- **Effort required:** {high|medium|low}

**Severity Confirmation:**
This issue is rated **HIGH** because {reasoning}.
Adjust severity? [H]igh / [M]edium / [L]ow / [Enter] to confirm

---

{Repeat for each HIGH severity issue}
```

## MEDIUM Severity Issues Presentation Template

```markdown
## 🟡 MEDIUM Severity Issues ({M-total})

> **Should Address:** These issues stretch believability and some readers will notice.

### Issue I00X: {Title}

**Location:** Chapter {N}, Scene {M}

**The Issue:** {brief description}
**Suggested Fix:** {correction}

Adjust severity? [H]igh / [M]edium / [L]ow / [Enter] to confirm

---

{Repeat for each MEDIUM severity issue}
```

## LOW Severity Issues Presentation Template

```markdown
## 🟢 LOW Severity Issues ({L-total})

> **Optional Polish:** Minor nitpicks for perfectionist revision.

**Summary:**
{list of LOW severity issues with brief one-line descriptions}

**Review Details?** [Y]es / [N]o

**IF [Y]es:** Present details with option to adjust each severity
**IF [N]o:** Proceed to Verified Facts
```

## Verified Facts Presentation Template

```markdown
## ✅ Verified Facts ({verified})

Claims confirmed accurate through research dossiers and web verification.

### Technical Accuracy ({verified-tech})
{list with sources}

### Factual Accuracy ({verified-fact})
{list with sources}

### Logical Consistency ({verified-logic})
{list with reasoning}

**What This Means:**
These claims are factually sound. You can write with confidence knowing these details are accurate.
```

## Completion Summary Template

```markdown
**✅ Reality Check Complete!**

### 📊 Final Statistics

**Claims Analyzed:** {total}
**Issues Found:** {issues} (HIGH: {H}, MEDIUM: {M}, LOW: {L})
**Verified Accurate:** {verified}

**Research Dossiers:**
- Created: {count} new
- Consulted: {count} existing

### 📄 Report Location

**Full Report:** `{outputFile}`
**Latest Report:** `{bbb_output_folder}/reality-check/chapter-{scope}-report-latest.md`

### 🎯 Next Steps

1. **Read the full report** — All issues are documented with corrections
2. **Prioritize HIGH severity fixes** — These affect story credibility
3. **Use research dossiers** — Reference them while making corrections
4. **Run follow-up check** — Verify corrections are accurate

### 💡 Strengths to Celebrate

{list of interesting verified facts or what went well}

**Your commitment to factual accuracy shows! Readers will notice the authenticity.**

---

**Would you like to:**
- **[R]e-read the report** — Review specific sections
- **[C]reate another dossier** — Add more to research base
- **[Q]uit** — Exit to Documentaliste menu

Your choice: _
```
