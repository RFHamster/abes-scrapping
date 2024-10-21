import os
from pymongo.mongo_client import MongoClient

def connect_mongo_abes():
    client = MongoClient(os.getenv('MONGO_URI_CLOUD'))
    database = client["abes_scrapping"]
    return database["data"]

collection = connect_mongo_abes()

def insert_data_abes(dict_data):
    collection.insert_one(dict_data)


def insert_many_data_abes(many_data):
    collection.insert_many(many_data)