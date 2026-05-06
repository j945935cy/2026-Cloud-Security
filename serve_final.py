import http.server
import socketserver
import os
import urllib.parse

PORT = 5500
DIRECTORY = "docs"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2026 資安大轉折 - 本地預覽</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; color: #333; }
        a { color: #0366d6; text-decoration: none; }
        a:hover { text-decoration: underline; }
        pre { background: #f6f8fa; padding: 16px; border-radius: 3px; overflow: auto; }
        code { font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace; background: #f6f8fa; padding: 0.2em 0.4em; border-radius: 3px; }
        blockquote { border-left: 0.25em solid #dfe2e5; color: #6a737d; padding: 0 1em; margin: 0; }
        img { max-width: 100%; }
        /* Preserve some HTML styling for index.md */
        .hero { text-align: center; padding: 40px 0; }
        .hero h1 { font-size: 2.5em; margin-bottom: 10px; }
        .hero-actions a { display: inline-block; padding: 10px 20px; margin: 10px; border-radius: 5px; background: #0366d6; color: white; }
        .hero-actions a.button-secondary { background: #6a737d; }
    </style>
</head>
<body>
    <div id="content"></div>
    <textarea id="markdown-source" style="display:none;">{markdown_content}</textarea>
    <script>
        document.getElementById('content').innerHTML = marked.parse(
            document.getElementById('markdown-source').value
        );
    </script>
</body>
</html>
"""

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # 自動導向根目錄與常見首頁路徑到 index.md
        if self.path == '/' or self.path == '/index' or self.path == '/index.html':
            self.send_response(301)
            self.send_header('Location', '/index.md')
            self.end_headers()
            return
            
        parsed_path = urllib.parse.unquote(self.path.lstrip('/'))
        file_path = os.path.join(DIRECTORY, parsed_path)
        
        # 處理 .html 請求，若本地沒有 .html 則 fallback 到 .md
        if parsed_path.endswith(".html") and not os.path.exists(file_path):
            fallback_path = file_path[:-5] + ".md"
            if os.path.exists(fallback_path):
                file_path = fallback_path
                parsed_path = parsed_path[:-5] + ".md"

        # 若為 .md 檔案，透過 marked.js 渲染 HTML 以確保連結可點擊
        if file_path.endswith(".md") and os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 簡易移除 YAML frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    content = parts[2]
            
            # 處理 textarea 的結束標籤避免跳脫問題
            safe_content = content.replace('</textarea>', '&lt;/textarea&gt;')
            html = HTML_TEMPLATE.replace('{markdown_content}', safe_content)
            
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
            return

        return super().do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        if self.path.endswith(".scss") or self.path.endswith(".css"):
            self.send_header('Content-Type', 'text/css; charset=utf-8')
        super().end_headers()

if __name__ == "__main__":
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"服務啟動於 http://127.0.0.1:{PORT}")
        print(f"模式：直接渲染 Markdown 至 HTML 視圖，並支援 .html fallback")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n伺服器已停止。")
