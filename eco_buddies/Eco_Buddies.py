"""
Eco-Buddies Module

This module implements the Eco-Buddies system, which provides specialized
AI assistants for environmental guidance. Eco-Buddies can be customized
for different modalities including vision, audio, and custom interactions.

The module provides:
- Base class for all Eco-Buddy types
- Specialized Eco-Buddies for vision and audio processing
- Factory functions for creating and customizing Eco-Buddies
- Integration with the agent system and GBTS

Classes:
    BaseEcoBuddy: Base class for all Eco-Buddy implementations
    EcoBuddy_Vision: Vision-enabled Eco-Buddy using CLIP
    EcoBuddy_Audio: Audio-enabled Eco-Buddy for voice interactions

Functions:
    create_eco_buddy(buddy_type, **kwargs): Factory for creating Eco-Buddies
    create_custom_eco_buddy(buddy_type, **kwargs): Create custom Eco-Buddy types

Author: KHMSmartBuild
Version: 1.0
"""

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
    """
    Collect Eco-Buddy configuration from user input.
    
    Args:
        name (str): Default name for the Eco-Buddy
        instruction (str): Default instruction for the Eco-Buddy
        llm_config (dict): LLM configuration dictionary
        
    Returns:
        dict: Configuration dictionary with name and instruction
    """
    name = input("Enter Buddy name: []")
    if name == "":
        name = "EcoBuddy"
    instruction = input("Enter Buddy instruction: []")
    return {"name": name, "instruction": instruction}


