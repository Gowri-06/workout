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
driver.get("http://13.235.64.60:3000/")
driver.maximize_window()
driver.implicitly_wait(10)
# Home login click to enter in to login page
login_click = driver.find_element(By.XPATH, "//*[@id='__next']/header/div/div[3]").click()

# login_click = driver.find_element(By.XPATH, "/html/body/header/div/div[3]/a")
actions = ActionChains(driver)
actions.click(on_element=login_click)
actions.perform()
# login = driver.find_element(By.CLASS_NAME, "login")
# login.click()
# print(login)
# Enter login details
driver.find_element(By.ID, "email-address").send_keys("ccc@gmail.com")
driver.find_element(By.ID, "password").send_keys("123")
driver.find_element(By.XPATH, "//button[text()='Sign in']").click()
# login = driver.find_element(By.CLASS_NAME, "login")
# login.click()
# print(login)
# Enter login details
# driver.find_element(By.ID, "id_login").send_keys("gowridev007@gmail.com")
# driver.find_element(By.ID, "id_password").send_keys("tester@123")
# login_page = driver.find_element(By.CSS_SELECTOR, "button").click()
# print("text",login_page)
# Enter in to setting's page
driver.find_element(By.XPATH, "//a[@href='/settings']").click()

# link = driver.find_element(By.LINK_TEXT, 'Settings')
# link.click()

#Navigate to ssh key Link Page
ssh_username_link = driver.find_element(By.XPATH, "//button[text()='SSH Key']")
ssh_username_link.click()

#delete ssh key code start
# ssh_key_delete = driver.find_element(By.XPATH,"//*[@id='__next']/div/div/div[2]/div[4]/div/div/div/div[2]/button")
# ssh_key_delete.click()
# ssh_key_delete = driver.find_element(By.CLASS_NAME, "delete_btn_open_btn")
# ssh_key_delete.click()
#delete ssh key code end

#ssh_key_pop_up_delete start
# ssh_key_pop_up_delete = driver.find_element(By.XPATH, "//*[@id='ssh_key']/div[1]/div/div/div[2]/a)")
# ssh_key_pop_up_delete.click()
#ssh_key_pop_up_delete end

#ssh_key_pop_up_close start
# ssh_key_pop_up_close = driver.find_element(By.CLASS_NAME, "delete_btn_close_btn")
# ssh_key_pop_up_close.click()
#ssh_key_pop_up_close end



#Navigate to ssh username Link Page
ssh_username_link = driver.find_element(By.XPATH, "//button[text()='SSH Username']")
ssh_username_link.click()
time.sleep(3)
#ssh username delete code start absolute path method
# ssh_username_delete = driver.find_element(By.XPATH, "/html/body/main/section/section/div[3]/div[1]/div/button")
# ssh_username_delete.click()
# time.sleep(3)
# ssh_username_delete = driver.find_element(By.CLASS_NAME, "delete_btn_open_btn")
# ssh_username_delete.click()
#ssh username delete code end

#ssh username popup delete start
# ssh_username_pop_up_delete = driver.find_element(By.XPATH, "/html/body/main/section/section/div[3]/div[1]/div/div/div[2]/a").click()
# ssh_username_pop_up_delete.click()
#ssh username popup delete end

#ssh username popup close start absolute path method
# ssh_username_pop_up_close = driver.find_element(By.XPATH, "/html/body/main/section/section/div[3]/div[1]/div/div/div[2]/div")
# ssh_username_pop_up_close.click()
# time.sleep(3)
# ssh_username_pop_up_close = driver.find_element(By.CLASS_NAME, "delete_btn_close_btn")
# ssh_username_pop_up_close.click()
#ssh username popup close end



#Navigate To IP Address Link Page
ip_address_link = driver.find_element(By.XPATH, "//button[text()='Ip Address']")
ip_address_link.click()

#IP address delete code start absolute path
# ip_address_delete = driver.find_element(By.XPATH, "/html/body/main/section/section/div[4]/div[1]/div/button")
# ip_address_delete.click()
# time.sleep(3)
# ip_address_delete = driver.find_element(By.CLASS_NAME, "delete_btn_open_btn")
# ip_address_delete.click()
#IP address delete code end

#IP address popup delete start
# ip_address_pop_up_delete = driver.find_element(By.XPATH, "href='/frontend/settings-del-ssh-key/employees.csv/'")
# ip_address_pop_up_delete.click()
#IP address popup delete end

#IP address popup close start
# ip_address_pop_up_close = driver.find_element(By.XPATH, "/html/body/main/section/section/div[4]/div[1]/div/div/div[2]/div")
# ip_address_pop_up_close.click()
# time.sleep(3)
# ip_address_pop_up_close = driver.find_element(By.CLASS_NAME, "delete_btn_close_btn")
# ip_address_pop_up_close.click()
#IP address popup close end

#Navigate to App store Page
# app_store_home = driver.find_element(By.LINK_TEXT, "App Store")
# app_store_home.click() 

# self_installer_home_page = driver.find_element(By.LINK_TEXT, "Selfinstaller")
# self_installer_home_page.click()

#code logout start
# logo_click = driver.find_element(By.CLASS_NAME, "profile_img")
# logo_click.click()
# logout_element = driver.find_element(By.ID, "logout")
# print(logout_element)
# logout_element.click()
#code logout end

