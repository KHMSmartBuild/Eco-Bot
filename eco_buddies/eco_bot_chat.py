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
    """
    Sets up debugging for the icecream library.

    This function creates a debug folder if it does not already exist. It then generates a timestamp
    using the current date and time, and renames a variable to `debug_timestamp`. It constructs a
    debug file name using the debug folder and the debug timestamp, and opens the file in append
    mode. Finally, it configures the output of the `ic` function from the icecream library to write
    to the debug file.

    Parameters:
    None

    Returns:
    None
    """
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

    def generate_response(self) -> str:
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
        # This code is for v1 of the openai package: pypi.org/project/openai
        try:
            ai_response = openai.chat.completions.create(
            model="gpt-4-1106-preview",
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
            temperature=0.72,
            max_tokens=2772,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            ic(ai_response)  # Debugging statement to print the whole response
            logging.info("Response received: %s", ai_response)    
            if "choices" in ai_response and len(ai_response["choices"]) > 0:
                message = ai_response["choices"][0]["message"]["content"]
                return message
            else:
                logging.error("Unexpected response format: %s", ai_response)
                return "Oops! There was a problem with the AI service. Let's try that again."
        except openai.OpenAIError as e:
            logging.error("An OpenAI-specific error occurred: %s", e)
            return "Oops! There was a problem with the AI service. Let's try that again."
    def handle_input(self,users_input) -> str:
        """
        Generates a response based on the user input.
        """
        logging.info("User input: %s", users_input)
        self.personality["prompt"] = users_input
        bot_response = self.generate_response()
        logging.info("Response: %s", bot_response) 
        return bot_response

# This code will run when you run this file from the command line
bot = EcoBot()
user_input = input("Enter your question for EcoBot: ")
response = bot.handle_input(user_input)  # Pass user_input to handle_input method
print(response)  # This line will output the response to the console.


