# Issue Template

## Issue Structure

Each identified issue follows this format:

```markdown
### ❌ [Severity]: [Issue Title]

**Location:** Chapter {N}, Scene {M}
**Category:** {technical|factual|logical}
**Claim:** {original claim text}

**Problem:**
{detailed explanation of why this is inaccurate or problematic}

**Evidence:**
{sources or reasoning that confirms the issue}

**Severity:** HIGH|MEDIUM|LOW

**Suggestion:**
{specific correction or alternative}

**Impact:**
{how this affects story credibility and reader immersion}
```

## Severity Guidelines

### HIGH Severity

**Criteria:**
- Breaks story credibility completely
- Factual impossibility or anachronism
- Professional procedure completely wrong
- Readers will definitely notice and lose trust

**Example:**
```markdown
### ❌ HIGH: Medical Procedure Impossible

**Location:** Chapter 12, Scene 3
**Category:** technical-profession-procedure
**Claim:** Marc (engineer) performs complex emergency surgery without medical training

**Problem:**
Emergency tracheotomy is a medical procedure requiring specific anatomical knowledge and training. An engineer without medical background would not have the skills to perform this safely. The procedure carries significant risk even for trained professionals.

**Evidence:**
- Medical literature: Tracheotomy requires knowledge of neck anatomy, thyroid isthmus location, cricothyroid membrane identification
- Standard emergency protocols: Only performed by medical personnel or with explicit radio instruction from emergency services
- Risk factors: Severing vital structures, bleeding, airway obstruction

**Severity:** HIGH

**Suggestion:**
Option 1: Make Marc have medical background (former medic, combat medic training)
Option 2: Have Marc assist an actual doctor who talks him through basic stabilization
Option 3: Change the scene to use Marc's engineering skills (improvising medical equipment, structural solution)

**Impact:**
Readers with medical knowledge will immediately recognize this as unrealistic. Breaks immersion and undermines story credibility.
```

### MEDIUM Severity

**Criteria:**
- Stretches believability but not impossible
- Minor technical inaccuracies
- Timeline issues that could be explained
- Some readers might notice

**Example:**
```markdown
### ⚠️ MEDIUM: Timeline Inconsistency

**Location:** Chapter 8, Scene 1
**Category:** logical-time-sequence
**Claim:** Character travels 200km in 30 minutes by car

**Problem:**
Travel time of 200km in 30 minutes requires average speed of 400km/h, which is impossible for normal car travel on public roads.

**Evidence:**
- Distance: 200km
- Time claimed: 30 minutes
- Required speed: 400km/h
- Typical highway speeds: 100-130km/h
- Realistic travel time: 2-2.5 hours

**Severity:** MEDIUM

**Suggestion:**
Option 1: Adjust time to 2 hours (consistent with highway driving)
Option 2: Reduce distance to 50km (consistent with 30-minute travel)
Option 3: Add explanation (helicopter transport, extreme emergency conditions with empty roads)

**Impact:**
Some readers will notice this timeline compression. Undermines the urgency the scene tries to establish.
```

### LOW Severity

**Criteria:**
- Minor nitpicks, polish-level issues
- Small details that don't affect credibility
- Optional corrections for perfection

**Example:**
```markdown
### 🔹 LOW: Minor Geographic Detail

**Location:** Chapter 5, Scene 2
**Category:** factual-geographic-detail
**Claim:** "The Eiffel Tower was visible from this cafe in Montmartre"

**Problem:**
While the Eiffel Tower is very tall and visible from many parts of Paris, the specific cafe location described (nestled in a narrow street with buildings on both sides) would not have a direct line of sight to the tower.

**Evidence:**
- Location: Montmartre, rue Lepic area
- Eiffel Tower visibility requires direct line of sight
- Street geography: Narrow streets with 5-6 story buildings block view

**Severity:** LOW

**Suggestion:**
Option 1: Remove the tower reference
Option 2: Change cafe location to higher elevation or wider street
Option 3: Character sees tower from a different vantage point (walks to end of street)

**Impact:**
Minor detail that most readers won't notice. Doesn't affect story credibility.
```

### INFO Level

**Criteria:**
- Verified accurate, no issue
- Confirms correctness of claim
- Builds confidence in story accuracy

**Example:**
```markdown
### ✅ INFO: Medical Tool Usage Verified

**Location:** Chapter 12, Scene 3
**Category:** technical-tool-usage
**Claim:** Use of specific surgical instruments (hemostat, scalpel, suction device)

**Verification:**
All instruments listed are appropriate for emergency tracheotomy procedure:
- Hemostat: Used to clamp blood vessels and control bleeding
- Scalpel: Used for initial incision
- Suction device: Used to clear blood and fluids for visibility

**Source:**
- Emergency medicine reference documentation
- Standard surgical instrument sets for tracheotomy

**Status:** Verified accurate
```
