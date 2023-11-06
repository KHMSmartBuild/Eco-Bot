"""
ECO-BOT Landing page
This is a simple Eco-Bot chat bot that uses OpenAI's GPT-4 model to generate responses to user input.
"""
import os
import sys
import openai
import streamlit as st
import streamlit.components.v1 as components
from icecream import ic
import logging
from dotenv import load_dotenv
sys.path.append("..")
from eco_buddies.eco_bot_chat import EcoBot



# Setup icecream for debugging

ic.configureOutput(prefix="ECO-BOT Chat | ")

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# Load API keys from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

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
st.title("Eco-Bot Landing Page")

# Hero Section
st.header("Welcome to Eco-Bot!")
st.subheader("Your eco-friendly assistant powered by OpenAI.")
st.write("Interact with Eco-Bot and learn more about our mission and features.")

# Display Eco-Bot Image
# Display Eco-Bot Image
eco_bot_image = load_image("assets/images/eco-bot.png")
if eco_bot_image:
    st.image(eco_bot_image, caption="Eco-Bot", use_column_width=False, width=200)

# Display Interactive Avatar
with open("assets/ecobot_index.html", "r", encoding="utf-8") as f:
    avatar_html = f.read()
components.html(avatar_html, height=450)
# Chat Interface in a Container with Conditional Execution
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
    Eco-Bot is designed to address environmental challenges and provide eco-friendly solutions.
    Learn more about our mission, benefits, and the impact we aim to create.
    """)

# Pitch Deck Section in a Container
with st.container():
    st.header("Why Eco-Bot?")
    st.write("""
    - Address Environmental Challenges
    - Innovative Eco-Friendly Solutions
    - Engage and Educate Communities
    """)


# Roadmap with a Timeline using Session State and Progress Bars
with st.container():
    st.header("Roadmap")
    st.write("Our journey is just beginning. Explore our roadmap to see our milestones and future plans.")

    # Define milestones with expected completion dates and descriptions
    milestones = [
        {"title": "Conceptualization & Initial Design", "date": "Q1 2023", "description": "Laying the groundwork for Eco-Bot's development."},
        {"title": "Development of MVP", "date": "Q2 2023", "description": "Creating a minimum viable product for initial user feedback."},
        {"title": "Beta Testing & Feedback Collection", "date": "Q3 2023", "description": "Testing with select users to refine and improve."},
        {"title": "Official Launch & Expansion", "date": "Q4 2023", "description": "Launching Eco-Bot to the public and expanding features."},
    ]

    # Display each milestone with a progress bar
    for index, milestone in enumerate(milestones):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"### {milestone['title']}")
            st.progress((index + 1) * 25)
            st.caption(milestone['description'])
        with col2:
            st.write(milestone['date'])

        if index < st.session_state.milestone:
            st.success(f"✅ Completed")
        else:
            st.warning(f"🔜 Upcoming")

    # Button to advance milestones
    if st.button("Advance to Next Milestone"):
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
    st.button("Donate Now")

# Footer
st.write("---")
st.write("Eco-Bot © 2023 | Contact Us | Terms of Service")
