"""
LEVEL 1: Single Port Check
---------------------------
The simplest possible version. No loops, no threading, no CLI args.
Just: "is this ONE port on this ONE host open?"
 
Concept introduced: raw TCP sockets and connect_ex()
 
WHY connect_ex() instead of connect()?
- connect() raises an exception on failure (e.g. ConnectionRefusedError),
  which means you'd need a try/except just to check one port.
- connect_ex() instead returns an integer error code. 0 means success
  (port is open). Anything else means it failed. This is much cleaner
  when you're about to do this thousands of times (later levels).
"""

import socket

HOST = "scanme.nmap.org"  # Target host
PORT = 22  # Target port (SSH - safe to test against)

def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """Timeout is a float, if not specified, use 1.0 seconds"""

    # AF_INET = IPv4 address family, SOCK_STREAM = TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout) # So it doesn't hang forever on filtered/dead port

    try:
        result = sock.connect_ex((host, port))
        return result == 0
    finally:
        # Always close socket, even if something went wrong above
        sock.close()

if __name__ == "__main__":
    is_open = scan_port(HOST, PORT)
    state = "OPEN" if is_open else "CLOSED_FILTERED"
    print(f"{HOST}:{PORT} -> {state}")
