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




#Magneto App:

# download chrome driver file
service = Service("E:/selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# our domian name
driver.get("http://13.235.64.60:3000/")
driver.maximize_window()
driver.implicitly_wait(1000)

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
# select magneto app:

magneto_app_select = driver.find_element(By.ID, "11")
magneto_app_select.click()
# Enter form details
driver.find_element(By.NAME, "app_name").send_keys("Test App magnetoo")
driver.find_element(By.ID, "project-id").send_keys("Magneto Project newDD")
# driver.find_element(By.ID, "default-checkbox").click()
# select_element1 = driver.find_element(By.ID, "project-app")
# select_element1.click()
#select drop down
# select_object1 = Select(select_element1)
# select_object1.select_by_index(3)
# select_element1.click()
#select drop down
select_element2 = driver.find_element(By.ID, "app_version")
select_object2 = Select(select_element2)
select_object2.select_by_index(0)
#select drop down
select_element3 = driver.find_element(By.ID, "os")
select_element3.click()
select_object3 = Select(select_element3)
select_object3.select_by_index(2)
select_element3.click()
# Enter IP address:
# driver.find_element(By.ID, "add_ip_open_btn").click()
# driver.find_element(By.ID, "add_ip").send_keys("182.12.14")   
# driver.find_element(By.ID, "add_ip_submit_btn").click()

#IP address select:
all_options = driver.find_elements(By.XPATH, '//*[@id="ip-address-id"]/option')
print("ip_address_list",all_options)
print(all_options)
for opt in all_options:
    
    print("opt",opt.text)
    ans = opt.get_attribute('value')
    print("ans",ans)
    if ans == "1.23.23.2":
        print("clickkkk")
        driver.find_element(By.ID, "ip-address").send_keys(ans)
        break
print("jj")
#ssh_user_name_select
ssh_username = driver.find_elements(By.XPATH, '//*[@id="ssh-username-show"]/option')
list=[]
for user_name in ssh_username:
    names = user_name.get_attribute('value')
    list.append(names)
# driver.find_element(By.NAME, "ssh_user").send_keys(list[5])
# print(list[5])
    if names == 'ubuntu':
        driver.find_element(By.ID, "ssh-username-input").send_keys(names)
        break




#db_name:
driver.find_element(By.ID, "db_name").send_keys("My Database")
#domian_name
driver.find_element(By.ID, "domain_name").send_keys("https://www.testdomian2.com/")
#Email_id
driver.find_element(By.ID, "email_id").send_keys("tester@gmail.com")

# magneto_video_clip = driver.find_element(By.XPATH, "//a[@href='https://youtu.be/HpwsbgqSR2g']").click()
# driver.back()
driver.find_element(By.ID, "magento_public_key").send_keys("********public_key")
driver.find_element(By.ID, "magento_private_key").send_keys("*******private_key")
driver.find_element(By.ID, "magento_admin_username").send_keys("admin_name")
#Select version in PHP
select_element4 = driver.find_element(By.ID, "php_version")
select_element4.click()
#select drop down
select_object4 = Select(select_element4)
select_object4.select_by_index(0)
select_element4.click()

#try code start
# driver.find_element(By.ID, "add_ssh_key_open_btn").click()
# driver.find_element(By.ID, "add_ssh_key").click()
# driver.find_element(By.XPATH, "//button[text()='Upload ssh key']").click()
# driver.find_element(By.ID, "add_ssh_key_close_btn").click()
#try code end

#SSH Pem Key Select:
driver.implicitly_wait(60)
# driver.find_element(By.XPATH,"//button[text()='Add ssh key']").click()
# driver.find_element(By.ID, "ssh-file").click()
# pathone = "E:/csv_file/employees.csv"
# path = "E:/Bank/bank/bankinfo.pdf"
# driver.find_element(By.XPATH, "//*[@id='ssh-file']").send_keys(path)
# driver.find_element(By.XPATH, "//button[text()='Upload ssh key']").click()
time.sleep(5)
select_element6 = driver.find_element(By.ID, "ssh-key-id")
select_element6.click()
select_object6 = Select(select_element6)
select_object6.select_by_index(0)
select_element6.click()


#checkbox Select
driver.find_element(By.ID, "key_delete").click()
#Submit btn
driver.find_element(By.ID, "comman-form-create-app-button").click()
 
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
#--------------------------------#





































