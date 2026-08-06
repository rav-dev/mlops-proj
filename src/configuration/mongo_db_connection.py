"""this module will set up the MongoDB client that will establish the connection 
    with the remote MongoDB remote cluster
"""

import os
import sys
import pymongo
import certifi

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME, MONGODB_URL_KEY

# Load the certificate authority file to avoid timeout errors when connecting to MongoDB
#when python knocks at the MongoDB door using TLS/SSL HTTPS connection, mongoDB asks for the
#certificate, we provide the certi path via pymongo module to MongoDB
#MOngoDB using the certi path creates the authentication
ca = certifi.where()

class MongoDBClient:
    """MongoDb client is responsible for establishing a connection to the MongoDB database """
    client = None #shared MongoClient instance across all MongoDBClient instances

    def __init__(self,database_name:str=DATABASE_NAME)->None:
        """Initializes a connection to the MongoDB dataabse. If no existing conection is found,
        it establishes a new one.

        Args:
            database_name (str, optional): Name of the MongoDB database to connect to. Default 
            is set by DATABASE_NAME constant.
        
        RAISES:
            MyException:
                if there is an issue connecting to MongoDB or if the env var for the MongoDB URL 
                is not set

        """
        try:
            #check if a MongoDB client connection has already been established; if not, create a new one
            if MongoDBClient.client is None:
                mongo_db_url=os.getenv(MONGODB_URL_KEY) #retrieve MongoDB URL from env vars
                if mongo_db_url is None:
                    raise Exception(f"Env var '{MONGODB_URL_KEY}' is not set")

                #estb a new MOngoDB client connection
                MongoDBClient.client=pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            # use the shared MongoClient for this instance 
            self.client=MongoDBClient.client
            self.database=self.client[database_name] #conect to the specified database
            self.database_name=database_name
            logging.info("MongoDB connection successful")
        except Exception as e:
            #we will raise the custom exception 
            raise MyException(e,sys)

