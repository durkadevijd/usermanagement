from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://opensource-demo.orangehrmlive.com/"
driver = webdriver.Chrome()

# Login Start
username = "Admin"
password = "admin123"

username_xpath = '//*[@name="username"]'
password_xpath = '//*[@name="password"]'
login_button_xpath = '//button[@type="submit"]'

driver.get(url)
username_elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, username_xpath)))

password_elem = driver.find_element(by=By.XPATH, value=password_xpath)
login_button_elem = driver.find_element(by=By.XPATH, value=login_button_xpath)
username_elem.send_keys(username)
password_elem.send_keys(password)
login_button_elem.click()
# Login End

# Navigate to PIM
pim_link_xpath = '//ul[@class="oxd-main-menu"]/li[2]/a'

pim_elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, pim_link_xpath)))

pim_elem.click()

# Add PIM User
add_xpath = '//div[@class="orangehrm-header-container"]/button[@type="button"]'

add_btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, add_xpath))
)

add_btn.click()

firstname_xpath = '//input[@name="firstName"]'

firstname_elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, firstname_xpath))
)

time.sleep(2)

middlename_xpath = '//input[@name="middleName"]'
lastname_xpath = '//input[@name="lastName"]'
save_emp_xpath = '//button[@type="submit"]'

middlename_elem = driver.find_element(by=By.XPATH, value=middlename_xpath)
lastname_elem = driver.find_element(by=By.XPATH, value=lastname_xpath)
save_emp_elem = driver.find_element(by=By.XPATH, value=save_emp_xpath)

firstname_elem.send_keys("Durka")
middlename_elem.send_keys("Devi")
lastname_elem.send_keys("Jayaseelan")

save_emp_elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, save_emp_xpath))
)

save_emp_elem.click()

# Verify PIM user is added
header_xpath = '//div[@class="orangehrm-edit-employee-name"]/h6'
header_elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, header_xpath))
)

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, header_xpath), 'Durka Jayaseelan')
)
print(driver.find_element(By.XPATH, header_xpath).text)

# Navigating to Admin 
admin_link_xpath = '//*[@class="oxd-main-menu"]/li[1]/a'
admin_link_elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, admin_link_xpath))
)

admin_link_elem.click()

# Create admin user
search_btn_xpath = '//button[@type="submit" and contains(.,"Search")]'

def WaitForElem(driver, xpath):
    return WebDriverWait(driver, 10).until((
        EC.presence_of_element_located((By.XPATH, xpath))
    ))

search_btn_elem = WaitForElem(driver, search_btn_xpath)
admin_add_btn_xpath = '//button[@type="button" and contains(.,"Add")]'
admin_add_btn_elem = driver.find_element(by=By.XPATH, value=admin_add_btn_xpath)
admin_add_btn_elem.click()

add_admin_user_xpath = '//h6[text()="Add User"]'
WaitForElem(driver, add_admin_user_xpath)


userrole_elem = driver.find_element(By.XPATH, '//form[@class="oxd-form"]//div[contains(@class,"oxd-select-text")][1]')
userrole_elem.click()

userrole_dropdown_xpath = '//form[@class="oxd-form"]//div[contains(@class,"oxd-select-text")][1]/../div[@role="listbox"]'
WaitForElem(driver, userrole_dropdown_xpath)

ess_role_xpath = '//form[@class="oxd-form"]//div[contains(@class,"oxd-select-text")][1]/../div[@role="listbox"]/div[3]'
driver.find_element(By.XPATH, ess_role_xpath).click()

emp_name_xpath = '//form[@class="oxd-form"]//div[contains(@class,"oxd-grid-item")][2]//div[contains(@class,"oxd-autocomplete-text-input")]/input'
emp_name_elem = driver.find_element(By.XPATH, emp_name_xpath)
emp_name_elem.send_keys("Durka devi Jayaseelan")

emp_name_dropdown_xpath = '//form[@class="oxd-form"]//div[contains(@class,"oxd-grid-item")][2]//div[contains(@class,"oxd-autocomplete-text-input")]/../div[@role="listbox"]'
WaitForElem(driver, emp_name_dropdown_xpath)
emp_name_option_xpath = '//form[@class="oxd-form"]//div[contains(@class,"oxd-grid-item")][2]//div[contains(@class,"oxd-autocomplete-text-input")]/../div[@role="listbox"]/div[1]/span'
emp_name_option_sel_xpath = '//form[@class="oxd-form"]//div[contains(@class,"oxd-grid-item")][2]//div[contains(@class,"oxd-autocomplete-text-input")]/../div[@role="listbox"]/div[1]/span'
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, emp_name_option_sel_xpath), 'Durka Devi Jayaseelan')
)
emp_name_elem = driver.find_element(By.XPATH, emp_name_option_xpath)
emp_name_elem.click()

