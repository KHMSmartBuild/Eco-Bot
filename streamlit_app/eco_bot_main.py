"""
ECO-BOT Landing page
This is a simple Eco-Bot chat bot that uses OpenAI's GPT-4 model
to generate responses to user input.
"""
import os
import sys
sys.path.append("..")
from eco_buddies.eco_chat import EcoBot
import json
import datetime
import logging
import openai
import streamlit as st
#import streamlit_timeline as timeline
import streamlit.components.v1 as components
from icecream import ic
from dotenv import load_dotenv




# Setup logging
log_folder = "logs"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)
log_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  
log_file = os.path.join(log_folder, f"log_{log_timestamp}.txt")  

# Configure the logging module to save logs to the log file
log_format = '%(asctime)s - %(levelname)s - Landing Page - %(message)s'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format=log_format)
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key
personality = json.load(open("../eco_buddies/eco_bot_personality.json", "r", encoding="utf-8"))
bot = EcoBot()

@st.cache_resource
def get_response(user_input):
    """
    Cache the data returned by this function for improved performance.

    Parameters:
    - user_input (str): The input provided by the user.

    Returns:
    - str: The generated response.
    """
    return bot.generate_response(user_input)
    

@st.cache_data
def load_image(image_path):
    """
    Cache the data returned by this function for improved performance.

    Parameters:
    - image_path (str): The path to the image file.

    Returns:
    - bytes or None: The content of the image file as bytes, or None if the file is not found.
    """
    try:
        return open(image_path, "rb").read()
    except FileNotFoundError:
        st.error(f"Error: Image not found at {image_path}")
        return None
# Set the title of the app
col1, col2 = st.columns(2)
with col1:
    st.title("Eco-Bot Landing Page")
with col2:
    st.image("assets/images/eco-botLF.png", caption="Eco-Bot", use_column_width=False, width=250)


# Hero Section
st.header("Welcome to Eco-Bot!")
st.subheader("Your eco-friendly assistant powered by OpenAI.")
st.write("Interact with Eco-Bot and learn more about our mission and features.")


# Display Eco-Bot Image
eco_bot_image = load_image("assets/images/eco-bot.png")
if eco_bot_image:
    st.sidebar.image(eco_bot_image, caption="Eco-Bot", use_column_width=False, width=50)

# Chat Interface in a Container with Conditional Execution
show_chat = st.checkbox("Show Chat Interface")
if show_chat:
    with st.container():
        st.subheader("Chat with Eco-Bot")
        chat_input = st.text_input("Type your message here...")  # <-- Renamed variable
        if chat_input:
            response = bot.generate_response(chat_input)
            st.write(f"Eco-Bot: {response}")
        
# About Section in a Container
with st.container():
    st.header("About Eco-Bot")
    st.write("""
    Eco-Bot is not just another bot; it's a movement. In a world grappling with environmental challenges, 
    Eco-Bot emerges as a beacon of hope, guiding users towards a sustainable future. 
    By integrating technology with environmental consciousness, 
    Eco-Bot aims to make green living accessible and enjoyable for everyone.
    """)

# Pitch Deck Section in a Container
with st.container():
    st.header("Why Eco-Bot?")
    st.write("""
    - Address Environmental Challenges
    - Innovative Eco-Friendly Solutions
    - Engage and Educate Communities
    """)
    # TODO:Display youtube video when videos are available
    # components.iframe("https://www.youtube.com/channel/UCmsH6r0FBNdhirOkgP5VuEQ", width=700, height=400, scrolling=True)


# Roadmap with a Timeline using Session State and Progress Bars
with st.container():
    st.header("Roadmap")
    st.write("Our journey is just beginning. Explore our roadmap to see our milestones and future plans.")
    #TODO: Add timeline here with timeline from streamlit_timeline

    # Define milestones with expected completion dates and descriptions
    milestones = [
        {"title": "Conceptualization & Initial Design", "date": "Q1 2023", "description": "Laying the groundwork for Eco-Bot's development."},
        {"title": "Development of MVP", "date": "Q2 2023", "description": "Creating a minimum viable product for initial user feedback."},
        {"title": "Beta Testing & Feedback Collection", "date": "Q3 2023", "description": "Testing with select users to refine and improve."},
        {"title": "Official Launch & Expansion", "date": "Q4 2023", "description": "Launching Eco-Bot to the public and expanding features."},
    ]
    if 'milestone' not in st.session_state:
        st.session_state.milestone = 0  # Or another appropriate default value

    # Display each milestone with a progress bar
    for index, milestone in enumerate(milestones):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"### {milestone['title']}")
            st.progress((index + 1) * 25)
            st.caption(milestone['description'])
            st.link_button("Learn More", url="https://patreon.com/user?u=103935097&utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=creatorshare_creator&utm_content=join_link")
        with col2:
            st.write(milestone['date'])

        if index < st.session_state.milestone:
            st.success("✅ Completed")
        else:
            st.warning("🔜 Upcoming")

        # Button to advance milestones
        if st.button("Advance to Next Milestone", key=f"milestone_{index}"):
            if st.session_state.milestone < len(milestones) - 1:
                st.session_state.milestone += 1
            else:
                st.session_state.milestone = 0  # Reset after the last milestone


    # Crowdfunding Section in a Container
with st.container():
    st.header("Support Eco-Bot")
    st.write("""
    Join our mission and support the development of Eco-Bot. Every contribution brings us closer to our goal.
    """)
    st.button("Donate Now",key="donate_now",help="Donate to Eco-Bot",on_click="https://www.justgiving.com/crowdfunding/Eco-Bot?utm_term=2VGrAgRdD",)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("JustGiving", url="https://www.justgiving.com/crowdfunding/Eco-Bot?utm_term=2VGrAgRdD",)
    with col2:
        st.link_button("Patreon", url="https://patreon.com/user?u=103935097",)
    with col3:
        st.link_button("Youtube", url="https://youtube.com/@EcoBot-qp4ss?si=ojG3SWdomEU5nX6w",)
    # create three columns
# Footer
st.write("---")
st.write("Eco-Bot © 2023 | Contact Us | Terms of Service")
