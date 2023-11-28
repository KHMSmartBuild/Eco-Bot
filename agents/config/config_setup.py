""" 
This module contains the config setup functions.
"""
import os
import json
import autogen


def load_config_from_js(file_path):
    """
    Load configuration data from a JavaScript file.

    Args:
        file_path (str): The path to the JavaScript file.

    Returns:
        dict: The loaded configuration data as a dictionary.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        JSONDecodeError: If the file does not contain valid JSON data.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        # Assuming the file contains a JSON array
        return json.load(file)

# Path to your OAI_CONFIG_LIST.js file
config_file_path = os.path.join('agents', 'config', 'OAI_CONFIG_LIST.js')

# Load the configuration
config_list_gpt4 = load_config_from_js(config_file_path)


