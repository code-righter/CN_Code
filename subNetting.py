import ipaddress

def parse_ip(ip_str):
    """Parses an IP address string into a list of integer octets."""
    return [int(part) for part in ip_str.split('.')]

def calculate_subnet_mask(prefix):
    """Calculates the subnet mask from a given prefix.
    """
    if not 0 <= prefix <= 32:
        raise ValueError("Prefix must be between 0 and 32")

    # Calculate the integer representation of the mask
    mask_int = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF

    # Extract the four octets from the integer mask
    octet1 = (mask_int >> 24) & 0xFF
    octet2 = (mask_int >> 16) & 0xFF
    octet3 = (mask_int >> 8) & 0xFF
    octet4 = mask_int & 0xFF

    # Format the octets into a dotted-decimal string
    subnet_mask_str = f"{octet1}.{octet2}.{octet3}.{octet4}"
    return subnet_mask_str


def calculate_broadcast_address(ip_parts, prefix):
    """Calculates the broadcast address from IP parts and prefix."""
    ip_int = (ip_parts[0] << 24) + (ip_parts[1] << 16) + (ip_parts[2] << 8) + ip_parts[3]
    mask = 0xFFFFFFFF << (32 - prefix)
    inverted_mask = ~mask & 0xFFFFFFFF  # Ensure it's 32-bit
    broadcast_int = ip_int | inverted_mask
    octet1 = (broadcast_int >> 24) & 0xFF
    octet2 = (broadcast_int >> 16) & 0xFF
    octet3 = (broadcast_int >> 8) & 0xFF
    octet4 = broadcast_int & 0xFF
    return f"{octet1}.{octet2}.{octet3}.{octet4}"

def get_ip_class(ip):
    """Return the class of an IPv4 address based on the first octet."""
    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 126:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    elif 224 <= first_octet <= 239:
        return 'D (Multicast)'
    elif 240 <= first_octet <= 255:
        return 'E (Experimental)'
    else:
        return 'Unknown'


def main():
    ip_address_str = input("Enter IP address : ")
    subnet_prefix = int(input("Enter subnet prefix : "))

    ip_parts = parse_ip(ip_address_str)
    ip_class = get_ip_class(ip_address_str)
    subnet_mask = calculate_subnet_mask(subnet_prefix)
    broadcast_address = calculate_broadcast_address(ip_parts, subnet_prefix)
    total_usable_hosts = (1 << (32 - subnet_prefix)) - 2 if (32 - subnet_prefix) > 1 else 0


    print(f"IP Class: {ip_class}")
    print(f"Subnet Mask: {subnet_mask}")
    print(f"Broadcast Address: {broadcast_address}")
    print(f"Total Usable Hosts: {total_usable_hosts}")

if __name__ == "__main__":
    main()

    