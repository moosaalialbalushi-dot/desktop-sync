# Desktop Audit Report
**Date:** 2026-10-19  
**Location:** /Users/moosaali/Desktop  
**Total Files:** 31,024 files (4,804.91 MB)

---

## Executive Summary

✅ **31,024 files catalogued** across Desktop  
📦 **4.8 GB total** — mostly Deep-Live-Cam-fast project (3.5 GB)  
📊 **5 business-critical Excel files** found (CPHI leads, NPI products, GMP checklist)  
🔧 **3 CRM update scripts** ready for server sync  
⚠️ **No Exim credentials found** — likely on Windows laptop or OneDrive  

### Key Findings

| Category | Count | Action Required |
|----------|-------|-----------------|
| Claude Code Projects | 1 (Deep-Live-Cam-fast) | ✅ Already on Desktop, skip sync |
| Business Data (xlsx/pptx/docx) | 8 files | 🟢 PRIORITY SYNC to server |
| CRM Scripts | 3 Python scripts | 🟢 Sync to server scripts/ |
| AI Workspace Logs | 2 folders | 🟢 Sync for reference |
| Large media files | 1 video (1.9 GB) | ⚠️ Skip (>500MB) |
| Python environments | 1 (.venv 2.3 GB) | ⚠️ Skip (regenerate on server) |

---

## Priority Sync Queue

### 🔴 HIGH PRIORITY — Business Data Files

```bash
# Sync business-critical Excel/PowerPoint files
rsync -avz --progress -e "ssh -i ~/.ssh/ollama_server_key" \
  "/Users/moosaali/Desktop/Claude_Work/files/CPHI_Milan_2026_Approach_Plan.xlsx" \
  "/Users/moosaali/Desktop/Claude_Work/files/CPHI_Milan_2026_Leads.xlsx" \
  "/Users/moosaali/Desktop/Al Wajer NPI Product Intelligence - 150 Products.xlsx" \
  "/Users/moosaali/Desktop/GMP_ MOH_Points__DT 14.09.2026.xlsx" \
  "/Users/moosaali/Desktop/Alwajer _Requirement Details_24-09-2026.xlsx" \
  "/Users/moosaali/Desktop/sudan_analysis.pptx" \
  "/Users/moosaali/Desktop/Document4 (1).docx" \
  hermes@91.98.94.195:~/.hermes/uploads/pharma_data/
```

### 🟠 MEDIUM PRIORITY — CRM Scripts

```bash
# Sync CRM update scripts
rsync -avz --progress -e "ssh -i ~/.ssh/ollama_server_key" \
  "/Users/moosaali/Desktop/update_crm.py" \
  "/Users/moosaali/Desktop/update_client_db.py" \
  "/Users/moosaali/Desktop/update_client_db_full.py" \
  hermes@91.98.94.195:~/.hermes/scripts/mac_imports/
```

### 🟡 MEDIUM PRIORITY — AI Workspace Logs

```bash
# Sync Claude Code and Hermes logs for reference
rsync -avz --progress -e "ssh -i ~/.ssh/ollama_server_key" \
  "/Users/moosaali/Desktop/AI_Workspace/" \
  hermes@91.98.94.195:~/.hermes/uploads/ai_workspace_logs/
```

### 🟡 MEDIUM PRIORITY — CPHI Milan Marketing Materials

```bash
# Sync all CPHI Milan print materials (banners, brochures, business cards)
rsync -avz --progress -e "ssh -i ~/.ssh/ollama_server_key" \
  "/Users/moosaali/Desktop/Claude_Work/files/" \
  hermes@91.98.94.195:~/obsidian-sync/Research/CPHI_Milan_2026/
```

---

## File Inventory

### Claude Code Projects

| Project | Purpose | Tech Stack | Size | Modified |
|---------|---------|------------|------|----------|
| **Deep-Live-Cam-fast** | Face swap tool (headless, CoreML, M4 optimized) | Python, ONNX, OpenCV, PyTorch | 3.5 GB | 2026-10-19 |

**Status:** Active development, already on Desktop, no sync needed.

---

### Business Data Files

#### Excel Files (5 files, 0.54 MB total)

| File | Size | Modified | Summary | Sync To |
|------|------|----------|---------|---------|
| CPHI_Milan_2026_Approach_Plan.xlsx | 0.26 MB | 2026-10-06 | Trade show approach plan | `pharma_data/` |
| CPHI_Milan_2026_Leads.xlsx | 0.18 MB | 2026-10-05 | Lead list for Milan event | `pharma_data/` |
| Al Wajer NPI Product Intelligence - 150 Products.xlsx | 0.08 MB | 2026-09-27 | NPI product catalog | `pharma_data/` |
| GMP_ MOH_Points__DT 14.09.2026.xlsx | 0.01 MB | 2026-09-15 | GMP compliance checklist | `pharma_data/` |
| Alwajer _Requirement Details_24-09-2026.xlsx | 0.01 MB | 2026-09-28 | Requirements spec | `pharma_data/` |

#### PowerPoint (1 file)

| File | Size | Modified | Summary | Sync To |
|------|------|----------|---------|---------|
| sudan_analysis.pptx | 0.04 MB | 2026-09-27 | Market analysis | `pharma_data/` |

#### Word Documents (1 file)

| File | Size | Modified | Summary | Sync To |
|------|------|----------|---------|---------|
| Document4 (1).docx | 0.02 MB | 2026-09-27 | Unknown content | `pharma_data/` |

---

### Scripts Found on Desktop Root

| Script | Purpose | Language | Sync To |
|--------|---------|----------|---------|
| update_crm.py | CRM database updater | Python | `scripts/mac_imports/` |
| update_client_db.py | Client database sync | Python | `scripts/mac_imports/` |
| update_client_db_full.py | Full client DB rebuild | Python | `scripts/mac_imports/` |

