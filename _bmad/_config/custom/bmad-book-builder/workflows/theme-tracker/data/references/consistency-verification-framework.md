# Consistency Verification Framework

Reference guide for verifying thematic coherence across chapters and identifying issues.

## Overview

Consistency verification ensures that the thematic tracking remains coherent across all chapters, flagging issues while providing actionable insights for future development.

## Verification Scope

### Three Layers of Verification

**1. Theme Continuity**
- Logical progression across chapters
- Alignment with phase plans
- Strategic vs problematic absences

**2. Character Emotional Arcs**
- Chapter-to-chapter emotional consistency
- Growth and development patterns
- Unexplained shifts or stagnation

**3. Character-Theme Connections**
- Verified connections in themes.md
- Evidence in chapter analyses
- Missing or incorrect connections

---

## Theme Continuity Verification

### Progression Logic Check

**For each theme in themes.md:**

**Examine Per-Chapter Progression table:**

**Valid progression patterns:**

1. **Linear Development:**
   - Each chapter builds on previous
   - Clear forward movement
   - No contradictions
   - Example: Trust grows gradually through challenges

2. **Spiral Development:**
   - Revisits similar territory with depth
   - Circular but forward-moving
   - Each return adds complexity
   - Example: Identity questioned repeatedly with new layers each time

3. **Interrupted Presence:**
   - Theme appears, disappears, reappears
   - Strategic absences create tension
   - Purposeful gaps
   - Example: Freedom theme absent during imprisonment, reintroduced upon escape

4. **Crisis Build:**
   - Theme intensifies toward breaking point
   - Escalating tension
   - Approaching resolution
   - Example: Sacrifice theme builds to ultimate choice

**Invalid progression patterns:**

1. **Inconsistent Treatment:**
   - Theme contradicts itself
   - Character positions shift without reason
   - Thematic logic violated
   - Example: Trust established then ignored without explanation

2. **Stalled Progression:**
   - Theme repeats without development
   - No forward movement across multiple chapters
   - Spinning wheels
   - Example: Character questions identity in chapters 3, 5, 7, 9 without any change

3. **Abandoned Thread:**
   - Theme active then disappears
   - No resolution reached
   - Thread dropped without explanation
   - Example: Redemption arc introduced then never mentioned again

### Phase Alignment Check

**For each theme:**

**Compare:**
- Progression by Chapter Phase (plan)
- Per-Chapter Progression table (actual)

**Check for alignment:**
- Does actual follow planned phase?
- Are phase transitions appropriately marked?
- Is timing consistent with story structure?

**Flag if:**
- Phase plan says "intensify" but actual shows "static"
- Phase plan says "resolve" but actual shows "introduce"
- Significant deviation without clear reason

### Gap Analysis

**For each theme:**

**Identify gaps in Per-Chapter Progression:**
- Chapters where theme should appear but doesn't
- Length of absence (1 chapter vs 5 chapters)
- Context during absence (was attention needed elsewhere?)

**Classify gaps:**

**Strategic Absence (OK):**
- Purposeful gap creates tension
- Other themes had priority
- Sets up later return
- Example: Love theme absent during war sequence, returns in aftermath

**Problematic Absence (Flag):**
- Theme should be present given context
- No reason for absence
- Breaks established pattern
- Example: Trust central to plot but absent for 8 chapters

---

## Character Emotional Arc Verification

### Emotional Continuity Check

**For each character in emotions.md:**

**Examine Per-Chapter Emotional Beats table:**

**Verify:**
- Chapter-to-chapter transitions make sense
- Emotional states flow logically
- No unexplained jumps

**Valid transitions:**
- Gradual evolution across chapters
- Triggered changes (event causes emotion shift)
- Recovery from extreme states
- Example: Anger → Processing → Understanding

**Invalid transitions:**
- Sudden unexplained changes
- Contradictory states
- Jumps without catalyst
- Example: Deep love → Sudden hate with no event

### Growth Pattern Analysis

**For each character:**

