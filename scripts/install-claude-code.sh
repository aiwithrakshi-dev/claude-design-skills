#!/usr/bin/env bash
# Install website-dev-skills into Claude Code (macOS / Linux / WSL).
#   bash scripts/install-claude-code.sh          -> installs all 15 plugins
#   bash scripts/install-claude-code.sh gsap ui-polish   -> installs only those
set -euo pipefail
REPO="aiwithrakshi-dev/claude-design-skills"
MARKET="aiwithrakshi"
ALL="design-taste emil-motion gsap framer-motion motion-design ui-polish interface-guidelines ux-product oil-ui stageshow dimensional-drawing frontend-slides mengto-collection 21st shadcn-mcp"

if ! command -v claude >/dev/null 2>&1; then
  echo "Claude Code is not installed. Install it first: https://code.claude.com/docs" >&2
  exit 1
fi

echo "Adding the marketplace $REPO ..."
claude plugin marketplace add "$REPO" || claude plugin marketplace update "$MARKET"

PICK="${*:-$ALL}"
for p in $PICK; do
  echo "Installing website-dev-$p ..."
  claude plugin install "website-dev-$p@$MARKET"
done
echo "Done. Start a new Claude Code session (or run /reload-plugins) to use the skills."
