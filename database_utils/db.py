import os
from pymongo.mongo_client import MongoClient


def connect_mongo_abes():
    client = MongoClient(os.getenv('MONGO_URI_CLOUD'))
    database = client['abes_scrapping']
    return database['data']


collection_abes = connect_mongo_abes()


def insert_data_abes(dict_data):
    collection_abes.insert_one(dict_data)


def insert_many_data_abes(many_data):
    collection_abes.insert_many(many_data)


def get_dict_abes_scrapping():
    return list(collection_abes.find({}, {'_id': 0}))


def get_dict_br_positions():
    return list(
        collection_abes.find(
            {}, {'_id': 0, 'brazil_position': 1, 'study_year': 1}
        )
    )


def get_dict_br_versus_la():
    return list(
        collection_abes.find(
            {
                'brazil_movement': {'$ne': 'Not Informed'},
                'latin_america_investment': {'$ne': 'Not Informed'},
            },
            {
                '_id': 0,
                'brazil_movement': 1,
                'latin_america_investment': 1,
                'study_year': 1,
            },
        )
    )


def get_dict_br_versus_world():
    return list(
        collection_abes.find(
            {
                'brazil_movement': {'$ne': 'Not Informed'},
                'global_investment': {'$ne': 'Not Informed'},
            },
            {
                '_id': 0,
                'brazil_movement': 1,
                'global_investment': 1,
                'study_year': 1,
            },
        )
    )
