import os
import logging
from datetime import datetime

# Create log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Set log path without including the log file name in the directory
log_path = os.path.join(os.getcwd(), "logs",LOG_FILE)
os.makedirs(log_path, exist_ok=True)

# Set full log file path
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")
