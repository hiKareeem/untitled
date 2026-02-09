# Step E3: Gather New Info

**Step:** E3 of 4 (Edit Mode)
**Purpose:** Research additional details to fill gaps
**Agent:** Documentaliste

---

## What This Step Does

Conduct focused web research to gather new information, update outdated facts, correct errors, and replace broken sources identified in Step E2.

---

## Instructions for Documentaliste

### 1. Review Gap Analysis

From Step E2, retrieve:
- Research questions for each gap
- Identified gaps (missing info, outdated facts, errors, broken sources)
- Estimated source needs
- Target sections for new information

### 2. Conduct Targeted Web Research

For each research question from gap analysis:

**a) Execute focused searches**
- Use web browsing to search for each research question
- Prioritize authoritative sources (academic, professional, government, legal)
- Look specifically for information that fills the identified gaps
- Focus on the time period/context from original dossier

**b) Gather new facts**
- Extract facts that directly answer research questions
- Note specific details (dates, procedures, terminology, legal references)
- Capture quantitative data when available
- Document any new contradictions or uncertainties

**c) Verify against existing dossier**
- Check that new facts don't contradict existing verified facts
- If contradiction found, document both versions with sources
- Note which source is more reliable

**d) Collect source references**
- Record URL for each new source
- Note source type and reliability
- Capture publication/update date
- Note author/organization

### 3. Handle Different Update Types

**For Adding New Information:**
- Focus research on new aspects identified in gap analysis
- Gather 3-5 facts per new aspect minimum
- Ensure facts integrate well with existing dossier structure

**For Updating Outdated Information:**
- Search for current information on outdated facts
- Compare new findings with old facts
- Note what has changed and why
- Keep old facts if still historically accurate but add context

**For Correcting Errors:**
- Research the correct information thoroughly
- Verify corrections with multiple sources
- Document why original fact was incorrect
- Note source of correction

**For Replacing Broken Sources:**
- Search for the same information from alternative sources
- Verify information matches original fact
- If information has changed, note the update
- Add new source with same or better reliability

### 4. Track Research Progress

After researching each gap, report progress:

```markdown
✅ Researched: [Gap/Aspect name]
- Found [N] new facts from [N] sources
- Sources: [list of source types]
- Key findings: [brief summary]
- Integration: [Which section(s) this will update]
- ⚠️ Issues noted: [if any contradictions or uncertainties]
```

### 5. Handle Contradictions

When new research contradicts existing dossier facts:

```markdown
⚠️ **Contradiction Found**

**Existing Fact (from dossier):**
- [What current dossier says]
- Source: [Existing source]
- Reliability: [Original reliability rating]

**New Research Finding:**
- [What new sources say]
- Source: [New source]
- Reliability: [New reliability rating]

**Recommended Resolution:**
- [Which version to use based on source reliability]
- [How to handle in dossier: replace, add note, mark contradiction]

**Should I:**
[R]eplace old fact with new fact
[K]eep both and mark as contradiction
[I]nvestigate further
```

### 6. Check Sufficiency

After researching each gap area, ask user:

```markdown
**Research Progress: [Gap/Aspect Name]**

✅ Found [N] new facts from [N] sources
✅ Research questions answered: [N] of [N]

**Coverage:**
- Question 1: ✅ Answered
- Question 2: ✅ Answered
- Question 3: ⚠️ Partial answer
- Question 4: ✅ Answered

**Should I:**
[C]ontinue researching (more sources/depth)
[M]ove to next gap
[S]top research (sufficient for this gap)
```

This prevents over-researching and maintains focus.

### 7. Organize New Findings

Structure new findings by target section:

```yaml
new_research_findings:
  section_key_facts:
    new_category: "Psychiatric Emergency Procedures"
    facts:
      - fact: "Fact description"
        sources:
          - url: "https://source-url"
            type: "legal/medical/historical"
            reliability: "high/medium/low"
            date: "publication date"
        verification: "verified / needs_confirmation"
        notes: "additional context"

  section_story_applications:
    new_entries:
      - story_element: "Chapter 15 psychiatric scene"
        application: "How research applies"

  section_sources:
    new_sources:
      - name: "Source name"
        url: "URL"
        type: "Source type"
        reliability: "High/Medium/Low"

  section_notes_for_author:
    new_warnings:
      - "New critical warning"
    new_recommendations:
      - "New recommendation"
```

### 8. Present Research Summary

After completing all gap research, present comprehensive summary:

```markdown
## Research Summary: [Topic Name] — Gap Filling

### New Information Gathered

**[Gap/Aspect 1]:** [N] new facts from [N] sources
**[Gap/Aspect 2]:** [N] new facts from [N] sources
**[Gap/Aspect 3]:** [N] new facts from [N] sources

**Total:** [N] new facts from [N] new sources

### New Sources Consulted

1. [Source 1] — [Type] — [Reliability]
2. [Source 2] — [Type] — [Reliability]
3. [Source 3] — [Type] — [Reliability]
...

### Contradictions/Issues Found

- [Contradiction 1] — [How handled]
- [Issue 1] — [How resolved]

### Updated Source Count

- Original sources: [N]
- New sources: [N]
- **Total sources:** [N]

### Sections to Update

- ✅ Key Facts (add [N] facts in [N] categories)
- ✅ Story Applications (add [N] entries)
- ✅ Sources (add [N] sources)
- ✅ Notes for Author (add [N] warnings/recommendations)
- ✅ Dossier Metadata (update Last Updated, Source Count)

### Key New Findings

[Highlight 2-3 most important new facts]

---

**Ready to update dossier with new information?**

[Y]es, proceed to update
[R]esearch more (specify what)
[M]odify findings (edit before updating)
```

