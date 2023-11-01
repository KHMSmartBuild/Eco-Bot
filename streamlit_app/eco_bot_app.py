"""
ECO-BOT CHAT
This is a simple chatbot that uses OpenAI's GPT-4 model to generate responses to user input.
"""
import os
import openai
import streamlit as st

from eco_buddies.eco_bot_chat import EcoBot
from icecream import ic
import logging
from dotenv import load_dotenv

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
eco_bot_image = load_image("assets/images/eco-bot.png")
if eco_bot_image:
    st.image(eco_bot_image, caption="Eco-Bot", use_column_width=False, width=200)

# Chat Interface in a Container with Conditional Execution
# Chat Interface in a Container with Conditional Execution
show_chat = st.checkbox("Show Chat Interface")
if show_chat:
    with st.container():
        st.subheader("Chat with Eco-Bot")
        user_input = st.text_input("Type your message here...")
        if user_input:
            response = bot.generate_response(user_input)
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

# Roadmap with a Timeline using Session State
if "milestone" not in st.session_state:
    st.session_state.milestone = 0

milestones = [
    "Conceptualization & Initial Design",
    "Development of MVP",
    "Beta Testing & Feedback Collection",
    "Official Launch & Expansion"
]

with st.container():
    st.header("Roadmap")
    st.write("Our journey is just beginning. Explore our roadmap to see our milestones and future plans.")
    
    for index, milestone in enumerate(milestones):
        if index <= st.session_state.milestone:
            st.write(f"✅ {milestone}")
        else:
            st.write(f"🔜 {milestone}")

    if st.button("Advance to Next Milestone"):
        st.session_state.milestone += 1

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
