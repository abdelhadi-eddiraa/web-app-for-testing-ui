from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import string
import random
import time
import sys


browser = webdriver.Firefox()
browser.get('https://erp-integraltech.onrender.com/auth')


# Function to generate a random string of given length
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))





# Wait for the login input field to be visible
login_input = WebDriverWait(browser, 30).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]'))
)
login_input.send_keys('superadmin')

# Wait for the password input field to be visible
pass_input = WebDriverWait(browser, 30).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
)
pass_input.send_keys('password')

continue_button = browser.find_element(
    By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/form/button')
continue_button.click()

##############################################################################################################

# Wait for the page to load after login (adjust the timeout as needed)
WebDriverWait(browser, 30).until(
    EC.url_contains('https://erp-integraltech.onrender.com/dashboard')
)

# Now you can interact with elements on the new page
# enter the DDB
DDB_select = WebDriverWait(browser, 20).until(
    EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="logo-sidebar"]/div/ul/li[2]/button'))
)
DDB_select.click()
# enter USER_MANAGEMENT
USER_management = WebDriverWait(browser, 30).until(
    EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[2]/main/aside/div/ul/li[2]/ul/li[1]/button'))
)
USER_management.click()

# enter in the user element
user = WebDriverWait(browser, 30).until(
    EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[2]/main/aside/div/ul/li[2]/ul/li[1]/ul/li[1]'))
)
user.click()



######################################################################################################################
############################################### the user model  ##############################################
###################################################################################################################
# the search bar
###################################################################################################################
# Wait for the page to load after login (adjust the timeout as needed)
WebDriverWait(browser, 30).until(
    EC.url_contains(
        'https://erp-integraltech.onrender.com/ddb/users-management/users')
)

# Enter a value of 'admin'
search_input = WebDriverWait(browser, 30).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="table-search"]'))
)
# search_input.send_keys('admin')  # Use a value that you know won't match


# time.sleep(2)

# Wait for the table body (tbody) to be visible
try:
    tbody_element = WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[2]/main/div/div[2]/div[2]/table/tbody'))
    )

    # Locate all paragraph elements (assuming they are enclosed in <p> tags)
    paragraphs = tbody_element.find_elements(By.TAG_NAME, 'p')

    matching_text_found = False
    # Extract and print the text from each paragraph
    for paragraph in paragraphs:
        if search_input.get_attribute("value") in paragraph.text:
            matching_text_found = True
            print("matching was found")
            break

except TimeoutException:
    matching_text_found = False

# Now check if matching_text_found is False and the "No content was found" message is displayed
if not matching_text_found:
    try:
        no_data_was_found = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="root"]/main/div/div[2]/div[2]/div/h3'))
        )
        assert no_data_was_found.is_displayed(), "No content was found"
        print("No content was found")
    except TimeoutException:
        print(
            "Matching text not found, and 'No content was found' message is not displayed.")
########################################################################################################################
################ add user ####################################################
#######################################################################################

add_user=WebDriverWait(browser,30).until(
    EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/main/div/div[1]/div[2]/button'))
)

add_user.click()
#get the form that has all inputs
form_element = WebDriverWait(browser, 30).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/section/div/div/form'))
)

# Get all input elements inside the form
popup_inputs = form_element.find_elements(By.TAG_NAME, 'input')

values_in_order = [
    'Username Value',
    'Email@gmail.com',
    'password',
    'password',
]

def switch_case(case):
    if case < len(values_in_order):
        return values_in_order[case]
    else:
        return 'out of range'

for key, value in enumerate(popup_inputs, start=1):
    print(key, switch_case(key - 1), value.get_attribute('id'))
    if key <= len(values_in_order):
        value.send_keys(switch_case(key - 1))
    else:
        break


################################################################################################################
#teh select opyion
time.sleep(2)
select_poupup=WebDriverWait(browser,30).until(
        EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div/div/div/div[2]/section/div/div/form/div[5]/select')))
all_options = select_poupup.find_elements(By.TAG_NAME, "option")


select_poupup.click()
for option in all_options:
    option.send_keys(Keys.ARROW_DOWN)
    # Simulate pressing Enter to select the option
    option.click()
######################################################################################################################
# the add user button


add_button_user=WebDriverWait(browser,30).until(
        EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div/div/div/div[2]/section/div/div/form/button'
)))

    
try:
    add_button_user.click()
    error_message_element = WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/section/div/div/form/div[1]/div'))
    )
    error_message = error_message_element.text

    while True :
        if "The username has already been taken. (and 1 more error)" in error_message:
            username_input = WebDriverWait(browser, 30).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]'))
            )
            random_number = random.randint(1, 40)
            new_username = values_in_order[0] + str(random_number)  # Convert the random number to a string
            username_input.clear()  # Clear the existing input
            username_input.send_keys(new_username)
            add_button_user.click()
            #whait for the text error to change and then move to the next line
            # Wait for the error message text to change
            while True:
                if error_message_element.text == "The email has already been taken."  :
                    email_input = WebDriverWait(browser, 30).until(
                        EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]'))
                        )
                    random_name = generate_random_string(8)
                    email_parts = values_in_order[1].split("@")
                    new_email = f"{random_name}@{email_parts[1]}"
                    email_input.clear()
                    email_input.send_keys(new_email)
                    add_button_user.click()
                    break
except TimeoutError:
    print('you cannot go outside the form')







    

#################################################################################################################
########################################### delete a user      ################################################
#################################################################################################################

search_input.clear()
search_input.send_keys(new_username)
#whait for the model to dispire and click delete button
WebDriverWait(browser, 30).until_not(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[1]'))
)
delete_button_user=WebDriverWait(browser,30).until(
             EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/main/div/div[2]/div[2]/table/tbody/tr/td[4]/div/button[2]'
)))

delete_button_user.click()

confirm_delete_button=WebDriverWait(browser,30).until(
             EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[2]/section/div/div/div[2]/button[1]'
)))
confirm_delete_button.click()

search_input.clear()

time.sleep(2)

browser.quit()


       

