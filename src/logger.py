import logging
import os
from datetime import datetime

# For logging execution details for tracking. 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True) # exist_ok means keep appending files inside 
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

# Overwrite logging method by specifying your custome logging requirement
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",       # Specify the format in which you are logging the data.
    level = logging.INFO,
)

