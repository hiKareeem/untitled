---
name: 'step-06-bible-update'
description: 'Update tracking files, story bible, project status, and finalize chapter'

# Navigation
# (No next step — this is the final step)

# Output
outputFile: '{bbb_output_folder}/current-book/chapters/chapter-{chapter_number}.md'
metaFile: '{bbb_output_folder}/current-book/chapters/chapter-{chapter_number}-meta.yaml'

# Tracking Files
themesTracking: '{bbb_output_folder}/current-book/tracking/themes.md'
emotionsTracking: '{bbb_output_folder}/current-book/tracking/emotions.md'
rhythmTracking: '{bbb_output_folder}/current-book/tracking/rhythm.md'
rhythmDashboard: '{bbb_output_folder}/current-book/tracking/rhythm-dashboard.md'

# Bible Files
charactersBible: '{bbb_output_folder}/bible/characters.md'
locationsBible: '{bbb_output_folder}/bible/locations.md'
objectsBible: '{bbb_output_folder}/bible/objects.md'
themesBible: '{bbb_output_folder}/bible/themes.md'

# Project Tracking
projectTrackingFile: '{bbb_output_folder}/project-status.yaml'

# References
metadataTemplateFile: '../data/metadata-template.yaml'
---

# Step 6: Bible Update & Finalization

## STEP GOAL:

To update all tracking files, story bible dimensions, and project status with the chapter's data, then lock the chapter as v1-complete.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- CRITICAL: Read the complete step file before taking any action
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- You are completing the chapter writing process
- The tracking and bible updates are CRITICAL for future chapters
- Accuracy enables continuity — errors here propagate forward

### Step-Specific Rules:

