import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import os



# download chrome driver file
service = Service("E:/selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# our domian name
driver.get("https://www.selfinstaller.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//a[@href='https://docs.selfinstaller.com/']").click()
time.sleep(3)
driver.back()
driver.find_element(By.XPATH, "//a[@href='/pricing']").click()
time.sleep(2)
driver.back()
driver.find_element(By.XPATH, "//a[@href='/contact-us']").click()
# driver.find_element(By.NAME, "name").send_keys("testname")
# driver.find_element(By.NAME, "email").send_keys("acv@gmail.com")
# driver.find_element(By.ID, "message").send_keys("Hi there how u doing???")
driver.find_element(By.XPATH, "//button[text()='Send']").click()
time.sleep(3)
driver.back()
driver.find_element(By.XPATH, "//a[@href='/tos']").click()
time.sleep(3)
driver.back()
driver.find_element(By.XPATH, "//a[@href='/privacy-policy']").click()
time.sleep(3)
driver.back()

cookies = driver.get_cookies()
print("cookies",cookies)
for cookiee in cookies:
    print(cookiee.values())
driver.switch_to.new_window('tab')
driver.get('https://www.selfinstaller.com/')
# driver.switch_to.new_window('window')
# driver.get('https://www.google.com/')
driver.save_screenshot(os.getcwd()+'//homeselfinstaller.png')
