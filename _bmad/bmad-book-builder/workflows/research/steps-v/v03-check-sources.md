# Step V3: Check Sources

**Step:** V3 of 4 (Validate Mode)
**Purpose:** Verify sources are reliable and accessible
**Agent:** Documentaliste

---

## What This Step Does

Validate that all sources cited in the dossier are accessible, reliable, and appropriately categorized for trustworthiness.

---

## Instructions for Documentaliste

### 1. Review Source List

From the dossier, extract complete source list:
- Source name
- Source URL
- Source reliability rating (from dossier)
- Source type (academic/professional/government/general)

Create source checklist:

```markdown
## Source Validation Checklist

**Total Sources:** [N]

**Sources to Check:**
1. [ ] [Source Name] — [URL] — Reliability: [Rating]
2. [ ] [Source Name] — [URL] — Reliability: [Rating]
3. [ ] [Source Name] — [URL] — Reliability: [Rating]
...

**Validation Checks:**
- ✓ URL accessibility (is link still working?)
- ✓ Reliability assessment (is rating accurate?)
- ✓ Source currency (is source still current?)
- ✓ Source relevance (does source actually support cited facts?)
```

### 2. Check URL Accessibility

For each source, verify URL is accessible:

**a) Attempt to access URL**
- Use WebFetch to check if URL is accessible
- Note HTTP status (accessible/redirect/broken)
- Check if content is still available (not paywalled or removed)

**b) Document accessibility status**
```yaml
url_check:
  source: "Source name"
  url: "URL"
  status: "accessible/redirect/broken/paywalled/removed"
  notes: "Additional details"
```

**c) Handle broken URLs**

If URL is broken:
```markdown
❌ **BROKEN URL:** [Source Name]
- Original URL: [URL]
- Status: [404/timeout/domain expired/etc.]
- Facts supported: [List facts that cite this source]
- Action needed: Find replacement source or verify facts independently
```

If URL redirects:
```markdown
↗️ **REDIRECT:** [Source Name]
- Original URL: [URL]
- Redirects to: [New URL]
- Status: [Still relevant/Different content/Domain changed]
- Recommendation: [Update URL/Find new source]
```

If content is paywalled:
```markdown
💰 **PAYWALLED:** [Source Name]
- URL: [URL]
- Issue: Content behind paywall (was it accessible before?)
- Recommendation: [Keep with note/Find open alternative]
```

### 3. Assess Source Reliability

For each accessible source, evaluate reliability:

**a) Identify source type**
- Academic (peer-reviewed journals, university research)
- Government/Official (government agencies, official organizations)
- Professional (industry organizations, professional publications)
- General Media (news sites, magazines)
- Personal/Blog (individual blogs, personal websites)

**b) Evaluate reliability factors**
- Author credentials and expertise
- Publication/organization reputation
- Date of publication (currency)
- Peer review status (for academic)
- Editorial standards (for media)
- Bias or conflicts of interest

**c) Assign reliability rating**
- **High:** Academic sources, government/official sources, established professional organizations
- **Medium:** Professional media, reputable news organizations, established industry publications
- **Low:** General blogs, personal websites, sources with unclear authority

**d) Compare to dossier rating**
```markdown
## Source Reliability Assessment: [Source Name]

**Dossier Rating:** [High/Medium/Low]
**Validated Rating:** [High/Medium/Low]

**Source Type:** [Academic/Government/Professional/General/Personal]

**Reliability Factors:**
- Author: [Name/credentials]
- Organization: [Name/reputation]
- Date: [Publication date]
- Peer review: [Yes/No/N/A]
- Editorial standards: [Assessment]

**Assessment:** [Agrees with dossier rating / Rating should be adjusted]

**Recommendation:** [Keep rating / Upgrade to [X] / Downgrade to [X]]
```

### 4. Verify Source Currency

Check if source information is still current:

**a) Check publication/update date**
- Note when source was published or last updated
- Compare to dossier creation date
- Assess if information might be outdated

**b) Look for updates or retractions**
- Search for newer versions of the same information
- Check if facts have been updated or corrected
- Note any retractions or corrections

**c) Document currency assessment**
```markdown
## Source Currency: [Source Name]

**Publication Date:** [Date]
**Last Updated:** [Date or "Not specified"]
**Dossier Created:** [Date]

**Currency Assessment:**
- ✅ Current (recent or timeless information)
- ⚠️ Aging (information still valid but getting old)
- ❌ Outdated (information has been superseded)

**Notes:** [Any updates or changes found]
```

### 5. Verify Source Relevance

Confirm sources actually support the facts they're cited for:

**a) Read source content (sample)**
- For key sources, read relevant sections
- Verify cited facts appear in source
- Check context matches how fact is used in dossier

**b) Check for misrepresentation**
- Does source actually say what dossier claims?
- Is context preserved or distorted?
- Are qualifiers or caveats missing?

