

import streamlit as st
#import streamlit.components.v1 as components
from eco_buddies.eco_chat import EcoBot
from icecream import ic

# Streamlit App Configuration
st.set_page_config(
    page_title="Eco-Bot",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com/',
        'Report a bug': 'https://www.google.com/',
        'About': 'This is a simple Eco-Bot chat bot that uses OpenAI\'s GPT-4 model to generate responses to user input.'
    }
    
)

# Page Title
st.title("The Big Clean APP")

# Page Description
st.write("Welcome to the Eco-Bot's Zero-Waste Challenge")

# Intro Contents
with st.container():
    st.write("The Challenge")
   
    col1, col2, col3 = st.columns(3)
    with col1:
        st.video("https://www.youtube.com/watch?v=veXEBFmqfj0")
    with col2:
        st.video("https://www.youtube.com/watch?v=4GtWGHvX-rk&pp=ygUPd2FzdGUgcmVjeWNsaW5n")
    with col3:
        st.video("https://www.youtube.com/watch?v=3PYYadvwkOo&pp=ygUYd2FzdGUgbWFuYWdlbWVudCBpc3N1ZXMg")
    with col1:
        st.video("https://www.youtube.com/watch?v=ccR2zK6yn8o&pp=ygUYd2FzdGUgbWFuYWdlbWVudCBpc3N1ZXMg")
    with col2:
        st.video("https://www.youtube.com/watch?v=Cti5HQZnTrQ&pp=ygUYd2FzdGUgbWFuYWdlbWVudCBpc3N1ZXMg")
    with col3:
        st.image(f"assets/images/eco-botLF.png", caption="Eco-Bot", use_column_width=True)
st.write("Litter is one of the biggest challenges we face today. How can we ensure that we are using as much as possible of our waste?")

# How To Solve The Challenge with Eco-Bot
# Page Contents
with st.container():
    st.write("How To Solve The Challenge with Eco-Bot")
    st.write("""
    Eco-Bot is a chatbot that helps you find the best way to recycle your waste. 
    """)
    if st.checkbox("Show Camera", False):
        st.camera_input("Take a picture of your waste")
        st.write("upload a picture of your waste")
        st.selectbox("Select an option", ("Option 1", "Option 2", "Option 3"))
        st.write("Eco-Bot will tell you how to recycle your waste")
    
        # Display Eco-Bot Image
        st.image(f"assets/images/eco-bot.png", caption="Eco-Bot", use_column_width=False, width=150)
        st.chat_input("Ask Eco-Bot a question: ")
        