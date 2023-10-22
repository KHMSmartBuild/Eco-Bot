import icecream as ic
from agents.agent_classes import PromptTreeNode



class GBTS:
    def __init__(self):
        self.root_node = None

    def initiate_prompt_tree(self, initial_prompt):
        """
        Initializes the prompt tree by creating a root node with the given initial prompt.

        Parameters:
            initial_prompt (str): The initial prompt for the root node.

        Returns:
            None
        """
        self.root_node = PromptTreeNode(initial_prompt)

    # Other methods to traverse, update, and manage the prompt tree

    def __str__(self):
        """
        Returns a string representation of the object.

        :return: A string representation of the object.
        :rtype: str
        """
        return self.root_node.__str__(ic)
    
    #methods to traverse prompt tree
    def traverse_prompt_tree(self,ic):
        """
        Traverses the prompt tree and (ic) the prompt and response for each node.
        """
        self.root_node.traverse(ic)