---
name: 'step-06-verify-consistency'
description: 'Verify thematic coherence with previous chapters and report findings'
---

# Step 6: Verify Consistency (Final)

## STEP GOAL:

To verify that the thematic tracking remains coherent across chapters and provide a final report with any red flags or concerns.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 THIS IS THE FINAL STEP - provide comprehensive verification
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE VERIFYING coherence and flagging concerns
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the **Thematic Weaver** - ensuring narrative coherence
- ✅ Compare this chapter's tracking against the full history
- ✅ Flag issues but don't alarm - some may be intentional
- ✅ Provide actionable insights, not just problems

### Step-Specific Rules:

- 🎯 Focus on CROSS-CHAPTER coherence
- 🚫 FORBIDDEN to modify any files in this step
- 💬 Approach: Quality assurance with constructive feedback

## EXECUTION PROTOCOLS:

- 🎯 Load all tracking files for comparison
- 💾 Generate verification report (display only, don't save separately)
- 📖 Identify patterns, concerns, and recommendations
- 🚫 This is read-only verification

## CONTEXT BOUNDARIES:

- Available: All tracking files, chapter analysis files
- Focus: Coherence verification
- Limits: Analysis and reporting only
- Dependencies: Steps 01-05 completed

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise.

### 1. Load Tracking History

"**Coherence check - Post Chapter {chapterNumber}**

Loading tracking history..."

Load:
- themes.md (full file)
- emotions.md (full file)
- Previous chapter-XX-themes.md files (if they exist)

### 2. Verify Theme Continuity

"**Checking thematic continuity...**"

For EACH theme in themes.md:

**Check progression logic:**
- Does the Per-Chapter Progression table show logical flow?
- Are there unexplained gaps (chapters where theme should appear but doesn't)?
- Does the progression match the Progression by Chapter Phase?

**Flag issues:**
- 🟡 **Attention:** [Theme] hasn't appeared in [N] chapters
- 🔴 **Issue:** [Theme] progression contradicts phase plan
- ✅ **OK :** [Theme] tracking is coherent

### 3. Verify Character Emotional Arcs

"**Checking emotional arcs...**"

For EACH character in emotions.md:

**Check emotional continuity:**
- Do chapter-to-chapter emotional states make sense?
- Are there unexplained emotional jumps?
- Does the Per-Chapter Beats table show growth/change?

**Flag issues:**
- 🟡 **Attention:** [Character] shows no emotional change in [N] chapters
- 🔴 **Issue:** [Character] emotional state inconsistent (was X, suddenly Y)
- ✅ **OK :** [Character] arc is coherent

### 4. Cross-Reference Themes and Characters

"**Checking character-theme connections...**"

Check Character Connections in themes.md against actual chapter data:
- Are claimed connections supported by chapter analyses?
- Are there characters engaging with themes not listed in connections?

**Flag issues:**
- 🟡 **Attention:** [Character] engages with [Theme] but not listed in connections
- ✅ **OK :** Connections match chapter evidence

### 5. Compile Red Flags Summary

"**══════════════════════════════════════════════════════════════════**
**VERIFICATION REPORT - Chapter {chapterNumber}**
**══════════════════════════════════════════════════════════════════**"

**Organize by severity:**

```markdown
## 🔴 Issues to address

[List critical issues that likely need addressing]
- [Issue 1 with explanation]
- [Issue 2 with explanation]

Or: "No critical issues detected."

## 🟡 Points of attention

[List items that might need attention but aren't critical]
- [Item 1 with context]
- [Item 2 with context]

Or: "No special points of attention."

## ✅ Successful checks

- Thematic continuity: [OK / N issues]
- Emotional arcs: [OK / N issues]
- Character-theme connections: [OK / N issues]
```

### 6. Provide Recommendations

"**Recommendations for upcoming chapters:**"

Based on the analysis:

1. **Themes to develop:**
   - [Theme] is due for progression based on phase plan
   - [Theme] hasn't had focus recently

2. **Characters to watch:**
   - [Character] arc needs movement
   - [Character] emotional state needs resolution

3. **Open questions:**
   - [Question raised by the narrative that should be addressed]

### 7. Present Final Summary

"**══════════════════════════════════════════════════════════════════**
**THEMATIC ANALYSIS COMPLETE - Chapter {chapterNumber}**
**══════════════════════════════════════════════════════════════════**

**Analysis summary:**

| Metric | Value |
|--------|-------|
| Themes tracked | [N] |
| Themes active this chapter | [N] |
| Characters tracked | [N] |
| Emotional beats this chapter | [N] |
| Red flags detected | [N] |

**Files updated:**
- ✅ tracking/themes.md
- ✅ tracking/emotions.md
- ✅ tracking/chapter-{chapterNumber}-themes.md

**Overall thematic health:** [Excellent / Good / Watch / Concerning]

---

**The thematic tracking for chapter {chapterNumber} is complete.**

To analyze the next chapter, rerun the theme-tracker workflow."

### 8. Workflow Complete

This is the FINAL STEP. No menu needed.

The workflow is complete. User can:
- Review the tracking files
- Run the workflow again for the next chapter
- Address any red flags raised

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All tracking files verified for coherence
- Theme continuity checked
- Character arcs verified
- Red flags clearly categorized
- Recommendations provided
- Final summary presented
- Workflow completes cleanly

### ❌ SYSTEM FAILURE:

- Not checking all tracking files
- Missing coherence issues
- Not providing recommendations
- Leaving workflow in incomplete state
- Modifying files in this step

**Master Rule:** Verify thoroughly. Report clearly. Complete cleanly.
