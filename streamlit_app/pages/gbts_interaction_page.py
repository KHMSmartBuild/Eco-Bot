import streamlit as st
import json

# Define the function to load the GBTS JSON content
def load_gbts_data():
    # Correct the file path according to the actual location of your GBTS.json file
    gbts_json_path = "../gbts/GBTS.json"  # Use a relative path suitable for deployment
    with open(gbts_json_path, "r", encoding="utf-8") as json_file:
        gbts_data = json.load(json_file)
    return gbts_data

# Define your Streamlit app logic using the loaded GBTS data
def gbts_interaction_page(gbts_data):
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
        render_d3_visualization('assets/gbtsVisualization.html')

    # Display the current state of the GBTS tree as JSON
    # Placeholder: replace with actual visual representation of GBTS
    st.json(st.session_state.user_responses)

# This function will read and render the D3 visualization HTML in Streamlit
def render_d3_visualization(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=600)  # You can adjust the height as needed

# Main function to run the Streamlit app
if __name__ == "__main__":
    gbts_data = load_gbts_data()
    gbts_interaction_page(gbts_data)
