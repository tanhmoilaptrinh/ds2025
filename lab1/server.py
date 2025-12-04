import socket

PORT = 8888
HOST = '127.0.0.1'
BUFFER_SIZE = 1024

def handle_client(connection, addr):
    print(f"New connection from {addr}")
    connection.close()

def main():
    
    print("Creating socket...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print(f"Binding to {HOST}:{PORT} ...")
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}")
    connection, addr = server_socket.accept()

    while True:
        print("Waiting to receive data from client...")
        data = connection.recv(BUFFER_SIZE)

        if not data:
            print("No data received. Closing connection.")
            break
        

        text = data.decode('utf-8')
        print(f"Received data:{text}")

        if text.strip().lower() == 'quit':
            print('close connection')
            break

        reply = f"Server got: {text}"
        print(f"[SERVER] Sending back: {reply!r}")
        connection.sendall(reply.encode("utf-8"))

    print("Closing client socket...")
    connection.close()    

    # print("[SERVER] Closing server listening socket")
    # server_socket.close()
if __name__ == "__main__":
    main()


s