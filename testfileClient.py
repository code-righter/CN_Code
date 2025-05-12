import socket

ADR = "localhost"
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# import connecting a socket
client_socket.connect((ADR, PORT))
print(f"Connected to the server at {ADR}: {PORT}")

# sending message to the server
message = "Hello from client!!"
client_socket.send(message.encode())

# getting reply from server
reply = client_socket.recv(1024).decode()
print(f"Server says: {reply}")

client_socket.close()



