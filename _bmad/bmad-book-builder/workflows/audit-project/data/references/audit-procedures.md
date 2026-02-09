# Audit Procedures Reference

## Overview

This document contains the detailed procedures for executing the comprehensive project audit workflow. It outlines the specific protocols, checks, and validation steps used across all audit phases.

## Loading Procedures

### Manuscript Chapter Loading

**Scope: All Chapters**
- Scan `{chaptersFolder}` for `chapter-*.md` pattern
- Extract: number, title, content, word count, modification date
- Store as: `chapter_{N}_data` with complete metadata
- Sort into: `manuscript_chapters` array

**Scope: Selected Chapters**
- Load only chapters specified in `targetChapters`
- For each chapter number in `targetChapters`:
  - Check existence of `chapter-{N}.md`
  - IF exists: Read content, metadata
  - IF missing: Note as missing, continue
- Store sorted: `manuscript_chapters` array

### Living Bible Dimension Loading

**Standard Dimensions:**
1. **Chronologie (Timeline)**: `{bibleFolder}/chronologie.md` or `timeline.md`
2. **Lieux (Locations)**: `{bibleFolder}/lieux.md` or `locations.md`
3. **Objets (Objects)**: `{bibleFolder}/objets.md` or `objects.md`
4. **Personnes (Characters)**: `{bibleFolder}/personnes.md` or `characters.md`
5. **Themes (Thematic)**: `{bibleFolder}/themes.md` or `thematic.md`

**Storage Format:**
- Found: `bible_{dimension}: {exists: true, content, modified_date}`
- Missing: `bible_{dimension}: {exists: false}`

### Previous Reports Loading

**Review Reports:**
- Pattern: `review-*.md`, `review-report-*.md`
- Extract: date, scope, issues count, key findings
- Store as: `review_report_{date}_data`
- Sort by date: `previous_reviews` array

**Character Audits:**
- Pattern: `character-audit-*.md`, `audit-*.md`
- Extract: character name, audit date, arc phase, findings
- Store as: `character_audit_{name}_data`
- Sort by character: `character_audits` array

## Narrative Arc Analysis Procedures

### Story Structure Assessment

**Narrative Phases Identification:**
- Exposition/Setup (beginning)
- Inciting Incident
- Rising Action
- Climax
- Falling Action
- Resolution

**For each phase:**
- Note presence/absence
- Identify chapter location(s)
- Assess effectiveness
- Store as: `narrative_phases` with phase_name, present, location, quality

**Arc Completion Analysis:**
- Assess completion percentage (0-100%)
- Identify incomplete elements
- Note missing structural components
- Store as: `arc_completion` with completion_percentage, missing_elements, assessment

### Pacing Evaluation

**Per-Chapter Pacing:**
- Assess: too slow / balanced / too fast
- Note pacing changes between chapters
- Identify inconsistencies
- Store as: `pacing_by_chapter` with chapter_number, pacing_assessment, notes

**Overall Pacing Problems:**
- Rushed sections (events unfold too quickly)
- Dragging sections (slow progress, excessive detail)
- Pacing inconsistencies (abrupt changes without justification)
- Store as: `pacing_assessment` with overall_pacing, issues_found, recommendations

**Rhythm and Flow:**
- Assess narrative rhythm between chapters
- Note smooth transitions vs. jarring jumps
- Identify flow interruptions
- Store as: `rhythm_flow` with flow_quality, issues, examples

### Setup/Payoff Tracking

**Setup Identification:**
- Track: foreshadowing, mysteries, character goals, plot elements
- For each: note chapter location, type, expected payoff
- Store as: `setups` with setup_description, chapter, type, payoff_status

**Payoff Identification:**
- Track delivered payoffs
- For each: note chapter location, type, setup_reference
- Store as: `payoffs` with payoff_description, chapter, type, setup_reference

**Validation:**
- Match payoffs to setups
- Identify orphaned setups (setup without payoff)
- Identify unearned payoffs (payoff without proper setup)
- Store as: `setup_payoff_analysis` with matched_pairs, orphaned_setups, unearned_payoffs

