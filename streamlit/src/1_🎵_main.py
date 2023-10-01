import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import json
import os

st.set_page_config(page_title="my seet home alabama",page_icon=":eye:",layout="wide")

# Get the path to the wired-lineal-56-document.json file
file_path = os.path.join(os.path.dirname(__file__), "wired-lineal-56-document.json")

# Open the file and load it into a Python object
with open(file_path, "r") as f:
    testing = json.load(f)

st.markdown(
    """
    <div style="background-color: #ff6666;border-radius: 10px;color: white; padding: 10px; text-align: center;">
        This app requires Firefox browser.
    </div>
    """,
    unsafe_allow_html=True
)

with st.container():
   left_column,right_column=st.columns(2)
   with left_column:
       st.title("My testing UI App")
       st.write("This UI testing app is a UI testing app for UI testing apps. It allows you to test the UI of your UI testing app without having to deploy it to production.Testimonials:This app is a lifesaver! It saved me so much time and hassle testing the UI of my UI testing app.This app is amazing! It's so easy to use, and it's really helped me improve the quality of my UI testing apps.")
   with right_column:
       st_lottie(testing,height=300,key="testing_id")


####################################################################################
# add a side bar
##########################################################################
# Using object notation
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# # Using "with" notation
# with st.sidebar:
#     st.danger("Thank you for using our Selenium Login Test application!")

       
     



