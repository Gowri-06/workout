# from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys  






# download chrome driver file
service = Service("http://3.110.146.90:3000/")
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
driver.find_element(By.ID, "project-name-text-input").send_keys("Test Project7")
# driver.find_element(By.ID, "add-existing-project").click()
# select_element1 = driver.find_element(By.ID, "project-name-select-input")
# select_element1.click()
#select drop down
# select_object1 = Select(select_element1)
# select_object1.select_by_index(5)
# select_element1.click()
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
# Enter IP address
# driver.find_element(By.ID, "add_ip_open_btn").click()
# driver.find_element(By.ID, "add_ip").send_keys("182.12.14")   
# driver.find_element(By.ID, "add_ip_submit_btn").click()

#IP address seletc:
all_options = driver.find_elements(By.XPATH, '//*[@id="ip_address_list"]/option')
print("ssh_user2",all_options)
print(all_options)
for opt in all_options:
    
    print("opt",opt.text)
    ans = opt.get_attribute('value')
    print("ans",ans)
    if ans == "4.233.432.6":
        print("clickkkk")
        driver.find_element(By.NAME, "ip_address").send_keys(ans)
        break

       
       
print("jj")
ssh_username = driver.find_elements(By.XPATH, '//*[@id="ssh_username_list"]/option')
list=[]
for user_name in ssh_username:
    names = user_name.get_attribute('value')
    list.append(names)
# driver.find_element(By.NAME, "ssh_user").send_keys(list[5])
# print(list[5])
    if names == 'ssh_user2':
        driver.find_element(By.NAME, "ssh_user").send_keys(names)
        break



# a = driver.find_element(By.XPATH, "//option[text()='ssh_user2']")
# a.click()


# select_element4 = driver.find_element(By.ID, "ip_address").click()
# driver.find_element(By.XPATH("//*[@id='ip_address']/option[1]")).click()
# By.XPath("//*[@id='applianceNames']/option["+ index +"]")
# //*[@id="ip_address_list"]/option[1]
# a =driver.find_element(By.TAG_NAME, "option")



# driver.find_element(By.XPATH , "//option[contains(text(),'192.168.1.1')]").click()
# driver.find_element(By.XPATH, "//*[@id="ip_address_list"]/option[1]").click()

# //*[@id="ip_address_list"]/option[1]
# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"[@id="ip_address_list"]/option[1]"))).click()

# plants = driver.find_element(By.TAG_NAME, "datalist")
# print("xxxxxx",plants.text[0:4])

# select_object4 = Select(select_element4)
# select_object4.select_by_index(1)
# select_element4.click()
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//option[@value='127.0.0.1:8006' and @ng-reflect-value='127.0.0.1:8006']"))).click()



# driver.find_element(By.XPATH("//*[@id='applianceNames']/option["+ "0" +"]")).click()

# Enter SSH Username
# driver.find_element(By.ID, "add_ssh_username_open_btn").click()
# driver.find_element(By.ID, "add_ssh_username").send_keys("ssh_user2")  
# driver.find_element(By.XPATH, "//button[text()='Add SSH Username']").click()

#try code start
driver.find_element(By.ID, "add_ssh_key_open_btn").click()
driver.find_element(By.ID, "add_ssh_key").click()
pathone = "E:/csv_file/employees.csv"
path = "E:/Bank/bank/bankinfo.pdf"
driver.find_element(By.XPATH, "//*[@name='add_ssh_key']").send_keys(path)
driver.find_element(By.XPATH, "//button[text()='Upload ssh key']").click()
driver.find_element(By.ID, "add_ssh_key_close_btn").click()
#try code end
driver.implicitly_wait(60)
# select_element6 = driver.find_element(By.ID, "ssh_key")
# select_element6.click()
# select_object6 = Select(select_element6)
# select_object6.select_by_index(3)
# select_element6.click()
driver.find_element(By.ID, "email_id").send_keys("tester@009.com")
driver.find_element(By.ID, "domain_name").send_keys("https://www.testdomian2.com/")
driver.find_element(By.ID, "key_delete").click()
# driver.find_element(By.CLASS_NAME, "main_form_submit_btn").click()
 
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

#Magneto App:































#  fruit = driver.find_element_by_css_selector("#fruits .tomatoes")
# fruit = driver.find_element_by_css_selector("feedback-btn")
# search_box = driver.find_element(by=By.NAME, value="q")
# search_button = driver.find_element(by=By.NAME, value="btnK")
# plants = driver.find_elements(By.TAG_NAME, "input")
# print("lissss",plants)

# element = driver.find_element(By.TAG_NAME, "div")
# print("element",element)
# elements = element.find_elements(By.TAG_NAME, "button")
# print("eleee",elements)
# for e in elements:
#     print("e---",e.text) 
# text = driver.find_element(By.CSS_SELECTOR, "button").text
# print("text",text)
# attr = driver.find_element(By.CSS_SELECTOR, "h1").rect
# print("attrb",attr)

# val = driver.find_element(By.CLASS_NAME ,"email")
# print("check",val)
# title = driver.title
# print("tabtitle",title)
# url = driver.current_url
# print("url_value",url)
# driver.find_element(By.CLASS_NAME, "email")
# driver.find_element(By.CLASS_NAME ,"login-submit").click()


  
# driver.find_element(By.PARTIAL_LINK_TEXT ,"Test").click()

# driver.find_element(By.CLASS_NAME, "email").send_keys("waranshankar91@gmail.com")
# driver.find_element(By.CLASS_NAME, "login__password").send_keys("test@123")
# driver.find_element(By.CLASS_NAME ,"login-submit").click()

# driver.refresh()
# driver.add_cookie({"name": "foo", "value": "bar"})
# driver.add_cookie({"name": "foo", "value": "value", 'sameSite': 'Strict'})
# driver.add_cookie({"name": "foo1", "value": "value", 'sameSite': 'Lax'})
# cookie1 = driver.get_cookie('foo')
# cookie2 = driver.get_cookie('foo1')
# print(cookie1)
# print(cookie2)
# # Get cookie details with named cookie 'foo'
# print(driver.get_cookie("foo"))


# time.sleep(5)
# login_form = driver.find_element(By.XPATH, "//form[@id='loginForm']")
# driver.find_element(By.ID, "ip_address").click()
# driver.find_element(By.XPATH, "//option[@value='182.12.14']").click()
# driver.find_element(By.XPATH, "//*[starts-with(@value,'182.12.14')]").click()
# XPath: //tagname[contains(@attribute, 'value')]

# driver.find_element(By.XPATH, "//option[contains(@value, '182.12.14')]").click()
# //tag_name[text()='any text content']
# //option[@value="182.12.14"]//following-sibling::option[@value='127.0.0.1:8001']
# xpath=//*[@value='182.12.14']//following-sibling::input
# driver.find_element(By.XPATH, "//[*value='182.12.14']//following-sibling::option")
# driver.find_element(By.XPATH, "//datalist[@id='ip_address_list']//following-sibling::option[@value='127.0.0.1:8001']").click()
# hi = driver.find_element(By.XPATH, "//option[text()='182.12.14']")
# print("hhhhhhhh",hi.text)


# driver.quit()