# Automated Audit Chain Reference
# Integrated into chapter-write steps 04-06

> **🎯 AUDIT CHAIN — Integrated into the chapter-write workflow**
>
> The audit chain is built into the final three steps of the chapter-write workflow.
> It executes automatically as part of the normal chapter writing process.
>
> | Workflow Step | Audit Chain Function |
> |--------------|---------------------|
> | step-04-self-review | Style audit against style profile, apply fixes |
> | step-05-audit | Character audit, continuity check, per-chapter thematic analysis |
> | step-06-bible-update | Update tracking (themes, emotions, rhythm), bible (characters, locations, objects, themes), project status |

## Chain Sequence

### Step 04: Style Audit (step-04-self-review.md)
**Voice consistency validation**

**Checks:**
- Negation-before-assertion count (POV-specific targets)
- Fragment/paratactic percentage
- Bimodal paragraphs
- Em dashes, italics, dialogue ratio
- Sensory hierarchy (POV-specific order)
- Emotion via physical sensation (never tell directly)
- Anti-slop checklist (zero tolerance)
- Metaphor domain (POV-specific, no cross-contamination)
- Dialogue tags (only "said" + action beats)
- Average sentence length

**Output:** Findings presented to author. Fixes applied with approval.

### Step 05: Character & Continuity Audit (step-05-audit.md)
**Content consistency validation**

**Character Audit:**
- Every character checked against dossier/bible
- Voice/speech register, mannerisms, psychological state, relationships
- Coherence scored out of 10

**Continuity Check:**
- Timeline consistency with previous chapters
- Object/location continuity with bible
- Character knowledge boundaries
- Plan adherence

**Output:**
- `tracking/audit-chapter-{N}.md` — structured audit findings
- `tracking/chapter-{N}-themes.md` — per-chapter thematic analysis

### Step 06: Bible & Tracking Update (step-06-bible-update.md)
**Data propagation to tracking and bible files**

**Tracking updates:**
- `tracking/themes.md` — chapter entries in all 8 theme tables + Progression by Chapter
- `tracking/emotions.md` — emotional beats per character
- `tracking/rhythm.md` — metrics, tension curve, beat map, flow scores, dashboard

**Bible updates:**
- `bible/characters.md` — appearances, recent history, arc progression, new characters
- `bible/locations.md` — new locations/sub-locations, key events
- `bible/objects.md` — new/updated objects
- `bible/themes.md` — Progression by Chapter row, new thematic symbols

**Project tracking:**
- `project-status.yaml` — chapter entry added
- Chapter frontmatter set to `status: v1-complete`

## Status Storage

Audit status is tracked in:
- **Audit file:** `tracking/audit-chapter-{N}.md` (detailed findings)
- **Chapter frontmatter:** `stepsCompleted` array tracks which steps are done
- **No separate `auditChain` block** in chapter frontmatter — the stepsCompleted array is sufficient

## Completion Output

```
Chapter {N} — "{title}" — v1-complete

Files created:
- tracking/audit-chapter-{N}.md
- tracking/chapter-{N}-themes.md

Files updated:
- tracking/themes.md, emotions.md, rhythm.md
- bible/characters.md, locations.md, objects.md, themes.md
- project-status.yaml

Chapter Statistics:
- Words: {count}
- Mode: {PRESSURE|TEXTURE}
- Flow: {score}/10
- Status: v1-complete
```
