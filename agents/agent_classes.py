"""
This is the agent class.
the script is acting as a library for the agent classes.
The agent class is responsible for creating the agent and the digital twin agent.


"""
import os
import sys
import json
import openai
from dotenv import load_dotenv
import autogen
from autogen.agentchat import AssistantAgent, UserProxyAgent, Agent, GroupChat, GroupChatManager
from agents.dt.digital_twin import DigitalTwinAgent


class GeneralManager():
    def __init__(self, name, role, llm_config=None):
        super().__init__(name=name)
        self.understanding_agent = UnderstandingAgent(name="Understanding Agent", role=GroupChatManager)
        self.task_master = TaskMaster(name="Task Master", role=AssistantAgent)
        self.main_safety_agent = SafetyAgent(name="Main Safety Agent", role=AssistantAgent)
        self.error_handling_safety_agent = SafetyAgent(name="Error Handling Safety Agent", role=AssistantAgent)
        self.digital_twin_agent = DigitalTwinAgent(name="Digital Twin Agent", role=AssistantAgent)
        self.agents = [DigitalTwinAgent(), AssistantAgent()]
        self.add_subordinate_agents(self.agents, role=Agent)
        self.add_subordinate_agents([self.task_master, self.main_safety_agent, self.error_handling_safety_agent, self.digital_twin_agent], role=AssistantAgent)
        self.llm_config = llm_config
        self.role = UserProxyAgent
    def handle_message(self, message):
        # This is a simplified representation.
        # Here, you can add logic to decide which agent the message should be forwarded to.
        
        # For the sake of illustration, let's assume all messages are tasks and send them to Task Master
        get_responses = self.understanding_agent.handle_message(message)

        # Error handling
        if "error" in response.lower():
            # Handle errors, potentially sending it to Error Handling Safety Agent
            error_response = self.error_handling_safety_agent.handle_message(response)
            return error_response
        
        return response
    
    def monitor_safety(self, script):
        # Safety monitoring can be done here.
        # For the sake of simplicity, let's assume any script that contains the word "unsafe" is flagged.
        if "unsafe" in script:
            alert = self.main_safety_agent.handle_message("Safety breach detected!")
            return alert
        return "Script is safe"

    def create_agent(self, task):
        """
        Create an agent and a digital twin agent for the given task.
        
        Args:
            task (str): The task for the agent.
        
        Returns:
            tuple: A tuple containing the agent and the digital twin agent.
        """
        agent = Agent(task)
        digital_twin = DigitalTwinAgent(agent)
        return agent, digital_twin
    


class Agent:
    def __init__(self, task):
        """
        Initialize an Agent instance.
        
        Args:
            task (str): The task for the agent.
        """
        self.task = task
    
    def handle_task(self, user_input):
        """
        Handle the task for the user input.
        
        Args:
            user_input (str): The user input.
        
        Returns:
            str: The response to the user input.
        """
        response = f"Handling task: {self.task} for input: {user_input}"
        return response

class DigitalTwinAgent:
    def __init__(self, agent):
        """
        Initialize a DigitalTwinAgent instance.
        
        Args:
            agent (Agent): The agent to create a digital twin for.
        """
        self.agent = agent

class PromptTreeNode:
    def __init__(self, prompt, parent=None):
        """
        Initialize a PromptTreeNode instance.
        
        Args:
            prompt (str): The prompt for the tree node.
            parent (PromptTreeNode, optional): The parent node. Defaults to None.
        """
        self.prompt = prompt
        self.parent = parent
        self.children = []

    def add_child(self, child_node):
        """
        Add a child node to the current node.
        
        Args:
            child_node (PromptTreeNode): The child node to add.
        """
        self.children.append(child_node)

    def remove_child(self, child_node):
        """
        Remove a child node from the current node.
        
        Args:
            child_node (PromptTreeNode): The child node to remove.
        """
        self.children.remove(child_node)

    def get_child(self, index):
        """
        Get the child node at the specified index.
        
        Args:
            index (int): The index of the child node.
        
        Returns:
            PromptTreeNode: The child node at the specified index.
        """
        return self.children[index]
    
    def get_parent(self):
        """
        Get the parent node.
        
        Returns:
            PromptTreeNode: The parent node.
        """
        return self.parent
    
    def get_children(self):
        """
        Get the list of children nodes.
        
        Returns:
            list: The list of children nodes.
        """
        return self.children
    
    def __str__(self):
        """
        Get the string representation of the node.
        
        Returns:
            str: The prompt
        """
        return self.prompt
    
video_platform = "YouTube"

# pictory_agent.py

class PictoryAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_imagery(self, keywords):
        """
        Generate imagery based on the provided keywords using the Pictory API.
        
        Parameters:
            keywords (list): List of keywords extracted from the conversation.

        Returns:
            str: URL or path to the generated imagery.
        """
        # Placeholder logic for Pictory API integration
        # In practice, you'll need to make an API call to Pictory with the keywords
        # and then retrieve the URL or path to the generated imagery.
        
        # For demonstration purposes:
        imagery_url = "https://example.com/path/to/generated/imagery.jpg"
        
        return imagery_url

    def out(self, user_input):
        """
        This function can be invoked from the chat to handle specific tasks related to the Pictory agent.
        
        Parameters:
            user_input (str): Input or command from the user.

        Returns:
            str: Response or feedback to the user.
        """
        # Placeholder logic to handle user input
        # Depending on the user_input, this function can perform specific tasks
        # related to the Pictory agent and return an appropriate response.
        
        response = "Pictory agent received your input."
        return response

class UnderstandingAgent(autogen.Agent):
    def __init__(self, name):
        super().__init__(name=name)
        # Initialize sub-agents
        self.what_agent = WhatAgent(name="What Agent")
        self.how_agent = HowAgent(name="How Agent")
        self.why_agent = WhyAgent(name="Why Agent")
        
    def handle_message(self, message):
        # Logic to determine which sub-agent to send the message to
        if "what" in message.lower():
            return self.what_agent.handle_message(message)
        elif "how" in message.lower():
            return self.how_agent.handle_message(message)
        elif "why" in message.lower():
            return self.why_agent.handle_message(message)
        else:
            # Default behavior or error handling
            return f"Don't understand the message: {message}"

class WhatAgent(autogen.Agent):
    def handle_message(self, message):
        # Logic for handling "what" related queries
        return f"Handling 'What' query: {message}"

class HowAgent(autogen.Agent):
    def handle_message(self, message):
        # Logic for handling "how" related queries
        return f"Handling 'How' query: {message}"

class WhyAgent(autogen.Agent):
    def handle_message(self, message):
        # Logic for handling "why" related queries
        return f"Handling 'Why' query: {message}"
class TaskMaster(autogen.Agent):
    def handle_message(self, message):
        # Here, tasks can be managed, delegated, or processed.
        # For the sake of simplicity, let's just return the message.
        return f"Task received: {message}"

class SafetyAgent(autogen.Agent):
    def handle_message(self, message):
        # Handle safety-related messages.
        return f"Alert: {message}"
class TaskMaker(autogen.Agent):
    def __init__(self, name):
        super().__init__(name=name)
        # You can initialize other attributes if necessary

    def formulate_task(self, message):
        # Based on the message or other criteria, create a task.
        # This is a simplified representation; real-world scenarios would require more complex logic.
        task = f"Formulated Task: {message}"
        return task
class TaskDelegator(autogen.Agent):
    def __init__(self, name, worker_agents):
        super().__init__(name=name)
        self.worker_agents = worker_agents  # A list or dictionary of worker agents

    def delegate_task(self, task):
        # Decide which worker agent should handle the task.
        # Here's a very simplified mechanism: round-robin assignment.
        # In real-world applications, you'd use more sophisticated task assignment logic.
        
        worker_agent = self.worker_agents.pop(0)
        self.worker_agents.append(worker_agent)
        
        response = worker_agent.handle_message(task)
        return response
worker_agents = [WorkerAgent(name=f"Worker Agent {chr(i)}") for i in range(65, 72)]  # A, B, C, ... G
task_maker = TaskMaker(name="Task Maker")
task_delegator = TaskDelegator(name="Task Delegator", worker_agents=worker_agents)

# Example usage:
task = task_maker.formulate_task("Analyze dataset X")
response = task_delegator.delegate_task(task)

class WorkerAgent(autogen.Agent):
    def __init__(self, name, speciality=None):
        super().__init__(name=name)
        self.speciality = speciality  # Each worker agent might have a speciality or area of expertise

    def handle_message(self, message):
        # This is where the main logic of the worker agent will reside.
        # For now, it's a placeholder. It will acknowledge the task and note its speciality.

        # Logic to handle the task based on the message and the agent's speciality
        # ...

        response = f"{self.name} with speciality {self.speciality} acknowledges task: {message}"
        return response

    # You can add more methods specific to the tasks the worker agents might perform.

class EcoBot(autogen.Agent):
    def __init__(self, name):
        super().__init__(name=name)
        # Initialize the Understanding Agent
        self.understanding_agent = UnderstandingAgent(name="Understanding Agent")
        
    def handle_message(self, message):
        # Forward the message to the Understanding Agent for processing
        response = self.understanding_agent.handle_message(message)
        return response

    def initiate_chat(self, message):
        # For starting a conversation with the user
        print(f"Eco-Bot: {message}")
        while True:
            user_input = input("User: ")
            if user_input.lower() in ["exit", "quit", "terminate"]:
                print("Eco-Bot: Goodbye!")
                break
            response = self.handle_message(user_input)
            print(f"Eco-Bot: {response}")
