import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

# Load the Environment
load_dotenv()     

# Configure te GenAI Secret Key
genai.configure(api_key = os.getenv("GOOGLE-API-KEY"))

# Design the Page
st.title('Image to Text Application')
user_input = st.text_input('Input Prompt:')
uploaded_file = st.file_uploader('Upload the Image', type = ['jpg','jpeg','png'])

# The following codes are to create sidebar, title it, and its drop down menus with its names
# st.sidebar.title('Model Diagnostics')
# st.sidebar.markdown('Click to know more')
# uni_analysis = st.sidebar.button('Univariate Analysis')

# Display image on the web page (that is being uploaded)
img = ''
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption = 'Uploaded Image', use_column_width = True)
    
# Function for evaluating the Image and Annotate it
def gemini_response(user_input, img):
    model = genai.GenerativeModel('gemini-1.5-flash')       # gemini-1.5-flash is good for images
    if user_input!='':
        response = model.generate_content([user_input, img])
    else:
        response = model.generate_content(img)
    return response.text

# Creating the Click Button
submit = st.button('Submit')  

if submit:
    response = gemini_response(user_input = user_input, img = img)
    st.subheader('The Response is:')
    st.write(response)
    