#!/bin/zsh
# Double-click to chat with Gemma 4 12B on this Mac. Works with no internet. Type your question and press Enter; type /bye to quit.
clear
echo "Gemma 12B - offline, on this Mac. The first answer takes about 20 s while it loads. Type /bye to quit."
echo
exec "/usr/local/bin/ollama" run gemma4-12b-biz --think=false
