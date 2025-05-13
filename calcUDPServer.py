import socket

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

def start_server(host='localhost', port=5000):
    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind socket to address
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Listening on {host}:{port}...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == "exit":
            print("[SERVER] Client disconnected.")
            break

        print(f"[SERVER] Received expression: {data}")
        result = evaluate_expression(data)
        conn.send(result.encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
