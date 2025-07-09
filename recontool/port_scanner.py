import socket
import concurrent.futures

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389]

# Escanea los puertos más comunes.
def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        return port
    except: 
        return None
    finally:
        sock.close()
    

def scan_ports(ip):
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(lambda p: scan_port(ip, p), COMMON_PORTS)
        for port in results:
            if port:
                open_ports.append(port)
    return open_ports