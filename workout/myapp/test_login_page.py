import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains







# download chrome driver file
service = Service("E:/selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# our domian name
driver.get("http://3.6.116.230:3000/")
driver.maximize_window()
driver.implicitly_wait(100)

# Home login click to enter in to login page
login_click = driver.find_element(By.XPATH, "//*[@id='__next']/header/div/div[3]").click()
actions = ActionChains(driver)
actions.click(on_element=login_click)
actions.perform()
time.sleep(2)


#Enter login details
driver.find_element(By.ID, "email-address").send_keys("ccc@gmail.com")
driver.find_element(By.ID, "password").send_keys("123")
driver.find_element(By.XPATH, "//button[text()='Sign in']").click()

#Forget password section
driver.find_element(By.ID, "forget-password").click()
driver.find_element(By.ID, "email-address").send_keys("gowrishankr366@gmail.com")
driver.find_element(By.XPATH, "//button[text()='Forget Password']").click()

#Logout section
driver.find_element(By.XPATH, "//*[@id='__next']/div/div/div[1]/div[1]/div/div[2]/button/div/div[2]/p[2]").click() 
driver.find_element(By.ID, "profile-close-btn").click()
driver.find_element(By.XPATH, "//button[text()='Logout']").click()
# login_page = driver.find_element(By.CSS_SELECTOR, "button").click()

#github login
driver.find_element(By.ID, "github-signin").click()
time.sleep(4)
driver.back()

#google login
driver.find_element(By.ID, "google login").click()
time.sleep(3)
driver.back()

#Signup Section
driver.find_element(By.ID, "Sign up").click()
# driver.find_element(By.XPATH, "//button[text()='Sign up']").click()
driver.find_element(By.ID, "email-address").send_keys("dddd@gmail.com")
# driver.find_element(By.NAME, "username").send_keys("someone.com")
driver.find_element(By.NAME, "password").send_keys("1234")
driver.find_element(By.NAME, "conform-password").send_keys("1234")
driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()






















