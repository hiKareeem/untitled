---
name: 'step-07-finalize'
description: 'Lock chapter, generate metadata with summary, update tracking'

# Output
outputFile: '{bbb_output_folder}/chapters/chapter-{chapter_number}.md'
metaFile: '{bbb_output_folder}/chapters/chapter-{chapter_number}-meta.yaml'
metaTemplate: '../data/metadata-template.yaml'

# Tracking
projectTrackingFile: '{bbb_output_folder}/project-status.yaml'

# References
finalizationProcedures: '../data/references/chapter-finalization-procedures.md'
auditChainReference: '../data/references/automated-audit-chain.md'
auditChainUserFlow: '../data/references/audit-chain-user-flow.md'
metadataTemplateFile: '../data/metadata-template.yaml'
---

# Step 7: Finalize Chapter

## STEP GOAL:

To lock the approved chapter, generate comprehensive metadata including the critical summary and key points, and update project tracking files.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- CRITICAL: Read the complete step file before taking any action
- YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- You are completing the chapter writing process
- The metadata you generate is CRITICAL for future chapters
- Accuracy in the summary enables continuity

### Step-Specific Rules:

- Chapter text is now LOCKED — no more content changes
- Generate comprehensive metadata with summary
- Summary must capture key events accurately (future chapters depend on it)
- Update all tracking files

## CONTEXT BOUNDARIES:

- Chapter approved by author in step-05
- All reviews complete
- Final chapter text is fixed
- Focus: Metadata generation and tracking

## MANDATORY SEQUENCE

### 1. Lock Chapter

> **Reference:** `{finalizationProcedures}` - Section 1: Chapter Locking Procedure

"**Finalizing Chapter {chapter_number}...**

The chapter text is now locked. No further content changes will be made.

**Final Statistics:**
- Word Count: {count}
- Draft Versions: {count}
- Review Status: Approved"

Update {outputFile} frontmatter:
- Set status: 'final'
- Set finalizedDate: {date}

### 2. Generate Synopsis Comment

> **Reference:** `{finalizationProcedures}` - Section 2: Synopsis Generation

"**Generating Chapter Synopsis Comment...**

This synopsis will be embedded in the chapter file for quick reference and continuity checking."

Generate and INSERT synopsis comment at the TOP of the chapter content (right after the frontmatter, BEFORE chapter title).

**Use template from:** `{finalizationProcedures}` Section 2

### 3. Generate Chapter Summary (CRITICAL)

> **Reference:** `{finalizationProcedures}` - Section 3: Chapter Summary Generation

"**Generating Chapter Summary...**

This summary is CRITICAL for:
- Writing future chapters (continuity)
- Book-level analysis without reading full text
- Tracking story progression"

Write 2-3 paragraph summary covering:
- Main events of the chapter
- Character developments
- Key decisions or turning points
- How the chapter ends (state of affairs)

### 4. Extract Key Points

> **Reference:** `{finalizationProcedures}` - Section 4: Key Points Extraction

Identify and categorize:
- Key Plot Points
- Characters Appearing
- Locations Used
- New Elements (divergences from plan)

### 5. Generate Metadata File

> **Reference:** `{finalizationProcedures}` - Section 5: Metadata File Generation

Create {metaFile} from template at `{metadataTemplateFile}`.

Fill in the template structure with:
- Chapter metadata (number, title, word count, POV, timeline)
- Summary (from Section 3)
- Key points (from Section 4)
- Characters, locations, new elements
- Review results (when available)
- Date and author information

### 6. Update Project Tracking

> **Reference:** `{finalizationProcedures}` - Section 6: Project Tracking Update

Update {projectTrackingFile} (if exists) with chapter completion status.

### 7. Automated Audit Chain

> **Reference:** `{auditChainUserFlow}` for complete user interaction flow
> **Technical Reference:** `{auditChainReference}` for audit chain procedures

"**🔗 Chaîne d'Audit Automatique**

Pour garantir la cohérence de votre roman, je vais maintenant déclencher automatiquement une série d'audits de qualité."

**Present user choice:** See `{auditChainUserFlow}` Section: User Choice Prompt

Wait for user input, then execute according to their choice:
- **[A] Automatic** - Execute full chain
- **[S] Selective** - Execute selected steps
- **[D] Defer** - Skip with confirmation

**Chain completion:** Present summary and store status in chapter frontmatter.

See `{auditChainUserFlow}` for complete flow and messaging.

### 8. Present Completion Summary

> **Reference:** `{finalizationProcedures}` - Section 7: Completion Summary

Present completion message with:
- Final chapter statistics
- Metadata generated
- Project tracking updates
- Summary preview

### 9. Final Confirmation

> **Reference:** `{finalizationProcedures}` - Section 8: Final Confirmation

Present final confirmation message with:
- All files saved
- Next steps options
- Thank you message

(No next step — this is the final step)

---

## SYSTEM SUCCESS/FAILURE METRICS

> **Reference:** `{finalizationProcedures}` - Success Metrics section

**SUCCESS:**
- Chapter text locked with final status
- Comprehensive summary generated
- All key points extracted accurately
- Metadata file created with complete schema
- Project tracking updated
- Clear completion confirmation

**SYSTEM FAILURE:**
- Incomplete summary (missing key events)
- Missing key points or characters
- Not tracking new elements/divergences
- Not updating project tracking
- Leaving status as 'draft'

**Master Rule:** The summary MUST be accurate and complete — future chapters depend on it for continuity.
