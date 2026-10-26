# [Everrett Nguyen] - Assignment 2

def evaluate_packet(port, packet_size_bytes):
    # TODO: Write your if / elif / else logic below and return the matching string
    if port == 80 or port == 443:
        return "STANDARD_WEB_TRAFFIC"
    elif packet_size_bytes > 1500:
        return "SUSPICIOUS_LARGE_PACKET"
    elif packet_size_bytes < 64:
        return "SUSPICIOUS_SMALL_PACKET"
    else:
        return "NORMAL_INTERNAL_TRAFFIC"
    pass