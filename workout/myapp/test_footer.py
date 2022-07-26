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
driver.get("http://3.108.225.70:3000/")
driver.maximize_window()
driver.implicitly_wait(10)
#docs page
driver.find_element(By.XPATH, "//*[@id='__next']/header/div/div[2]/span[2]").click()
time.sleep(3)
driver.back()
#pricing
driver.find_element(By.XPATH, "//*[@id='__next']/header/div/div[2]/span[3]").click()
# driver.find_element(By.XPATH, "//a[@href='/pricing']").click()
time.sleep(2)
driver.back()
#contact us
driver.find_element(By.XPATH, "//*[@id='__next']/header/div/div[2]/span[4]").click()
driver.find_element(By.NAME, "firstName").send_keys("test")
driver.find_element(By.NAME, "lastName").send_keys("name")
driver.find_element(By.NAME, "email").send_keys("acv@gmail.com")
driver.find_element(By.NAME, "phone").send_keys("8867679012")
driver.find_element(By.NAME, "subject").send_keys("subject")
driver.find_element(By.ID, "message").send_keys("Hi there how u doing???")
driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(3)
driver.back()
driver.find_element(By.XPATH, "//*[@id='__next']/footer/div/div[1]/div[2]/div[2]/div[2]/span").click()
time.sleep(3)
driver.back()
driver.find_element(By.XPATH, "//*[@id='__next']/footer/div/div[1]/div[2]/div[2]/div[3]/span").click()
time.sleep(3)
driver.back()
#footer twitter
driver.find_element(By.XPATH, "//*[@id='__next']/footer/div/div[1]/div[2]/div[3]/div[1]/span").click()
driver.back()
#footer linked in
driver.find_element(By.XPATH, "//*[@id='__next']/footer/div/div[1]/div[2]/div[3]/div[2]/span").click()
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
