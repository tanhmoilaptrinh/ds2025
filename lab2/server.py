# rpc_server.py
from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from xmlrpc.client import Binary
import os

HOST = "127.0.0.1"
PORT = 8888

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVER_FILES_DIR = os.path.join(BASE_DIR, "files", "server_files")

os.makedirs(SERVER_FILES_DIR, exist_ok=True)

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)

def list_files():
    """Return list of filenames available on the server."""
    return os.listdir(SERVER_FILES_DIR)

def download_file(filename):
    """
    Return file content as xmlrpc.client.Binary.
    If file does not exist, return None.
    """
    path = os.path.join(SERVER_FILES_DIR, filename)

    if not os.path.isfile(path):
        print(f"[SERVER] File not found: {filename}")
        return None

    with open(path, "rb") as f:
        data = f.read()
    print(f"[SERVER] Sending file: {filename} ({len(data)} bytes)")
    return Binary(data)

def main():
    print(f"[SERVER] Starting XML-RPC server at {HOST}:{PORT}")
    with SimpleXMLRPCServer((HOST, PORT),
                            requestHandler=RequestHandler,
                            allow_none=True) as server:
        server.register_introspection_functions()

        server.register_function(list_files, "list_files")
        server.register_function(download_file, "download_file")

        print("[SERVER] Available methods: list_files, download_file")
        print("[SERVER] Waiting for RPC calls...")
        server.serve_forever()

if __name__ == "__main__":
    main()
