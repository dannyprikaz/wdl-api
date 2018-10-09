from main.user import UserService
from mock import Mock

def test_create_user():
    #setup
    db_conn = Mock()
    db_conn.index_user = Mock()
    mocked_user = Mock()
    user_service = UserService(db_conn)
    #functionality
    user_service.create_user(mocked_user)
    #test
    db_conn.index_user.assert_called_with(mocked_user)
