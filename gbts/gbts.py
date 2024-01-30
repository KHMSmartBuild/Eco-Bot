"""
This module defines the GBTS class and related functionalities for managing conversation trees.
"""

import json
import matplotlib.pyplot as plt
import networkx as nx


class PromptTreeNode:
    """
    Represents a node in the PromptTree.
    """
    def __init__(self, role, message):
        """
        Initializes a new instance of the class.

        Args:
            role (str): The role of the instance.
            message (str): The message of the instance.

        Returns:
            None
        """
        self.role = role
        self.message = message
        self.children = []

    def add_child(self, child_node):
        """
        Adds a child node to the current node.

        Parameters:
            child_node (Node): The node to be added as a child.

        Returns:
            None
        """
        self.children.append(child_node)

    def traverse(self, graph, parent_name, node_name):
        """
        Traverse the graph and add nodes and edges to represent the tree structure.

        Args:
            graph (Graph): The graph object to add nodes and edges to.
            parent_name (str): The name of the parent node.
            node_name (str): The name of the current node.

        Returns:
            None
        """
        graph.add_node(node_name, label=self.message)
        if parent_name:
            graph.add_edge(parent_name, node_name)
        for child in self.children:
            child.traverse(graph, node_name, f"{node_name}-{child.message[:5]}")

    
class GBTS:
    """
    Represents a conversation tree with methods to traverse and visualize the tree.
    """

    def __init__(self):
        """
        Initializes a new instance of the class.
        """
        self.root_node = None
        
    def build_from_conversation(self, conversation):
        """
        Builds a PromptTree from a given conversation.

        Args:
            conversation (List[Dict[str, str]]): A list of dictionaries representing the conversation.
                Each dictionary should have the keys "role" and "message", representing the role of the
                speaker and the message they sent, respectively.

        Returns:
            None: If the conversation is empty.
        """
        if not conversation:
            return
        first_message = conversation[0]
        self.root_node = PromptTreeNode(first_message["role"], first_message["message"])
        current_node = self.root_node
        for message in conversation[1:]:
            new_node = PromptTreeNode(message["role"], message["message"])
            current_node.add_child(new_node)
            current_node = new_node
            self.node_counter = 0

    def visualize(self):
        """
        Visualizes the graph representation of the tree structure.

        Parameters:
            None

        Returns:
            None
        """
        graph = nx.DiGraph()
        if self.root_node:
            self.root_node.traverse(graph, None, self.root_node.message[:5])
        self.node_counter += 1
        pos = nx.spring_layout(graph)
        labels = {node: graph.nodes[node]['label'] for node in graph.nodes()}
        plt.figure(figsize=(10, 6))
        nx.draw(graph, pos, labels=labels, with_labels=True, node_size=3000, node_color="skyblue")
        plt.show()

def visualize_conversation_tree(conversation, structure=None):
    """
    Generate a visualization of a conversation tree.

    Parameters:
        conversation (list): A list of strings representing the conversation.
        structure (Optional): An optional structure object to define the tree structure.

    Returns:
        None
    """
    tree = GBTS()
    tree.build_from_conversation(conversation)
    tree.visualize()

# Load the JSON structure
with open("../gbts/GBTS.json", "r", encoding="utf-8") as file:
    prompt_structure = json.load(file)

# Sample usage:
conversation = [
    {"role": "user", "message": "explain how i can make my own compost"},
    {"role": "assistant", "message": "Seed of Inquiry: The question you've posed is about creating your own compost. This is a fantastic initiative! Composting is an excellent way to recycle organic waste, reduce landfill contributions and enhance soil health in your garden."},
    {"role": "assistant", "message": "Branches of Understanding: Creating compost involves several related topics. We need to discuss the types of waste that are suitable for composting, the composting process itself, which includes the balance of green and brown materials, moisture, air circulation, and temperature. Additionally, we could explore the timeline and stages of compost maturation, the benefits of composting for soil health and food production, and potential challenges one might encounter in the process."},
    {"role": "assistant", "message": "Leaves of Application: Applying this knowledge involves setting up your composting system - whether it's a compost heap, bin, or tumbler. You'd need to collect green waste like fruit and vegetable peels or grass clippings and brown waste such as dried leaves or paper. Maintaining the right balance, turning the compost regularly, and ensuring it's moist but not wet are all essential steps. Once mature, compost can be used in your garden to enrich the soil and boost plant growth."},
    {"role": "assistant", "message": "Roots of Connection (Infranodes): This practice connects with broader subjects like waste management, sustainable agriculture, and soil science. It also ties into concepts of circular economy - where waste is not just discarded but returned back into the system as a resource. Moreover, it has implications on climate change as composting reduces methane emissions from landfills."},
    {"role": "assistant", "message": "Forest of Exploration: From here, we could branch into discussions about other sustainable practices such as rainwater harvesting, permaculture, or even renewable energy. These all contribute to a more sustainable lifestyle and a healthier planet."},
    {"role": "assistant", "message": "Canopy of Synthesis: By exploring the process and benefits of composting, we gain insights into its role in sustainability. It is a practical application of the circular economy concept, contributing to waste reduction and healthier soils. This understanding could inspire further exploration into sustainable living practices."},
    {"role": "assistant", "message": "Harvest of Wisdom: The key insight here is that composting is a simple yet effective way to contribute to environmental sustainability. It reduces waste, improves soil health, and can even stimulate a wider interest in other sustainable practices. This exploration not only answers your initial question but paints a broader picture of how individual actions can contribute to global sustainability."},
    {"role": "user", "message": "Eco-Bot can you give me a eco-mission to complete this week"},
    {"role": "assistant", "message": "Absolutely! I'm thrilled to see your enthusiasm. Here's your eco-mission for this week: Mission: 'Zero Waste Week Challenge' Objective: Reduce the amount of waste you generate in a week. Steps: 1. Audit Your Waste: For the first two days, don't change anything about your routine. Instead, keep track of all the waste you produce. This will serve as a baseline for your mission. 2. Identify Areas of Improvement: Look at your waste and identify where you can make changes. Is there a lot of food waste? Are there many disposable items? 3. Implement Changes: Try to reduce your waste by making small changes. Here are few ideas: Bring a reusable bag for shopping. Use a refillable water bottle instead of buying bottled water. Cook meals at home and try to use all parts of your ingredients to minimize food waste. Compost your organic waste. Recycle items like paper, metal, glass, and certain types of plastic. 4. Reflect: At the end of the week, take stock. How much were you able to reduce your waste? What worked, and what was challenging? Remember, the goal is not perfection but improvement. Every little bit counts towards a more sustainable world. Good luck on your mission!"}
]


visualize_conversation_tree(conversation, prompt_structure)

