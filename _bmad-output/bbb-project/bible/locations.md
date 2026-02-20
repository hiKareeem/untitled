---
title: "Locations"
type: bible-dimension
dimension: locations
lastUpdated: "2026-02-20"
lastChapter: "B2 Ch 27"
totalLocations: 20
activeLocations: 15
project_name: "Untitled"
---

# Locations

> Living Narrative Bible — Spatial Dimension
> Location database with resources, events, and occupants

---

## Usage Instructions

This bible dimension maps the **story world**:

- **Each location** is documented with full description
- **Resources** are tracked (abundant, moderate, depleted)
- **Events** that occur there are recorded
- **Control/occupation** is traced

### Entry Format

```markdown
### [Location Name]

**Description:** [Physical and atmospheric description]

**Discovered:** Day [N], by [character]

**Resources:**
- [Resource 1] (abundant/moderate/scarce/depleted)

**Dangers:**
- [Danger 1]

**Key Events:**
- Day [N]: [Event]

**Significance:** [Narrative importance of location]

**Current State:** [Current condition]

**Controlled by:** [Group/Character or "Neutral"]
```

---

## Narrative Map — Neo-Shanghai

Neo-Shanghai is a vertical megacity spanning ~3.7km from Deep Sump (-200m below ground) to the Spires (~3.5km altitude). Class, geography, and risk are vertically stratified. The city is **not enclosed** — it is open-air at the top, built upward from the original ground-level industrial city.

### Vertical Model

| Stratum | Altitude | Origin | Sky Visibility |
|---------|----------|--------|---------------|
| **Deep Sump** | -200m to 0m | Downward expansion for nitro conduit infrastructure | None — subterranean |
| **Sump** | 0m to ~50m | Original ground-level city. Industry, residential, markets. Where the city started. | Effectively none from street level — the Mid-Levels and Spires are built directly above, creating a dense urban canopy. Orange conduit glow is the dominant light. Slivers of sky might be visible at district edges or through construction gaps, but functionally the Sump lives under a ceiling of its own city. |
| **Brightline** | ~50m | The visible boundary where conduit glow (orange) gives way to artificial white light. Not a place — a transition. | Marks the shift from canopy shadow to managed lighting |
| **Mid-Levels** | 50m to ~500m | Upward population expansion. Commercial, residential, transit hubs. | Increasing with altitude. Lower Mid-Levels still heavily canopied; upper Mid-Levels have gaps, terraces, observation platforms where sky is visible. |
| **Spires** | 500m to ~3.5km | Corporate towers, ego, power. Latest construction. | Full sky access. Open-air terraces, panoramic offices, the world the Sump built for people who never go down. |

**Sky access note:** Clean energy (nitro) eliminated smog generations ago. The sky is clear and visible — the issue isn't atmospheric, it's architectural. The layers of the city itself block the view from below. A Sump resident who wants to see the sky needs to travel upward through the Mid-Levels to an observation platform or canopy gap. This requires transit permits (managed by GridLine, a NitroCore subsidiary) and costs money. The sky is free; the access isn't.

**Observation decks:** Exist at various points in the upper Mid-Levels (~200-400m) where the urban canopy thins. Some are commercial (charge admission), some are transit-adjacent (visible during transfers). Level 12 observation deck referenced in Ch 4 is one such platform — charges a day's wages for 30 minutes of unobstructed upward view. For a Sump resident, seeing the sky is an event, not a daily experience.

### Deep Sump

**Description:** Below ground level to -200m. The oldest infrastructure — trunk-lines, converter stations, automated systems. Skeleton-crew maintenance. The void doesn't invade from outside; it blooms upward from here.

**Stratum:** Lowest
**RCI Range:** 25–40+
**Characters Present:** Fuxi (work shifts)

