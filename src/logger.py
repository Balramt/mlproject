import logging
import os
from datetime  import datetime
#The purpose of logging in a program is to record and store information about the program's runtime behavior, errors, warnings,
#and other messages, which can be useful for debugging and monitoring.

#LOG_FILE: This variable is assigned a string containing the current date and time formatted as 'month_day_year_hour_minute_second.log'.
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#logs_path: This variable is assigned the path to a directory named "logs" within the current working directory, and it includes the log file name.
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

#os.makedirs(logs_path, exist_ok=True): This line creates the "logs" directory if it doesn't exist.
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) #complete path to the log file.

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",

    #level=logging.INFO: Sets the logging level to INFO, which means that messages with severity INFO and above (e.g., WARNING, ERROR, CRITICAL) will be recorded.
    level=logging.INFO,
)
