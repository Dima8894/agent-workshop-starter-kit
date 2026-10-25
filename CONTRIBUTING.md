# Contribute

Help a beginner complete a useful task with less confusion. Good contributions include clearer wording, fictional examples with expected outputs, accessibility improvements, and evidence from trying the learning path.

1. Open an issue describing the learner problem without private data.
2. Make a focused change in a branch or fork.
3. Keep the core path usable without programming or paid integrations.
4. Include expected outputs and missing/conflicting-data cases for new examples.
5. Run `python3 tools/check.py` and `python3 -m unittest discover -s tests -v`.
6. Rebuild with `python3 tools/build.py`; inspect the ZIP before release.

Public files must be in English. Keep personal work under workspace/ and out of commits. Never submit customer data, transcripts, credentials, or real employee records as test fixtures. If adding a release file, update tools/release-files.json deliberately.

Be respectful and specific. Critique the artifact, not the person. Harassment and publishing others' personal information are not acceptable. Maintainers may remove harmful content. Contributions are provided under the repository's MIT license.

Do not claim that a new workflow is production-ready without actual evidence. Report which assistant, inputs, and checks you used, with any limitations.
