import random
import time

# Function to get total number of packets and window size
def get_parameters():
    total_packets = int(input("Enter total number of packets to send: "))
    window_size = int(input("Enter sliding window size: "))
    return total_packets, window_size

# Function to simulate sending packets with Selective Repeat
def sender(total_packets, window_size):
    base = 0
    next_seq = 0
    acked = [False] * total_packets
    receiver_buffer = [None] * total_packets

    print("\n--- Sender starts sending packets ---\n")

    while base < total_packets:
        # Send packets in window
        while next_seq < base + window_size and next_seq < total_packets:
            print(f"Sender: Sending packet {next_seq}")
            if random.random() < 0.8:  # 80% chance of successful delivery
                receiver_buffer[next_seq] = f"Packet-{next_seq}"
                print(f"Receiver: Received packet {next_seq}")
            else:
                print(f"Receiver: Packet {next_seq} LOST")
            next_seq += 1

        # Simulate ACKs
        for i in range(base, next_seq):
            if receiver_buffer[i] is not None and not acked[i]:
                print(f"Sender: ACK received for packet {i}")
                acked[i] = True

        # Slide window
        while base < total_packets and acked[base]:
            base += 1

        # Retransmit unACKed packets in window
        for i in range(base, min(base + window_size, total_packets)):
            if not acked[i]:
                print(f"Sender: Retransmitting packet {i}")
                if random.random() < 0.9:
                    receiver_buffer[i] = f"Packet-{i}"
                    print(f"Receiver: Received retransmitted packet {i}")
                    acked[i] = True
                else:
                    print(f"Receiver: Retransmitted packet {i} LOST again")

        print(f"\nSliding Window: base={base}, next_seq={next_seq}\n")
        time.sleep(1)

    print("\n--- All packets successfully sent and acknowledged ---")

# Main function
def main():
    total_packets, window_size = get_parameters()
    sender(total_packets, window_size)

if __name__ == "__main__":
    main()
