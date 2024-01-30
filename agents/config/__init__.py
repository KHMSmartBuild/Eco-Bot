# __init__.py for agents/config package

from .llm_config import get_config_list, get_config_json_string

# Load environment variables (if needed globally)
from dotenv import load_dotenv
load_dotenv(dotenv_path="agents/config/.env")
