import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['appointment_project']

    @staticmethod
    def insert(collections, data):
        Database.DATABASE[collections].insert(data)

    @staticmethod
    def find(collections, query):
        return Database.DATABASE[collections].find(query)

    @staticmethod
    def find_one(collections, query):
        return Database.DATABASE[collections].find_one(query)
