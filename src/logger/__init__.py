"""this is our logger module that will do all the loggings
"""

import logging 
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

#these are the constants for log configuration
LOG_DIR = 'logs' #this is the dir where the log files will sit
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5*1024*1025 #our log files can be at max 5MB size
BACKUP_COUNT = 3 #at the max we can have 3 logfiles per execution

#construct log file path 
#from_root module will provide the path from the project's root dir
log_dir_path = os.path.join(from_root(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok = True)
log_file_path = os.path.join(log_dir_path, LOG_FILE)

def configure_logger():
    """it configures logging with the rotating file handler and a console handler.
    the rotating file handler auto manages the log files by limiting their size and preventing 
    them to overgrow indefinately. 
    We have set a limit of 5 MB so the rotating logger let the logger module to write the 
    logs until the fiule reaches the size of 5 MB. As soon as the file reaches 5 MB then it will 
    stop logging in that .log file, rather creates the new file and starts logging in it. We have also 
    set the backup as 3 files so at the most for one execution we can have at most 3 files.
    """
    #create a custom logger 
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    #define formatter 
    formatter = logging.Formatter("[%(asctime)s] %(name)s - %(levelname)s - %(message)s")

    #file handler with rotation
    file_handler = RotatingFileHandler(log_file_path,  maxBytes = MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    #console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)

    #adding the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

#configure the logger
configure_logger()