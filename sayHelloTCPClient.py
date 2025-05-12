import socket  # Import the socket module for network communication

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define server address and port (must match server)
host = 'localhost'
port = 12345

# Connect to the server
client_socket.connect((host, port))
print(f"Connected to server at {host}:{port}")

# Send a message to the server
message = "Hello from Client!"
client_socket.send(message.encode())

# Receive a response from the server
reply = client_socket.recv(1024).decode()
print("Server says:", reply)

# Close the socket
client_socket.close()
