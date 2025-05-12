import socket
import os

def main():
    host = '0.0.0.0'   # Accept from any address
    port = 5001

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server is listening on port", port)

    conn, addr = server_socket.accept()
    print("Connection from:", addr)

    filename = conn.recv(1024).decode()
    print("Client requested file:", filename)

    if os.path.exists(filename):
        conn.send("FOUND".encode())
        with open(filename, 'rb') as f:
            data = f.read(1024)
            while data:
                conn.send(data)
                data = f.read(1024)
        print("File sent successfully.")
    else:
        conn.send("NOTFOUND".encode())
        print("Requested file not found.")

    conn.close()

if __name__ == '__main__':
    main()
