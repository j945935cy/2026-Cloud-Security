import http.server
import socketserver
import os

PORT = 5500
DIRECTORY = "docs"

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # 徹底禁用快取，確保前端 SPA 取得最新檔案
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        
        # 確保 CSS 檔案能正確載入
        if self.path.endswith(".css"):
            self.send_header('Content-Type', 'text/css; charset=utf-8')
        elif self.path.endswith(".js"):
            self.send_header('Content-Type', 'application/javascript; charset=utf-8')
            
        super().end_headers()

if __name__ == "__main__":
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), NoCacheHTTPRequestHandler) as httpd:
        print(f"服務啟動於 http://127.0.0.1:{PORT}")
        print(f"模式：靜態檔案伺服器 (SPA 架構)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n伺服器已停止。")