**Check Emotional Arc Summary:**
- Does it match actual chapter-by-chapter progression?
- Are claimed developments supported by beats?
- Is trajectory coherent?

**Look for:**

**Healthy Growth:**
- Character evolves over time
- Emotional complexity increases
- Trajectory follows arc
- Example: Fear → Caution → Trust

**Stagnation:**
- Character shows no change over multiple chapters
- Same emotional beats repeated
- No development
- Example: Anger in chapters 1, 3, 5, 7, 9 without variation

**Regression:**
- Character moves backward without explanation
- Development undone
- Previous growth ignored
- Example: Trust achieved then suddenly lost without cause

### Emotional Range Check

**For each character:**

**Assess emotional variety:**
- Range of emotions shown
- Appropriateness to context
- Character consistency

**Flag if:**
- Character only shows one emotion (flat)
- Emotions don't match situations (inappropriate)
- Character acts out of established nature (inconsistent)

---

## Character-Theme Connection Verification

### Connection Evidence Check

**For each connection claimed in themes.md:**

**Verify in chapter analyses:**
- Does chapter-{XX}-themes.md show character engaging with theme?
- Is there evidence of character position on theme?
- Does character's emotional arc connect to theme?

**Valid connection:**
- Multiple chapters show engagement
- Emotional beats relate to theme
- Character position documented
- Example: Sarah's grief connects to Isolation vs Connection theme

**Invalid connection:**
- Claimed but not evidenced in chapters
- Character listed but no thematic engagement shown
- Tenuous or forced connection
- Example: Marc connected to Redemption theme without any redemptive arc

### Missing Connection Detection

**Check chapter analyses for unlisted connections:**

**Look for:**
- Characters engaging with themes not in themes.md
- Thematic development attributed to unlisted characters
- Emotional arcs clearly tied to themes but not documented

**Flag if:**
- Character consistently engages with theme but not listed
- Connection should be documented but isn't

---

## Red Flag Classification

### Severity Levels

#### 🔴 Critical Issues (Problèmes à traiter)

**Definition:** Issues that likely need addressing

**Examples:**
- Thème abandonné: Active theme disappears without resolution
- Position personnage inchangée: Character static for 5+ chapters
- Incohérence avec chapitres précédents: Contradictions in tracking
- Arc incohérent: Character behavior violates established arc
- Progression contradicts phase plan: Major deviation without reason

**Action required:** Address or explain

#### 🟡 Attention Items (Points d'attention)

**Definition:** Items that might need attention but aren't critical

**Examples:**
- Thème mentionné mais pas exploré: Theme referenced but not developed
- Character shows no change in 3-4 chapters: Possible stagnation
- Theme hasn't appeared in 3 chapters: May be intentional absence
- Character engages with theme but not listed in connections: Documentation issue

**Action recommended:** Monitor or review

#### ✅ Successful Verification

**Definition:** No issues detected

**Criteria:**
- Progression logical and coherent
- Character arcs consistent
- Connections verified
- No contradictions or gaps

---

## Verification Checklist

### Theme Continuity

For each theme:
- [ ] Progression follows logical pattern
- [ ] Phase alignment verified
- [ ] Gaps classified (strategic vs problematic)
- [ ] No contradictions detected
- [ ] No abandoned threads

### Character Arcs

For each character:
- [ ] Chapter-to-chapter transitions logical
- [ ] Growth pattern appropriate
- [ ] No unexplained emotional jumps
- [ ] Emotional range adequate
- [ ] No stagnation issues

### Connections

For each claimed connection:
- [ ] Evidence found in chapter analyses
- [ ] Character engagement documented
- [ ] Thematic link clear
- [ ] No missing connections detected

---

## Reporting Format

### Verification Report Structure

