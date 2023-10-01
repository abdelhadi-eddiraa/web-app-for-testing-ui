from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import string
import random
import time
import sys
import pygetwindow as gw
import requests



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

WebDriverWait(browser, 30).until(
    EC.url_contains(
        'https://erp-integraltech.onrender.com/dashboard')
)

try:
    # Wait for the element to be visible
    button_hover = browser.find_element(By.XPATH,'/html/body/div[2]/nav/div/button')
    actions = ActionChains(browser)
    actions.move_to_element(button_hover).perform()
    # print('dine right')

    dropdown=WebDriverWait(browser,30).until(
        EC.visibility_of_element_located((By.ID,'user-dropdown'))
    )

    hrefs=dropdown.find_elements(By.TAG_NAME,'a')
    if hrefs:
       last_href = hrefs[-1]
       last_href.click()
    else:
        print("No 'a' elements found in the dropdown.")
except TimeoutException:
    print("Timeout: Element not found within the specified time.")
except NoSuchElementException:
    print("Element not found.")


time.sleep(2)

browser.quit()