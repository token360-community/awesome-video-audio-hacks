#!/usr/bin/env python3
"""Re-read GitHub numbers for every GitHub-hosted entry in data/catalog.json (read-only API calls).

Updates stars, last_commit (default branch, America/Los_Angeles date), archived, and last_checked.
License is reported but NOT overwritten: a change must be reviewed by a human (GitHub reports
NOASSERTION for some valid licenses). Posts and people are not touched (check them on X by hand).
For Token360 editions (`edition.upstream`), the upstream repo's stars and last commit are refreshed too.

Auth: GITHUB_TOKEN / GH_TOKEN env var, or falls back to `gh api` if the gh CLI is logged in.
Run `python3 scripts/generate_readme.py` afterwards; it fails if an entry dropped below the bar.
"""
import datetime as dt
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "data" / "catalog.json"
GITHUB_TYPES = {"repo", "skill", "mcp", "node", "list"}
LA = dt.timezone(dt.timedelta(hours=-7))  # PDT; good enough for a date stamp


def gh(path: str):
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        req = urllib.request.Request(f"https://api.github.com/{path}", headers={
            "Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json", "User-Agent": "avah-refresh"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    out = subprocess.run(["gh", "api", path], capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def main() -> int:
    cat = json.loads(CATALOG.read_text(encoding="utf-8"))
    today = dt.datetime.now(LA).date().isoformat()
    for sec in cat["sections"]:
        for it in sec["items"]:
            if it["type"] not in GITHUB_TYPES:
                continue
            full = it["url"].split("github.com/", 1)[1].strip("/")
            r = gh(f"repos/{full}")
            c = gh(f"repos/{r['full_name']}/commits?per_page=1&sha={r['default_branch']}")
            last = dt.datetime.fromisoformat(c[0]["commit"]["committer"]["date"].replace("Z", "+00:00")).astimezone(LA).date().isoformat()
            lic = (r.get("license") or {}).get("spdx_id")
            changes = []
            if r["html_url"] != it["url"]:
                changes.append(f"url {it['url']} -> {r['html_url']} (renamed/moved; update by hand)")
            if lic != it["license"] and not it.get("license_note"):
                changes.append(f"license {it['license']} -> {lic} (review by hand)")
            for k, v in (("stars", r["stargazers_count"]), ("last_commit", last), ("archived", r["archived"])):
                if it.get(k) != v:
                    changes.append(f"{k} {it.get(k)} -> {v}")
                    it[k] = v
            up = (it.get("edition") or {}).get("upstream")
            if up:  # Token360 edition: the bar is checked on the upstream repo, so refresh it too
                ufull = up["url"].split("github.com/", 1)[1].strip("/")
                ur = gh(f"repos/{ufull}")
                uc = gh(f"repos/{ur['full_name']}/commits?per_page=1&sha={ur['default_branch']}")
                ulast = dt.datetime.fromisoformat(uc[0]["commit"]["committer"]["date"].replace("Z", "+00:00")).astimezone(LA).date().isoformat()
                for k, v in (("stars", ur["stargazers_count"]), ("last_commit", ulast)):
                    if up.get(k) != v:
                        changes.append(f"upstream {k} {up.get(k)} -> {v}")
                        up[k] = v
            it["last_checked"] = today
            print(f"{full}: " + ("; ".join(changes) if changes else "no change"))
    cat["updated"] = today
    CATALOG.write_text(json.dumps(cat, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
