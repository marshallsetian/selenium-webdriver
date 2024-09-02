from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Path ke WebDriver (sesuaikan dengan lokasi WebDriver Anda)
driver_path = '/home/eng/Downloads/chromedriver-linux64/chromedriver'

# Menentukan layanan dan membuat instance WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Membuka halaman Google
    driver.get("https://www.google.com")
    
    # Menunggu agar halaman sepenuhnya dimuat
    time.sleep(2)

    # Mencari elemen input pencarian dan mengetikkan kueri
    search_box = driver.find_element("name", "q")
    search_box.send_keys("Selenium WebDriver")
    search_box.send_keys(Keys.RETURN)
    
    # Menunggu beberapa detik untuk melihat hasilnya
    time.sleep(3)
    
finally:
    # Menutup browser
    driver.quit()
