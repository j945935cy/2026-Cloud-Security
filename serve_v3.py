import http.server
import socketserver
import os

PORT = 5500
DIRECTORY = "docs"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # 如果請求的是根目錄，自動導向到 /index.md
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.md')
            self.end_headers()
            return
        return super().do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        # 強制瀏覽器使用 UTF-8 編碼
        if self.path.endswith(".md") or self.path.endswith(".html"):
            self.send_header('Content-Type', 'text/html; charset=utf-8')
        super().end_headers()

if __name__ == "__main__":
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    
    # 允許地址重用，避免 10048 錯誤
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"服務啟動於 http://127.0.0.1:{PORT}")
        print(f"首頁已設定自動引導至 index.md")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n伺服器已停止。")
