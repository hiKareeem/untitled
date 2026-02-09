# Examples & Use Cases

This section provides practical examples for using BMad Book Builder.

---

## Example Workflows

### Example 1: Thomas's Sci-Fi Novel

**Scenario:** Thomas has had a sci-fi novel idea for 7 years — a tech entrepreneur who wakes from cryogenic sleep 278 years later to find Earth regenerated but humanity gone. He's written only 5,000 words.

**Step 1: StyleCapture**
```
/bmad-bbb → SC
```
Thomas uploads his blog posts and a short story. Style Coach analyzes his voice: first-person present, reflective asides, TTR 0.58, concrete imagery.

**Step 2: FrameworkSelect**
```
/bmad-bbb → FO
```
Story Architect recommends Save the Cat for plot-driven sci-fi. Thomas agrees.

**Step 3: Foundation**
```
/bmad-bbb → FD
```
Story Architect asks about protagonist Marc, central conflict, themes. Generates 28-chapter outline with Save the Cat's 15 beats distributed across chapters.

**Step 4: ChapterWrite**
```
/bmad-bbb → CW
```
Thomas selects Chapter 1. Chapter Writer crafts 3,200 words in Thomas's voice. Thomas reads, amazed — it sounds like him, only better.

**Result:** 4 chapters in one week. Thomas feels "finally an author."

---

### Example 2: Marie's Third Thriller

**Scenario:** Marie is a published author working on her third thriller. She wants BBB's consistency tracking.

**Week 1:**
- Runs **BuildCharacters** for 12 characters
- Runs **Foundation** for her existing plot outline
- Runs **StyleCapture** with her previous novels

**Weeks 2-12:**
- Writes 3 chapters/week using **ChapterWrite**
- After each chapter: **BibleUpdate**, **ThemeTracker**, **RhythmAnalysis**, **Review**

**Week 13:**
- Runs **AuditProject** — Continuity Editor reports:
  - ⚠️ Agent Ramirez: Glock 19 in Chapter 7, SIG Sauer P226 in Chapter 14
  - ⚠️ Timeline gap: Chapter 9 says "three days since bombing," Chapter 10 starts "next morning"

Marie fixes these in an hour. *This would have taken her beta readers weeks to catch.*

---

### Example 3: Sofia's Family Saga

**Scenario:** Sofia is 60,000 words into a family saga. Something feels off, but she can't identify it.

**Diagnosis:**
Sofia runs **RhythmAnalysis** on chapters 10-15. The Rhythm Monitor generates a tension curve visualization:

```
Tension Curve — Chapters 10-15:
10: ████████░░ 8/10 — Family crisis peaks
11: ██████░░░░ 6/10 — Resolution begins
12: ████░░░░░░ 4/10 — Continues resolving...
13: ████░░░░░░ 4/10 — Still flat...
14: ████░░░░░░ 4/10 — Why isn't this moving?
15: █████░░░░░ 5/10 — Finally...
```

*"Your tension is flatlining across five chapters. You resolved the central conflict in Chapter 11, but you have 5 more chapters before the next plot point. The reader is disengaging."*

**Solution:** Either introduce a B-story complication (Chapter 12), compress Chapters 12-14 into one chapter (accelerate), or add foreshadowing (raise stakes even in quiet moments).

**Result:** Sofia realizes she's been filling space. The BBB agent just saved her from 20,000 words of dead narrative.

---

## Common Scenarios

### Scenario: "I have an idea but don't know where to start"

**Solution:** Use **Foundation** workflow
- Story Architect will ask guided questions
- Framework selection provides structure
- Chapter breakdown gives you a roadmap

### Scenario: "I'm stuck on Chapter 5"

**Solution:** Use **ChapterWrite** with your existing plan
- Chapter Writer continues from where you are
- Maintains all continuity with previous chapters
- Follows your established chapter plan

### Scenario: "I think I have a continuity problem"

**Solution:** Use **Review** workflow
- Continuity Editor identifies specific issues
- Provides examples from your text
- Suggests actionable fixes

### Scenario: "I want to check my pacing"

**Solution:** Use **RhythmAnalysis**
- Visualizes tension curves
- Identifies flat spots
- Recommends pacing improvements

### Scenario: "I need to reference my story details"

**Solution:** Use **ExportBible**
- Generates complete reference document
- Characters, locations, objects, timeline
- Perfect for reviewing while writing

---

## Tips & Tricks

### Tip 1: Run StyleCapture Early

Before writing your first chapter, provide BBB with your writing samples. The more it learns your voice, the better it can match it.

**What to provide:**
- Blog posts
- Short stories
- Previous chapters (if continuing a work)
- Any writing that sounds like *you*

### Tip 2: Use BuildCharacters Before Foundation

Character dossiers inform story structure. When Story Architect knows your protagonist's psychology, it can create a more targeted chapter plan.

### Tip 3: Run BibleUpdate After Every Chapter

Don't wait until you've written 10 chapters. Tracking elements continuously prevents compounding errors.

### Tip 4: Check Rhythm Mid-Project

Don't wait until the end. Run RhythmAnalysis after every 5-10 chapters to catch pacing problems early.

### Tip 5: Audit Before Final Revision

Run AuditProject before your final revision pass. This ensures you're fixing the right problems.

---

## Troubleshooting

### Common Issues

**Issue: "The chapter doesn't sound like me"**

Solution:
- Run StyleCapture with more recent writing samples
- Provide specific feedback to Chapter Writer about what doesn't match
- Review your style profile for accuracy

**Issue: "I'm getting continuity errors"**

Solution:
- Run BibleUpdate to refresh tracking
- Review your character dossiers
- Check that previous chapters were tracked properly

**Issue: "My pacing feels off"**

Solution:
- Run RhythmAnalysis to identify the problem
- Check tension curve for flat spots or rushed sections
- Consider whether action/reflection is balanced

**Issue: "BBB doesn't understand my story"**

Solution:
- Be more specific in Foundation when describing your story
- Provide examples of similar stories you admire
- Use targeted questions to clarify your vision

---

## Milestone Celebrations

BBB celebrates your progress:

- **10,000 words:** *"You've crossed the threshold into serious writing. Hemingway said 'The first draft of anything is sh*t.' You're past that. Keep refining."*

- **50,000 words:** *"A novel! You've written a novel. That's something most people only dream of."*

- **100,000 words:** *"Epic territory. You're in the company of Tolstoy, King, and Rowling. Now: make it count."*

---

## Getting More Help

- Review the main BMAD documentation
- Check module configuration in module.yaml
- Verify all agents and workflows are properly installed
- Consult the agent and workflow specs for detailed implementation information

---

**Remember:** BBB is AI-assisted, not AI-generated. You are the author. BBB is your team at Second Chance Press, here to help you finally write that book.
