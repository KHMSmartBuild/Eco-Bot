import sys
import os
import json
import clip
import autogen as ag
from icecream import ic
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.agent_classes import GeneralManager, Agent, DigitalTwinAgent
from agents.config.config_setup import ConfigSetup

ConfigSetup.load_config(os.path.join("agents", "config", "LLM_config.json"))

# Load API keys from .env file
load_dotenv(os.path.join("agents", "config", ".env"))
openai_api_key = os.getenv("OPENAI_API_KEY")
Orginization_ID = os.getenv("OpenAI_Orginization_ID")

# Create LLM config and save or update the json file with the API key
LLM_config = {
    "model": "gpt-4-1106-preview",
    "api_key": openai_api_key,
    "base_url": Orginization_ID,
}
ConfigSetup.save_config(LLM_config, os.path.join("agents", "config", "LLM_config.json"))

def kwargs(name: str, instruction: str, llm_config: dict = LLM_config):
    name = input("Enter Buddy name: []")
    if name == "":
        name = "EcoBuddy"
    instruction = input("Enter Buddy instruction: []")
    return {"name": name, "instruction": instruction}



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
class EcoBuddy_Vision(BaseEcoBuddy, clip):
    def __init__(self):
        super().__init__()
        # Vision-specific properties and methods
        try:
            self.vision_agent = ag.VisionAgent(Agent)# TODO:ADD VISION AGENT TO AGENT CLASSES
        except:
            self.vision_agent = ag.VisionAgent(DigitalTwinAgent)
        self.clip = clip.load("ViT-B/32", device="cuda")
        # ... other vision-related initializations
        # Add your code here for other vision-related initializations
        # For example:
        # vision_agent = VisionAgent()
        # vision_agent.initialize()
        # vision_agent.load_model()
        # vision_agent.load_data()
        # ...

    def analyze_image(self, image_path):
        # Method to analyze an image file or URL or path with clip
        with open(image_path, "rb") as image_file:
            image = image_file.read()
        image = clip.__package__.load(image)
        # Add your code here to analyze the image
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
    with input("Enter your custom eco-buddy code here: \n"):
        """
        Enter your custom eco-buddy code here: \n
        eco_buddy = eval(input())

        """
        try:
            eco_buddy = eval(input())
            if isinstance(eco_buddy, BaseEcoBuddy):
                return eco_buddy
        except Exception as e:
            print(f"Error creating custom eco-buddy: {e}")
            return None
    

# example usage
# buddy = create_eco_buddy("vision")
# buddy.analyze_image("path_to_image.jpg")

# buddy = create_eco_buddy("audio")
# buddy.analyze_audio("path_to_audio.wav")
    
# buddy = create_custom_eco_buddy("custom")
# buddy.analyze_custom("path_to_custom_data")
    
if __name__ == "__main__":
    buddy = create_eco_buddy("vision")
    buddy.analyze_image("path_to_image.jpg")

    buddy = create_eco_buddy("audio")
    buddy.analyze_audio("path_to_audio.wav")
    
    buddy = create_custom_eco_buddy("custom")
    buddy.analyze_custom("path_to_custom_data")