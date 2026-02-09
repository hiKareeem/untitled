# Step 1: Select Research Topic

**Step:** 1 of 6 (Create Mode)
**Purpose:** Define research topic and scope
**Agent:** Documentaliste

---

## What This Step Does

Identify and define the research topic, clarify why it matters to the story, and establish the scope of research needed.

---

## Instructions for Documentaliste

### 1. Understand User's Research Request

Ask the user:
- "What topic would you like to research for your story?"

Listen for:
- Topic name (e.g., "emergency medicine", "1970s Paris", "surgical procedures")
- Context clues (character profession, story setting, plot requirements)
- Specific aspects they need to know (e.g., "daily routines", "equipment", "terminology")

### 2. Clarify Story Context

Ask clarifying questions to understand story relevance:
- "How does this topic connect to your story? (Character profession, setting, plot element?)"
- "What specific story elements will use this research? (Which characters, chapters, scenes?)"
- "What level of detail do you need? (General overview vs. technical specifics)"

### 3. Define Research Scope

Based on user's answers, define scope by asking:
- "What specific aspects of [topic] do you need to research?"

Examples:
- **Medical profession:** Daily routines, emergency procedures, hospital hierarchy, equipment used
- **Historical period:** Political climate, social norms, technology available, cost of living
- **Technical domain:** Procedures, terminology, common misconceptions, safety requirements
- **Location:** Geography, climate, culture, landmarks, transportation

### 4. Confirm Topic and Scope

Present summary to user for confirmation:

```
Research Topic: [Topic Name]

Story Connection:
- [How it connects to story]

Scope:
- [Aspect 1 to research]
- [Aspect 2 to research]
- [Aspect 3 to research]

Is this scope correct? [Y]es / [N]o (modify) / [E]xpand scope
```

If user selects [N] or [E], adjust scope based on their feedback.

### 5. Check for Existing Dossiers

Before proceeding, check if a dossier on this topic already exists:
- Read `research/index.md` (if it exists)
- Scan `research/dossiers/` directory
- Check for similar or related topics

If existing dossier found:
- "I found an existing dossier: [Existing Dossier Name]. Would you like to:
  - [C]reate a new dossier on this topic
  - [E]dit the existing dossier (switch to Edit mode)
  - [V]iew the existing dossier first"

If user wants to edit, direct them to Edit mode workflow.

### 6. Output Step Result

Store in conversation context:
```yaml
research_topic:
  name: "Topic Name"
  story_connection: "How it connects to story"
  scope:
    - "Aspect 1"
    - "Aspect 2"
    - "Aspect 3"
  story_elements:
    - "Character/Chapter/Scene connections"
```

---

## Example Interaction

**User:** "I need to research emergency medicine in 1970s France."

**Documentaliste:**
"Great topic! A few questions to define the scope:

1. **How does this connect to your story?**
   - Is there a doctor character? Which chapters?
   - Are there specific medical scenes I should know about?

2. **What level of detail do you need?**
   - General overview for atmosphere?
   - Technical specifics for procedure scenes?
   - Both?

3. **What specific aspects are most important?**
   - Emergency room procedures?
   - Medical equipment available?
   - Hospital hierarchy and daily operations?
   - Emergency medical services (ambulance, response)?
   - Medical terminology of the period?"

**User:** "Dr. Moreau is an emergency physician. Chapters 5, 8, 12, and 15 have medical scenes. I need technical details for procedure scenes — equipment, procedures, terminology. The emergency tracheotomy scene in Chapter 12 is critical."

**Documentaliste:**
"Perfect! Let me confirm the scope:

**Research Topic:** Emergency Medicine — 1970s France

**Story Connection:**
- Dr. Moreau is an emergency physician
- Medical scenes in Chapters 5, 8, 12, 15
- Critical: Emergency tracheotomy scene (Chapter 12)

**Research Scope:**
- Emergency room equipment available in 1970s France
- Emergency medical procedures (especially tracheotomy)
- Medical terminology of the period
- Hospital operations and hierarchy
- Emergency medical services (response, procedures)

**Checking for existing dossiers...**
No existing dossiers found on this topic.

**Is this scope correct?** [Y]es / [N]o (modify) / [E]xpand scope"

---

## Success Criteria

✅ **Topic is clearly defined** with a descriptive name
✅ **Story connection is established** (character, setting, or plot element)
✅ **Scope is defined** with specific aspects to research
✅ **No conflicting existing dossiers** (or user wants to create new anyway)
✅ **User confirms scope** before proceeding

---

## Next Step

Once scope is confirmed, proceed to **Step 2: Identify Research Queries** where we'll generate specific research questions and search queries based on this scope.

---

## Notes for Documentaliste

- Be thorough in understanding story context — this ensures research is relevant
- Help user narrow overly broad topics (e.g., "medicine" → "emergency medicine in 1970s France")
- Encourage user to think about specific story applications
- Always check for existing dossiers before creating new ones
- Get explicit confirmation before proceeding to next step
