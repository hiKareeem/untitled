# Anti-Patterns Detection Guide
# Common writing pitfalls and how to fix them

> **Purpose:** This document contains the comprehensive list of anti-patterns (24 Humanizer patterns) used by Style Coach to detect and suggest improvements for common writing issues.

---

## Overview

Anti-patterns are common writing pitfalls that weaken prose. This guide draws from the **Humanizer** tool (https://github.com/blader/humanizer) and identifies patterns to avoid along with specific alternatives.

**Note:** These are generic patterns, not judgments of an author's unique voice. Awareness helps writers strengthen their prose.

---

## 1. Excessive Adverbs

### Problem
Adverbs, especially -ly words, often indicate weak verb choice.

### Patterns to Detect
- **-ly adverbs:** quickly, slowly, softly, loudly, angrily, happily, sadly, etc.
- **Intensifiers:** very, really, extremely, absolutely, quite, rather, somewhat
- **Vague modifiers:** slightly, a bit, a little, somewhat, rather

### Detection Procedure
1. Scan for adverb patterns in text
2. For each overused pattern, extract 1-2 examples
3. Provide stronger verb alternatives

### Example Transformations
- "He walked **slowly** down the hall" → "He **sauntered** down the hall"
- "She was **very** angry" → "She **fumed**"
- "He **really** wanted to go" → "He **yearned** to go"
- "She spoke **softly**" → "She **whispered**"
- "He looked **angrily** at her" → "He **glared** at her"

### Storage Format
```yaml
excessive_adverbs:
  - pattern: "[adverb or intensifier]"
    examples:
      - original: "[sentence with adverb]"
        alternative: "[stronger verb replacement]"
```

### Minimum Detection
3 patterns (or note "none detected")

---

## 2. Passive Voice Overuse

### Problem
Passive voice hides the actor and weakens sentences.

### Patterns to Detect
- "to be" + past participle (was written, were told, had been seen)
- Hidden subjects (by [agent] phrases)
- Stative constructions lacking agency

### Detection Procedure
1. Scan for passive voice markers
2. Extract examples where passive voice weakens the sentence
3. Provide active voice alternatives

### Example Transformations
- "The letter **was written by** John" → "John **wrote** the letter"
- "Mistakes **were made**" → "We **made** mistakes"
- "The decision **has been made**" → "I **decided**"
- "It **was agreed that**..." → "We **agreed** that..."
- "The castle **was surrounded**" → "Enemy troops **surrounded** the castle"

### Storage Format
```yaml
passive_voice_overuse:
  - pattern: "[passive construction]"
    examples:
      - original: "[passive sentence]"
        alternative: "[active alternative]"
```

### Minimum Detection
3 examples (or note "acceptable use - no overuse detected")

---

## 3. Cliché Phrases

### Problem
Overused expressions that lack originality.

### Patterns to Detect
- **Time-worn metaphors:** quiet as a mouse, cold as ice, hard as a rock
- **Overused idioms:** bite the bullet, play it safe, at the end of the day
- **Generic descriptions:** tall, dark, and handsome, dead of night, in the nick of time
- **Stock phrases:** a deep guttural laugh, eyes like pools, heart pounded like a drum

### Detection Procedure
1. Scan for cliché patterns
2. For each cliché detected, extract example
3. Provide fresh, original alternatives

### Example Transformations
- "Quiet as a **mouse**" → "Quiet as a **breath held**"
- "Dead of **night**" → "The hour when **sleepers turn**"
- "**Heart pounded like a drum**" → "Heart **hammered against ribs**"
- "**Eyes like pools**" → "Eyes **holding depths uncharted**"
- "**At the end of the day**" → "When all is said and done" or delete entirely

### Storage Format
```yaml
cliche_phrases:
  - phrase: "[cliché expression]"
    examples:
      - original: "[sentence with cliché]"
        alternative: "[fresh alternative]"
```

### Minimum Detection
3 clichés (or note "few clichés detected - original language used")

### Note
Use web search to verify if phrases are common clichés if uncertain.

---

## 4. Generic Dialogue

### Problem
Dialogue that feels unnatural, on-the-nose, or lacking in subtext.

### Patterns to Detect
- **Unnatural exposition:** "As you know, Bob..." (information dumping)
- **On-the-nose emotions:** "I am very sad right now"
- **Uniform character voices:** everyone sounds the same
- **Lack of subtext or tension:** characters say exactly what they mean
- **Overly formal:** speech patterns that don't match natural conversation

### Detection Procedure
1. Scan for generic dialogue patterns
2. Extract examples where dialogue could be more specific or natural
3. Provide improvement suggestions

### Example Transformations
- "I am very angry at you right now" → "Don't. Don't even **look** at me."
- "As you know, the castle is under attack" → "They're **at the gates**."
- "Hello, my name is John and I am here to help you" → "John. I can help."
- "I love you so much and I never want to leave you" → "Stay. Please."
- "**I do not think that is a good idea**, he said" → "**Bad idea**, he said."

### Storage Format
```yaml
generic_dialogue:
  - pattern: "[generic dialogue issue]"
    examples:
      - original: "[generic dialogue line]"
        alternative: "[specific, natural alternative]"
```

### Minimum Detection
3 examples (or note "dialogue feels natural - no generic patterns detected")

### Note
This applies only if dialogue exists in samples.

---

## 5. Slop Patterns

### Problem
Lazy writing that lacks precision or care.

### Patterns to Detect

#### 5.1 Vague Pronouns
- **it, this, that** without clear antecedents
- **Ambiguous references:** "It was a thing that happened"

#### 5.2 Noun Strings
- **Noun stacks without prepositions:** "computer screen light reflection"
- **Better:** "reflection of the light from the computer screen"

#### 5.3 Wordy Phrases
- "in order to" → "to"
- "due to the fact that" → "because"
- "at this point in time" → "now"
- "in the event that" → "if"
- "for the purpose of" → "to"

#### 5.4 Filler Words
- "basically" (when not actually basic)
- "actually" (when not factual)
- "literally" (when not literal)
- "just" (unnecessary qualifier)

#### 5.5 Weak Sentence Starters
- "There is/are/was/were..."
- "It is/was..."
- "There seems to be..."

### Detection Procedure
1. Scan for slop markers
2. Extract examples with specific alternatives
3. Provide precise, concise alternatives

### Example Transformations
- "In order to succeed" → "To succeed"
- "It was a thing that happened" → "This happened"
- "Due to the fact that he was late" → "Because he was late"
- "There are many people who think" → "Many think"
- "I just wanted to say" → "I wanted to say" or "I wanted to tell you"
- "He literally exploded with anger" → "He exploded with anger" (metaphor)

### Storage Format
```yaml
slop_patterns:
  - pattern: "[slop type]"
    examples:
      - original: "[sloppy phrase]"
        alternative: "[precise alternative]"
```

### Minimum Detection
3 patterns (or note "precise writing - no slop detected")

### Reference
Humanizer tool patterns for comprehensive slop detection.

---

## 6. Humanizer Tool Patterns (24 Total)

### From https://github.com/blader/humanizer

The Humanizer tool identifies these specific anti-slop patterns:

1. **Basically** - Unnecessary qualifier
2. **Vague pronouns** - it/this/that without clear reference
3. **Noun strings** - Stacked nouns without prepositions
4. **Wordy phrases** - in order to, due to the fact that
5. **There is/are** - Weak sentence construction
6. **It is** - Weak sentence construction
7. **Just** - Unnecessary filler
8. **Actually** - Unnecessary filler
9. **Literally** - Misused metaphorically
10. **Very** - Weak intensifier
11. **Really** - Weak intensifier
12. **Extremely** - Weak intensifier
13. **Absolutely** - Weak intensifier
14. **Quite** - Weak intensifier
15. **Rather** - Weak intensifier
16. **Somewhat** - Weak intensifier
17. **Slightly** - Weak intensifier
18. **A bit** - Weak intensifier
19. **-ly adverbs** - Indicate weak verb choice
20. **Passive voice** - to be + past participle
21. **Cliché phrases** - Overused expressions
22. **Generic dialogue** - Unnatural speech patterns
23. **Show vs tell issues** - Telling instead of showing
24. **Filler phrases** - Unnecessary padding

---

## Detection Priority

For Style-Capture workflow, analyze in this order:

1. **Excessive Adverbs** (High impact, easy to fix)
2. **Passive Voice** (High impact, structural)
3. **Cliché Phrases** (Medium impact, creative)
4. **Generic Dialogue** (Medium impact, if applicable)
5. **Slop Patterns** (Low-High impact, precision issues)

---

## Storage Structure

All anti-patterns should be stored in this unified structure:

```yaml
anti_patterns:
  excessive_adverbs:
    - pattern: "[pattern]"
      examples:
        - original: "[example]"
          alternative: "[better version]"

  passive_voice_overuse:
    - pattern: "[pattern]"
      examples:
        - original: "[example]"
          alternative: "[better version]"

  cliche_phrases:
    - phrase: "[cliché]"
      examples:
        - original: "[example]"
          alternative: "[fresh alternative]"

  generic_dialogue:
    - pattern: "[issue]"
      examples:
        - original: "[example]"
          alternative: "[better version]"

  slop_patterns:
    - pattern: "[slop type]"
      examples:
        - original: "[example]"
          alternative: "[precise alternative]"
```

---

## Usage Notes

- **Diagnostic, not judgmental:** These are common pitfalls, not author-specific flaws
- **Representative examples:** Extract 1-2 examples per pattern type
- **Actionable alternatives:** Always provide specific, better alternatives
- **Categorization:** Use the 5 main categories above
- **Minimum thresholds:** 3 examples per category, or note "none detected"

---

*Reference document for BMad Book Builder Style Coach - Anti-Pattern Detection*
