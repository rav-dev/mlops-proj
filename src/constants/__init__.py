"""in this module we are defining all the constants that we will be requiring in our project
"""

import os
from datetime import date
from datetime import datetime

"""Loging operation constants"""
LOG_DIR = 'logs' #this is the dir where the log files will sit
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5*1024*1025 #our log files can be at max 5MB size
BACKUP_COUNT = 3 #at the max we can have 3 logfiles per execution


"""For MongoDB connections"""
#thus we have already created in MongoDB_demo.ipynb
DATABASE_NAME = "Proj1" 
COLLECTION_NAME = "Proj1-Data"
MONGODB_URL_KEY = "MONGODB_URL" #this is the placeholder for the mongoKey

PIPELINE_NAME: str = ""
ARTIFACT_DIR: str = "artifact" #this is the name of the directory where we will store the data

FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config","schema.yaml")

"""Data Ingestion related constants start wirth DATA_INGESTION var name"""
DATA_INGESTION_COLLECTION_NAME: str = "Proj1-Data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25
