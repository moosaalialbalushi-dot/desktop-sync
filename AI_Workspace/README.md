# Unified AI Workspace
**Created:** 2026-09-12  
**Purpose:** Central hub for all AI tools — sessions, outputs, configs, shared knowledge

---

## Tool Structure

| Tool | Sessions | Projects | Notes | Outputs | Configs |
|------|----------|----------|-------|---------|---------|
| **Hermes** | `Hermes/sessions/` (→ `~/Desktop/Hermes_Work/`) | `Hermes/projects/` | `Hermes/notes/` | `Hermes/outputs/` | `Hermes/configs/` |
| **Claude Code** | `Claude_Code/sessions/` (→ `~/Desktop/Claude_Work/`) | `Claude_Code/projects/` | `Claude_Code/notes/` | `Claude_Code/outputs/` | `Claude_Code/configs/` |
| **OpenCode** | `OpenCode/sessions/` | `OpenCode/projects/` | `OpenCode/notes/` | `OpenCode/outputs/` | `OpenCode/configs/` |
| **OpenWebUI** | `OpenWebUI/sessions/` | `OpenWebUI/projects/` | `OpenWebUI/notes/` | `OpenWebUI/outputs/` | `OpenWebUI/configs/` |
| **ChatGPT** | `ChatGPT/sessions/` | `ChatGPT/projects/` | `ChatGPT/notes/` | `ChatGPT/outputs/` | `ChatGPT/configs/` |
| **Antigravity** | `Antigravity/sessions/` | `Antigravity/projects/` | `Antigravity/notes/` | `Antigravity/outputs/` | `Antigravity/configs/` |
| **Continue** | `Continue/sessions/` | `Continue/projects/` | `Continue/notes/` | `Continue/outputs/` | `Continue/configs/` |
| **Other** | `Other/sessions/` | `Other/projects/` | `Other/notes/` | `Other/outputs/` | `Other/configs/` |

---

## Shared Knowledge Base

| Category | Path | Description |
|----------|------|-------------|
| **Brain Memory** | `Shared_Knowledge/brain_memory/` | Exports from Hermes brain/RAG |
| **Obsidian Vault** | `Shared_Knowledge/obsidian_vault/` | Symlink to `~/OneDrive/Desktop/Claude Obsidian/` |
| **Pharma Data** | `Shared_Knowledge/pharma_data/` | Al Wajer, KAD, trade data |
| **Trade Data** | `Shared_Knowledge/trade_data/` | EXIM, supplier, market intel |
| **Projects** | `Shared_Knowledge/projects/` | Cross-tool project files |
| **Meetings** | `Shared_Knowledge/meetings/` | Meeting notes, action items |

---

## Quick Commands

```bash
# Open Hermes session folder
cd ~/Desktop/AI_Workspace/Hermes/sessions/

# Open Obsidian vault
cd ~/Desktop/AI_Workspace/Shared_Knowledge/obsidian_vault/

# Save current session to tool folder
# (use the save_session script below)
```

---

## Integration Points

1. **Hermes** → saves to `Hermes/sessions/` via `file_publisher`
2. **Claude Code** → already saves to `Claude_Work/` (symlinked)
3. **OpenCode** → configure output dir to `OpenCode/outputs/`
4. **OpenWebUI** → export chats to `OpenWebUI/sessions/`
5. **ChatGPT** → export conversations to `ChatGPT/sessions/`
6. **Antigravity (agy)** → save sessions to `Antigravity/sessions/`
7. **Continue** → configure to save to `Continue/sessions/`

---

## Brain/RAG Status
- **VPS**: `91.98.94.195:8010` — REST API for semantic search
- **Local**: `~/.hermes/state.db`, `projects.db`, `kanban.db`
- **MCP Tools**: `mcp__brain__search_memory`, `mcp__moosa_hermes__hermes_brain_query`

---

## Obsidian Vault
- **Location**: `~/OneDrive/Desktop/Claude Obsidian/` (synced)
- **Symlink**: `~/Desktop/AI_Workspace/Shared_Knowledge/obsidian_vault/`
- **Contains**: 392+ markdown files, Moosa Business, Finance, Production, etc.

