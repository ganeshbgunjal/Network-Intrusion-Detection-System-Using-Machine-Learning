# This utils.py file is for defining utility functions used across the project.
import os
import sys
import yaml
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

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




