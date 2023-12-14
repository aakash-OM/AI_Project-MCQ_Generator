import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #file name with .log extension

log_path=os.path.join(os.getcwd(),"logs")   #getcwd: current working directory
#in cwd we create a folder logs 's path

os.makedirs(log_path,exist_ok=True) #here we create folder(logs)


LOG_FILEPATH=os.path.join(log_path,LOG_FILE) #inside folder(logs) we create .log files


logging.basicConfig(level=logging.INFO, 
        filename=LOG_FILEPATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)