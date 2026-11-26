"""Writes README.md for the repository. Called by scripts/build.py."""
import os
import re

RAW = "https://github.com/{repo}/raw/main/dist/{file}"


def _first(text, limit=150):
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    s = m.group(1) if m else text
    return s if len(s) <= limit else s[: limit - 1].rsplit(" ", 1)[0] + "…"


def write_readme(root, cfg, per_plugin, total, bundle_count):
    repo = cfg["repo"]
    url = f"https://github.com/{repo}"
    market = cfg["marketplace"]
    bundle = cfg["bundle"]
    plugins = cfg["plugins"]
    size = lambda f: os.path.getsize(os.path.join(root, "dist", f)) / 1e6
    L = []
    a = L.append

    a(f"# website-dev-skills")
    a("")
    a(f"**{total} open-source skills that teach Claude to design and build better websites**: design taste, UI polish, UX, animation (GSAP, Framer Motion, Emil Kowalski), 3D and WebGL effects, React components and presentations, packaged as ready-to-install Claude plugins.")
    a("")
    a(f"![License: MIT](https://img.shields.io/badge/packaging-MIT-green) ![Skills](https://img.shields.io/badge/skills-{total}-blue) ![Plugins](https://img.shields.io/badge/plugins-{len(plugins)}%20%2B%20all--in--one-purple) ![Works with](https://img.shields.io/badge/works%20with-claude.ai%20%7C%20Desktop%20%7C%20Claude%20Code-orange)")
    a("")
    a("Collected, fixed and packaged by **Rakshith** ([@aiwithrakshi.global](https://www.instagram.com/aiwithrakshi.global) · [MyDesignNexus](https://www.instagram.com/mydesignnexus.in)). The skills themselves were written by the authors credited below. Every skill keeps its original open-source license.")
    a("")
    a("---")
    a("")
    a("## Contents")
    a("")
    for t in ["What's inside", "Install in 2 minutes", "How to use the skills", "Sample prompts", "A full example session", "Full skill list", "Troubleshooting", "FAQ", "Rebuild or contribute", "Credits and licenses"]:
        a(f"- [{t}](#{re.sub(r'[^a-z0-9 -]', '', t.lower()).replace(' ', '-')})")
    a("")

    # ---------- What's inside
    a("## What's inside")
    a("")
    a(f"You can install everything at once with **`{bundle}`** ({bundle_count} skills in one plugin), or pick only the plugins you need.")
    a("")
    a("| Plugin | Skills | Original author | Best for | Download |")
    a("|---|---:|---|---|---|")
    a(f"| **{bundle}** (all-in-one) | {bundle_count} | Everyone below | Everything in this repo, one install | [{bundle}.plugin]({RAW.format(repo=repo, file=bundle + '.plugin')}) ({size(bundle + '.plugin'):.0f} MB) |")
    for p in plugins:
        n = len(per_plugin[p["name"]])
        f = p["name"] + ".plugin"
        a(f"| [`{p['name']}`](plugins/{p['name']}) | {n if n else 'MCP'} | {p['author']} | {p['best_for']} | [{f}]({RAW.format(repo=repo, file=f)}) |")
    a("")
    a("> The all-in-one bundle contains every skill but **not** the shadcn connector. Install `website-dev-shadcn-mcp` on its own if you want it (it needs Claude Code or the desktop app).")
    a("")

    # ---------- Install
    a("## Install in 2 minutes")
    a("")
    a("Pick the way that matches where you use Claude. You only need one of them.")
    a("")
    a("### Option 1: claude.ai or the Claude desktop app, by uploading a file (easiest)")
    a("")
    a(f"1. Download **[{bundle}.plugin]({RAW.format(repo=repo, file=bundle + '.plugin')})**, or any single plugin from the table above.")
    a("2. Open **[Customize > Plugins](https://claude.ai/customize/plugins)** in claude.ai or the desktop app.")
    a("3. Select **Add**, then **Upload plugin**, and choose the file you downloaded.")
    a("4. Open the plugin and make sure its toggle is on.")
    a("5. Start a new chat and try a prompt from [Sample prompts](#sample-prompts).")
    a("")
    a("The plugin is saved to your account, so it also appears in Cowork and in Claude Code (run `/reload-plugins` there).")
    a("")
    a("### Option 2: claude.ai or the desktop app, as a marketplace (gets updates automatically)")
    a("")
    a("1. Open **[Customize > Plugins](https://claude.ai/customize/plugins)** and select **Add**, then **Add marketplace**.")
    a(f"2. Enter `{repo}` (or `{url}`).")
    a("3. The 15 plugins now appear in your plugin list. Select the ones you want and press **Add**.")
    a("4. To get new versions later, select **Check for updates**, or turn on **Sync automatically**.")
    a("")
    a("### Option 3: Claude Code (terminal, VS Code, JetBrains)")
    a("")
    a("On Claude Code 2.1.275 or later, one line installs a plugin straight from this repo:")
    a("")
    a("```bash")
    a(f"/plugin install website-dev-gsap --marketplace {repo}")
    a("```")
    a("")
    a("On any version, add the marketplace once, then install what you want:")
    a("")
    a("```bash")
    a(f"claude plugin marketplace add {repo}")
    a("")
    a("# install one plugin")
    a(f"claude plugin install website-dev-gsap@{market}")
    a("")
    a("# or install all 15 plugins with the script in this repo")
    a(f"git clone {url}.git")
    a("cd claude-design-skills")
    a("bash scripts/install-claude-code.sh                 # macOS, Linux, WSL")
    a("powershell -ExecutionPolicy Bypass -File scripts\\install-claude-code.ps1   # Windows")
    a("```")
    a("")
    a(f"Inside a Claude Code session you can do the same with `/plugin marketplace add {repo}` and then `/plugin`. To install only a few with the script, name them: `bash scripts/install-claude-code.sh gsap ui-polish design-taste`.")
    a("")
    a("### Option 4: copy single skills by hand")
    a("")
    a("Every skill is a normal folder with a `SKILL.md`. Copy any folder from `plugins/<plugin>/skills/` into `~/.claude/skills/` (Claude Code) or zip it and upload it in **Customize > Skills**.")
    a("")
    a("### Requirements")
    a("")
    a("- A Claude account. Plugins and skills are added from **Customize** on claude.ai and the desktop app, or with Claude Code.")
    a("- Some skills write and run code (for example screenshots, checks or builds). They work best in Claude Code or the desktop app, where Claude can use your project folder.")
    for p in plugins:
        if p.get("note"):
            a(f"- **{p['name']}:** {p['note']}")
    a("")

    # ---------- How to use
    a("## How to use the skills")
    a("")
    a("You don't need to remember skill names. **Describe the task and Claude loads the right skill by itself.** For example, \"add a GSAP scroll animation that pins the hero\" loads the GSAP ScrollTrigger skill.")
    a("")
    a("To pick a skill yourself:")
    a("")
    a("- **claude.ai and desktop:** type `/` in the message box, type the plugin or skill name, and select it.")
    a("- **Claude Code:** type `/plugin-name:skill-name`, for example `/website-dev-gsap:gsap-scrolltrigger`. If you installed the all-in-one bundle, use `/website-dev-skills:gsap-scrolltrigger`.")
    a("")
    a("A few skills only run when you call them by name, so Claude never starts them on its own. They are marked *run by name* in the [full skill list](#full-skill-list). Examples: `/review-animations`, `/prototype`, `/learn-taste`.")
    a("")
    a("**Tips for the best results**")
    a("")
    a("- Say what you are building and for whom: \"a landing page for a dental clinic in Mysuru\" works better than \"a landing page\".")
    a("- Name the stack when it matters: plain HTML, React, Next.js, Tailwind, Vue.")
    a("- Ask for a review after a build: \"now review it with the web interface guidelines\" or \"run baseline-ui on it\".")
    a("- Combine skills: design-taste for the look, GSAP or Framer Motion for motion, ui-polish for the final pass.")
    a("")

    # ---------- Samples
    a("## Sample prompts")
    a("")
    a("Copy any of these into Claude after installing the matching plugin (or the all-in-one bundle).")
    a("")
    for p in plugins:
        a(f"### {p['title']} (`{p['name']}`)")
        a("")
        for s in p["samples"]:
            a(f"```text\n{s}\n```")
        a("")

    # ---------- Example session
    a("## A full example session")
    a("")
    a("Here is how several skills work together on one real task, a portfolio landing page:")
    a("")
    a("```text")
    a("You:    Build a one-page portfolio for a Bengaluru UI designer. Plain HTML, CSS and JS.")
    a("        Make it feel premium and hand-made, with a calm entrance animation.")
    a("Claude: (loads design-taste-frontend) picks a direction, type scale and palette,")
    a("        then builds the page section by section.")
    a("")
    a("You:    Add a scroll animation where the project cards slide in and the hero pins.")
    a("Claude: (loads gsap-scrolltrigger and gsap-timeline) adds ScrollTrigger with cleanup")
    a("        and a reduced-motion fallback.")
    a("")
    a("You:    Now check it before I publish.")
    a("Claude: (loads web-interface-guidelines and fixing-accessibility) lists problems such as")
    a("        missing alt text, weak focus states and small touch targets, then fixes them.")
    a("")
    a("You:    /review-animations")
    a("Claude: reviews every animation for timing, easing and interruptibility and suggests fixes.")
    a("```")
    a("")

    # ---------- Full list
    a("## Full skill list")
    a("")
    a(f"All {total} skills, grouped by plugin. Open a group to see every skill. Full descriptions are in [docs/SKILLS.md](docs/SKILLS.md) and machine-readable data is in [catalog.json](catalog.json).")
    a("")
    for p in plugins:
        sk = per_plugin[p["name"]]
        if not sk:
            continue
        a(f"<details>\n<summary><b>{p['name']}</b> · {len(sk)} skill{'s' if len(sk) != 1 else ''} · by {p['author']}</summary>\n")
        a("| Skill | What it does |")
        a("|---|---|")
        for s in sk:
            tag = " *(run by name)*" if s["manual"] else ""
            a(f"| `{s['name']}` | {_first(s['description']).replace('|', '/')}{tag} |")
        a("\n</details>\n")
    a("")

    # ---------- Troubleshooting
    a("## Troubleshooting")
    a("")
    a("| Problem | Fix |")
    a("|---|---|")
    a("| **Upload says plugin validation failed** | Download the file again from this repo. Every skill here passes the validator (`python3 scripts/build.py --check`). If you edited a skill, keep its description under 1024 characters and without `<` or `>`. |")
    a("| **Upload says plugin.json must be at the root** | Upload the `.plugin` file as it is. Don't unzip it and re-zip the parent folder. |")
    a("| **A skill never seems to run** | Describe the task more specifically, or call it directly with `/` (claude.ai) or `/plugin-name:skill-name` (Claude Code). Some skills only run by name. |")
    a("| **The plugin is installed but skills are missing** | Open **Customize > Plugins**, open the plugin and check that its toggle is on. In Claude Code run `/reload-plugins` or start a new session. |")
    a("| **Too many similar skills load** | Install only the plugins you need instead of the all-in-one bundle, or turn off plugins you aren't using. |")
    a("| **shadcn connector doesn't work on claude.ai web** | It runs a local command (`npx shadcn@latest mcp`), so it only works in Claude Code and the desktop app, with Node.js 18 or newer installed. |")
    a("| **21st.dev skills ask for a login** | Run `npx @21st-dev/cli login`, or create an API key at https://21st.dev/mcp and set `TWENTYFIRST_TOKEN`. |")
    a("| **`claude plugin install` says plugin not found** | Use the name exactly as listed, with `@aiwithrakshi` at the end, for example `website-dev-gsap@aiwithrakshi`. Run `claude plugin marketplace update aiwithrakshi` first. |")
    a("| **Script says Claude Code is not installed** | Install Claude Code from https://code.claude.com/docs, open a new terminal, then run the script again. |")
    a("")

    # ---------- FAQ
    a("## FAQ")
    a("")
    a("**Is it free?** Yes. The skills are open source and so is this packaging. You need your own Claude account to use them.")
    a("")
    a("**Who wrote the skills?** The original authors in the [credits](#credits-and-licenses). This repository collects them, fixes descriptions so they pass Claude's validator, renames the plugins consistently, and adds install files, docs and scripts. Each plugin's `NOTICE.md` lists exactly what changed.")
    a("")
    a(f"**All-in-one or separate plugins?** The bundle is the quickest way to try everything. Separate plugins are better for daily use: fewer skills means Claude picks the right one more reliably, and you can turn groups on and off.")
    a("")
    a("**Do 343 skills slow Claude down?** Claude only reads a skill's short description until a task needs it, then loads the full instructions. Still, if you see the wrong skill being picked, install fewer plugins.")
    a("")
    a("**Can I use these at work or in client projects?** Yes, under each skill's license (almost all are MIT; the 21st.dev skills are Apache-2.0 and ISC). Keep the license files when you share them.")
    a("")
    a("**How do I update?** Marketplace installs: **Check for updates** in Customize > Plugins, or `claude plugin marketplace update aiwithrakshi` in Claude Code. File uploads: download the new `.plugin` file and upload it again.")
    a("")
    a("**Is this affiliated with Anthropic, GSAP, Vercel or the authors?** No. It's a community collection. Product names belong to their owners.")
    a("")

    # ---------- Rebuild
    a("## Rebuild or contribute")
    a("")
    a("```bash")
    a("pip install pyyaml")
    a("python3 scripts/build.py --check   # validate every skill, change nothing")
    a("python3 scripts/build.py           # rebuild plugin.json files, READMEs, docs, catalog.json and dist/*.plugin")
    a("claude plugin validate .           # optional: Claude Code's own marketplace check")
    a("```")
    a("")
    a("Repository layout:")
    a("")
    a("```text")
    a(".claude-plugin/marketplace.json   marketplace for Claude Code and Customize > Plugins > Add marketplace")
    a("plugins/<name>/                   one folder per plugin: skills/, LICENSE, NOTICE.md, README.md")
    a("dist/*.plugin                     ready-to-upload files, including the all-in-one bundle")
    a("docs/SKILLS.md                    every skill with its full description")
    a("catalog.json                      the same list as data (plugin, skill, how to call it)")
    a("scripts/plugins.json              plugin names, credits and sample prompts (edit this, then build)")
    a("scripts/build.py                  validator and builder")
    a("scripts/install-claude-code.*     install all plugins into Claude Code")
    a("```")
    a("")
    a("To suggest a skill, report a broken one or ask for a change, open an issue or a pull request. If you are one of the original authors and want your work changed or removed, open an issue and it will be handled quickly.")
    a("")

    # ---------- Credits
    a("## Credits and licenses")
    a("")
    a("The packaging in this repository (scripts, manifests, marketplace file and documentation) is released under the [MIT License](LICENSE). **Each skill keeps its author's license**, included in every plugin folder and in the bundle's `licenses/` folder. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).")
    a("")
    a("| Plugin | Written by | Original repository | License |")
    a("|---|---|---|---|")
    for p in plugins:
        links = " + ".join(f"[{u.strip().split(' ')[0]}](https://github.com/{u.strip().split(' ')[0]})" for u in p["upstream"].split("+") if "/" in u.strip().split(" ")[0])
        a(f"| `{p['name']}` | {p['author']} | {links or p['upstream']} | {p['license']} |")
    a("")
    a("Thank you to every author for publishing their work openly. Please star their repositories.")
    a("")
    a("---")
    a("")
    a("Made in Karnataka by **Rakshith** · Founder, MyDesignNexus · Instagram: [@AIwithRakshith (Kannada)](https://www.instagram.com/aiwithrakshi) · [@aiwithrakshi.global](https://www.instagram.com/aiwithrakshi.global) · [@mydesignnexus.in](https://www.instagram.com/mydesignnexus.in)")
    a("")
    open(os.path.join(root, "README.md"), "w", encoding="utf-8").write("\n".join(L))
