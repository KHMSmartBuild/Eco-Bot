class GeneralManagerAgent:
    def create_agent(self, task):
        agent = Agent(task)
        digital_twin = DigitalTwinAgent(agent)
        return agent, digital_twin

class Agent:
    def __init__(self, task):
        self.task = task

class DigitalTwinAgent:
    def __init__(self, agent):
        self.agent = agent

class PromptTreeNode:
    def __init__(self, prompt, parent=None):
        self.prompt = prompt
        self.parent = parent
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
