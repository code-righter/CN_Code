import socket
import os

# Server settings
server_ip = '127.0.0.1'  # change this to the receiver's IP
server_port = 12345
buffer_size = 65535

# File to send (change file path as needed)
filename = input("Enter the name of the file to send (with extension): ")

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send filename first
client_socket.sendto(filename.encode(), (server_ip, server_port))

# Read and send file in chunks
with open(filename, 'rb') as f:
    while True:
        chunk = f.read(buffer_size)
        if not chunk:
            break
        client_socket.sendto(chunk, (server_ip, server_port))

# Send EOF to signal end of file
client_socket.sendto(b"EOF", (server_ip, server_port))
print(f"File {filename} sent successfully.")

client_socket.close()
