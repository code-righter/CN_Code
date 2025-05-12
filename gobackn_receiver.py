import socket
import random

# Config
HOST = 'localhost'
PORT = 9999

# Setup socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print(f"Receiver: Connected by {addr}")

expected_frame = 0

while True:
    data = conn.recv(1024).decode()
    if data == 'DONE':
        print("Receiver: All frames received.")
        break

    frame = int(data)

    # Randomly simulate dropping frames
    drop = random.choice([False, False, True])  # ~33% chance to drop

    if drop:
        print(f"Receiver: Dropped Frame {frame}")
        # Resend ACK for last correct frame
        conn.send(str(expected_frame - 1).encode() if expected_frame > 0 else b'0')
        continue

    if frame == expected_frame:
        print(f"Receiver: Received Frame {frame}")
        conn.send(str(frame).encode())
        expected_frame += 1
    else:
        print(f"Receiver: Out of order Frame {frame}, expecting Frame {expected_frame}")
        conn.send(str(expected_frame - 1).encode())

conn.close()
s.close()
