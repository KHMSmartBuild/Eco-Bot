"""
Fixes the script by adding missing indentation and correcting function comments.

Returns:
    None
"""
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from icecream import ic, IceCreamDebugger

import sys
# Append the parent directory to sys.path
import os

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Append the parent directory to sys.path
sys.path.append(parent_dir)
from eco_buddies.eco_chat import EcoBot

# Initialize the icecream module for debugging
ic.configureOutput(prefix="DTA Debug | ")

# add iframe link to streamlit to open the Whimsical flowchart
whimsical_iframe = """
<iframe style="border:none" width="800" height="450" src="https://whimsical.com/embed/JUyX8eXkcdgqpRKgqbKNC1"></iframe>
"""

# Initialize the EcoBotChat
bot = EcoBot()
DTwatch = IceCreamDebugger()
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


# Overview Section
st.header("Overview")
st.write("""
Eco-Bot is envisioned as an interactive, educational, and engaging AI bot focused on promoting ecological and environmental awareness and actions. 
It's designed to navigate users through a rich, exploratory journey within the realms of environmental knowledge, utilizing a unique approach, 
potentially named the Gaia-Bohm Thought Style (GBTS).
""")

# Agent Hierarchy Section
st.header("Agent Hierarchy")
# Display Agent Hierarchy Image
eco_bot_image = load_image("assets/images/Eco-Bot agents flow.png")
if eco_bot_image:
    st.image(eco_bot_image, caption="Eco-Bot", use_column_width=True, width=800)

st.write("""
The Agent Hierarchy section describes the three levels of agents in the Eco-Bot system: Managerial Agents, Task Team Agents, and Worker Team Agents. It outlines their respective roles and responsibilities in the system.
""")
st.latex(r"""
\begin{align}
    \text{Eco-Bot} \rightarrow \text{Managerial Agents} \rightarrow \text{Task Team Agents} \rightarrow \text{Worker Team Agents} \rightarrow \text{User Dashboard}
\end{align}
""")
# Key Components Section
st.header("Key Components")
st.write("""
In this section, you will find detailed information about the key components of the Eco-Bot system. These components include Digital Twins, which enable virtual simulations of real-world entities; the Centralized Communication Protocol, which ensures efficient communication between agents; the Centralized Data Management System, which stores and manages data; and the User Dashboard, which provides users with a user-friendly interface to interact with the system.
""")

components.html(whimsical_iframe, width=800, height=450, scrolling=True)

# Challenges and Considerations Section
st.header("Challenges and Considerations")
st.write("""
This section discusses potential challenges that may arise during the development and implementation of the Eco-Bot system. It highlights areas such as inter-agent communication, ensuring data quality, and designing user-friendly communication interfaces.
""")
st.multiselect("Challenges and Considerations", ["Inter-agent communication", "Ensuring data quality", "Designing user-friendly communication interfaces"])

# Next Steps Section
st.header("Next Steps")
st.write("""
The Next Steps section outlines the subsequent stages of development for the Eco-Bot system. It covers activities such as planning, prototyping, and continuous optimization to ensure the system's effectiveness and efficiency.
""")
with st.chat_message("user"):
    st.write("Donate now to help support our mission! these graphs are for demonstration purposes only.")
    st.line_chart(np.random.randn(30, 3))

# Conclusion Section
st.header("Conclusion")
st.write("""
In the conclusion, the document emphasizes the importance of careful planning and consideration in the development of the Eco-Bot system. It highlights the key components of the system, its challenges, and the next steps in the system's development.
""")
# Display Eco-Buddies Options
with open("../streamlit_app/pages/eco_buddies_page.toml", "r", encoding="utf-8") as file:
    eco_buddies_content = file.read()
    st.write(eco_buddies_content)

# Footer Section
st.write("---")
st.write("© 2023. All rights reserved.")

