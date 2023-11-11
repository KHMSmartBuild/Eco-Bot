"""

"""
import os
from icecream import ic
from gbts.gbts import GBTS
from dt.digital_twin import DigitalTwinAgent
from agents.agent_classes import *

# Set up logging with the appropriate level and timestamp
import logging
import datetime

# Configure icecream to save output to a file in the debug folder
def setup_icecream_debugging():
    debug_folder = "debug"
    if not os.path.exists(debug_folder):
        os.makedirs(debug_folder)
    debug_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Renamed variable
    debug_file = os.path.join(debug_folder, f"debug_{debug_timestamp}.txt")  # Use the renamed variable
    with open(debug_file, "a+", encoding="utf-8") as debug_file_handle:
        ic.configureOutput(outputFunction=lambda s: debug_file_handle.write(s + '\n'))

# Call this function at the beginning of your script or before you start logging
setup_icecream_debugging()


# Setup logging
log_folder = "logs"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)
log_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Renamed variable
log_file = os.path.join(log_folder, f"log_{log_timestamp}.txt")  # Use the renamed variable

# Configure the logging module to save logs to the log file
log_format = '%(asctime)s - %(levelname)s - GeneralManagerAgent - %(message)s'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format=log_format)# Load API keys from .env file


class GeneralManager:
    def __init__(self, name, role, llm_config=None):
        # Assuming there is a base class named Agent which GeneralManager inherits from
        super().__init__(name=name)
        self.main_safety_agent = [DigitalTwinAgent(name="Digital Twin Agent")]
        self.understanding_agent = [UnderstandingAgent(name="Understanding Agent")]
        self.task_master = [TaskMaster(name="Task Master")]
        self.task_delegator = [TaskDelegator(name="Task Delegator")]
        self.task_maker = [TaskMaker(name="Task Maker")]
        self.task_executor = [WorkerAgent(name="Task Executor")]
        # ... initialize other agents as appropriate
        self.role = role
        self.llm_config = llm_config
        self.agents = [SafetyAgent]  # Simplified list for illustration
        self.gbts = GBTS()
        self.gbts.build_from_conversation("Seed of Inquiry")
        self.digital_twin = DigitalTwinAgent()

    def handle_message(self, message):
        try:
            response = self.understanding_agent.handle_message(message)
        except Exception as e:
            error_response = self.error_handling_safety_agent.handle_message(str(e))
            return error_response
        return response

    def monitor_safety(self, script):
        if "unsafe" in script:
            alert = self.main_safety_agent.handle_message("Safety breach detected!")
            return alert
        return "Script is safe"

    # Additional methods like create_agent, manage_conversation, etc.