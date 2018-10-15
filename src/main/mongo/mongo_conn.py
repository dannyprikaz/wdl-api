from main import USER_COLLECTION
from pymongo import MongoClient

class MongoConn(object):
    def __init__(self, url=None):
        self.client = MongoClient(url)
        self.db = self.client.get_database()

    def index_user(self, user):
        self.db[USER_COLLECTION].insert_one(dict(user))

    def get_user(self, user):
        return self.db[USER_COLLECTION].find_one(dict(user))
