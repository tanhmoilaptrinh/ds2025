import socket

HOST = "127.0.0.1"   
PORT = 8888

def main():
    print("[CLIENT] Creating socket...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"[CLIENT] Connecting to server at {HOST}:{PORT} ...")
    sock.connect((HOST, PORT))
    print("[CLIENT] Connected!")

    while True:
        msg = input("[CLIENT] Nhập message (gõ 'quit' để thoát): ")

        print(f"[CLIENT] Sending: {msg!r}")
        sock.sendall(msg.encode("utf-8"))

        if msg.strip().lower() == "quit":
            print("[CLIENT] Asked to quit, không chờ server nữa")
            break

        print("[CLIENT] Waiting for reply from server...")
        data = sock.recv(1024)
        if not data:
            print("[CLIENT] Server closed the connection")
            break

        print(f"[CLIENT] Received from server: {data.decode('utf-8')!r}")

    print("[CLIENT] Closing client socket (sock.close())")
    sock.close()

if __name__ == "__main__":
    main()
