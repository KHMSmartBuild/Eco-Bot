"""
====================================================================================
 Script Name: group_chat.py
 Description:  
    This script allows for the creation of a group chat.
    The group chat can be used to communicate with multiple agents.
    The group chat can be used to create a conversation between multiple agents.

 Location: agents/assistants/group_chat.py
 Company: KindaHelpfulMachines, KHM Smart Build
 Author: Kyle Morgan
 Version: 1.0
 Date: 15-01-2024
 Copyright: KHMSmartBuild
====================================================================================
"""
import os
import json
import icecream as ic
import openai
import autogen 
from autogen.agentchat import AssistantAgent, UserProxyAgent, Agent, GroupChat, GroupChatManager
import logging
import requests
import datetime
import sqlalchemy
from pathlib import Path
from agents.config.llm_config import config_list_str
from agents.config.config_setup import ConfigSetup
from agents.assistants.assistant_retrevial import *
from dotenv import load_dotenv

# set date and time for logging
current_datetime = datetime.datetime.now()
logging.info(f"Current date and time: {current_datetime}")
logging.basicConfig(filename='group_chat.log', 
    level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', 
    filemode='w', datefmt='%Y-%m-%d %H:%M:%S',encoding='utf-8')
# Connect to thepostgresdatabase AgentDB using SQLAlchemy 
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5433/AgentDB')


load_dotenv(os.path.join("agents", "assistants", ".env"))

# Load API keys from .env file and set OpenAI API key 
openai.api_key = os.getenv("OPENAI_API_KEY")


# Load configurations from OAI_CONFIG_LIST.js
config_data = ConfigSetup.load_config_from_js(
    os.path.join("agents", "config", "OAI_CONFIG_LIST.js")
    )

# Create JSON script from config_data
json_script = ConfigSetup.create_config_json(config_data)
try:
    with config_list_str.open('w') as f:
        f.write(json_script)
except:
    print("Error creating JSON script")
    raise

print("Configurations created successfully")
print("Configurations: ", config_list_str)

# create the llm_config from the json script
llm_config = json.loads(json_script)

# Create a list of agents from the asstant_retrevial module
assistant_list = list_assistants()

# Create a list of operations from the assistant_retrevial module
operations = [
    create_assistant,
    list_assistants,
    create_thread,
    get_assistant_names,
    delete_all_assistants,
    retrieve_assistants_by_name,
    delete_assistant,
    get_assistant_by_id
]



def create_group_chat(UserProxyAgent, AssistantAgent, Agent, GroupChat, GroupChatManager):
    """
    Create a group chat with the list of agents specified by the user.
    The group chat can be used to communicate with multiple agents.

    Args:
        assistant_list (list): A list of agents.
        operations (list): A list of operations.
        table_list (list): A list of tables.
        llm_config (dict): A dictionary of configurations.
    """
    # create the group chat loading mechanisms
    def __init__(self, **kwargs):
        """
        Initializes the object with the provided keyword arguments.

        Args:
            **kwargs: The keyword arguments used to initialize the object.

        Returns:
            None
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
    # requirements for the group chat to be created
    def assign_agent_roles(self, agents):
        """
        Assigns roles to the agents in the group chat.

        Args:
            agents (list): A list of agents.

        Returns:
            None
        """
        for agent in agents:
            agent.role = "Agent"
    """
    these are the requirements for the group chat to be created
    1. create group chat with the list of agents specified by the user
    2. create group chat with the list of operations specified by the user
    3. create group chat with the list of tables specified by the user
    4. create group chat with the llm_config specified by the user
    5. each agent should be able to communicate with each other
    6. each agent should have a log of their interactions with the group chat
    7. a manager should be able to manage the group chat
    8. a manager should be able to monitor the group chat
    9. a manager should be able to manage the group chat log 
    10. a userproxy should be able to communicate with the group chat as a user
    11. a userproxy should be able to monitor the group chat as a user
    12. a userproxy should be able to manage the group chat log as a user

    """
    # create the group chat loading mechanisms
    # requirements for the group chat to be created

    