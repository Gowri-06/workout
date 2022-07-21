# http://3.110.146.90:3000/contact#

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains


# download chrome driver file
service = Service("E:/selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# our domian name
driver.get("http://3.110.146.90:3000/")
driver.maximize_window()
# driver.implicitly_wait(10)
driver.set_page_load_timeout(7000)



# Home login click to enter in to login page
login = driver.find_element(By.CLASS_NAME, "login")
login.click()
print(login)
action = ActionChains(driver)
action.reset_actions()

# Enter login details
driver.find_element(By.ID, "id_login").send_keys("gowridev007@gmail.com")
driver.find_element(By.ID, "id_password").send_keys("tester@123")
login_page = driver.find_element(By.CSS_SELECTOR, "button").click()
print("text",login_page)

# Enter in to credits page
link = driver.find_element(By.LINK_TEXT, 'Credits')
link.click()

# Navigate to payment history
driver.find_element(By.XPATH, "//button[text()='Payment History']").click()
time.sleep(4)

# Navigate to add credit points page 
driver.find_element(By.XPATH, "//button[text()='Add Credit Points']").click()

#Add money to increase your credits
add_credits = driver.find_element(By.ID, "credit_amount").send_keys("10")
driver.find_element(By.XPATH, "//button[text()='Proceed']").click()

#Pay with card
email_field = driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
# card_info = driver.find_element(By.NAME, "cardNumber").send_keys("1234 1111 1111 1111")
# card_expiry = driver.find_element(By.CLASS_NAME, "cardExpiry").send_keys("07/27")
# card_cvc = driver.find_element(By.CLASS_NAME, "cardCvc").send_keys("022")
billing_name = driver.find_element(By.NAME, "billingName").send_keys("Legend")
billing_country = driver.find_element(By.NAME, "billingCountry").send_keys("India")
billing_address_line1 = driver.find_element(By.NAME, "billingAddressLine1").send_keys("Iris Watson P.O. Box 283 8562 Fusce Rd. Frederick Nebraska 20620(372) 587-2335")
billing_address_line2 = driver.find_element(By.NAME, "billingAddressLine2").send_keys("Cecilia Chapman711-2880 Nulla St.Mankato Mississippi 96522(257) 563-7401")
city_name = driver.find_element(By.NAME, "billingLocality").send_keys("ny city")
postal_code = driver.find_element(By.NAME, "billingPostalCode").send_keys("96522")
billing_administrative_area = driver.find_element(By.NAME, "billingAdministrativeArea").send_keys("Tamil Nadu")
pay_submit = driver.find_element(By.CLASS_NAME, "SubmitButton-IconContainer").click()
back_opt = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/header/div/div/a/div/div/div[2]/div/span")
actions = ActionChains(driver)
actions.double_click(on_element=back_opt)
actions.perform()
alert = Alert(driver)
alert.accept()
# alert.dismiss()
# driver.find_element(By.XPATH, "//span[text()='Back']").click()

# pay_submit.click()

# driver.back()
# driver.back()
# driver.back()



# billing_country = driver.find_element(By.ID, "billingCountry")
# billing_country.click()
# billing_country_object = Select(billing_country)
# billing_country_object.select_by_index(0)
# billing_country_object.click()






#Navigate to App store Page
# app_store_home = driver.find_element(By.LINK_TEXT, "App Store")
# app_store_home.click() 

# self_installer_home_page = driver.find_element(By.LINK_TEXT, "Selfinstaller")
# self_installer_home_page.click()

#code logout start
logo_click = driver.find_element(By.ID, "profile_img")
logo_click.click()
logout_element = driver.find_element(By.ID, "logout")
print(logout_element)
logout_element.click()
action = ActionChains(driver)
#code logout end