---

## Example Interaction

**Documentaliste:**
"Beginning gap-filling research for Emergency Medicine — 1970s France...

---

✅ Researched: Psychiatric Emergency Protocols
- Found 4 facts from 3 sources
- Sources: French medical law reference, Psychiatric care history, Medical protocol archive
- Key findings: Specific legal procedures existed; physician authorization required for involuntary commitment
- Integration: Key Facts (new category)
- No contradictions

✅ Researched: Psychiatric Medications 1970s
- Found 3 facts from 2 sources
- Sources: Pharmaceutical history database, Medical formulary archive
- Key findings: Chlorpromazine, Haloperidol commonly used; benzodiazepines available
- Integration: Key Facts (new category) and Technical Details
- No contradictions

✅ Researched: Psychiatric Patient Transport
- Found 2 facts from 2 sources
- Sources: SAMU operations manual, Medical transport history
- Key findings: Regular ambulance used; police involvement for violent cases
- Integration: Key Facts (new category)
- No contradictions

⚠️ **Contradiction Found**

**Existing Fact (from dossier):**
- Emergency response times: 10-15 minutes in urban Paris
- Source: SAMU operations guide
- Reliability: High

**New Research Finding:**
- Psychiatric consultation response: 30-60 minutes
- Source: French psychiatric services history
- Reliability: High

**Recommended Resolution:**
- Both are accurate — different services, different response times
- Add note in dossier distinguishing emergency medical response (10-15 min) from psychiatric consultation (30-60 min)

**Should I:**
[K]eep both and add clarification note ✓

---

## Research Summary: Emergency Medicine — 1970s France — Gap Filling

### New Information Gathered

**Psychiatric Emergency Protocols:** 4 facts from 3 sources
**Psychiatric Medications:** 3 facts from 2 sources
**Psychiatric Patient Transport:** 2 facts from 2 sources

**Total:** 9 new facts from 7 new sources

### New Sources Consulted

1. French Medical Law Reference — Legal/Government — High
2. History of French Psychiatric Care — Academic — High
3. Medical Protocol Archives — Professional — High
4. Pharmaceutical History Database — Academic — High
5. Medical Formulary Archive 1970s — Professional — Medium
6. SAMU Operations Manual — Official — High
7. Medical Transport History — Professional — Medium

### Contradictions/Issues Found

- Response times: Clarified difference between emergency medical (10-15 min) vs psychiatric consultation (30-60 min)

### Updated Source Count

- Original sources: 5
- New sources: 7
- **Total sources:** 12

### Sections to Update

- ✅ Key Facts (add 9 facts in 1 new category: "Psychiatric Emergency Procedures")
- ✅ Technical Details (expand with medication details)
- ✅ Story Applications (add Chapter 15 psychiatric scene)
- ✅ Sources (add 7 sources)
- ✅ Notes for Author (add warnings about psychiatric procedure accuracy)
- ✅ Dossier Metadata (update Last Updated: 2026-01-25, Source Count: 12)

### Key New Findings

1. **Legal procedures clear:** Physician authorization required for involuntary commitment in 1970s France
2. **Medication options:** Chlorpromazine and Haloperidol were standard psychiatric emergency medications
3. **Transport protocols:** Regular ambulance used for cooperative patients; police involvement for violent cases

---

**Ready to update dossier with new information?**

[Y]es, proceed to update
[R]esearch more (specify what)
[M]odify findings (edit before updating)"

---

## Success Criteria

✅ **All research questions from gap analysis addressed**
✅ **Multiple sources consulted** (minimum 2-3 per gap area)
✅ **Sources are authoritative** (academic/professional/legal preferred)
✅ **Facts verified** across sources when possible
✅ **Contradictions documented** and resolved
✅ **New findings organized** by target section
✅ **User confirms research is sufficient** before updating dossier

---

## Next Step

Once new research is complete and confirmed, proceed to **Step E4: Update Dossier** where we'll integrate the new findings into the existing dossier file.

---

## Notes for Documentaliste

- **Focus on gaps** — research only what's needed, don't expand scope
- **Maintain dossier quality** — new sources should match existing reliability
- **Check for contradictions** — new info may conflict with existing facts
- **Be efficient** — Edit mode should be faster than Create mode
- **Document thoroughly** — every new fact needs source citation
- **Respect original dossier** — preserve existing structure and verified facts
- **Think integration** — new info should blend seamlessly with existing content
- **Flag issues early** — if contradictions found, involve user in resolution
- **Stay story-focused** — research should support specific story needs
