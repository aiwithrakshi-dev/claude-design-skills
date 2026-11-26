#!/usr/bin/env python3
"""Build website-dev-skills.

What this does, in order:
  1. Reads scripts/plugins.json (the list of plugins, credits and sample prompts).
  2. Writes each plugin's .claude-plugin/plugin.json, README.md and NOTICE.md.
  3. Validates every SKILL.md (name, description length, no angle brackets).
  4. Builds the all-in-one bundle (website-dev-skills) from every plugin's skills.
  5. Writes .claude-plugin/marketplace.json, catalog.json, docs/SKILLS.md and README.md.
  6. Zips every plugin and the bundle into dist/*.plugin (ready for Customize > Plugins > Upload).

Usage:
  python3 scripts/build.py            # build everything
  python3 scripts/build.py --check    # validate only, change nothing

Needs Python 3.9+ and PyYAML (pip install pyyaml).
"""
import json
import os
import re
import shutil
import sys
import zipfile

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = json.load(open(os.path.join(ROOT, "scripts", "plugins.json"), encoding="utf-8"))
REPO = CFG["repo"]
REPO_URL = f"https://github.com/{REPO}"
MARKET = CFG["marketplace"]
BUNDLE = CFG["bundle"]
VERSION = CFG["version"]
PLUGINS_DIR = os.path.join(ROOT, "plugins")
DIST = os.path.join(ROOT, "dist")
BUILD = os.path.join(ROOT, "build")
CHECK_ONLY = "--check" in sys.argv

NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
FM_RE = re.compile(r"^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n?", re.S)


def read_skill(path):
    text = open(path, encoding="utf-8").read()
    m = FM_RE.match(text)
    if not m:
        return None, text
    return yaml.safe_load(m.group(1)) or {}, text[m.end():]


def validate_skill(plugin, folder, path):
    errors = []
    fm, _ = read_skill(path)
    if not isinstance(fm, dict):
        return [f"{plugin}/{folder}: SKILL.md has no valid YAML frontmatter"]
    name = str(fm.get("name", ""))
    desc = fm.get("description")
    if not NAME_RE.match(name):
        errors.append(f"{plugin}/{folder}: name '{name}' must be lowercase letters, digits and hyphens (max 64)")
    if name != folder:
        errors.append(f"{plugin}/{folder}: name '{name}' must match its folder name")
    if re.search(r"anthropic|claude", name):
        errors.append(f"{plugin}/{folder}: name may not contain a reserved word")
    if not desc:
        errors.append(f"{plugin}/{folder}: description is missing")
    else:
        d = str(desc)
        if len(d) > 1024:
            errors.append(f"{plugin}/{folder}: description is {len(d)} characters (max 1024)")
        if "<" in d or ">" in d:
            errors.append(f"{plugin}/{folder}: description cannot contain XML tags or angle brackets")
    return errors


def skills_of(plugin_dir):
    sdir = os.path.join(plugin_dir, "skills")
    if not os.path.isdir(sdir):
        return []
    out = []
    for folder in sorted(os.listdir(sdir)):
        p = os.path.join(sdir, folder, "SKILL.md")
        if os.path.isfile(p):
            fm, _ = read_skill(p)
            desc = re.sub(r"\s+", " ", str((fm or {}).get("description", ""))).strip()
            manual = bool((fm or {}).get("disable-model-invocation"))
            out.append({"name": folder, "description": desc, "manual": manual, "path": p})
    return out


def first_sentence(text, limit=170):
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    s = m.group(1) if m else text
    return s if len(s) <= limit else s[: limit - 1].rsplit(" ", 1)[0] + "…"


def md_escape(text):
    return text.replace("|", "\\|")


