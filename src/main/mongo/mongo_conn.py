from main import DB_NAME, USER_COLLECTION
from pymongo import MongoClient

class MongoConn(object):
    def __init__(self, url=''):
        self.client = MongoClient(url)
        self.db = self.client[DB_NAME]

    def index_user(self, user):
        self.db[USER_COLLECTION].insert_one(dict(user))
