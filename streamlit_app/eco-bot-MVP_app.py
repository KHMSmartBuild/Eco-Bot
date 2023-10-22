#Script name: eco-bot-MVP_app.py # streamlit_app/eco-bot-MVP_app.py
#Author: Kyle
#Company: KHM Smart Build
#Description: This is the streamlit app for the Eco-Bot MVP.
"""This is the streamlit app for the Eco-Bot MVP.
the apps main funtions are as listed;
chatbot:Eco-Bot
settings:Configure your settings.
eco_buddies:Meet your Eco-Buddies!
#gbts_interaction:Choose your eco-buddies to help complete your eco-missions.
#gbts_interaction:Explore the Gaia-Bohm Thought Style (GBTS) interaction here.
main page has chatbot, settings, eco_buddies, gbts_interaction,"""
#Date: 2023-05-10

import streamlit as st
import sys
import os
from icecream import ic
from agents.autogen_agents import GeneralManagerAgent, Agent, DigitalTwinAgent
from eco_buddies import eco_bot, eco_buddies
# Append the parent directory to sys.path
sys.path.append(".")





# Streamlit App Configuration
st.set_page_config(
    page_title="Eco-Bot",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load the Eco-Bot Image
@st.cache_data
def load_image(image_path):
    return open(image_path, "rb").read()

# Main App
def main():
    # Apply custom styles
    with open("assets/styles/styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    html_content = load_html("assets/site_layout.html")
    st.markdown(html_content, unsafe_allow_html=True)
    # App Header
    st.title("Eco-Bot")
    st.write("Welcome to the Eco-Bot app! Here, we integrate nature with technology.")

    # Display Eco-Bot Image
    eco_bot_image = load_image("assets/images/eco-bot.png")
    st.image(eco_bot_image, caption="Eco-Bot", size=(50, 50))

    # Main Content Area
    st.subheader("About Eco-Bot")
    st.write("""
    Eco-Bot represents the harmonious blend of technology and nature. 
    It's our commitment to a sustainable future where technology complements nature.
    """)
    # Quadrant Layout
    col1, col2, col3, col4 = st.columns(4)

    # Agent 1 in Quadrant 1
    with col1:
        st.image("path_to_agent1_avatar.jpg")
        st.text_area("Agent 1 Response:", value="", key="agent1_response")

    # Agent 2 in Quadrant 2
    with col2:
        st.image("path_to_agent2_avatar.jpg")
        st.text_area("Agent 2 Response:", value="", key="agent2_response")

    # Agent 3 in Quadrant 3
    with col3:
        st.image("path_to_agent3_avatar.jpg")
        st.text_area("Agent 3 Response:", value="", key="agent3_response")

    # Agent 4 in Quadrant 4
    with col4:
        st.image("path_to_agent4_avatar.jpg")
        st.text_area("Agent 4 Response:", value="", key="agent4_response")

    # Center Area for Visual Representation
    # (Placeholder - Replace with actual visual representation logic)
    st.text("Live Visual Representation of Conversation")

    # Combined Text Area for User & Eco-Bot
    st.text("Conversation History")
    st.text_area("Chat with Eco-Bot:", value="", key="main_conversation")

    # Placeholder for chat history
    chat_history = ""

    # Check if there's a previous chat history saved in the session state
    if 'chat_history' in st.session_state:
        chat_history = st.session_state.chat_history

    # Display the chat history
    st.text_area("Chat History", value=chat_history, height=300, key="chat_display", disabled=True)

    # Input field for user messages
    user_message = st.text_input("Type your message:")

    # Send button
    if st.button("Send"):
        # Append user message to chat history
        chat_history += f"User: {user_message}\n"
        
        # Compute and append responses from Eco-Bot and EcoBuddies
        # (This is just a placeholder, replace with actual logic)
        chat_history += "Eco-Bot: Hello!\n"
        
        # Update session state with new chat history
        st.session_state.chat_history = chat_history

        # Clear the user input field
        st.text_input("Type your message:", value="", key="user_input")

        # User Interactions
        st.subheader("Interact with Eco-Bot")
        user_input = st.text_input("Ask Eco-Bot a question:")
        if user_input:
            # Placeholder for Eco-Bot's response logic
            st.write("Eco-Bot says: ...")  # Replace with actual response
    st.sidebar.header("Menu")
    st.sidebar.text("Previous Conversations")
    # Display previous conversations, perhaps in a selectbox or list
    st.sidebar.text("Settings")
    # Settings options/buttons


    # Imagery
    st.text("Imagery")
    imagery_upload = st.file_uploader("Upload an image or other visual items", type=["jpg", "png", "jpeg"])

    # Key Points - Meeting Minutes
    st.text("Key Points - Meeting Minutes")
    meeting_minutes = st.text_area("Topics:", value="")

    # Key Points - Issues
    # Issues
    st.text("Issues")
    issues_covered = st.text_area("Issues Covered:", value="")
    issues_agreed = st.text_area("Issues Agreed:", value="")
    issues_pending = st.text_area("Issues Pending:", value="")

    # User chat or Prompt
    st.text("User chat or Prompt")
    user_chat = st.text_area("Type your message:", value="", key="user_chat")

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
def load_html(filename):
    with open(filename, "r") as f:
        return f.read()
# Home Page
def home_page():
    st.write("Welcome to Eco-Bot! Let's make eco-friendly choices together.")

# GBTS Interaction Page
def gbts_interaction_page():
    st.write("Explore the Gaia-Bohm Thought Style (GBTS) interaction here.")
    # ... additional code for GBTS interaction

# Eco-Buddies Page
def eco_buddies_page():
        """
        Display the Eco-Buddies page and provide options to add them to the chat window.
    
        This function is responsible for displaying the Eco-Buddies page. It uses the `st.write` function 
        to display the heading "Meet your Eco-Buddies!". It then reads the content of the file 
        "eco_buddies_options.txt" and writes it to the page using the `st.write` function.
    
        After displaying the Eco-Buddies page, the function provides options to add the Eco-Buddies to the chat window.
    
        Parameters:
            None
    
        Returns:
            None
        """
        # ... code for displaying and updating Eco-Buddies
        if st.button("Add Eco-Buddies"):
            st.__path__.append("eco_buddies")
            with open("eco_buddies_options.txt", "r") as f:
                st.write(f.read())
# Settings Page
def settings_page():
    st.write("Configure your settings.")
    # ... code for displaying and updating settings

# Main function
def main():
    # ... code for displaying and updating Eco-Bot
    with st.spinner("Loading Eco-Bot..."):
        eco_bot()   
# Run the app
if __name__ == "__main__":
    main()
