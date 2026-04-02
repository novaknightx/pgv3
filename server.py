#!/usr/bin/env python3
"""
PhishGuard — Local Dev Server
Run: python server.py
Then open: http://localhost:8080
"""
import http.server, socketserver, webbrowser, os, threading

PORT = 8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"  [{self.address_string()}] {format % args}")

def open_browser():
    import time; time.sleep(0.8)
    webbrowser.open(f"http://localhost:{PORT}")

print(f"\n🛡️  PhishGuard Server")
print(f"   Running at  →  http://localhost:{PORT}")
print(f"   Press Ctrl+C to stop\n")

threading.Thread(target=open_browser, daemon=True).start()
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n  Server stopped. Goodbye!\n")
