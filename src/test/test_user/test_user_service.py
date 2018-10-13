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

def test_get_user():
    #setup
    mocked_check_user = Mock()
    expected = Mock()
    db_conn = Mock()
    db_conn.get_user = Mock(return_value=expected)
    user_service = UserService(db_conn)
    #functionality
    actual = user_service.get_user(mocked_check_user)
    #test
    db_conn.get_user.assert_called_with(mocked_check_user)
    assert actual == expected, 'actual: {} != expected: {}'.format(actual, expected)
