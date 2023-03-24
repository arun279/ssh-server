import argparse
import http.server
import logging
import os
import socket
import socketserver
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Simple HTTP server")
    parser.add_argument("-p", "--port", type=int, default=8000, help="port number")
    parser.add_argument("-d", "--directory", default="", help="directory to serve")
    return parser.parse_args()


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=None, **kwargs):
        if directory is None:
            directory = os.getcwd()
        self.directory = directory
        super().__init__(*args, directory=self.directory, **kwargs)

    def do_GET(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            index_path = os.path.join(path, "index.html")
            if os.path.exists(index_path):
                with open(index_path, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.send_header("Content-Length", len(content))
                self.end_headers()
                self.wfile.write(content)
                return
        super().do_GET()


def main():
    args = parse_args()
    logging.basicConfig(level=logging.INFO)
    try:
        with socketserver.TCPServer(("", args.port), CustomHandler) as httpd:
            logging.info(f"Serving at http://{socket.gethostname()}:{args.port}")
            logging.info(f"Shared folder: {os.path.abspath(args.directory)}")
            httpd.serve_forever()
    except OSError as e:
        logging.error(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
