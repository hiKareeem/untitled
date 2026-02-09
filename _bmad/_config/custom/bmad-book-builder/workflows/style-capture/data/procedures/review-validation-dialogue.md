# Style Review Validation Dialogue Procedure

## 1. Initialize Review

Display:

"**📋 Author Review Step**

Welcome to the final review! Your style profile has been generated based on analysis of your writing samples.

**This step has two purposes:**
1. **Validate examples** — Review qualitative patterns and anti-patterns to ensure they feel representative of your voice
2. **Accept profile** — Confirm that the profile accurately captures your writing voice

You can remove any examples that don't feel right. Metrics (TTR, sentence length, etc.) are factual calculations and should not be changed.

Let's start by reviewing the qualitative examples."

## 2. Present Qualitative Examples for Validation

Load {generatedProfile} and extract qualitative examples section.

Display each category with examples:

"**Favorite Words Validation**

These words were identified as frequently used or characteristic in your writing:

{Display each favorite word with examples}

**For each word, ask:**
- Does this feel representative of your voice?
- Should any be removed?

Please respond with:
- The numbers of any words to remove (e.g., "remove 2, 5")
- Or "keep all" if all feel representative"

**Wait for user response.**

**IF user requests removals:**
- Remove specified words from {generatedProfile}
- Update the profile file
- Confirm: "Removed {count} word(s). Any others to remove?"

**Repeat for each qualitative category:**

"**Characteristic Phrases Validation**

{Display each phrase with examples}

Ask: "Which phrases should be removed? (numbers or 'keep all')"

"**Imagery Themes Validation**

{Display each theme with examples}

Ask: "Which themes should be removed? (numbers or 'keep all')"

"**Transition Patterns Validation**

{Display each pattern with examples}

Ask: "Which patterns should be removed? (numbers or 'keep all')"

## 3. Present Anti-Patterns for Review

"**Anti-Patterns Review**

These patterns were detected as areas for improvement. They don't diminish your voice — they're common writing pitfalls to be aware of.

{Display each anti-pattern category with examples}

**Note:** These are generic patterns to avoid, not judgments of your voice. They serve as guidance for stronger writing.

Ask: "Do any of these anti-patterns feel incorrect or mischaracterized? If so, let me know which ones to remove."

**IF user flags items:**
- Discuss the flagged item
- Determine if it's truly a mischaracterization
- Remove if agreed, or explain why it's included
