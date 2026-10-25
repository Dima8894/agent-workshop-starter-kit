"""Build the chat prompt and a reproducible, allowlisted learner ZIP."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CHAT_PARTS = ['AGENTS.md', 'onboarding/INTERVIEW.md', 'templates/task.md',
              'templates/workflow.md', 'templates/checks.md',
              'templates/onboarding.md', 'templates/progress.md']


def chat_prompt(root=ROOT):
    intro = ('AGENT WORKSHOP / AI STARTER KIT — CHAT MODE\n\n'
             'Use the instructions and templates below to guide me through one task. '
             'You may not have local file access. Do not claim to read or save local files '
             'without a successful tool operation. Provide named blocks for manual saving. '
             'Begin with one question from the interview. Referenced files not included '
             'below must be supplied by me if needed.\n')
    return intro + ''.join('\n\n--- ' + p + ' ---\n' + (root / p).read_text()
                           for p in CHAT_PARTS)


def release_paths(root=ROOT):
    root = root.resolve()
    names = json.loads((root / 'tools/release-files.json').read_text())
    if not isinstance(names, list) or len(names) != len(set(names)):
        raise ValueError('Release manifest must be a list of unique paths')
    for name in names:
        p = Path(name)
        if p.is_absolute() or '..' in p.parts or any(
            part in {'workspace', '.git', 'dist', 'work'} or part.startswith('.env')
            for part in p.parts
        ):
            raise ValueError('Unsafe release path: ' + name)
        target = root / p
        if any(parent.is_symlink() for parent in [target, *target.parents]
               if parent == root or root in parent.parents):
            raise ValueError('Symlinks are not allowed: ' + name)
        if not target.is_file() or not target.resolve().is_relative_to(root.resolve()):
            raise ValueError('Missing or escaping release file: ' + name)
    return names


def build(root=ROOT):
    (root / 'CHATGPT-START.txt').write_text(chat_prompt(root))
    names = release_paths(root)
    dist = root / 'dist'
    dist.mkdir(exist_ok=True)
    archive = dist / 'agent-workshop-starter-kit.zip'
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for name in sorted(names):
            info = zipfile.ZipInfo('agent-workshop-starter-kit/' + name,
                                   date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, (root / name).read_bytes())
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (dist / 'SHA256SUMS.txt').write_text(digest + '  ' + archive.name + '\n')
    return archive


if __name__ == '__main__':
    print(build())
