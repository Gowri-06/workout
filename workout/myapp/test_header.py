import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
flag = driver.find_element(By.XPATH, "/html/body/div/section[4]/div[1]/h2")
driver.execute_script("arguments[0].scrollIntoView();", flag)
time.sleep(4)
# driver.execute_script("window.scrollBy(0,900)","") 
# yaxis_pixels = driver.execute_script("return window.pageYOffset;")
# print(yaxis_pixels)
driver.back()
driver.find_element(By.XPATH, "//a[@href='/contact-us']").click()
# driver.find_element(By.NAME, "name").send_keys("testname")
# driver.find_element(By.NAME, "email").send_keys("acv@gmail.com")
# driver.find_element(By.ID, "message").send_keys("Hi there how u doing???")
driver.find_element(By.XPATH, "//button[text()='Send']").click()
time.sleep(3)
driver.back()
driver.find_element(By.XPATH, "//a[@href='/blog/']").click()
driver.find_element(By.XPATH, "//a[@href='/blog/self-installer-intro']").click()
driver.execute_script("window.scrollTo(5, document.body.scrollHeight);")
time.sleep(3)
driver.back()
driver.back()
driver.find_element(By.XPATH, "//a[@href='/tutorial/']").click()
# driver.find_element(By.XPATH, "//a[@href='/tutorial/https']").c
# click()
mywait = WebDriverWait(driver,10,poll_frequency=2)
element = mywait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/tutorial/https']")))
element.click()
driver.back()
element2 = mywait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/tutorial/wordpress']")))
# element2.click()
# driver.back()
driver.find_element(By.XPATH, "//a[@href='/tutorial/wordpress']").click()
time.sleep(3) 
driver.back()
mywait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/tutorial/lamp']")))
driver.find_element(By.XPATH, "//a[@href='/tutorial/lamp']").click()
time.sleep(5)
driver.back()
mywait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/tutorial/wordpress_simple']")))
driver.find_element(By.XPATH, "//a[@href='/tutorial/wordpress_simple']").click()
time.sleep(3)
driver.back()
time.sleep(2)
mywait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/tutorial/lamp_simple']")))
driver.find_element(By.XPATH, "//a[@href='/tutorial/lamp_simple']").click()
time.sleep(5)
driver.back()
mywait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/tutorial/magento']")))
driver.find_element(By.XPATH, "//a[@href='/tutorial/magento']").click()
time.sleep(3)
driver.back()



