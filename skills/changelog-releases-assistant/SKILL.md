---
name: changelog-releases-assistant
description: >-
  Set up GitHub Release automation driven by a repo's CHANGELOG.md. Use when
  the user wants to populate an empty GitHub Releases tab, backfill releases
  for existing tags, or automate publishing a Release every time a version
  tag is pushed — using the matching changelog section as the release body.
  Applies to any repo that follows Keep a Changelog conventions and tags
  releases with a "v*.*.*"-style scheme.
license: MIT
---

# Changelog Releases Assistant

Wires a repo's `CHANGELOG.md` up to its GitHub Releases: pushing a version tag
publishes a Release whose body is that version's changelog section, verbatim
— no manual release-notes writing, ever again.

## When to use this skill

- "Populate the GitHub Releases tab for this repo."
- "Set up automatic releases from the changelog."
- "Backfill GitHub releases for our existing tags."
- Any repo with a `CHANGELOG.md` and git tags, but an empty Releases page.

## Before touching anything

1. **Check for an existing release workflow.** Look for any
   `.github/workflows/*.yml` that already creates/publishes GitHub Releases
   (grep for `gh release`, `softprops/action-gh-release`,
   `actions/create-release`, or similar). If one exists, stop and tell the
   user what's already there instead of adding a second, competing workflow.
2. **Check `CHANGELOG.md` follows Keep a Changelog conventions**: version
   sections headed `## [X.Y.Z] — YYYY-MM-DD` (or close enough — a regex on
   `^## \[VERSION\]` must match). If the repo has no changelog, or its format
   doesn't match, tell the user this skill needs one and ask whether to
   proceed anyway (e.g. by first drafting a changelog) rather than guessing.
3. **Check the tag scheme**: `git tag -l` should show tags like `v0.1.0`.
   If tags use a different prefix or omit `v`, the bundled workflow's
   `on.push.tags` glob and `scripts/extract_changelog.py`'s `version.lstrip('v')`
   both assume `v`-prefixed semver tags — adjust both to match the repo's
   actual scheme rather than silently leaving them broken.

## What to install

Copy two files from this plugin, unmodified unless step 3 above required a
tag-scheme tweak:

| Source (`$CLAUDE_PLUGIN_ROOT/...`) | Destination in target repo |
| --- | --- |
| `scripts/extract_changelog.py` | `scripts/extract_changelog.py` |
| `.github/workflows/release.yml` | `.github/workflows/release.yml` |

If the target repo's `scripts/` directory already has a same-named file,
don't overwrite it blindly — check what it does first.

`extract_changelog.py` takes a version (e.g. `v0.7.3` or `0.7.3`) and prints
the matching `## [X.Y.Z]` section of `CHANGELOG.md`, stripping the trailing
`[X.Y.Z]: https://...` reference link and any `---` separator. The workflow
runs on every `v*.*.*` tag push (and via `workflow_dispatch` with a `tag`
input for backfilling), pipes that script's output into `gh release create`
(or `gh release edit` if a release for that tag already exists), and needs no
secrets beyond the default `GITHUB_TOKEN` (`permissions: contents: write`).

## Land the change

1. Create a branch, commit both files together
   (`ci: add GitHub Release automation from CHANGELOG entries` — or match
   the repo's own commit convention if its CLAUDE.md specifies one), push,
   and open a PR. Don't push straight to the default branch of an existing,
   non-empty repo.
2. In the PR description, note how many existing tags have no Release yet
   and that they can be backfilled post-merge via `workflow_dispatch` (ref
   = default branch, input `tag=v0.x.y`), one dispatch per tag.
3. After merge, offer to run that backfill for the user (via the GitHub
   Actions "run workflow" API/UI) rather than leaving old tags un-released.

## Scope notes

- This skill only wires up **Release publishing from existing tags and
  changelog entries** — it does not create tags, bump versions, or write
  changelog content. If the target repo has no version-bump automation and
  no tags yet, that's a separate, prior step.
- Every file this skill installs is generic: no repo name, owner, or path is
  hardcoded, so the same two files work unmodified across repos (beyond the
  tag-scheme check above).
