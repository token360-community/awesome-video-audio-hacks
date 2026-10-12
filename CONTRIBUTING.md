# Contributing

**EN** · [简体中文](./CONTRIBUTING.zh-CN.md) · [日本語](./CONTRIBUTING.ja.md)

There is no limit on entries per section: if a resource meets the bar below, it gets added. Entries that go stale or fall below the bar are removed. The bar is the filter, so please check every rule for your entry's type before opening a PR.

## How to add an entry

1. Edit **`data/catalog.json` only**. The three READMEs are generated; hand edits fail CI.
2. Fill every required field, including `blurb.en`, `blurb.zh-CN` and `blurb.ja` (one sentence each; the English one ends with a period). Machine-drafted translations are fine; set `blurb_status` to `machine-draft`.
3. Copy numbers from the source (GitHub API, the post itself). Never estimate stars, likes or followers. Set `last_checked` to the day you checked.
4. Run `python3 scripts/generate_readme.py` and commit the regenerated READMEs.
5. Open a PR using the template.

## Inclusion bar

Every rule must hold. `scripts/generate_readme.py` enforces the numeric ones; reviewers check the rest.

**General**

- In scope: AI video, voice/TTS, music, dubbing/subtitles, lip-sync/digital humans, editing and motion. Image-only resources are out of scope.
- No competitor platforms or their promotional posts (hosted model resellers and aggregators).
- No projects that break a third party's terms of service or rely on reverse-engineered private APIs.
- One resource, one entry. If a post only links to a repo that qualifies, list the repo.
- Non-commercial, source-available or unlicensed repos may appear **link-only (⛔)**, only with ≥ 5,000★ and only if they are the reference project in their category.
- `last_checked` must be within the last **30 days**. Entries that are not re-checked fail CI until refreshed or removed.
- ⚡ ("runs on Token360") only with a published, tested guide (`token360.guide`). Never on assumption.
- 🔷 **Token360 editions.** A fork kept in [token360-community](https://github.com/token360-community) may be listed when the upstream project meets the bar for its type (stars and activity are checked on `edition.upstream`), the license and copyright are unchanged, the fork's README credits the original author at the top, and it ships a tested Token360 quick start (so it carries ⚡). It sits next to the original, which stays listed if it qualifies on its own. An edition may cover stills for ad and listing workflows (for example product motion GIFs); third-party image-only resources remain out of scope.

| Type | Hard requirements |
|---|---|
| `Repo` (app / tool) | ≥ 1,000★; last commit on the default branch ≤ 90 days before `last_checked` (≤ 180 days for model-weights research repos, `model_weights: true`); not archived; README has a working quickstart or demo; OSI license (otherwise ⛔ rules above). |
| `Skill` (SKILL.md, Claude Code / Codex skill) | Hosted on GitHub; ≥ 200★; updated ≤ 90 days; explicit license; produces finished video/audio or prompts for video/audio models. |
| `MCP` server | Works with the current MCP spec with documented install steps; ≥ 100★ or vendor-official; last commit ≤ 120 days; not archived. |
| `Node` (ComfyUI) | ≥ 300★; last commit ≤ 120 days; ships an importable example workflow. |
| `Plugin` / `Web` | Free tier; no invite code; not a competitor platform; a maintainer has opened and tried it. |
| `Post` (X post / article) | Reproducible: full prompts or steps, a long-form article, or a link to an open-source repo. No "comment/retweet to get it" gates. ≥ 500 likes or ≥ 1,000 bookmarks; ≤ 120 days old when added; not a brand account or ad. |
| `Person` | ≥ 5,000 followers; at least one of their own reproducible video/audio posts with ≥ 300 likes in the last 120 days; feed is mainly video/audio. |
| `List` (related awesome list) | ≥ 1,000★; updated ≤ 90 days; video/audio focused or directly useful for it. |

## Rotation

- Posts are reviewed every quarter; posts older than 180 days or superseded move out.
- Tool entries that fall outside the activity window are flagged; if they do not recover within 30 days they are removed.

## Keeping numbers fresh

`python3 scripts/refresh_github_stats.py` re-reads stars, last commit, license and archived state for every GitHub entry (read-only, needs `gh` or `GITHUB_TOKEN`) and updates `last_checked`. Review the diff: an entry that now fails the bar must be fixed or removed, not waved through.
