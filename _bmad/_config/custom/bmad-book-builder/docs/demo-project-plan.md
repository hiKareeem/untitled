# BBB Demo Project Plan

**Purpose:** Create a complete sample project that allows new users to explore BBB's capabilities without investing time in their own content first.

---

## Overview

The demo project is a mini-novel called **"The Last Lighthouse"** — a 3-chapter mystery that showcases all BBB features while being short enough to explore in one session.

**Genre:** Mystery / Literary Fiction
**Length:** 3 chapters (~10,000 words total)
**Theme:** Isolation, duty, and the weight of secrets

---

## Story Premise

**Logline:** An aging lighthouse keeper discovers that the automated replacement system about to make him obsolete was designed by the son he abandoned thirty years ago.

**Why this story?**
- Simple enough to understand immediately
- Rich enough to demonstrate character contradictions
- Contains mystery elements (good for showing continuity tracking)
- Emotional depth (good for showing thematic tracking)
- Specific setting (good for showing research/fact verification)

---

## Demo Project Structure

```
_bmad-output/bbb-demo-project/
├── README-DEMO.md                    # Instructions for the user
├── chapter-plan-lighthouse.md        # Complete 3-chapter plan
├── chapters/
│   ├── chapter-01-the-letter.md      # Written (complete)
│   ├── chapter-02-the-arrival.md     # Written (complete)
│   └── chapter-03-the-choice.md      # EMPTY (exercise for user)
├── characters/
│   ├── character-henri.md            # Protagonist (complete)
│   ├── character-lucas.md            # Antagonist/Son (complete)
│   └── character-margot.md           # Supporting (complete)
├── bible/
│   ├── living-bible-lighthouse.md    # Pre-filled with CH.1-2 data
│   ├── chronology.md
│   ├── locations.md
│   ├── objects.md
│   └── themes.md
├── style-profile-demo.yaml           # Sample author style
├── research/
│   └── lighthouse-technology.md      # Research dossier
└── analysis/
    ├── theme-analysis.md             # Thematic progression CH.1-2
    └── rhythm-analysis.md            # Pacing analysis CH.1-2
```

---

## Characters

### Henri Lefebvre (Protagonist)

**Age:** 67
**Role:** Lighthouse keeper for 40 years

**5 Contradictions:**
1. **Duty vs Freedom** — Devoted to the lighthouse but dreams of leaving
2. **Pride vs Shame** — Proud of his work but ashamed of abandoning his family
3. **Isolation vs Connection** — Chose solitude but yearns for his son
4. **Tradition vs Progress** — Distrusts automation but understands its necessity
5. **Forgiveness vs Grudge** — Wants reconciliation but can't forgive himself

**Voice:** Sparse, observational, nautical metaphors

---

### Lucas Lefebvre (Antagonist/Son)

**Age:** 35
**Role:** Engineer who designed the automated lighthouse system

**Arc:** From cold professionalism to understanding his father's sacrifice

---

### Margot Chen (Supporting)

**Age:** 42
**Role:** Coast Guard liaison, Henri's only regular human contact

**Function:** Catalyst who reveals Lucas's identity to Henri

---

## Chapter Plan

### Chapter 1: "The Letter" (3,200 words)

**Beat:** Opening Image + Setup
**POV:** Henri

**Summary:** Henri receives official notice that his lighthouse will be automated in 30 days. He must train the new system. He reflects on 40 years of service and the family he left behind.

**Key scenes:**
1. Henri reads the letter at dawn
2. Flashback: The day he chose the lighthouse over his wife and infant son
3. Margot delivers supplies, mentions the engineer's name: "Lucas Lefebvre"
4. Henri realizes it's his son

**Ends with:** Henri staring at the letter, the name "Lucas" circled

---

### Chapter 2: "The Arrival" (3,500 words)

**Beat:** Catalyst + Debate
**POV:** Henri

**Summary:** Lucas arrives to install the automated system. Father and son interact without acknowledging their relationship. Tension builds as Henri watches Lucas work.

**Key scenes:**
1. Lucas arrives by boat, professional and cold
2. Henri gives the "tour" — 40 years of memories Lucas doesn't share
3. Lucas finds an old photo of himself as a baby (hidden in the lighthouse)
4. Confrontation: "Did you ever think about coming back?"

