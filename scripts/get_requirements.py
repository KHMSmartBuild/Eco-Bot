"""
    This script generates a requirements.txt file for a Python project.
    to run this script, run the following command in the terminal:
    python get_requirements.py
    make sure you have pipdeptree installed:
    pip install pipdeptree
    make sure this script is in the root directory of your project.
"""

import os
import subprocess
from pkg_resources import working_set

def find_python_files(directory):
    """
    Finds all Python files in the given directory and its subdirectories.
    Args:
        directory (str): The directory to search for Python files.
    Returns:
        list: A list of file paths to Python files found in the directory.
    """
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') or file.endswith('.ipynb'):
                python_files.append(os.path.join(root, file))
    return python_files

def extract_imports(file_path):
    """
    Extracts the imported modules from a given file.
    Parameters:
        file_path (str): The path to the file.
    Returns:
        set: A set containing the imported modules.
    """
    imports = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith('import ') or ' import ' in line:
                    imported = line.split()[1].split('.')[0]
                    imports.add(imported)
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            for line in file:
                if line.startswith('import ') or ' import ' in line:
                    imported = line.split()[1].split('.')[0]
                    imports.add(imported)
    return imports


def get_package_versions(packages):
    """
    Retrieves the versions of the specified packages.
    Parameters:
        packages (list): A list of package names.
    Returns:
        dict: 
        A dictionary containing the package names as keys 
        and their corresponding versions as values.
    """
    installed_packages = {pkg.project_name.lower(): pkg.version for pkg in list(working_set)}
    package_versions = {package: installed_packages.get(package.lower()) for package in packages}
    return package_versions

def generate_requirements_txt(package_versions, output_file='requirements.txt'):
    """
    Generate a requirements.txt file with the specified package versions.
    Parameters:
        package_versions (dict): 
        A dictionary containing the package names as keys and the desired versions as values.
        output_file (str, optional): 
        The name of the output file. Defaults to 'requirements.txt'.
    Returns:
        None
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        for package, version in package_versions.items():
            file.write(f"{package}=={version}\n")

def main():
    """
    Generate the requirements.txt file for the project.
    
    This function finds all the Python files in the project directory,
    it then extracts the imports from each file. 
    It then retrieves the versions of the imported packages and generates
    a requirements.txt file with the package versions.
    
    Parameters:
        None
    
    Returns:
        None
    """
    project_directory = '.'  # Replace with your project directory
    python_files = find_python_files(project_directory)

    all_imports = set()
    for file in python_files:
        imports = extract_imports(file)
        all_imports.update(imports)

    package_versions = get_package_versions(all_imports)
    generate_requirements_txt(package_versions)

    # Generate dependency tree
    subprocess.run(["pipdeptree"], check=True)

if __name__ == "__main__":
    main()
