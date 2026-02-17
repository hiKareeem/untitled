# Chapter 13 "The Pattern" — Handoff Prompt

## Purpose

This document is a handoff prompt for a frontier model to rewrite Chapter 13 from scratch. Two previous drafts were produced and rejected. This prompt documents all authorial decisions, continuity requirements, source file locations, and the specific failures of the previous drafts so they are not repeated.

## Workflow

Use the chapter-write workflow defined in `_bmad/bmad-book-builder/workflows/chapter-write/workflow.md`. Chapter 13 is at **Step 03 (Draft)** — the brief is approved, the output file exists. The model should:

1. Read all required inputs (listed below)
2. Write the chapter draft from scratch (~4000-5000 words)
3. Proceed through Steps 04-06 (self-review, audit, bible update) per workflow

## Required Inputs

All paths are relative to `d:\Writing\_bmad-output\bbb-project\` unless noted.

| Input | Path |
|-------|------|
| Chapter plan | `chapter-plan-untitled.md` (lines ~743-779 for Ch 13 details, lines ~1260 for rhetoric ref, lines ~1351 for epigraph) |
| Style profile (quick-ref) | `d:\Writing\_bmad\_memory\style-coach-sidecar\style-profile.md` |
| Anti-slop checklist | `d:\Writing\_bmad\bmad-book-builder\workflows\chapter-write\data\anti-slop-checklist.md` |
| Character dossier | `characters/mirelle-dubois-dossier.md` |
| Bible: characters | `bible/characters.md` |
| Bible: locations | `bible/locations.md` |
| Bible: objects | `bible/objects.md` |
| Bible: themes | `bible/themes.md` |
| Lexicon | `lexicon.md` |
| Worldbuilding reference | `worldbuilding-reference-untitled.md` |
| **Chapter 2** (Mirelle #1) | `chapters/chapter-2.md` — her first appearance, establishes: borrowed RCI sensor, Junction 7, Gauthier's refusal, chalk-name wall, Sump beat, lodgings in Sump Sector 3 |
| **Chapter 9** (Mirelle #2) | `chapters/chapter-9.md` — her second appearance, establishes: dead-hand protocol with Talia, 16 disappearances/5 sectors, nitro-ear onset, junction reclassification intel, Talia Ravid on-page, repair shop physical details, passphrase mechanics, room layout, RCI sensor location |
| Chapter 12 (context) | `chapters/chapter-12.md` — Aurielle sees the same infrastructure data from the other side (reader-ahead beat) |

## Chapter 13 Brief (Approved)

**Title:** "The Pattern"
**POV:** Mirelle Dubois (3rd appearance)
**Location:** Neo-Shanghai — lower Mid-Levels → Resonance District (Talia Ravid's Black Babel node RD-14) → transit box
**Phase:** 2 (Disruption — "Fault Lines")
**Thread:** B (Information/Truth)
**Word target:** 4000-5000

**Epigraph:**
> "The geographic distribution of the sample set is not random. I have overlaid it with six demographic maps and four infrastructure schematics. The clustering cannot be explained by any variable in the public dataset."
> — Dr. Maren Solberg, *On the Statistical Correlation Between Nitro Throughput Density and Void Breach Frequency*, 2170 (suppressed)

**Rhetoric reference:** Wire internal dispatch (encrypted) — "Three Sump-beat journalists terminated this quarter. Two sources stopped responding."

**Key Events (from chapter plan):**
- Mirelle meets Talia Ravid at Talia's node in the Resonance District
- Dead-drop exchange: trades Sump demographics (18 months of population movement data) for partial Arctic-7 document
- Talia warns: "You're building a target on your chest"
- Black Babel rules restated (never edits data, compartmentalization, transactional trust)
- Mirelle reads Arctic-7 document and assembles the pattern: infrastructure + demographics + disappearances = architecture, not negligence

**Seeds planted for future chapters:**
- Ch 17: First information bridge with Zeyad (NOT yet established in Ch 13 — no Zeyad reference)
- Ch 21: "Matched Districts" — Mirelle's next chapter
- Ch 34: Dead-hand deposit (final cache)
- Ch 40: Mirelle absorbed mid-sentence

## Authorial Decisions (Confirmed)

These are decisions made by the author during the review process. They are non-negotiable.

1. **Arctic-7 document authorship:** Unnamed atmospheric research lead. NOT Solberg. The attribution was stripped before the pages entered the Black Babel network. Solberg appears ONLY in the epigraph attribution — she is not mentioned in the prose.

2. **Solberg in prose:** Keep her out of the prose entirely except for institutional references (the epigraph). Do not connect her to Arctic-7 in Mirelle's thoughts or dialogue.

3. **Transit terminology:** Whatever makes sense for the infrastructure and time period. Narratively irrelevant — don't overthink it.

4. **"brightline" capitalization:** Lowercase in prose. It's an aurora borealis phenomenon, not a proper noun. The capitalization in the bible file is because it's a section header.

5. **Mirelle's realization scope:** The pattern she discovers is the *architecture of designed sacrifice* — infrastructure density correlates with disappearances, and the reclassifications seal the evidence. She does NOT realize the void is "responsive" or "sentient" or "following" anything. Her POV is journalistic: she sees institutional design, not metaphysical properties.

6. **Arctic-7 document content:** Infrastructure density maps of the *station* showing nitro flow and void breach response as co-originating from the same locations. Mirelle then abstracts this to conduit junctions/disappearances in Neo-Shanghai. The document is maps and data overlays, not a narrative report.

7. **No Zeyad connection:** The first information bridge between Mirelle and Zeyad is Ch 17. Ch 13 must not reference Zeyad, any encrypted channel to him, or any mutual contact.

8. **No Sofia Reyes reference:** Mirelle does not know Sofia exists. Any reference to Sofia or parallel investigation is a POV violation.

9. **No meta-references:** No "Chapter 2" or similar in character thoughts. No referring to previous chapters by number.

## Continuity Requirements (from Ch 9)

These physical details were established in Chapter 9 and MUST be consistent in Chapter 13. However — and this is critical — **they must not be copy-pasted or closely paraphrased from Chapter 9.** The reader has already read Chapter 9. Chapter 13 should evoke the same space through *different details, different angles, different sensory emphasis.* A return visit to a familiar place should feel like a return visit, not a reprint.

### What Ch 9 established:
- **Shop front:** Counter, woman behind it, refurbished frame components on backlit shelf, sliding door behind the shelf (Ch 9 L129-133)
- **Passphrase:** Six words in Cantonese, rotated monthly via dead-letter system requiring physical presence (Ch 9 L131)
- **Back room:** Larger than front, cool, well-lit (not conduit-orange), insulated, storage racks, encrypted relay stations, three displays, hum muted (Ch 9 L137-138)
- **Talia's position:** Workstation in center of room, back to door, doesn't turn around when Mirelle enters (Ch 9 L139)
- **Talia's appearance:** Ghanaian-Israeli, close-cropped hair, military-grade optical hardware (luminescent ring behind irises), plain gray coverall, no jewelry (Ch 9 L145)
- **Talia's workstation:** Mug of tea, data interface (Ch 9 L145)
- **Talia's voice:** Even, unhurried, tracks time "the way other people tracked weather" (Ch 9 L141)
- **RCI sensor:** In boot, under insole (Ch 9 L103)
- **Mirelle's previous lodgings:** Room in Sump Sector 3, six blocks from the brightline, mechanical lock, no mesh connection (Ch 9 L105) — this is a DIFFERENT location from Ch 13's transit box

### How Ch 13 should handle the return visit:
- The reader already knows the shop front, the passphrase mechanic, the room layout, and Talia's appearance. **Do not re-describe these in detail.** Brief, glancing references that confirm we're in the same place. Focus new sensory detail on what has *changed* or what Mirelle notices *differently* this time.
- Talia's rules recitation should feel like repetition to Mirelle (she's heard them before) but carry new weight given the stakes.
- The "four minutes early" / "five minutes early" beat from Ch 9 should NOT be repeated. We've established she shows up early. Move on.

## Disappearance Count Progression

- Ch 2: Mirelle investigating individual disappearance (Dao Suen) near Junction 7. Hints at a second.
- Ch 9: 16 disappearances across 5 sectors. 7 junctions reclassified to restricted-corporate maintenance.
- Ch 13: 18 disappearances (2 new since Ch 9, both Sector 8, both near trunk-line junctions). 7 reclassified junctions (same count as Ch 9).

## Dead-Hand Protocol

- Established Ch 9: 72-hour rolling check-in window. Mirelle pings an address; the timer resets. If she misses two consecutive windows, the sealed data package auto-distributes through Black Babel's network.
- Ch 13: Timer should be partway through a window (she pinged yesterday). She should add the Arctic-7 analysis to the dead-hand deposit by chapter's end.

## Nitro-Ear

- Onset: Ch 9, three weeks of a high-pitched tone in right ear
- Ch 13: Now five weeks. Still present. Mirelle treats it as tinnitus but the reader should sense it may be more.

## Communication Devices

- **Frames** are nitro-coupled mobility platforms (exosuits/rigs), NOT communication devices
- **Burner comms** are battery-powered legacy communication devices (no mesh connection, disposable)
- Mirelle uses burner comms for notes and communication
- She has an isolated terminal (salvage components, no corporate firmware) for data analysis

## Style Profile Key Points

- **Signature technique:** Negation-before-assertion ("Not louder. Not quieter. *Thinner.*") — target 2-4 instances for Mirelle POV
- **Sensory hierarchy:** Sound/vibration > Temperature > Tactile > Visual > Taste
- **Emotion through physical sensation**, never named directly
- **Bimodal paragraphs:** Dense atmospheric blocks alternating with single-line punches
- **Dialogue:** Minimalist tags ("said"), terse/technical, narration-heavy ratio
- **Mirelle's metaphor domain:** Journalism/investigation (exposure, sources, lenses, angles, deadline, redaction)
- **Anti-slop watchlist:** "something shifted/changed", telling emotions directly, expository dialogue, quippy dialogue

## What Failed in Previous Drafts

### Draft v1 failures (critical errors):
- Used "burner frame" for communication device
- RCI sensor on ankle instead of under insole
- Shop front described wrong (empty counter, curtain instead of sliding door)
- Passphrase was four syllables instead of six words
- Talia wore utility jacket instead of gray coverall
- Room had workbench along wall instead of workstation in center
- Solberg fabricated as Arctic-7 field researcher
- Sofia Reyes referenced (POV violation)
- Fabricated "Correlation 0.91" figure
- Mirelle realized void was "responsive" (too much, too soon, wrong POV)
- Meta-reference to "Chapter 2"
- Zeyad connection established prematurely
- Talia spoke French (no established connection)
- Arctic-7 timeline wrong (5 years instead of ~1 year)
- Talia didn't know about disappearances (she already knew from Ch 9)

### Draft v2 failures (the reason for this handoff):
- **Copy-pasted scene descriptions from Chapter 9.** The back room description (Ch 13 L116) was a lightly reworded version of Ch 9 L137-138. Talia's appearance description (Ch 13 L124) was copy-pasted from Ch 9 L145 with minor word changes. The "four minutes early / five minutes early" beat was repeated verbatim from Ch 9.
- **Lazy scene-setting.** Instead of writing a *return visit* — with the familiarity, the subtle differences, the journalist's eye noticing what has changed — the draft simply re-described the same space in nearly the same words. This is not how experienced fiction handles a character's second visit to a location.
- The transit box description (L88) was confirmed clean — this is a new location not previously described.
- The core *structure* of the chapter (Wire dispatch → transit to Resonance District → Talia exchange → return to transit box → analysis of Arctic-7 maps → pattern assembly → dead-hand deposit) is sound. The failures were in execution, not architecture.

## Summary

Write Chapter 13 from scratch. The brief, the corrections list, and the authorial decisions above are all confirmed. The chapter's architecture (four movements: transit, exchange, analysis, realization) is approved. The failures to avoid are: (1) copy-pasting or closely paraphrasing descriptions from Chapter 9, (2) re-describing known details at length instead of writing a return visit, (3) any of the factual errors listed above. Read Chapter 9 carefully, then write Chapter 13 as a chapter that *follows* Chapter 9 — not one that *repeats* it.
