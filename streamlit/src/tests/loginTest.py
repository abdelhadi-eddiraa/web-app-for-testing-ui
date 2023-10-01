from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import string
import random
import time
import sys
import pygetwindow as gw


options = webdriver.FirefoxOptions()
options.add_argument('--new-tab')
browser = webdriver.Firefox(options=options)




browser.get('https://erp-integraltech.onrender.com/auth')




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

time.sleep(5)

browser.quit()

# # Switch to the original tab (the first tab)
# browser.switch_to.window(all_handles[0])
# time.sleep(5)
# browser.get('http://localhost:8501/login')
