import socket

ADR = "localhost"
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((ADR, PORT))
print(f"Server has been started at {ADR}: {PORT}")

server_socket.listen(1)
print("Server listening...")

client_socket, client_addr = server_socket.accept()
print(f"Connected to Client at {client_addr}")

message = client_socket.recv(1024).decode()
print("Client says : ", message)

reply = "Hello from server!!"
client_socket.send(reply.encode())

client_socket.close()
server_socket.close()