class BaseEcoBuddy:
    """
    Base class for all Eco-Buddy implementations.
    
    BaseEcoBuddy provides the fundamental infrastructure for all Eco-Buddy types,
    including:
    - Session management with assistant and thread IDs
    - General manager integration for agent coordination
    - Common logging and communication methods
    - Agent initialization and management
    
    Attributes:
        config (dict): Configuration dictionary for the Eco-Buddy
        kwargs (dict): Additional keyword arguments
        general_manager (GeneralManager): Agent coordination manager
        agents (list): List of associated agents
        
    Example:
        >>> buddy = BaseEcoBuddy(config={'model': 'gpt-4'})
        >>> buddy.log("Buddy initialized")
        >>> buddy.communicate("Hello! I'm your Eco-Buddy.")
    """
    
    def __init__(self, config, **kwargs):
        """
        Initialize a Base Eco-Buddy.
        
        Sets up the Eco-Buddy with configuration, restores previous session if
        available, and initializes the general manager and agent list.
        
        Args:
            config (dict): Configuration dictionary containing model settings
            **kwargs: Additional keyword arguments for customization
            
        Attributes initialized:
            config (dict): Stored configuration
            kwargs (dict): Stored additional arguments
            general_manager (GeneralManager): Agent coordination manager
            agents (list): Empty list for agent management
            
        The initialization attempts to restore the previous session by loading:
        - assistant_id: ID of the assistant from last session
        - thread_id: ID of the conversation thread from last session
        
        If no previous session exists, these are set to None.
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
        """
        Log a message for debugging and monitoring.
        
        Args:
            message (str): Message to log
        """
        # Common method to log the provided message
        ic(message)
        
    def communicate(self, message):
        """
        Send a message to the user.
        
        Args:
            message (str): Message to communicate to the user
        """
        # Common method to communicate with the user
        print(message)

    @staticmethod
    def get_last_session_ids():
        """
        Retrieve session IDs from the last session.
        
        Returns:
            tuple: (assistant_id, thread_id, run_id) from previous session
            
        Note:
            This is a placeholder implementation. In production, this should
            read from actual session storage (database, file, etc.)
        """
        # TODO: Implement actual session retrieval logic
        assistant_id = "your_assistant_id"
        thread_id = "your_thread_id"
        run_id = "your_run_id"
        return assistant_id, thread_id, run_id


class EcoBuddy_Vision(BaseEcoBuddy):
    """
    Vision-enabled Eco-Buddy using CLIP for image analysis.
    
    EcoBuddy_Vision extends BaseEcoBuddy with computer vision capabilities
    for analyzing environmental images and videos. It uses the CLIP model
    for visual understanding and can:
    - Analyze images for recycling identification
    - Process video content for environmental assessment
    - Extract environmental insights from visual data
    
    Attributes:
        vision_agent: Vision agent for image processing
        clip: CLIP model instance for visual analysis
        
    Example:
        >>> vision_buddy = EcoBuddy_Vision()
        >>> vision_buddy.analyze_image("recyclable_item.jpg")
        >>> vision_buddy.analyze_video("waste_sorting.mp4")
    """
    
    def __init__(self):
        """
        Initialize Vision Eco-Buddy with CLIP model.
        
        Sets up:
        - Vision agent for image processing
        - CLIP model for visual understanding
        - Integration with base Eco-Buddy functionality
        
        Raises:
            Exception: If CLIP model loading fails
        """
        super().__init__()
        # Vision-specific properties and methods
        try:
            self.vision_agent = ag.VisionAgent(Agent)  # TODO: ADD VISION AGENT TO AGENT CLASSES
        except:
            self.vision_agent = ag.VisionAgent(DigitalTwinAgent)
        self.clip = clip.load("ViT-B/32", device="cuda")
        # Additional vision-related initializations

    def analyze_image(self, image_path):
        """
        Analyze an image file for environmental insights.
        
        Uses CLIP to analyze images and provide environmental guidance,
        such as identifying recyclable materials, assessing waste types,
        or recognizing environmental hazards.
        
        Args:
            image_path (str): Path to the image file, or URL
            
        Returns:
            dict: Analysis results including:
                - identified_items: List of recognized objects
                - recyclability: Recycling classification
                - recommendations: Environmental action suggestions
                
        Example:
            >>> result = vision_buddy.analyze_image("plastic_bottle.jpg")
            >>> print(result['recyclability'])
            'Recyclable - Plastic #1'
        """
        with open(image_path, "rb") as image_file:
            image = image_file.read()
        image = clip.__package__.load(image)
        # TODO: Add image analysis logic
        pass

    def analyze_video(self, video_path):
        """
        Analyze a video file for environmental content.
        
        Processes video content frame-by-frame to identify environmental
        actions, waste management practices, or ecological phenomena.
        
        Args:
            video_path (str): Path to the video file, or URL
            
        Returns:
            dict: Video analysis results
        """
        # TODO: Add video analysis logic
        pass
    
    def analyze_audio(self, audio_path):
        """
        Analyze audio clip for environmental sounds.
        
        Args:
            audio_path (str): Path to audio file
            
        Returns:
            dict: Audio analysis results
        """
        # TODO: Add audio analysis logic
        pass


class EcoBuddy_Audio(BaseEcoBuddy):
    """
    Audio-enabled Eco-Buddy for voice interactions.
    
    EcoBuddy_Audio extends BaseEcoBuddy with audio processing capabilities
    for voice-based environmental guidance and interaction.
    
    Example:
        >>> audio_buddy = EcoBuddy_Audio()
        >>> audio_buddy.analyze_audio("user_question.wav")
    """
    
    def __init__(self):
        """Initialize Audio Eco-Buddy."""
        super().__init__()
        # Audio-specific properties and methods

    def analyze_audio(self, audio_path):
        """
        Analyze an audio clip.
        
        Processes audio input for speech recognition, environmental sound
        identification, or voice-based queries.
        
        Args:
            audio_path (str): Path to the audio clip
            
        Returns:
            dict: Audio analysis results
        """
        # TODO: Add audio analysis logic
        pass


def create_eco_buddy(buddy_type, **kwargs):
    """
    Factory function to create Eco-Buddies of specified types.
    
    Creates and returns an Eco-Buddy instance based on the specified type.
    Supports standard types (vision, audio) and can create custom types.
    
    Args:
        buddy_type (str): Type of Eco-Buddy to create ('vision', 'audio', etc.)
        **kwargs: Additional configuration parameters
        
    Returns:
        BaseEcoBuddy: Instance of the requested Eco-Buddy type
        
    Example:
        >>> vision_buddy = create_eco_buddy("vision")
        >>> audio_buddy = create_eco_buddy("audio")
        >>> custom_buddy = create_eco_buddy("custom", special_feature=True)
    """
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
    """
    Create a custom Eco-Buddy type through user input.
    
    Allows advanced users to create custom Eco-Buddy implementations by
    providing Python code that defines a new Eco-Buddy class.
    
    Args:
        buddy_type (str): Type identifier for the custom buddy
        **kwargs: Additional configuration parameters
        
    Returns:
        BaseEcoBuddy or None: Custom Eco-Buddy instance if successful,
                              None if creation fails
        
    Warning:
        This function uses eval() on user input and should only be used
        in trusted environments. In production, use proper class registration
        instead of eval().
        
    Example:
        >>> custom = create_custom_eco_buddy("recycling_specialist")
        Enter your custom eco-buddy code here:
        # User enters custom class definition
    """
    # Implement your custom eco-buddy creation logic here
    print("Enter your custom eco-buddy code here:")
    print("(Must define a class inheriting from BaseEcoBuddy)")
    
    try:
        # WARNING: Using eval() is dangerous in production
        # This is for development/learning purposes only
        eco_buddy = eval(input())
        if isinstance(eco_buddy, BaseEcoBuddy):
            return eco_buddy
        else:
            print("Error: Custom eco-buddy must inherit from BaseEcoBuddy")
            return None
    except Exception as e:
        print(f"Error creating custom eco-buddy: {e}")
        return None
    

# Example usage
# These examples demonstrate how to use the Eco-Buddy system

if __name__ == "__main__":
    # Example 1: Create and use a vision buddy
    print("Example 1: Vision Eco-Buddy")
    vision_buddy = create_eco_buddy("vision")
    # vision_buddy.analyze_image("path_to_image.jpg")

    # Example 2: Create and use an audio buddy
    print("\nExample 2: Audio Eco-Buddy")
    audio_buddy = create_eco_buddy("audio")
    # audio_buddy.analyze_audio("path_to_audio.wav")
    
    # Example 3: Create a custom buddy (advanced)
    print("\nExample 3: Custom Eco-Buddy")
    # custom_buddy = create_custom_eco_buddy("custom")
    # custom_buddy.analyze_custom("path_to_custom_data")
    
    print("\nEco-Buddies initialized successfully!")