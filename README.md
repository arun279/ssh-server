# Simple SSH HTTP Server with Download Folder

This is a simple HTTP server that serves files from a directory and provides a download link for the entire directory as a ZIP archive.

## Usage

To use this server, run the `server.py` file with the following optional arguments:

- `-p`, `--port`: specify the port number to use (default is 8000)
- `-d`, `--directory`: specify the directory to serve (default is the current working directory)

Once the server is running, you can access it in your web browser by navigating to `http://localhost:port`, where `port` is the port number you specified (or the default 8000). You should see a web page displaying the contents of the directory being served. To download the entire directory as a ZIP archive, click the "Download Folder" button.

## Files

- `server.py`: Python script that starts the HTTP server and handles requests
- `index.html`: HTML file that displays the contents of the directory and provides a download link

## Example

Suppose you have a directory called `my_folder` with some files and subdirectories that you want to serve. To start the server and serve this directory on port 8080, you can run:

```
python server.py -p 8080 -d my_folder
```


Then, you can access the contents of `my_folder` in your web browser at `http://localhost:8080`, and download the entire folder as a ZIP archive by clicking the "Download Folder" button.

Note that the `index.html` file must be present in the directory being served, otherwise the server will not work properly.
