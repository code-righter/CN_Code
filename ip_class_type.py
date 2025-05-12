import ipaddress

def detect_ip_version(ip):
    """Detect if the IP address is IPv4 or IPv6."""
    try:
        ip_obj = ipaddress.ip_address(ip)
        if isinstance(ip_obj, ipaddress.IPv4Address):
            return "IPv4"
        elif isinstance(ip_obj, ipaddress.IPv6Address):
            return "IPv6"
    except ValueError:
        return "Invalid"

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

def is_private_ip(ip):
    """Check if an IPv4 address is private."""
    octets = list(map(int, ip.split('.')))
    if octets[0] == 10:
        return True
    elif octets[0] == 172 and 16 <= octets[1] <= 31:
        return True
    elif octets[0] == 192 and octets[1] == 168:
        return True
    else:
        return False

# --- Main Program ---
if __name__ == "__main__":

    ip_input = input("Enter an IP address: ").strip()
    ip_version = detect_ip_version(ip_input)

    if ip_version == "Invalid":
        print("Invalid IP address format.")
    elif ip_version == "IPv6":
        print(f"\nIP Address : {ip_input}")
        print("Version    : IPv6")
        print("Class      : Not applicable")
        print("Type       : Not applicable")
    else:
        ip_class = get_ip_class(ip_input)
        ip_type = "Private" if is_private_ip(ip_input) else "Public"
        print(f"\nIP Address : {ip_input}")
        print("Version    :", ip_version)
        print("Class      :", ip_class)
        print("Type       :", ip_type)
