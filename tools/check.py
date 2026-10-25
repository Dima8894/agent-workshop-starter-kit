"""Bounded repository checks, not a comprehensive security audit."""
from pathlib import Path
import json
import re
import subprocess
import sys
from urllib.parse import unquote

from build import ROOT, chat_prompt, release_paths


def validate(root=ROOT):
    errors = []
    try:
        names = release_paths(root)
    except (ValueError, OSError) as exc:
        return [str(exc)]
    if (root / 'CHATGPT-START.txt').read_text() != chat_prompt(root):
        errors.append('CHATGPT-START.txt is stale; run tools/build.py')
    # This allowlist describes every public source file, including developer tools.
    public = json.loads((root / 'tools/public-files.json').read_text())
    if len(public) != len(set(public)):
        errors.append('Duplicate public manifest entries')
    for name in public:
        path = root / name
        if not path.is_file() or path.is_symlink():
            errors.append('Missing or symlinked public file: ' + name)
            continue
        text = path.read_text()
        if re.search('[\u0400-\u04ff]', text):
            errors.append('Non-English Cyrillic content: ' + name)
        # Split literals keep this checker from matching its own test patterns.
        for marker in ['/' + 'Users/', 'gh' + 'p_', 'sk' + '-proj-',
                       '-----BEGIN ' + 'PRIVATE KEY-----']:
            if marker in text:
                errors.append('Potential private material: ' + name)
        if path.suffix == '.md' or name == 'llms.txt':
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if target.startswith(('https://', 'http://', '#', 'mailto:')):
                    continue
                clean = unquote(target.split('#')[0])
                if clean and not (path.parent / clean).exists():
                    errors.append('Broken relative link in ' + name + ': ' + target)
    if not set(names).issubset(public):
        errors.append('Release contains files outside public manifest')
    if (root / '.git').exists():
        tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0')
        for name in filter(None, tracked):
            if name not in public:
                errors.append('Tracked file outside public manifest: ' + name)
    return errors


if __name__ == '__main__':
    problems = validate()
    for problem in problems:
        print('FAIL:', problem)
    print('PASS: public files, English content, links, chat prompt, and release boundary'
          if not problems else f'{len(problems)} check(s) failed')
    sys.exit(bool(problems))
