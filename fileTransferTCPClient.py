import socket

def main():
    host = 'localhost'
    port = 5001

    client_socket = socket.socket()
    client_socket.connect((host, port))

    filename = input("Enter filename to request: ")
    client_socket.send(filename.encode())

    status = client_socket.recv(1024).decode()
    if status == "FOUND":
        with open("received_" + filename, 'wb') as f:
            data = client_socket.recv(1024)
            while data:
                f.write(data)
                data = client_socket.recv(1024)
        print("File received and saved as 'received_" + filename + "'")
    else:
        print("File not found on server.")

    client_socket.close()

if __name__ == '__main__':
    main()