---

### Large Files (Skip — Too Large or Redundant)

| File | Size | Reason |
|------|------|--------|
| Screen Recording 2026-10-13 at 10.27.54 AM.mov | 1.94 GB | >500MB, skip unless critical |
| Deep-Live-Cam-fast/models/* | 1.5 GB | ONNX models, regenerate on server if needed |
| Deep-Live-Cam-fast/.venv/* | 2.3 GB | Python venv, skip (pip install on server) |

---

## Credentials & API Keys Found

**No sensitive credentials detected in root Desktop files.**

The following are internal library config files (safe to ignore):
- Deep-Live-Cam-fast torch/torchgen YAML configs (25 files)
- GitHub workflow yamls (1 file)

---

## New CRM Records to Create

### Contacts Extracted from Business Files

Based on file names and known context, the following contacts **may** need CRM entries. Manual verification required:

**No new contacts found in file names.** All business files relate to existing entities:
- Al-Wajer Pharma (already in CRM)
- CPHI Milan 2026 (event, not a contact)
- MOH Oman (already in CRM)
- Sudan analysis (region, not a contact)

**Action:** After server sync, open Excel files and extract any new supplier/customer names from:
- `CPHI_Milan_2026_Leads.xlsx` → parse company/contact columns
- `Al Wajer NPI Product Intelligence - 150 Products.xlsx` → check supplier column

---

## Server-Side Ingestion Commands

After sync, SSH into server and run:

```bash
# 1. Verify files landed
ssh -i ~/.ssh/ollama_server_key hermes@91.98.94.195 '
  echo "=== Pharma Data ===" && ls -lh ~/.hermes/uploads/pharma_data/ && echo
  echo "=== Scripts ===" && ls -lh ~/.hermes/scripts/mac_imports/ && echo
  echo "=== AI Workspace ===" && ls -lh ~/.hermes/uploads/ai_workspace_logs/ && echo
  echo "=== CPHI Materials ===" && ls -lh ~/obsidian-sync/Research/CPHI_Milan_2026/
'

# 2. Parse Excel files for new CRM contacts
ssh -i ~/.ssh/ollama_server_key hermes@91.98.94.195 \
  'python3 ~/.hermes/scripts/mac_imports/update_crm.py'

# 3. Ingest pharma data into brain/RAG
ssh -i ~/.ssh/ollama_server_key hermes@91.98.94.195 \
  'cd ~/.hermes/rag && ./venv/bin/python brain_indexer.py --source ~/.hermes/uploads/pharma_data/'

# 4. Refresh graphify knowledge graph
ssh -i ~/.ssh/ollama_server_key hermes@91.98.94.195 \
  'python3 ~/.hermes/scripts/graphify_refresh.py 2>/dev/null || echo "Graphify refresh needs manual run"'
```

---

## Cleanup Recommendations

### Safe to Delete (After Sync)

1. **Screen Recording 2026-10-13 at 10.27.54 AM.mov** (1.94 GB)  
   → Archive to external drive or delete if no longer needed

2. **altserver.zip** (12.1 MB)  
   → AltStore installer, re-downloadable, safe to delete

3. **AI_Workspace/** logs (after sync)  
   → Archive for reference but not needed on Desktop

### Keep on Desktop

- **Deep-Live-Cam-fast/** — active development project
- **Claude_Work/** — active project folder with marketing materials
- All `.command` launchers (Hermes.command, Local Mode.command, etc.)

---

## Next Steps

### Immediate Actions (5 min)

1. ✅ **Run priority sync commands** (business data + scripts)
2. ✅ **Verify files landed on server** (SSH verification command)
3. ✅ **Trigger brain indexing** (pharma data → RAG)

### Follow-Up Actions (30 min)

4. 🔍 **Parse CPHI_Milan_2026_Leads.xlsx** on server → extract new contacts
5. 🔍 **Parse Al Wajer NPI Product Intelligence** → extract supplier names
6. 📝 **Create CRM records** for any new suppliers/contacts found
7. 🧹 **Archive screen recording** to external drive
8. 🧹 **Delete altserver.zip** after confirming AltStore is installed

### Missing Items (Search Required)

⚠️ **Exim credentials NOT found on Desktop**  
   → Check: OneDrive, Windows Surface laptop, Google Drive  
   → Search for: `exim_credentials.json`, `.env` files with API keys

---

## Sync Execution Script

All commands combined into one executable script:

```bash
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
  echo "  Pharma data: $(ls -1 ~/.hermes/uploads/pharma_data/ | wc -l) files"
  echo "  Scripts: $(ls -1 ~/.hermes/scripts/mac_imports/ | wc -l) files"
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
```

**Save as:** `/Users/moosaali/Desktop/SYNC_TO_SERVER.sh`  
**Run with:** `bash /Users/moosaali/Desktop/SYNC_TO_SERVER.sh`

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total files scanned | 31,024 |
| Total size | 4,804.91 MB |
| Claude Code projects | 1 |
| Business data files | 8 |
| Scripts | 10,572 (mostly Deep-Live-Cam deps) |
| Files to sync | ~35 files (0.54 MB) |
| New CRM records | 0 (pending Excel parsing) |
| Brain/RAG ingestion | Pending (after sync) |

---

**✅ Audit complete.** Execute sync script above to unify Desktop with server.

**Report saved to:**  
- Local: `/Users/moosaali/Desktop/DESKTOP_AUDIT_REPORT.md`  
- Server copy: Sync manually with `scp -i ~/.ssh/ollama_server_key ~/Desktop/DESKTOP_AUDIT_REPORT.md hermes@91.98.94.195:~/obsidian-sync/Reports/`
