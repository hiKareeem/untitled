# Reference Check Success/Failure Metrics

## SUCCESS Metrics

- Research dossier directory scanned
- Available dossiers identified
- Claims matched to dossiers by keywords/topics
- Relevant dossiers read and facts extracted
- Claim statuses updated based on matches
- Contradicted claims flagged as issues
- User allowed to specify additional dossiers
- Output file updated with reference check results
- Auto-proceed to web verification

## SYSTEM FAILURE Conditions

- Not scanning research dossier directory
- Not matching claims to available dossiers
- Not reading relevant dossiers
- Not updating claim statuses
- Not flagging contradicted claims
- Not allowing user to add dossiers
- Proceeding without presenting summary

## Master Rule

Leveraging existing research dossiers is efficient and builds project knowledge. Every relevant dossier should be checked, every claim matched where possible. Only proceed to web verification after exhausting existing knowledge. Contradictions must be flagged immediately as they represent confirmed issues.
