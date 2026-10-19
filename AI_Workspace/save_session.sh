#!/bin/bash
# Save current AI session to the appropriate tool folder
# Usage: ./save_session.sh <tool> <session_name> [content_file]

TOOL="${1:-Hermes}"
SESSION_NAME="${2:-$(date +%Y-%m-%d_%H-%M-%S)}"
CONTENT="${3:-}"

SESSION_DIR="$HOME/Desktop/AI_Workspace/$TOOL/sessions"
mkdir -p "$SESSION_DIR"

SESSION_FILE="$SESSION_DIR/${SESSION_NAME}.md"

if [ -n "$CONTENT" ] && [ -f "$CONTENT" ]; then
    cp "$CONTENT" "$SESSION_FILE"
else
    cat > "$SESSION_FILE" << SESS_EOF
# Session: $SESSION_NAME
**Tool:** $TOOL
**Date:** $(date)
**Status:** Active

## Notes
[Add session notes here]

## Actions
- [ ] Action 1
- [ ] Action 2

## Files Generated
- None yet

SESS_EOF
fi

echo "Session saved to: $SESSION_FILE"
open "$SESSION_FILE"
