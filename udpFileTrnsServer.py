import socket

# Server settings
host = 'localhost'
port = 12345
buffer_size = 65535  # Max size for UDP

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))

print(f"UDP Server listening on {host}:{port}...")

# Receive filename
file_data, client_addr = server_socket.recvfrom(buffer_size)
filename = file_data.decode()
print(f"Receiving file: {filename} from {client_addr}")

# Open file to write in binary mode
with open("received_" + filename, 'wb') as f:
    while True:
        data, _ = server_socket.recvfrom(buffer_size)
        if data == b"EOF":
            print("File received successfully.")
            break
        f.write(data)

server_socket.close()
