import socket
import threading
import sys

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass

target = sys.argv[1]
port_range = sys.argv[3].split("-")
start_port = int(port_range[0])
end_port = int(port_range[1])

print(f"Scanning {target}...")

threads = []
for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(target, port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Scan Finished")
