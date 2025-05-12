import socket
import time

# Config
HOST = 'localhost'
PORT = 9999
WINDOW_SIZE = 4
TOTAL_FRAMES = 8

# Setup socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

base = 0
while base < TOTAL_FRAMES:
    # Send frames in the window
    for i in range(base, min(base + WINDOW_SIZE, TOTAL_FRAMES)):
        print(f"Sender: Sending Frame {i}")
        s.send(str(i).encode())
        time.sleep(0.2)

    try:
        ack = int(s.recv(1024).decode())
        print(f"Sender: Received ACK for Frame {ack}")
        
        if ack >= base:
            base = ack + 1  # Move window forward
        else:
            print(f"Sender: Duplicate ACK for Frame {ack}, resending from Frame {ack + 1}")
            # Reset will happen in next loop
    except:
        print("Sender: No ACK received, assuming timeout")
        # Simulate timeout behavior (resend from base)

s.send(b'DONE')
s.close()
