import json
import re

# First, define the structure that will hold our keypoints
keypoints_structure = {
    # GBTS-related keypoints
    "Gaia Interconnectedness": [],
    "Open Dialogue and Language": [],
    "Strategic Thought Process": [],
    "Structured Roles for Agents": [],
    # Conversation stages
    "Seedling Stage (Greeting)": [],
    "Rooting (Understanding the Problem)": [],
    "Photosynthesis (Problem-Solving)": [],
    "Budding (Offering Solutions)": [],
    "Pollination (Confirmation and Feedback)": [],
    "Fruiting (Resolution)": [],
    "Decomposition (Follow-Up)": []
}

# Define patterns that might indicate each keypoint or stage
# These should be refined to match the conversation style
keypoint_patterns = {
    "Gaia Interconnectedness": [r"whole|together|synergy|interconnected"],
    # Add more patterns to match other GBTS principles and agent flow stages...
}

def identify_and_save_keypoints(conversation):
    """
    Process a given conversation, extract keypoints, and save them to JSON or JS.
    
    Args:
    conversation (str): The conversation text to be processed.
    
    Returns:
    None
    """
    # Split the conversation into sentences or dialogue turns
    dialogues = conversation.split('\n')
    
    # Iterate over each dialogue line
    for dialogue in dialogues:
        # Check each pattern to see if it matches a part of the conversation
        for keypoint, patterns in keypoint_patterns.items():
            for pattern in patterns:
                if re.search(pattern, dialogue, re.IGNORECASE):
                    keypoints_structure[keypoint].append(dialogue)
    
    # After processing, save the keypoints to a file
    
    # Convert to JSON
    json_filename = "/mnt/data/conversation_keypoints.json"
    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(keypoints_structure, jsonfile, indent=4)
    
    # If you prefer a JavaScript object
    js_filename = "/mnt/data/conversation_keypoints.js"
    js_content = f"const keypoints = {json.dumps(keypoints_structure, indent=2)};"
    with open(js_filename, 'w', encoding='utf-8') as jsfile:
        jsfile.write(js_content)

    # For the sake of demonstration, let's return the file names
    return json_filename, js_filename

# Define your conversation text here, and call the function
conversation_text = """
... Your conversation text goes here ...
"""

# Call the function to process the conversation
json_file, js_file = identify_and_save_keypoints(conversation_text)

# The output file names should now contain the processed keypoints
print(f"The keypoints have been saved to {json_file} and {js_file}.")