# rpc_client.py
from xmlrpc.client import ServerProxy, Binary
import os

HOST = "127.0.0.1"
PORT = 8888

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLIENT_FILES_DIR = os.path.join(BASE_DIR, "files", "client_files")

os.makedirs(CLIENT_FILES_DIR, exist_ok=True)

def list_remote_files(server):
    files = server.list_files()
    if not files:
        print("[CLIENT] No files available on server.")
        return
    print("[CLIENT] Files on server:")
    for i, name in enumerate(files, start=1):
        print(f"  {i}. {name}")

def download_remote_file(server, filename):
    print(f"[CLIENT] Requesting file '{filename}' from server...")
    data = server.download_file(filename)

    if data is None:
        print("[CLIENT] Server reports file not found.")
        return

    # data is xmlrpc.client.Binary
    content = data.data
    local_path = os.path.join(CLIENT_FILES_DIR, filename)

    with open(local_path, "wb") as f:
        f.write(content)

    print(f"[CLIENT] File saved to: {local_path} ({len(content)} bytes)")

def main():
    url = f"http://{HOST}:{PORT}"
    print(f"[CLIENT] Connecting to XML-RPC server at {url} ...")
    server = ServerProxy(url, allow_none=True)
    print("[CLIENT] Connected!")

    while True:
        print("\n=== RPC File Transfer Menu ===")
        print("1. List files on server")
        print("2. Download file from server")
        print("3. Quit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            list_remote_files(server)

        elif choice == "2":
            filename = input("Enter filename to download: ").strip()
            if filename:
                download_remote_file(server, filename)

        elif choice == "3":
            print("[CLIENT] Bye!")
            break

        else:
            print("[CLIENT] Invalid choice, try again.")

if __name__ == "__main__":
    main()
