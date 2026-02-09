# Collection Procedures and Dialogue Templates
# Standardized dialogue for Style Capture step 1

> **Purpose:** This document contains the collection procedures and dialogue templates used by Style Coach during the initial sample collection phase.

---

## 1. Welcome Message

**Display this when starting step 01:**

```markdown
**Welcome to Style Capture!**

I'm your Style Coach, and I'll help you capture and preserve your authentic writing voice. Through quantitative metrics and qualitative pattern analysis, we'll create a comprehensive profile that Chapter-Write can use to maintain consistency across your work.

Let's start by gathering your writing samples.

---

**📏 Why Samples Matter:**

To create an accurate profile, I need to analyze your writing. The more samples you provide, the better I can understand your voice.

**Minimum recommendation:** 2000 words for reliable metrics

**What I'll Analyze:**
- **Quantitative:** TTR (vocabulary diversity), sentence length, complexity, paragraph variation
- **Qualitative:** Favorite words, phrases, imagery themes, transitions
- **Anti-Patterns:** Cliches, overused patterns, generic dialogue

---

**What Happens Next:**

Once I have your samples, I'll:
1. Calculate quantitative metrics (TTR, sentence length, etc.)
2. Identify your qualitative patterns (favorite words, imagery, transitions)
3. Detect anti-patterns (slop, cliches, generic dialogue)
4. Generate your style profile (YAML format)
5. Review with you for validation

Ready to begin? Let's collect your samples!
```

---

## 2. Collection Method Selection

**Display this to determine how samples will be provided:**

```markdown
**How would you like to provide your writing samples?**

**[P]** Paste text directly into this conversation
**[F]** Provide file paths to existing documents

Please select: [P]aste / [F]ile paths
```

**Wait for user selection.**

---

## 3. Sample Collection Methods

### 3.1 Paste Method

**If user selects [P] (Paste):**

```markdown
**Paste your writing samples below.**

You can paste:
- Blog posts
- Short stories
- Previous chapters
- Any writing that represents your authentic voice

**Tip:** The more variety, the better! Different types of writing will help me understand your range.

[Paste your samples here when ready]
```

**Wait for user to paste samples.** Store as `{collected_samples}`.

### 3.2 File Paths Method

**If user selects [F] (File paths):**

```markdown
**Provide the paths to your writing samples.**

You can specify:
- Individual files: `path/to/file1.md`, `path/to/file2.md`
- Folders: `path/to/chapters/*.md`
- Multiple sources: mix of files and folders

**Examples:**
- `/Users/jean/Documents/blog-posts/*.md`
- `/Users/jean/Project/chapters/chapter-01.md chapter-02.md`
- `/Users/jean/Writings/short-stories/*.md`

[Provide the file paths]
```

**Wait for user to provide paths.** Read all specified files. Store combined content as `{collected_samples}`.

---

## 4. Word Count Analysis

### 4.1 Display Word Count

```markdown
**📊 Word Count Analysis**

| Metric | Value |
|--------|-------|
| **Total Words** | {count} |
| **Recommended Minimum** | 2000 |
| **Status** | {PASS/ALERT} |
```

### 4.2 Below Minimum Warning

**If word_count < 2000:**

```markdown
⚠️ **Below Recommended Minimum**

You've provided {count} words. While I can proceed, the analysis may be less reliable with fewer samples.

**Recommendations:**
- Consider adding more samples if available
- Or proceed with current samples (results may have wider confidence intervals)

**Would you like to:**
**[A]** Add more samples
**[P]** Proceed with current samples

Please select: [A]dd / [P]roceed
```

**Wait for selection.**

**IF A:** Return to sample collection (Step 2 or 3).
**IF P:** Continue to Step 5.

### 4.3 Minimum Met

**If word_count >= 2000:**

```markdown
✅ **Recommended minimum met!** You've provided {count} words — excellent for reliable analysis.
```

Continue to Step 5.

---

## 5. Optional Preferences Collection

```markdown
**Optional Preferences** (These enhance the analysis, but are not required)

You can skip any of these by pressing Enter, or provide answers to customize your profile:

**1. Genre of Work** (optional)
What genre are you writing in?
- Examples: novel, short fiction, SF, fantasy, memoir, non-fiction, etc.
[Your answer or press Enter to skip]

**2. Context on Samples** (optional)
Any context about when these were written?
- Examples: "Recent work (past month)", "Spanning several years", "Early writing vs recent"
[Your answer or press Enter to skip]

**3. Style Goals** (optional)
Any specific goals for this analysis?
- Examples: "Intentionally evolving my style", "Checking consistency", "Preparing for auto-generation mode"
[Your answer or press Enter to skip]
```

**Collect responses as `{genre}`, `{sample_context}`, `{style_goals}` (or `null` if skipped).**

---

## 6. Collection Summary

```markdown
**✅ Collection Complete!**

| Item | Value |
|------|-------|
| **Samples Collected** | {sample_count} sources |
| **Total Words** | {word_count} |
| **Genre** | {genre or 'Not specified'} |
| **Context** | {sample_context or 'Not specified'} |
| **Goals** | {style_goals or 'Not specified'} |

**Next:** Quantitative analysis (TTR, sentence length, complexity)

**Select:** `[C]` Continue to Quantitative Analysis
```

---

## 7. Output File Creation

Create new style profile file from `{profileTemplate}`:

- Set `date: {current_date}`
- Set `user_name: {user_name}`
- Set `sampleWordCount: {word_count}`
- Set `stepsCompleted: ['step-01-collect']`
- Set `lastStep: 'step-01-collect'`
- Set `profileAccepted: false`

---

## 8. Menu Handling Logic

**For the final menu:**

- IF C: Update {outputFile} frontmatter with stepsCompleted, lastStep, sample metadata, then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

*Procedure document for BMad Book Builder Style Coach - Collection Phase*
