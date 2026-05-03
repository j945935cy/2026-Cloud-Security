import http.server
import socketserver
import os

PORT = 5500
DIRECTORY = "docs"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # 強制指定頁面編碼為 UTF-8
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        super().end_headers()

    def do_GET(self):
        # 如果請求的是 .md 檔案，也給予正確的 Content-Type
        if self.path.endswith('.md'):
            super().do_GET()
        else:
            super().do_GET()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()
