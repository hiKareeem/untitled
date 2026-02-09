# Profile Acceptance Dialogue Procedure

## 5. Request Explicit Acceptance

Display:

"**🎯 Final Step: Profile Acceptance**

Please review the complete profile at: {outputFile}

When you're ready, confirm acceptance by typing:

**[x] I accept this profile**

This confirms that:
- The profile accurately captures your writing voice
- The examples are representative of your style
- You're ready for Chapter-Write to use this profile for voice mimicry

**Or, if you need changes:**
- Describe what you'd like to adjust
- We can modify before final acceptance"

**Wait for user response.**

## 6. Handle Acceptance or Revision

**IF user accepts:**

Display: "✅ **Profile Accepted!**

Updating frontmatter..."

Load {generatedProfile}, update frontmatter:

```yaml
---
stepsCompleted: ['step-01-collect', 'step-02-analyze-quant', 'step-03-analyze-qual', 'step-04-detect-antipatterns', 'step-05-generate', 'step-06-review']
lastStep: 'step-06-review'
date: {date}
user_name: {user_name}
sampleWordCount: {word_count}
profileAccepted: true
---
```

Save updated profile.

Proceed to completion summary.

**IF user requests changes:**

Discuss the requested changes:
- What aspects need adjustment?
- Are they factual errors (metrics) or subjective (examples)?
- Make reasonable adjustments

After changes, re-present acceptance prompt:
"Changes made. Please review again and confirm:

**[x] I accept this profile**"

**Repeat until user accepts.**

## 7. Present Completion Summary

After acceptance:

"**🎉 Style Capture Complete!**

**Location:** {outputFile}
**Status:** Accepted and ready for use

**What Happens Next:**

Your style profile will be used by:
- **Chapter-Write** — Mimics your voice when generating chapters
- **Review** — Validates quality against your established patterns

**To Update Your Profile:**

If your style evolves over time, you can:
- Run Style Capture again with new samples
- Request re-analysis after manual text modifications
- The workflow will track style evolution in temporal tracking

**Thank you for collaborating!**

Your authentic writing voice has been captured and preserved. Chapter-Write will now maintain consistency across your work."
