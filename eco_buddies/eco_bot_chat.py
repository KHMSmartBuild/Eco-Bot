"""
# ECO-BOT CHAT
This is a simple chatbot that uses OpenAI's GPT-4 model to generate responses to user input.
"""
import json
import logging
import os

import dotenv
import openai
from icecream import ic

# Setup icecream for debugging
ic.configureOutput(prefix="ECO-BOT Chat | ")

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Load API keys from .env file in the eco_buddies directory
dotenv.load_dotenv(os.path.join(".env"))

api_key = os.getenv("OPENAI_API_KEY", "")
organization_id = os.getenv("OpenAI_Organization_ID", None)
print(f"API Key loaded: {api_key != ''}")



class EcoBot:
    def __init__(self):
        """
        Initializes the class object.

        Parameters:
            None

        Returns:
            None
        """
        self.api_key = api_key
        self.organization_id = organization_id
        self.temperature = ("TEMPERATURE", 0.72)  # 0.72
        self.use_azure = os.getenv("USE_AZURE", "False").lower() == "true"
        current_dir = os.path.dirname(os.path.abspath(__file__))
        eco_bot_personality_file = os.path.join(current_dir, "eco_bot_personality.json")
        with open(eco_bot_personality_file, "r", encoding="utf-8") as file:
            self.personality = json.load(file)

    def generate_response(self, user_input: str) -> str:
        """
        Generates a response based on the user input.

        Args:
            user_input (str): The input provided by the user.

        Returns:
            str: The generated response.

        """
        response = openai.ChatCompletion.create(
            engine=openai.Engine("gpt-4-613"),
            messages=[
                {
                    "role": "system",
                    "content": "you are Eco-Bot, A tech and nature merge-focused sustainability companion and guide."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            temperature=self.temperature,
            max_tokens=1024,
            n=1,
            stop=None,
            presence_penalty=None,
            frequency_penalty=None,
            best_of=None,
            logprobs=None,
            echo=False,
            stop_sequence=None,
            restart_sequence=None,
            context=None,
            model=None,
            prompt=None,
            temperature_schedule=None,
        )
        logging.info(response)
        return response.choices[0].text.strip()

    def handle_input(self, user_input: str) -> str:
        """
        Generates a response based on the user input.
        """
        response = self.generate_response(user_input)
        logging.info(user_input, response)
        return response
