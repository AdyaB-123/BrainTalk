import streamlit as st
from home import show_home_page
from about import show_about_page
from faq_resources import show_faq_resources_page

# Constants
IMAGE_ADDRESS = "https://www.tsukuba.ac.jp/en/research-news/images/p20230904180000.jpg"

# Page config
st.set_page_config(
    page_title="BrainTalk - EEG to Speech",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Us", "FAQ & Resources"])

# Header - always show the header
st.image(IMAGE_ADDRESS, caption="EEG to Speech Conversion")

# Show content based on selected page
if page == "Home":
    show_home_page()
elif page == "About Us":
    show_about_page()
elif page == "FAQ & Resources":
    show_faq_resources_page()
