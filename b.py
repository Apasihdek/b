from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import time

print("=== Headless Browser (VPS Mode) ===")

# ===== Input User =====
url = input("Masukkan URL (contoh https://example.com): ")
jumlah_request = int(input("Jumlah request: "))
delay = float(input("Jeda antar request (detik): "))

# ===== Setup Chrome Options =====
options = Options()
options.add_argument("--headless=new")          # Mode tanpa GUI
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

# Tambahan supaya lebih stabil di VPS
options.add_argument("--disable-blink-features=AutomationControlled")

try:
    driver = webdriver.Chrome(options=options)

    print("\n=== Mulai Request ===\n")

    for i in range(jumlah_request):
        try:
            start = time.time()

            driver.get(url)

            time.sleep(3)  # beri waktu JS load

            end = time.time()

            print(f"[{i+1}]")
            print("Title:", driver.title)
            print("Final URL:", driver.current_url)
            print("Waktu:", round(end - start, 4), "detik")
            print("-" * 40)

        except Exception as e:
            print(f"[{i+1}] Error:", e)

        time.sleep(delay)

    driver.quit()
    print("\nSelesai.")

except WebDriverException as e:
    print("Gagal menjalankan ChromeDriver.")
    print("Pastikan Chrome & Chromedriver terinstall.")
    print("Detail error:", e)
