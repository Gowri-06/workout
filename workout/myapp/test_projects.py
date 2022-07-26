import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.action_chains import ActionChains


# downolad chrome driver file
service = Service("E:/selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service)
# our domian name
driver.get("http://13.235.64.60:3000/")
# driver.find_element(By.XPATH,"/html/body/header/div/div[3]/a")
driver.maximize_window()
driver.implicitly_wait(10)
# Home login click to enter in to login page
login_click = driver.find_element(By.XPATH, "//*[@id='__next']/header/div/div[3]").click()
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
# Enter Projects Page
driver.find_element(By.XPATH, "//a[@href='/projects']").click()

# link = driver.find_element(By.LINK_TEXT, 'Projects').send_keys(Keys.CONTROL + Keys.RETURN)
# link = driver.find_element(By.LINK_TEXT, 'Projects')
# link.click()
# driver.implicitly_wait(100)
# Go to all projects link
all_project_link = driver.find_element(By.ID, "all_project_id")
all_project_link.click()

#Projects delete code start
# projects_delete = driver.find_element(By.XPATH, "//*[@id='63']/div/div[3]/button")
# projects_delete.click()
#Projects delete code end

#Projects popup delete start
# projects_pop_up_delete = driver.find_element(By.XPATH, "//a[@href='/frontend/project/50/']").click()
# projects_pop_up_delete = driver.find_element(By.CLASS_NAME, "delete_btn")
# projects_pop_up_delete.click()
#Projects popup delete end

#Projects popup close start
# projects_pop_up_close = driver.find_element(By.CLASS_NAME, "delete_project_close_btn")
# projects_pop_up_close.click()
#Projects popup close end
time.sleep(5)
# click project link
single_project_link = driver.find_element(By.XPATH, "//*[@id='63']")
single_project_link.click()
# single_project_link = driver.find_element(By.LINK_TEXT, "testing")
# single_project_link.click()
# click project name to open
test_link_open = driver.find_element(By.XPATH, "//*[@id='132']/td[1]/div/div")
test_link_open.click()
# click project name to close
test_link_close = driver.find_element(By.ID, "viewdomain-close-btn")
test_link_close.click()
# view log link
driver.find_element(By.XPATH, "//a[@href='/projects/view-log/132']").click()

# view_log_link = driver.find_element(By.CLASS_NAME, 'app_log')
# view_log_link.click()
# time.sleep(5)
# view_log_link = driver.find_element(By.CLASS_NAME, 'app_log')
# view_log_link.click()
# time.sleep(5)
# view log return
# tab position in chrome browser
driver.switch_to.window(driver.window_handles[1])
# view log return
# driver.find_element(By.XPATH, "//a[@href='/frontend/project/50/']").click()
# time.sleep(3)

# view_log_return = driver.find_element(By.LINK_TEXT, "testing")
# view_log_return.click()
# view credentials open
view_credentials_link = driver.find_element(By.XPATH, "//*[@id='132']/td[6]/div[2]/div")   
view_credentials_link.click()
# download credentials
download_credentials = driver.find_element(By.ID, "download-csv-file") 
download_credentials.click()
#close credentials in popup
close_credentials = driver.find_element(By.ID, "credential-close-btn")
close_credentials.click()
# Enter in to docs page
docs_page = driver.find_element(By.LINK_TEXT, 'Docs')
docs_page.click()
driver.back()

# delete button start
# delete_single_project = driver.find_element(By.XPATH, "//*[@id='132']/td[8]/div[2]/div")   
# delete_single_project.click()
#delete button end

#App section popup delete start
# app_section_pop_up_delete = driver.find_element(By.XPATH, "//a[@href='/frontend/project/50/']")
# app_section_pop_up_delete.click()
#App section popup delete end

#App section popup close code start
# app_section_pop_up_close = driver.find_element(By.CLASS_NAME, "delete_app_close_btn")
# app_section_pop_up_close.click()
#App section popup close code end

# Create app
create_app = driver.find_element(By.CLASS_NAME, "apps_library_open_btn")
create_app.click()

#Navigate to projects page
projects_dashboard = driver.find_element(By.LINK_TEXT, "Projects")
projects_dashboard.click()

self_installer_home_page = driver.find_element(By.LINK_TEXT, "Selfinstaller")
self_installer_home_page.click()

#code logout start
logo_click = driver.find_element(By.CLASS_NAME, "profile_img")
logo_click.click()
logout_element = driver.find_element(By.ID, "logout")
print(logout_element)
logout_element.click()
#code logout end



