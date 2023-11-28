# logging_setup.py

import logging
import os
import datetime
from icecream import ic


def setup_icecream_debugging():
    """
    Set up logging for debugging purposes.
    
    This function creates a log folder if it doesn't exist and generates a log file name with a timestamp. It then configures the logging module to save logs to the log file.
    
    Parameters:
    None
    
    Returns:
    None
    """
    # Set up logging
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)
    
    # Generate log file name with timestamp
    log_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(log_folder, f"log_{log_timestamp}.txt")
    
    # Configure logging module to save logs to the log file
    log_format = '%(asctime)s - %(levelname)s - Eco-Bot Chat - %(message)s'
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format=log_format)
    logging.info("Logging started")
    
    # Set up icecream
    ic.configureOutput(prefix="DTA Debug | ")
