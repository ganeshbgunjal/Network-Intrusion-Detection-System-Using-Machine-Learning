# This utils.py file is for defining utility functions used across the project.
import os
import sys
import yaml
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score

from sklearn.metrics import r2_score

import pandas as pd
import numpy as np
# import dill
import pickle



def read_yaml_file(file_path:str)-> dict:
    try:
        with open(file_path,'r') as yaml_file:
            return yaml.safe_load(yaml_file)  # safe_load(): safely parses a YAML file into Python objects
    except Exception as e:
        raise NetworkSecurityException(e,sys)

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.safe_dump(content, file)

        logging.info(f"YAML file written successfully at: {file_path}")
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
def save_numpy_array_data(file_path: str, array: np.ndarray) -> None:
    '''
    Save numpy array data to file.
    file_path: str location of file to save
    array: np.ndarray data to save
    '''
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise NetworkSecurityException(e, sys)

def save_object(file_path: str, obj: object) -> None:
    '''
    Save a Python object to a file using pickle.
    file_path: str location of file to save
    obj: object to save
    '''
    try:
        logging.info(f"Enteres the save object method of main utils class")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
        logging.info(f"Exited the save object method of main utils class")
    except Exception as e:
        raise NetworkSecurityException(e, sys)

def load_object(file_path: str) -> object:
    '''
    Load a Python object from a file using pickle.
    file_path: str location of file to load
    returns: object loaded from file
    '''
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} does not exist")
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)

def load_numpy_array_data(file_path: str) -> np.ndarray:
    '''
    Load numpy array data from file.
    file_path: str location of file to load
    returns: np.ndarray data loaded from file
    '''
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """
    Performs GridSearchCV for classification models and
    returns the best trained estimator for each model.
    """
    try:
        report = {}

        for model_name, model in models.items():
            logging.info(f"Training model: {model_name}")

            params = param.get(model_name, {})

            gs = GridSearchCV(
                estimator=model,
                param_grid=params,
                cv=3,
                n_jobs=-1,
                scoring="f1_weighted"
            )

            gs.fit(X_train, y_train)

            best_model = gs.best_estimator_  # already fitted

            report[model_name] = best_model  #  RETURN MODEL

        return report

    except Exception as e:
        raise NetworkSecurityException(e, sys)




