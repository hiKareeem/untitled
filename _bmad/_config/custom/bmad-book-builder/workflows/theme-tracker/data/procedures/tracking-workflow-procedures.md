# Theme Tracker Workflow Procedures

Complete procedural guide for the theme tracking workflow from data loading through verification.

## Workflow Overview

The Theme Tracker workflow analyzes chapter content for thematic elements, character emotions, and character development through a thematic lens. It maintains persistent tracking files across all chapters.

**6 Steps:**
1. Load Chapter and Tracking Data
2. Identify Themes
3. Map Emotions
4. Analyze Arc + CHECKPOINT
5. Update Progression
6. Verify Consistency

**Output Files:**
- `tracking/themes.md` - Master theme tracking
- `tracking/emotions.md` - Master emotion tracking
- `tracking/chapter-{XX}-themes.md` - Per-chapter analysis

---

## Step 1: Load Chapter and Tracking Data

### Objective
Load chapter content, Living Bible, and existing tracking data - initializing tracking files if they don't exist.

### Prerequisites
- User provides chapter path and number
- Project folder accessible

### Procedure

#### 1.1 Request Chapter Information

**Prompt user for:**
1. Chapter path (file or folder location)
2. Chapter number (integer)

**Store in context:**
- `chapterPath` - path to chapter file
- `chapterNumber` - chapter number

#### 1.2 Load Chapter Content

**Action:** Read chapter file from `chapterPath`

**If file not found:**
- Inform user of error
- Request path verification
- Return to step 1.1

**If successful:**
- Confirm chapter loaded
- Note approximate word count
- Store content in context

#### 1.3 Load Living Bible

**Search locations in order:**
1. `{project_folder}/living-bible.md`
2. `{project_folder}/docs/living-bible.md`
3. `{project_folder}/bible/living-bible.md`

**If not found:**
- Warn user that tracking will be limited
- Ask if they want to continue
  - IF yes: Continue with limited tracking
  - IF no: Request Living Bible path

**If found:**
- Load Living Bible
- Extract theme definitions for reference
- Confirm loaded

#### 1.4 Verify Tracking Folder Structure

**Check:** Does `{project_folder}/tracking/` exist?

**If no:** Create folder and confirm

#### 1.5 Load or Initialize Tracking Files

**For themes.md:**

Check if `{project_folder}/tracking/themes.md` exists:

- **If exists:**
  - Load file
  - Count tracked themes
  - Confirm loaded

- **If not exists:**
  - Initialize from `data/theme-template.md`
  - Create file with template structure
  - Confirm initialized

**For emotions.md:**

Check if `{project_folder}/tracking/emotions.md` exists:

- **If exists:**
  - Load file
  - Count tracked characters
  - Confirm loaded

- **If not exists:**
  - Initialize from `data/emotion-template.md`
  - Create file with template structure
  - Confirm initialized

**For chapter-{XX}-themes.md:**

Check if `{project_folder}/tracking/chapter-{chapterNumber}-themes.md` exists:

- **If exists:**
  - Warn that analysis will be updated
  - Load existing analysis
  - Confirm

- **If not exists:**
  - Note this is new analysis
  - Proceed

#### 1.6 Summarize Loaded Data

**Present summary table:**

```
| Élément | Statut |
|---------|--------|
| Chapter {N} | ✅ Chargé |
| Living Bible | {status} |
| themes.md | {status} |
| emotions.md | {status} |
| Previous analysis | {exists/new} |
```

**List reference themes** (if Living Bible loaded)
**List tracked characters** (if emotions.md exists)

#### 1.7 Auto-Proceed

**Action:** Automatically proceed to Step 2

---

## Step 2: Identify Themes

### Objective
Detect which Living Bible themes are present in chapter and document how they appear with evidence.

### Prerequisites
- Step 1 completed
- Chapter content loaded
- Living Bible themes available

### Procedure

#### 2.1 Review Available Themes

**List all Living Bible themes:**
- Theme name
- Core question
- Key indicators to look for

#### 2.2 Scan Chapter for Theme Presence

**For EACH Living Bible theme:**

**Search for indicators:**
- Direct mentions of theme concepts
- Situations embodying theme's tension
- Character actions relating to theme
- Dialogue referencing theme questions
- Symbolic elements connected to theme

**Document findings:**
- If found: Note specific passages/moments
- If not found: Mark as "Not present"

