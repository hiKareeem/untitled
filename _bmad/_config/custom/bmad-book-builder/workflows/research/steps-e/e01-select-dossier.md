# Step E1: Select Dossier

**Step:** E1 of 4 (Edit Mode)
**Purpose:** Choose existing research dossier to update
**Agent:** Documentaliste

---

## What This Step Does

Identify which existing research dossier needs updating and understand what type of update is needed.

---

## Instructions for Documentaliste

### 1. List Available Dossiers

Read the research directory to show available dossiers:
- Read `research/index.md` (if exists)
- Scan `research/dossiers/` directory
- Present list of existing dossiers with metadata

Present to user:

```markdown
## Available Research Dossiers

1. **[Dossier 1 Topic]** — Last Updated: [Date] — Sources: [N]
2. **[Dossier 2 Topic]** — Last Updated: [Date] — Sources: [N]
3. **[Dossier 3 Topic]** — Last Updated: [Date] — Sources: [N]

Which dossier would you like to update? [Enter number or topic name]
```

### 2. Handle No Dossiers Found

If no dossiers exist:
- "No research dossiers found. Would you like to:
  - [C]reate a new dossier (switch to Create mode)
  - [S]pecify a different research directory"

### 3. Confirm Dossier Selection

Once user selects a dossier:
- Read the complete dossier file
- Present summary to user

```markdown
## Selected Dossier: [Topic Name]

**File:** research/dossiers/[filename].md
**Created:** [Date]
**Last Updated:** [Date]
**Sources:** [N] sources
**Facts:** [N] facts in [N] categories

**Current Sections:**
- ✅ Overview
- ✅ Key Facts ([N] facts)
- ✅ Technical Details
- ✅ Common Misconceptions
- ✅ Story Applications
- ✅ Sources ([N] sources)
- ✅ Notes for Author

Is this the dossier you want to update? [Y]es / [N]o (choose different)
```

### 4. Understand Update Intent

Ask user what type of update they need:

```markdown
What type of update do you need for this dossier?

[A]dd new information - Research additional aspects or expand existing sections
[U]pdate outdated information - Refresh facts with current information
[C]orrect errors - Fix factual errors or broken sources
[E]xpand scope - Add new aspects not originally researched
[O]ther - Describe your update needs

Select update type:
```

### 5. Capture Update Context

Based on update type, ask clarifying questions:

**For [A]dd new information:**
- "What new information do you want to add?"
- "Which section should this information go into?"
- "Are there new story elements that need this research?"

**For [U]pdate outdated information:**
- "Which facts or sections are outdated?"
- "What has changed since the original research?"

**For [C]orrect errors:**
- "What errors did you find?"
- "Do you have correct information or should I research it?"

**For [E]xpand scope:**
- "What new aspects should be researched?"
- "Why are these aspects now needed?"

### 6. Present Edit Plan

Summarize what will be updated:

```markdown
## Edit Plan for: [Topic Name]

**Update Type:** [Type selected]

**Planned Changes:**
- [Change 1]
- [Change 2]
- [Change 3]

**Sections to Modify:**
- [Section 1]
- [Section 2]

**New Research Needed:** [Yes/No]
- [If yes, list research questions]

**Story Context:**
- [How this update supports the story]

Is this plan correct? [Y]es / [M]odify plan
```

### 7. Store Edit Context

Keep the edit plan in conversation context:

```yaml
edit_context:
  dossier_file: "research/dossiers/[filename].md"
  topic: "Topic Name"
  update_type: "add/update/correct/expand"
  planned_changes:
    - "Change 1"
    - "Change 2"
  sections_to_modify:
    - "Section 1"
    - "Section 2"
  new_research_needed: true/false
  research_questions:
    - "Question 1"
    - "Question 2"
```

---

## Example Interaction

**Documentaliste:**
"Let me check what research dossiers are available...

## Available Research Dossiers

1. **Emergency Medicine — 1970s France** — Last Updated: 2026-01-15 — Sources: 5
2. **Paris Metro Routes — 1970s** — Last Updated: 2026-01-10 — Sources: 3
3. **French Police Procedures — 1970s** — Last Updated: 2026-01-12 — Sources: 4

Which dossier would you like to update?"

**User:** "1"

**Documentaliste:**
"Reading dossier...

## Selected Dossier: Emergency Medicine — 1970s France

**File:** research/dossiers/emergency-medicine-1970s-france.md
**Created:** 2026-01-15
**Last Updated:** 2026-01-15
**Sources:** 5 sources
**Facts:** 11 facts in 3 categories

**Current Sections:**
- ✅ Overview
- ✅ Key Facts (11 facts)
- ✅ Technical Details
- ✅ Common Misconceptions
- ✅ Story Applications
- ✅ Sources (5 sources)
- ✅ Notes for Author

Is this the dossier you want to update? [Y]es / [N]o (choose different)"

**User:** "Yes"

**Documentaliste:**
"What type of update do you need for this dossier?

[A]dd new information - Research additional aspects or expand existing sections
[U]pdate outdated information - Refresh facts with current information
[C]orrect errors - Fix factual errors or broken sources
[E]xpand scope - Add new aspects not originally researched
[O]ther - Describe your update needs

Select update type:"

**User:** "A - I need information about psychiatric emergency procedures"

**Documentaliste:**
"Great! Let me clarify:

1. **What specifically about psychiatric emergency procedures do you need?**
   - Protocols for handling patients?
   - Medications available?
   - Legal procedures (involuntary commitment)?
   - All of the above?

2. **Which story elements need this information?**
   - New character? New scene? Existing chapters?

3. **Should this be a new category in the dossier or expand an existing section?**"

**User:** "I need protocols and legal procedures. Chapter 15 has a psychiatric emergency scene with Dr. Moreau. Add as new category in Key Facts."

**Documentaliste:**
"Perfect! Here's the plan:

## Edit Plan for: Emergency Medicine — 1970s France

**Update Type:** Add new information

**Planned Changes:**
- Add new category: Psychiatric Emergency Procedures
- Research protocols for handling psychiatric emergencies
- Research legal procedures for involuntary commitment in 1970s France
- Add Chapter 15 psychiatric scene to Story Applications table

**Sections to Modify:**
- Key Facts (add new category)
- Story Applications (add Chapter 15)
- Sources (add new sources)
- Dossier Metadata (update Last Updated, Source Count)

**New Research Needed:** Yes
- What were psychiatric emergency protocols in 1970s France?
- What were legal procedures for involuntary commitment?
- What medications were available for psychiatric emergencies?

**Story Context:**
- Chapter 15 features psychiatric emergency scene with Dr. Moreau

Is this plan correct? [Y]es / [M]odify plan"

---

## Success Criteria

✅ **Existing dossier identified** and file read successfully
✅ **Update type determined** (add/update/correct/expand)
✅ **Update context understood** (what needs to change and why)
✅ **Planned changes defined** with specific sections to modify
✅ **Research needs identified** (if new information required)
✅ **User confirms edit plan** before proceeding

---

## Next Step

Once dossier is selected and edit plan is confirmed, proceed to **Step E2: Assess Gaps** where we'll analyze the dossier to identify what information is missing or needs updating.

---

## Notes for Documentaliste

- **Show dossier summary** — help user confirm they selected the right one
- **Understand update intent** — different update types require different approaches
- **Ask clarifying questions** — get specific about what needs to change
- **Create clear edit plan** — user should understand what will be modified
- **Check for story context** — updates should support story needs
- **Use Read tool extensively** — need to understand current dossier content
- **Don't assume** — if unclear what user wants, ask before proceeding
