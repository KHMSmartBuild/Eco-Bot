# Script name: Eco-BotAPP.py
# Author: Kyle
# Company: KHM Smart Build
# Description: Hybrid version of the Eco-Bot MVP Streamlit app.
# Date: 2023-05-10
import streamlit as st
from icecream import ic
import logging
import os
import datetime
import sys

# Append the parent directory to sys.path
sys.path.append('C:/Users/User/OneDrive/Desktop/Buisness/KHM Smart Build/Coding/Projects/OCFS_projects/Eco-Bot/')

from eco_buddies.eco_bot_chat import EcoBot

# Configure icecream to save output to a file in the debug folder
def setup_icecream_debugging():
    debug_folder = "debug"
    if not os.path.exists(debug_folder):
        os.makedirs(debug_folder)
    debug_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Renamed variable
    debug_file = os.path.join(debug_folder, f"debug_{debug_timestamp}.txt")  # Use the renamed variable
    with open(debug_file, "a+", encoding="utf-8") as debug_file_handle:
        ic.configureOutput(outputFunction=lambda s: debug_file_handle.write(s + '\n'))

# Call this function at the beginning of your script or before you start logging
setup_icecream_debugging()

# Setup logging
log_folder = "logs"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)
log_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Renamed variable
log_file = os.path.join(log_folder, f"log_{log_timestamp}.txt")  # Use the renamed variable

# Configure the logging module to save logs to the log file
log_format = '%(asctime)s - %(levelname)s - Eco-Bot Chat - %(message)s'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format=log_format)

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
@st.cache_data
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
