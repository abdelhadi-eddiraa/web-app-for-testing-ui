import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json
import subprocess

# Set page title, icon, and layout
st.set_page_config(
    page_title="Selenium Login Test",
    page_icon=":unlock:",
    layout="wide"
)

# Load your Lottie animation
lottie_animation = "C:\\Users\\Destock\\Downloads\\Astronaut with space shuttle.json"

# Main title and description
st.title("Selenium Permissions Test")
st.markdown("Welcome to the Selenium Permissions Test. This automated test will perform a login operation on your website. "
            "Click the button below to start the test.")

# Create a button to start the test
if st.button("Start Selenium Permissions Test", key="start_button", type="primary"):
    # Use subprocess to run the login test script
    result = subprocess.run(["python", "C:\\Users\\Destock\\Desktop\\frontend-integral\\integral-tech-front-end-from-zero\\py\\streamlit\\src\\tests\\loginTest.py"], capture_output=True)

    # Check if the test script was successful
    if result.returncode == 0:
        # Execute a request to check the test results
        response = requests.post('https://erp-integraltech.onrender.com/auth')
        
        if response.status_code == 200:
            st.success("Selenium test passed successfully. Status Code: 200")
        else:
            st.error(f"Selenium test failed. Unexpected Status Code: {response.status_code}")
    else:
        st.error("Selenium test failed")

# Lottie animation
st_lottie(lottie_animation, height=400)

# Additional content
st.header("Additional Information")
st.markdown("Here are some details about the Selenium login test:")

# Test steps with accordion
with st.expander("Test Steps"):
    st.markdown("1. Navigate to the login page.")
    st.markdown("2. Enter valid credentials.")
    st.markdown("3. Click the 'Login' button.")
    st.markdown("4. Verify if the login is successful.")

# Test results with interactive chart
with st.expander("Test Results"):
    st.markdown("After the test is complete, the results will be displayed here.")
    st.line_chart({"data": [1, 2, 3, 4, 5]})

# Contact information
st.header("Contact Information")
st.markdown("If you encounter any issues or have questions, please contact our support team at support@example.com.")

# Footer
st.info("Thank you for using our Selenium Login Test application!")




#########################################################################


