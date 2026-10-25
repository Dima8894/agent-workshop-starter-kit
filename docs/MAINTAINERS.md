# Maintain and release

Use a clone of the GitHub source repository for maintenance; the learner ZIP omits tools and tests. Learners do not need these commands. Maintainers need Python 3.10+ and Git; the tools use only the standard library.

```sh
python3 tools/build.py
python3 tools/check.py
python3 -m unittest discover -s tests -v
```

The build generates CHATGPT-START.txt from the canonical instructions and templates, plus dist/agent-workshop-starter-kit.zip and its SHA-256 checksum. Do not edit the generated chat prompt directly.

`tools/release-files.json` explicitly lists the learner package. `tools/public-files.json` explicitly lists all public source files. Update both deliberately when adding public material. Never use a recursive archive of the user's working folder. The builder rejects private paths, traversal paths, and symlinks.

`python3 tools/bootstrap.py` optionally creates a local workspace for testing. It creates only missing files and refuses symlinked destinations. The normal beginner route asks the assistant to do this without Python.

## Release procedure

1. Update VERSION and CHANGELOG.md; keep the source attribution and license.
2. Build, validate, and run tests. Review all new public text and the exact staged diff.
3. Inspect `git ls-files` against the public manifest and check that no personal workspace is tracked.
4. Extract the ZIP into a fresh temporary folder and verify the first-prompt and chat paths.
5. Record actual checks and remaining gaps in docs/EVALUATION.md. Do not call a scripted review a learner study.
6. Commit the reviewed files, tag the version, and publish a GitHub Release with the ZIP and SHA256SUMS.txt.
7. Download the published ZIP, verify the checksum, and check that the README download link works.

The CI workflow runs validation, unit tests, and a build. Release publication remains a deliberate maintainer action. It does not deploy a site or connect a business system.
