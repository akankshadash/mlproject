import os
import sys
import pandas as pd
import numpy as np
import dill
from source.exceptions import CustomException
from source.loggers import logging

def save_object(file_path, obj):
    """
    Saves a Python object to a file using pickle serialization.
    Args:
        file_path (str): The path where the object will be saved.
        obj (object): The Python object to be saved.
    Raises:
        CustomException: If there is an error during the saving process.
    Returns:
        None
    """
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file:
            pd.to_pickle(obj, file)
    except Exception as e:
        raise CustomException(f"Error saving object to {file_path}: {e}", sys)