# website-dev-shadcn-mcp

**shadcn/ui MCP connector** · MCP connector · part of [website-dev-skills](https://github.com/aiwithrakshi-dev/claude-design-skills)

- **Original author:** shadcn
- **Original source:** [shadcn-ui/ui](https://github.com/shadcn-ui/ui)
- **License:** Configuration only (MIT, this repository); the shadcn CLI itself is MIT (see `LICENSE` in this folder)
- **Best for:** Letting Claude browse, search and install shadcn/ui components and registries.

## Install

- **claude.ai or desktop app:** download [website-dev-shadcn-mcp.plugin](https://github.com/aiwithrakshi-dev/claude-design-skills/raw/main/dist/website-dev-shadcn-mcp.plugin), then go to Customize > Plugins > Add > Upload plugin.
- **Claude Code (2.1.275 or later):** `/plugin install website-dev-shadcn-mcp --marketplace aiwithrakshi-dev/claude-design-skills`
- **Claude Code (any version):** `claude plugin marketplace add aiwithrakshi-dev/claude-design-skills` then `claude plugin install website-dev-shadcn-mcp@aiwithrakshi`

> **Before you use it:** Runs `npx shadcn@latest mcp` locally, so it works in Claude Code and the Claude desktop app on a computer with Node.js 18+. It does not run in the claude.ai web app.

## Try these prompts

- Using shadcn, add a data table with sorting and pagination to my dashboard.
- Show me the available shadcn components for forms and install the ones I need.
- Install the calendar and date-picker components from shadcn.
