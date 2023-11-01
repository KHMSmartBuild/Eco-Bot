import os
from pathlib import Path
# Title for the script
title = """
# Script name: file_structure_tree_updater.py
# location: build_utils
# Function: Generates a file structure tree for the Eco-Bot Project.
# Author: Kyle
# Version: 1.0
# Copyright: KHMSmartBuild
# Date: 29/10/2023
"""

def scan_directory(path, prefix=''):
    tree_structure = ''
    items = os.listdir(path)
    sorted_items = sorted(items)

    gitignore_path = os.path.join(path, '.gitignore')
    gitignore = Path(gitignore_path) if os.path.exists(gitignore_path) else None

    for item in sorted_items:
        if item in ['eco-bot_env', '.env']:
            continue

        item_path = os.path.join(path, item)
        if gitignore and gitignore.match(item_path):
            continue

        if os.path.isdir(item_path):
            tree_structure += f"{prefix}+-- {item}\n"
            tree_structure += scan_directory(item_path, prefix + "    ")
        else:
            tree_structure += f"{prefix}+-- {item}\n"

    return tree_structure

def generate_tree_structure(root_path, output_file):
    tree_structure = scan_directory(root_path)
    with open(output_file, 'w') as file:
        # Write the title to the file
        file.write(title)
        # Write the tree structure to the file
        file.write(tree_structure)

# ...

# Root directory path (one level up from the script's location)
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Output file path in the 'utils' folder
output_file = os.path.join(root_path,'debug_data', 'file_structure_tree.txt')

generate_tree_structure(root_path, output_file)