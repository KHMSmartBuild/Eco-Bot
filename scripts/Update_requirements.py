import os
import subprocess
import pkg_resources

def find_python_files(directory):
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') or file.endswith('.ipynb'):
                python_files.append(os.path.join(root, file))
    return python_files

def extract_imports(file_path):
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

def get_installed_pip_packages():
    installed_packages = subprocess.run(['pip', 'freeze'], capture_output=True, text=True, check=True).stdout
    return {line.split('==')[0].lower() for line in installed_packages.split('\n') if line}

def filter_pip_imports(imports, pip_packages):
    return {imp for imp in imports if imp.lower() in pip_packages}

def generate_requirements_txt(packages, output_file='requirements.txt'):
    with open(output_file, 'w', encoding='utf-8') as file:
        for package in sorted(packages):
            file.write(f"{package}\n")

def main():
    project_directory = '.'  # Replace with your project directory
    python_files = find_python_files(project_directory)

    all_imports = set()
    for file in python_files:
        imports = extract_imports(file)
        all_imports.update(imports)

    pip_packages = get_installed_pip_packages()
    filtered_imports = filter_pip_imports(all_imports, pip_packages)
    generate_requirements_txt(filtered_imports)

if __name__ == "__main__":
    main()