#### 2.3 Classify Theme Presence

**For each detected theme, classify:**

**Strong Presence:**
- Central to chapter events
- Multiple scenes engage with theme
- Character decisions driven by theme tension

**Moderate Presence:**
- Present but not central
- One or two clear moments
- Supports other themes or plot

**Background Presence:**
- Subtly present
- Indirectly referenced
- Maintains continuity without focus

#### 2.4 Document Theme Findings

**For EACH theme found:**

```markdown
### [Theme Name]

**Niveau de présence:** [Strong/Moderate/Background]

**Comment il apparaît:**
[Description of manifestation in chapter]

**Moments clés:**
- [Moment 1 with reference]
- [Moment 2]

**Citations ou passages révélateurs:**
> "[Quote demonstrating theme]"

**Progression depuis le chapitre précédent:**
[How theme advanced since last chapter, if tracking exists]
```

#### 2.5 Identify New Theme Elements

Check if chapter introduces:
- New aspects of existing themes
- New character-theme connections
- Shifts in theme tension

**Document under "Nouveaux éléments thématiques"**

#### 2.6 Check for Absent Expected Themes

**If theme strongly present in recent chapters but absent here:**
- Note under "Thèmes attendus mais absents"
- List theme, previous presence, current absence
- Note: This isn't necessarily a red flag

#### 2.7 Present Theme Summary

**Summary table:**

```
| Thème | Présence | Moments clés |
|-------|----------|--------------|
| [Theme 1] | Strong | [Description] |
| [Theme 2] | Moderate | [Description] |
```

**List themes not present**
**List new developments**

#### 2.8 User Confirmation

**Present menu:**
- [C] Continuer vers l'analyse émotionnelle

**Wait for user input before proceeding**

---

## Step 3: Map Emotions

### Objective
Track emotional beats of each character throughout chapter - states, triggers, expressions, impacts.

### Prerequisites
- Step 2 completed
- Chapter content loaded
- Theme findings available

### Procedure

#### 3.1 Identify Characters in Chapter

**List all significant characters:**
- Name
- Role in chapter (POV, supporting, minor)
- Starting emotional state (if evident)

**Include:** POV characters, speaking roles, meaningful actions
**Exclude:** Background characters, nameless crowd members

#### 3.2 Track Emotional Beats Per Character

**For EACH significant character:**

**Scan chapter for emotional moments:**
- Direct emotional descriptions
- Physical indicators
- Dialogue tone and content
- Actions revealing emotional state
- Reactions to events/characters

**For each emotional beat found:**

```markdown
### [Character Name]

**Beat 1:**
- **État émotionnel:** [Emotion name]
- **Déclencheur:** [Trigger]
- **Expression:** [How shown]
- **Impact sur les autres:** [Effect]

**Beat 2:**
- [Same structure]
```

#### 3.3 Map Emotional Trajectory

**For characters with multiple beats:**

**Format:**
[Character]: [Starting state] → [Key shift] → [Ending state]

**Example:**
Méfiance → Surprise → Gratitude hésitante

#### 3.4 Identify Emotional Interactions

**Note moments where emotions interact:**

**Format:**
- [Character A]'s [emotion] triggers [Character B]'s [response]
- Describe emotional dynamic

#### 3.5 Note Significant Absences

**If major character shows no emotional beats:**

**Flag under "Personnages sans beats émotionnels":**
- [Character] - présent mais émotionnellement neutre

**Note:** Could be intentional (masking) or potential issue

#### 3.6 Check Against Previous Chapter

**If emotions.md has previous data:**

**Check continuity:**
- Where did character end emotionally last chapter?
- Does this chapter's opening align?
- Any unexplained emotional shifts?

#### 3.7 Present Emotional Summary

**Summary table:**

```
| Personnage | Beats | Trajectoire | Notes |
|------------|-------|-------------|-------|
| [Char 1] | [N] | [start→end] | [key moment] |
```

**List major interactions**
**List most significant beats**

#### 3.8 User Confirmation

**Present menu:**
- [C] Continuer vers l'analyse des arcs

**Wait for user input before proceeding**

---

## Step 4: Analyze Arc + CHECKPOINT

### Objective
Connect character development with themes, analyze how characters embody themes, present COMPLETE ANALYSIS for user validation.

