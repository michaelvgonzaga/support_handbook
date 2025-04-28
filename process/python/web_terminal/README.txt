
AFTER CHANGES:
- Save web_terminal.py.
- source ~/webterminal-env/bin/activate
- python3 web_terminal.py
- reload localhost:8080/terminal.html in web browser.

FLOW:
- Start WebSocket server (backend) → python3 web_terminal.py
- Start HTTP server (frontend) → python3 -m http.server 8080
- Open browser → http://localhost:8080/terminal.html
- Browser connects via WebSocket to localhost:9001
- Type in browser → send/receive commands to your real shell!