# Simple SSH File Server

This is a simple file server implemented in Python using the `http.server` and `socketserver` modules. It allows you to serve the contents of a directory over HTTP and provides a download link to download the entire directory as a ZIP archive.

## Usage

1. Place the files you want to serve in a directory on your computer.
2. Modify the `DIRECTORY` variable in `server.py` to the path of the directory you want to serve.
3. Run `server.py` in a terminal or command prompt.
4. Open a web browser and navigate to `http://localhost:8000`.
5. You should see a directory listing of the files in the directory you are serving. If you have an `index.html` file in the directory, it will be served instead of the directory listing.
6. To download the entire directory as a ZIP archive, click the "Download Folder" link on the web page.

That's it! You now have a simple file server running on your computer. You can stop the server by pressing `Ctrl + C` in the terminal or command prompt where it is running.