## Coherence Validation Procedures

### Character Consistency Checks

**For each major character:**
- Track all appearances across chapters
- Validate voice consistency (dialogue patterns, speech patterns, tone)
- Validate behavior consistency (personality, reactions, decisions)
- Validate physical description consistency
- Store as: `character_{name}_coherence` with appearances, voice_consistency, behavior_consistency, description_consistency, issues_found

**Knowledge and Memory:**
- Validate character knowledge continuity
- Identify: forgetting past events, knowing things they shouldn't
- Store as: `character_knowledge_coherence` with character_name, knowledge_issues

**Relationship Consistency:**
- Validate relationship consistency across manuscript
- Identify relationship status changes
- Verify changes are intentional/justified
- Store as: `character_relationship_coherence` with relationship, consistency_status, changes

**Bible Cross-Reference:**
- IF bible_personnes exists: Compare bible vs. manuscript character details
- Identify discrepancies
- Store as: `character_bible_discrepancies` with character_name, discrepancies

### Location Validation

**For each location:**
- Track all appearances across chapters
- Validate description consistency (layout, features, atmosphere)
- Validate geographic consistency (distances, directions, relationships)
- Identify description changes
- Store as: `location_{name}_coherence` with name, appearances, description_consistency, geographic_consistency, issues_found

**Spatial and Movement:**
- Validate character movements between locations
- Check travel times and distances
- Identify impossible movements or timeline violations
- Store as: `spatial_movement_coherence` with movement_issues, timeline_violations

**Bible Cross-Reference:**
- IF bible_lieux exists: Compare bible vs. manuscript location details
- Store as: `location_bible_discrepancies` with location_name, discrepancies

### Object Tracking

**For each significant object:**
- Track all appearances across chapters
- Validate presence continuity (object exists when it should)
- Validate state changes (verify logical/documented)
- Identify objects appearing/disappearing without explanation
- Store as: `object_{name}_coherence` with name, appearances, presence_consistency, state_changes, issues_found

**Special/Magical Objects:**
- Validate rule-following for special objects
- Identify rule violations or inconsistencies
- Store as: `special_object_rules` with object_name, rule_violations

**Bible Cross-Reference:**
- IF bible_objets exists: Compare bible vs. manuscript object details
- Store as: `object_bible_discrepancies` with object_name, discrepancies

### Timeline Validation

**Event Sequence:**
- For each major event: Track temporal placement
- Validate sequence (logical order)
- Identify temporal inconsistencies
- Store as: `event_sequence_coherence` with event, temporal_placement, sequence_issues

**Duration and Timing:**
- Validate event duration consistency
- Validate time gaps between events
- Identify timing inconsistencies
- Store as: `timing_coherence` with timing_issues, duration_inconsistencies

**Temporal Shifts:**
- Validate temporal markers for flashbacks/flashforwards
- Ensure temporal shifts are clearly marked
- Identify confusing temporal jumps
- Store as: `temporal_shift_handling` with flashback_issues, flashforward_issues

**Bible Cross-Reference:**
- IF bible_chronologie exists: Compare bible vs. manuscript timeline
- Store as: `timeline_bible_discrepancies` with event, discrepancies

### Plot Hole Detection

**Narrative Gaps:**
- Identify missing information critical to plot
- Note unresolved plot threads
- Identify logic gaps
- Store as: `narrative_gaps` with gap_description, location, severity

**Logic Inconsistencies:**
- Identify contradictory events or statements
- Note character actions contradicting motivations
- Identify cause/effect violations
- Store as: `logic_inconsistencies` with inconsistency_description, location, severity

**Unresolved Elements:**
- Track unresolved plot threads
- Identify dropped storylines
- Note unanswered questions
- Store as: `unresolved_elements` with element_description, location, priority

## Quality Assessment Procedures

### Style Consistency Evaluation

