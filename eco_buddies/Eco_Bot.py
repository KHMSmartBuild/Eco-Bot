import openai
import cv2
from PIL import Image
from icecream import ic
from ..agents.agent_classes import GeneralManager, Agent, DigitalTwinAgent
from ..gbts.gbts import GBTS

class EcoBot_Chat:
    """
    Represents the main bot that interacts with the user.
    Handles user input and generates responses using OpenAI's GPT-4 model.
    """

    def __init__(self):
        self.general_manager = GeneralManager(self)
        self.personality = self.load_personality()
        self.system_message = "Hello! I'm Eco-Bot, The sustainability AI bot, here to help you with environmental information and tips also Eco-Missions. With my eco-buddies' help, our plan is to..."
        self.gbts = GBTS()
        self.gbts.build_from_conversation("Seed of Inquiry")

    @staticmethod
    def load_personality():
        """Load the personality script for the bot."""
        try:
            with open("C:/Users/User/OneDrive/Desktop/Buisness/KHM Smart Build/Coding/Projects/OCFS_projects/Eco-Bot/eco_buddies/eco_bot_personality.js", "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            ic("Personality file not found!")
            return ""

    def handle_input(self, user_input):
        """Manage the conversation based on user input."""
        response = self.general_manager.manage_conversation(user_input)

        # If the user's input matches the expected response type for the current GBTS node
        if self.gbts.root_node.response_type == "Open Dialogue":
            # Save user's response in the current node
            self.gbts.root_node.response = user_input

            # Move to the next node in GBTS based on user's input (for simplicity, moving to the first child)
            if self.gbts.root_node.children:
                self.gbts.root_node = self.gbts.root_node.children[0]

            # Provide the prompt for the next node
            next_prompt = self.gbts.root_node.prompt
        else:
            # If user's response doesn't match the expected response type, provide guidance
            next_prompt = self.gbts.root_node.guidance

        return response, next_prompt

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
        

    # Update the GBTS tree based on the user's response
    def initiate_prompt_tree(self, user_response):
        """Update the GBTS tree based on the user's response."""
        self.gbts.root_node.response = user_response
