#!/usr/bin/env python3
"""
ADOV Care Group - Executive Management Portal Local Web Server
Serves the password-protected internal management portal on localhost.
"""

import os
import sys
import socketserver
import http.server

PORT = 8080
DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "portal")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Cache control for fresh internal dashboard data
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run_server():
    port = PORT
    for attempt in range(5):
        try:
            with socketserver.TCPServer(("", port), Handler) as httpd:
                print("==================================================================")
                print("  ADOV CARE GROUP - INTERNAL EXECUTIVE MANAGEMENT PORTAL")
                print("  CONFIDENTIAL & PASSWORD PROTECTED // INTERNAL MANAGEMENT USE")
                print("==================================================================")
                print(f"  Portal URL:       http://localhost:{port}")
                print(f"  Access PIN:       adov2026")
                print(f"  Serving Dir:      {DIRECTORY}")
                print("==================================================================")
                print("  Press Ctrl+C to terminate the local server.\n")
                httpd.serve_forever()
                break
        except OSError as e:
            if "Address already in use" in str(e):
                port += 1
            else:
                raise e

if __name__ == "__main__":
    run_server()
