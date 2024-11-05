import os
from pymongo.mongo_client import MongoClient


def connect_mongo_abes():
    client = MongoClient(os.getenv('MONGO_URI_CLOUD'))
    database = client['abes_scrapping']
    return database['data']


collection = connect_mongo_abes()


def insert_data_abes(dict_data):
    collection.insert_one(dict_data)


def insert_many_data_abes(many_data):
    collection.insert_many(many_data)


def get_dict_abes_scrapping():
    return list(collection.find({}, {'_id': 0}))


def get_dict_br_versus_la():
    return list(
        collection.find(
            {},
            {
                '_id': 0,
                'brazil_movement': 1,
                'latin_america_investment': 1,
                'study_year': 1,
            },
        )
    )
