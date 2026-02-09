# Framework Selection Procedures

This document outlines the procedures for analyzing stories and selecting appropriate frameworks.

## Step 1: Story Analysis Procedure

### Information Collection

**Required Information:**
1. Story concept/summary
2. Genre

**Optional Information:**
3. Scope (novel/novella/series)
4. Target audience
5. Author experience level

### Collection Methods

**Method 1: Check Existing Files**
- Read `{storyConceptPath}` if exists
- Extract: concept, genre, scope, audience, tone, themes
- Confirm accuracy with author

**Method 2: Direct Prompting**
- Prompt for required information
- Ask specific questions
- Validate minimum requirements

### Validation Rules

**Must Have:**
- ✅ Story concept
- ✅ Genre

**Can Proceed Without:**
- Target audience (optional)
- Experience level (optional)

## Step 2: Framework Analysis Procedure

### Analysis Framework

For each framework, evaluate:

**Save the Cat Analysis:**
- Clear protagonist? (Yes/No)
- Strong external goal? (Yes/No)
- Pacing critical? (Yes/No)
- Genre benefits from beat structure? (Yes/No)
- **Suitability Score:** Count of "Yes" answers

**Hero's Journey Analysis:**
- Transformational arc? (Yes/No)
- Mythic/epic elements? (Yes/No)
- Clear hero/villain dynamic? (Yes/No)
- Genre fits monomyth? (Yes/No)
- **Suitability Score:** Count of "Yes" answers

**Snowflake Method Analysis:**
- Character-driven? (Yes/No)
- Multiple POV characters? (Yes/No)
- Author prefers organic development? (Yes/No)
- Literary vs commercial? (Yes/No)
- **Suitability Score:** Count of "Yes" answers

**Custom Framework Analysis:**
- Author experienced? (Yes/No)
- Story experimental/non-traditional? (Yes/No)
- Blends multiple genres? (Yes/No)
- **Suitability Score:** Count of "Yes" answers

### Ranking Logic

1. Calculate suitability scores for each framework
2. Primary recommendation: Highest score
3. Secondary recommendations: Next highest scores
4. Always include "Custom" as an option
5. Always provide at least 2-3 options

## Step 3: Explanation Procedure

### Presentation Order

1. Primary recommendation (highest ranked)
2. Secondary recommendations
3. Custom framework option

### Explanation Format

For each framework include:
- Brief overview (2-3 sentences)
- Complete structure (list all beats/phases/steps)
- How it works (approach and philosophy)
- Why recommended for this story (specific connections)
- What author will get (concrete benefits)
- Things to consider (potential challenges)
- Example application (brief story-specific example)

### Connection Guidelines

Make specific connections:
- "Your {story_feature} aligns with {framework_feature}"
- "The {framework_element} will help with {story_challenge}"
- "{Another specific connection}"

## Step 4: Selection Procedure

### Menu Presentation

Display options clearly:
- [S] Save the Cat (one-sentence description)
- [H] Hero's Journey (one-sentence description)
- [N] Snowflake Method (one-sentence description)
- [C] Custom Framework (one-sentence description)
- [?] Help / Explain More

### Confirmation Sequence

1. **Initial Selection:** User chooses option
2. **First Confirmation:** "Is this correct? [Y] Yes / [N] No"
3. **Final Confirmation:** "Ready to configure? [C] Yes / [R] Reconsider"

### Custom Framework Flow

1. Present custom framework prompt
2. Collect author's description
3. Repeat back in own words
4. Confirm understanding
5. Allow modifications
6. Final confirmation

### Validation Rules

**Must Have Before Proceeding:**
- ✅ Explicit user choice
- ✅ Confirmed selection
- ✅ Custom description (if custom selected)

## Step 5: Configuration Procedure

### Framework Structure Generation

**Save the Cat Structure:**
- All 15 beats with purposes
- Chapter targets for each beat
- Act assignments
- Act breakpoints: Catalyst, Break into Two, Midpoint, All Is Lost, Break into Three

**Hero's Journey Structure:**
- All 12 stages with purposes
- Chapter targets for each stage
- Phase assignments
- Act breakpoints: Call to Adventure, Crossing the Threshold, Ordeal, Resurrection

**Snowflake Method Structure:**
- All 10 steps with purposes
- Phase assignments
- Output files for each step
- Act breakpoints: One-Page Synopsis, Character Descriptions, Scene List

**Custom Framework Structure:**
- Elements extracted from description
- Purposes for each element
- Application notes
- Empty act breakpoints (Foundation identifies natural breaks)

### Foundation Configuration

Generate settings for Foundation workflow:
- `applyToChapterPlan: true`
- `beatLabelsInPlan: true`
- `actBreakpoints: {framework-specific}`
- `autoProgression: true`
- `validationEnabled: true`

### Output Validation

Verify output contains:
- ✅ `selectedFramework` set
- ✅ `frameworkReasoning` complete and detailed
- ✅ `frameworkStructure` with all beats/stages/steps
- ✅ `foundationConfig` with appropriate settings
- ✅ `storyAnalysis` preserved
- ✅ `recommendations` preserved
- ✅ `stepsCompleted` includes all 5 steps
- ✅ `status: complete`

## Quality Assurance

### Success Metrics

**Step 1 Success:**
- Story information collected
- Minimum required (concept + genre) obtained
- Output file created
- Frontmatter updated

**Step 2 Success:**
- Story analysis loaded
- Framework definitions loaded
- Fit analysis performed
- 2-3+ options provided
- Clear reasoning for each

**Step 3 Success:**
- All frameworks explained
- Structural elements included
- Story-specific connections made
- Clear summary presented

**Step 4 Success:**
- Selection presented with clear menu
- Author made informed choice
- Selection confirmed
- Output file updated

**Step 5 Success:**
- Framework structure complete
- Foundation configuration created
- Output file written
- Output validated
- Summary presented

### Failure Conditions

**Step 1 Failure:**
- Proceeding without story concept
- Proceeding without genre
- Not creating output file

**Step 2 Failure:**
- Not analyzing story attributes
- Providing only one option
- Arbitrary recommendations without reasoning

**Step 3 Failure:**
- Not explaining all frameworks
- Skipping structural details
- Steering toward one option

**Step 4 Failure:**
- Making selection for author
- Proceeding without confirmation
- Not handling custom properly

**Step 5 Failure:**
- Incomplete framework structure
- Missing Foundation configuration
- Output not validated
