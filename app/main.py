"""Small HTTP server for Docker port, bind mount, and volume exercises."""

import html
import os
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


CONTENT_FILE = Path(os.environ.get("CONTENT_FILE", "/app/content/message.txt"))
DATA_FILE = Path(os.environ.get("DATA_FILE", "/data/visits.txt"))
PORT = int(os.environ.get("PORT", "8000"))
counter_lock = threading.Lock()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = b"ok\n"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
        elif self.path == "/":
            with counter_lock:
                DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
                try:
                    visits = int(DATA_FILE.read_text(encoding="utf-8").strip())
                except (FileNotFoundError, ValueError):
                    visits = 0
                visits += 1
                DATA_FILE.write_text(f"{visits}\n", encoding="utf-8")
            message = html.escape(CONTENT_FILE.read_text(encoding="utf-8").strip())
            body = (
                "<!doctype html><html lang=\"ko\"><meta charset=\"utf-8\">"
                "<title>Mission Workstation</title>"
                f"<h1>{message}</h1><p>Visits: {visits}</p></html>\n"
            ).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
        else:
            self.send_error(404)
            return
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print(f"Serving on port {PORT}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
