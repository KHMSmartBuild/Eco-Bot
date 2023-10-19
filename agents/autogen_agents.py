import autogen as ag
from icecream import ic

class GeneralManagerAgent:
    def __init__(self):
        self.agents = []
        self.digital_twin = DigitalTwinAgent()
        llm_config = {"config_list": config_list_gpt4, "seed": 42}

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

        self.groupchat = ag.GroupChat(
            agents=[self.what_agent, self.how_agent, self.why_agent],
            messages=[], max_round=20
        )
        self.manager = ag.GroupChatManager(groupchat=self.groupchat, llm_config=llm_config)


    def manage_conversation(self, user_input):
        # Determine which sub-agent(s) should respond based on the nature of the user_input
        # Hypothetical criteria for routing user input
        if "fact" in user_input:
            agent = self.what_agent
        elif "how to" in user_input:
            agent = self.how_agent
        elif "why" in user_input:
            agent = self.why_agent
        else:
            agent = None  # No suitable agent found

        if agent:
            response = agent.handle_task(user_input)  # Assume handle_task is a method of ag.AssistantAgent
            # Add response to group chat
            self.groupchat.add_message(agent.name, response)
            # Optionally, send the response to digital twin for logging/debugging
            self.digital_twin.log_and_debug(response)
        else:
            print("No suitable agent found for input:", user_input)

   
    def create_agent(self, task):
        agent = Agent(task)
        self.agents.append(agent)
        return agent


class Agent:
    def __init__(self, task):
        self.task = task
        self.name = "Agent"

    def handle_task(self, user_input):
        response = f"Handling task: {self.task} for input: {user_input}"
        return response

class DigitalTwinAgent:
    def log_and_debug(self, conversation):
        ic(conversation)  # Debugging with IceCream

def initiate_conversation(user_input):
    manager = GeneralManagerAgent()
    manager.create_agent("Example Task")
    manager.manage_conversation(user_input)