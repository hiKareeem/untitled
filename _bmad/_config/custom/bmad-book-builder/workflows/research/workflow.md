# Workflow: Research

**Module:** bmad-book-builder
**Agent:** Documentaliste (Research & Fact Specialist)
**Type:** Tri-Modal (Create/Edit/Validate)
**Web Browsing:** Required

---

## Purpose

Create and manage research dossiers for story topics requiring factual accuracy - professions, locations, historical periods, technical domains, etc.

Research dossiers centralize factual information with verified sources, enabling authors to write with confidence and maintain consistency across the story.

---

## When to Use This Workflow

- **During Foundation** - Research worldbuilding topics before writing
- **While writing** - Create dossiers for technical scenes requiring accuracy
- **During revision** - Verify facts with existing dossiers
- **When feedback flags issues** - Research to address accuracy concerns

---

## Mode Selection

**Which mode do you need?**

**Create** - Start a new research dossier on a topic
**Edit** - Update an existing dossier with new information
**Validate** - Verify accuracy and sources of an existing dossier

---

## Workflow Modes

### Create Mode
Create a new research dossier from scratch through guided discovery and web research.

**Steps:**
1. Topic Identification - Choose research topic and scan for duplicates
2. Scope Definition - Define research questions and depth needed
3. Web Research - Conduct focused web research (5-10 sources)
4. Organize Facts - Structure findings into categories
5. Create Dossier - Generate organized research document
6. Link to Story - Connect research to story elements

**Outputs:**
- `{project-root}/research/dossiers/{topic-name}.md`
- Updated `{project-root}/research/index.md`

---

### Edit Mode
Update an existing research dossier with new information or fill gaps.

**Steps:**
1. Select Dossier - Choose existing dossier to update
2. Assess Gaps - Identify missing or outdated information
3. Gather New Info - Research additional details
4. Update Dossier - Add new findings to existing dossier

**Outputs:**
- Updated dossier file
- Updated metadata (Last Updated date, Source Count)

---

### Validate Mode
Verify accuracy and reliability of an existing research dossier.

**Steps:**
1. Select Dossier - Choose dossier to validate
2. Verify Facts - Spot-check key facts for accuracy
3. Check Sources - Verify sources are reliable and accessible
4. Generate Report - Add validation summary to dossier

**Outputs:**
- Validation History section added to dossier
- Flagged issues (dead URLs, contradictions, reliability concerns)

---

## Quality Standards

**Minimum Requirements for Dossiers:**
- ✅ At least 3 reliable sources
- ✅ At least 10 verified facts organized in categories
- ✅ At least 1 link to story element (character, scene, chapter)
- ✅ Template 100% completed (all sections filled)
- ✅ Sources include dates and URLs

**Source Reliability Priority:**
Academic/Official > Professional Media > General Media > Blog/Personal

---

## Scope Control

To avoid research rabbit holes:
- User checkpoint before web research (after scope definition)
- Target 5-10 sources maximum
- Agent proposes "sufficient research" after 5 quality sources
- Focus: Answer the scope questions, not exhaustive coverage

---

## Handling Source Conflicts

When sources contradict:
1. Document both versions with sources
2. Mark as "⚠️ Contradiction" in facts section
3. Apply reliability priority (academic beats blog)
4. Let author decide which version to use

---

## Integration with Other Workflows

- **Reality-Check** - Uses research dossiers for fact verification
- **Foundation** - Can trigger research for worldbuilding topics
- **Chapter-Write** - References dossiers during writing
- **Character-Keeper** - Links profession/background research to characters

---

## Entry Point

Based on your mode selection, proceed to:

- **Create Mode:** → `steps-c/c01-topic-identification.md`
- **Edit Mode:** → `steps-e/e01-select-dossier.md`
- **Validate Mode:** → `steps-v/v01-select-dossier.md`

---

## Reference Files

- **Dossier Template:** `data/template-dossier.md`
- **Source Evaluation Guide:** `data/source-evaluation.md`
- **Example Dossier:** `data/example-dossier.md` (Emergency Medicine 1970s)
