import os
import sys

import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score

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
    
def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]

            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report
    
    except Exception as e:
        raise CustomException(e, sys)