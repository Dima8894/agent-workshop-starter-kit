"""Optional maintainer helper; never overwrites an existing learner file."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAPPING = {
    'templates/start.md': 'START.md',
    'templates/projects.md': 'PROJECTS.md',
    'templates/onboarding.md': 'onboarding.md',
    'templates/progress.md': 'progress.md',
    'templates/task.md': 'projects/first-task/task.md',
    'templates/workflow.md': 'projects/first-task/workflow.md',
    'templates/checks.md': 'projects/first-task/checks.md',
    'templates/project/AGENTS.md': 'projects/first-task/AGENTS.md',
}


def initialize(root=ROOT):
    root = root.resolve()
    workspace = root / 'workspace'
    # Inspect every destination before making any mutation.
    targets = [workspace / p for p in MAPPING.values()]
    targets += [workspace / 'projects/first-task/inputs',
                workspace / 'projects/first-task/results']
    for target in targets:
        if any(p.is_symlink() for p in [target, *target.parents] if p == root or root in p.parents):
            raise ValueError('Refusing a symlinked workspace path')
        if not target.resolve().is_relative_to(root.resolve()):
            raise ValueError('Destination leaves the kit')
    created = []
    for source, relative in MAPPING.items():
        target = workspace / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            with target.open('x') as f:
                f.write((root / source).read_text())
            created.append(relative)
        except FileExistsError:
            pass
    for name in ['inputs', 'results']:
        (workspace / 'projects/first-task' / name).mkdir(exist_ok=True)
    return created


if __name__ == '__main__':
    print('Created:', ', '.join(initialize()) or 'nothing; existing work preserved')
