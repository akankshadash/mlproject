import sys
import logging
import os
from datetime import datetime
from source.exceptions import CustomException

Log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", Log_file)
os.makedirs(os.path.dirname(log_path), exist_ok=True)

Log_file_path = os.path.join(os.getcwd(), "logs", Log_file)

logging.basicConfig(
    filename=Log_file_path,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)


    