import os
import json
import autogen as ag
from agents.autogen_agents import GeneralManagerAgent, Agent, DigitalTwinAgent
from icecream import ic
from dotenv import load_dotenv

class EcoBuddies_Vision:
    def __init__(self):
        """
        Initializes the class instance by loading API keys and configurations, and initializing various agents and properties.

        Parameters:
            None

        Returns:
            None
        """
        # Load API keys and configurations
        self.config_list = self.load_configurations()

        # Initialize agents
        self.vision_agent = ag.VisionAgent(Agent)
        self.general_manager = GeneralManagerAgent()
        self.digital_twin = DigitalTwinAgent(self.general_manager)
        self.personality = self.load_personality()

    @staticmethod
    def load_personality():
        """Load the personality of the bot."""
        # TODO: Implement the method to load the bot's personality
        pass

    @staticmethod
    def load_configurations():
        """Load API keys and configurations from .env and llm_config.json."""
        # Load API keys from .env file
        load_dotenv("config/.env")
        openai_api_key = os.getenv("OPENAI_API_KEY")
        azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")

        # Load configurations from llm_config.json
        with open("config/llm_config.json", "r") as file:
            config_list = json.load(file)

        # Replace placeholders in config_list with actual API keys
        for config in config_list:
            if "<placeholder_for_openai_api_key>" in config.get("api_key", ""):
                config["api_key"] = openai_api_key
            elif "<placeholder_for_azure_openai_api_key>" in config.get("api_key", ""):
                config["api_key"] = azure_openai_api_key

        # Debugging: Print the configuration list
        ic(config_list)

        return config_list

# TODO: Implement other functionalities or methods related to vision processing

