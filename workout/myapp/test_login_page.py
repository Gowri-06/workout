# from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys  






# download chrome driver file
service = Service("E:/selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service)
# our domian name
driver.get("http://3.110.146.90:3000/")
driver.maximize_window()
driver.implicitly_wait(1000)
# Home login click to enter in to login page
login_click = driver.find_element(By.XPATH, "//a[@href='/signin']").click()

# login_click = driver.find_element(By.XPATH, "/html/body/header/div/div[3]/a")
actions = ActionChains(driver)
actions.click(on_element=login_click)
actions.perform()
# login = driver.find_element(By.CLASS_NAME, "login")
# login.click()
# print(login)
# Enter login details
driver.find_element(By.ID, "email-address").send_keys("xyz@gmail.com")
driver.find_element(By.ID, "password").send_keys("xyz")
driver.find_element(By.XPATH, "//button[text()='Sign in']").click()
driver.find_element(By.XPATH, "//*[@id='__next']/div/div/div[1]/div[1]/div/div[2]/button/div/div[2]/p[2]").click() 
driver.implicitly_wait(1000)
driver.find_element(By.ID, "profile-close-btn").click()
# driver.find_element(By.ID, "profile-button").click()

# login_page = driver.find_element(By.CSS_SELECTOR, "button").click()
# driver.find_element(By.ID, "id_login").send_keys("gowridev007@gmail.com")
# driver.find_element(By.ID, "id_password").send_keys("tester@123")
# login_page = driver.find_element(By.CSS_SELECTOR, "button").click()
# time.sleep(5)
# print("text",login_page)
# driver.back()
# driver.find_element(By.XPATH, "//a[@href='/accounts/password/reset/']").click()
# driver.find_element(By.ID, "id_email").send_keys("tesss@gmail.com")
# driver.find_element(By.XPATH, "//button[text()='Send Mail']").click()
# time.sleep(2)
# driver.back()
# driver.back()
# driver.implicitly_wait(2000)
# driver.find_element(By.XPATH, "//a[@href='/accounts/github/login/']").click()
# driver.find_element(By.XPATH, "//a[@href='/accounts/login/']").click() 
# driver.back()
# driver.find_element(By.XPATH, "//a[@href='/accounts/signup/']").click() 
# driver.back()
# driver.find_element(By.XPATH, "/html/body/div/ul/li[1]/a") 
# driver.back()
# driver.find_element(By.XPATH, "/html/body/div/ul/li[1]/a") 
# driver.back()

# driver.find_element(By.XPATH, "//button[text()='Continue']").click()
# driver.find_element(By.ID, "login_field").send_keys("tesss@gmail.com")
# driver.find_element(By.ID, "password").send_keys("password")
# driver.find_element(By.NAME, "commit").click()

# driver.back()
# driver.back()
# driver.find_element(By.XPATH, "//a[@href='/accounts/google/login/']").click()
# driver.find_element(By.XPATH, "//a[@href='/accounts/login/']").click() 
# driver.back()
# driver.find_element(By.XPATH, "//a[@href='/accounts/signup/']").click() 
# driver.back()
# time.sleep(2)

# driver.find_element(By.XPATH, "//button[text()='Continue']").click()
# time.sleep(2)
# driver.back()
# driver.back()

driver.find_element(By.XPATH, "//a[@href='/signup']").click()
driver.find_element(By.NAME, "email").send_keys("ccc@gmail.com")
# driver.find_element(By.NAME, "username").send_keys("someone.com")
driver.find_element(By.NAME, "password").send_keys("1234")
driver.find_element(By.NAME, "conform-password").send_keys("1234")
# driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
# driver.back()
# driver.back()



















# logo_click = driver.find_element(By.CLASS_NAME, "profile_img")
# logo_click.click()
# logout_element = driver.find_element(By.ID, "logout")
# print(logout_element)
# logout_element.click()

