import sys
import os
import json
import codecs
import streamlit as st
import streamlit.components.v1 as components
sys.path.append("../gbts")
from gbts.gbts import GBTS, PromptTreeNode
#from gbts.gaia_assit import GaiaAssistant

#gaia = GaiaAssistant()
update_gbts = PromptTreeNode(role="...", message="...")
GBTS = GBTS()
# Define the gaia_assist function
#def gaia_assist(self, **kwargs):
#    self.assistant = gaia(**kwargs)
# Define the function to load the GBTS JSON content
def load_gbts_data():
    # Correct the file path according to the actual location of your GBTS.json file
    gbts_json_path = "../gbts/GBTS.json"  # Use a relative path suitable for deployment
    with open(gbts_json_path, "r", encoding="utf-8") as json_file:
        gbts_data = json.load(json_file)
    return gbts_data

# Define your Streamlit app logic using the loaded GBTS data
def gbts_interaction_page(gbts_data):
    """
    Generates a page for interacting with the Gaia-Bohm Thought Style (GBTS).

    Args:
        gbts_data (dict): A dictionary containing the GBTS data.

    Returns:
        None
    """
    st.title("Explore the Gaia-Bohm Thought Style (GBTS) Interaction")

    # Initialize the GBTS session state if not already done
    if 'current_stage' not in st.session_state:
        st.session_state.current_stage = "Seed of Inquiry"
    if 'user_responses' not in st.session_state:
        st.session_state.user_responses = []

    # Get the current GBTS prompt
    current_prompt = gbts_data[st.session_state.current_stage]['prompt']

    # Display the prompt for the current stage
    st.write(current_prompt)
    user_response = st.text_area("Your Response:", "")

    # Handle user response
    if st.button("Next"):
        # Save the user's response
        st.session_state.user_responses.append(user_response)
        
        # Logic to determine the next stage based on the response
        # Placeholder: update this logic as per your GBTS structure
        next_stage = "Branches of Understanding"  # This should be dynamically set
        st.session_state.current_stage = next_stage

        # Render the D3 visualization after the user progresses
        render_d3_visualization('../gbts/visualizations/index.html')

    # Display the current state of the GBTS tree as JSON
    # Placeholder: replace with actual visual representation of GBTS
    st.json(st.session_state.user_responses)

# This function will read and render the D3 visualization HTML in Streamlit
def render_d3_visualization(file_path):
    with codecs.open(file_path, 'r', 'utf-8') as f:
        html_content = f.read()
    components.html(html_content, height=600)
    return html_content

    

# Main function to run the Streamlit app
if __name__ == "__main__":
    gbts_data = load_gbts_data()
    gbts_interaction_page(gbts_data)
    html_file_path = '../gbts/visualizations/index.html'