**Ends with:** Lucas leaves for the night. Henri alone with the automated system blinking to life.

---

### Chapter 3: "The Choice" (3,300 words) — USER EXERCISE

**Beat:** Dark Night of the Soul + Resolution
**POV:** Henri

**Summary:** A storm threatens. The automated system fails. Henri and Lucas must work together to keep the light burning. Through crisis, they find understanding.

**Key scenes:**
1. Storm approaches, automated system malfunctions
2. Henri and Lucas forced to cooperate
3. Conversation during the storm — truths revealed
4. Dawn: The light held. Lucas offers Henri a job consulting on the project.

**Ends with:** Henri watching Lucas's boat leave, a letter in his hand (Lucas's contact info). He smiles.

---

## Exercise Instructions (README-DEMO.md)

```markdown
# BBB Demo Project — Your Turn!

Welcome to the BMad Book Builder demo project!

You've inherited a story in progress. Chapters 1 and 2 are written.
Your mission: **Write Chapter 3 using BBB.**

## What's Already Here

- ✅ Chapter plan (all 3 chapters outlined)
- ✅ Character dossiers (Henri, Lucas, Margot)
- ✅ Style profile (demo author voice)
- ✅ Living Bible (updated through Chapter 2)
- ✅ Research dossier (lighthouse technology)

## Your Exercise

1. **Review the materials:**
   - Read `chapter-plan-lighthouse.md` to understand the story
   - Check `characters/character-henri.md` to know the protagonist
   - Glance at `bible/living-bible-lighthouse.md` for continuity

2. **Launch Chapter Writer:**
   ```
   bmad agent chapter-writer
   CW
   ```

3. **Select Chapter 3** and let BBB generate the draft

4. **Run the audit chain:**
   - Review → Bible-Update → Theme-Tracker → Rhythm-Analysis

5. **Export your bible:**
   ```
   bmad agent character-keeper
   EB
   ```

## What You'll Learn

- How BBB uses the plan, characters, and style to generate authentic prose
- How the audit chain catches issues and updates tracking
- How Export-Bible consolidates everything into one document

## Time Required

~30-45 minutes for the full exercise

---

**Tip:** After completing this exercise, you'll be ready to start your own project with `bmad agent story-architect` → `FD` (Foundation)!
```

---

## Implementation Tasks

### Phase 1: Core Files (2 hours)

- [ ] Write `chapter-plan-lighthouse.md` (detailed 3-chapter plan)
- [ ] Write `character-henri.md` (full dossier with 5 contradictions)
- [ ] Write `character-lucas.md` (antagonist dossier)
- [ ] Write `character-margot.md` (supporting dossier)
- [ ] Create `style-profile-demo.yaml` (sample metrics)

### Phase 2: Content (3 hours)

- [ ] Write Chapter 1: "The Letter" (~3,200 words)
- [ ] Write Chapter 2: "The Arrival" (~3,500 words)
- [ ] Create empty Chapter 3 template with brief and objectives

### Phase 3: Bible & Tracking (1 hour)

- [ ] Create `living-bible-lighthouse.md` with CH.1-2 data
- [ ] Create `chronology.md`, `locations.md`, `objects.md`, `themes.md`
- [ ] Create `theme-analysis.md` showing progression
- [ ] Create `rhythm-analysis.md` with tension curves

### Phase 4: Research & Polish (1 hour)

- [ ] Create `lighthouse-technology.md` research dossier
- [ ] Write `README-DEMO.md` with clear instructions
- [ ] Test the exercise flow end-to-end

---

## Success Criteria

1. User can complete the exercise in under 45 minutes
2. Generated Chapter 3 is coherent with existing chapters
3. All BBB features are demonstrated naturally
4. User understands the workflow without reading external docs

---

## Future Enhancements

- [ ] Add a "speedrun" mode (15-minute quick demo)
- [ ] Create additional demo projects (romance, thriller, fantasy)
- [ ] Add video walkthrough companion
- [ ] Translate demo to French for francophone users

---

*Created: 2026-01-25*
*Status: PLAN — Ready for implementation*
