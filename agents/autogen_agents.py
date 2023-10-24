import json
import os
from agents.config import config_list_gpt4
from eco_buddies import Eco_Bot
from icecream import ic
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample.json
config_list = config_list_from_json(env_or_file="config_list_gpt4")
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})
user_proxy.initiate_chat(assistant, message=("..."))
# This initiates an automated chat between the two agents to solve the task
ic = ic.configureOutput(prefix="")
Eco_Bot = Eco_Bot()
class GeneralManagerAgent:
    """
    A manager class that oversees the conversation between the user and Eco-bot.
    Uses its sub-agents (What, How, Why) to enhance the conversation in real-time.
    """
    
    def __init__(self, eco_bot):
        self.eco_bot = eco_bot
        self.agents = []  # List to store individual agents
        self.digital_twins = []  # List to store digital twin agents
        
        # Configuration for the LLM GPT model
        llm_config = {"config_list": config_list_gpt4, "seed": 42}

        # Define specific agents with their roles and configurations
        self.initialize_agents(llm_config)

    def initialize_agents(self, llm_config):
        """
        Initializes the specific agents and their corresponding digital twins.
        """
        agent_names = ["What_Agent", "How_Agent", "Why_Agent"]
        agent_messages = [
            "I provide factual information.",
            "I provide procedural information.",
            "I provide reasoning and explanations."
        ]

        for name, msg in zip(agent_names, agent_messages):
            agent = AssistantAgent(name=name, system_message=msg, llm_config=llm_config)
            self.agents.append(agent)
            
            # Create a digital twin for each agent
            dta = DigitalTwinAgent(agent)
            self.digital_twins.append(dta)

    def assist_eco_bot(self, user_input):
        """
        The GMA observes the conversation between the user and Eco-bot,
        and uses its sub-agents to assist in real-time.
        """
        # Initial response from Eco-bot
        initial_response = self.eco_bot.respond_to_user(user_input)
        
        # GMA analyzes the response and consults its sub-agents for additional input
        enhanced_response = self.manage_conversation(initial_response)
        
        # Combine the responses or choose the best one
        final_response = self.combine_responses(initial_response, enhanced_response)
        
        return final_response

    def manage_conversation(self, input_message):
        """
        GMA manages the conversation between its sub-agents to enhance the input message.
        """
        # Here, we can implement logic to decide which sub-agent(s) should be consulted
        # based on the content of the input_message.

        # For demonstration, we'll just consult all agents for now.
        responses = []
        for agent in self.agents:
            response = agent.perform_task(input_message)
            responses.append(response)
        
        # Combine or process the responses from the sub-agents
        combined_response = " ".join(responses)
        return combined_response

    def combine_responses(self, initial_response, enhanced_response):
        """
        Combines the initial response from Eco-bot with the enhanced response from the GMA.
        Logic can be added to choose the best parts of each response.
        """
        # For simplicity, we'll concatenate the responses for now.
        return initial_response + " " + enhanced_response

    # ... [Rest of the GeneralManagerAgent class methods]

# ... [Rest of the DigitalTwinAgent, AssistantAgent, and EcoBot classes]

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
    def perform_task_check(self, input_message):
        """
        Performs the agent-specific task based on the input message.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def get_name(self):
        """
        Returns the name of the agent.
        """
        return self.name

    def get_role(self):
        """
        Returns the role of the agent.
        """
        return self.role

    # ... [Rest of the Agent class methods]
        # ... [Any other methods or functionalities you want to add for the Agent class]

class AssistantAgent(Agent):

    
    # Configuration for the LLM GPT model
    def __init__(self, name, system_message, llm_config=None):
        super().__init__(name, "assistant", llm_config)
        self.system_message = system_message

    def perform_task(self, task):
        """
        Perform a specific task. This method can be overridden by subclasses to provide 
        specific functionalities for different types of agents.
        """
        # Basic implementation: just log the task using ic
        ic(f"{self.name} is performing task: {task}")

class EcoBot:
    """
    Represents the main bot that interacts with the user.
    """

def __init__(self,):
    self.name = "Eco-Bot"
    self.role = "pm(Eco_Bot)"
    self.llm_config = {"config_list": EcoBot+config_list_gpt4, "seed": 42}
    self.common_manager = GeneralManagerAgent()
    self.agents = [DigitalTwinAgent(), AssistantAgent()]



def respond_to_user(self, user_input):
    """
    Generates a response to the user's input.
    """
    # Logic to generate a response
    # For demonstration, we'll just return a placeholder response for now.
    return "EcoBot's response to: " + user_input

# ... [Rest of the EcoBot class methods]