# Bible Edit Protocols

## Final Menu Options (Edit Mode)

After completing all dimension updates in Edit mode, present this menu to the user:

```
Update complete - What would you like to do?

[R] Review theme changes
[V] Launch coherence validation
[M] Start another update
[Q] Exit the workflow
```

### Menu Execution Rules

- ALWAYS halt and wait for user input
- This is the FINAL step of Edit mode — no automatic progression

### Menu Handling Logic

**[R] Review:** Return to theme update processing to revise changes
- Action: Return to step 3 (Process Theme Updates)
- User can make additional changes before final save

**[V] Validation:** Transition to Validate mode
- Action: Display "Switching to Validation mode..."
- Load: `../steps-v/step-v-01-load.md`
- Begin integrity checking workflow

**[M] Update:** Start new edit session
- Action: Display "New update session..."
- Load: `./step-e-01-trigger.md`
- Begin new extraction and update cycle

**[Q] Exit:** Exit workflow
- Action: Display closing message: "The Narrative Bible is up to date. See you soon, guardian of stories!"
- Terminate session

**Any other input:** Help user understand options, then redisplay menu

## Session Completion Protocol

### Update Session File

When Edit mode completes successfully, update the session file:

```yaml
status: complete
stepsCompleted:
  - trigger
  - chronology
  - locations
  - objects
  - characters
  - themes
completedAt: [current datetime ISO 8601]
```

Location: `{bbb_output_folder}/bible/.update-session.yaml`

### Final Update Summary

Generate a comprehensive summary of all changes:

```markdown
**✅ BIBLE UPDATE COMPLETE**

**Session summary:**

| Dimension | Changes |
|-----------|--------------|
| Chronology | [summary of changes] |
| Locations | [summary of changes] |
| Objects | [summary of changes] |
| Characters | [summary of changes] |
| Themes | [summary of changes] |

**Narrative bible updated successfully!**

All files have been saved in {bibleFolder}/

*The memory of your story is up to date. Nothing has been forgotten.*
```

## File Update Protocols

### Frontmatter Updates

Each dimension file should have its frontmatter updated:

```yaml
lastUpdated: [current date YYYY-MM-DD]
total[Dimension]s: [updated count]
[dimension]InCrisis: [count at phase 3, if applicable]
```

Example for themes:
```yaml
lastUpdated: 2025-01-15
totalThemes: 12
themesInCrisis: 3
```

### Save Verification

Before marking step complete:
1. Verify file write was successful
2. Confirm frontmatter updated
3. Check session file updated
4. Present summary to user
5. Only then mark complete and offer menu options

## Related References

- **Dimension-Specific Procedures:** See individual dimension reference files
- **Validation Mode:** See `validation-protocols.md`
- **Session Management:** See workflow-level session documentation
