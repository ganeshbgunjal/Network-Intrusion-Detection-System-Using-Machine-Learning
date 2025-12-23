import os
import sys
import json

from dotenv import load_dotenv  # to load environment variables from a .env file to system environment variables.
load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')  # Fetching the MongoDB URL from environment variables.

print(f"MONGO_DB_URL: {MONGO_DB_URL}")  # Debugging line to print the MongoDB URL.

import certifi  # to provide SSL certificates for secure connection.
ca = certifi.where()  # Get the path to the CA bundle.  CA = Certificate Authority.

import pymongo
import pandas as pd
import numpy as np

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def csv_to_json_converter(self,file_path):
        """
        This function will convert CSV file to JSON file.
        file_path: str: path of the csv file.
        return: json_data: list of json objects.
        """
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def insert_data_mongodb(self,records,database,collection):
        """
        This function will insert data into MongoDB collection.
        records: list of json objects: data to be inserted.
        database: str: name of the database.
        collection: str: name of the collection.
        return: len(records): int: number of records inserted.
        """
        try:
            self.database = database
            self.collection = collection
            self.records = records
            
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)

            return(len(self.records))        
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__ == '__main__':
    FILE_PATH = 'Network_Data\phisingData.csv'
    DATABASE = 'NetworkSecurityDB'
    COLLECTION = 'PhishingDataCollection'

    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_converter(file_path=FILE_PATH)

    no_of_records = networkobj.insert_data_mongodb(records,DATABASE,COLLECTION)

    print(f'No of records inserted: {no_of_records}')








