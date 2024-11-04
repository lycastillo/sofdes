import streamlit as st

st.set_page_config(layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "welcome"
if "name" not in st.session_state:
    st.session_state.name = ""
if "selected_module" not in st.session_state:
    st.session_state.selected_module = None

def welcome_page():
    st.markdown(
        """
        <style>
        .main {
            background-color: #FFFFFF;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align: center; color: #4682B4;'>Welcome Learner!</h1>", unsafe_allow_html=True)
    name = st.text_input("What is your name?", "")

    if st.button("Continue"):
        st.session_state.name = name  
        st.session_state.page = "selection"  

def selection_page():
    st.markdown(
        """
        <style>
        .main {
            background-color: #FFFFFF;
        }
        .center-text {
            text-align: center;
            margin-top: 20px;
        }
        .center-button {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .card {
            text-align: center;
            padding: 20px;
            border-radius: 10px;
            background-color: #FFEBCC;
            border: 2px solid #FFB74D;
            color: #000000;
            font-family: Arial, sans-serif;
            height: 240px;
            position: relative;
        }
        .card-title {
            font-size: 16px;
            font-weight: bold;
            color: #333333;
            margin-bottom: 10px;
        }
        .card-content {
            font-size: 13px;
            color: #666666;
            line-height: 1.4;
        }
        .button-wrapper {
            display: flex;
            justify-content: center;
            margin-top: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"<h1 style='text-align: center;'>Hi, {st.session_state.name}!</h1>", unsafe_allow_html=True)
    st.markdown("<div class='center-text'>Choose your desired module and mode of difficulty.</div>", unsafe_allow_html=True)

    modules = {
        "A": ("PRE-K - Kinder", "CVC Words<br>Sight Words<br>Color Words<br>Shape Words<br>Animal Names"),
        "B": ("Grade 1", "High-Frequency Words<br>Simple Nouns<br>Action Words<br>Family Vocabulary<br>Basic Adjectives"),
        "C": ("Grade 2", "Synonyms and Antonyms<br>Expanded Vocabulary<br>Words Related to Seasons<br>Descriptive Adjectives<br>Word Families"),
        "D": ("Grade 3", "Academic Vocabulary<br>Context Clues Vocabulary<br>Homophones<br>Multi-Syllable Words<br>Topic-Specific Vocabulary")
    }

    
    cols = st.columns(len(modules))  

    for index, (key, (title, content)) in enumerate(modules.items()):
        with cols[index]:
            
            st.markdown("<div class='button-wrapper'>", unsafe_allow_html=True)
            if st.button(f"{title}", key=key):
                st.session_state.selected_module = key
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown(
                f"""
                <div class='card'>
                    <div class='card-title'>{title}</div>
                    <div class='card-content'>{content}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div class='center-button'>", unsafe_allow_html=True)
    if st.button("Get Started"):
        if st.session_state.selected_module:
            st.write(f"Starting Module {st.session_state.selected_module}...")  # Placeholder action
        else:
            st.warning("Please select a module before proceeding.")
    st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.page == "welcome":
    welcome_page()
elif st.session_state.page == "selection":
    selection_page()
