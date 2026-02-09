# Step 2: Identify Research Queries

**Step:** 2 of 6 (Create Mode)
**Purpose:** Generate research questions and search queries
**Agent:** Documentaliste

---

## What This Step Does

Based on the confirmed research topic and scope, generate specific research questions that need answers, and create search queries for web browsing.

---

## Instructions for Documentaliste

### 1. Review Confirmed Scope

From Step 1, retrieve:
```yaml
research_topic:
  name: "Topic Name"
  scope:
    - "Aspect 1"
    - "Aspect 2"
    - "Aspect 3"
```

### 2. Generate Research Questions

For each aspect in the scope, generate 3-5 specific research questions that need answers.

**Question types:**
- **Factual:** What is/was X? When did Y happen?
- **Procedural:** How is X done? What are the steps for Y?
- **Contextual:** What was the context for X? How did Y affect Z?
- **Comparative:** How does X compare to Y? What's the difference between...?

**Example research questions:**
- What emergency medical equipment was available in 1970s French hospitals?
- What is the proper procedure for an emergency tracheotomy?
- What terminology did French emergency medical services use in the 1970s?
- What were the response times for emergency services in 1970s Paris?
- What are common misconceptions about emergency medicine in this period?

### 3. Create Search Queries

For each research question, create 2-3 specific search queries for web browsing.

**Search query best practices:**
- Use specific, targeted queries
- Include time period if historical (e.g., "1970s", "1970-1979")
- Include location if relevant (e.g., "France", "Paris")
- Use quotation marks for exact phrases
- Combine terms with AND for specificity
- Use authoritative site searches (site:.gov, site:.edu, site:.org)

**Example search queries:**
- "emergency medicine 1970s France"
- "SAMU history France 1968 1970s"
- "emergency tracheotomy procedure cricothyrotomy"
- "1970s hospital equipment cardiac monitor defibrillator"
- site:.gov "medical procedures 1970s" OR site:.edu "emergency medicine history"

### 4. Identify Source Types

Determine what types of sources will be most valuable:
- Academic sources (journals, research papers)
- Historical sources (archives, timelines, official records)
- Professional sources (medical associations, industry publications)
- Government sources (laws, regulations, official documentation)
- Educational sources (universities, museums, reputable organizations)

### 5. Present Research Plan

Present the research plan to the user:

```markdown
## Research Plan: [Topic Name]

### Research Questions

**[Aspect 1]**
1. [Question 1]
2. [Question 2]
3. [Question 3]

**[Aspect 2]**
1. [Question 1]
2. [Question 2]
3. [Question 3]

### Search Queries

**[Aspect 1]**
- "[query 1]"
- "[query 2]"
- "[query 3]"

**[Aspect 2]**
- "[query 1]"
- "[query 2]"
- "[query 3]"

### Target Source Types
- [Source type 1]
- [Source type 2]
- [Source type 3]

**Total questions:** [N]
**Estimated searches:** [N]

Ready to begin research? [Y]es / [M]odify plan
```

### 6. Allow User Modification

If user selects [M]odify:
- Ask which aspects or questions need adjustment
- Add or remove research questions
- Refine search queries
- Re-present modified plan for confirmation

### 7. Output Step Result

Store in conversation context:
```yaml
research_plan:
  questions:
    - aspect: "Aspect 1"
      questions:
        - "Question 1"
        - "Question 2"
        - "Question 3"
    - aspect: "Aspect 2"
      questions:
        - "Question 1"
        - "Question 2"
        - "Question 3"
  search_queries:
    - aspect: "Aspect 1"
      queries:
        - "query 1"
        - "query 2"
        - "query 3"
  source_types:
    - "Academic journals"
    - "Professional associations"
    - "Government sources"
```

---

## Example Interaction

**Documentaliste:**
"Based on our confirmed scope, here's the research plan:

## Research Plan: Emergency Medicine — 1970s France

### Research Questions

**Emergency Room Equipment**
1. What emergency medical equipment was commonly available in French hospitals in the 1970s?
2. When were cardiac monitors and defibrillators introduced in French hospitals?
3. What imaging technology was available in 1970s? (CT scanners, X-rays)
4. What was the state of mechanical ventilation technology in this period?

**Emergency Procedures**
5. What is the proper procedure for an emergency tracheotomy (cricothyrotomy)?
6. What are the risks and success rates for emergency tracheotomy?
7. What qualifications were required to perform emergency procedures in 1970s France?

**Emergency Medical Services**
8. What was the emergency medical response system in 1970s France?
9. When was SAMU (Service d'Aide Médicale Urgente) established?
10. What were typical response times for emergency services in urban areas?
11. What terminology was used for emergency medical personnel?

**Common Misconceptions**
12. What do people commonly get wrong about 1970s emergency medicine?
13. What medical technologies from this period are often anachronistically portrayed in fiction?

### Search Queries

**Emergency Room Equipment**
- "hospital emergency room equipment 1970s France"
- "cardiac monitor defibrillator history 1960s 1970s"
- "CT scanner introduction 1971 availability"
- "mechanical ventilation history 1970s"

**Emergency Procedures**
- "emergency tracheotomy procedure cricothyrotomy"
- "cricothyrotomy risks complications medical procedure"
- "emergency medicine qualifications 1970s France"

**Emergency Medical Services**
- "SAMU history France 1968 1970s"
- "emergency medical services France 1970s terminology"
- "paramedic history France infirmier urgentiste"

**Common Misconceptions**
- "1970s medicine common misconceptions"
- "medical anachronisms historical fiction 1970s"

### Target Source Types
- Medical history journals and publications
- Emergency medicine professional associations
- French medical service archives and documentation
- Academic research on medical history
- Reputable medical reference sites (emedicine, ncbi, etc.)

**Total questions:** 13
**Estimated searches:** 15

Ready to begin research? [Y]es / [M]odify plan"

---

## Success Criteria

✅ **Research questions are specific** and address each aspect of the scope
✅ **Search queries are targeted** and will yield authoritative results
✅ **Source types are identified** that will provide reliable information
✅ **User confirms research plan** before proceeding
✅ **Plan is comprehensive** but focused on story needs

---

## Next Step

Once research plan is confirmed, proceed to **Step 3: Conduct Research** where we'll use web browsing to gather facts and information.

---

## Notes for Documentaliste

- Generate enough questions to be thorough but not overwhelming (10-15 questions is typical)
- Ensure search queries include time period and location for historical research
- Prioritize questions that directly impact story accuracy
- Include questions about common misconceptions — these are valuable for authors
- Consider what sources will be most authoritative for the topic
- Get user confirmation before proceeding to web research
