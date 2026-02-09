# Web Verification Templates

## Verification Plan Presentation Template

Display:

"**📋 Web Verification Plan**

Unverified claims found: {total}

### Auto-Verify ({auto_count})

**High-Stakes ({high_count}):**
{list of high-stakes claims}
- Example: T00X: {claim} — {reason}

**Medium-Stakes ({medium_count}):**
{list of medium-stakes claims}
- Example: F00Y: {claim} — {reason}

These will be automatically verified via web search.

### User Choice Needed ({low_count})

**Low-Stakes ({low_count}):**
{list of low-stakes claims}
- Example: L00Z: {claim} — {reason}

These are minor details. Verify them or skip?"

## Verification Plan Confirmation Prompt

"Proceed with auto-verification of {auto_count} claims?

**[Y]es** — Auto-verify all high and medium-stakes claims
**[N]o** — Review all claims individually
**[R]eview** — Show detailed list before deciding

Your choice: "

### Response Handling

#### **[Y] YES — Auto-Verify**
Skip to Step 5 (Execute Web Verification)

#### **[N] NO — Review Individually**
Present detailed claim list with checkboxes, process user input, update auto-verify list accordingly.

#### **[R] REVIEW — Show Detailed List**
Present detailed list with claim excerpts and verification rationale, then return to confirmation prompt.

## Web Verification Results Presentation Template

Display:

"**✅ Web Verification Complete**

### Verification Results

**Web Searches Performed:** {searches}
**Sources Consulted:** {sources}

| Result | Count | Claims |
|--------|-------|--------|
| ✅ Verified | {verified} | {list} |
| ❌ Contradicted | {contradicted} | {list} |
| 📝 Partial Match | {partial} | {list} |
| ❓ Uncertain | {uncertain} | {list} |

### Verified Claims
{list of newly verified claims with sources}

### Contradicted Claims (New Issues)
{list of claims contradicted by web sources}

### Partial Matches
{list of partially accurate claims}

### Uncertain Claims
{list of claims with insufficient or conflicting sources"
