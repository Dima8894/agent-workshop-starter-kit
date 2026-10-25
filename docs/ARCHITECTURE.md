# A workspace that grows with you

The central idea is a navigation layer around independent projects. A company root need not be a Git repository. Each project can keep its own instructions, history, and release process. This generalizes the orchestration pattern used at Alpes without including its private data.

## Start with one project

```text
agent-workshop-starter-kit/      Public learning materials
  AGENTS.md                     Assistant entry point
  onboarding/                   Interview protocol
  templates/                    Blank reusable structures
  workspace/                    Your local work; created on first use
    START.md                    Active project and next action
    PROJECTS.md                 Navigation and owner roles
    onboarding.md               Interview checkpoint
    progress.md                 Evidence-based milestones
    projects/
      first-task/
        AGENTS.md               Project boundaries
        task.md                 Outcome and working rules
        workflow.md             Repeatable steps
        checks.md               Actual verification history
        inputs/                 Source copies, kept unchanged
        results/                Generated artifacts
```

## Add coordination only when needed

Create workspace/shared/context.md from templates/shared-context.md when several projects truly share definitions. Keep project-specific or sensitive material within its project. Link to canonical sources instead of copying them into multiple folders.

For larger work, the registry may point to independent local repositories. Do not nest them in this public kit's tracked tree. Do not initialize the whole company workspace as one repository by default. Opening a project independently may not load instructions above its Git root; keep its rules self-contained or explicitly load the shared guidance.

## Routing contract

1. Identify the active project and intended artifact.
2. Read its instructions, latest checks, and only relevant sources.
3. Check source ownership, freshness, and permission.
4. For cross-project work, list affected projects and the specific shared information authorized.
5. Make drafts inside the owning project; do not silently change sibling projects.
6. Verify each result where it belongs. Commit and release independent repositories separately.
7. Record common decisions in shared context and product decisions in the owning project.

No subagent fleet is needed for the learning path. “Orchestration” here means deliberate context routing and coordinated work. Real parallel agents are optional and require clear scope and tool support.

## Failure handling

If the registry points to a missing folder, report it and ask for the correct location. If sources disagree, preserve both with dates and request the responsible person's decision. If authorization is unclear, produce a fictional draft. If a task fails, record the failed check and next action rather than marking the project complete.

The files store explicit project state. They do not provide automatic memory, synchronization, access control, or backups. Gitignore reduces accidental tracking; it cannot prevent uploads or forced commits.
