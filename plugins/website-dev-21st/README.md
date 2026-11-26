# website-dev-21st

**21st.dev Skills** · 8 skills · part of [website-dev-skills](https://github.com/aiwithrakshi-dev/claude-design-skills)

- **Original author:** 21st.dev
- **Original source:** [21st-dev/skill](https://github.com/21st-dev/skill) + [21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp)
- **License:** Apache-2.0 (21st-dev/skill) and ISC (21st-ui from 21st-dev/magic-mcp) (see `LICENSE` in this folder)
- **Best for:** Finding, installing and generating React/shadcn components from 21st.dev with the 21st CLI.

## Install

- **claude.ai or desktop app:** download [website-dev-21st.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-21st.plugin), then go to Customize > Plugins > Add > Upload plugin.
- **Claude Code (2.1.275 or later):** `/plugin install website-dev-21st --marketplace aiwithrakshi-dev/claude-design-skills`
- **Claude Code (any version):** `claude plugin marketplace add aiwithrakshi-dev/claude-design-skills` then `claude plugin install website-dev-21st@aiwithrakshi`

> **Before you use it:** Needs a free 21st.dev account: run `npx @21st-dev/cli login` or create an API key at https://21st.dev/mcp.

## Try these prompts

- Find a pricing table component on 21st.dev that matches my site and install it.
- Generate three hero section drafts with 21st AI and give me the code for the best one.
- Review my navbar and suggest a better 21st.dev component for it.

## Skills in this plugin

| Skill | What it does |
|---|---|
| `21st-ai` | Generate and iterate on UI with 21st AI from the terminal via the `21st` CLI (`@21st-dev/cli`): sketch a UI from a prompt, preview the variants in the browser, edit any… |
| `21st-cli-use` | Search, install and pull code from the 21st.dev catalog with the `21st` CLI (`@21st-dev/cli`): find React/shadcn components, themes and templates, print a component's… |
| `21st-design-sync` | Look at the current project's design (its shadcn / Tailwind CSS variables and color tokens) and publish it to the 21st.dev community as a shareable theme, using `21st… |
| `21st-registry` | Publish your own work to 21st.dev and manage it from the terminal with the `21st` CLI (`@21st-dev/cli`): publish a React component to a team library, publish a CSS… |
| `21st-ui` | Find, install, and generate UI with 21st.dev. |
| `21st-ui-build` | Build or substantially change production UI using the current project's design context, existing components, and grounded 21st inspiration. |
| `21st-ui-explore` | Explore and compare multiple meaningfully different UI directions grounded in the current project's design system and 21st inspiration. |
| `21st-ui-review` | Review existing UI against the project's design context, accessibility expectations, responsive behavior, interaction quality, and high-confidence production rules. |
