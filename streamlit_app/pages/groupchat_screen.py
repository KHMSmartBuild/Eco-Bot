# /streamlit_app/pages/groupchat_screen.py
"""
This is the streamlit app for the group chat screen.

This app is used to create a group chat screen for the eco-buddies project.

"""

import streamlit as st
import streamlit.components.v1 as components
from eco_buddies.eco_chat import EcoBot
# from logging import Logger, basicConfig, INFO, Formatter, FileHandler, StreamHandler
# from data.database.utils.db_operations import Agent, ChatHistory, Assistant
# from data.database.utils.setconn import session

# TODO:set up logging
# TODO:set up database connection

# Main chatbot Eco-Bot chat object
ecobot=EcoBot()
# Page Title
st.subheader("create a group chat and make your own Eco Episode")

# create a container with three columns
with st.container():
    st.markdown("GroupChat")
    # create three columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("UserProxyAgent")
        if st.checkbox("UserProxyAgent Options" ,key="UserProxyAgent",value=True): 
            st.markdown("UserProxyAgent Options")
            st.text_input("UserProxyAgent Name", "", key="UPA_Name")
            st.text_input("UserProxyAgent id", "", key="UPA_id")
            st.text_input("UserProxyAgent System Message", "", key="UPA_System_Message")
            st.selectbox("Tools", ["1", "2", "3"], key="UPA_tools")    
        st.text_area("UserProxyAgent Response", "")
        st.divider()
        st.markdown("Agent")
        if st.checkbox("Agent",key="Agent",value=True):
            st.text_input("Agent Name", "", key="Agent_Name")
            st.text_input("Agent id", "", key="Agent_id")
            st.text_input("Agent System Message", "", key="Agent_System_Message")
            st.selectbox("Tools", ["1", "2", "3"], key="Agent_tools")
        st.text_area("Agent Response", "")
        
    with col2:
        st.markdown("Imagination Screen")
        st.select_slider("Imagination Screen", ["1", "2", "3"])
        with st.container():
            components.iframe("https://video.pictory.ai/preview/18299332479991105903001699135484198")
            st.divider()
            st.text_area("Imagination Screen script", "")
    with col3:
        st.markdown("AssistantAgent")
        if st.checkbox("AssistantAgent",key="AssistantAgent"):
            st.text_input("AssistantAgent Name", "", key="AA_Name")
            st.text_input("AssistantAgent id", "", key="AA_id")
            st.text_input("AssistantAgent System Message", "", key="AA_System_Message")
            st.selectbox("Tools", ["1", "2", "3"], key="AA_tools")
        st.text_area("AssistantAgent Response", "")
        st.divider()
        st.markdown("Agent2")
        if st.checkbox("Agent",key="Agent2"):
            st.text_input("Agent2 Name", "", key="Agent2_Name")
            st.text_input("Agent2 id", "", key="Agent2_id")
            st.text_input("Agent2 System Message", "", key="Agent2_System_Message")
            st.selectbox("Tools", ["1", "2", "3"], key="Agent2_tools")
        st.text_area("Agent2 Response", "")

# create the message input box and chat history container
with st.container():
    message = st.text_input("Type your message here", key="message_input")
    avatar = st.text_input("Avatar URL")
# message = st.text_area("Type your message here", height=100)
# avatar = st.text_area("Avatar URL", height=100)

context = []

def message_input():
    global message
    # write the message to the chat history container
    context.append(message)
    context.append(avatar)

    # send the message to the ecobot and get the response
    response = ecobot.generate_response(message)

    # display the response in the chat history container
    context.append(response)

    # clear the message input box
    message = ""

def display_chat_history():
    """
    Display the chat history in the chat history container.

    This function iterates over each message in the context and writes it to the chat history container.

    Parameters:
    - None

    Return:
    - None
    """
    # display the chat history in the chat history container
    for message in context:
        st.write(message)

def ecobot_chat(self, message, runid):
    """
    Sends a message to the Ecobot and returns the generated response.

    Parameters:
    - message (str): The message to send to the Ecobot.
    - runid (int): The ID of the run.

    Returns:
    - response (str): The generated response from the Ecobot.
    """
    #use the ecobot to send the message and get the response
    self.runid = runid
    ecobot_chat = ecobot.generate_response( message(context))
    response = ecobot_chat
    return response
