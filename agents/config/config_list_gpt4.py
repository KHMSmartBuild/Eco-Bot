import json
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv(os.path.join("agents", "config", ".env"))
openai_api_key = os.getenv("OPENAI_API_KEY")
azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")

# Load configurations from llm_config.json
with open(r"C:\Users\User\OneDrive\Desktop\Buisness\KHM Smart Build\Coding\Projects\OCFS_projects\Eco-Bot\agents\config\llm_config.json", "r") as file:
    config_list = json.load(file)


# Replace placeholders in config_list with actual API keys
for config in config_list:
    if "<placeholder_for_openai_api_key>" in config.get("api_key", ""):
        config["api_key"] = openai_api_key
    elif "<placeholder_for_azure_openai_api_key>" in config.get("api_key", ""):
        config["api_key"] = azure_openai_api_key

# Now config_list has the actual API keys and can be used in your GeneralManagerAgent
