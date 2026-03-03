from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

url = input("Masukkan URL: ")
driver.get(url)

time.sleep(5)

print("Title:", driver.title)
print("Final URL:", driver.current_url)

html = driver.page_source
print("\nPreview HTML (500 karakter pertama):\n")
print(html[:500])

driver.quit()
