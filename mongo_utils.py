from unittest import TestCase
import datetime
from pymongo import MongoClient
from configs import mongo_db_uri, mongo_db_name

__author__ = 'charlie'


def save_to_mongo(documents):
    client = MongoClient(mongo_db_uri)
    db = client[mongo_db_name]
    results = db.speedtest.insert_many(documents)
    message = '%s documents inserted into Mongo with the following ids:' % len(documents)
    for inserted_id in results.inserted_ids:
        message += '%s\n' % inserted_id
    print(message)
    return results.inserted_ids


class TestInsertMongo(TestCase):
    results = []

    def tearDown(self):
        client = MongoClient(mongo_db_uri)
        db = client[mongo_db_name]
        db.speedtest.delete_many({})

    def test_insert(self):
        jsons = []
        for i in range(10):
            now = datetime.datetime.now()
            jsons.append({'foo': now.timestamp() + i})
        self.results = save_to_mongo(jsons)
        self.assertTrue(len(self.results) == len(jsons))
        client = MongoClient(mongo_db_uri)
        db = client[mongo_db_name]
        for result in self.results:
            found = db.speedtest.find({'_id': result})
            self.assertIsNotNone(found)
            for document in found:
                print(document)



