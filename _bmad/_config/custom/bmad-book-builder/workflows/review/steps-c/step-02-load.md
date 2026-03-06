---
name: 'step-02-load'
description: 'Load chapter content, style profile, and forward continuity context'

# Navigation
nextStepFile: './step-03-analyze.md'

# Inputs (resolved from step-01)
# chapterFile: resolved at runtime from session state
# styleProfilePath: resolved from frontmatter
# forward_continuity_enabled: from session state
# forward_chapters: from session state (POV chain)

# Reference
styleProfilePath: '{bbb_output_folder}/style-profile.yaml'
metadataFolder: '{bbb_output_folder}/book-1/metadata'
trilogyIndex: '{bbb_output_folder}/trilogy-chapter-index.md'
---

# Step 2: Load Chapter Content

## STEP GOAL:
Read the target chapter file and the style profile into context. If forward continuity is enabled, identify the POV character and load metadata for all FORWARD chapters in their POV chain. Prepare the content payloads that will be dispatched to the parallel review subagents in step 03.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:
- NEVER generate content without user input
- CRITICAL: Read the complete step file before taking any action
- YOU ARE A FACILITATOR, not a content generator
- TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:
- You are a **Review Coordinator** preparing inputs for parallel reviewers
- Do NOT read the chapter yourself for review purposes — the subagents will do that

### Step-Specific Rules:
- Focus ONLY on loading files
- FORBIDDEN to comment on chapter quality or content
- FORBIDDEN to begin analysis

---

## MANDATORY SEQUENCE

### 1. Load Chapter File

Read the full contents of the target chapter file. Store as `{chapter_content}`.

Report: `Loaded {chapter_id}: {word_count} words, {line_count} lines`

### 2. Load Style Profile

Read `{styleProfilePath}`. Store as `{style_profile}`.

If missing: Note absence. Editorial reviewer will operate without style reference.

Report: `Style profile: {loaded/not found}`

### 3. Load Forward Continuity Context (if enabled)

**SKIP this step entirely if `{forward_continuity_enabled}` is false.**

If enabled:

1. **Identify POV character** from the chapter content (the POV character should be evident from the chapter header or metadata file). If unclear, check `{metadataFolder}/chapter-{N}-meta.yaml` for the `pov` field.

2. **Look up the POV chain** from the trilogy chapter index. Find all chapters AFTER the current one for this character in the current book.

3. **Load forward metadata files** from `{metadataFolder}`:
   - For each forward chapter in the POV chain, read `chapter-{N}-meta.yaml`
   - Store the `summary`, `keyPoints`, `characters`, and `newElements` fields from each
   - Combine into `{forward_context}` — a concatenation of all forward chapter metadata

4. **Report:**
   ```
   Forward continuity: {pov_character}
   Forward chapters: {list of chapter numbers}
   Metadata loaded: {N} files ({total_tokens} est. tokens)
   ```

Note: Load ONLY metadata files, NOT full chapter prose. The metadata summaries are sufficient for forward continuity review.

### 4. Prepare Subagent Payloads

Two or three payloads will be needed in step 03:

**Adversarial payload:**
- Chapter text only (no style profile, no project context)

**Editorial payload:**
- Chapter text + style profile

**Forward Continuity payload (if enabled):**
- Chapter text + forward chapter metadata + POV character name + POV chain list

Do NOT dispatch yet. Payload preparation is implicit — step 03 handles dispatch.

### 5. Auto-Proceed

Display:

```
Chapter loaded: {chapter_id} ({word_count} words)
Style profile: {status}
Forward continuity: {enabled — {N} forward chapters | disabled}

Dispatching parallel reviewers...
```

Immediately load and execute `step-03-analyze.md`.

---

## SYSTEM SUCCESS/FAILURE METRICS

### SUCCESS:
- Chapter content loaded in full
- Style profile loaded (or absence noted)
- No analysis performed
- Auto-proceeded to step 03

### SYSTEM FAILURE:
- Began reviewing or commenting on chapter content
- Failed to load chapter file
- Did not auto-proceed

**Master Rule:** Load and pass through. Do not analyze.
