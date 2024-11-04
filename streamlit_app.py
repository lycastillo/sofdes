import streamlit as st
import random
from PIL import Image
import pytesseract
import re

words = ["apple", "banana", "grape", "orange", "watermelon", "strawberry", "blueberry"]

if "page" not in st.session_state:
    st.session_state.page = "welcome"
if "name" not in st.session_state:
    st.session_state.name = ""
if "selected_module" not in st.session_state:
    st.session_state.selected_module = None
if "target_word" not in st.session_state:
    st.session_state.target_word = None

def welcome_page():
    st.title("Welcome Learner!")
    name = st.text_input("What is your name?", "")
    if st.button("Continue"):
        st.session_state.name = name
        st.session_state.page = "selection"

def selection_page():
    st.title(f"Hi, {st.session_state.name}!")
    st.write("Choose your desired module and mode of difficulty.")
    modules = ["PRE-K - Kinder", "Grade 1", "Grade 2", "Grade 3"]

    for module in modules:
        if st.button(module):
            st.session_state.selected_module = module
            st.session_state.page = "spelling"

    st.write("Get Started")
    if st.button("Get Started"):
        if st.session_state.selected_module:
            st.session_state.page = "spelling"
        else:
            st.warning("Please select a module before proceeding.")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z]', '', text)
    return text.strip()

def spelling_page():
    if st.session_state.target_word is None:
        st.session_state.target_word = random.choice(words)

    st.title("Spelling Challenge")
    st.write(f"Please spell the word: **{st.session_state.target_word}**")

    uploaded_image = st.file_uploader("Upload an image of your spelling", type=["png", "jpg", "jpeg"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        extracted_text = pytesseract.image_to_string(image)
        
        cleaned_extracted_text = clean_text(extracted_text)
        cleaned_target_word = clean_text(st.session_state.target_word)

        st.write("Extracted Text from Image:", extracted_text)
        st.write("Cleaned Extracted Text:", cleaned_extracted_text)

        if cleaned_extracted_text == cleaned_target_word:
            st.success("Correct! You spelled the word correctly.")
        else:
            st.error("Incorrect spelling. Please try again.")

if st.session_state.page == "welcome":
    welcome_page()
elif st.session_state.page == "selection":
    selection_page()
elif st.session_state.page == "spelling":
    spelling_page()
