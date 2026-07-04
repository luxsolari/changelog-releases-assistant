# Changelog

All notable changes to this project will be documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] — 2026-07-04

### Added
- Initial release of the **Changelog Releases Assistant** skill: `skills/changelog-releases-assistant/SKILL.md` scaffolds a target repo's GitHub Release automation from its `CHANGELOG.md`.
- `.github/workflows/release.yml`: publishes a GitHub Release whenever a `v*.*.*` tag is pushed, using the matching `CHANGELOG.md` section (`## [X.Y.Z]`) as the release body. Also accepts `workflow_dispatch` with a `tag` input to backfill releases for existing tags.
- `scripts/extract_changelog.py`: extracts a single version's section from a Keep a Changelog-formatted `CHANGELOG.md`, stripping the trailing reference-link line and `---` separator, for use as release notes.
- This repo dogfoods its own automation: the workflow and script above are the exact files the skill copies into target repos.

[0.1.0]: https://github.com/luxsolari/changelog-releases-assistant/releases/tag/v0.1.0
