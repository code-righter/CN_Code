

def get_frame():
    fs = int(input("Enter Frame size: "))
    frame = []
    print("Enter Frame bits:")
    for _ in range(fs):
        bit = int(input())
        frame.append(bit)
    return frame

def get_generator():
    gs = int(input("Enter Generator size: "))
    generator = []
    print("Enter Generator bits:")
    for _ in range(gs):
        bit = int(input())
        generator.append(bit)
    return generator

def display_data(message, data):
    print(f"{message}: ", end="")
    for bit in data:
        print(bit, end="")
    print()

def append_zeros_to_frame(frame, num_zeros):
    return frame + [0] * num_zeros

def perform_division(dividend, divisor):
    dividend = dividend[:]
    divisor_size = len(divisor)
    for i in range(len(dividend) - divisor_size + 1):
        if dividend[i] == 1:
            for j in range(divisor_size):
                dividend[i + j] ^= divisor[j]
    remainder = dividend[-(divisor_size - 1):]
    return remainder

def generate_transmitted_frame(frame, crc):
    return frame + crc

def check_error(remainder):
    return any(bit != 0 for bit in remainder)

def main():
    print("----- Sender Side -----")
    frame = get_frame()
    generator = get_generator()

    display_data("Input Frame", frame)
    display_data("Generator", generator)

    remainder_size = len(generator) - 1
    print(f"Number of 0's to be appended: {remainder_size}")

    augmented_frame = append_zeros_to_frame(frame, remainder_size)
    display_data("Augmented Frame", augmented_frame)

    crc = perform_division(augmented_frame, generator)
    display_data("CRC", crc)

    transmitted_frame = generate_transmitted_frame(frame, crc)
    display_data("Transmitted Frame", transmitted_frame)

    print("\n----- Receiver Side -----")
    received_frame = transmitted_frame  # Simulate same frame (no error)
    display_data("Received Frame", received_frame)

    receiver_remainder = perform_division(received_frame, generator)
    display_data("Remainder after division", receiver_remainder)

    if not check_error(receiver_remainder):
        print(" No error detected: Message received correctly.")
    else:
        print(" Error detected: Message is corrupted.")

if __name__ == "__main__":
    main()
