import os
import sys

from networksecurity.constants.training_pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkModel:
    def __init__(self,preprocessor,model):
        """
        Initialising the NetworkModel class with preprocessor and model

        Args:
          preprocessor: The preprocessor object
          model: The model object
        """
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def predict(self,x):
        """
        It takes in a numpy array and returns the predictions of the model

        Args:
          x: The input data

        Returns:
          The predictions of the model
        """
        try:
            x_transform = self.preprocessor.transform(x)
            y_hat = self.model.predict(x_transform)
            return y_hat
        except Exception as e:
            raise NetworkSecurityException(e,sys)    