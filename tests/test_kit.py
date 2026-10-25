import csv
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from bootstrap import initialize
from build import build, release_paths
from supply_check import classify


class DeliveryTests(unittest.TestCase):
    def test_fixture_and_boundaries(self):
        with (ROOT / 'examples/supply-check/input.csv').open() as f:
            rows = list(csv.DictReader(f))
        actual = [classify(row, '2026-10-23') for row in rows]
        self.assertEqual(actual, [
            {'status': 'overdue', 'days_overdue': 2},
            {'status': 'excluded', 'days_overdue': None},
            {'status': 'missing_date', 'days_overdue': None}])
        self.assertEqual(classify(rows[0], '2026-10-23', ['2026-10-24'])['status'], 'conflict')
        for day in ['2026-10-23', '2026-10-24']:
            self.assertEqual(classify({'status': 'open', 'planned_date': day}, '2026-10-23')['status'], 'not_due')
        self.assertEqual(classify({'status': 'open', 'planned_date': 'invalid'}, '2026-10-23')['status'], 'invalid_date')
        self.assertEqual(classify({'status': 'unknown'}, '2026-10-23')['status'], 'invalid_status')


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / 'kit'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', 'dist', 'workspace', '__pycache__'))

    def tearDown(self):
        self.tmp.cleanup()

    def test_resume_preserves_user_work(self):
        self.assertEqual(len(initialize(self.root)), 8)
        task = self.root / 'workspace/projects/first-task/task.md'
        task.write_text('My existing task and decisions\n')
        self.assertEqual(initialize(self.root), [])
        self.assertEqual(task.read_text(), 'My existing task and decisions\n')

    def test_private_files_never_enter_archive(self):
        initialize(self.root)
        (self.root / 'workspace/private.txt').write_text('PRIVATE_SENTINEL')
        (self.root / '.env').write_text('PRIVATE_SENTINEL')
        archive = build(self.root)
        first = archive.read_bytes()
        with zipfile.ZipFile(archive) as z:
            self.assertEqual(set(z.namelist()), {'agent-workshop-starter-kit/' + p for p in release_paths(self.root)})
            self.assertFalse(any(b'PRIVATE_SENTINEL' in z.read(n) for n in z.namelist()))
        self.assertEqual(build(self.root).read_bytes(), first)

    def test_manifest_rejects_private_and_traversal_paths(self):
        manifest = self.root / 'tools/release-files.json'
        for bad in ['workspace/private.txt', '../outside.txt', '/absolute.txt', '.env', 'dist/output.zip']:
            manifest.write_text(json.dumps([bad]))
            with self.assertRaises(ValueError):
                release_paths(self.root)

    def test_manifest_rejects_symlink(self):
        target = self.root / 'README.md'
        target.unlink()
        target.symlink_to(self.root / 'LICENSE')
        with self.assertRaises(ValueError):
            release_paths(self.root)

    def test_bootstrap_rejects_symlink_without_writing(self):
        outside = Path(self.tmp.name) / 'outside'
        outside.mkdir()
        (self.root / 'workspace').symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            initialize(self.root)
        self.assertEqual(list(outside.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