### Prerequisites
- Steps 1-3 completed
- Theme findings available
- Emotional beats available
- Existing tracking loaded

### Procedure

#### 4.1 Synthesize Themes and Emotions

**For EACH character with significant emotional beats:**

**Connect emotions to themes:**

```markdown
### [Character Name]

**Position thématique dans ce chapitre:**

**[Theme 1]:**
- Position on theme
- How emotions/actions reflect theme
- Movement: [toward/away from/static]

**[Theme 2]:**
- [Same structure]
```

#### 4.2 Identify Character Development Moments

**For each character, identify if chapter contains:**
- **Turning points:** Major position shifts
- **Deepening:** Existing traits intensified
- **Revelation:** New aspects revealed
- **Testing:** Values tested
- **Static:** No development (note if intentional/concerning)

#### 4.3 Map Theme Advancement

**For EACH theme identified in step 2:**

```markdown
### [Theme Name]

**État au début du chapitre:** [Starting state]
**Ce qui se passe:** [Progression through events]
**État à la fin du chapitre:** [Ending state]

**Personnages impliqués:**
- [Character]: [Their role]
- [Character]: [Their role]

**Prochaine étape attendue:** [What follows]
```

#### 4.4 Detect Red Flags

**Check for potential issues:**

- [ ] Thème mentionné mais pas exploré
- [ ] Position personnage inchangée
- [ ] Thème abandonné
- [ ] Incohérence avec chapitres précédents

**Flag detected issues or note "None"**

#### 4.5 Prepare Analysis Summary

**Present COMPLETE analysis:**

```markdown
## Résumé thématique
[Table of themes, presence, progression, characters]

## Résumé émotionnel
[Table of characters, beats, arcs, thematic connections]

## Développements clés
1. [Most significant development]
2. [Second most significant]
3. [Third if applicable]

## Red Flags
[List or "Aucun détecté"]

## Ce que cette analyse va mettre à jour
**themes.md:** [What will be updated]
**emotions.md:** [What will be updated]
**chapter-{XX}-themes.md:** [Will be created/updated]
```

#### 4.6 CHECKPOINT: User Validation

**CRITICAL:** Do NOT proceed without user approval

**Present validation questions:**
1. Les thèmes identifiés sont-ils corrects?
2. Les beats émotionnels reflètent-ils votre intention?
3. Les connexions personnage-thème sont-elles justes?
4. Y a-t-il des éléments que j'ai manqués?
5. Y a-t-il des corrections à apporter?

**Present options:**
- **[A] Approuver** - Analysis correct, proceed to update
- **[C] Corriger** - Provide corrections
- **[R] Refaire** - Redo analysis with new instructions

#### 4.7 Handle User Response

**IF A (Approve):**
- Proceed to Step 5
- Load and read entire next step file

**IF C (Correct):**
- Collect corrections
- Revise analysis summary
- Redisplay checkpoint

**IF R (Redo):**
- Ask for new instructions
- Load step-02 to re-analyze

**IF other:**
- Help user
- Redisplay menu

---

## Step 5: Update Progression

### Objective
Update all tracking files with user-validated analysis from step 4.

### Prerequisites
- Step 4 completed with user approval
- Validated analysis available
- Existing tracking files loaded

### Procedure

#### 5.1 Confirm Validation Status

**Verify:** User approved analysis in step 4
**Confirm:** Ready to proceed with updates

#### 5.2 Update themes.md

**For EACH theme with activity in this chapter:**

**Load existing theme entry**

**Add to Per-Chapter Progression table:**
```
| {chapterNumber} | [Theme Event] | [Character Impact] | [Next Step] |
```

**Update Progression by Chapter Phase (if applicable):**
- Only if chapter marks phase transition
- Reference validated analysis

**Update Character Connections (if new insights):**
- Only add, don't remove existing
- New character-theme connections discovered

**Write updated themes.md**

**Confirm:**
- Number of themes with new entries
- Number of new connections

#### 5.3 Update emotions.md

**For EACH character with emotional beats:**

**Load existing character entry (or create from template)**

**Add to Per-Chapter Emotional Beats table:**
```
| {chapterNumber} | [State] | [Trigger] | [Expression] | [Impact] |
```

**Update Emotional Arc Summary (if significant shift):**
- Only if chapter contains turning point
- Append to existing summary, don't overwrite

**Write updated emotions.md**

