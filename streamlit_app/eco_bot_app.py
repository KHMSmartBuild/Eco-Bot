import sys
import streamlit as st

# append the parent directory to the Python path
sys.path.append("..")
from eco_buddies.eco_bot_chat import EcoBotChat

bot = EcoBotChat()




@st.cache_data
def load_image(image_path):
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
