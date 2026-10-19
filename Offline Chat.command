#!/bin/zsh
# Offline Chat (2026-10-12): local Gemma 12B + Ponytail, works with no internet. Answers in ~25 s.
# Replaces Local Mode.command - its Hermes-offline options took 400+ s to answer, so only the fast chat was kept.
# For anything that needs memory, tools or the brain, use Hermes (cloud) instead.
exec /usr/local/bin/ollama run gemma4-12b-ponytail --think=false
