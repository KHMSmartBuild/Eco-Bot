"""
The eco-bot-MVP_app.py script is used to demonstrait the working of multiple
agents in a streamlit app.
"""
import streamlit as st
import streamlit.components.v1 as components
from streamlit_webrtc import webrtc_streamer
from icecream import ic
import json
import sys
# Append the parent directory to sys.path
sys.path.append("..")
from gbts.gbts import GBTS
from eco_buddies.eco_bot_chat import  EcoBot


# Initialize icecream setup
ic.configureOutput(prefix="eco-bot-MVP_app | ")

# Load GBTS prompts structure
with open('C:/Users/User/OneDrive/Desktop/Buisness/KHM Smart Build/Coding/Projects/OCFS_projects/Eco-Bot/gbts/GBTS.json', 'r', encoding='utf-8') as f:  # replace with the path to your GBTS prompts JSON file
    GBTS_PROMPTS = json.load(f)

# Initialize GBTS
gbts_instance = GBTS()


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
    """
    Load an image from the given image path.

    Parameters:
        image_path (str): The path to the image file.

    Returns:
        bytes: The contents of the image file.
    """
    return open(image_path, "rb").read()

# Main App
def main():
    """
    Generates the function comment for the given function body in a markdown code block with the correct language syntax.
    
    Returns:
        str: The function comment in markdown format.
    """
    # Apply custom styles
    with open("assets/styles/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    html_content = load_html("assets/site_layout.html")
    st.markdown(html_content, unsafe_allow_html=True)
    # App Header
    st.title("Eco-Bot")
    st.write("Welcome to the Eco-Bot app! Here, we integrate nature with technology.")

    # Display Eco-Bot Image
    eco_bot_image = load_image("assets/images/eco-bot.png")
    st.image(eco_bot_image, caption="Eco-Bot", width=200)
    

    # Main Content Area
    with st.container():
        st.subheader("Eco-Bot")
        st.write("""
        Eco-Bot represents the harmonious blend of technology and nature. 
        It's our commitment to a sustainable future where technology complements nature.
        """)

        # Quadrant Layout
        col1, col2, col3, col4 = st.columns(4)

        # Agent 1 in Quadrant 1
        with col1:
            st.image(r"C:/Users/User/OneDrive/Desktop/Buisness/KHM Smart Build/Coding/Projects/OCFS_projects/Eco-Bot/streamlit_app/assets/images/eco_buddy1.png")
            st.text_area("Agent 1 Response:", value="", key="agent1_response")

        # Agent 2 in Quadrant 2
        with col2:
            st.image(r"C:/Users/User/OneDrive/Desktop/Buisness/KHM Smart Build/Coding/Projects/OCFS_projects/Eco-Bot/streamlit_app/assets/images/eco_buddy2.png")
            st.text_area("Agent 2 Response:", value="", key="agent2_response")

        # Agent 3 in Quadrant 3
        with col3:
            st.image(r"C:/Users/User/OneDrive/Desktop/Buisness/KHM Smart Build/Coding/Projects/OCFS_projects/Eco-Bot/streamlit_app/assets/images/eco_buddy3.png")
            st.text_area("Agent 3 Response:", value="", key="agent3_response")

        # Agent 4 in Quadrant 4
        with col4:
            st.image(r"C:/Users/User/OneDrive/Desktop/Buisness/KHM Smart Build/Coding/Projects/OCFS_projects/Eco-Bot/streamlit_app/assets/images/eco_buddy4.png")
            st.text_area("Agent 4 Response:", value="", key="agent4_response")
            
    # Center Area for Visual Representation
    # (Placeholder - Replace with actual visual representation logic)
    with st.container():
        
       # WebRTC Streamer Expander
        with st.expander("Try our WebRTC Streamer"):
            webrtc_streamer(key="example") 
    # Combined Text Area for User & Eco-Bot
    with st.container():

        st.expander("Chat with Eco-Bot")
        st.text("Conversation History")
        st.text_area("Chat with Eco-Bot:", value="", key="main_conversation")
        st.__cached__ = EcoBot().generate_response(user_input)
        # Placeholder for chat history

        chat_history = "response+\n, user_input+\n" 

        # Check if there's a previous chat history saved in the session state
        if 'chat_history' in st.session_state:
            chat_history = st.session_state.chat_history

        # Display the chat history
        st.text_area("Chat History", value=chat_history, height=400, key="chat_display", disabled=True)

        # Input field for user messages
        user_message = st.text_input("Type your message:")

        # Send button
        if st.button("Send"):
            # Append user message to chat history
            chat_history += f"User: {user_message}\n"
            
            # Compute and append responses from Eco-Bot and EcoBuddies
            # (This is just a placeholder, replace with actual logic)
            #with GeneralManagerAgent():
                #chat_history += f"Eco-Bot: {EcoBot_Chat().generate_response(user_message)}\n"

                #with DigitalTwinAgent():
                    #chat_history += f"Eco-Buddies: {EcoBot_Chat().generate_response(user_message)}\n"
                #response= EcoBot_Chat().generate_response(user_message)

                
                #return  response
            # Update session state with new chat history
        st.session_state.chat_history = chat_history

            # Clear the user input field
        user_input = st.text_input("Type your message:", value="", key="user_input")

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
    st.sidebar.text("Help")
    # Help options/buttons
    st.sidebar.header("Menu")
    st.sidebar.text("Previous Conversations")
    # Display previous conversations, perhaps in a selectbox or list
    st.sidebar.text("Settings")
    # Settings options/buttons
    if st.sidebar.button("Help"):
        # Add your help functionality here
        st.write("This is the help content.")

    # Imagery from Pictory agent
    st.container()
    with st.text("Imagery"):
     st.dataframe("Imagery from Pictory agent")

    # TODO: Add imagery from Pictory agent
    # Imagery from Pictory agent
    #imagery_url = PictoryAgent().generate_imagery(keywords)
    #st.image(imagery_url, caption="Imagery from Pictory agent")

    # Key Points - Meeting Minutes from parsing agent with gbts system
    st.container()
    with st.text("Key Points - Meeting Minutes"):
     st.dataframe("Key Points - Meeting Minutes from parsing agent with gbts system")
    

    # Key Points - Issues
    # Issues
    st.text("Issues")
    issues_covered = st.text_area("Issues Covered:", value="")
    issues_agreed = st.text_area("Issues Agreed:", value="")
    issues_pending = st.text_area("Issues Pending:", value="")
    
    # User chat or Prompt
    st.text("User chat or Prompt")
    user_chat = st.text_area("Type your message:", value="", key="user_chat")


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
    
# GBTS Interaction Page
def d3_node_structure():
    with open('index.html', 'r', encoding='utf-8') as f:
        html_code = f.read()
    components.html(html_code, height=600)
def gbts_interaction_page():

    st.container()
    with st.write("Explore the Gaia-Bohm Thought Style (GBTS) interaction here."):
        st.echo()
        #gbts_instance = GBTS()
    # Example of guiding user through the first prompt
    if 'current_stage' not in st.session_state:
        st.session_state.current_stage = "Seed of Inquiry"
    
    st.write(GBTS_PROMPTS[st.session_state.current_stage]['prompt'])
    user_response = st.text_area("Your Response:", "")
    
    if st.button("Next"):
        # Save the user's response in the GBTS tree
        if gbts_instance.root_node is None:
            gbts_instance.initiate_prompt_tree(user_response)
        else:
            # Logic to add the response as a new node in the GBTS tree
            pass  # This will be developed further based on how you want the conversation to progress
        
        # Move to the next stage (this is a simple example, you'd need more complex logic for branching paths)
        if st.session_state.current_stage == "Seed of Inquiry":
            st.session_state.current_stage = "Branches of Understanding"

    # Display the current state of the GBTS tree (as a JSON string for now)
    st.json(gbts_instance.to_json())
    d3_node_structure()

#home_page()

def home_page():
    """ display the home page """
    if home_page:
        st.write("Welcome to Eco-Bot! Let's make eco-friendly choices together.")
        #with GeneralManagerAgent():
            #input = st.text_input("Ask Eco-Bot a question:")
            #if input:
                #response = EcoBot_Chat.handle_input(input)
                #st.write(f"Eco-Bot: {response}")
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
    # TODO: code for displaying and updating settings

 
# Run the app
if __name__ == "__main__":
    main()


    #Script name: eco-bot-MVP_app.py # streamlit_app/eco-bot-MVP_app.py
    #script root: streamlit_app
    # project root: C:\Users\User\OneDrive\Desktop\Buisness\KHM Smart Build\Coding\Projects\OCFS_projects\Eco-Bot
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
    #Version: 1.0