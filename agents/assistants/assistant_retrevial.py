"""This module contains functions for creating and retrieving assistants."""
import os
import openai
import requests
from dotenv import load_dotenv
load_dotenv('../config/.env')


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ORGANIZATION_ID = os.getenv("ORGANIZATION_ID")
BASE_URL = "https://api.openai.com/v1/assistants"


# Initialize OpenAI client with API key
openai.api_key = OPENAI_API_KEY
openai.organization = ORGANIZATION_ID

def list_assistants():

    assistant_object = openai.beta.assistants.list()
    return assistant_object

HEADERS = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

def delete_assistant(assistant_id):
    """Delete an assistant by ID."""
    delete_url = f"{BASE_URL}/{assistant_id}"
    response = requests.delete(delete_url, headers=HEADERS, timeout=10)

    if response.status_code == 200:
        print(f"Deleted assistant with ID: {assistant_id}")
    else:
        print(f"Failed to delete assistant with ID: {assistant_id}. Status Code: {response.status_code}")


def delete_all_assistants():
    """Delete all assistants."""
    a_list = list_assistants()
    assitant_obj_list = a_list.data
    for i in range(len(assitant_obj_list)):
        delete_assistant(assitant_obj_list[i].id)

def select_assistant(assistant_id):
    """
    Retrieves an assistant object using the given assistant ID.

    Args:
        assistant_id (str): The ID of the assistant to retrieve.

    Returns:
        str: The ID of the retrieved assistant.
    """
    # Use the 'beta.assistants' attribute, not 'Assistant'
    assistant = openai.beta.assistants.retrieve(assistant_id)
    return assistant.id

def create_assistant(name, instructions, tools, model):
    """
    Create an assistant with the given name, instructions, tools, and model.

    Parameters:
        name (str): The name of the assistant.
        instructions (str): The instructions for the assistant.
        tools (list): The tools used by the assistant.
        model (str): The model used by the assistant.

    Returns:
        str: The ID of the created assistant.
    """
    assistant = openai.beta.assistants.create(
        name=name,
        instructions=instructions,
        tools=tools,
        model=model
    )
    return assistant.id  # Return the assistant ID



def get_assistant_by_id(assistant_id):
    """
    Retrieves an assistant object from the database based on the provided assistant_id.

    Parameters:
        assistant_id (str): The ID of the assistant to retrieve.

    Returns:
        str: The ID of the retrieved assistant.
    """
    assistant = openai.beta.assistants.retrieve(assistant_id)
    return assistant.id


def create_thread():
    """
    Creates a new thread.

    :return: The newly created thread.
    """
    thread = openai.beta.threads.create()
    return thread


