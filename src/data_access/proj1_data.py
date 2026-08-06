"""this is a data access module. It uses the mongoDB_Cconnection module. Estb 
    connection to the remote MongoDB database. Extracts the required data in {k:v} pair
    then convert them into dataframe.
"""

import sys
import pandas as pd
import numpy as np
from typing import Optional 

from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import MyException

class Proj1Data:
    """a class to export MongoDB records as a pandas df
    """
    def __init__(self)->None:
        """initializes the MongoDB client connection
        """
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise MyException(e,sys)

    def export_collection_as_dataframe(self,collection_name:str,database_name:Optional[str]=None)->pd.DataFrame:
        """Exports an entire MongoDB collection as a pandas Dataframe

        Args:
            collection_name (str): the name of the MongoDB collection to export
            database_name (Optional[str], optional): the name of the database (optional). Defaults to DATABASE_NAME


        Returns:
            pd.DataFrame: Dataframe containing the collection data, with '_id' column removed
            and 'na' values replces with NaN
        """
        try:
            #Access specified colelction from the default or dspecified database
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            #convert colllection data to DataFrame and preprocess 
            print("fetching data from mongoDB")
            df = pd.DataFrame(list(collection.find()))#extracting the collection and converting it into d
            print(f"Data fetched with len: {len(df)}")
            if "id" in df.columns.to_list():
                df = df.drop(columns = ['id'])
            df.replace({"na":np.nan},inplace = True)
            return df
        except Exception as e:
            raise MyException(e,sys)