**Confirm:**
- Number of characters with new beats
- Number of trajectories updated

#### 5.4 Create/Update Chapter Analysis File

**Action:** Create or update `chapter-{chapterNumber}-themes.md`

**If file doesn't exist:** Create from template

**Fill all sections from validated analysis:**
- Themes Present (from step 2)
- Emotional Beats (from step 3)
- Character Development (from step 4 synthesis)
- Red Flags (from step 4 analysis)
- Continuity Notes (from analysis)
- Summary (from analysis)

**Write chapter-{XX}-themes.md**

#### 5.5 Summarize Updates

**Present update summary:**

```
| Fichier | Action | Détails |
|---------|--------|---------|
| themes.md | Mis à jour | [N] thèmes, [N] entrées |
| emotions.md | Mis à jour | [N] personnages, [N] beats |
| chapter-{XX}-themes.md | Créé/Mis à jour | Analyse complète |
```

**Confirm all data persisted**

#### 5.6 User Confirmation

**Present menu:**
- [C] Continuer vers la vérification

**Wait for user input before proceeding**

---

## Step 6: Verify Consistency (Final)

### Objective
Verify thematic tracking remains coherent across chapters and provide final report with red flags/concerns.

### Prerequisites
- Steps 1-5 completed
- All tracking files updated
- Chapter analysis created

### Procedure

#### 6.1 Load Tracking History

**Load complete files:**
- themes.md (full file)
- emotions.md (full file)
- Previous chapter-XX-themes.md files (if exist)

#### 6.2 Verify Theme Continuity

**For EACH theme in themes.md:**

**Check progression logic:**
- Does Per-Chapter Progression show logical flow?
- Any unexplained gaps?
- Does progression match Progression by Chapter Phase?

**Flag issues:**
- 🟡 **Attention:** Theme hasn't appeared in N chapters
- 🔴 **Problème:** Progression contradicts phase plan
- ✅ **OK:** Tracking is coherent

#### 6.3 Verify Character Emotional Arcs

**For EACH character in emotions.md:**

**Check emotional continuity:**
- Do chapter-to-chapter states make sense?
- Any unexplained emotional jumps?
- Does Per-Chapter Beats table show growth/change?

**Flag issues:**
- 🟡 **Attention:** Character shows no change in N chapters
- 🔴 **Problème:** Emotional state inconsistent
- ✅ **OK:** Arc is coherent

#### 6.4 Cross-Reference Themes and Characters

**Check Character Connections in themes.md:**
- Are claimed connections supported by chapter data?
- Are there characters engaging with themes not listed?

**Flag issues:**
- 🟡 **Attention:** Character engages with theme but not listed
- ✅ **OK:** Connections match evidence

#### 6.5 Compile Red Flags Summary

**Organize by severity:**

```markdown
## 🔴 Problèmes à traiter
[Critical issues needing attention]
Or: "Aucun problème critique détecté"

## 🟡 Points d'attention
[Items needing attention but not critical]
Or: "Aucun point d'attention particulier"

## ✅ Vérifications réussies
- Continuité thématique: [OK / N issues]
- Arcs émotionnels: [OK / N issues]
- Connexions personnage-thème: [OK / N issues]
```

#### 6.6 Provide Recommendations

**Based on analysis:**

**1. Thèmes à développer:**
- Themes due for progression
- Themes needing focus

**2. Personnages à surveiller:**
- Characters needing arc movement
- Characters needing resolution

**3. Questions ouvertes:**
- Questions raised by narrative
- Issues to address

#### 6.7 Present Final Summary

**Complete workflow summary:**

```markdown
## ANALYSE THÉMATIQUE TERMINÉE - Chapitre {N}

**Résumé de l'analyse:**

| Métrique | Valeur |
|----------|--------|
| Thèmes suivis | [N] |
| Thèmes actifs ce chapitre | [N] |
| Personnages suivis | [N] |
| Beats émotionnels ce chapitre | [N] |
| Red flags détectés | [N] |

**Fichiers mis à jour:**
- ✅ tracking/themes.md
- ✅ tracking/emotions.md
- ✅ tracking/chapter-{N}-themes.md

**Santé thématique globale:** [Excellente/Bonne/À surveiller/Préoccupante]
```

**Workflow complete.**

**User can:**
- Review tracking files
- Run workflow again for next chapter
- Address red flags raised

