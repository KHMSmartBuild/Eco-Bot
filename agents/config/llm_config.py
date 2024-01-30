#   Script: agents/config/llm_config.py
""" 
This script creates a JSON script from the given config_data dictionary.
"""

import json
from dotenv import dotenv_values

# Load environment variables (if needed globally)
def get_config_list():
    """
    Get a list of configurations based on the environment file path.

    :param env_file_path: The path to the environment file.
    :type env_file_path: str

    :return: A list of configuration settings.
    :rtype: list
    """
    env_vars = dotenv_values(dotenv_path='../agents/config/.env')
    api_key = env_vars.get('OPENAI_API_KEY')

    # Check if the OPENAI_API_KEY is not found
    if not api_key:
        print("OpenAI API Key not found. Please enter your OpenAI API Key:")
        api_key = input("API Key: ").strip()

    # Create the JSON list of configurations
    config_list = [
        {
            "model": "gpt-4-1106-preview",
            "api_key": env_vars['OPENAI_API_KEY'],
            "org_id": env_vars['OpenAI_Orginization_ID'],
            "logger": {
                "level": "info",
                "format": "json",
                "transports": [
                    {
                        "filename": "gpt-4-1106-preview.log"
                    }
                ]
            }
        },
        {
            "model": "gpt-4",
            "api_key": env_vars['OPENAI_API_KEY'],
            "org_id": env_vars['OpenAI_Orginization_ID'],
            "logger": {
                "level": "info",
                "format": "json",
                "transports": [
                    {
                        "filename": "gpt-4.log"
                    }
                ]
            }
        },
        {
            "model": "gpt-3.5-turbo",
            "api_key": env_vars['OPENAI_API_KEY'],
            "org_id": env_vars['OpenAI_Orginization_ID'],
            "logger": {
                "level": "info",
                "format": "json",
                "transports": [
                    {
                        "filename": "gpt-3.5-turbo.log"
                    }
                ]
            }
        }
        # other configurations...
    ]
    return config_list
# Convert the JSON list to a string
def get_config_json_string():
    """
    Returns a JSON string representation of the configuration from the specified environment file path.

    :param env_file_path: The path to the environment file
    :type env_file_path: str
    :return: A JSON string representing the configuration
    :rtype: str
    """
    return json.dumps(get_config_list())
