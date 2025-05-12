import socket  # Import the socket module for network communication

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define server address and port
host = 'localhost'  # Server runs on local machine
port = 12345        # Arbitrary non-privileged port

# Bind the socket to the address and port
server_socket.bind((host, port))
print(f"Server is running on {host}:{port}")

# Listen for incoming connections (1 client at a time)
server_socket.listen(1)
print("Waiting for a client to connect...")

# Accept the connection from the client
client_socket, client_address = server_socket.accept()
print(f"Connected to client at {client_address}")

# Receive data from the client (max 1024 bytes)
message = client_socket.recv(1024).decode()
print("Client says:", message)

# Send a response back to the client
reply = "Hello from Server!"
client_socket.send(reply.encode())

# Close sockets
client_socket.close()
server_socket.close()