status_dropdown_xpath = '//form[@class="oxd-form"]//div[contains(@class,"oxd-grid-item")][3]//div[contains(@class,"oxd-select-text")]'
status_elem = driver.find_element(By.XPATH, status_dropdown_xpath)
status_elem.click()

status_dropdown_option_xpath = '//form[@class="oxd-form"]//div[contains(@class,"oxd-grid-item")][3]//div[contains(@class,"oxd-select-text")]/../div[@role="listbox"]'
WaitForElem(driver, status_dropdown_option_xpath)

enable_status_xpath = '//form[@class="oxd-form"]//div[contains(@class,"oxd-grid-item")][3]//div[contains(@class,"oxd-select-text")]/../div[@role="listbox"]/div[2]'
driver.find_element(By.XPATH, enable_status_xpath).click()

admin_username_xpath = '//form[@class="oxd-form"]//div[contains(@class,"oxd-grid-item")][4]//input[contains(@class,"oxd-input")]'
admin_password_xpath = '//form[@class="oxd-form"]//div[contains(@class,"user-password-row")]//div[contains(@class,"oxd-grid-item")][1]//input[contains(@class,"oxd-input")]'
admin_confirm_password_xpath = '//form[@class="oxd-form"]//div[contains(@class,"user-password-row")]//div[contains(@class,"oxd-grid-item")][2]//input[contains(@class,"oxd-input")]'

admin_save_xpath = '//form[@class="oxd-form"]//div[contains(@class,"oxd-form-actions")]/button[@type="submit"]'

driver.find_element(By.XPATH, admin_username_xpath).send_keys('durkadevi')
time.sleep(1)
driver.find_element(By.XPATH, admin_username_xpath).send_keys('')

driver.find_element(By.XPATH, admin_password_xpath).send_keys('Puppy@123')
driver.find_element(By.XPATH, admin_confirm_password_xpath).send_keys('Puppy@123')
time.sleep(1)
driver.find_element(By.XPATH, admin_save_xpath).click()
time.sleep(3)

# Verify created admin user
admin_filter_xpath = '//div[@class="oxd-table-filter"]'
WaitForElem(driver, admin_filter_xpath)

username_search_xpath = '//form[@class="oxd-form"]//div[contains(@class,"oxd-grid-item")][1]//input'
username_elem = WaitForElem(driver, username_search_xpath)

username_elem.send_keys('durkadevi')

submit_search_xpath = '//form[@class="oxd-form"]//button[@type="submit"]'
submit_search_elem = driver.find_element(By.XPATH, submit_search_xpath)

submit_search_elem.click()
time.sleep(2)

admin_table_row_xpath = '//div[@class="oxd-table"]//div[contains(@class,"oxd-table-body")]//div[contains(@class,"oxd-table-row")][1]/div[2]/div'
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, admin_table_row_xpath),"durkadevi")
)

admin_table_username_elem = driver.find_element(By.XPATH, admin_table_row_xpath)

print(admin_table_username_elem.text)

# Logout
user_menu_xpath = '//header//span[@class="oxd-userdropdown-tab"]'
user_menu_elem = driver.find_element(By.XPATH, user_menu_xpath)
user_menu_elem.click()

logout_xpath = '//header//ul[@class="oxd-dropdown-menu"]/li[4]/a'
WaitForElem(driver, logout_xpath)

logout_elem = driver.find_element(By.XPATH, logout_xpath)
logout_elem.click()


# Login with created user

username_elem = WaitForElem(driver, username_xpath)
password_elem = driver.find_element(by=By.XPATH, value=password_xpath)
login_button_elem = driver.find_element(by=By.XPATH, value=login_button_xpath)
username_elem.send_keys('durkadevi')
password_elem.send_keys('Puppy@123')
login_button_elem.click()

# Verify user logged in by checking dashboard text
dashboard_text_xpath = '//header//span[@class="oxd-topbar-header-breadcrumb"]/h6'
WaitForElem(driver, dashboard_text_xpath)
print("logged in")


time.sleep(5)

driver.close()
