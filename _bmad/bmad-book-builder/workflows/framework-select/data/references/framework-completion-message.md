# Framework Selection Completion Messages

This document contains the completion messages for each step in the Framework Selection workflow.

## Step 1: Story Analysis Complete

```
**✅ Story Analysis Complete!**

| Aspect | Information |
|--------|-------------|
| **Concept** | {story_concept} |
| **Genre** | {story_genre} |
| **Scope** | {story_scope} |
| **Audience** | {target_audience or 'Not specified'} |
| **Experience** | {author_experience or 'Not specified'} |

**Next:** I'll analyze this information and recommend the most suitable narrative frameworks for your story.

**Select:** `[C]` Continue to Framework Recommendations
```

## Step 2: Framework Recommendations Complete

```
**✅ Framework Analysis Complete!**

Based on your {genre} story with {scope} scope, I've analyzed how each framework aligns with your narrative needs.

---

## 🎯 Primary Recommendation

### {Primary Framework Name}

**Suitability:** ⭐⭐⭐ {High/Medium/Low}

**Why It Fits:**
- {Reason 1}
- {Reason 2}
- {Reason 3}

**Considerations:**
- {Consideration 1}
- {Consideration 2}

---

## 📚 Alternative Options

### {Secondary Framework 1}

**Suitability:** ⭐⭐ {Medium/Low}

**Why Consider It:**
- {Reason}
- {Reason}

### {Secondary Framework 2}

**Suitability:** ⭐⭐ {Medium/Low}

**Why Consider It:**
- {Reason}
- {Reason}

### Custom Framework

**Suitability:** Always available

**Why Consider It:**
- Create a structure tailored to your unique storytelling approach
- Blend elements from multiple frameworks
- Ideal if you have specific structural preferences

---

**Next:** I'll explain each framework in detail so you can make an informed choice.

**Select:** `[C]` Continue to Detailed Explanations
```

## Step 3: Framework Explanations Complete

```
**✅ Framework Explanations Complete!**

You now have detailed information about each recommended framework.

---

## 📖 Framework Summary

**{Primary Framework}:**
{3-sentence recap focusing on why it fits this story}

**{Secondary Framework 1}:**
{3-sentence recap focusing on why consider it}

**{Secondary Framework 2}:**
{3-sentence recap focusing on why consider it}

**Custom Framework:**
{3-sentence recap of what custom offers}

---

**Questions?**

If you'd like me to clarify anything about any framework, just ask.

Otherwise, let's move to the final step: making your selection!

**Select:** `[C]` Continue to Framework Selection
```

## Step 4: Framework Selection Complete

```
**✅ Framework Selected!**

Your Choice: **{selected_framework}**

{For standard frameworks:}
This framework will provide {key benefit} for your {genre} story.

{For custom:}
Your custom approach will {unique benefit} for your storytelling style.

---

**Next:** I'll configure this framework for use in the Foundation workflow.

**Select:** `[C]` Continue to Configuration
```

## Step 5: Framework Configuration Complete

```
**✅ Framework Configuration Complete!**

Your framework selection has been configured and saved.

---

## 📋 Configuration Summary

**Selected Framework:** {framework_name}

**File Location:** `{outputFile}`

**What's Included:**
- Complete framework structure ({total beats/stages/steps})
- Foundation integration settings
- Full selection reasoning
- Story analysis and recommendations

---

## 🚀 Next Steps

Your framework is ready for the **Foundation workflow**!

When you run Foundation:
1. It will detect your framework selection
2. Use the structure to guide chapter planning
3. Apply beat/stage labels to your story outline
4. Validate against act breakpoints

**Want to start Foundation now?**
Run: `foundation` workflow (when available)

**Want to change your framework?**
Re-run this workflow anytime to create a new selection.

---

## 📊 Framework Details

**{Framework Name}:**
{Brief recap of key structural elements}

**How Foundation Will Use It:**
- {Integration point 1}
- {Integration point 2}
- {Integration point 3}

---

**Framework Selection Complete!** ✅
```

## Welcome Message

```
**Welcome to Framework Selection!**

I'm your Story Architect, and I'll help you choose the right narrative framework for your story. A good framework provides structure while supporting your creative vision — like a house's architectural style that both guides and enhances the design.

Let's start by understanding your story.

---

**📋 What I'll Learn:**

- Your story concept and type
- Genre and scope
- Target audience
- Your experience level (optional)

**What Happens Next:**

Once I understand your story, I'll:
1. Recommend the most suitable framework(s)
2. Explain what each framework offers
3. Let you choose with full information
4. Configure the framework for use in Foundation

Ready? Let's learn about your story!
```

## Framework Selection Menu

```
**⚡ Framework Selection**

You've learned about each framework and received my recommendations. Now it's time to choose!

---

## 🎯 My Recommendation for You

Based on your {genre} story, I recommend:

**⭐ [{Primary Framework}]**

**Why:**
{Primary recommendation reasoning from Step 2}

**But the final choice is yours!**

---

## 📋 Your Options

**[S]** Save the Cat
{One sentence description}

**[H]** Hero's Journey
{One sentence description}

**[N]** Snowflake Method
{One sentence description}

**[C]** Custom Framework
{One sentence description}

**[?]** Help / Explain More

---

**Your choice:** [S] / [H] / [N] / [C] / [?]
```

## Custom Framework Prompt

```
**🎨 Creating Your Custom Framework**

Excellent! Let's create a framework that fits your unique storytelling approach.

---

**Tell me about your storytelling style.**

For example:
- 'I want three acts with cliffhangers at each chapter end'
- 'I use alternating character POVs, each with their own arc'
- 'I blend mystery structure with romance beats'
- 'I follow a seasonal/cyclical structure'
- 'I use flashbacks and non-linear timelines'

**Describe your approach:**
```