**Resources:**
- Trunk-line infrastructure (critical — city's circulatory system)
- Converter stations (critical — nitro processing)
- Old stockpiles (moderate)

**Dangers:**
- Highest RCI readings in the city
- The Confluence (breach origin point)
- Void absorption fronts follow infrastructure upward
- BLACKWEIR flood zone

**Key Interior Locations (established Ch 4):**
- **Monitoring Bay, Section 4-East:** Concrete box bolted to Trunk-Line 4-East at the junction where first-generation infrastructure meets 2160s bypass conduits. Six monitors (three automated, three crewed). Bolted furniture (trunk-line vibration walks unsecured items). Amber/green data displays. Orange conduit glow as dominant light source — pipe walls thinned over 150 years, metal becoming translucent. Industrial fluorescent overhead (irrelevant). The hum is physical — pressure through floor, chair, bones, settling behind the eyes.
- **Trunk-Line Corridor (Section 4-East to ascent shaft):** 200m reinforced concrete. Metal grating floor — see-through to service channels below where smaller conduit branches split off. Trunk-line runs along ceiling. Conduit glow lighting. Grating vibrates with trunk-line heartbeat. Not a place for conversation — hum makes it effortful.
- **Ascent Shaft:** Vertical transit corridor, pressurized tube with cargo lift (repurposed for personnel after 2160s automation wave when personnel lifts decommissioned). Slow. Trunk-lines run vertically through the shaft. Hum character changes during ascent — first-generation low-frequency drone fades, replaced by higher-pitched composite of newer distribution branches.

**Key Interior Locations (established Ch 39):**
- **Converter Station (three levels below Monitoring Bay):** R0 intake valve processing — steps nitro between grades (R1→R0 for local distribution, R0→trunk-line feed). Two operators per shift. Reinforced glass partition between main floor and intake booth. Alarm panel (wall of indicators). Emergency exits: trunk-line corridor east to monitoring bay/ascent shaft, maintenance access west to Resonance District stairwell. First-generation pipes meeting 2140s processing nodes. During BLACKWEIR: all valves under NitroCore corporate security override; both exits sealed (pressure door + pre-installed manual bolt on maintenance access). The station becomes an island of processed air in a flooded network.

**Key Events:**
- **Ch 4:** RCI fluctuation on monitor 6 (Section 4-East, near Resonance District boundary). Spike from 27.1 to 31.2, held ~40 seconds, self-corrected with atypical linear decay profile. Fuxi logged anomaly; Chen Wei dismissed. Baseline for this section: 26-28. Alarm threshold: 35. Emergency protocols: 40.
- **Ch 16:** Eleven weeks of accumulated data. Seven spikes logged on monitor 6, acceleration pattern visible (40s → 19s decay times). First-generation infrastructure running at three times design specification. Fuxi maintains private log correlating spikes with residential disappearances. Quarterly safety briefing conducted in the bay — "nobody believed and everybody signed." Chen Wei continues institutional routine without examining the pattern.
- **Ch 40:** Mirelle Dubois absorbed in western maintenance corridor during BLACKWEIR. Running toward Resonance District service level access (RS-WEST junction marker). Flood valves FV-7 and FV-3 documented as open. Wet-film residue saturating corridors — airborne, substrate-propagated. Absorption front advancing along conduit network. Mirelle stops 140m from RS-WEST, absorbed mid-sentence while thought-dictating to Black Babel. Implant continues transmitting briefly after body ceases motor function.
- **Ch 22:** Step-function spike on monitor 6 — 27.1→43.1, 4.7σ above baseline, sustained, no correction. Phase 2→3 transition trigger (The Confluence begins its activation gradient). Automated alert fires: VEC-STK-2175-Q1-0412, cross-references classified VEC-THR-2169.4-D. Chen Wei leaves 47 minutes early — doctrine broken. Monitoring bay goes amber→red for the first time. Private log entry 62 recorded.
- **Ch 24:** Mirelle descends below Level 12 via Shaft 7-C with former NitroCore conduit inspector (22 years, son disappeared). Discovers hidden parallel infrastructure: modern composite construction (Spire-grade material), NitroCore 2170s serial numbers, installation dates 2171-2173. Four junctions documented: B-12-East (RCI 34.6, 2173), B-12-South (RCI 37.2, 2172), B-12-Sub (RCI 39.8, 2171 — earliest), B-12-Confluence (RCI 41.3, 2172, six trunk-line branches mirroring upper Confluence). Throughput volumes exceeding residential distribution by order of magnitude. Infrastructure concealed by decommission classification on all public maps.
- **Ch 28:** Kindling network meeting. Bench from Ch 22 (ascent shaft corridor) removed — cut at mounting bolts, institutional erasure of gathering points. Kindling woman leads Fuxi to decommissioned pump station beneath Section 4-East: 12 maintenance workers, 214 combined years. 47 flood valves revealed (NitroCore, 2171-2173). Step-function spike sustained 48 hours and counting. Black Babel / Wire / Erasure List named as delivery channels.
- **Ch 34:** Mirelle deposits complete fourteen-month evidence dataset with Talia Ravid at Node RD-14 (rotated to textile wholesaler's loading dock, Resonance District commercial strip). Dead-hand protocol finalized with three sealed recipients. 7th flood valve documented via ventilation corridor, Sector 6 (retired inspector's credentials). Sofia's atmospheric convergence data crosses Talia's node but compartmentalized from Mirelle's stream. Nitro-ear bilateral at 11 weeks — 1 week to permanent damage. 28 disappearances / 6 sectors.
- **Ch 39:** BLACKWEIR activation. Eighth spike on monitor 6 — step-function, no decay (27.3→34.1+, still climbing). Every maintenance alarm fires simultaneously. R0 crude floods trunk-lines via synchronized NitroCore corporate valve override. Pressure doors seal Sump sectors in cascade — 23 sectors, "[17 alerts suppressed]." Fuxi in converter station recognizes infrastructure as delivery system. Both exits sealed. Absorption front propagates along conduit network — visible on residential grid map as violet wave. Duan (co-operator) attempts valve shutdown — lockout. Converter station survives as processed-air pocket below the flooding.

**Key Interior Locations (established Ch 24):**
- **Shaft 7-C:** Industrial sub-level beneath Sump Sector 7. Service elevator with biometric access (contact's duplicated credentials). Transition point from known Sump infrastructure to hidden Below Level 12 network.
- **Below Level 12 — Main Corridor:** Modern poured composite walls (not pre-NitroCore concrete). Conduit housings at regular intervals, each stamped with NitroCore corporate logo and 2170s serial numbers. Orange glow brighter than anywhere in upper Sump or Resonance District. Pipes thicker, reinforced. Designed for throughput volumes exceeding residential distribution.
- **Junction B-12-East:** First junction. RCI 34.6. Installed 2173. Standard trunk-line junction with reinforced housing.
- **Junction B-12-South:** Second junction. RCI 37.2. Installed 2172. NitroCore maintenance schedule mounted — regularly serviced infrastructure that officially doesn't exist.
- **Junction B-12-Sub:** Third junction. Subsidiary level beneath main corridor, accessed through biometric maintenance hatch. RCI 39.8. Installed 2171 (earliest). Built during same quarter NitroCore allocated residential maintenance funding above — funding that was deferred.
- **Junction B-12-Confluence:** Fourth junction. RCI 41.3. Installed 2172. Six trunk-line branches at deeper level, mirroring the upper Confluence geometry. The infrastructure's purpose node.

**Significance:** The Confluence sits beneath the Resonance District here — six first-generation trunk-lines converge at the highest-throughput conduit junction in the city. This is where BLACKWEIR detonates. Below Level 12, a parallel infrastructure network (2171-2173) was built for throughput volumes that exceed residential distribution — purpose unknown to Mirelle but connected to BLACKWEIR's flood valve system.

**Current State:** Operational pre-BLACKWEIR; scoured post-BLACKWEIR

**Controlled by:** NitroCore (infrastructure), Hollow Legion (territory)

---

### Sump

**Description:** Ground level to ~50m. The old city surface — residential districts, Church halls, markets, labor pool. Abundant with life, rotting with neglect. The hum through the walls is white noise. Power flickers. Shimmers near conduit access points.

**Stratum:** Low
**RCI Range:** 15–25
**Characters Present:** Fuxi (home), Nuwa (home), Nephthys (arriving Phase 3)

**Resources:**
- Residential housing (dense, low-quality)
- Church of Blessed Nitro halls (spiritual infrastructure)
- Markets / Hum Market (commerce)
- Labor pool (expendable)

**Dangers:**
- Proximity to Deep Sump trunk-lines
- RCI fluctuations increasing
- Disappearances near conduit access points
- Transit permits denied during "infrastructure maintenance periods"
- BLACKWEIR sacrifice basin

**Key Interior Locations (established Ch 4):**
- **Residential Corridor (Fuxi/Nuwa's block):** Narrow, low-ceilinged. Poured concrete walls (pre-NitroCore era). Exposed conduit housing along ceiling — orange-glowing pipes bolted to brackets, NitroCore logo stamped every third joint. Conduit glow is primary light source (overhead fixtures burned out months ago, unreplaced). Smells: cooking oil, recycled air, faint chemical sweetness of nitro. Children play in corridors (apartments too small, surface streets too close to conduit access points where shimmers appear).
- **Fuxi and Nuwa's Apartment:** Third floor, 2080s residential block (renovated never). Two rooms. Shared bathroom down the hall. Frosted polymer window facing adjacent block's corridor (looks at nothing). Rent subsidized by municipal service (deducted from wages before Fuxi sees them). Compressed foam mattress on wall-built platform, covered with deep blue salvaged textile (interlocking circles pattern — Nuwa says it reminds her of the sky). Hum transmitted through building structure — quieter than Deep Sump, constant, domestic. Boot mat by door (running negotiation: Nuwa wants boots off in corridor, Fuxi wants them off inside where they won't be stolen).

**Key Events:**
- **Ch 4:** Fuxi returns from Deep Sump shift. Residential corridor and apartment details established. Nuwa absent (textile recycling second shift, ends 20:00). Fuxi sits in the hum and thinks about monitor 6.
- **Ch 8:** First shared domestic scene — Fuxi and Nuwa together in the apartment. Nuwa cooking (early rotation, 06:00-14:00). Boot-mat ritual. P-3 / Mid-Level transfer argument. Shimmer near Hum Market conduit access points — neither names it ("Normal crowd"). Jun's multitool first prose appearance. Nuwa's shift details confirmed (this rotation: early). Municipal advisory updated twice ("Ambient hum levels within certified tolerance").
- **Ch 16:** Nuwa's transfer plan progressing — the apartment at its most domestic and hopeful. Fuxi withholds the private log from Nuwa. Closes on the blue textile with the file open on the cracked frame. The apartment as site of competing architectures: rising (Nuwa's plan) and counting (Fuxi's log).
- **Ch 20:** Stalker-7 deployed to Sump Sector 9-East — first Sump operation. Breach propagation non-radial: lattice follows conduit infrastructure, bypasses dead-end corridors, prioritizes high-throughput trunk-lines and junction nodes. Two maintenance technicians absorbed at junction node 9-14 (night shift, 02:15). RCI peak 24.1. Lattice advancing at 4 m/min along trunk-line toward junction 9-17. Absorbed: eleven percent metabolic/neural baseline (canonical). Breach still mobile at chapter end — extraction team not cleared.
- **Ch 42:** BLACKWEIR hits Block 14. Power out, hum changes to wet/pressurized, conduit glow drops from orange to nothing. Walkway between Building 14 and Building 11 (4th floor, metal grating) — people absorbed into infrastructure (embedded, not dissolved). Mrs. Huang's laundry still on the line. Neighbor's hand on Nuwa's frosted polymer window — textile reclamation staining, drawn into the polymer. Nuwa descends via back stairwell (masonry walls, not metal framing) to masonry annex (ground floor, Block 14 — poured concrete, manual door on wooden frame, no electronic lock, no conduit connections). Coherence spike (11 seconds) passes through masonry. Violet glow replaces orange conduit glow. Post-spike: hum "fuller" — contains more than building resonance should.

**New sub-locations (Ch 20):**
- **Sector 9-East:** Sump residential core on first-generation conduit infrastructure. Higher baseline vibration than other sectors due to trunk-line proximity. Evacuation zone established during Ch 20 breach. Boot mat with one boot missing in an apartment doorway — Sump domesticity interrupted.
- **Junction node 9-14:** Trunk-line intersection, three primary conduits converging. Site of two absorbed maintenance technicians (night shift, 02:15). RCI peak 24.1 — highest Nikolai has recorded outside Deep Sump. Lattice boundary 1.8m. Lattice extending northeast along trunk-line toward 9-17.
- **Junction node 9-17:** Downstream trunk-line junction northeast of 9-14. Patil's L-Frame held position here. Lattice advancing toward this node at 4 m/min at chapter end.

**New sub-locations (Ch 23):**
- **FOB Meridian (Sector 12 junction complex):** Forward Operating Base at the Sump/Mid-Levels boundary. Repurposed infrastructure maintenance junction — tool racks converted to weapon racks, calibration benches to operational displays, relay technician quarters to sleeping quarters (still smell of insulation compound and metallic tang). Conduit network transitions here from residential-scale distribution to heavy trunk-lines feeding Mid-Levels grid. Baseline hum 12.4 (vs garrison 8.1). Reinforced conduit housings run through the complex like exposed arteries. Tactical overlay covers Sectors 10-14 (1.4 million residents). Stalker-7 forward-deployed here under VS-2175-0089 (indefinite duration, no evacuation authority). 17 emergency evacuation corridors connect Sump to Mid-Levels within operational zone.

**New sub-locations (Ch 42):**
- **Walkway (Building 14 ↔ Building 11):** 4th floor metal grating connection. 18m gap between buildings (ventilation corridor per original construction codes for conduit heat dissipation). Emergency strips on railing (non-functional during BLACKWEIR). Absorption site.
- **Back stairwell (Block 14):** Masonry walls instead of metal framing. Three extra minutes vs. main stairwell. Emergency strips dead. Violet glow bleeds through gap where masonry meets original building frame at 2nd-floor landing.
- **Masonry annex (Block 14, ground floor):** Storage room. Manual door — metal handle on wooden frame set into poured concrete. No electronic lock, no biometric reader, no connection to building systems. Broken shelving unit, bicycle frame with no wheels, dust on storage shelves. Cold concrete floor. Path-poor construction — minimal conduit proximity. Survival pocket during BLACKWEIR.

**Significance:** The Sump is the sacrifice basin. BLACKWEIR floods it with raw nitro, severs junctions upward. The Sump's residents are "projected casualties." This was always the design.

**Current State:** Populated pre-BLACKWEIR; scoured post-BLACKWEIR

**Controlled by:** Neutral (residents, Church presence, NitroCore infrastructure)

---

### Mid-Levels

**Description:** 50m to ~500m. Commercial, residential, transit hubs. Where most of the city's visible life happens. Chén Academy operates here. The first residential void incursion in 8 months triggers Phase 2.

**Stratum:** Middle
**RCI Range:** 8–15
**Characters Present:** Nikolai (deployed), Mirelle (mobile), Sofia Reyes (B2 Ch 26+)

**Resources:**
- Commercial districts (abundant)
- Residential housing (moderate quality)
- Transit hubs (infrastructure)
- Chén Academy (mage training)

**Dangers:**
- Occasional void incursions (contained by Stalkers)
- RCI fluctuations from below
- Increasing post-BLACKWEIR: refuge for Sump survivors

**Key Events:**
- **Ch 11:** Stalker-7 deploys to Level 7 residential breach, junction housing 7-14. Three absorbed (civilian woman, civilian man embedded in wall, conduit tech embedded in junction housing). RCI 14.2-14.6 (anomalous for stratum). Hum near junction carries perceived name (Corporal Deng). Containment successful, area secured.
- **Ch 38:** BLACKWEIR perimeter enforcement at Sump/Mid-Level boundary (south sector). Stalker-7 holds line at Junction 12. Blast doors seal at 06:17. Emergency broadcast cycling 640+ times. 69 civilians redirected ("Return to your residence"). Absorption front advances through Junction 14-East via unsevered secondary service conduit — institutional gap in severance work orders. Jarek Kowalski absorbed at 16:47. Garrison south sector used for post-deployment processing.

**New sub-locations (B2 Ch 26):**
- **Sofia's Apartment (39th floor, Mid-Levels residential block):** Non-VEC-affiliated rental unit. Secondhand desk (purchased from transit corridor dealer — price less than one calibration cycle of the immersion pod). Kitchen 2 meters from desk (vs. 3 at VEC housing). No acoustic dampening. Conduit density higher than 61st-floor VEC tower — hum at 1.4x amplitude, audible without instruments. 4 blocks east of sacrifice district boundary (designation markers visible from window). Field kit set up before boxes unpacked. Encrypted terminal beside field kit on the desk. 11 boxes in hallway (3 unpacked as of B2 Ch 26). Sofia's base of operations from B2 Ch 26 forward.

**Key Events (B2):**
- **B2 Ch 26:** Sofia moves in after 30-day VEC housing clock expires (27 days used on analysis). Erasure List channel open. Sacrifice district correlation assembled (14 cities, 0.89-0.95). De-escalation framework begun. Midnight: boxes still in hallway, hum through walls, designation markers 4 blocks east.

**Significance:** The buffer zone between Sump expendability and Spire privilege. Where "normal" is maintained longest.

**Current State:** Operational

**Controlled by:** Mixed governance (corporate, civic, Academy)

---

### Spires

**Description:** 500m to ~3.5km altitude. Corporate towers, self-contained vertical districts — each essentially a self-contained city owned and operated by a specific corporation or consortium: NitroCore Spire, Helix Spire, Chimera Spire, Government Spire (PCC administrative offices). State-of-the-art conduit systems: sealed, monitored, real-time RCI dampening. The hum is nearly inaudible. Spire residents have never heard the hum the way Sump residents hear it.

**Stratum:** Highest
**RCI Range:** <5
**Characters Present:** Aurielle Vasquez, Sofia Reyes (VEC HQ)

**Resources:**
- Corporate infrastructure (abundant)
- Nanite-grade technology (elite)
- Self-contained life support (redundant)
- Power supply (abundant — nitro-fed)

**Dangers:**
- Political exposure
- Moral complicity
- BLACKWEIR authorization originates here

**Key Events:**
- Ch 5: Sofia detects anomalous 0.7 Hz pulse in VEC HQ sub-strata sensors. Liang deflects (SOP 7.1). Instruments fine. Personal archive entry #15.
- Ch 15: Sofia discovers 0.94 correlation between atmospheric pulse and Stalker deployments. Liang holds paper for methodology review. Vertical gradient discovered: Sump 0.96, Mid-Levels 0.91, Spires 0.87. Personal archive entry #16.
- Ch 27: Sofia's atmospheric model complete — 0.7 Hz pulse classified as VEC (Void Emergence Correlation). Liang approves for internal circulation only. Model predicts Confluence activation gradient. Personal archive entry #17.
- Ch 33: Sofia's convergence model presented to VEC senior staff. Throughput reduction recommendation (40%) rejected. Liang assigns Sofia to real-time monitoring during "infrastructure stress test." Personal archive entry #18.
- Ch 41: BLACKWEIR observed from 35th floor immersion pod — Confluence wave propagation visible on holographic display, coupling events populating as points of light tracing conduit architecture. Engineered differential confirmed: Sump climbing 3x faster than Mid-Levels, Spires barely moving. 11-second coherence spike overwhelms pod sensors. Sofia locked out of 47th floor classified briefing (biometric denial). VEC Emergency Alert displayed: "Confluence confirmed. VPI: 87.3%. AEGIS targeting calculated." Dead-hand cache fragments received via encrypted relay. Complete dataset archived outside VEC network.

**Sub-Locations (established Ch 5):**
- **VEC Atmospheric Monitoring Lab (35th floor):** 11 workstations in horseshoe around central holographic display (3m sphere, decorative, not used for real analysis). Immersion pods at each station. Sofia's pod at far end (chosen for isolation). Evening protocol dims lights.
- **Immersion Pod (Sofia's):** VEC-standard holographic analysis environment — sealed chamber, walk-in closet sized. Projection arrays render data as 3D spatial fields. Haptic suit translates frequency as texture, amplitude as pressure, temporal patterns as rhythm. Where Sofia does her real work.
- **Dr. Liang's Office (47th floor):** Administrative stratum. Floor-to-ceiling window facing outward/upward — Spire district view, Sump invisible below. Three holographic displays in semicircle. Clean, organized. Window orientation = institutional gaze.
- **Sofia's Apartment (VEC residential level):** Institutional housing for senior research fellows. Quiet, climate-controlled. Window shows sky/stars. Contains encrypted personal terminal (non-VEC network components). Small desk. The hum reduced to a whisper.

**Significance:** Where the decisions are made. Where BLACKWEIR is authorized. Where the stock price recovers within 48 hours.

**Current State:** Operational, insulated

**Controlled by:** NitroCore, corporate sovereignty

---

### The Confluence

**Description:** Beneath the Resonance District in Deep Sump. Six first-generation trunk-lines converge at the highest-throughput conduit junction in the city. Automated, skeleton-crew maintenance. The breach origin point.

**Characters Present:** None (automated)

**Resources:**
- Highest nitro throughput in the city

**Dangers:**
- Breach origin point
- Activation gradient begins here (Phase 2→3 transition)
- The void blooms upward from this junction

**Key Events:**
- [To be populated as chapters are written]

**Significance:** The void doesn't invade Neo-Shanghai from outside — it follows the plumbing up from here. The Confluence's activation is the point of no return.

**Current State:** Active, escalating

**Controlled by:** NitroCore (automated)

---

### Cathedral of Living Sound

**Description:** In the Sump. Acoustic architecture that dephases wet-film network remnants — creates a bubble of coherence-disruption. Nephthys experiences the chorus resolving into something she interprets as harmony here.

**Characters Present:** Nephthys (Phase 3+), Imani

**Resources:**
- Unique acoustic architecture (broadband resonance dephasing)
- Spiritual gathering space

**Dangers:**
- Located in the Sump (BLACKWEIR zone)
- Theological implications of its protective properties

**Key Events:**
- **Ch 26:** Nephthys and Imani arrive. Cathedral sealed by Luminarch's Office on Malachi's recommendation — deconsecrated, magnetic seal dead (conduit severed). Nephthys enters; chorus resolves for the first time — individual threads distinguishable, pain gone. Stone's geological inertness dephases infrastructure noise. She interprets it as divine architecture; the reader suspects physics. Imani begins making the Cathedral habitable. "Third option" theology articulated. Resonance beads warm against the brand.
- **Ch 44:** BLACKWEIR. Nephthys has spent three days here; chorus resolved into individual threads for the first time. When R0 flooding begins, the Cathedral's acoustic architecture dephases the wet-film propagation — the hum changes to a crude growl outside but the chorus remains distinguishable inside. Nephthys walks to the threshold, witnesses three absorptions (running man, waiting child, old woman in metal chair). Coherence spike (11 seconds) collapses her at the threshold — one hand inside, one outside. "They are all still here." Imani pulls her inside. ~340 survivors fill the Cathedral (31 initially present + those who reached it during the event). First congregation forms around Nephthys's listening — not preaching, not theology, just presence. Stone vibrates but does not carry the wet-film. Resonance beads "vibrating hard enough to crack."

**Significance:** Protects Nephthys during BLACKWEIR — not by divine intervention but by physics. She interprets it as providence. This becomes the foundation of a theology that reshapes the world. First congregation forms here among survivors. The Cathedral's survival pocket (~340 people) is confirmed by AEGIS orbital data (Book 2 AEGIS chapter).

**Current State:** Standing (survives BLACKWEIR — masonry/acoustic, path-poor for wet-film). Interior occupied by ~340 survivors post-BLACKWEIR.

**Controlled by:** Church of Blessed Nitro (historical) → Nephthys (de facto post-BLACKWEIR, first congregation)

---

### NitroCore Tower

**Description:** Dominant structure in the Spires. Corporate headquarters. Where Aurielle's board meetings happen, where Thorne briefs her on "Sump lifecycle management," where BLACKWEIR is authorized.

**Key Interior Locations (established Ch 1):**
- **Celestial Ballroom (114th floor):** Gala venue. Floor-to-ceiling windows, commissioned art (rotated quarterly), environmental systems scrubbing air to tastelessness. Stage with podium and row of high-backed chairs for executive delegation. Holographic display behind podium. Drone cameras broadcasting live feeds. Site of Eduardo Vasquez's assassination.
- **Corridor (outside ballroom):** 90m long, lined with commissioned light sculptures by PCC-funded artist — nitro-infused glass casting amber refractions. Dark carpet.
- **Private Suite (116th floor):** Medical staging area. Floor-to-ceiling windows facing the Spires. 114 floors above the city. The Sump is invisible from here — "Nobody could."

**Key Interior Locations (established Ch 7):**
- **Executive Chamber / Boardroom (108th floor):** Sealed ovoid, 21.2°C (behavioral study on decision-making compliance), acoustics designed to project from the Chair's position. Fifteen seats. Eduardo's chair at the head — nanite-threaded leather, adjusted to his body, doesn't fit Aurielle yet. The hum calibrated to a frequency the human ear registers as silence. Six floors below the Celestial Ballroom.
- **Eduardo's Office:** 30m corridor from the Executive Chamber — same dark wood paneling, recessed lighting, temperature-controlled silence. Spanish walnut desk shipped from Cádiz (where the Vasquez name started). Desk chair still holds Eduardo's body impression. Sandalwood cologne was embedded at molecular level — processed out by atmospheric scrubbers by Ch 25 (gone); Ch 7/12 present, Ch 19 fading, Ch 25+ gone. Floor-to-ceiling window. Reading alcove. Handkerchief in top left drawer (bloodstained, won't fully clean). Three datapads + NitroCore water glass on desk. Outbox tray (brushed steel, right side — positioned by Eduardo ~30 years ago). NitroCore institutional pen (weighted, blue ink). Executive assistant station outside (unfilled — assistant on leave since assassination).
- **Corridor (Executive Chamber → Office):** 30m, dark wood paneling, recessed lighting, silent carpet. Two security personnel stationed along route.

**Key Interior Locations (established Ch 12):**
- **Sub-level 7 Briefing Room:** Classified facility below lobby level. Hexagonal chamber, composite walls (same matte material throughout), fluorescent lighting ("did not pretend"), two chairs, water dispenser. Holographic array with recessed control surface in table edge. Built by Aurielle's grandfather, used quarterly by Eduardo for eleven years, now inherited by Aurielle. Requires three authentications: biometric (palm + retinal + subcutaneous ID), daily 16-digit authorization code (delivered via intelligence brief at 06:00), and physical carbon key (Eduardo's desk, false bottom of top drawer). The hum is present here — not managed away as on executive floors. "The room where the real numbers lived." No windows, no records, no schematic listing.
- **Sub-levels (general):** Negative floors below lobby. Building structural diagrams classify as "environmental and mechanical systems" — accurate but incomplete. Accessed via authenticated elevator. Numbers count backward from lobby.

**Characters Present:** Aurielle, Marcus Thorne, Chen-Nakamura (CFO), board members

**Significance:** The institutional seat of the genocide. Aurielle's view from the tower window — looking down at where the Sump used to be — is a candidate for the book's final image. The Sump's invisibility from Spire altitude established in Ch 1 closing. Tower confirmed as 212 floors (Ch 12).

**Current State:** Operational

**Controlled by:** NitroCore

**Key Events:**
- Ch 1: Eduardo Vasquez assassinated at Celestial Ballroom gala (thermal-kinetic round, military grade, high angle). Aurielle inherits NitroCore.
- Ch 7: First board meeting in Executive Chamber. Quarterly review — slide 17 ("Sump Infrastructure Lifecycle Management"). Thorne's private LP9 briefing in Eduardo's office. Cause-cost separation revealed.
- Ch 12: Aurielle descends to Sub-level 7 for first time. Thorne presents holographic Sump model — maintenance, absorption, cost projections. Three scenarios. "Welcome to the quarterly."
- Ch 37: BLACKWEIR executed from Operations Center (63rd floor). Aurielle and Thorne watch holographic display as 23 Sump sectors sealed, conduit flood initiated, absorption front propagates. Protocol completes in 84 minutes. 98.4% grid integrity. Aurielle returns to Eduardo's office. Hum *Thinner*.
- Ch 19: First active complicity — Aurielle signs 7 Sump maintenance deferrals in Eduardo's office. Work Order #2175-1847 (Sector 4-7B, 62%). Thorne's standing 08:15 briefing discusses Sector 14 success, not the deferrals. Sandalwood fading. Pen motif introduced. "Because she had filed it."
- Ch 25: Unscheduled quarterly in Sub-level 7. BLACKWEIR introduced — Confluence briefing, three-generation protocol, "system management protocol." Holographic model shows deferred sectors now red. Evacuation paradox presented. Alternatives analysis requested. Eduardo's office: sandalwood gone (atmospheric scrubbers processed last trace). Chair impression intermediate. Small voice maps deferrals to BLACKWEIR perimeter.
- Ch 36: BLACKWEIR authorization. Aurielle signs in Sub-level 7 after reviewing three-generation protocol. Holographic Sump model shows 23 sectors. "The authorization is signed." Small voice and executive voice merge.
- Ch 46: Board meeting — three days post-BLACKWEIR. Thorne presents containment report. Formal commendation (unanimous). Stock ticker: NTRC +3.7%. Corridor walk (Thorne as colleague). Eduardo's office: sandalwood gone, chair impression intermediate, hum thinner = normal. SHEPHERD seeded via Anchor Zone "opportunities." Executive balcony introduced (not opened).
- B2 Ch 1: Six months post-BLACKWEIR quarterly. Stock recovered. Containment reclassified as "infrastructure investment." Anchor Zone atmospheric data: "commercial applications pending review." Thorne beside Aurielle (dynamic inverted). SHEPHERD as unnamed R&D line item. "The Chair opened the next report."
- B2 Ch 10: Same day as B2 Ch 1. Private briefing in Eduardo's office — Thorne arrives without paper. SHEPHERD named. Conductivity 7.2x. Three sites: Neo-Shanghai, Lagos, Mumbai. "You're describing a factory." / "I'm describing the future of the grid." Aurielle requests projections. Chair replaced by month 3 (standard requisition — new detail). Handkerchief in drawer, not opened. Hands still on walnut.

**Key Interior Locations (established Ch 46):**
- **Executive Balcony (adjacent to Eduardo's office):** Glass door with biometric reader (reconfigured from Eduardo's palm to Aurielle's). Narrow terrace, two meters deep, width of the office, matte composite railing. Eduardo never used it. Aurielle has never opened it. "The terrace existed as architecture — executive privilege, outdoor air at Spire altitude, a feature specified in the building plans and maintained by the facilities division and occupied by no one." Seeds Book 2/3.

**Key Interior Locations (established Ch 37):**
- **Operations Center (63rd floor):** Sealed chamber on executive corridor — door with no designation, biometric reader recessed flush into frame (palm only). Hexagonal (same geometry as Sub-level 7, scaled up). Twelve workstations in semicircle facing central holographic display area. Structural ring suspends volumetric array across full chamber width. Raised observation platform at rear: two chairs (ergonomic, temperature-regulated, nanite-threaded leather — same as boardroom), recessed control surface identical to Sub-level 7. Real-time infrastructure telemetry feed — every conduit junction, pressure door, residential zone. Designed for long occupancy. "The room was designed for this." NitroCore security personnel, corporate engineering liaisons, grid management division staff. The room's existence unknown to Aurielle until authorization signed — institutional blindness by architectural design.

---

### Conduit Junction 7

**Description:** The critical node at the Sump/Mid-Level boundary where trunk-line throughput is highest (serving the densest population) and infrastructure is oldest. Six trunk-lines from the Confluence route upward through here into the Mid-Levels. This is where BLACKWEIR severance occurs — severing charges fire, transit shafts collapse, blast doors drop, all conduit connections upward physically destroyed.

**Characters Present:** Nikolai (BLACKWEIR execution — turns one of the two physical keys), Mirelle (investigation)

**Key Interior Locations (established Ch 2):**
- **Level 3 Trunk-Line Access Corridor:** Narrow, low-ceilinged, amber conduit-glow strip along left wall. Trunk-line access hatch 30m from residential corridor junction — reinforced steel, biometric lock, NitroCore logo stamped upper-left corner. Poured concrete walls (pre-NitroCore era). Chalk names written on wall to the right of the hatch — Sump tradition, workers write names of the disappeared near where they vanished. Dried flowers left at the base beneath the names.
- **Residential block (Sump, near Junction 7):** Where Lien Suen lives. Apartments with frosted polymer windows, orange conduit-glow casting copper light. Close enough to trunk-line for audible hum in walls.

**Resources:**
- Highest throughput junction above the Confluence
- BLACKWEIR controller hardware (physically hardened)
- Two-key execution system (one military, one civic)

**Dangers:**
- BLACKWEIR severance point — this is where the ceiling falls
- Post-severance: all communications above the cut collapse; only ELF/VLF bedrock pings (1-2 bit status) transmit upward
- Elevated RCI near access hatch: 19.4 (baseline 14-16 for this stratum) — sustained, not spiking (Ch 2)
- Disappearances: entire Junction 7 maintenance crew "reassigned" per NitroCore press release

**Key Events:**
- Ch 2: Dao Suen (conduit maintenance tech) disappeared entering Level 3 access corridor — corridor log shows entry, no exit. Chen Yue disappeared from same residential block three weeks prior. Entire Junction 7 maintenance crew "reassigned" per NitroCore Sump Division. Chalk names on wall: Dao Suen, Chen Yue, at least one older illegible name. Mirelle's RCI sensor read 19.4 near the hatch. Shimmer reported near hatch by neighbor (sub-threshold, VPI-0).

**Significance:** Control this junction and you control whether the breach travels up or stays down. The BLACKWEIR decision focuses here. Post-severance, the people above cannot change what's happening below; the people below cannot call for help.

**Current State:** Operational pre-BLACKWEIR; severed post-BLACKWEIR

**Controlled by:** NitroCore (infrastructure), Void Stalkers (military access during operations)

---

### The Resonance District

**Description:** A Deep Sump neighborhood built directly on top of first-generation trunk-lines. Chronic high RCI. High nitro-ear rates among residents. High Hollow Legion membership. Home to the Confluence beneath it. The breach originates here and propagates upward — by the time it's detected at Sump level, the Deep Sump is already gone. Streets narrower than the commercial strip. Fewer feed-screens. Counter-surveillance hardware in storefront windows (mesh scramblers, frame jammers, signal-dampening paint). The Hum Market is two blocks east. The district polices itself by discomfort, not law — if the hum doesn't drive you out, the Hollow Legion's territorial markers will, and if those don't, the readings above 30 will.

**Stratum:** Deep Sump (surface)
**RCI Range:** 30–40+ (chronic)

**Characters Present:** Fuxi (work proximity), Mirelle (Talia's node), Talia Ravid (node operator)

**Key Interior Locations (established Ch 9):**
- **Talia's Node (repair shop front, established Ch 9):** From the street, a frame-servicing repair shop — refurbished components on a backlit shelf, counter staffed by rotating personnel. Monthly Cantonese passphrase for access. Sliding door behind the display shelf. Back room larger than the front (exterior footprint lies about interior — common Resonance District arrangement). Cool, well-lit by non-conduit spectrum. Dense with hardware: storage racks, encrypted relay stations, three data displays. Serious insulation — the hum is present but muted. Talia's workstation in the center, back to the door. Mug of tea. Data interface capable of processing more than The Wire's Paris bureau.

**Dangers:**
- Ground zero for the breach
- Chronic high RCI exposure
- First area consumed during BLACKWEIR
- Nitro-ear onset for prolonged visitors (Mirelle: 3 weeks onset Ch 9, 5 weeks Ch 13, 7 weeks Ch 21)

**Key Events:**
- Ch 9: Mirelle enters the district via counter-surveillance route (Variation B). Deposits dead-hand cache with Talia at her node. Receives junction reclassification intel. Exits via Variation C.
- Ch 13: Mirelle enters via brightline descent, different route from Ch 9. Different face at the counter. Back room warmer — more equipment generating heat. Talia's operation visibly expanded (more hardware, heat shielding, relay chassis rebuild). Exchanges demographics data for Arctic-7 classified chip. Exits via different route.
- Ch 21: Meeting at Node RD-14 — decommissioned relay station in commercial sub-level (listed as pending renovation for 4 years; conduit connection severed, no active heating). Cable spool seating, chemical-strip green lighting. Talia offers Deep Sump access (below Level 12, NitroCore subcontractor credentials, 12-hour window, 4 trunk-line junctions). Mirelle accepts.

**Significance:** The neighborhood most directly built on top of the thing that kills it. Residents live their entire lives over the loudest part of the scream without knowing what they're hearing. Also the information underground's natural habitat — the high RCI keeps corporate security from staying longer than they have to, making it ideal for Black Babel nodes and counter-surveillance commerce.

**Current State:** Populated pre-BLACKWEIR; obliterated post-BLACKWEIR

**Controlled by:** Neutral (residents, Hollow Legion presence, Black Babel nodes)

---

### The Hum Market

**Description:** Open-air market district in the Sump near a major conduit line. Named for the ever-present sound. Orange glow from conduit lines is the dominant light source. Where ampoules are traded, Frames are repaired, identity credentials are leased, and information moves. Chop shops, black-market mesh hardware, counter-surveillance tools.

**Stratum:** Sump
**Characters Present:** Fuxi (commerce), Mirelle (contacts/sources)

**Resources:**
- Black-market nitro ampoules and canisters (commerce)
- Frame repair yards (technical services)
- Identity credential leasing (survival infrastructure)
- Information brokering (Black Babel adjacent)
- Counter-surveillance tools (illegal in corporate territory)

**Dangers:**
- Elevated RCI near conduit lines
- Corporate security raids (intermittent)
- BLACKWEIR flood zone

**Key Events:**
- [To be populated as chapters are written]

**Significance:** The economic heart of the Sump. Where Mirelle cultivates her "seedy connections at every social level." Where the formal economy and black market overlap.

**Current State:** Active pre-BLACKWEIR; scoured post-BLACKWEIR

**Controlled by:** Neutral (market operators, Kindling presence)

---

## Narrative Map — Secondary Locations

### New Geneva

**Description:** Deliberately preserved as a "legacy" political capital. Lower than other major cities — no Spires, deliberate height restrictions, parks and lakefront maintained as political theater. Where other cities rebuilt around nitro, Geneva maintained significant conventional infrastructure alongside nitro integration — partly Swiss political tradition, partly because Accords signatories wanted a neutral meeting ground not dependent on any single corporation's grid. The hum is present but muted. It feels like the past — which is either a refuge or an anachronism depending on who's visiting. Zeyad's grandfather's portrait hangs in the committee chamber.

**Characters Present:** Zeyad Al-Fahim

**Resources:**
- Diplomatic infrastructure (UGC headquarters)
- Accords framework (legal — renegotiated at regular intervals)
- Classified intelligence channels
- Orbital Weapons Governance Board (AEGIS oversight meets here)
- Faction embassies and delegations

**Dangers:**
- Institutional impotence
- Classified information suppression
- Political theater masking real power (which resides in the Spires)

**Key Interior Locations (established Ch 6):**
- **Hall of Nations:** Length of the main corridor. 87 holographic signatory flags projected from marble ceiling emitters. Eastern alcove: portrait of Ambassador Khalil Al-Fahim (2044, great-grandfather) beside glass case with original signed Accords. Marble floors, glass ceiling — looks like a cathedral from certain angles.
- **Committee Chamber 3:** Circular. 32 seats in a ring (equality signaled, simultaneous visibility denied). Datapad stands, microphones, nameplates. Holographic agenda display at center. Acoustically designed for the record — sound absorbed by curved walls, reflected by ceiling, channeled toward center microphones. Every session recorded, transcribed, timestamped. Conduit infrastructure four floors below, sealed and dampened.
- **Zeyad's Office:** Administrative wing, second floor, east corridor. Small. Desk, 3 datapads, leather notebook, antique pen, silver-framed photograph (desk-scale copy of Hall portrait). Window overlooking lake and low skyline.
- **Commissary (4th floor):** Ceramic cups (budget not updated for disposables). Institutional coffee. Part of the building's performance of permanence.

**Key Events:**
- 2044: Nitro Accords signed here (ceremonial hall, 6th floor — now used for press conferences)
- **Ch 6:** Quarterly Accords Compliance Review. Dr. Patel mentions Arctic-7 under security classification (not scientific review). Zeyad requests full briefing, denied — routed to Classification Directorate pipeline (10-15 business days). Discovers "contained" in GCTA briefing p.9.
- **Ch 17:** Arctic-7 data request returns: 14 pages, 8 redacted under Annex C. Zeyad initiates encrypted back-channel with Mirelle from forgotten cantonal terminal in east corridor. First omission from institutional record.
- **Ch 30:** Emergency UGC session in Chamber 3 — Neo-Shanghai escalation. Zeyad invokes Article 7, Section 3 (first invocation in 11 years). NitroCore Legal counsel invokes Section 14 sovereign consent ("where practicable" as veto). Committee votes 23-3 to continue monitoring with enhanced briefing cadence. Cease-and-desist delivered to Zeyad's office (Article 12, NitroCore framing data as proprietary). Back-channel exchange from secure comm alcove (east corridor terminal): Mirelle diagnoses institutional architecture. Notebook full (47 questions), placed on desk not in drawer. Portrait touched deliberately (not ritual). Jordanian flag still flickering (9 weeks). "The mechanism did not exist."
- **Ch 45:** BLACKWEIR aftermath. Class 4 → Class Apex reclassification. Committee emergency session in Chamber 3: votes on response framework (how to discuss, not what to do). Dead-hand fires Day 5 — Mirelle's cache arrives. Zeyad publishes public statement through Black Babel relay. Article 12, Section 8 violated.
- **Ch 50:** Accords Compliance Tribunal convened — Article 12, Section 8 prosecution. Tribunal Chamber (same circular architecture as Committee Chamber 3). Dr. Adeyemi presides (Nigerian diplomat, 20-year acquaintance). Five counts of unauthorized disclosure. Evidence displayed as prosecution exhibits. Zeyad says nothing. Guilty on all five counts. Credentials revoked, access suspended. Biometric panel glows red — office inaccessible. Jordanian flag still flickering (months, maintenance request pending). FINAL Zeyad POV in Book 1.

**Key Interior Locations (established Ch 50):**
- **Tribunal Chamber:** Same circular architecture as Committee Chamber 3 — "the same acoustics, the same procedural fluency." Seven tribunal members. Gallery seating. NitroCore terminal (observer status). Evidence display screens behind defendant's seat.

**Building Details (established Ch 6):**
- 42 floors (required 3 rounds of canton commission review)
- Actual glass windows (not polymer — heritage materials as UGC commitment signal)
- Conduit infrastructure modern, well-maintained, but runs alongside conventional power (solar arrays, battery reserves — redundancy as political philosophy)
- The hum is present but muted — background vibration in the floor, not the bones. "An abstraction."
- Jordanian holographic flag (third row, western wall) flickering at lower edge — 43+ mornings, maintenance request pending 6 weeks (budget cuts)

**Significance:** Where faction representatives meet, negotiate, and betray each other. The GRRM "King's Landing" — power contested through words, votes, and backroom deals rather than breaches and orbital strikes. Book 2's political machinations play out here — where the decision to normalize sacrifice districts is debated, where AEGIS strike authority is contested.

**Current State:** Operational

**Controlled by:** United Governance Council (UGC)

---

### European Outlands

**Description:** Nephthys's pilgrimage origin. Outside the European energy grid. Dead towns, residual void scars from years-old events. The chorus flares near old conduit infrastructure.

**Characters Present:** Nephthys (Phase 1–2), Imani (Phase 1–2)

**Resources:**
- Void Witness communes (grassroots knowledge)
- Residual void scar data (unofficial)

**Dangers:**
- Remnant void activity near abandoned infrastructure
- Isolation from institutional support

**Key Events:**
- **Ch 3:** Nephthys and Imani arrive at unnamed dead town. Chorus flares at void scar in central square. Nephthys refuses suppressants, kneels at scar, detects structured/active/plural signal. Orients toward Neo-Shanghai.
- **Ch 14:** Nephthys and Imani arrive at Void Witness commune (converted relay station, grid edge). Lene's testimony — peace during vigil. Grassroots validation. Transit papers secured. Depart for Neo-Shanghai.

**Sub-locations:**

**Dead Town (unnamed)** — Grid-disconnected 7 years ago when Helix Energetics reclassified regional trunk-line as "non-viable." Population ~10-12K, now empty. European Outlands pattern: central square, church hall (north), municipal building (south, partially collapsed), residential rings. Converter station on eastern edge (drained, locked). Void Witness commune 40km south in converted relay station (14 people).
- **Void scar:** Central square, ~8m diameter. Paving stones darker with violet undertone, smoother (molecular reorganization). Adjacent café façade warped (curved, not cracked). Shop windows milky/translucent. Stone is COLD — deeper than surface, deeper than stone should hold. 3 absorbed: couple who ran the café, maintenance worker inspecting converter station. Scar appeared overnight, 7 years ago. No RCI spike recorded (monitoring decommissioned). Chorus is active, structured, strongest scar Nephthys has found.
- **Church hall:** Stone walls, heavy timber roof. Stained glass mostly broken. Wooden pews. Altar bare (sacred objects removed when Church withdrew). Conduit housing still in walls — residual hum from resonance architecture. Nephthys and Imani camp here.
- **Previous scars visited:** Relay station south of Bruges (1 absorbed), junction outside Metz (1 absorbed) — both weaker chorus than this town.

**Void Witness Commune (grid edge)** — Converted relay station near the European energy grid edge. 14 residents, all excommunicates or voluntary Church departures. Reinforced concrete foundations, stripped signal equipment, mounting brackets and antenna scars on roof. Garden plot in salvaged conduit housing (orange NitroCore logos still visible). Solar collector on roof. Windows refitted with salvaged glass (warped, imperfect). Interior includes communal dining area, sleeping quarters, and a former signal processing room repurposed as testimony/confessional space. Chorus is residual here — stripped infrastructure, muted coherence, whisper-level. Led by Dara (former Prelate, Rhineland, Silenced 8 years). Notable resident: Lene (former acolyte, ~26-28, Cologne, left voluntarily after vigil experience at Church of the Blessed Convergence). Transit paper contacts available.
- **Church of the Blessed Convergence (Cologne):** Named parish referenced in Lene's testimony. Location of a point-three void incursion years ago. Standard Breach Vigil conducted (3-day continuous harmonization). Not visited in prose — backstory location only.

**Significance:** Where Nephthys gathers grassroots testimony that validates her theology before arriving in Neo-Shanghai.

**Current State:** Depopulated, remnant infrastructure

**Controlled by:** Neutral / abandoned

---

### Arctic-7

**Description:** Remote research station. Prologue only. Where Dr. Elise Vantanen's breach occurs — the first confirmed absorption event in the story.

**Characters Present:** Dr. Elise Vantanen (prologue only)

**Significance:** Establishes the void's rules viscerally. Remote, classified, contained. "This can happen to anyone, including the protagonist of their own story."

**Current State:** Classified / contained post-breach

**Controlled by:** Classified (likely VEC/NitroCore)

---

### Singapore

**Description:** Rebuilt after the 2128 incident but never fully recovered psychologically. The original breach site — NitroCore Deep Research Facility 1 — was sealed and quarantined. Three absorbed researchers still stand inside the sealed chamber, monitored continuously by the VEC for 47 years — not dead, not alive, transformed into void-matter. The zone around the facility is a permanent low-occupancy buffer. Also a major PCC financial hub and hosts several Chimera Collective data centers.

**Characters Present:** Aurielle (possible remote authorization), Sofia (VEC Asia-Pacific)

**Resources:**
- VEC Asia-Pacific headquarters (institutional)
- Longest-running void monitoring data (47 years)
- Chimera Collective data centers (AI infrastructure)
- Financial hub (PCC)

**Dangers:**
- Proximity to original breach site
- Psychological weight of the sealed chamber

**Key Events:**
- 2128: First documented void breach — 12 researchers killed/absorbed
- 2128+: Three absorbed researchers discovered standing in sealed chamber

**Significance:** Characters who visit Singapore confront the origin of the crisis. The sealed chamber is the world's first evidence that absorption isn't simple death — and the VEC has been watching them for 47 years without understanding what they're seeing.

**Current State:** Operational

**Controlled by:** VEC (regional HQ), PCC (financial)

---

### Chén Academy

**Description:** Mage training facility in Neo-Shanghai's Mid-Levels. Where mages learn to metabolize R3 nitro, where the scream builds. One of several elite academies globally (see also: Varma Academy, Mumbai).

**Characters Present:** [No current POV characters]

**Significance:** The institution that produces mages — the paradox weapons that are tactically useful but aggregately dangerous near breaches.

**Current State:** Operational

**Controlled by:** Chén Academy (institutional)

---

### Free African States

**Description:** A confederation of states that resisted full nitro integration during the Uplift Protocols. Maintained solar, nuclear, and battery infrastructure as primary power sources. Their nitro grid is thin — low-density conduit networks serving critical facilities rather than entire cities. Democratic governance (messy, fractious, but functional). Viewed by the Grid as backward, by the Root as a model, by the Flame as godless, and by the Lens as potentially the most important dataset in the world.

**Characters Present:** [No current POV characters — potential Book 2/3 setting]

**Resources:**
- Partial energy independence (legacy + limited nitro)
- The lowest breach rate on Earth (buried in VEC data)
- Democratic governance infrastructure
- Political independence from corporate blocs

**Dangers:**
- Isolation from global corporate infrastructure
- Potential target if Grid/Sword decides their independence threatens global containment strategy

**Key Events:**
- 2044: Negotiate special Accords provisions maintaining partial energy independence
- 2053–2059: Survive Resource Wars relatively intact by refusing full nitro integration
- 2085: Resist full Uplift Protocol integration

**Significance:** **Chekhov's gun.** If nitro density correlates with breach probability, the region using the least nitro should have the fewest breaches. This data exists and is part of the suppressed evidence trail. The FAS is the control group that proves the correlation — critical evidence in Book 2.

**Current State:** Operational, independent, increasingly isolated

**Controlled by:** Confederation of democratic states

---

### Varma Academy, Mumbai

**Description:** Elite cyber-mage training academy in the South Asian Federation. Kira's academy. One of several globally (see also: Chén Academy, Neo-Shanghai). Corporate-operated, prestigious, family-dynasty mages trained here.

**Characters Present:** Kira (graduated — backstory location)

**Significance:** Kira's origin. Where she was trained to metabolize R3 nitro and use her abilities as performance spectacle. The pop-star pipeline for mages — different packaging from battlefield deployment, same extraction of a child's body for someone else's benefit.

**Current State:** Destroyed (within sterilization radius of AEGIS orbital strike, 2176)

**Controlled by:** Varma Academy (institutional, corporate-affiliated) — pre-destruction

---

### Greater Mumbai Metropolitan Zone

**Description:** Major vertical megacity in the South Asian Federation. First-generation conduit infrastructure (2050s trunk-lines, never fully retrofitted). Population ~3.4 million in target zone (corrected for Frame underpenetration). Vertical stratification follows the global megacity model: ground-level residential (0–50m), mid-altitude commercial/transit (50–500m), high-altitude corporate/elite (500m+). Unlike Neo-Shanghai, Mumbai's conduit walls are 23% thinner — never upgraded from first-generation specifications.

**Void History:**
- VPI exceeded 70% at timestamp 2175.079 (March 2175), entering AEGIS active-storage targeting
- Sub-threshold breach activity over 14 years deposited wet-film residue throughout conduit network
- Wet-film network denser than Neo-Shanghai's at equivalent VPI due to older infrastructure and neglected maintenance
- AEGIS reclassification (2176): wet-film deposits are void *infrastructure*, not residue — the void built a network inside the human network
- Void propagation followed residue, not conduits — no BLACKWEIR containment option (flood pressure would rupture first-generation conduit walls)
- Absorption front: 55 m/s along wet-film pathways (faster than Neo-Shanghai)

**Key Events:**
- 2176.049: VPI exceeded 85%. AEGIS autonomous engagement protocol activated. 15-minute countermand window expired (OWGB vote 4-5-3, dual-key not achieved). 14 tungsten penetrators deployed. Impact at 19:34:06 UTC.
- Casualties: 3,379,000 ± 200,000. Survivors: 8,219 (peripheral zones outside sterilization radius).
- Vitrification radius: 2.3 km from epicenter (modeled: 2.1 km). Surface sterilization: 5.1 km.
- Post-impact anomaly: void structured signal persists in vitrified zone despite destruction of all carrier media.

**Characters Present:** AEGIS (orbital, processing)

**Significance:** First autonomous orbital kinetic strike on a populated city. Proof that BLACKWEIR containment model does not generalize — Mumbai's wet-film network made conduit-based intervention impossible. The wet-film reclassification (infrastructure, not residue) has implications for every city with conduit infrastructure. The signal-in-glass anomaly challenges AEGIS's model that signals require media.

**Current State:** Destroyed (vitrified within sterilization radius; VPI descending post-strike)

**Controlled by:** N/A (post-destruction)

---

### Orbital / AEGIS Platform

**Description:** Humanity has a permanent but limited presence beyond Earth. Several large orbital stations in LEO and GEO serve as manufacturing platforms, research facilities, corporate headquarters, and military installations. AEGIS operates from a dedicated platform in high orbit. Two to three permanent lunar bases (10,000–20,000 total residents). A single small Mars research outpost (~500 people). Nitro IS used in orbital operations — the most efficient fuel for space habitation energy demands.

**Resources:**
- AEGIS orbital kinetic bombardment platform
- Chimera Collective orbital data center
- Lunar mining operations (rare earth, helium-3)
- Manufacturing platforms

**Dangers:**
- Orbital breach vulnerability — no evacuation route, no geography to sacrifice
- AEGIS itself runs on nitro — the weapon pointed at the void is powered by the thing that summons it

**Significance:** Book 3 pressure point. If Earth's nitro infrastructure is throttled, orbital/lunar populations face energy starvation. The strategic paradox at planetary scale.

**Current State:** Operational

**Controlled by:** Mixed (corporate, military, GCTA nominal oversight)

---

## Geopolitical Blocs

| Bloc | Territory | Character | Nitro Relationship |
|------|-----------|-----------|-------------------|
| **Pacific Corporate Coalition (PCC)** | East/Southeast Asia + Pacific Corridor (Vancouver–Tijuana coastal strip). Three capitals: Neo-Shanghai (corporate), Singapore (science/VEC), Bay Area (legislative) | Corporate-governed; Pacific coast of North America aligned during Corporate Realignment — economic gravity, not conquest | Fully integrated; highest nitro density on Earth |
| **Euro-Asian Energy Bloc (EAEB)** | Europe, Central Asia, Russia | Mixed state/corporate governance; Geneva is political capital | Heavily integrated but stronger state regulation |
| **Free African States (FAS)** | Sub-Saharan Africa | Most independent; resisted full integration | Partial nitro use; maintained legacy energy; lowest breach rates |
| **Americas Compact** | Former US/Canada/Mexico interior and Atlantic coast. Pacific coast defected to PCC | Fragmented — corporate Atlantic cities, ungoverned interior. Former US shattered by Cascade Crisis and Resource Wars | Heavy coast integration; interior on legacy/black-market nitro |
| **South Asian Federation** | South Asia | Dense population, democratic but corporate-penetrated | Very high integration; multiple Spire cities; high Sump populations |
| **Greater Middle Eastern League** | Middle East | Post-petroleum identity crisis; mixed adoption | Some regions highest consumers, others maintain independence |
| **Oceanic Territories** | Pacific Islands, Oceania | Low population; extraction-heavy (offshore vent access) | Extraction-focused rather than consumption-focused |

---

## Location Index

| Location | Stratum/Region | Characters | Controlled By | State |
|----------|----------------|------------|---------------|-------|
| Deep Sump | Lowest | Fuxi (work) | NitroCore / Hollow Legion | Operational → Scoured |
| Sump | Low | Fuxi, Nuwa, Nephthys | Neutral / Church | Populated → Scoured |
| Mid-Levels | Middle | Nikolai, Mirelle | Mixed | Operational |
| Spires | Highest | Aurielle | NitroCore / Corporate | Operational |
| The Confluence | Sub-Deep Sump | None | NitroCore (automated) | Active / Escalating |
| Conduit Junction 7 | Sump/Mid boundary | Nikolai (BLACKWEIR) | NitroCore / Stalkers | Operational → Severed |
| The Resonance District | Deep Sump surface | Fuxi (proximity) | Neutral / Hollow Legion | Populated → Obliterated |
| The Hum Market | Sump | Fuxi, Mirelle | Market operators | Active → Scoured |
| Cathedral of Living Sound | Sump | Nephthys, Imani | Church → Nephthys | Standing (survives) |
| NitroCore Tower | Spires | Aurielle, Thorne | NitroCore | Operational |
| New Geneva | EAEB | Zeyad | UGC | Operational |
| European Outlands | EAEB | Nephthys, Imani | Abandoned | Depopulated |
| Arctic-7 | Remote | Vantanen (prologue) | Classified | Contained |
| Singapore | PCC | Sofia, (Aurielle remote) | VEC / PCC | Operational |
| PCC Bay Area | PCC (legislative capital) | Kira, Sofia (born here) | Coalition Assembly / PCC | Operational |
| Chén Academy | Mid-Levels | — | Academy | Operational |
| Free African States | FAS | — | Democratic confederation | Independent |
| Varma Academy, Mumbai | South Asian Fed | Kira (graduated) | Academy | Operational |
| Orbital / AEGIS | Space | — | Mixed (military/corporate) | Operational |

---

## Locations by Category

### Active Locations (pre-BLACKWEIR)
- Deep Sump, Sump, Mid-Levels, Spires, NitroCore Tower, Conduit Junction 7, Resonance District, Hum Market, New Geneva, Chén Academy, Singapore, Free African States, Orbital/AEGIS

### Transformed Locations (post-BLACKWEIR)
- Deep Sump → scoured, violet frost, absorbed embedded in infrastructure
- Sump → scoured, depopulated, hum of the absorbed
- Resonance District → obliterated (ground zero)
- Hum Market → scoured
- Conduit Junction 7 → severed, physically destroyed

### Dormant Locations
- Arctic-7 (prologue only, classified)
- European Outlands (pilgrimage transit)
- Varma Academy, Mumbai (Kira backstory)

### Destroyed/Inaccessible Locations
- Greater Mumbai Metropolitan Zone (AEGIS orbital strike, 2176 — vitrified within sterilization radius; void signal persists in glass)
- Note: Neo-Shanghai's Sump is transformed, not destroyed — infrastructure coated in violet frost, absorbed still present

---

## Resources by Location

| Location | Resource | Quantity | State |
|----------|----------|----------|-------|
| Deep Sump | Trunk-line infrastructure | Critical | Operational |
| Deep Sump | Converter stations | Critical | Operational |
| Sump | Residential housing | Dense | Low-quality |
| Sump | Church halls | Several | Active |
| Mid-Levels | Commercial districts | Abundant | Active |
| Mid-Levels | Transit hubs | Major | Active |
| Spires | Corporate infrastructure | Abundant | Premium |
| Spires | Nanite technology | Elite | Restricted |
| The Confluence | Nitro throughput | Highest in city | Escalating |
| New Geneva | Diplomatic infrastructure | Institutional | Active |
| European See | Church institutional authority | Theological/administrative | Active |

---

### European See

**Description:** Institutional heart of the Church of the Blessed Nitro in Europe. Administrative complex of vaulted stone ceilings, heavy wooden doors, and architectural grammar designed for deliberation over urgency. The See runs on the same nitro grid as every other building in the diocese — the hum is present but quieter, institutional rather than raw. Post-BLACKWEIR, the hum is denser.

**Discovered:** Established location (Church institutional center)

**Resources:**
- Theological library (extensive — commentaries on Book of Radiance, doctrinal review proceedings, institutional memory spanning 130+ years)
- Diocesan administrative infrastructure (secretariat, communications, intelligence office coordination with Luminarch in New Geneva)
- Resonance chapel network (312 active chapels across European See)

**Dangers:**
- Institutional suppression mechanisms (nitro-psychosis protocol: diagnose, suppress, reassign)
- Post-BLACKWEIR: 41/312 resonance chapels reporting anomalous acoustic phenomena (congregants hearing "additional voices")
- Void Witness migration (19% increase post-BLACKWEIR, congregants leaving for Nephthys's movement)

**Key Events:**
- B2 Ch 3: Malachi receives 41 diocesan reports of anomalous phenomena. Convenes council. Publishes encyclical "The Voice Is Not Wounded." Visits locked study.

**Significance:** Institutional counterpoint to Nephthys's grassroots Cathedral. The Church's administrative machinery managing the same truth it suppresses. Malachi's domain — where institutional theology is written, where the framework holds "for now."

**Current State:** Active. Managing post-BLACKWEIR resonance anomalies through pastoral framing. Encyclical distributed to 312 chapels. Framework intact but strained.

**Controlled by:** Church of the Blessed Nitro (Arch-Prelate Malachi, reports to Luminarch in New Geneva)

**Key Locations Within:**
- **Malachi's office:** Dark oak desk, floor-to-ceiling theological library, vaulted stone ceilings. Where institutional documents are written.
- **Chapter Hall:** Stone chamber, barrel-vaulted ceiling, long oak table (seats 24). Where councils convene.
- **Locked study:** Separate room at end of unused hallway. Mechanical lock, no digital access logs. Appears as "auxiliary storage" on architectural plans. Forty-three steps from Malachi's office. Bare stone walls, single desk, single lamp. Where the correspondence lives — Nephthys's letters, Malachi's unsent responses, the private theology.
- **Resonance chapel corridor:** (Referenced but not directly shown in Ch 3)

**Occupants:**
- Malachi (Arch-Prelate)
- Diocesan secretariat
- Senior clergy (14 present at council: diocesan administrators, seminary representatives, theological review board, pastoral affairs coordinator)
- Prelate Breslin (pastoral affairs coordinator, 20-year veteran)

**Atmospheric Notes:**
- Quiet by design — sound-absorbing architecture
- The hum: low vibration through desk surfaces, faint pressure behind sternum
- Post-BLACKWEIR: hum is denser, "populated" (Voss's word from congregants)
- Institutional weight expressed through architecture, furniture, vestments

---

## Lagos, Federation of African States

Lagos is the primary FAS city featured in the narrative. Lower conduit density than grid-dependent cities (New Geneva, Neo-Shanghai). Distributed infrastructure architecture — conduits visible on building facades rather than buried. Hum is present but quieter: stays in the soles, does not rise into the chest. The city that voted for the lower curve.

### FAS Ministry of Infrastructure and Atmospheric Compliance

**Description:** Four-story building on Victoria Island, Lagos. Concrete and glass, functional — "the architecture of a government that had spent its construction budget on load-bearing walls rather than holographic flags." Reading room on second floor, administrative corridor on third.

**Discovered:** B2 Ch 17, by Zeyad Al-Fahim (courtesy access)

**Key Events:**
- B2 Ch 17: Zeyad reads 40 years of FAS atmospheric compliance data. Conclusions in first paragraph — disorienting. Intelligence files brought by K. Adeyemi. Independent confirmation of nitro-suffering correlation.

**Significance:** The institutional architecture of a government that acts on what it measures. Filing architecture designed for action, not deferral. Contrast with UGC's Hall of Nations.

**Current State:** Active, functioning as designed. Minister Adaeze Obiora in charge.

**Controlled by:** Federation of African States (federal government)

**Atmospheric Notes:**
- Hum: present but quieter than New Geneva or Neo-Shanghai. Lower conduit density. Stays in soles and ankles, does not rise into chest. "The hum was something he noticed because it was less."
- Building: concrete floor transmits low-frequency vibration at reduced intensity.

---

### Ikoyi Junction, Lagos

**Description:** Commercial corridor adjacent to FAS Ministry. Conduit infrastructure is not merely visible but architectural — trunk lines along building facades in reinforced channels, clearly labeled, regularly spaced. Junction points marked with maintenance access panels showing service dates stenciled in white paint. Lower-density conduit architecture: no single trunk line carries more than 15% of district capacity. Redundant routing.

**Discovered:** B2 Ch 17, by Zeyad Al-Fahim (walked with Minister Obiora)

**Key Events:**
- B2 Ch 17: Obiora walks Zeyad through the district. Explains FAS infrastructure summit (41 years ago), Proposal B vote (14-9), distributed architecture. "We chose to be poor rather than murderous." Exchange: "Then why are you writing it?" / "Because the record should contain it." Maintenance crew visible — two workers in federal coveralls, checking conduit access panel.

**Significance:** The physical argument for the alternative model. What infrastructure looks like when designed for resilience rather than efficiency. The hum here "asked nothing." Service dates (11 days ago) contrast with Jordanian flag (9 months).

**Current State:** Active, maintained. Service dates recent.

**Controlled by:** FAS federal infrastructure authority

---

### FAS Government Guesthouse, Lagos

**Description:** Residential compound maintained by FAS Foreign Affairs office for visiting observers. Six blocks from the Ministry. Functional — desk, terminal, bed, window showing Lagos skyline at dusk. Single low-density conduit line along compound wall, junction box at corner, service date stenciled (9 days ago).

**Discovered:** B2 Ch 17, by Zeyad Al-Fahim

**Key Events:**
- B2 Ch 17: Zeyad writes the framework document (6 pages, handwritten). COURTESY badge placed on desk beside pen. Closing margin note: "The alternative exists. It is sound. It will not be adopted. The pen continues." Lamp off. "The hum continued."

**Significance:** The guesthouse is where Zeyad produces — contrast with New Geneva diplomatic residence (where he receives). The desk ritual (badge, pen, notebook) persists across three credentials and two continents.

**Current State:** Active. Zeyad present as visiting observer.

**Controlled by:** FAS Foreign Affairs office

---

### Apapa Industrial Corridor, Lagos (FAS Theater)

**Description:** Sub-grade conduit infrastructure beneath the Apapa industrial district, Lagos. Lower-density distributed grid — RCI baseline 4.2 across the eastern conduit cluster (instruments: 4.4). Conduit clusters spaced for redundancy rather than throughput. The hum is wide and shallow — not compressed. Industrial sub-grade junction network with maintenance access points and service corridors.

**Discovered:** B2 Ch 25, by Nikolai Volkov (breach response deployment)

**Key Interior Locations:**
- **Sub-grade conduit junction (breach origin):** Stage 2 breach site, 06:14 local. Lattice geometry propagating through conduit network. Two absorbed figures at junction at resolution — present, unchanged, uncategorized by FAS as casualties.
- **FAS district command center:** Permanent building, maintained. Windows. After-action filing location. Afolabi's operational base.
- **Forward staging area:** Tactical assembly point. Acoustic dampening arrays deployed from here.

**Key Events:**
- **B2 Ch 25:** Stage 2 breach, Apapa industrial corridor. FAS non-kinetic containment — acoustic dampening (counter-resonance at three points) and infrastructure severance (non-kinetic, isolation clamps). Duration 4.7 hours. RCI at contact: 38.2. RCI at resolution: 18.3 and falling. Zero secondary absorption events. Two absorbed present at resolution, uncategorized. Nikolai files honest VS-7 via free-text override: "FAS non-kinetic containment achieved stable resolution in 4.7 hours. Zero secondary absorption events. No kinetic intervention required. PCC tactical support not deployed."

**Significance:** The breach zone where the different doctrine worked. The FAS approach — observation, acoustic dampening, managed redirection — achieved stable resolution without kinetic intervention. The VS-7's dropdown had no category for what happened. The free-text override is the honest report that seeds the Ch40 court-martial arc.

**Current State:** Resolved. Absorbed figures present at junction, status unchanged.

**Controlled by:** FAS Breach Containment Division (Colonel Afolabi, Lagos district command)

---

---

### Resonance Chapel of St. Václav, Prague (European See)

**Description:** Pre-nitro Romanesque structure in Prague's old city. Walls one meter thick, grey-gold stone darkened by centuries of lamp-smoke and prayer. Arched ceiling fifteen meters above the nave — proportions calculated for choral resonance before the grid existed, before the hum had a name. The acoustic architecture was built by medieval masons who understood resonance the way institutional administrators understand governance: through accumulated practice, not theory. The Church retrofitted it: copper conduit fittings bracketed against medieval masonry with modern fasteners that look surgical against the old stone. Nitro-powered heating grid feeds through the floor — subsurface conduits carrying warmth and the global frequency simultaneously. The old building and the new infrastructure exist in the same space without being designed for each other.

**Discovered:** B2 Ch 27, by Malachi (pastoral investigation visit)

**Key Interior Locations:**
- **Western door:** Romanesque arch, inscription above in worn pre-nitro lettering: *"The stone remembers every voice that filled it. The stone does not distinguish between the living and the carried."* Malachi passes it on exit without reading it.
- **Rear alcove:** Stone recess beside the western door, partially screened by a pillar. Where Malachi observes Vespers unannounced. The Arch-Prelate's camouflage: architecture.
- **Nave:** Old wood pews, dark with use. Sixty to seventy congregants for weekday Vespers — attendance increased since the reports. Amber glow from nitro-powered sconces. Copper conduit fittings visible along walls, catching the light.
- **Altar:** Where Father Ondřej leads the service. His hands on the lectern after the harmonization. He waits before continuing — the chaplain's instinct: let the room breathe.

**Key Events:**
- **B2 Ch 27:** Malachi attends Vespers unannounced, observes from rear alcove. During Communal Harmonization, the hum through the heating grid and electrical conduits resolves into structured sound — the chapel's acoustic architecture separating something from the carrier frequency the way a prism separates light. A woman near the front presses her hands flat against the pew and says: "That is my mother. She was in Neo-Shanghai." Malachi hears it. Gives Father Ondřej the institutional framework after the service. Leaves through the western door without reading the inscription.

**Significance:** The specific site that haunts Malachi's Voice chapter (B2 Ch 38). The first time Malachi encounters the hum outside the institutional architecture he governs — no desk, no council, no encyclical, no 43-step corridor. He is in a congregation. He hears what they hear. He cannot manage it from the back of the room. The chapel's pre-nitro acoustic design amplifies what the retrofitted infrastructure carries — generosity exceeding intent. The woman's four words ("That is my mother") are what the locked correspondence cannot say in public and what the encyclicals cannot hold.

**Current State:** Active parish. Father Ondřej continuing services. Applying institutional framework. Attendance elevated.

**Controlled by:** Church of the Blessed Nitro, Prague Diocese (Father Ondřej, chaplain)

---

_Last updated: 2026-02-20_
_Updated by: B2 Ch 27 — "Prague" bible update_
