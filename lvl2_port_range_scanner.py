"""
LEVEL 2: Port Range Scan (Sequential)
--------------------------------------
Now scanning a RANGE of ports instead of just one. Still no threading -
each port is checked one after another, in order.
 
Concepts introduced:
  - looping over a range of ports
  - timing the scan with `time` (so you can SEE how slow this is,
    which is the whole motivation for threading in Level 4+)
  - collecting results in a list instead of just printing immediately
 
Scanning 1-1000 on scanme.nmap.org 
"""

import socket, time

HOST = "scanme.nmap.org"  # Target host
START_PORT = 1
END_PORT = 1000
TIMEOUT = 0.5 # Lower since scanning many ports

def scan_ports(host: str, port: int, timeout: float) -> bool:

    # AF_INET = IPv4 address family, SOCK_STREAM = TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        return sock.connect_ex((host, port)) == 0 # Try connection, return True if 0, else False (0 is success)
    finally:
        sock.close()

def scan_range(host: str, start: int, end: int, timeout: float) -> list[int]:
    open_ports = []
    for port in range(start, end + 1): 
        if scan_ports(host, port, timeout):
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)
    return open_ports

if __name__ == "__main__":
    print(f"SCANNING {HOST} PORTS FROM {START_PORT} TO {END_PORT} SEQUENTIALLY \n")

    start_time = time.time()
    results = scan_range(HOST, START_PORT, END_PORT, TIMEOUT)
    elapsed_time = time.time() - start_time

    print(f"SCAN COMPLETE. {len(results)} open port(s) found: {results}")
    print(f"Time taken: {elapsed_time:.2f} seconds") # Took ~199.97 seconds - ~ 2m20s