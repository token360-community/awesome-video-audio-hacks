#!/usr/bin/env python3
"""Generate README.md / README.zh-CN.md / README.ja.md from data/catalog.json.

Usage:
  python3 scripts/generate_readme.py            # validate, then write the three READMEs
  python3 scripts/generate_readme.py --check    # validate, and fail if any README is out of date (CI)
  python3 scripts/generate_readme.py --check --today 2026-10-11   # pin "today" (tests)
  python3 scripts/generate_readme.py --check --live-models        # also compare quickstart model ids with live GET /v1/models

Standard library only. Exit code 1 on any validation error or stale README.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "data" / "catalog.json"
LANGS = ["en", "zh-CN", "ja"]
OUTFILE = {"en": "README.md", "zh-CN": "README.zh-CN.md", "ja": "README.ja.md"}
LANG_LABEL = {"en": "EN", "zh-CN": "简体中文", "ja": "日本語"}

TYPE_TAG = {"repo": "Repo", "skill": "Skill", "mcp": "MCP", "node": "Node", "plugin": "Plugin",
            "web": "Web", "post": "Post", "person": "Person", "list": "List", "tutorial": "Tutorial"}
GITHUB_TYPES = {"repo", "skill", "mcp", "node", "list"}

# Inclusion bar, mirrored in CONTRIBUTING.md. Activity is measured from last_commit to last_checked.
BAR = {
    "repo":  {"min_stars": 1000, "max_inactive_days": 90, "max_inactive_days_model": 180},
    "skill": {"min_stars": 200,  "max_inactive_days": 90},
    "mcp":   {"min_stars": 100,  "max_inactive_days": 120},
    "node":  {"min_stars": 300,  "max_inactive_days": 120},
    "list":  {"min_stars": 1000, "max_inactive_days": 90},
    "post":  {"min_likes": 500, "min_bookmarks": 1000, "max_age_days_at_add": 120},
    "person": {"min_followers": 5000, "min_proof_likes": 300, "max_proof_age_days_at_add": 120},
}
LINK_ONLY_MIN_STARS = 5000
REQUIRED = {
    "_all": ["id", "type", "title", "url", "last_checked", "added_at", "source", "blurb"],
    "_github": ["license", "license_class", "link_only", "stars", "last_commit", "archived", "token360"],
    "post": ["author", "posted_at", "likes", "bookmarks", "metrics_at", "use_case"],
    "person": ["handle", "followers", "lang", "focus", "proof"],
}

CHROME = {
    "en": {
        "generated": "GENERATED from data/catalog.json by scripts/generate_readme.py. Do not edit by hand.",
        "banner_alt": "Awesome Video & Audio Hacks, by Token360",
        "tagline": "A strictly curated list of open-source workflows, agent skills, MCP servers and reproducible posts for AI **video, voice, dubbing, lip-sync and editing**. Every entry is re-checked against a written bar (see [Contributing](#contributing)), and each section is capped at {cap} entries. Maintained by the [Token360]({site}) developer community.",
        "legend": "**Tags:** {tags} · ⛔ link-only (non-commercial or source-available license) · ⚠️ read the note before using commercially",
        "legend_ready": "A ⚡ mark will mean \"verified to run on Token360 by changing `base_url` and key\". No entry carries it yet: nothing has been tested.",
        "qs_title": "Token360 quickstart",
        "qs_intro": "Token360 serves text, image and video models behind one OpenAI-compatible `base_url`.",
        "qs_table": ["Modality", "Endpoint", "Example model ids"],
        "modality": {"text": "Text", "image": "Image", "video": "Video", "audio": "Audio"},
        "pending": "pending verification",
        "qs_models_link": "Full model list and per-model request examples: [token360.ai/models]({models_url}).",
        "toc": "Contents",
        "contributing": "Contributing",
        "contrib_body": "Edit `data/catalog.json` only (never the READMEs), run `python3 scripts/generate_readme.py`, and open a pull request. Read the inclusion bar in [CONTRIBUTING.md](./CONTRIBUTING.md) first; entries that miss it are closed without merge.",
        "license_line": "List content is released under [CC0 1.0](./LICENSE). Linked projects, posts and trademarks belong to their owners; inclusion is not an endorsement by them or of Token360.",
        "ja_note": None,
        "stars": "⭐ {n}",
        "via": "Example",
        "via_post": "post",
        "use_case": {"video-gen": "Video generation", "editing": "Editing & motion", "voice": "Voice & TTS",
                     "dubbing": "Dubbing", "short-drama": "Short drama", "lipsync": "Lip-sync"},
        "badge_entries": "entries", "badge_verified": "last verified",
        "count_line": "{n} entries across {s} sections · last verified {date}",
    },
    "zh-CN": {
        "generated": "由 scripts/generate_readme.py 从 data/catalog.json 生成，请勿手改。",
        "banner_alt": "Awesome Video & Audio Hacks，Token360 出品",
        "tagline": "一份严格筛选、逐条核验的 AI **视频、配音、翻译配音、对口型、剪辑**清单，收录开源工作流、Agent Skill、MCP server，以及可以照着复现的帖子。每一条都要过书面门槛（见[参与贡献](#参与贡献)），每个分类最多 {cap} 条。由 [Token360]({site}) 开发者社区维护。",
        "legend": "**标签：** {tags} · ⛔ 仅链接（非商用或 source-available 许可） · ⚠️ 商用前请先看备注",
        "legend_ready": "⚡ 表示“只改 `base_url` 和 key 就能在 Token360 上跑通，并已验证”。目前还没有任何条目带 ⚡：都还没测过。",
        "qs_title": "Token360 快速上手",
        "qs_intro": "Token360 用一个 OpenAI 兼容的 `base_url` 提供文本、图像和视频模型。",
        "qs_table": ["模态", "接口", "模型 id 示例"],
        "modality": {"text": "文本", "image": "图像", "video": "视频", "audio": "音频"},
        "pending": "待验证",
        "qs_models_link": "完整模型列表和每个模型的请求示例：[token360.ai/models]({models_url})。",
        "toc": "目录",
        "contributing": "参与贡献",
        "contrib_body": "只改 `data/catalog.json`（不要直接改 README），运行 `python3 scripts/generate_readme.py`，再提 PR。提交前请先读 [CONTRIBUTING.zh-CN.md](./CONTRIBUTING.zh-CN.md) 里的门槛，不达标的条目会直接关闭。",
        "license_line": "列表内容以 [CC0 1.0](./LICENSE) 发布。所链接的项目、帖子和商标归各自所有者；收录不代表对方背书，也不代表 Token360 背书。",
        "ja_note": None,
        "stars": "⭐ {n}",
        "via": "代表作",
        "via_post": "帖子",
        "use_case": {"video-gen": "视频生成", "editing": "剪辑与动效", "voice": "配音与 TTS",
                     "dubbing": "翻译配音", "short-drama": "短剧", "lipsync": "对口型"},
        "badge_entries": "条目", "badge_verified": "最近核验",
        "count_line": "共 {n} 条，{s} 个分类 · 最近核验 {date}",
    },
    "ja": {
        "generated": "data/catalog.json から scripts/generate_readme.py で生成。手で編集しないこと。",
        "banner_alt": "Awesome Video & Audio Hacks（Token360）",
        "tagline": "AI の**動画・音声合成・吹き替え・リップシンク・編集**向けに、オープンソースのワークフロー、エージェントスキル、MCP サーバー、再現できる投稿を厳選したリストです。すべての項目は書面の基準（[コントリビュート](#コントリビュート)）で再確認しており、各カテゴリは最大 {cap} 件です。メンテナンスは [Token360]({site}) 開発者コミュニティ。",
        "legend": "**タグ：** {tags} · ⛔ リンクのみ（非商用または source-available ライセンス） · ⚠️ 商用利用の前に注記を確認",
        "legend_ready": "⚡ は「`base_url` とキーを変えるだけで Token360 で動くことを確認済み」を表します。現時点では未検証のため、⚡ の付いた項目はありません。",
        "qs_title": "Token360 クイックスタート",
        "qs_intro": "Token360 は OpenAI 互換の `base_url` ひとつで、テキスト・画像・動画モデルを提供しています。",
        "qs_table": ["モダリティ", "エンドポイント", "モデル ID の例"],
        "modality": {"text": "テキスト", "image": "画像", "video": "動画", "audio": "音声"},
        "pending": "検証待ち",
        "qs_models_link": "全モデルの一覧とモデルごとのリクエスト例：[token360.ai/models]({models_url})。",
        "toc": "目次",
        "contributing": "コントリビュート",
        "contrib_body": "`data/catalog.json` だけを編集し（README は直接編集しない）、`python3 scripts/generate_readme.py` を実行してから PR を出してください。先に [CONTRIBUTING.ja.md](./CONTRIBUTING.ja.md) の基準を読んでください。基準に満たない項目はマージせずにクローズします。",
        "license_line": "リストの内容は [CC0 1.0](./LICENSE) で公開しています。リンク先のプロジェクト・投稿・商標は各権利者に帰属し、掲載は権利者や Token360 による推奨を意味しません。",
        "ja_note": "この日本語版は機械翻訳による下書きで、ネイティブスピーカーのレビュー前です。誤りに気づいたら Issue でお知らせください。",
        "stars": "⭐ {n}",
        "via": "例",
        "via_post": "投稿",
        "use_case": {"video-gen": "動画生成", "editing": "編集・モーション", "voice": "音声・TTS",
                     "dubbing": "吹き替え", "short-drama": "ショートドラマ", "lipsync": "リップシンク"},
        "badge_entries": "entries", "badge_verified": "last verified",
        "count_line": "{s} カテゴリ・全 {n} 件 · 最終確認 {date}",
    },
}


class ValidationError(Exception):
    pass


def days(a: str, b: str) -> int:
    return (dt.date.fromisoformat(b) - dt.date.fromisoformat(a)).days


def norm_url(u: str) -> str:
    u = u.strip().lower().rstrip("/")
    u = re.sub(r"^https?://(www\.)?", "", u)
    return u.replace("twitter.com/", "x.com/")


def validate(cat: dict, today: str, models_snapshot: set[str] | None) -> list[str]:
    errs: list[str] = []
    max_age = cat.get("max_age_days", 30)
    max_lo = cat.get("max_link_only_per_section", 2)
    seen_urls: dict[str, str] = {}
    seen_ids: set[str] = set()
    for key in ("name", "repo", "langs", "sections", "token360"):
        if key not in cat:
            errs.append(f"catalog: missing top-level '{key}'")
    if cat.get("langs") != LANGS:
        errs.append(f"catalog: langs must be {LANGS}")
    for sec in cat.get("sections", []):
        sid = sec.get("id", "?")
        for lang in LANGS:
            if not (sec.get("title") or {}).get(lang):
                errs.append(f"[{sid}] section title missing '{lang}'")
        items = sec.get("items", [])
        cap = sec.get("cap")
        if not isinstance(cap, int):
            errs.append(f"[{sid}] section has no integer cap")
        elif len(items) > cap:
            errs.append(f"[{sid}] {len(items)} entries exceeds cap {cap}")
        if sum(1 for i in items if i.get("link_only")) > max_lo:
            errs.append(f"[{sid}] more than {max_lo} link-only entries")
        for it in items:
            iid = it.get("id", "?")
            where = f"[{sid}/{iid}]"
            typ = it.get("type")
            if typ not in TYPE_TAG:
                errs.append(f"{where} unknown type '{typ}'")
                continue
            req = REQUIRED["_all"] + (REQUIRED["_github"] if typ in GITHUB_TYPES else []) + REQUIRED.get(typ, [])
            for f in req:
                if it.get(f) in (None, "") and not (f == "link_only" and it.get(f) is False) and not (f == "archived" and it.get(f) is False):
                    errs.append(f"{where} missing required field '{f}'")
            for lang in LANGS:
                b = (it.get("blurb") or {}).get(lang, "")
                if not b.strip():
                    errs.append(f"{where} blurb missing '{lang}'")
                elif lang == "en" and not b.rstrip().endswith((".", "!", "?")):
                    errs.append(f"{where} en blurb must end with a period")
                if "caveat" in it and not it["caveat"].get(lang):
                    errs.append(f"{where} caveat missing '{lang}'")
            if iid in seen_ids:
                errs.append(f"{where} duplicate id")
            seen_ids.add(iid)
            nu = norm_url(it.get("url", ""))
            if nu in seen_urls:
                errs.append(f"{where} duplicate url (also in {seen_urls[nu]})")
            seen_urls[nu] = where
            if not str(it.get("url", "")).startswith("https://"):
                errs.append(f"{where} url must be https")
            lc = it.get("last_checked")
            if lc:
                age = days(lc, today)
                if age > max_age:
                    errs.append(f"{where} last_checked {lc} is {age} days old (max {max_age}); re-verify the entry")
                if age < 0:
                    errs.append(f"{where} last_checked {lc} is in the future")
            if (it.get("token360") or {}).get("ready") and not it["token360"].get("guide"):
                errs.append(f"{where} token360.ready=true requires a guide link (no unverified ⚡)")
            bar = BAR[typ] if typ in BAR else None
            if typ in GITHUB_TYPES and lc and it.get("last_commit"):
                if it.get("archived"):
                    errs.append(f"{where} repository is archived")
                need = bar["min_stars"]
                if it.get("stars", 0) < need and not it.get("bar_exception"):
                    errs.append(f"{where} {it.get('stars')} stars < {need}")
                lim = bar.get("max_inactive_days_model") if it.get("model_weights") and "max_inactive_days_model" in bar else bar["max_inactive_days"]
                idle = days(it["last_commit"], lc)
                if idle > lim:
                    errs.append(f"{where} last commit {it['last_commit']} is {idle} days before last_checked (max {lim})")
                lic_class = it.get("license_class")
                if lic_class not in ("osi", "non-commercial", "source-available", "none"):
                    errs.append(f"{where} bad license_class '{lic_class}'")
                if lic_class != "osi":
                    if not it.get("link_only"):
                        errs.append(f"{where} non-OSI license must be link_only")
                    if it.get("stars", 0) < LINK_ONLY_MIN_STARS:
                        errs.append(f"{where} link-only entries need >= {LINK_ONLY_MIN_STARS} stars")
                elif it.get("link_only"):
                    errs.append(f"{where} link_only set on an OSI-licensed entry")
            if typ == "post":
                if it.get("likes", 0) < bar["min_likes"] and it.get("bookmarks", 0) < bar["min_bookmarks"]:
                    errs.append(f"{where} post below engagement bar")
                if it.get("posted_at") and it.get("added_at") and days(it["posted_at"], it["added_at"]) > bar["max_age_days_at_add"]:
                    errs.append(f"{where} post older than {bar['max_age_days_at_add']} days when added")
                if not (it.get("title_i18n") or {}).get("zh-CN") or not (it.get("title_i18n") or {}).get("ja"):
                    errs.append(f"{where} post title_i18n needs zh-CN and ja")
            if typ == "person":
                if it.get("followers", 0) < bar["min_followers"]:
                    errs.append(f"{where} followers below {bar['min_followers']}")
                pr = it.get("proof") or {}
                if pr.get("likes", 0) < bar["min_proof_likes"]:
                    errs.append(f"{where} proof post below {bar['min_proof_likes']} likes")
                if pr.get("posted_at") and days(pr["posted_at"], it["added_at"]) > bar["max_proof_age_days_at_add"]:
                    errs.append(f"{where} proof post too old when added")
                for lang in LANGS:
                    if not (it.get("focus") or {}).get(lang):
                        errs.append(f"{where} focus missing '{lang}'")
    t = cat.get("token360", {})
    for ep in t.get("endpoints", []):
        for m in ep.get("models", []):
            if models_snapshot is not None and m not in models_snapshot:
                errs.append(f"[token360] model id '{m}' not in the /v1/models list")
    for k in ("chat_example_model", "video_example_model"):
        if models_snapshot is not None and t.get(k) and t[k] not in models_snapshot:
            errs.append(f"[token360] {k} '{t[k]}' not in the /v1/models list")
    for lang in LANGS:
        if not (t.get("verified_note") or {}).get(lang):
            errs.append(f"[token360] verified_note missing '{lang}'")
    return errs


def fmt_stars(n: int) -> str:
    if n >= 1000:
        s = f"{n / 1000:.1f}k"
        return s.replace(".0k", "k")
    return str(n)


def slug(text: str) -> str:
    """GitHub-style heading anchor."""
    s = text.strip().lower()
    s = "".join(c for c in s if c.isalnum() or c in " -_")
    return s.replace(" ", "-")


def site(cat: dict, path: str = "") -> str:
    return f"https://www.token360.ai{path}?{cat['utm']}"


def entry_line(it: dict, lang: str, cat: dict) -> str:
    """One line per entry, awesome-lint style: `- [name](url) - meta · description.`"""
    C = CHROME[lang]
    tag = f"`{TYPE_TAG[it['type']]}`"
    blurb = it["blurb"][lang].strip()
    if it["type"] == "post":
        title = it["title"] if lang == "en" else it["title_i18n"][lang]
        uc = C["use_case"].get(it["use_case"], it["use_case"])
        head = f"- [@{it['author']} — {title}]({it['url']}) - "
        meta = [tag, it["posted_at"][:7], uc]
    elif it["type"] == "person":
        head = f"- [{it['title']}]({it['url']}) - "
        meta = [tag, it["lang"], it["focus"][lang]]
    else:
        head = f"- [{it['title']}]({it['url']}) - "
        marks = (" ⛔" if it.get("link_only") else "") + (" ⚡" if (it.get("token360") or {}).get("ready") else "")
        meta = [tag + marks, C["stars"].format(n=fmt_stars(it["stars"])), it["license"]]
    line = head + " · ".join(meta) + " · " + blurb
    if it["type"] == "person":
        sep = " " if lang == "en" else ""
        line += f"{sep}{C['via']}: [{C['via_post']}]({it['proof']['url']})" + ("." if lang == "en" else "。")
    if it.get("caveat"):
        line += f" ⚠️ {it['caveat'][lang]}"
    return line


def table(rows: list[list[str]]) -> list[str]:
    """Markdown table with padded, aligned pipes (remark-lint table rules). Width counts East Asian chars as 2."""
    import unicodedata
    def w(s: str) -> int:
        return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in s)
    widths = [max(w(r[i]) for r in rows) for i in range(len(rows[0]))]
    def fmt(r):
        return "| " + " | ".join(c + " " * (widths[i] - w(c)) for i, c in enumerate(r)) + " |"
    sep = "| " + " | ".join("-" * widths[i] for i in range(len(widths))) + " |"
    return [fmt(rows[0]), sep] + [fmt(r) for r in rows[1:]]


def lang_switcher(lang: str) -> str:
    parts = []
    for l in LANGS:
        parts.append(f"<strong>{LANG_LABEL[l]}</strong>" if l == lang else f'<a href="./{OUTFILE[l]}">{LANG_LABEL[l]}</a>')
    return '<p align="center">\n  ' + " · ".join(parts) + "\n</p>"


def badge(label: str, message: str, color: str) -> str:
    def esc(s: str) -> str:
        return quote(s.replace("-", "--").replace("_", "__").replace(" ", "_"), safe="_")
    return f"https://img.shields.io/badge/{esc(label)}-{esc(message)}-{color}"


def render(cat: dict, lang: str) -> str:
    C = CHROME[lang]
    secs = cat["sections"]
    n = sum(len(s["items"]) for s in secs)
    verified = min(i["last_checked"] for s in secs for i in s["items"])
    cap = max(s["cap"] for s in secs)
    t = cat["token360"]
    tags = " ".join(f"`{TYPE_TAG[k]}`" for k in sorted({i["type"] for s in secs for i in s["items"]}, key=list(TYPE_TAG).index))
    zh = lang == "zh-CN"
    site_path = "/zh-CN" if zh else ""
    models_url = site(cat, f"{site_path}/models")
    out = ['<h1 align="center">',
           f'  <img src="./assets/banner.png" alt="{C["banner_alt"]}" width="800" />',
           "  <br />",
           "  Awesome Video &amp; Audio Hacks",
           "</h1>", "", f"<!-- {C['generated']} -->", "", lang_switcher(lang), "",
           '<p align="center">',
           '  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>',
           f'  <img src="{badge(C["badge_entries"], str(n), "9633af")}" alt="{C["badge_entries"]}: {n}" />',
           f'  <img src="{badge(C["badge_verified"], verified, "informational")}" alt="{C["badge_verified"]}: {verified}" />',
           f'  <img src="{badge("license", "CC0-1.0", "lightgrey")}" alt="License: CC0-1.0" />',
           "</p>", "",
           "> " + C["tagline"].format(cap=cap, site=site(cat, site_path)), "",
           C["legend"].format(tags=tags), "",
           C["legend_ready"], "",
           f"<sub>{C['count_line'].format(n=n, s=len(secs), date=verified)}</sub>", ""]
    # Quickstart
    out += [f"## {C['qs_title']}", "", C["qs_intro"], "",
            "```python",
            "import os",
            "from openai import OpenAI",
            "",
            f'client = OpenAI(base_url="{t["base_url"]}", api_key=os.environ["TOKEN360_API_KEY"])',
            "resp = client.chat.completions.create(",
            f'    model="{t["chat_example_model"]}",',
            '    messages=[{"role": "user", "content": "Write a 3-shot storyboard for a 10-second product teaser."}],',
            ")",
            "print(resp.choices[0].message.content)",
            "```", "",
            "```bash",
            "# Video: create a task, then poll GET /videos/{id} until it completes",
            f"curl {t['base_url']}/videos \\",
            '  -H "Authorization: Bearer $TOKEN360_API_KEY" -H "Content-Type: application/json" \\',
            f"  -d '{{\"model\": \"{t['video_example_model']}\", \"prompt\": \"A paper-cut crane takes off over a misty lake\"}}'",
            "```", "",
            ]
    rows = [C["qs_table"]]
    for ep in t["endpoints"]:
        mod = C["modality"][ep["modality"]]
        endpoint = f"`{ep['method']} {ep['path']}`" if ep["status"] != "pending" else f"_{C['pending']}_"
        rows.append([mod, endpoint, ", ".join(f"`{m}`" for m in ep["models"])])
    out += table(rows)
    out += ["", "<sub>" + t["verified_note"][lang].format(date=json.loads((ROOT / t["models_snapshot"]).read_text())["fetched_at"]) + "</sub>",
            "", C["qs_models_link"].format(models_url=models_url), ""]
    # TOC
    out += [f"## {C['toc']}", ""]
    for s in secs:
        title = s["title"][lang]
        out.append(f"- [{title}](#{slug(title)}) ({len(s['items'])})")
    out.append("")
    for s in secs:
        out += [f"## {s['title'][lang]}", ""]
        out += [entry_line(it, lang, cat) for it in s["items"]]
        out.append("")
    out += [f"## {C['contributing']}", "", C["contrib_body"], "", "---", "",
            f"<sub>{C['license_line']}</sub>"]
    if C["ja_note"]:
        out += ["", f"<sub>※ {C['ja_note']}</sub>"]
    return "\n".join(out) + "\n"


def load_snapshot(cat: dict, live: bool) -> set[str]:
    if live:
        req = urllib.request.Request(cat["token360"]["base_url"] + "/models", headers={"User-Agent": "awesome-video-audio-hacks-ci"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return {m["id"] for m in json.load(r)["data"]}
    snap = json.loads((ROOT / cat["token360"]["models_snapshot"]).read_text())
    return {m["id"] for m in snap["models"]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="validate and fail if READMEs are stale; write nothing")
    ap.add_argument("--today", default=dt.date.today().isoformat())
    ap.add_argument("--live-models", action="store_true", help="check quickstart model ids against live GET /v1/models")
    a = ap.parse_args()
    cat = json.loads(CATALOG.read_text(encoding="utf-8"))
    errs = validate(cat, a.today, load_snapshot(cat, a.live_models))
    if errs:
        print(f"✗ catalog validation failed ({len(errs)}):", file=sys.stderr)
        for e in errs:
            print("  - " + e, file=sys.stderr)
        return 1
    stale = []
    for lang in LANGS:
        text = render(cat, lang)
        p = ROOT / OUTFILE[lang]
        if a.check:
            if not p.exists() or p.read_text(encoding="utf-8") != text:
                stale.append(OUTFILE[lang])
        else:
            p.write_text(text, encoding="utf-8")
    n = sum(len(s["items"]) for s in cat["sections"])
    if stale:
        print("✗ out of date (edit data/catalog.json and run scripts/generate_readme.py, never the README): " + ", ".join(stale), file=sys.stderr)
        return 1
    print(f"✓ {n} entries in {len(cat['sections'])} sections; " + ("READMEs in sync" if a.check else "wrote " + ", ".join(OUTFILE.values())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
