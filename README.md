# Changelog Releases Assistant

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A Claude Code plugin that wires a repo's `CHANGELOG.md` up to its GitHub
Releases. Push a version tag, get a Release — body pulled straight from the
matching changelog section. No manual release-notes writing.

## What it does

- Adds `.github/workflows/release.yml`: publishes a GitHub Release on every
  `v*.*.*` tag push, using the matching `## [X.Y.Z]` section of
  `CHANGELOG.md` as the body. Supports `workflow_dispatch` (with a `tag`
  input) to backfill Releases for tags that already exist.
- Adds `scripts/extract_changelog.py`: pulls a single version's section out
  of a Keep a Changelog-formatted `CHANGELOG.md`.
- Checks for existing release automation and changelog conventions before
  touching anything — see [`skills/changelog-releases-assistant/SKILL.md`](skills/changelog-releases-assistant/SKILL.md)
  for the full decision process.

This repo dogfoods itself: `.github/workflows/release.yml` and
`scripts/extract_changelog.py` here are the exact files the skill copies
into target repos.

## Requirements

- A `CHANGELOG.md` following [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
  (`## [X.Y.Z] — YYYY-MM-DD` section headers).
- Git tags in `v*.*.*` form (e.g. `v0.7.3`). A different scheme works too,
  but the workflow's tag glob and the script's version parsing need a
  matching tweak — the skill checks for this.

## Install

```
/plugin marketplace add luxsolari/lux-solari-plugins
/plugin install changelog-releases-assistant@lux-solari-plugins
```

Then, in any repo with a changelog and tags:

```
Set up GitHub release automation from our changelog.
```

## License

MIT — see [LICENSE](LICENSE).