**Narrative Voice:**
- Assess voice consistency across manuscript
- Identify voice shifts (determine if intentional)
- Note register changes (formal/casual, poetic/terse)
- Store as: `narrative_voice` with voice_description, consistency_score, shifts, issues

**Tone Consistency:**
- Evaluate tone consistency (humorous/serious, dark/light)
- Identify inappropriate tone shifts
- Note tonal misalignments with content
- Store as: `tone_consistency` with overall_tone, consistency_issues, misalignments

**Style Register:**
- Assess writing style register across manuscript
- Identify style inconsistencies (sentence patterns, word choice)
- Note jarring style changes
- Store as: `style_register` with register_description, consistency_issues

### Dialogue Quality Assessment

**Character Voice Distinctiveness:**
- For each major character: Assess dialogue voice uniqueness
- Identify characters with unique vs. generic dialogue
- Note voice blending (characters sounding alike)
- Store as: `dialogue_voice_distinctiveness` with character_name, voice_quality, distinctiveness_score, issues

**Dialogue Naturalness:**
- Assess dialogue naturalness and authenticity
- Identify stilted or artificial dialogue
- Note on-the-nose speeches (excessive exposition)
- Store as: `dialogue_naturalness` with overall_quality, issues, examples

**Subtext and Depth:**
- Evaluate dialogue for subtext and depth
- Identify dialogue that says too much directly
- Note effective subtext examples
- Store as: `dialogue_subtext` with subtext_quality, effective_examples, improvement_opportunities

**Dialogue Mechanics:**
- Check dialogue tag usage (said/booked vs. creative tags)
- Identify formatting issues
- Note action beat effectiveness
- Store as: `dialogue_mechanics` with mechanics_quality, issues, recommendations

### Prose Metrics Analysis

**Vocabulary Variety:**
- Assess word choice variety
- Identify repetitive words or phrases
- Note overused words (especially in close proximity)
- Store as: `vocabulary_variety` with variety_score, overused_words, recommendations

**Sentence Structure:**
- Analyze sentence pattern variety
- Identify repetitive sentence structures
- Note sentence length variety
- Store as: `sentence_structure` with variety_score, repetitive_patterns, recommendations

**Readability:**
- Evaluate overall readability
- Assess sentence complexity and paragraph length
- Identify readability issues (run-ons, fragments, confusion)
- Store as: `readability` with readability_score, issues, examples

**Show vs Tell Balance:**
- Evaluate show vs tell balance
- Identify excessive telling
- Note effective show examples
- Store as: `show_vs_tell` with balance_score, tell_heavy_sections, show_examples

### Thematic Coherence

**Theme Presence:**
- IF theme tracking exists: Cross-reference with manuscript
- IF no tracking: Identify themes through analysis
- Track theme presence across chapters
- Assess theme development
- Store as: `theme_presence` or `identified_themes` with theme_name, presence_score, progression, issues

**Thematic Consistency:**
- Validate thematic consistency with story events
- Identify thematic contradictions
- Note effective reinforcement moments
- Store as: `thematic_consistency` with consistency_score, contradictions, effective_moments

**Symbol and Motif Tracking:**
- Identify symbols and motifs
- Track recurrence and development
- Assess effectiveness and clarity
- Store as: `symbols_motifs` with symbol_name, recurrence, development, effectiveness

**Bible Cross-Reference:**
- IF bible_themes exists: Compare themes in bible vs. manuscript
- Store as: `theme_bible_comparison` with alignment, discrepancies

## Report Synthesis Procedures

### Historical Analysis

**Review History:**
- Extract key findings from all previous reviews
- Track issue types and frequencies
- Identify: recurring issues, resolved issues, new issues
- Store as: `review_history_analysis` with total_reviews, recurring_issues, resolved_issues, new_issues, trends

**Quality Trend:**
- Track quality scores over time
- Identify improvement or decline trends
- Note significant shifts
- Store as: `quality_trend` with trend_direction, significant_changes, trajectory

