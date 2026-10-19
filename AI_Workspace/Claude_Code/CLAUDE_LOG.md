# Claude Code Session Log
_Running log of what got done in each Claude Code session — newest entries at the top. I add one entry per session that does real work, including unfinished ones._

---

## 2026-09-14 — Local LLM / OmniRoute / Hermes router / Dify audit
**Status:** ongoing (this session)

- Fixed OpenCode's OpenCode-Ollama wiring (local + cloud models, brain/hermes memory attached)
- Diagnosed and fixed the Cloudflare Access + Ollama Host-header bug blocking OpenWebUI from reaching this Mac's local Ollama
- Wired OpenWebUI's memory ("brain") tool live
- Cleaned 9 dead entries out of the Hermes VPS router (SiliconFlow, direct NVIDIA) — 46 → 37 models, live-tested clean
- Cleaned 9 dead OAuth connections out of OmniRoute (48 → 39) — full before/after list kept in chat
- Found OmniRoute already has 6 working smart-routing tiers (tier0-frontier … tier5-glm-kimi) — verified live
- Fixed Hermes desktop's dead Gemini key by reusing a spare key already owned (via the VPS router)
- **Found Dify is currently down** (no container running, `hermes` user lacks docker permission to fully diagnose — needs Moosa's sudo)
- Found this `AI_Workspace` folder already existed (built 2026-09-12, unrecorded) as a skeleton with no automation — built the first real automation for it (Hermes session log, see `Hermes/HERMES_LOG.md`, hourly via launchd)

**Open:** Dify restart (needs sudo on the VPS), OpenWebUI/Dify chat history export into this workspace (needs a script run/scheduled server-side — same permission boundary as everything else touching the VPS this session).

Full detail in `~/.claude/memory/` (search for `ollama-relay-host-header-fix-20260914`, `opencode-ollama-cloud-wired-20260914`).
