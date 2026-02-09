# Source Evaluation Guide

**Purpose:** Help Documentaliste and authors evaluate the reliability of research sources.

---

## Source Reliability Hierarchy

### Tier 1: Academic Sources (Highest Reliability)

**Examples:**
- Peer-reviewed journal articles
- University publications and research papers
- Expert books published by academic presses
- Government research institutions
- Professional medical/scientific organizations

**Why reliable:**
- Peer review process
- Expert authorship
- Citation of sources
- Methodological rigor

**When to use:**
- Critical facts that impact plot accuracy
- Technical or scientific details
- Historical facts and dates
- Medical/legal procedures

**How to identify:**
- .edu or .gov domains
- Author credentials listed
- References/bibliography included
- Published by known academic institution

---

### Tier 2: Media Sources (Medium-High Reliability)

**Examples:**
- Reputable news outlets (NYT, BBC, Reuters, AP)
- Established magazines (National Geographic, Scientific American)
- Official organizational websites
- Documentary films from reputable producers
- Expert interviews

**Why generally reliable:**
- Fact-checking processes
- Editorial standards
- Accountability to reputation
- Expert consultation

**Cautions:**
- May simplify complex topics
- May have editorial bias
- Verify technical details elsewhere
- Check publication date for currency

**When to use:**
- General background information
- Cultural and social context
- Recent events and trends
- Interviews with practitioners

**How to identify:**
- Known publication name
- Author byline present
- Date of publication clear
- Professional presentation

---

### Tier 3: Blog/Forum Sources (Use with Caution)

**Examples:**
- Personal blogs
- Reddit/forum discussions
- Social media posts
- Self-published articles
- Anonymous sources

**Why less reliable:**
- No editorial oversight
- No peer review
- Potential for misinformation
- Personal bias/experience only

**When acceptable:**
- First-person experiences/perspectives
- Cultural insights from community members
- Niche hobby/profession details
- Initial leads (must verify elsewhere)

**Required safeguards:**
- ⚠️ Mark as "Needs confirmation"
- Cross-reference with Tier 1 or 2 sources
- Use only for color/flavor, not critical facts
- Note the personal/anecdotal nature

**Red flags:**
- No author attribution
- Extreme/sensational claims
- No sources cited
- Poor grammar/presentation
- Advertising-heavy sites

---

## Handling Source Contradictions

**When sources disagree:**

1. **Check tier hierarchy**
   - Academic > Media > Blog
   - Newer publication > Older (for changing fields)

2. **Document both versions**
   - Mark as "⚠️ Contradiction" in facts section
   - List both claims with sources
   - Note the reliability tier of each source

3. **Present to author**
   ```markdown
   - **Fact:** [Topic]
     - **Version A:** [Claim from Source 1]
       - Source: [Academic source, 2020]
       - Verification: ✅ Verified
     - **Version B:** [Claim from Source 2]
       - Source: [Blog source, 2018]
       - Verification: ⚠️ Contradiction (lower tier source)
     - **Recommendation:** Use Version A (higher tier source)
   ```

4. **Let author decide**
   - Story needs may trump strict accuracy
   - Fiction requires "believable" not "perfect"
   - Author may choose dramatic version with caveat

---

## Cross-Referencing Standards

**Minimum verification requirements:**

**Critical facts** (affects plot logic):
- 2+ Tier 1 sources OR
- 3+ Tier 2 sources OR
- 1 Tier 1 + 2 Tier 2 sources

**Standard facts** (background details):
- 1 Tier 1 OR 2 Tier 2 sources OR
- 1 Tier 2 + 1 Tier 3 (with confirmation note)

**Background color** (flavor/atmosphere):
- 1 Tier 2 source OR
- 2 Tier 3 sources (mark "anecdotal")

---

## Source Freshness

**Check publication dates:**

**Time-sensitive topics** (technology, medicine, law):
- Prefer sources from last 5 years
- Note if using older source: "Historical context only"

**Historical topics**:
- Older scholarly sources acceptable
- Check for recent revisionist scholarship

**Evergreen topics** (basic science, geography):
- Date less critical
- Still verify URL active during validation

---

## Special Cases

### Wikipedia
**Tier:** 2.5 (Medium)

**Appropriate use:**
- Starting point for overview
- Finding primary sources (check references)
- General background

**Not appropriate for:**
- Direct citation as primary source
- Critical facts without verification

**Best practice:**
- Use Wikipedia references section
- Cite the original sources, not Wikipedia

---

### Expert Interviews / Personal Communication
**Tier:** 1-2 (depends on expert credentials)

**When acceptable:**
- Expert has verifiable credentials
- Topic is their specialty
- Document their title/affiliation

**Documentation format:**
```markdown
- **Source:** Dr. Jane Smith, Professor of Emergency Medicine, UCLA
- **Type:** Personal communication / Published interview
- **Date:** 2024-01-15
- **Verification:** ✅ Expert credentials verified
```

---

### Fiction/Media as Research
**Tier:** 3 (Use only as cultural artifact)

**When acceptable:**
- Researching cultural perceptions
- Understanding common tropes
- Noting what NOT to copy

**Not acceptable for:**
- Factual accuracy
- Technical procedures
- Historical events

**Note format:**
```markdown
- **Cultural Reference:** [Movie/show] portrays [profession] as [x]
- **Reality Check:** Actual [profession] is [y] (Source: [Tier 1/2 source])
```

---

## Red Flags for Unreliable Sources

🚩 **Immediate disqualification:**
- No author attribution
- No date
- Broken English (unless researching non-English culture)
- Excessive ads/popups
- Conspiracy theory language
- "Big [Industry] doesn't want you to know"
- Anonymous sources making medical/legal claims

⚠️ **Use with extreme caution:**
- Single source for major claim
- Emotionally charged language
- Lack of citations
- Commercial bias (selling product)
- Outdated information (>10 years for technical topics)

---

## Documentaliste Workflow Integration

**During c03-web-research.md:**
1. Identify source tier as you research
2. Prioritize Tier 1 sources
3. Use Tier 2 for breadth
4. Use Tier 3 only when noted with caution
5. Stop after 5 quality Tier 1-2 sources (unless gaps remain)

**During e03-gather-new-info.md:**
1. Assess tier of new sources
2. Replace lower-tier sources if higher-tier found
3. Note upgrades in dossier

**During v02-verify-facts.md:**
1. Spot-check 3-5 critical facts
2. Verify source tier appropriate for fact priority
3. Flag any Tier 3 sources for upgrade

**During v03-check-sources.md:**
1. Verify URLs still active
2. Check if newer sources available
3. Note if source tier changed (e.g., blog now has peer review)

---

*Use this guide every time you evaluate sources for research dossiers.*
