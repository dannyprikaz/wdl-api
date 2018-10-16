import os

USER_COLLECTION = 'users'
MONGO_URL = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/test')
