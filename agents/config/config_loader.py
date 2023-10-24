import json
import os
from dotenv import load_dotenv
import autogen

def load_configurations():
    # Load API keys from .env file
    load_dotenv(os.path.join("agents", "config", ".env"))
    openai_api_key = os.getenv("OPENAI_API_KEY")
    OpenAI_Orginization_ID = os.getenv("OpenAI_Orginization_ID")

    # Debugging: Print API keys to ensure they're loaded
    print(f"OpenAI API Key: {openai_api_key}")
    print(f"Azure OpenAI API Key: {OpenAI_Orginization_ID}")

    # Load configurations from llm_config.json
    with open(r"C:/Users/User/OneDrive/Desktop/Buisness/KHM Smart Build/Coding/Projects/OCFS_projects/Eco-Bot/agents/config/llm_config.json", "r") as file:
        config_list_api = json.load(file)

    # Update the configurations with the actual API keys
    for config in config_list_api:
        if "OPENAI_API_KEY" in config.get("api_key", ""):
            config["api_key"] = openai_api_key
        elif "OpenAI_Orginization_ID" in config.get("api_key", ""):
            config["api_key"] = OpenAI_Orginization_ID

    # Load configurations using autogen
    config_list_autogen = autogen.config_list_from_json(
        "OAI_CONFIG_LIST",
        file_location=".",
        filter_dict={
            "model": {
                "gpt-4",
                "gpt-3.5-turbo",
                "gpt-3.5-16k",
                "gpt-4-32k",

            }
        }
    )

    # Combine the configurations
    config_list = config_list_autogen + config_list_api

    return config_list