- Update ALL tracking files listed in this step
- Update ALL relevant bible dimensions
- Use `<!-- INSERT_NEXT_* -->` markers to find insertion points (grep, don't read whole files)
- Use `<!-- CHARACTER: Name -->` markers in emotions.md for navigation
- Never overwrite existing data — append/insert new entries
- Update project-status.yaml
- Set chapter frontmatter status to v1-complete

## CONTEXT BOUNDARIES:

- Chapter has been style-audited (step-04) and content-audited (step-05)
- Audit file and per-chapter thematic analysis already created in step-05
- Focus: Data propagation to tracking and bible files

## MANDATORY SEQUENCE

### 1. Update Tracking: themes.md

Using the per-chapter thematic analysis from step-05:

- Add **compact** rows to per-theme tables for themes at **Dominant or Strong** intensity only
- Moderate/Background themes: optional (full detail already in `chapter-{N}-themes.md`)
- Update the Progression by Chapter summary table (all themes, full detail)
- Update the file's lastChapter and lastUpdated metadata

**Navigation:** Grep for `<!-- INSERT_NEXT_COMPLICITY -->`, `<!-- INSERT_NEXT_COMMODIFICATION -->`, etc. to find insertion points for each theme table. Grep for `<!-- INSERT_NEXT_PROGRESSION -->` for the master table.

**Compact per-theme format** (new entries only — existing entries unchanged):
```
| Ch {N} | **{Intensity}.** {1-2 sentence summary} | {Character}: {1-line impact} | {Next step pointer} |
```
Full thematic analysis remains in `tracking/chapter-{N}-themes.md`.

### 2. Update Tracking: emotions.md

For each character appearing in the chapter:

- Add emotional beats to their Per-Chapter Emotional Beats table
- If this is a character's debut, create their full section (Arc Summary, Dominant Emotions, Emotional State by Phase, beats table)
- Update the Summary Table entry for each modified character
- Update the file's lastChapter metadata

**Navigation:** Grep for `<!-- CHARACTER: {Name} -->` to jump to a character's section. Grep for `<!-- SUMMARY_TABLE -->` for the summary.

**Format:** Match existing entry format. Each beat includes: Chapter-Beat #, Emotional State, Trigger, Expression, Impact on Others.

### 3. Update Tracking: rhythm.md + rhythm-dashboard.md

The rhythm system is split into two files:
- **`rhythm.md`** — Full per-chapter rhythm analyses (append new analysis before `<!-- INSERT_NEXT_ANALYSIS -->`)
- **`rhythm-dashboard.md`** — Summary dashboard + Phase Health (quick-update file)

**In `rhythm.md`**, add the chapter's rhythm analysis section:

- **Metrics table:** Word count, scenes, paragraphs, dialogue %, avg sentence length, fragment %
- **Tension curve:** ASCII art + descriptions per scene
- **Beat map:** Sequential beats with % position and tension delta
- **Transitions:** Scene-to-scene transition quality
- **Flow scores:** Component scores + overall
- **Action/Reflection balance**
- **Pacing notes:** Strengths, concerns, recommendations
- **Comparison to plan:** Mode match, adjacent chapter contrast
- **Comparison to previous chapters:** Metrics table with delta

**In `rhythm-dashboard.md`**, update:
- Fill in the chapter's row (before `<!-- INSERT_NEXT_DASHBOARD -->`)
- Update Phase Health table (written/analyzed counts)
- Update both files' lastChapter and analyzedChapters metadata

### 4. Update Bible: characters.md

For each character appearing in the chapter:

- **POV characters:** Update Recent History (append chapter summary), Appearances (last/next), Arc progression (next step), any relationship changes
- **Supporting characters:** Update Recent History, Appearances
- **New characters:** Add to Recent Changes table (before `<!-- INSERT_NEXT_RECENT_CHANGES -->`); if significant, create a full supporting character entry
- Update the file's lastUpdated metadata

### 5. Update Bible: locations.md

- Add any new locations or sub-locations established in the chapter
- Update existing location entries with new details (interior locations, key events)
- Add the chapter to the location's Key Events list

### 6. Update Bible: objects.md

- Update existing objects with new details or state changes from the chapter
- Add any new objects introduced

### 7. Update Bible: themes.md

- Add chapter row to the Progression by Chapter table (before `<!-- INSERT_NEXT_PROGRESSION -->`)
- Add any new thematic symbols to the Thematic Symbols table (before `<!-- INSERT_NEXT_SYMBOLS -->`)
- Update the file's lastUpdated metadata

### 8. Ensure Meta File Exists

If `{metaFile}` does not already exist, generate it using `{metadataTemplateFile}` as a guide. Fill in:
- Chapter metadata (number, title, word count, POV, timeline)
- Key points, characters, locations, new elements
- Date and author information

If it already exists (created during drafting), verify it's complete.

### 9. Update Project Status

Update `{projectTrackingFile}`:

```yaml
chapter_{N}:
  title: "{title}"
  status: v1-complete
  pov: "{character}"
  wordCount: {count}
  completedDate: "{date}"
  metaFile: "chapter-{N}-meta.yaml"
  mode: {PRESSURE|TEXTURE}
```

Update `completedCount`, `totalWords`, and `lastUpdated`.

### 10. Lock Chapter

Update {outputFile} frontmatter:
- Add 'step-06-bible-update' to stepsCompleted
- Set lastStep: 'step-06-bible-update'
- Set status: v1-complete

### 11. Present Completion Summary

```
**Chapter {chapter_number} — "{title}" — v1-complete**

**Files created:**
- tracking/audit-chapter-{N}.md
- tracking/chapter-{N}-themes.md

**Files updated:**
- tracking/themes.md — Ch {N} entries in all 8 theme tables
- tracking/emotions.md — {character} ({count} beats) + supporting characters
- tracking/rhythm.md — Ch {N} metrics + dashboard
- bible/characters.md — {list of updated characters}
- bible/locations.md — {list of updated locations}
- bible/objects.md — {list of updated objects}
- bible/themes.md — Ch {N} row + {count} new symbols
- project-status.yaml — Ch {N} added

**Chapter Statistics:**
- Words: {count}
- Mode: {PRESSURE|TEXTURE}
- Flow: {score}/10
- Status: v1-complete

Ready for the next chapter.
```

(No next step — this is the final step of the chapter-write workflow)

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:

- All 3 tracking files updated with chapter data
- All relevant bible dimensions updated
- Project status updated
- Meta file complete
- Chapter frontmatter set to v1-complete
- Completion summary presented

### SYSTEM FAILURE:

- Missing tracking updates (themes, emotions, or rhythm)
- Missing bible updates
- Not updating project-status.yaml
- Leaving chapter status as draft
- Overwriting existing data instead of appending

**Master Rule:** Every tracking and bible update must be accurate and complete — future chapters depend on this data for continuity. Use `<!-- INSERT_NEXT_* -->` markers to find insertion points efficiently — grep for the marker instead of reading the whole file.
