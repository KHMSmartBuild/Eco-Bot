import json
import os
from dotenv import load_dotenv
from autogen.oai import get_config_list

# Load API keys from .env file
load_dotenv(os.path.join("agents", "config", ".env"))
openai_api_key = os.getenv("OPENAI_API_KEY")
Orginization_ID = os.getenv("OpenAI_Orginization_ID")
config_list_autogen = get_config_list([openai_api_key])
  # Call the function

# Debugging: Print API keys to ensure they're loaded
print(f"OpenAI API Key: {openai_api_key}")
print(f"Azure OpenAI API Key: {Orginization_ID}")

# Ensure API keys are loaded
if not openai_api_key or not Orginization_ID:
    raise ValueError("API keys not loaded correctly from .env file.")

# Load configurations from llm_config.json
config_file_path = os.path.join("agents", "config", "llm_config.json")
with open(config_file_path, "r") as file:
    config_list_api = json.load(file)

# Update the configurations with the actual API keys
for config in config_list_api:
    if "OPENAI_API_KEY" in config.get("api_key", ""):
        config["api_key"] = openai_api_key
    elif "OpenAI_Orginization_ID" in config.get("api_key", ""):
        config["api_key"] = Orginization_ID

# Combine the configurations
config_list = config_list_autogen + config_list_api

# Now config_list has the actual API keys and can be used in your GeneralManagerAgent