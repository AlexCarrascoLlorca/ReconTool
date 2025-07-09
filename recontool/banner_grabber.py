import socket

# Intenta obtener el banner del puerto.
def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner.decode().strip()
    except:
        return "No banner"
    finally:
        s.close()