# Install website-dev-skills into Claude Code (Windows PowerShell).
#   powershell -ExecutionPolicy Bypass -File scripts\install-claude-code.ps1
#   powershell -ExecutionPolicy Bypass -File scripts\install-claude-code.ps1 gsap ui-polish
$ErrorActionPreference = "Stop"
$Repo = "aiwithrakshi-dev/claude-design-skills"
$Market = "aiwithrakshi"
$All = @("design-taste","emil-motion","gsap","framer-motion","motion-design","ui-polish","interface-guidelines","ux-product","oil-ui","stageshow","dimensional-drawing","frontend-slides","mengto-collection","21st","shadcn-mcp")

if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
  Write-Error "Claude Code is not installed. Install it first: https://code.claude.com/docs"
}
Write-Host "Adding the marketplace $Repo ..."
try { claude plugin marketplace add $Repo } catch { claude plugin marketplace update $Market }

$Pick = if ($args.Count -gt 0) { $args } else { $All }
foreach ($p in $Pick) {
  Write-Host "Installing website-dev-$p ..."
  claude plugin install "website-dev-$p@$Market"
}
Write-Host "Done. Start a new Claude Code session (or run /reload-plugins) to use the skills."
