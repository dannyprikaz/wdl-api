from main.mongo import MongoConn
from main.mongo import mongo_conn as module
from main.user import User
from mock import Mock, MagicMock

def test_index_user():
    #setup
    test_name = 'test'
    module.DB_NAME = module.USER_COLLECTION = test_name
    mocked_client = Mock()
    mocked_db = Mock()
    mocked_collection = Mock()
    mocked_client.__getitem__ = Mock(return_value=mocked_db)
    mocked_db.__getitem__ = Mock(return_value=mocked_collection)
    mocked_collection.insert_one = Mock()
    module.MongoClient = Mock(return_value=mocked_client)
    user = User('test@test.com', 'test_display_name')
    mongo_conn = MongoConn()
    #functionality
    mongo_conn.index_user(dict(user))
    #test
    mocked_collection.insert_one.assert_called_with(user)
