import http.server
import socketserver
import socket
import os

PORT = 8000
DIRECTORY = ""

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(os.path.join(path, "index.html"), "rb") as file:
                self.copyfile(file, self.wfile)
        else:
            super().do_GET()

Handler = CustomHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Serving at http://{socket.gethostname()}:{PORT}")
print(f"Shared folder: {DIRECTORY}")

httpd.serve_forever()
