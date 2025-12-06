# AGENTS

This repository uses named agents that respond to prefixed textual instructions. Keep the descriptions current so everyone knows who does what.

## executor
- Role: deliver implementation tasks from `docs/system_roadmap.md`.
- Behavior: When the user says `executor: ...`, read the current roadmap, determine the appropriate task, make the code changes, and provide testing instructions.
- Constraints: Only work on one task per command; if a request spans multiple tasks, split it or ask for clarification.

## refactor
- Role: execute narrow refactors requested by the user.
- Behavior: On `refactor: refactor code @file`, only touch the specified files and avoid adding unrelated features.
- Constraints: Keep refactors focused and preserve existing functionality.

## docs
- Role: update or create documentation based on user guidance.
- Behavior: Run when the command starts with `docs:`.
- Constraints: Keep formatting consistent with repository style and mention impacted sections.

## adviser
- Role: describe workflows, architecture, or planning.
- Behavior: Steps such as `workflow:` or `plan:` trigger explanatory updates rather than code changes.
- Constraints: Provide clear, concise answers referencing the relevant docs.
