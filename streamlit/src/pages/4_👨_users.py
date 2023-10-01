import streamlit as st
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
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import json
import os
import subprocess

st.set_page_config(page_title="my seet home alabama",
                   page_icon=":eye:", layout="wide")

##########################################################################
file_path = "C:\\Users\\Destock\\Downloads\\Astronaut with space shuttle.json"

with open(file_path, "r") as f:
    menu = json.load(f)
##############################################################################

login_test_url = r'C:\Users\Destock\Desktop\frontend-integral\integral-tech-front-end-from-zero\py\streamlit\src\tests\usersTest.py'
# login_url_site=r'https://erp-integraltech.onrender.com/auth'

def execute_user_test():
    # Use subprocess to run the other script as a separate process
    result = subprocess.run(["python", login_test_url])
    
    if result.returncode == 0:
        # Check the response of the test URL
        response = requests.post('https://erp-integraltech.onrender.com/auth')
        if response.status_code == 200:
            success_message = st.success("Selenium test passed successfully. Status Code: 200")
            # time.sleep(8)  # Wait for 5 seconds
            # success_message.empty() 
        else:
            st.error(f"Selenium test failed. Unexpected Status Code: {response.status_code}")
        # st.success("Selenium test passed successfully")
    else:
        st.error("Selenium test failed")
   
    


####################################################################################
############# the login selinuem logig################################
# Get the URL parameters


def start_user_test():
    execute_user_test()


##################################################################################
          ############ import svg #################################


#################################################################################
       ######### the embede fream for the test #############################
# Define the URL of the webpage you want to embed
embedded_url = "https://erp-integraltech.onrender.com/auth"
with st.container():
    left_column, right_column = st.columns((1, 2))
    with left_column:
        # Set the title of the page
        st.title("Users")
        # Add a brief description of what the page does
        st.write("This page allows you to start a Selenium test.")
        # Add a button to start the test
        st.button("Start Selenium users Test", type="primary",on_click=start_user_test)
        # Add a button to the page
    with right_column:
        st_lottie(menu, height=300, key="menu")
######################################################################################
