import os
import sys

import numpy as np
import pandas as pd
import dill

from src.exception import CustomException 

def save_object(file_path, obj):
    try:
        # Get the directory path from the given file path
        dir_path = os.path.dirname(file_path)

        # Create the directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)

        # Open the file in binary write mode and use dill to serialize and save the object
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        # If any exception occurs, raise a CustomException with details
        raise CustomException(e, sys)