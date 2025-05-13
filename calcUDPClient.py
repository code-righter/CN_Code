import socket

def start_client(server_host='localhost', server_port=5000):
    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to server
    client_socket.connect((server_host, server_port))
    print(f"Connected to server at {server_host}:{server_port}")

    print("Enter expressions or 'exit' to quit.")
    while True:
        expression = input(">> ")

        client_socket.send(expression.encode())

        if expression.lower() == "exit":
            break

        result = client_socket.recv(1024).decode()
        print(f"[CLIENT] Server Response: {result}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
