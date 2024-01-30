import sys
sys.path.append('..')
from agents.config import get_config_list, get_config_json_string

# Assuming your .env file is located in the 'agents/config' directory
env_file_path = '../agents/config/.env'

# Get configuration as a list
config_list = get_config_list(env_file_path)

# Get configuration as a JSON string
config_json = get_config_json_string(env_file_path)