**Character Audit Synthesis:**
- Extract arc phase, issues, recommendations from audits
- Track character arc progression
- Identify development patterns
- Store as: `character_audit_synthesis` with character_name, audit_history, arc_progression, recurring_issues

### Systemic Pattern Recognition

**Cross-Workflow Patterns:**
- Identify issues appearing across multiple dimensions
- Note systemic weaknesses
- Store as: `systemic_patterns` with pattern_name, appears_in, severity, examples

**Workflow Alignment:**
- Identify misalignments between workflow findings
- Note contradictions or discrepancies
- Store as: `workflow_alignment` with misalignments, contradictions

**Strength Patterns:**
- Identify consistent strengths across all dimensions
- Note what author does well
- Store as: `strength_patterns` with strength_type, appears_in, examples

### Data Currency Assessment

**Living Bible Currency:**
- For each dimension: Assess currency (up to date / needs update / missing)
- Note which dimensions need updating
- Store as: `bible_currency` with dimension_name, currency_status, coverage

**Tracking Data Currency:**
- Assess currency of all tracking data
- Note which tracking needs updating
- Store as: `tracking_currency` with tracking_type, currency_status, last_updated

**Audit Currency:**
- Assess currency of character audits
- Note which characters need fresh audits
- Store as: `audit_currency` with character_name, currency_status, last_audited

## Scoring Calculations

### Narrative Arc Health Score (0-100)

**Breakdown:**
- Story structure completeness: 20 points
- Arc completion: 20 points
- Pacing quality: 20 points
- Character arc progression: 15 points
- Setup/payoff validity: 15 points
- Transition quality: 10 points

**Assessment Labels:**
- 90-100: Excellent — Strong narrative arc with minimal issues
- 75-89: Good — Solid narrative arc with minor weaknesses
- 60-74: Fair — Functional arc with notable issues
- 40-59: Poor — Significant structural problems
- 0-39: Critical — Major narrative arc failures

### Coherence Health Score (0-100)

**Breakdown:**
- Character consistency: 30 points
- Location accuracy: 20 points
- Object tracking: 15 points
- Timeline validation: 20 points
- Plot hole absence: 15 points

**Assessment Labels:**
- 90-100: Excellent — Minimal coherence issues
- 75-89: Good — Minor inconsistencies
- 60-74: Fair — Notable coherence problems
- 40-59: Poor — Significant continuity errors
- 0-39: Critical — Major coherence failures

### Quality Health Score (0-100)

**Breakdown:**
- Style consistency: 20 points
- Dialogue quality: 25 points
- Prose metrics: 25 points
- Thematic coherence: 20 points
- Quality pattern strength: 10 points

**Assessment Labels:**
- 90-100: Excellent — Consistently high-quality prose
- 75-89: Good — Solid writing with minor issues
- 60-74: Fair — Competent but notable quality concerns
- 40-59: Poor — Significant quality problems
- 0-39: Critical — Major quality failures

### Overall Project Health Score (0-100)

**Weighted Average:**
- Narrative Arc Health Score: 25%
- Coherence Health Score: 30%
- Quality Health Score: 25%
- Historical Progress: 10%
- Data Currency: 10%

**Formula:**
```
overall_health_score = (narrative_arc_score * 0.25) +
                       (coherence_score * 0.30) +
                       (quality_score * 0.25) +
                       (progress_score * 0.10) +
                       (currency_score * 0.10)
```

**Assessment Labels:**
- 90-100: Excellent — Ready for final polish
- 75-89: Good — Minor improvements needed
- 60-74: Fair — Notable issues requiring attention
- 40-59: Poor — Substantial work required
- 0-39: Critical — Comprehensive revision needed

## Issue Severity Classification

**Critical Issues:**
- Must fix before finalizing
- Break narrative logic or credibility
- Confuse readers significantly
- Undermine story structure

**Major Issues:**
- Should fix before publishing
- Noticeable problems affecting reading experience
- Inconsistencies that distract
- Gaps in development

**Minor Issues:**
- Polish before final
- Small inconsistencies or weaknesses
- Stylistic improvements
- Editorial refinements
