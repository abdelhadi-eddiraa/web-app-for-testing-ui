import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import json

st.set_page_config(page_title="my seet home alabama",page_icon=":eye:",layout="wide")

with open("Astronaut with space shuttle.json","r") as f:
     astronaut = json.load(f)
def local_css(file_name):
      with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("styles/style.css")
# img_contact=Image.open("public\media\avatars\300-1.jpg")

# ----header section -------
with st.container():
     st.subheader("hi i'm abel")
     st.title("A Web developper from ...")
     st.write("hello world")
     st.write("[learn MO >](https://www.webfx.com/tools/emoji-cheat-sheet/)")


#-----what i do-----
with st.container():
     st.write("---")
     left_column,right_column=st.columns(2)
     with left_column:
          st.header("What I do")
          st.write("##")
          st.write(""" 
           from selenium import webdriver

selenium_grid_url = "http://198.0.0.1:4444/wd/hub"
 Create a desired capabilities object as a starting point.
capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities['platform'] = "WINDOWS"
capabilities['version'] = "10"
 Instantiate an instance of Remote WebDriver with the desired capabilities.
driver = webdriver.Remote(desired_capabilities=capabilities,
                          command_executor=selenium_grid_url)
                   
""")
     with right_column:
        st_lottie(astronaut,height=300,key="astro") 
          

#--------- projects--
with st.container():
     st.write("---")
     st.header("My project")
     st.write("##")
     image_column,text_column=st.columns((1,2))
     with image_column:
                  st_lottie(astronaut,height=300,key="astrpo") 

     with text_column:
          st.subheader("Integral lotties animation")
          st.write("""
            with selenium.context(selenium.CONTEXT_CHROME):
            # chrome scope
            ... do stuff ...
            """)
          st.markdown("[Watch Video....](https://www.youtube.com/watch?v=VqgUkExPvLY)")
          


with st.container():
     st.write("---")
     st.header("My project")
     st.write("##")
     image_column,text_column=st.columns((2,1))
    

     with text_column:
          st.subheader("Integral lotties animation")
          st.write("""
            with selenium.context(selenium.CONTEXT_CHROME):
            # chrome scope
            ... do stuff ...
            """)
          st.markdown("[Watch Video....](https://www.youtube.com/watch?v=VqgUkExPvLY)")
     with image_column:
                  st_lottie(astronaut,height=300,key="astddrpo") 
          


#----contact
with st.container():
      st.write("---")
      st.header("get In touch")
      st.write("##")
      contact_form="""<form action="https://formsubmit.co/your@email.com" method="POST">
         <input type="text" name="name" required>
         <input type="email" name="email" required>
          <button type="submit">Send</button>
          </form>"""
      left_column,right_column=st.columns(2)
      with left_column:
            st.markdown(contact_form,unsafe_allow_html=True)
      with right_column:
        st.empty()
 

      