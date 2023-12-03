""" 
This module contains the config setup functions.
"""
import os
import json
import re
from dotenv import load_dotenv

# Load environment variables from .env file in agents/config directory
load_dotenv(os.path.join("agents", "config", ".env"))

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
        ValueError: If no JSON data is found in the file.
    """
    file_path = os.path.join("agents", "config", "OAI_CONFIG_LIST.js")

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist")

    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

        # Extract JSON part from the JavaScript file
        # Assuming the JSON object starts with '{' and ends with '}'
        json_part = re.search(r'{\s*".*}\s*;', file_content, re.DOTALL)
        if json_part:
            json_string = json_part.group().rstrip(';')  # Remove trailing semicolon if present
            json_data = json.loads(json_string)

            # Replace environment variables in the JSON data
            for key, value in json_data.items():
                if isinstance(value, str) and value.startswith('process.env.'):
                    env_var = value.split('process.env.')[1]
                    json_data[key] = os.getenv(env_var)

            config_data = json_data
        else:
            raise ValueError("No JSON data found in the file")

    return config_data

# create a json script with the config_data as a variable
def create_config_json(config_data):
    """
    Create a JSON script with the config_data as a variable.

    Args:
        config_data (dict): The configuration data to be included in the JSON script.

    Returns:
        str: The JSON script with the config_data as a variable.

    Raises:
        ValueError: If config_data is not a dictionary.
    """
    if not isinstance(config_data, dict):
        raise ValueError("config_data must be a dictionary")

    json_script = f"const config = {json.dumps(config_data)};"

    return json_script

# print the json script to a new cell in the notebook
def print_config_json(config_data):
    """
    Print the JSON script with the config_data as a variable.

    Args:
        config_data (dict): The configuration data to be included in the JSON script.

    Returns:
        None
    """
    json_script = create_config_json(config_data)
    print(json_script)

# define the function to be called from app pages
def config_setup():
    """
    Loads the configuration data from the "OAI_CONFIG_LIST.js" file and prints the resulting JSON data.

    Parameters:
        None

    Returns:
        None
    """
    config_data = load_config_from_js("OAI_CONFIG_LIST.js")
    print_config_json(config_data)
