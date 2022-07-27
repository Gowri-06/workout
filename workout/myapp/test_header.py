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
driver.get("http://3.6.116.230:3000/")
driver.maximize_window()
driver.implicitly_wait(10)

#Header section starts
#Pricing section
driver.find_element(By.ID, "pricing").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

#flag is scroll to desired element: 
# flag = driver.find_element(By.XPATH, "/html/body/div/section[4]/div[1]/h2")
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# time.sleep(4)
# driver.execute_script("window.scrollBy(0,900)","") 
# yaxis_pixels = driver.execute_script("return window.pageYOffset;")
# print(yaxis_pixels)
driver.back()
# driver.find_element(By.XPATH, "//a[@href='/contact-us']").click()

#Contact-us section
driver.find_element(By.ID, "contact-us").click()
driver.find_element(By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/div[1]/ul/li[1]/a/span[2]/img").click()
time.sleep(3)
driver.back()
driver.implicitly_wait(7)
driver.find_element(By.XPATH, "//a[@href='https://github.com/premjagadeesan']").click()
time.sleep(3)
driver.back()
# driver.find_element(By.ID, "first-name").send_keys("person")
driver.find_element(By.ID, "last-name").send_keys("enters")
driver.find_element(By.ID, "email").send_keys("acv@gmail.com")
driver.find_element(By.ID, "phone").send_keys("8345678910")
driver.find_element(By.ID, "subject").send_keys("quotation")
driver.find_element(By.ID, "message").send_keys("Hi there how u doing???")
driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(3)
driver.back()
time.sleep(5)
#Blog section
driver.find_element(By.ID, "blog").click()
driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/div/div[1]").click()
driver.execute_script("window.scrollTo(5, document.body.scrollHeight);")
time.sleep(3)
driver.back()
driver.back()
#Tutorial section
driver.find_element(By.ID, "tutorial").click()
mywait = WebDriverWait(driver,10,poll_frequency=2)

element = mywait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[2]/div[1]/div[1]"))).click()
time.sleep(5)
driver.back()

element2 = mywait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/div[2]/div[2]/div[1]"))).click()
time.sleep(5)
driver.back()

element3 = mywait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/div[2]/div[3]/div[1]"))).click()
time.sleep(5) 
driver.back()

element4 = mywait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/div[2]/div[4]/div[1]"))).click()
# driver.find_element(By.XPATH, "//a[@href='/tutorial/lamp']").click()
time.sleep(5)
driver.back()

element5 = mywait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/div[2]/div[5]/div[1]"))).click()
# driver.find_element(By.XPATH, "//a[@href='/tutorial/wordpress_simple']").click()
time.sleep(5)
driver.back()


element6 = mywait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/div[2]/div[6]/div[1]"))).click()
# driver.find_element(By.XPATH, "//a[@href='/tutorial/lamp_simple']").click()
time.sleep(5)
driver.back()
driver.back()

# mywait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/tutorial/magento']")))
# driver.find_element(By.XPATH, "//a[@href='/tutorial/magento']").click()
# time.sleep(3)
# driver.back()



