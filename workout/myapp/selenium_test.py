import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# C:\Users\Vishali Arumugam\Downloads\chromedriver_win32
service = Service("E:/selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://tester.userpeek.io/login")

driver.find_element(By.CLASS_NAME ,"email").send_keys("vishalisri1551@gmail.com")
driver.find_element(By.CLASS_NAME ,"login__password").send_keys("Test@123")
driver.find_element(By.CLASS_NAME ,"login-submit").click()

actual_title = driver.title
exp_title = "userpeek"

# time.sleep(1000)

if(driver.title == exp_title):
    try:
        driver.find_element(By.PARTIAL_LINK_TEXT ,"Test").click()
    except Exception as err:
        print(err)
