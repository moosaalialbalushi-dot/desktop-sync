#!/bin/bash
# Desktop → Server Sync Script
# Generated: 2026-10-19

set -e  # Exit on error

SSH_KEY="$HOME/.ssh/ollama_server_key"
SERVER="hermes@91.98.94.195"

echo "=== DESKTOP → SERVER SYNC ==="
echo "Starting sync at $(date)"
echo

# 1. Business data files
echo "[1/4] Syncing business data files..."
rsync -avz --progress -e "ssh -i $SSH_KEY" \
  "$HOME/Desktop/Claude_Work/files/CPHI_Milan_2026_Approach_Plan.xlsx" \
  "$HOME/Desktop/Claude_Work/files/CPHI_Milan_2026_Leads.xlsx" \
  "$HOME/Desktop/Al Wajer NPI Product Intelligence - 150 Products.xlsx" \
  "$HOME/Desktop/GMP_ MOH_Points__DT 14.09.2026.xlsx" \
  "$HOME/Desktop/Alwajer _Requirement Details_24-09-2026.xlsx" \
  "$HOME/Desktop/sudan_analysis.pptx" \
  "$HOME/Desktop/Document4 (1).docx" \
  "$SERVER:~/.hermes/uploads/pharma_data/"

# 2. CRM scripts
echo "[2/4] Syncing CRM scripts..."
rsync -avz --progress -e "ssh -i $SSH_KEY" \
  "$HOME/Desktop/update_crm.py" \
  "$HOME/Desktop/update_client_db.py" \
  "$HOME/Desktop/update_client_db_full.py" \
  "$SERVER:~/.hermes/scripts/mac_imports/"

# 3. AI Workspace logs
echo "[3/4] Syncing AI Workspace logs..."
rsync -avz --progress -e "ssh -i $SSH_KEY" \
  "$HOME/Desktop/AI_Workspace/" \
  "$SERVER:~/.hermes/uploads/ai_workspace_logs/"

# 4. CPHI marketing materials
echo "[4/4] Syncing CPHI Milan materials..."
rsync -avz --progress -e "ssh -i $SSH_KEY" \
  "$HOME/Desktop/Claude_Work/files/" \
  "$SERVER:~/obsidian-sync/Research/CPHI_Milan_2026/"

echo
echo "=== VERIFICATION ==="
ssh -i "$SSH_KEY" "$SERVER" '
  echo "Files landed on server:"
  echo "  Pharma data: $(ls -1 ~/.hermes/uploads/pharma_data/ 2>/dev/null | wc -l) files"
  echo "  Scripts: $(ls -1 ~/.hermes/scripts/mac_imports/ 2>/dev/null | wc -l) files"
  echo "  AI Workspace: $(ls -1 ~/.hermes/uploads/ai_workspace_logs/ 2>/dev/null | wc -l) files"
  echo "  CPHI materials: $(ls -1 ~/obsidian-sync/Research/CPHI_Milan_2026/ 2>/dev/null | wc -l) files"
'

echo
echo "=== INGESTION ==="
echo "Triggering brain indexing..."
ssh -i "$SSH_KEY" "$SERVER" \
  'cd ~/.hermes/rag && ./venv/bin/python brain_indexer.py --source ~/.hermes/uploads/pharma_data/ 2>&1 | tail -5'

echo
echo "✅ Sync complete at $(date)"
echo
echo "Next steps:"
echo "  1. Parse CPHI_Milan_2026_Leads.xlsx for new contacts"
echo "  2. Update CRM with any new suppliers found"
echo "  3. Archive/delete Screen Recording (1.94 GB)"
