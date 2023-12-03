import sys
import os
import json
import clip
import autogen as ag
from icecream import ic
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.agent_classes import GeneralManager, Agent, DigitalTwinAgent
from agents.config.config_setup import *

# Load API keys from .env file
load_dotenv(os.path.join("agents", "config", ".env"))
openai_api_key = os.getenv("OPENAI_API_KEY")
Orginization_ID = os.getenv("OpenAI_Orginization_ID")

# set up llm config
with create_config_json as config:
    config["api_key"] = openai_api_key

kwargs = {
    "api_key": openai_api_key,
    "organization_id": Orginization_ID,
    "model": print_config_json,
}



class BaseEcoBuddy(id='', thread_id='', **kwargs):
    def __init__(self,config, **kwargs):
        """
        Initializes a new instance of the class.

        Args:
            config (dict): The configuration dictionary.
            **kwargs: Additional keyword arguments.

        Attributes:
            config (dict): The configuration dictionary.
            kwargs (dict): Additional keyword arguments.
            assistant_id (str): The ID of the assistant from the last session.
            thread_id (str): The ID of the thread from the last session.
            general_manager (GeneralManager): The instance of the GeneralManager class.
            agents (list): The list of agents.

        Returns:
            None
        """
        self.config = config
        self.kwargs = kwargs
        # get assistant id and tread id from last session
        try:
            with open('session.logs.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                assistant_id = data['assistant_id']
                thread_id = data['thread_id']
        except FileNotFoundError:
            assistant_id = None
            thread_id = None
        # Initialize the general manager
        self.general_manager = GeneralManager()
        # Initialize the agents as needed
        self.agents = []

    def log(self, message):
        # Common method to log the provided message
        ic(message)
    def communicate(self, message):
        # Common method to communicate with the user
        print(message)

    def get_last_session_ids():
            # Your code here to retrieve the assistant ID and thread ID from the last session
            assistant_id = "your_assistant_id"
            thread_id = "your_thread_id"
            run_id = "your_run_id"
            return assistant_id, thread_id, run_id
class EcoBuddy_Vision(BaseEcoBuddy):
    def __init__(self):
        super().__init__()
        # Vision-specific properties and methods
        self.vision_agent = ag.VisionAgent(Agent)
        # ... other vision-related initializations

    def analyze_image(self, image_path):
        # Method to analyze an image file or URL or path with clip
        pass

    def analyze_video(self, video_path):
        # Method to analyze a video file or URL or path with clip
        pass
    
    def analyze_audio(self, audio_path):
        # Method to analyze an audio clip
        pass

    # ... other specialized eco-buddies

class EcoBuddy_Audio(BaseEcoBuddy):
    def __init__(self):
        super().__init__()
        # Audio-specific properties and methods

    def analyze_audio(self, audio_path):
        # Method to analyze an audio clip
        pass

# ... other specialized eco-buddies

def create_eco_buddy(buddy_type, **kwargs):
    eco_buddies = {
        "vision": EcoBuddy_Vision,
        "audio": EcoBuddy_Audio,
        # ... other eco-buddies
    }
    
    eco_buddy_class = eco_buddies.get(buddy_type, None)
    if eco_buddy_class:
        return eco_buddy_class()
    
    return create_custom_eco_buddy(buddy_type, **kwargs)
    
def create_custom_eco_buddy(buddy_type, **kwargs):
    # Implement your custom eco-buddy creation logic here
    

# example usage
# buddy = create_eco_buddy("vision")
# buddy.analyze_image("path_to_image.jpg")
