# Script name: Eco-BotAPP.py
# Author: Kyle
# Company: KHM Smart Build
# Description: Hybrid version of the Eco-Bot MVP Streamlit app.
# Date: 2023-05-10

import sys

# Append the parent directory to sys.path
sys.path.append('C:/Users/User/OneDrive/Desktop/Buisness/KHM Smart Build/Coding/Projects/OCFS_projects/Eco-Bot/')

import streamlit as st
from icecream import ic
from eco_buddies.eco_bot_chat import EcoBot

# Streamlit App Configuration
st.set_page_config(
    page_title="Eco-Bot",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize the EcoBot and GeneralManagerAgent
ecobot_chat = EcoBot()


# Utility Functions
@st.cache
def load_image(image_path):
    try:
        return open(image_path, "rb").read()
    except FileNotFoundError:
        st.error(f"Error: Image not found at {image_path}")
        return None

# Main App Function
def main():
    # App Header
    st.title("Eco-Bot")
    st.write("Welcome to the Eco-Bot app! Here, we integrate nature with technology.")
    
    # Display Eco-Bot Image
    eco_bot_image = load_image("assets/images/eco-bot.png")
    if eco_bot_image:
        st.image(eco_bot_image, caption="Eco-Bot", use_column_width=False, width=200)

    # Sidebar Navigation
    st.sidebar.header("Menu")
    page = st.sidebar.radio("Select a page:", ["Home", "GBTS Interaction", "Eco-Buddies", "Settings"])

    if page == "Home":
        home_page()
    elif page == "GBTS Interaction":
        gbts_interaction_page()
    elif page == "Eco-Buddies":
        eco_buddies_page()
    elif page == "Settings":
        settings_page()
    if st.button('Close App'):
        raise SystemExit("The app was closed by the user.")

# Home Page
def home_page():
    st.write("Welcome to Eco-Bot! Let's make eco-friendly choices together.")
    
    # Chatbot Interface
    user_input = st.text_input("Ask Eco-Bot a question:")
    
    if user_input:
        # Using GMA to enhance the response
        response = ecobot_chat.handle_input(user_input)
        st.write(f"Eco-Bot: {response}")

# GBTS Interaction Page
def gbts_interaction_page():
    st.write("Explore the Gaia-Bohm Thought Style (GBTS) interaction here.")
    # ... additional code for GBTS interaction

# Eco-Buddies Page
def eco_buddies_page():
    st.write("Meet your Eco-Buddies!")
    # ... code for displaying and updating Eco-Buddies

# Settings Page
def settings_page():
    st.write("Configure your settings.")
    # ... code for displaying and updating settings

# Run the app
if __name__ == "__main__":
    main()
