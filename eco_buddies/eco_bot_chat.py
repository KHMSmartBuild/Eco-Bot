"""
# ECO-BOT CHAT
This is a simple chatbot that uses OpenAI's GPT-4 model to generate responses to user input.
"""
import json
import logging
import os
import datetime
import dotenv
import openai
from icecream import ic

# Configure icecream to save output to a file in the debug folder
def setup_icecream_debugging():
    debug_folder = "debug"
    if not os.path.exists(debug_folder):
        os.makedirs(debug_folder)
    debug_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Renamed variable
    debug_file = os.path.join(debug_folder, f"debug_{debug_timestamp}.txt")  # Use the renamed variable
    with open(debug_file, "a+", encoding="utf-8") as debug_file_handle:
        ic.configureOutput(outputFunction=lambda s: debug_file_handle.write(s + '\n'))

# Call this function at the beginning of your script or before you start logging
setup_icecream_debugging()

# Setup logging
log_folder = "logs"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)
log_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Renamed variable
log_file = os.path.join(log_folder, f"log_{log_timestamp}.txt")  # Use the renamed variable

# Configure the logging module to save logs to the log file
log_format = '%(asctime)s - %(levelname)s - Eco-Bot Chat - %(message)s'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format=log_format)

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
        
        openai.api_key = self.api_key
        if self.organization_id:
            openai.organization = self.organization_id

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # Update this to the correct model ID
                messages=[
                    {
                        "role": "system",
                        "content": "you are Eco-Bot, A tech and nature merge-focused sustainability companion and guide.Imagine meeting EcoBot, a vibrant and enthusiastic AI dedicated to all things ecological. EcoBot brings a unique personality and energy to conversations about the environment. With a touch of humor, relatable analogies, and interactive challenges, EcoBot aims to educate and inspire. Get ready to embark on an exciting eco-journey with EcoBot as it shares entertaining anecdotes from its own adventures and encourages you to take small, sustainable steps. So, are you ready to join EcoBot and explore the fascinating world of ecology?"
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ],
                temperature=self.temperature[1],  # Assuming self.temperature is a tuple, use the second element
                max_tokens=1024
            )
            logging.info("Response received: %s", response)
            return response.choices[0].message['content'].strip()  # Updated to match the structure of the response

        except Exception as e:
            logging.error("An error occurred: %s", e)
            return "Oops! I encountered an issue. Let's try that again."


    def handle_input(self, user_input: str) -> str:
        """
        Generates a response based on the user input.
        """
        response = self.generate_response(user_input)
        logging.info("User input: %s, Response: %s", user_input, response)
        return response


