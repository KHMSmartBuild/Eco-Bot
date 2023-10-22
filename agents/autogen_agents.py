import json
import autogen as ag
from .config import config_list_gpt4
from icecream import ic

class GeneralManagerAgent:
    """
    A manager class that oversees multiple agents and their interactions.
    """
    
    def __init__(self):
        """
        Initializes the GeneralManagerAgent with specific agents and configurations.
        """
        self.agents = []  # List to store individual agents
        self.digital_twin = DigitalTwinAgent()  # Digital twin for debugging
        
        # Configuration for the LLM GPT model
        llm_config = {"config_list": config_list_gpt4, "seed": 42}

        # Define specific agents with their roles and configurations
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

    def manage_conversation(self, user_input):
        """
        Manages the conversation by routing the user input to the appropriate agent.
        
        Args:
            user_input (str): The input provided by the user.
        """
        # Determine which sub-agent(s) should respond based on the nature of the user_input
        if "fact" in user_input:
            agent = self.what_agent
        elif "how to" in user_input:
            agent = self.how_agent
        elif "why" in user_input:
            agent = self.why_agent
        else:
            agent = None  # No suitable agent found

        if agent:
            # Get the response from the appropriate agent
            response = agent.handle_task(user_input)
            
            # Add the agent's response to the group chat
            self.groupchat.add_message(agent.name, response)
            
            # Optionally, send the response to digital twin for logging/debugging
            self.digital_twin.log_and_debug(response)
        else:
            print("No suitable agent found for input:", user_input)

    def create_agent(self, task):
        """
        Creates a new agent for a specific task.
        
        Args:
            task (str): The task for which the agent is created.
        
        Returns:
            Agent: The newly created agent.
        """
        agent = Agent(task)
        self.agents.append(agent)
        return agent

class Agent:
    """
    Represents an individual agent that can handle specific tasks.
    """
    
    def __init__(self, task):
        """
        Initializes the Agent with a specific task.
        
        Args:
            task (str): The task assigned to the agent.
        """
        self.task = task
        self.name = "Agent"
        self.analyze_user_behavior = GeneralManagerAgent.analyze_user_behavior

    def handle_task(self, user_input):
        """
        Handles the assigned task based on the user input.
        
        Args:
            user_input (str): The input provided by the user.
        
        Returns:
            str: The response to the user input.
        """
        response = f"Handling task: {self.task} for input: {user_input}"
        return response

    # ... [Rest of the Agent class methods with docstrings and comments]

class DigitalTwinAgent:
    """
    Represents a digital twin agent used for debugging purposes.
    """
    
    def log_and_debug(self, conversation):
        """
        Logs and debugs the conversation using the IceCream module.
        
        Args:
            conversation (str): The conversation to be logged and debugged.
        """
        ic(conversation)  # Debugging with IceCream

    def __str__(self):
        """
        Get the string representation of the agent.
        
        Returns:
            str: The name of the agent.
        """
        return self.name
    
    def __repr__(self):
        """
        Get the string representation of the agent.

        Returns:
            str: The name of the agent.
        """
        return self.name
    
    def __hash__(self):
        """
        Get the hash value of the agent.
        """
        return hash(self.name)
    
    def __eq__(self, other):
        """
        Check if two agents are equal. with usync for live error checking
        """
        with ag.usync():
            return self.name == other.name
        
    def __ne__(self, other):
        """
        Check if two agents are not equal.
        """
        with ag.usync():
            return self.name != other.name
        
    def __lt__(self, other):

        """
        Check if two agents are less than.
        """

        return self.name == other.name
    

    def __gt__(self, other):
        """
        Check if two agents are greater than.
        """
        return self.name == other.name
# ... [Rest of the code with docstrings and comments]