**c) Document relevance check**
```markdown
## Source Relevance: [Source Name]

**Facts Supported by This Source:** [N] facts
1. [Fact description] — ✅ Confirmed in source / ⚠️ Partial / ❌ Not found
2. [Fact description] — ✅ Confirmed in source / ⚠️ Partial / ❌ Not found

**Content Match:** [How well source supports facts]
**Context Preserved:** [Yes/No/Partially]

**Issues:** [Any misrepresentations or context problems]
```

### 6. Track Source Validation Progress

Report progress as sources are checked:

```markdown
✅ Validated Source: [Source Name]
- URL: Accessible ✓
- Reliability: [Rating] — [Confirmed/Adjusted from [old] to [new]]
- Currency: [Current/Aging/Outdated]
- Relevance: Supports [N] facts ✓

**Progress:** [N] of [N] sources validated
```

### 7. Handle Source Issues

For each issue found, propose resolution:

**Broken URLs:**
```markdown
**Issue:** Broken URL for [Source Name]
**Impact:** Supports [N] facts
**Resolution Options:**
1. Find replacement source with same information
2. Use Internet Archive (Wayback Machine) to retrieve original
3. Verify facts independently and cite new sources
**Recommended:** [Option number]
```

**Reliability Concerns:**
```markdown
**Issue:** Source reliability questionable — [Source Name]
**Current Rating:** [High/Medium/Low]
**Concern:** [Why reliability is questioned]
**Impact:** Supports [N] facts
**Resolution Options:**
1. Downgrade reliability rating and flag facts
2. Find higher-quality replacement source
3. Verify facts with additional sources
**Recommended:** [Option number]
```

**Outdated Information:**
```markdown
**Issue:** Source contains outdated information — [Source Name]
**Published:** [Date]
**Outdated because:** [Reason]
**Impact:** Supports [N] facts
**Resolution Options:**
1. Find updated version of same source
2. Research current information and add new source
3. Keep with note about historical context
**Recommended:** [Option number]
```

### 8. Present Source Validation Summary

After checking all sources:

```markdown
## Source Validation Summary: [Topic Name]

**Sources Validated:** [N] sources

### URL Accessibility

**✅ Accessible:** [N] sources ([X]%)
**↗️ Redirected:** [N] sources
**❌ Broken:** [N] sources
**💰 Paywalled:** [N] sources

**Broken/Problematic URLs:**
1. [Source name] — [URL] — [Status]
2. [Source name] — [URL] — [Status]

### Reliability Assessment

**High Reliability:** [N] sources ([X]%)
**Medium Reliability:** [N] sources ([X]%)
**Low Reliability:** [N] sources ([X]%)

**Reliability Adjustments Recommended:**
1. [Source name] — [Old rating] → [New rating] — [Reason]

**Reliability Concerns:**
1. [Source name] — [Issue description]

### Currency Assessment

**✅ Current:** [N] sources
**⚠️ Aging but Valid:** [N] sources
**❌ Outdated:** [N] sources

**Outdated Sources:**
1. [Source name] — [Date] — [Why outdated]

### Relevance Assessment

**✅ Fully Relevant:** [N] sources
**⚠️ Partially Relevant:** [N] sources
**❌ Misrepresented:** [N] sources

**Issues Found:**
1. [Source name] — [Relevance issue]

### Overall Source Quality

**Source Quality:** [Excellent/Good/Fair/Poor]
- [X]% sources accessible and current
- [X]% sources High/Medium reliability
- [X]% sources fully relevant to cited facts

**Issues Requiring Action:** [N] issues
1. [Issue description]
2. [Issue description]

---

**Ready to generate validation report?**

[Y]es, create validation report
[R]eview specific sources (show details)
[F]ix issues now (find replacement sources)
```

---

## Example Interaction

**Documentaliste:**
"Validating sources for Emergency Medicine — 1970s France...

## Source Validation Checklist

**Total Sources:** 12

Checking URL accessibility and reliability...

---

✅ Validated Source: History of Emergency Medicine
- URL: Accessible ✓
- Reliability: High — Confirmed (professional association, authoritative)
- Currency: Current (timeless historical content)
- Relevance: Supports 3 facts ✓

✅ Validated Source: SAMU France Official History
- URL: Accessible ✓
- Reliability: High — Confirmed (official government source)
- Currency: Current (official history)
- Relevance: Supports 2 facts ✓

❌ Validated Source: Medscape Cricothyrotomy Procedure
- URL: Paywalled (requires login)
- Reliability: High — Confirmed (medical reference database)
- Currency: Current (regularly updated)
- Relevance: Supports 1 fact ✓
- **Issue:** Article now paywalled, may not be accessible to all users

✅ Validated Source: NCBI - Mechanical Ventilation History
- URL: Accessible ✓
- Reliability: High — Confirmed (academic research, peer-reviewed)
- Currency: Current (published 2015, historical content)
- Relevance: Supports 2 facts ✓

↗️ Validated Source: RadiologyInfo CT Scan History
- URL: Redirects to new domain (radiologyinfo.org moved)
- Reliability: High — Confirmed (professional medical imaging organization)
- Currency: Current (content updated regularly)
- Relevance: Supports 1 fact ✓
- **Recommendation:** Update URL to new domain

