#!/bin/zsh
# Local Mode launcher - built 2026-09-28, rebuilt 2026-10-15 from the measured memory audit
# (see memory-hogs-audit-20261015). Set LOCALMODE_DRYRUN=1 to list what it WOULD quit, changing nothing.
# Keeps: Chrome, Finder, Terminal, Claude, Ollama (the engine for all 3 tiers).

APPS=("Notes" "Pages" "Keynote" "Numbers" "Tips" "OpenCode" "QuickTime Player" "Preview" "Mail" "Music" "Telegram" "Calendar" "System Settings")

if [ -n "$LOCALMODE_DRYRUN" ]; then
  for app in $APPS; do pgrep -xq "$app" && echo "would quit: $app"; done
  pgrep -f mlx_lm.server >/dev/null && echo "would stop: MLX server (frees ~3-5 GB)"
  sysctl vm.swapusage; exit 0
fi

CHOICE=$(osascript -e 'choose from list {"Fast chat - instant, no memory (~20s)", "Local + memory/brain/skills - recommended (~10-15s)", "Full Hermes agent - every tool, several minutes to warm up"} with prompt "Which local mode?" default items {"Local + memory/brain/skills - recommended (~10-15s)"}')
[ "$CHOICE" = "false" ] && { echo "Cancelled."; exit 0; }

echo "Closing non-essential apps (keeping Chrome, Finder, Terminal, Claude, Ollama)..."
echo "If Pages/Keynote/Numbers ask to save, answer on screen - nothing is force-closed."
for app in $APPS; do osascript -e "tell application \"$app\" to quit" >/dev/null 2>&1 & done
pkill -f app_mode_loader >/dev/null 2>&1
# MLX server is on-demand since 2026-10-15 (pdfask restarts it); free its 3-5 GB for the Ollama model
launchctl stop com.moosa.mlx-server >/dev/null 2>&1
disown -a 2>/dev/null

echo "Opening Activity Monitor so you can watch memory free up..."
open -a "Activity Monitor"

case "$CHOICE" in
  "Fast chat"*)  CMD='ollama run gemma4-12b-ponytail --think=false' ;;
  "Local + memory"*) CMD='hermes chat -m ponytail-local --reasoning none -t "$HERMES_LEAN_TOOLSETS"' ;;
  "Full Hermes"*) CMD='hermes chat -m ponytail-local --reasoning none' ;;
esac

osascript <<OSA
tell application "Terminal"
  activate
  do script "$CMD"
end tell
OSA
