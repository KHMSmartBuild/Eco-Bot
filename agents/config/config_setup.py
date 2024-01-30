# This file contains the ConfigSetup
"""
class which provides methods to load, create, and print configuration data.
"""
import os
import json
import re
from dotenv import load_dotenv
load_dotenv(os.path.join("agents", "config", ".env"))
class ConfigSetup:
    """
    A class that provides methods to load, create, and print configuration data.

    Methods:
    load_config_from_js(file_path): Load configuration data from a JavaScript file.
    create_config_json(config_data): Create a JSON script from the given config_data dictionary.
    print_config_json(config_data): Print the given config_data as a formatted JSON string.
    llm_config_setup(): Set up the LLM configuration by loading and printing the configuration data.
    """
    @staticmethod
    def load_config_from_js(file_path):
        """
        Load configuration data from a JavaScript file.

        Args:
            file_path (str): The path to the JavaScript file.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If no JSON data is found in the file.

        Returns:
            dict: The loaded configuration data.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist")

        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

            json_part = re.search(r'{\s*".*}\s*;', file_content, re.DOTALL)
            if json_part:
                json_string = json_part.group().rstrip(';')
                json_data = json.loads(json_string)

                for key, value in json_data.items():
                    if isinstance(value, str) and value.startswith('process.env.'):
                        env_var = value.split('process.env.')[1]
                        json_data[key] = os.getenv(env_var)

                config_data = json_data
            else:
                raise ValueError("No JSON data found in the file")

        return config_data

    @staticmethod
    def create_config_json(config_data):
        """
        Creates a JSON script from the given config_data dictionary.

        Parameters:
            config_data (dict): The dictionary containing the config data.

        Returns:
            str: The JSON script created from the config_data dictionary.
        """
        if not isinstance(config_data, dict):
            raise ValueError("config_data must be a dictionary")

        json_script = f"const config = {json.dumps(config_data)};"

        return json_script

    @staticmethod
    def print_config_json(config_data):
        """
        Print the given `config_data` as a formatted JSON string.

        Args:
            config_data (dict): The configuration data to be printed.

        Returns:
            None
        """
        print(json.dumps(config_data, indent=4))

    @staticmethod
    def llm_config_setup():
        """
        Set up the LLM configuration.

        This function loads the configuration data from the 
        `OAI_CONFIG_LIST.js` file located in the `agents/config` directory. 
        It then prints the configuration data as a JSON object.

        Parameters:
        None

        Returns:
        None
        """
        config_data = {
            ConfigSetup.load_config_from_js
            (os.path.join("agents", "config", "OAI_CONFIG_LIST.js"))
        }
        ConfigSetup.print_config_json(config_data)
if __name__ == "__main__":
    ConfigSetup.llm_config_setup()
