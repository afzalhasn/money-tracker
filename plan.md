# Development Plan & Command List

This document helps the team coordinate by describing the sequential workflow and the textual commands you can say to trigger work.

## Workflow

1. Review `docs/system_roadmap.md` for the current project phases and task definitions.
2. When ready for execution, issue a command in the form `executor: <instruction>`. The executor will:
   - Pick the next uncompleted task from the roadmap unless you specify one explicitly.
   - Read the necessary code, propose adjustments, apply changes, and describe how to test.
   - Confirm completion before awaiting the next command.
3. For targeted refactors, use `refactor: <objective>`. The refactorer will focus exclusively on the requested files (e.g., `refactor: refactor code @page.tsx`) while keeping the rest of the system stable.
4. When documentation or coordination is needed, use `docs:` or `brainstorm:` prefixes, and the relevant agent will respond with updated text/ideas.

## Command Examples

* `executor: pick the next uncompleted task and implement it`
  - The executor follows the roadmap, works on the next pending task, and reports once done.
* `executor: implement backend item create endpoint`
  - The executor works on that specific story even if it isn't the next chronological task.
* `refactor: refactor code @page.tsx`
  - The refactorer updates the `page.tsx` file as requested, ensuring functionality remains intact.
* `docs: expand AGENTS.md with roles`
  - The documentation agent updates the requested files.

## Task Granularity

Tasks must remain small enough to complete in a self-contained pass. If you give a composite request, the executor should either break it down or ask for clarification first.

## Communication

Always describe:

* What was changed.
* Why it was necessary.
* How to verify (tests to run or manual steps).

Use references like `frontend/app/login/page.tsx` with line context when appropriate.
