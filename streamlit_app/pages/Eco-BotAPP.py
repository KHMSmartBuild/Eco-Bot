# script location:streamlit_app/pages/Eco-BotAPP.py
"""
Script name: Eco-BotAPP.py
Author: Kyle
Company: KHM Smart Build
Description: Hybrid version of the Eco-Bot MVP Streamlit app.
Date: 2023-05-10
Version: 1.0

This is a simple Eco-Bot chat bot that uses OpenAI's GPT-4-1106 preview model
"""
import sys
import datetime
import os
# Append the parent directory to sys.path
sys.path.append('../')
from eco_buddies.eco_chat import EcoBot
from icecream import ic
import logging
import streamlit as st

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
    """
    A function that loads an image from the specified image path.

    Parameters:
    - image_path (str): The path to the image file.

    Returns:
    - bytes: The contents of the image file as bytes.
    - None: If the image file is not found, an error message is displayed and None is returned.
    """
    try:
        return open(image_path, "rb").read()
    except FileNotFoundError:
        st.error(f"Error: Image not found at {image_path}")
        return None

# Main App Function
def main():
    """
    Function to run the main Eco-Bot application.
    
    This function displays the app header, an image of the Eco-Bot, and a sidebar navigation menu. 
    The user can select a page from the menu, which will then be displayed. If the user clicks the 'Close App' button, 
    the function raises a SystemExit exception to close the app.
    
    Parameters:
        None
    
    Returns:
        None
    """
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
    """
    Function to render the home page of the Eco-Bot application.
    
    This function displays a welcome message and provides a chatbot interface for the user to interact with Eco-Bot.
    
    Parameters:
        None
        
    Returns:
        None
    """
    st.write("Welcome to Eco-Bot! Let's make eco-friendly choices together.")
    
    # Chatbot Interface
    user_input = st.text_input("Ask Eco-Bot a question:")
    
    if user_input:
        # Using GMA to enhance the response
        response = ecobot_chat.generate_response(user_input)
        st.write(f"Eco-Bot: {response}")
        ic(response)

# GBTS Interaction Page
def gbts_interaction_page():
    """
    A function that displays the Gaia-Bohm Thought Style (GBTS) interaction page.

    Parameters:
    None

    Returns:
    None
    """
    st.write("Explore the Gaia-Bohm Thought Style (GBTS) interaction here.")
    # ... additional code for GBTS interaction

# Eco-Buddies Page
def eco_buddies_page():
    """
    Display and update the Eco-Buddies page.

    This function is responsible for displaying and updating the Eco-Buddies page. It uses the `st.write` function to display the message "Meet your Eco-Buddies!" on the page. The page content is then updated with the necessary code for displaying and updating the Eco-Buddies.

    Parameters:
    None

    Returns:
    None
    """
    st.write("Meet your Eco-Buddies!")
    # ... code for displaying and updating Eco-Buddies

# Settings Page
def settings_page():
    """
    Displays the settings page.

    This function is responsible for rendering and updating the settings page. It utilizes the `st.write` function to display the message "Configure your settings." The code for displaying and updating the settings is implemented here.

    Parameters:
    None

    Returns:
    None
    """
    st.write("Configure your settings.")
    # ... code for displaying and updating settings
    with st.expander("Expand me!"):
        st.write("More settings...")

# Run the app
if __name__ == "__main__":
    main()
