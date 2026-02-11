---
title: 'Reality Check — Untitled (Book 1)'
date: 2026-02-11
project: 'Untitled'
author: 'Kareem'
verifier: 'Documentaliste (Claude)'
scope: 'all'
scopeType: 'all'
targetChapters: ['prologue', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
verificationStatus: 'complete'
stepsCompleted: ['step-01-select-scope', 'step-02-extract-claims', 'step-03-check-references', 'step-04-web-verification', 'step-05-identify-issues', 'step-06-provide-corrections']
lastStep: 'step-06-provide-corrections'
claimsExtracted: 47
highPriorityClaims: 8
mediumPriorityClaims: 18
lowPriorityClaims: 21
issuesIdentified: 8
correctionsProvided: 8
issuesResolved: 6
issuesDismissed: 2
resolutionStatus: 'complete'
---

# Reality Check: Untitled (Book 1)

**Generated:** February 11, 2026
**Scope:** All chapters (Prologue + Ch 1-10)
**Verifier:** Documentaliste

---

## Claims Summary

**Total Claims Extracted:** 47

| Category | High | Medium | Low | Total |
|----------|------|--------|-----|-------|
| Technical Accuracy | 4 | 8 | 5 | 17 |
| Factual Accuracy | 2 | 8 | 8 | 18 |
| Logical Consistency | 2 | 5 | 5 | 12 |
| **TOTAL** | **8** | **21** | **18** | **47** |

---

## Issues Identified (8 Total)

**Resolution Status:** 6 resolved, 2 dismissed (not issues)
- Issue 1 (Mirelle camera): DISMISSED — intentional analog tradecraft
- Issue 2 (Thermal round): RESOLVED — changed to "thermal-kinetic round" (Ch 1)
- Issue 3 (UTC timezone): RESOLVED — changed to 11:30 UTC (Ch 10, no DST in PCC)
- Issue 4 (SCADA refresh): RESOLVED — changed to 2-second refresh (Ch 4)
- Issue 5 (EM spectrum): RESOLVED — changed to "frequency spectrum" (Ch 5)
- Issue 6 (Nosebleed): RESOLVED — neoplastic turbinate engorgement (Ch 3)
- Issue 7 (3Hz resonance): RESOLVED — changed to sternum (Ch 4)
- Issue 8 (Standing corpse): DISMISSED — dramatic license, effective
- Issue 9 (Cantonese): DISMISSED — intentional worldbuilding

### CRITICAL (3) — Breaks credibility for informed readers

#### Issue 1: UTC Timezone Contradiction (Ch 10)

- **Claim:** The scream occurs at "21:30 UTC" during what is described as an evening/night stream in the Bay Area.
- **Problem:** 21:30 UTC = 1:30 PM PST (or 2:30 PM PDT). The chapter describes "sundown," "tonight," and a late-night atmosphere. Hour 9 of a 10-hour stream ending at night would place the scream around 8-9 PM local time.
- **Severity:** CRITICAL — Any reader who converts timezones will catch this.
- **Correction:** Change "21:30 UTC" to approximately **04:30 UTC** (8:30 PM PST) or **05:30 UTC** (9:30 PM PDT), depending on whether Daylight Saving Time is observed in 2175.
- **Files affected:** chapter-10.md, and any cross-references in tracking files.

#### Issue 2: SCADA Monitor Refresh Rate (Ch 4)

- **Claim:** "The monitors updated every fifteen seconds." A 4-point RCI jump in 15 seconds is treated as alarming.
- **Problem:** For critical high-pressure infrastructure in 2175, a 15-second refresh rate is dangerously slow. Modern (2025) SCADA systems update in milliseconds to 1-second intervals. A 15-second blind spot in a flow system would allow catastrophic failure before the operator saw anything.
- **Severity:** CRITICAL — Engineers and anyone familiar with industrial monitoring will notice.
- **Correction Options:**
  - (A) Change "fifteen seconds" to "two seconds" or "one second" — the drama still works with a 4-point jump in 2 seconds.
  - (B) Keep 15 seconds but explain it: the Deep Sump uses legacy/degraded equipment that hasn't been upgraded (consistent with "maintenance deferred 14 months" from Ch 7). Add a line like: "The monitors were legacy — fifteen-second cycles, because the Deep Sump hadn't warranted a systems upgrade in twenty years."
  - **Recommended:** Option B — it reinforces the systemic neglect theme.

#### Issue 3: Thermal Round vs. Blood Spatter (Ch 1)

- **Claim:** A "thermal round" destroys Eduardo's head ("smoking ruin") but also drenches Aurielle in "thick, dark crimson."
- **Problem:** Thermal weapons cauterize tissue on contact, sealing blood vessels and reducing immediate hemorrhage. A "smoking ruin" implies vaporization/charring. Massive arterial spray ("drenched") contradicts thermal physics — it implies explosive kinetic force (hydrostatic shock), not heat.
- **Severity:** CRITICAL — Forensic-aware readers (and there are many in thriller readership) will flag this.
- **Correction Options:**
  - (A) Change to a kinetic/explosive round — explains both the destruction and the spray.
  - (B) Keep "thermal" but add a kinetic component: "thermal-kinetic round" or "thermal round with fragmentation jacket" — the heat destroys the target, the kinetic energy produces the spray.
  - (C) Reduce the blood: change "drenched" to "spattered" — thermal rounds produce less volume but can still expel some matter.
  - **Recommended:** Option B — maintains the specific "thermal round" worldbuilding while explaining the physics.

### MAJOR (3) — Noticeable to informed readers

#### Issue 4: EM Spectrum vs. Acoustic Confusion (Ch 5)

- **Claim:** Sofia's 0.7 Hz pulse is described as being in the "deep basement of the electromagnetic spectrum" alongside "geological processes."
- **Problem:** Geological processes (seismic activity, tidal loading) produce **mechanical** waves (vibration/pressure), not **electromagnetic** waves. If Sofia is measuring vibrations in the sub-strata, this is the acoustic/seismic frequency domain, not EM.
- **Correction:** Change "electromagnetic spectrum" to "frequency spectrum" or "acoustic spectrum." If she IS measuring EM fields, remove references to "tidal loading" and "bedrock" as primary interference sources.

#### Issue 5: Nosebleed Etiology (Ch 3)

- **Claim:** Nephthys's nosebleed is caused by "pressure... on tissue of the brain" rupturing "capillaries behind her sinuses."
- **Problem:** Increased intracranial pressure (ICP) does not typically cause epistaxis (nosebleeds). This is a common Hollywood/fiction trope. Nosebleeds from physiological stress are caused by *hypertension* (blood pressure spike) or *sinus barotrauma*, not "brain pressure."
- **Correction:** Change "the pressure of whatever the chorus was doing to the tissue of her brain" to something like "the blood pressure spike that followed" or "the pressure wave that rattled through her sinus cavities." The nosebleed remains; the mechanism becomes medically sound.

#### Issue 6: 3 Hz Tooth Resonance (Ch 4)

- **Claim:** "Three hertz flat" is felt "first in his molars."
- **Problem:** 3 Hz is infrasound. The resonant frequency of teeth/skull is much higher (1000+ Hz for teeth, 200-400 Hz for skull). At 3 Hz, the body resonance occurs in the chest cavity (4-8 Hz), abdomen, and eyeballs (18-19 Hz). Feeling 3 Hz in the teeth first is physiologically incorrect.
- **Correction:** Change "molars" to "chest" or "sternum" — or change the frequency to something higher (e.g., "two hundred hertz" would resonate in teeth). Alternatively, add "transmitted through the jaw" to imply bone conduction from the floor through the skeleton, which is plausible for any frequency.
- **Recommended:** "registered first in his jaw, transmitted up through the concrete" — bone conduction is frequency-agnostic and avoids the resonance problem.

### MINOR (2) — Background details, low credibility risk

#### Issue 7: Post-Decapitation Body Mechanics (Ch 1)

- **Claim:** Eduardo's body remains "standing... held upright by lectern" after the thermal round removes everything from the nose up.
- **Problem:** Loss of the brainstem causes immediate flaccid paralysis. The body would collapse unless physically braced. Leaning on a lectern *could* briefly support the torso, but the legs would buckle.
- **Assessment:** This is dramatic license and works in the shock of the scene. The text doesn't dwell on it, and the image is powerful. Most readers will accept it.
- **Optional correction:** Add "for a moment" or imply the body slumped almost immediately — "Eduardo was still at the podium. Still standing — for a second that stretched — before the legs gave."

#### Issue 8: Cantonese Access Phrase in Neo-Shanghai (Ch 9)

- **Claim:** A Cantonese phrase is used as an access code in Neo-Shanghai.
- **Problem:** Shanghai's native dialect is Shanghainese (Wu Chinese); the common language is Mandarin. Cantonese is Southern (Hong Kong/Guangdong). Using Cantonese as a code phrase in Shanghai is a specific choice.
- **Assessment:** This could be intentional — marking the Black Babel node as connected to southern trade routes or diaspora networks. If intentional, it's good worldbuilding. If unintentional, it should be Mandarin or Shanghainese.
- **Recommendation:** If intentional, add a brief thought from Mirelle noting the southern dialect choice. If unintentional, change to Mandarin.

---

## Verified Claims (No Issues — Selected Highlights)

| Chapter | Claim | Status | Notes |
|---------|-------|--------|-------|
| Prologue | Barents shelf as resource extraction location | ✅ Accurate | Real hydrocarbon-rich shelf |
| Prologue | Radiative cold of vacuum | ✅ Accurate | Correct thermodynamics |
| Prologue | Pipe resonance ("singing") from high-flow fluid | ✅ Accurate | Flow-induced vibration |
| Ch 1 | Auditory exclusion under stress | ✅ Accurate | Established psychophysiology |
| Ch 1 | Emergency corporate succession without quorum | ✅ Plausible | Delaware law precedent |
| Ch 1 | Copper/burnt hair smell from head trauma | ✅ Accurate | Iron in blood + keratin |
| Ch 3 | Oxbow lake formation analogy | ✅ Accurate | Correct geomorphology |
| Ch 3 | Cluster headache symptom description | ✅ Accurate | Clinical presentation |
| Ch 4 | PID loop / linear decay = artificial | ✅ Accurate | Sound control theory |
| Ch 4 | Joule heating analogy | ✅ Accurate | Correct physics |
| Ch 5 | Recalibration procedures (impedance, firmware) | ✅ Accurate | Standard sensor diagnostics |
| Ch 5 | Natural decay is exponential | ✅ Accurate | Damped harmonic oscillators |
| Ch 6 | Rue du Rhône as luxury street | ✅ Accurate | Geneva landmark |
| Ch 6 | Geneva low-rise zoning | ✅ Accurate | Lake/mountain view preservation |
| Ch 6 | "Contained" contradicts "No action required" | ✅ Sound logic | Zeyad's deduction valid |
| Ch 7 | 21.2°C as comfort temperature | ✅ Accurate | ASHRAE Standard 55 |
| Ch 7 | Sandalwood scent retention in leather | ✅ Accurate | Low-volatility base note |
| Ch 7 | Signal-to-noise ratio / secular trend detection | ✅ Accurate | Standard data science |
| Ch 8 | Chemical staining from textile solvents | ✅ Plausible | Dermal absorption |
| Ch 8 | AR glitching near EMI sources | ✅ Accurate | Magnetometer interference |
| Ch 8 | Occupational tinnitus from LFN exposure | ✅ Accurate | Vibroacoustic disease |
| Ch 9 | Dead-hand protocol as journalist failsafe | ✅ Accurate | Real tradecraft |
| Ch 9 | SSD secure erase methodology | ✅ Accurate | Wear-leveling awareness |
| Ch 9 | Infrasound body resonance | ✅ Accurate | Chest/skull pressure |
| Ch 10 | Bay Area sea-level rise (San Jose submerged) | ✅ Plausible | Climate projection |
| Ch 10 | 40mg milligram scale requirement | ✅ Accurate | Correct precision |
| Ch 10 | Insufflation pharmacokinetics (rapid onset) | ✅ Accurate | Mucosal absorption |

---

## Corrections Summary (Prioritized)

| # | Issue | Chapter | Priority | Recommended Fix |
|---|-------|---------|----------|-----------------|
| 1 | UTC timezone | Ch 10 | CRITICAL | Change 21:30 UTC to ~04:30 or 05:30 UTC |
| 2 | SCADA refresh rate | Ch 4 | CRITICAL | Add legacy equipment justification or reduce to 2s |
| 3 | Thermal round + blood | Ch 1 | CRITICAL | "Thermal-kinetic round" or reduce blood volume |
| 4 | EM vs acoustic spectrum | Ch 5 | MAJOR | Change "electromagnetic" to "frequency" spectrum |
| 5 | Nosebleed mechanism | Ch 3 | MAJOR | Change "brain pressure" to "blood pressure spike" |
| 6 | 3 Hz tooth resonance | Ch 4 | MAJOR | Change "molars" to "jaw" + bone conduction |
| 7 | Standing corpse | Ch 1 | MINOR | Add "for a moment" before collapse |
| 8 | Cantonese in Shanghai | Ch 9 | MINOR | Clarify as intentional or change dialect |

---

## Research Notes

### Worldbuilding Science That Works Well

The manuscript's fictional science is generally well-grounded:
- **Nitro as resonance-based energy** — follows real fluid dynamics (flow-induced vibration, Joule heating)
- **Void absorption** — radiative cold, structural geometry, "fracture" physics are internally consistent
- **Infrastructure monitoring** — RCI correlations, decay profiles, throughput logic all sound
- **Tradecraft** — dead-hand protocols, air-gapped storage, Faraday cages, tradecraft procedures
- **Corporate governance** — emergency succession, classification manipulation, budget obfuscation

### Areas Where Extrapolation Is Strong

- The "hum" as occupational hazard (vibroacoustic disease) is medically grounded
- Climate-adapted geography (expanded Bay, submerged San Jose) follows IPCC projections
- AR/implant interference near heavy infrastructure is electromagnetically sound
- The distinction between linear and exponential decay as a diagnostic tool is real engineering

---

*Reality check complete. 8 issues identified across 11 chapters. 3 critical, 3 major, 2 minor.*