---

## File Structure Reference

### themes.md Structure

```markdown
## Theme: [Theme Name]

### Core Question
[Central question theme explores]

### Tension
[Opposing forces]

### Progression by Chapter Phase
- Chapters 1-5: [Introduction]
- Chapters 6-10: [Exploration]
- etc.

### Character Connections
- **[Character]:** [How they embody theme]

### Per-Chapter Progression
| Chapter | Theme Event | Character Impact | Next Step |
```

### emotions.md Structure

```markdown
## Character: [Character Name]

### Emotional Arc Summary
[Overall journey description]

### Dominant Emotions
- **Primary:** [Main emotion]
- **Secondary:** [Supporting]
- **Conflict:** [Tension]

### Emotional State by Phase
- **Opening:** [State]
- **Rising Action:** [Intensification]
- etc.

### Per-Chapter Emotional Beats
| Chapter | Emotional State | Trigger | Expression | Impact |
```

### chapter-{XX}-themes.md Structure

```markdown
# Chapter [XX] Thematic Analysis

**Chapter Title:** [Title]
**Analyzed:** [Date]
**Word Count:** [Count]

---

## Themes Present
[Theme 1 analysis]
[Theme 2 analysis]

---

## Emotional Beats
[Beat table and analysis]

---

## Character Development
[Per-character development]

---

## Red Flags
[Issues detected or "None"]

---

## Continuity Notes
[References to previous/future chapters]

---

## Summary
**One-line summary:** [Sentence]
**Themes advanced:** [List]
**Themes static:** [List]
**New elements:** [List]
```

---

## Quality Assurance Checklist

### Step Completion Criteria

**Step 1 complete when:**
- [ ] Chapter content loaded
- [ ] Living Bible loaded or confirmed skipped
- [ ] Tracking folder exists
- [ ] themes.md loaded or initialized
- [ ] emotions.md loaded or initialized
- [ ] User informed of all loaded data

**Step 2 complete when:**
- [ ] All Living Bible themes checked
- [ ] Each detected theme has evidence
- [ ] Presence levels classified
- [ ] New elements identified
- [ ] Absent themes noted
- [ ] Summary presented
- [ ] User confirmed to continue

**Step 3 complete when:**
- [ ] All significant characters analyzed
- [ ] Emotional beats documented with triggers/expressions
- [ ] Trajectories mapped
- [ ] Interactions noted
- [ ] Continuity checked
- [ ] Summary presented
- [ ] User confirmed to continue

**Step 4 complete when:**
- [ ] Themes and emotions synthesized
- [ ] Character positions documented
- [ ] Theme advancement mapped
- [ ] Red flags detected
- [ ] Complete analysis presented
- [ ] User explicitly approved

**Step 5 complete when:**
- [ ] themes.md updated with chapter entries
- [ ] emotions.md updated with character beats
- [ ] chapter-{XX}-themes.md created/updated
- [ ] Only validated content written
- [ ] Updates confirmed
- [ ] User confirmed to continue

**Step 6 complete when:**
- [ ] All tracking files verified
- [ ] Theme continuity checked
- [ ] Character arcs verified
- [ ] Red flags categorized
- [ ] Recommendations provided
- [ ] Final summary presented
- [ ] Workflow completes cleanly

---

## Error Handling

### File Not Found Errors

**Chapter file not found:**
- Inform user of exact path tried
- Request path verification
- Return to step 1.1

**Living Bible not found:**
- Offer to continue without it
- Or request alternate path
- Document limitation if continuing

**Tracking files not found:**
- Initialize from templates
- Inform user of initialization
- Proceed with new tracking

### Data Validation Errors

**Chapter has no content:**
- Inform user of issue
- Request different file
- Don't proceed with empty content

**Living Bible has no themes:**
- Inform user of issue
- Proceed with manual theme identification
- Document limitation

### Analysis Validation Errors

**No themes detected:**
- Verify with user if this is expected
- May be valid (some chapters are theme-light)
- Document and proceed

**No emotional beats found:**
- Verify with user if this is expected
- May be valid (some chapters are action-heavy)
- Document and proceed

### Update Errors

**File write fails:**
- Inform user of error
- Retry if possible
- Don't mark step complete

**Data mismatch:**
- Verify validated analysis matches file content
- Correct mismatches
- Confirm before proceeding
