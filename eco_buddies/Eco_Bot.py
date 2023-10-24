import openai
import cv2
from autogen.agentchat import conversable_agent
from PIL import Image
from icecream import ic
from agents.autogen_agents import GeneralManagerAgent, Agent, DigitalTwinAgent
from gbts.gbts import GBTS
class EcoBot_Chat:
    """
    Represents the main bot that interacts with the user.
    Handles user input and generates responses using OpenAI's GPT-4 model.
    """
    
    def __init__(self):
        self.general_manager = GeneralManagerAgent(DigitalTwinAgent,Agent)
        self.personality = self.load_personality()
        self.system_message = GBTS+"Hello! I'm Eco-Bot, The sustainablity AI bot, here to help you with environmental information and tips also Eco-Missions. with my eco-buddies help our plan is to ."

    @staticmethod
    def load_personality():
        """Load the personality script for the bot."""
        try:
            with open("C:/Users/User/OneDrive/Desktop/Buisness/KHM Smart Build/Coding/Projects/OCFS_projects/Eco-Bot/eco_buddies/eco_bot_personality.js", "r") as file:
                return file.read()
        except FileNotFoundError:
            ic("Personality file not found!")
            return ""

    def handle_input(self, user_input):
        """Manage the conversation based on user input."""
        response = self.general_manager.manage_conversation(user_input)
        return response

    def generate_response(self, user_input):
        """Generate a response using OpenAI's GPT-4 model."""
        try:
            response = openai.Completion.create(
                engine="gpt-4",
                prompt=f"{self.system_message} You are Eco-Bot {self.personality}\n{user_input}",
                temperature=0.7,
                max_tokens=8000,
                n=1,
                stop=None,
                log_level="info"
            )
            return response.choices[0].text.strip()
        except Exception as e:
            ic(f"Error generating response: {e}")
            return "Sorry, I couldn't generate a response at the moment."

def process_image(image_path):
    """Process an image and convert it to grayscale."""
    try:
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray_image
    except Exception as e:
        ic(f"Error processing image: {e}")
        return None

# If you want to use the EcoBot_Chat class:
# ecobot_chat = EcoBot_Chat()
# user_input = "How can I reduce my carbon footprint?"
# response = ecobot_chat.generate_response(user_input)
# print(response)
