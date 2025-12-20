import logging  # importing logging module to set up logging functionality
import os  # importing os module to handle file paths
from datetime import datetime  # importing datetime module to work with date and time

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(),'logs',LOG_FILE)
os.makedirs(logs_path,exist_ok=True) # creating logs directory if it doesn't exist

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


