"""
Fixes the script by adding missing indentation and correcting function comments.

Returns:
    None
"""
import streamlit as st
from icecream import ic, IceCreamDebugger

import sys
# Append the parent directory to sys.path
import os

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Append the parent directory to sys.path
sys.path.append(parent_dir)
from eco_buddies.eco_bot_chat import EcoBot

# Initialize the icecream module for debugging
ic.configureOutput(prefix="DTA Debug | ")

# Initialize the EcoBotChat
bot = EcoBot()
DTwatch = IceCreamDebugger()

def eco_buddies_page():
    """
    Display the Eco-Buddies page and provide options to add them to the chat window.
    
    This function is responsible for displaying the Eco-Buddies page. It uses the `st.write` function 
    to display the heading "Meet your Eco-Buddies!". It then reads the content of the file 
    "eco_buddies_options.txt" and writes it to the page using the `st.write` function.
    
    After displaying the Eco-Buddies page, the function provides options to add the Eco-Buddies to the chat window.
    
    Returns:
        None
    """
    # Title and Introduction
    st.title("Eco-Bot System Overview")
    st.write("Welcome to the Eco-Bot System! Here's a comprehensive overview of our system and its significance in promoting environmental sustainability.")

    # Display Eco-Buddies Options
    with open("eco_buddies_options.txt", "r", encoding="utf-8") as file:
        eco_buddies_content = file.read()
        st.write(eco_buddies_content)

    # Overview Section
    st.header("Overview")
    st.write("""
    This section provides an introduction to the Eco-Bot system and explains its purpose in promoting environmental sustainability.
    """)

# Title and Introduction
st.title("Eco-Bot System Overview")
st.write("Welcome to the Eco-Bot System! Here's a comprehensive overview of our system and its significance in promoting environmental sustainability.")

# Overview Section
st.header("Overview")
st.write("""
This section provides an introduction to the Eco-Bot system and explains its purpose in promoting environmental sustainability.
""")

# Agent Hierarchy Section
st.header("Agent Hierarchy")
st.write("""
The Agent Hierarchy section describes the three levels of agents in the Eco-Bot system: Managerial Agents, Task Team Agents, and Worker Team Agents. It outlines their respective roles and responsibilities in the system.
""")

# Key Components Section
st.header("Key Components")
st.write("""
In this section, you will find detailed information about the key components of the Eco-Bot system. These components include Digital Twins, which enable virtual simulations of real-world entities; the Centralized Communication Protocol, which ensures efficient communication between agents; the Centralized Data Management System, which stores and manages data; and the User Dashboard, which provides users with a user-friendly interface to interact with the system.
""")

# Challenges and Considerations Section
st.header("Challenges and Considerations")
st.write("""
This section discusses potential challenges that may arise during the development and implementation of the Eco-Bot system. It highlights areas such as inter-agent communication, ensuring data quality, and designing user-friendly communication interfaces.
""")

# Next Steps Section
st.header("Next Steps")
st.write("""
The Next Steps section outlines the subsequent stages of development for the Eco-Bot system. It covers activities such as planning, prototyping, and continuous optimization to ensure the system's effectiveness and efficiency.
""")

# Conclusion Section
st.header("Conclusion")
st.write("""
In the conclusion, the document emphasizes the importance of careful planning and consideration in the development of the Eco-Bot system. It highlights the key components of the system, its challenges, and the next steps in the system's development.
""")

# Footer Section
st.write("---")
st.write("© 2023. All rights reserved.")

