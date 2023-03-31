import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_COLLECTION = os.getenv('DB_COLLECTION')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT'))


client = MongoClient(f'mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/')
db = client[DB_NAME]
col = db[DB_COLLECTION]


def get_countries():
    countries = list(col.find({},{'_id':0}))
    return countries