✅ Validated Source: French Medical Law Reference
- URL: Accessible ✓
- Reliability: High — Confirmed (legal/government source)
- Currency: Current (legal archive, historical regulations)
- Relevance: Supports 2 facts ✓

✅ Validated Source: History of French Psychiatric Care
- URL: Accessible ✓
- Reliability: High — Confirmed (academic research)
- Currency: Current (published 2018, historical content)
- Relevance: Supports 3 facts ✓

✅ Validated Source: Medical Protocol Archives
- URL: Accessible ✓
- Reliability: High — Confirmed (professional medical archive)
- Currency: Current (archived historical protocols)
- Relevance: Supports 2 facts ✓

✅ Validated Source: Pharmaceutical History Database
- URL: Accessible ✓
- Reliability: High — Confirmed (academic pharmaceutical history)
- Currency: Current (updated 2023)
- Relevance: Supports 2 facts ✓

⚠️ Validated Source: Medical Formulary Archive 1970s
- URL: Accessible ✓
- Reliability: Medium — Adjusted from High
- **Adjustment Reason:** Personal blog by retired pharmacist, not peer-reviewed
- Currency: Aging (blog post from 2010)
- Relevance: Supports 1 fact ✓
- **Recommendation:** Downgrade reliability rating to Medium; consider finding professional source

✅ Validated Source: SAMU Operations Manual
- URL: Accessible ✓
- Reliability: High — Confirmed (official manual)
- Currency: Current (official documentation)
- Relevance: Supports 2 facts ✓

✅ Validated Source: Medical Transport History
- URL: Accessible ✓
- Reliability: Medium — Confirmed (professional publication)
- Currency: Current (published 2020)
- Relevance: Supports 1 fact ✓

---

## Source Validation Summary: Emergency Medicine — 1970s France

**Sources Validated:** 12 sources

### URL Accessibility

**✅ Accessible:** 11 sources (92%)
**↗️ Redirected:** 1 source (should update URL)
**💰 Paywalled:** 1 source (Medscape - may limit accessibility)
**❌ Broken:** 0 sources

**URLs Needing Update:**
1. RadiologyInfo CT Scan History — Redirects to new domain, update URL recommended

**Access Concerns:**
1. Medscape Cricothyrotomy — Now requires login, still high quality but less accessible

### Reliability Assessment

**High Reliability:** 11 sources (92%)
**Medium Reliability:** 1 source (8%)
**Low Reliability:** 0 sources

**Reliability Adjustments Recommended:**
1. Medical Formulary Archive 1970s — High → Medium — Personal blog, not peer-reviewed source

### Currency Assessment

**✅ Current:** 11 sources (92%)
**⚠️ Aging but Valid:** 1 source (8%)
**❌ Outdated:** 0 sources

**Aging Sources:**
1. Medical Formulary Archive — Blog from 2010, information still valid for historical topic

### Relevance Assessment

**✅ Fully Relevant:** 12 sources (100%)
**⚠️ Partially Relevant:** 0 sources
**❌ Misrepresented:** 0 sources

All sources appropriately support the facts they're cited for.

### Overall Source Quality

**Source Quality:** Excellent
- 92% sources accessible and current
- 92% sources High reliability, 8% Medium reliability
- 100% sources relevant to cited facts
- Strong diversity: academic, government, professional, medical sources

**Issues Requiring Action:** 2 minor issues
1. Update RadiologyInfo URL to new domain (redirect works but should update)
2. Downgrade Medical Formulary Archive reliability rating from High to Medium

**Strengths:**
- Excellent source diversity (academic, government, professional)
- No broken URLs
- All sources accessible (1 paywalled but high quality)
- Strong reliability across sources

---

**Ready to generate validation report?**

[Y]es, create validation report
[R]eview specific sources (show Medscape paywall concern)
[F]ix issues now (update URL, adjust rating)"

---

## Success Criteria

✅ **All sources checked** for accessibility
✅ **Broken URLs identified** and documented
✅ **Reliability assessed** independently and compared to dossier
✅ **Currency evaluated** for each source
✅ **Relevance verified** (sources support cited facts)
✅ **Issues documented** with resolution recommendations
✅ **Overall source quality** assessed
✅ **User informed** of source validation results

---

## Next Step

Once source validation is complete, proceed to **Step V4: Generate Report** where we'll create a comprehensive validation summary and add it to the dossier.

---

## Notes for Documentaliste

- **Check EVERY source URL** — broken links are common validation issues
- **Use WebFetch** to verify URL accessibility
- **Be objective about reliability** — don't assume dossier ratings are correct
- **Document all issues** — even minor ones should be noted
- **Propose solutions** — don't just identify problems, suggest fixes
- **Consider accessibility** — paywalled sources may be high quality but less accessible
- **Note redirects** — update URLs even if redirects work
- **Verify relevance** — source should actually support the facts citing it
- **Assess currency** — old sources may be fine for historical topics
- **Report thoroughly** — source quality affects overall dossier reliability
