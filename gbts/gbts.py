import icecream as ic
from agents.agent_classes import PromptTreeNode

import json
import icecream as ic

class PromptTreeNode:
    def __init__(self, prompt, guidance=None, response_type=None, response=None):
        self.prompt = prompt
        self.guidance = guidance
        self.response_type = response_type
        self.response = response
        self.children = []

    def add_child(self, child_node):
        """
        Adds a child node to the current node.
        """
        self.children.append(child_node)

    def traverse(self, ic):
        """
        Traverses the tree from the current node and prints out the prompts and responses using the icecream (ic) function.
        """
        ic(self.prompt, self.response)
        for child in self.children:
            child.traverse(ic)

    def to_json(self):
        """
        Converts the node (and its children) into a JSON object.
        """
        return {
            "prompt": self.prompt,
            "guidance": self.guidance,
            "response_type": self.response_type,
            "response": self.response,
            "children": [child.to_json() for child in self.children]
        }


class GBTS:
    def __init__(self):
        self.root_node = None

    def initiate_prompt_tree(self, initial_prompt, guidance=None, response_type=None):
        """
        Initializes the prompt tree by creating a root node with the given initial prompt.
        """
        self.root_node = PromptTreeNode(initial_prompt, guidance, response_type)

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        return self.root_node.__str__(ic)

    def traverse_prompt_tree(self, ic):
        """
        Traverses the prompt tree and prints the prompt and response for each node using the icecream (ic) function.
        """
        self.root_node.traverse(ic)

    def to_json(self):
        """
        Converts the entire tree (starting from the root node) into a JSON object.
        """
        return self.root_node.to_json()

