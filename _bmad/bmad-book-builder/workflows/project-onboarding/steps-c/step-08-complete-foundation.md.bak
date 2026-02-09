---
name: 'step-08-complete-foundation'
description: 'Launch workflows to fill detected gaps and complete BBB foundation'

# File references (ONLY variables used in this step)
gapReportFile: '{bbb_output_folder}/bbb-gap-report-{project_name}.md'
finalSummaryTemplate: './data/final-summary-template.md'
---

# Step 8: Complete Foundation

## STEP GOAL:

Guide the author through launching BBB workflows to address detected gaps, ensuring the project is fully BBB-ready before completion.

## MANDATORY EXECUTION RULES:
### Universal Rules:
- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read (but this is final step, no next)
- 📋 YOU ARE A FACILITATOR, not content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the config `{communication_language}`

### Role Reinforcement:
- ✅ You are a Migration Specialist — completing the foundation
- ✅ Guide author through workflow selection
- ✅ Ensure nothing is missed
- ✅ Celebrate completion when done

### Step-Specific Rules:
- 🎯 Focus on gap completion and finalization
- 📋 Present options clearly
- 💬 Allow author to choose approach
- 🎉 Make completion satisfying

## EXECUTION PROTOCOLS:
- 🎯 Present gap report and options
- 💾 Guide workflow launching
- 📖 Generate final summary
- 🎉 Mark project as BBB-ready

## CONTEXT BOUNDARIES:
- Available: Gap report from step 7
- Focus: Gap completion and finalization
- Limits: Guidance and orchestration
- Dependencies: Requires gap detection from step 7

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Gap Report

Load {gapReportFile} to present to author.

### 2. Present Gap Summary

Load and present gap report from {gapReportFile}:

```markdown
**🎯 BBB FOUNDATION FINALIZATION**

Your migration is complete! Here's what's missing to be fully functional with BBB:

---

## Detected Gaps

{gap_summary_table}

**Estimated total time:** {total_time}

**BBB Readiness :** {readiness_level}

---

See **Gap Detection Criteria** for detailed explanations:
- `{workflow_root}/data/references/gap-detection-criteria.md`

## Options

How would you like to proceed?

**[A]** **ALL** — Automatically launch all recommended workflows
**[S]** **Selective** — Choose which workflows to launch
**[M]** **Manual** — Complete manually later
**[I]** **Info** — More information about each workflow
**[C]** **Continue** — Go directly to the summary (without launching)
```

### 3. Handle User Choice

**IF A — Launch ALL:**

Execute workflows in optimal order (see **Gap Detection Criteria**):
1. **style-capture** — Analyze author's voice (15 min)
2. **foundation** — Create chapter plan (30 min)
3. **build-characters** — Enrich characters (20 min)
4. **living-bible** — Organize story bible (15 min)

For each workflow: Launch, monitor completion, log results.

After all workflows:
```markdown
**✅ ALL WORKFLOWS COMPLETE**

Your project is now fully integrated with BBB!

Type [C] to view the final summary.
```

**IF S — Selective:**

```markdown
**Which workflows would you like to launch?**

**[1]** style-capture ({time})
**[2]** foundation ({time})
**[3]** build-characters ({time})
**[4]** living-bible ({time})

Enter the numbers (comma-separated) or [C] to continue.
```

Launch selected workflows sequentially.

**IF M — Manual:**

```markdown
**Manual Completion**

You can complete the gaps manually:

**Style Profile :** Lancez `style-capture` plus tard
**Chapter Plan :** Lancez `foundation` plus tard
**Characters :** Enrichissez manuellement dans story-bible/characters/
**Story Bible :** Organisez manuellement dans story-bible/

**Documentation :** `{project-root}/_bmad/bmad-book-builder/README.md`

Type [C] to continue to the summary.
```

**IF I — Info:**

Display workflow information from **Gap Detection Criteria** reference.

**IF C — Continue directly:**

Skip workflow launching, proceed to final summary.

### 4. Generate Final Summary

Load {finalSummaryTemplate} and create final summary at:
`{bbb_output_folder}/bbb-complete-{project_name}.md`

**Fill template with:**
- All workflows executed status
- New project structure (see **BBB Folder Structure** reference)
- Ready to write instructions
- Quick reference guide

### 5. Present Completion

Display final summary using template, including:
- Migration completion summary
- New BBB structure overview
- Ready to write instructions with workflow commands
- Documentation reference links
- Congratulations message

### 6. Update Project Status

Update {gapReportFile} status:
```yaml
status: "COMPLETE"
completedDate: "{current_date}"
bbb_ready: "true"
```

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS:

### ✅ SUCCESS:
- Gap report presented clearly
- User options provided and handled
- Workflows launched (if chosen)
- Final summary generated
- Project marked BBB-ready
- Author satisfied with completion

### ❌ SYSTEM FAILURE:
- Skipping gap presentation
- Not providing workflow options
- Incomplete final summary
- Not marking project complete

**Master Rule:** This is the FINAL step. Ensure the author feels confident and ready to use BBB. Make completion satisfying and clear.
