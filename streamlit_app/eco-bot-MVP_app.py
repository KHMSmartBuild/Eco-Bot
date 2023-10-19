# Import necessary libraries and modules
import json
import streamlit as st
import sys
sys.path.append("..",)  # Append the parent directory to sys.path
import os

if not os.path.exists('path/to/file'):
    logging.error('File not found: path/to/file')
    sys.exit(1)  # Exit the script
from agents.autogen_agents import GeneralManagerAgent, Agent, DigitalTwinAgent, PromptTreeNode
from config import config_list_gpt4, llm_config
from icecream import ic
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=os.path.join(log_dir, 'app.log'),
    filemode='w'
)
# Now you can use logging.info(), logging.warning(), logging.error(), etc.


# Usage: ic(variable)





# Streamlit App Configuration
st.set_page_config(
    page_title="Eco-Bot",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load the Eco-Bot Image
@st.cache
def load_image(image_path):
    return open(image_path, "rb").read()

# Main App
def main():
    # Apply custom styles
    with open("streamlit_app/assets/styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # App Header
    st.title("Eco-Bot")
    st.write("Welcome to the Eco-Bot app! Here, we integrate nature with technology.")

    # Display Eco-Bot Image
    eco_bot_image = load_image("streamlit_app/assets/images/Eco_bot.png")
    st.image(eco_bot_image, caption="Eco-Bot", use_column_width=True)

    # Main Content Area
    st.subheader("About Eco-Bot")
    st.write("""
    Eco-Bot represents the harmonious blend of technology and nature. 
    It's our commitment to a sustainable future where technology complements nature.
    """)

    # User Interactions
    st.subheader("Interact with Eco-Bot")
    user_input = st.text_input("Ask Eco-Bot a question:")
    if user_input:
        # Placeholder for Eco-Bot's response logic
        st.write("Eco-Bot says: ...")  # Replace with actual response

    # Multi-Agent Chat Interface
    st.sidebar.header("Multi-Agent Chat Interface")

    # Agent 1
    st.sidebar.text("Agent 1")
    agent1_response = st.sidebar.text_area("Response:", value="")

    # Agent 2
    st.text("Agent 2 Reply")
    agent2_response = st.text_area("Response:", value="")

    # Imagery
    st.text("Imagery")
    imagery_upload = st.file_uploader("Upload an image or other visual items", type=["jpg", "png", "jpeg"])

    # Key Points - Meeting Minutes
    st.text("Key Points - Meeting Minutes")
    meeting_minutes = st.text_area("Topics:", value="")

    # Agent 3
    st.sidebar.text("Agent 3")
    agent3_response = st.sidebar.text_area("Response:", value="")

    # Agent 4
    st.text("Agent 4")
    agent4_response = st.text_area("Response:", value="")

    # Issues
    st.text("Issues")
    issues_covered = st.text_area("Issues Covered:", value="")
    issues_agreed = st.text_area("Issues Agreed:", value="")
    issues_pending = st.text_area("Issues Pending:", value="")

    # User chat or Prompt
    st.text("User chat or Prompt")
    user_chat = st.text_area("Type your message:", value="")

    # Optional: Add a button to send/save the chat
    send_button = st.button("Send")
    if send_button:
        st.write("Chat saved or sent!")

    # Navigation Sidebar
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

# Home Page
def home_page():
    st.write("Welcome to Eco-Bot! Let's make eco-friendly choices together.")

# GBTS Interaction Page
def gbts_interaction_page():
    st.write("Explore the Gaia-Bohm Thought Style (GBTS) interaction here.")
    # ... additional code for GBTS interaction

# Eco-Buddies Page
def eco_buddies_page():
    st.write("Meet your Eco-Buddies!")
    # ... code for displaying and interacting with Eco-Buddies

# Settings Page
def settings_page():
    st.write("Configure your settings.")
    # ... code for displaying and updating settings
def handle_error(error):
    with open(os.path.join(error_dir, 'error.log'), 'a') as error_file:
        error_file.write(f'{str(error)}\n')
def save_debug_data(data):
    with open(os.path.join(debug_dir, 'debug.log'), 'a') as debug_file:
        debug_file.write(f'{str(data)}\n')

# Run the app
if __name__ == "__main__":
    main()
