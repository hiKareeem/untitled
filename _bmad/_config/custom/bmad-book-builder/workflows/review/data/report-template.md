---
chapter_id: "{chapter_id}"
book: "{book_number}"
date: "{date}"
word_count: "{word_count}"
reviewers:
  - adversarial
  - editorial
  - forward-continuity  # if enabled
severity_counts:
  critical: 0
  major: 0
  minor: 0
total_findings: 0
overall_assessment: ""
---

# Review Report: {chapter_id}

## Executive Summary

**Chapter:** {chapter_id}
**Date:** {date}
**Word Count:** {word_count}
**Total Findings:** {total_findings} ({critical}C / {major}M / {minor}m)
**Overall Assessment:** {one_sentence}

### Triage Priorities

1. {highest_impact_finding_1}
2. {highest_impact_finding_2}
3. {highest_impact_finding_3}
4. {highest_impact_finding_4}
5. {highest_impact_finding_5}

---

## Section 1: Adversarial Review

> *Reviewer perspective: hostile reader, no project context, chapter assessed on standalone merits*

### Critical Findings

{adversarial_critical_findings}

### Major Findings

{adversarial_major_findings}

### Minor Findings

{adversarial_minor_findings}

---

## Section 2: Editorial Review

> *Reviewer perspective: substantive editor, style profile reference*

### 1. Sentence Rhythm & Variety

{editorial_rhythm_findings}

### 2. Word Choice & Precision

{editorial_word_choice_findings}

### 3. Clarity & Readability

{editorial_clarity_findings}

### 4. Emotional Precision

{editorial_emotion_findings}

### 5. Scene-Level Pacing

{editorial_pacing_findings}

### 6. Voice Consistency

{editorial_voice_findings}

---

## Section 3: Forward Continuity (if enabled)

> *Reviewer perspective: continuity editor who has read the full series, checking forward setup/payoff*

### Thread Tracking

| Thread/Element | Established In | Paid Off In | Status |
|---------------|---------------|-------------|---------|
{thread_tracking_table}

### Critical Findings (contradictions, broken continuity)

{continuity_critical_findings}

### Major Findings (missing setups, dropped threads)

{continuity_major_findings}

### Minor Findings (foreshadowing opportunities)

{continuity_minor_findings}

### Arc Coherence Assessment

{arc_coherence_assessment}

---

## Cross-Reviewer Patterns

{patterns_identified_across_both_reviewers}

---

## Resolution Tracking

- [ ] {finding_1_resolution}
- [ ] {finding_2_resolution}
- [ ] {finding_3_resolution}
{...continue for all critical and major findings...}
