import http.server
import socketserver
import os

PORT = 5500
DIRECTORY = "docs"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # 修正：針對常見的根目錄請求提供自動導向
        if self.path == '/' or self.path == '/index' or self.path == '/index.html':
            self.send_response(301)
            self.send_header('Location', '/index.md')
            self.end_headers()
            return
        return super().do_GET()

    def end_headers(self):
        # 徹底禁用快取，確保內容更新
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        # 強制指定 MIME 類型與編碼，避免瀏覽器無法解析或顯示亂碼
        # 對於 .md 檔案，我們暫時設定為 text/html 以便部分瀏覽器直接渲染文字
        if self.path.endswith(".md"):
            self.send_header('Content-Type', 'text/html; charset=utf-8')
        elif self.path.endswith(".scss") or self.path.endswith(".css"):
            self.send_header('Content-Type', 'text/css; charset=utf-8')
        super().end_headers()

if __name__ == "__main__":
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"服務啟動於 http://127.0.0.1:{PORT}")
        print(f"模式：直接渲染 Markdown 至 HTML 視圖")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n伺服器已停止。")