def write_plugin_meta(p, skills):
    pdir = os.path.join(PLUGINS_DIR, p["name"])
    os.makedirs(os.path.join(pdir, ".claude-plugin"), exist_ok=True)
    count = len(skills)
    kind = f"{count} skill{'s' if count != 1 else ''}" if count else "MCP connector"
    manifest = {
        "name": p["name"],
        "version": VERSION,
        "description": f"{p['title']}: {kind} by {p['author']} ({p['license'].split(' ')[0]}). {p['best_for']} Packaged by {CFG['packager']} in website-dev-skills.",
        "author": {"name": p["author"]},
        "homepage": REPO_URL,
        "repository": REPO_URL,
        "license": p["license"].split(" ")[0],
        "keywords": ["website", "frontend", "design", "ui", "ux", "animation", p["category"].lower()],
    }
    json.dump(manifest, open(os.path.join(pdir, ".claude-plugin", "plugin.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    upstream_links = " + ".join(f"[{u.strip().split(' ')[0]}](https://github.com/{u.strip().split(' ')[0]})" for u in p["upstream"].split("+") if "/" in u)
    lines = [
        f"# {p['name']}",
        "",
        f"**{p['title']}** · {kind} · part of [website-dev-skills]({REPO_URL})",
        "",
        f"- **Original author:** {p['author']}",
        f"- **Original source:** {upstream_links or p['upstream']}",
        f"- **License:** {p['license']} (see `LICENSE` in this folder)",
        f"- **Best for:** {p['best_for']}",
        "",
    ]
    lines += [
        "## Install",
        "",
        f"- **claude.ai or desktop app:** download [{p['name']}.plugin]({REPO_URL}/raw/main/dist/{p['name']}.plugin), then go to Customize > Plugins > Add > Upload plugin.",
        f"- **Claude Code (2.1.275 or later):** `/plugin install {p['name']} --marketplace {REPO}`",
        f"- **Claude Code (any version):** `claude plugin marketplace add {REPO}` then `claude plugin install {p['name']}@{MARKET}`",
        "",
    ]
    if p.get("note"):
        lines += [f"> **Before you use it:** {p['note']}", ""]
    lines += ["## Try these prompts", ""] + [f"- {s}" for s in p["samples"]] + [""]
    if skills:
        lines += ["## Skills in this plugin", "", "| Skill | What it does |", "|---|---|"]
        for s in skills:
            tag = " *(run it by name, e.g. `/" + s["name"] + "`)*" if s["manual"] else ""
            lines.append(f"| `{s['name']}` | {md_escape(first_sentence(s['description']))}{tag} |")
        lines.append("")
    open(os.path.join(pdir, "README.md"), "w", encoding="utf-8").write("\n".join(lines))

    notice = [
        f"# NOTICE for {p['name']}",
        "",
        f"The skills in this plugin were written by **{p['author']}** and come from {p['upstream']}.",
        f"They are redistributed under their original license: {p['license']}. The full license text is in `LICENSE` (and any extra `LICENSE-*` file) in this folder.",
        "",
        f"Packaged for Claude by {CFG['packager']} as part of website-dev-skills ({REPO_URL}).",
        "",
        "Changes made while packaging:",
        f"- Plugin renamed to `{p['name']}` and given a new plugin.json.",
        "- Skill descriptions longer than 1024 characters were shortened, and angle brackets were removed, so they pass Claude's plugin validator. Skill instructions are unchanged.",
        "- Repository files that are not part of the skills (git history, CI files, tests) were left out.",
    ]
    if p["name"] == "website-dev-mengto-collection":
        notice.append("- Demo pages, demo videos and preview images not referenced by a skill were removed to keep the download small. They remain in the original repository.")
    if p["name"] == "website-dev-interface-guidelines":
        notice.append("- The original `command.md` was turned into a skill (`web-interface-guidelines`).")
    notice.append("")
    open(os.path.join(pdir, "NOTICE.md"), "w", encoding="utf-8").write("\n".join(notice))


def zip_dir(src, dest):
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for r, ds, fs in os.walk(src):
            ds[:] = [d for d in ds if d not in (".git", "node_modules", "__pycache__")]
            for f in sorted(fs):
                if f == ".DS_Store":
                    continue
                full = os.path.join(r, f)
                z.write(full, os.path.relpath(full, src))


def main():
    all_errors = []
    catalog = []
    per_plugin = {}
    for p in CFG["plugins"]:
        pdir = os.path.join(PLUGINS_DIR, p["name"])
        if not os.path.isdir(pdir):
            all_errors.append(f"missing plugin folder: plugins/{p['name']}")
            continue
        skills = skills_of(pdir)
        for s in skills:
            all_errors += validate_skill(p["name"], s["name"], s["path"])
        if not os.path.isfile(os.path.join(pdir, "LICENSE")) and p["name"] != "website-dev-shadcn-mcp":
            all_errors.append(f"plugins/{p['name']}: LICENSE file is missing")
        per_plugin[p["name"]] = skills
        for s in skills:
            catalog.append({"plugin": p["name"], "skill": s["name"], "invoke": f"/{p['name']}:{s['name']}", "bundle_invoke": f"/{BUNDLE}:{s['name']}", "manual_only": s["manual"], "description": s["description"]})

    names = [c["skill"] for c in catalog]
    dupes = sorted({n for n in names if names.count(n) > 1})
    if dupes:
        all_errors.append("skill names repeat across plugins (the bundle needs unique names): " + ", ".join(dupes))

    if all_errors:
        print("VALIDATION FAILED:")
        for e in all_errors:
            print("  -", e)
        sys.exit(1)
    total = len(catalog)
    print(f"Validation passed: {len(CFG['plugins'])} plugins, {total} skills.")
    if CHECK_ONLY:
        return

    for p in CFG["plugins"]:
        write_plugin_meta(p, per_plugin[p["name"]])

    # All-in-one bundle (skills only; the shadcn MCP stays a separate plugin)
    shutil.rmtree(BUILD, ignore_errors=True)
    bdir = os.path.join(BUILD, BUNDLE)
    os.makedirs(os.path.join(bdir, ".claude-plugin"))
    os.makedirs(os.path.join(bdir, "licenses"))
    for p in CFG["plugins"]:
        pdir = os.path.join(PLUGINS_DIR, p["name"])
        for s in per_plugin[p["name"]]:
            shutil.copytree(os.path.dirname(s["path"]), os.path.join(bdir, "skills", s["name"]))
        for f in os.listdir(pdir):
            if f.startswith("LICENSE"):
                shutil.copy(os.path.join(pdir, f), os.path.join(bdir, "licenses", f"{p['name']}.{f}"))
        shutil.copy(os.path.join(pdir, "NOTICE.md"), os.path.join(bdir, "licenses", f"{p['name']}.NOTICE.md"))
    shutil.copy(os.path.join(ROOT, "LICENSE"), os.path.join(bdir, "LICENSE"))
    shutil.copy(os.path.join(ROOT, "THIRD_PARTY_NOTICES.md"), os.path.join(bdir, "THIRD_PARTY_NOTICES.md"))
    bundle_count = len(os.listdir(os.path.join(bdir, "skills")))
    json.dump({
        "name": BUNDLE,
        "version": VERSION,
        "description": f"All-in-one website development pack: {bundle_count} skills for design taste, UI polish, UX, animation (GSAP, Framer Motion, Emil Kowalski), 3D/WebGL effects, components (21st.dev) and presentations. Packaged by {CFG['packager']}. Each skill keeps its original author's license (see licenses/).",
        "author": {"name": CFG["packager"]},
        "homepage": REPO_URL,
        "repository": REPO_URL,
        "license": "MIT",
        "keywords": ["website", "frontend", "design", "ui", "ux", "animation", "gsap", "framer-motion", "threejs"],
    }, open(os.path.join(bdir, ".claude-plugin", "plugin.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    open(os.path.join(bdir, "README.md"), "w", encoding="utf-8").write(
        f"# {BUNDLE}\n\nAll {bundle_count} skills from {REPO_URL} in one plugin. Every skill keeps its original author's license; see `licenses/` and `THIRD_PARTY_NOTICES.md`.\n")

    # Marketplace (Claude Code and Customize > Plugins > Add marketplace)
    market = {
        "name": MARKET,
        "description": f"website-dev-skills by {CFG['packager']}: {total} open-source skills for building websites with Claude.",
        "owner": {"name": "Rakshith", "url": "https://github.com/aiwithrakshi-dev"},
        "plugins": [
            {"name": p["name"], "source": f"./plugins/{p['name']}", "description": f"{p['title']}: {p['best_for']}", "version": VERSION, "category": p["category"]}
            for p in CFG["plugins"]
        ],
    }
    json.dump(market, open(os.path.join(ROOT, ".claude-plugin", "marketplace.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    json.dump({"version": VERSION, "repository": REPO_URL, "total_skills": total, "plugins": [
        {"name": p["name"], "title": p["title"], "author": p["author"], "license": p["license"], "upstream": p["upstream"], "skills": len(per_plugin[p["name"]])} for p in CFG["plugins"]
    ], "skills": catalog}, open(os.path.join(ROOT, "catalog.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)

    # docs/SKILLS.md: full catalog with full descriptions
    doc = [f"# Full skill catalog ({total} skills)", "", "Every skill in website-dev-skills, grouped by plugin, with its full description.", "Call a skill by name, for example `/website-dev-gsap:gsap-scrolltrigger`, or just describe the task and Claude picks the right one.", ""]
    for p in CFG["plugins"]:
        sk = per_plugin[p["name"]]
        if not sk:
            continue
        doc += [f"## {p['name']} ({len(sk)})", "", f"By {p['author']} · {p['license']} · source: {p['upstream']}", ""]
        for s in sk:
            doc.append(f"- **`{s['name']}`**{' (run by name only)' if s['manual'] else ''}: {s['description']}")
        doc.append("")
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    open(os.path.join(ROOT, "docs", "SKILLS.md"), "w", encoding="utf-8").write("\n".join(doc))

    # dist zips
    shutil.rmtree(DIST, ignore_errors=True)
    os.makedirs(DIST)
    for p in CFG["plugins"]:
        zip_dir(os.path.join(PLUGINS_DIR, p["name"]), os.path.join(DIST, f"{p['name']}.plugin"))
    zip_dir(bdir, os.path.join(DIST, f"{BUNDLE}.plugin"))

    from readme import write_readme  # noqa: E402  (scripts/readme.py)
    write_readme(ROOT, CFG, per_plugin, total, bundle_count)
    shutil.rmtree(BUILD, ignore_errors=True)
    print(f"Built {len(CFG['plugins']) + 1} .plugin files in dist/ ({bundle_count} skills in {BUNDLE}.plugin).")


if __name__ == "__main__":
    sys.path.insert(0, os.path.join(ROOT, "scripts"))
    main()
