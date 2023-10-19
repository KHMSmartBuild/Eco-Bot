from agents.agent_classes import PromptTreeNode


class GBTS:
    def __init__(self):
        self.root_node = None

    def initiate_prompt_tree(self, initial_prompt):
        self.root_node = PromptTreeNode(initial_prompt)

    # Other methods to traverse, update, and manage the prompt tree
