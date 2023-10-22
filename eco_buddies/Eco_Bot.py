import autogen as ag
import openai
import cv2  # OpenCV for computer vision
from PIL import Image
from icecream import ic
from agents.autogen_agents import GeneralManagerAgent, Agent, DigitalTwinAgent

# Load personality script
with open("eco-buddies/eco-bot_personality.js", "r") as file:
    personality_script = file.read()

class EcoBot:
    def __init__(self):
        self.general_manager = GeneralManagerAgent()
        self.personality = self.load_personality()

    @staticmethod
    def load_personality():
        with open("eco-buddies/eco-bot_personality.js", "r") as file:
            return file.read()

    def handle_input(self, user_input):
        response = self.general_manager.manage_conversation(user_input)
        return response

def process_image(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image  # or other processed image data

class EcoBot_Chat:
    def __init__(self):
        self.general_manager = GeneralManagerAgent()
        self.personality = self.load_personality()
        self.system_message = "Hello! I'm Eco-Bot, here to help you with environmental information and tips."

    @staticmethod
    def load_personality():
        with open("eco-buddies/eco-bot_personality.js", "r") as file:
            return file.read()
        
    def handle_input(self, user_input):
        response = self.general_manager.manage_conversation(user_input)
        return response

    def generate_response(self, user_input):
        # Use OpenAI's GPT-4 model for chat completions
        # Note: You might need to adjust this based on the latest OpenAI API documentation
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=f"{self.system_message}you are Eco-Bot {self.personality}\n{user_input}",
            temperature=0.7,
            max_tokens=8000,
            n=1,
            stop=None,
            log_level="info"
        )
        return response.choices[0].text.strip()

# If you want to use the EcoBot_Chat class:
# ecobot_chat = EcoBot_Chat()
# user_input = "How can I reduce my carbon footprint?"
# response = ecobot_chat.generate_response(user_input)
# print(response)
