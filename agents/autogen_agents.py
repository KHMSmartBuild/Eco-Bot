import json
import autogen as ag
from .config import config_list_gpt4
from icecream import ic

class GeneralManagerAgent:
    """
    A manager class that oversees multiple agents and their interactions.
    Designed to run in a containerized environment.
    """
    
    def __init__(self):
        self.agents = []  # List to store individual agents
        self.digital_twin = self.initialize_digital_twin()  # Initialize the digital twin
        
        # Configuration for the LLM GPT model
        llm_config = {"config_list": config_list_gpt4, "seed": 42}

        # Define specific agents with their roles and configurations
        self.initialize_agents(llm_config)

    def initialize_digital_twin(self):
        """
        Initializes and returns the Digital Twin Agent.
        """
        return DigitalTwinAgent()

    def initialize_agents(self, llm_config):
        """
        Initializes the specific agents.
        """
        self.what_agent = ag.AssistantAgent(
            name="What_Agent",
            system_message="I provide factual information.",
            llm_config=llm_config,
        )

        self.how_agent = ag.AssistantAgent(
            name="How_Agent",
            system_message="I provide procedural information.",
            llm_config=llm_config,
        )

        self.why_agent = ag.AssistantAgent(
            name="Why_Agent",
            system_message="I provide reasoning and explanations.",
            llm_config=llm_config,
        )

        # Group chat to manage interactions between agents
        self.groupchat = ag.GroupChat(
            agents=[self.what_agent, self.how_agent, self.why_agent],
            messages=[], max_round=20
        )
        
        # Manager for the group chat
        self.manager = ag.GroupChatManager(groupchat=self.groupchat, llm_config=llm_config)

    # ... [Rest of the GeneralManagerAgent class methods]

class DigitalTwinAgent:
    """
    Represents a digital twin agent used for debugging purposes.
    Designed to run in a separate container and sync with the GMA.
    """
    
    def __init__(self):
        # Initialize the icecream module for debugging
        ic.configureOutput(prefix="DTA Debug | ")

    def log(self, message):
        """
        Logs the provided message.
        """
        ic(message)

    # ... [Rest of the DigitalTwinAgent class methods]


class Agent:
    """
    Base class for all agents managed by the GeneralManagerAgent (GMA).
    """
    
    def __init__(self, name, role, llm_config=None):
        self.name = name  # Name of the agent
        self.role = role  # Role or function of the agent
        self.llm_config = llm_config  # Configuration for the LLM GPT model
        self.status = "idle"  # Current status of the agent (e.g., "idle", "working", "error")

    def perform_task(self, task):
        """
        Perform a specific task. This method can be overridden by subclasses to provide 
        specific functionalities for different types of agents.
        """
        # Basic implementation: just log the task using ic
        ic(f"{self.name} is performing task: {task}")

    def update_status(self, new_status):
        """
        Update the current status of the agent.
        """
        self.status = new_status
        ic(f"{self.name}'s status updated to: {self.status}")

    # ... [Any other methods or functionalities you want to add for the Agent class]