```markdown
## 🔴 Problèmes à traiter

### [Issue Category]

**[Theme/Character]:** [Specific issue]
- **Problem:** [Description of what's wrong]
- **Impact:** [Why this matters]
- **Suggested action:** [What to do about it]
- **Chapters affected:** [Where it appears]

[Additional critical issues]

Or: "Aucun problème critique détecté"

---

## 🟡 Points d'attention

### [Issue Category]

**[Theme/Character]:** [Specific item]
- **Observation:** [What was noticed]
- **Why it might matter:** [Potential concern]
- **Recommendation:** [What to watch for]
- **Chapters affected:** [Where it appears]

[Additional attention items]

Or: "Aucun point d'attention particulier"

---

## ✅ Vérifications réussies

- **Continuité thématique:** [OK / Number of themes with issues]
- **Arcs émotionnels:** [OK / Number of characters with issues]
- **Connexions personnage-thème:** [OK / Number of connection issues]
```

---

## Recommendations Generation

### Theme Development Recommendations

**Analyse:**
- Which themes are due for progression based on phase plan?
- Which themes haven't had focus recently?
- Which themes are approaching crisis points?

**Generate:**

**1. Thèmes à développer:**
- [Theme]: [Why it needs development, what phase suggests]
- [Theme]: [What's at stake if not developed]

### Character Monitoring Recommendations

**Analyse:**
- Which characters show stagnation?
- Which characters need resolution?
- Which characters are approaching arc climax?

**Generate:**

**2. Personnages à surveiller:**
- [Character]: [What arc movement is needed, what's at stake]

### Open Questions Recommendations

**Analyse:**
- What questions has the narrative raised?
- What setups need payoffs?
- What tensions need resolution?

**Generate:**

**3. Questions ouvertes:**
- [Question]: [Why it matters, what chapters it connects to]

---

## Common Verification Patterns

### Example 1: Critical Issue Detection

**Issue:** Thème abandonné

**Theme:** Sacrifice

**Problem:**
- Theme strongly present in chapters 1-5
- Character arc established around willing to sacrifice
- Theme disappears completely from chapters 6-12
- No resolution reached

**Impact:**
- Major character arc left hanging
- Reader question unanswered
- Thematic promise unfulfilled

**Suggested action:**
- Reintroduce theme in upcoming chapters
- Provide resolution or explanation
- OR explicitly show character moving away from sacrifice

### Example 2: Attention Item Detection

**Issue:** Character stagnation

**Character:** Julie

**Observation:**
- Emotional state: Hopeful/cautious
- Same state across chapters 4, 6, 8, 10
- No development despite significant events
- Other characters showing growth

**Why it might matter:**
- Julie is POV character
- Stasis contrasts with other development
- May indicate missed opportunities

**Recommendation:**
- Consider if this is intentional (Julie as observer/anchor)
- OR create event that challenges her stasis
- Monitor if this serves narrative purpose

### Example 3: Successful Verification

**Theme:** Trust vs Mistrust

**Verification:**
- Progression: Linear, logical
- Chapters 1-3: Mistrust established
- Chapters 4-6: First openings
- Chapters 7-9: Crisis and choice
- Chapters 10-12: New dynamic
- Phase alignment: Perfect
- No gaps, no contradictions

**Character:** Marc

**Verification:**
- Emotional arc: Méfiance → Hésitation → Choix → Vulnérabilité
- Each transition triggered by events
- Growth consistent
- No unexplained jumps

**Connection:**
- Marc connected to Trust theme
- Evidence in chapters 2, 5, 7, 9, 11
- Emotional beats align with theme
- Position progression documented

**Result:** ✅ All verifications passed

---

## Health Assessment

### Overall Thematic Health Rating

**Excellente:**
- All themes progressing logically
- All characters showing growth
- No critical issues
- No attention items

**Bonne:**
- Themes progressing with minor gaps
- Characters developing well
- No critical issues
- 1-2 attention items

**À surveiller:**
- Some themes showing stalled progression
- One or two characters stagnating
- 1-2 critical issues
- Multiple attention items

**Préoccupante:**
- Multiple themes with progression problems
- Several characters stagnant
- 3+ critical issues
- Many attention items

### Rating Criteria

**For each assessment:**
- Number of critical issues
- Number of attention items
- Severity of issues
- Impact on narrative coherence
- Reader experience implications
