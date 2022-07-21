
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

# def headless_chrome():
#     from selenium.webdriver.chrome.service import Service
#     service = Service("E:/selenium/chromedriver.exe")
#     ops = webdriver.ChromeOptions()
#     ops.headless=True
#     driver = webdriver.Chrome(service=service,options=ops)
#     return driver







# driver = headless_chrome()
# download chrome driver file
service = Service("E:/selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# our domian name
driver.get("https://www.selfinstaller.com/")
driver.maximize_window()
driver.implicitly_wait(1000)
# Home login click to enter in to login page
login = driver.find_element(By.CLASS_NAME, "login")
login.click()
print(login)
# Enter login details
driver.find_element(By.ID, "id_login").send_keys("gowridev007@gmail.com")
driver.find_element(By.ID, "id_password").send_keys("tester@123")
login_page = driver.find_element(By.CSS_SELECTOR, "button").click()
print("text",login_page)
# select first app 
sslOnApache1 = driver.find_element(By.CLASS_NAME, "apps_library_select_btn")
sslOnApache1.click()
# Enter form details
driver.find_element(By.ID, "app_name").send_keys("Test App")
driver.find_element(By.ID, "project-name-text-input").send_keys("Test Project")
driver.find_element(By.ID, "add-existing-project").click()
select_element1 = driver.find_element(By.ID, "project-name-select-input")
select_element1.click()
#select drop down
select_object1 = Select(select_element1)
select_object1.select_by_index(0)
select_element1.click()
#select drop down
select_element2 = driver.find_element(By.ID, "app_version")
select_object2 = Select(select_element2)
select_object2.select_by_value("latest")
#select drop down
select_element3 = driver.find_element(By.ID, "os")
select_element3.click()
select_object3 = Select(select_element3)
select_object3.select_by_index(2)
select_element3.click()
data = driver.find_elements(By.TAG_NAME, "option")
driver.find_element(By.ID, "ip_address").click()
# print(data)
# list = []
# for dataone in data:
    # print(type(data))
#     data2 = dataone.get_attribute('value')
#     list.append(data2)
#     print("list",list)

# print("6thvalue",list[6])
    # print("daaneewwe",data2[1])


# data = driver.find_elements(By.XPATH,"//option[contains(text(),'182.12.14')]/parent::datalist")
# print("dataaaa",len(data))
# data = driver.find_elements(By.XPATH,"//div[@id='ip_address_list']//option")
# print("dataaaass",len(data))
# for datas in data:
#     print("amna",datas.text)
time.sleep(3)
driver.implicitly_wait(1000)
all_options = driver.find_elements(By.XPATH, '//*[@id="ip_address_list"]/option')
print("ssh_user2",all_options)
print(all_options)
for opt in all_options:
    
    print("opt",opt.text)
    print("\nm\n\n")
    # print("optssh_username_listssh_username_list",opt)
    ans = opt.get_attribute('value')
    print("ans",ans)
    # driver.find_element(By.NAME, "")
    if ans == "4.233.432.6":
        print("clickkkk")
        driver.find_element(By.NAME, "ip_address").send_keys(ans)

        # try:
        #     opt.click()
        # except Exception as er:
        #     print(er)
        print('solution')
        break
       
print("jj")
ssh_username = driver.find_elements(By.XPATH, '//*[@id="ssh_username_list"]/option')
# naame = ssh_username.get_attribute('value')
list=[]
for naame in ssh_username:
    names = naame.get_attribute('value')
    list.append(names)
# driver.find_element(By.NAME, "ssh_user").send_keys(list[5])
# print(list[5])
    if names == 'ssh_user2':
        driver.find_element(By.NAME, "ssh_user").send_keys(names)
        break
driver.back()
driver.forward()
driver.refresh()
#temp code ends here


