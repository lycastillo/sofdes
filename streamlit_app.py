import streamlit as st
from PIL import Image

# Load the background image
background_image_path = 'Desktop - 2.png'  # Adjust the path if needed
background_image = Image.open(background_image_path)

# Set up Streamlit app layout
st.set_page_config(layout="centered")

# Display background image with Streamlit's `st.image`
st.image(background_image, use_column_width=True)

# Add welcome text
st.markdown("<h1 style='text-align: center; color: #4682B4;'>Welcome Learner!</h1>", unsafe_allow_html=True)

# Input box for user to enter their name
name = st.text_input("What is your name?", "")

# Continue button
if st.button("Continue"):
    st.write(f"Hello, {name}! Welcome to the learning platform.")
