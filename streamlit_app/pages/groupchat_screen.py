import streamlit as st
import streamlit.components.v1 as components
from eco_buddies.eco_bot_chat import EcoBot



# Streamlit App Configuration
st.set_page_config(
    page_title="Eco-Bot",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="auto",
)
ecobot=EcoBot()
# Page Title
st.subheader("create a group chat and make your own Eco Episode")

# create a container with three columns
with st.container():
    # create three columns
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.checkbox("UserProxyAgent" ,key="UserProxyAgent",value=True):
            st.text_input("UserProxyAgent Name", "", key="UPA_Name")
            st.text_input("UserProxyAgent id", "", key="UPA_id")
            st.text_input("UserProxyAgent System Message", "", key="UPA_System_Message")
            st.selectbox("Tools", ["1", "2", "3"], key="UPA_tools")    
        st.text_area("UserProxyAgent Response", "")
        
        st.divider()
        if st.checkbox("Agent",key="Agent",value=True):
            st.text_input("Agent Name", "", key="Agent_Name")
            st.text_input("Agent id", "", key="Agent_id")
            st.text_input("Agent System Message", "", key="Agent_System_Message")
            st.selectbox("Tools", ["1", "2", "3"], key="Agent_tools")
        st.text_area("Agent Response", "")
        
    with col2:
        st.write("Imagination Screen")
        with st.container():
            components.iframe("https://video.pictory.ai/preview/18299332479991105903001699135484198")
            st.select_slider("Imagination Screen", ["1", "2", "3"])
            st.text_area("Imagination Screen script", "")
    with col3:
        if st.checkbox("AssistantAgent",key="AssistantAgent"):
            st.text_input("AssistantAgent Name", "", key="AA_Name")
            st.text_input("AssistantAgent id", "", key="AA_id")
            st.text_input("AssistantAgent System Message", "", key="AA_System_Message")
            st.selectbox("Tools", ["1", "2", "3"], key="AA_tools")
        st.text_area("AssistantAgent Response", "")
        st.divider()
        if st.checkbox("Agent",key="Agent2"):
            st.text_input("Agent2 Name", "", key="Agent2_Name")
            st.text_input("Agent2 id", "", key="Agent2_id")
            st.text_input("Agent2 System Message", "", key="Agent2_System_Message")
            st.selectbox("Tools", ["1", "2", "3"], key="Agent2_tools")
        st.text_area("Agent2 Response", "")

# create the message input box and chat history container
with st.container():
    message = st.text_input("Type your message here")
    avatar = st.text_input("Avatar URL")
# message = st.text_area("Type your message here", height=100)
# avatar = st.text_area("Avatar URL", height=100)

def message_input():
    # write the message to the chat history container
    # send the message to the ecobot and get the response
    chat_history.append(message,runid='..')

    # send the message to the ecobot and get the response
    response = ecobot_chat.handle_input(message='..')

    # display the response in the chat history container
    chat_history.append(response)

    # clear the message input box
    message = ""

def chat_history():
    # display the chat history in the chat history container
    for message in chat_history:
        st.write(message)

def ecobot_chat(self, message, runid):
    #use the ecobot to send the message and get the response
    self.runid = runid
    ecobot_chat = ecobot.handle_input(message)
    response = ecobot_chat
    return response
