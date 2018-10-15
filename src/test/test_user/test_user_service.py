from main.user import UserService, User
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

def test_check_user_success():
    #setup
    mocked_check_user = Mock()
    returned_user_data = {'email': 'test_email', 'display_name': 'test_name'}
    db_conn = Mock()
    db_conn.get_user = Mock(return_value=returned_user_data)
    user_service = UserService(db_conn)
    #functionality
    actual = user_service.check_user(mocked_check_user)
    #test
    db_conn.get_user.assert_called_with(mocked_check_user)
    assert actual, 'returned False'

def test_check_user_failure():
    #setup
    mocked_check_user = Mock()
    returned_user_data = None
    db_conn = Mock()
    db_conn.get_user = Mock(return_value=returned_user_data)
    user_service = UserService(db_conn)
    #functionality
    actual = user_service.check_user(mocked_check_user)
    #test
    db_conn.get_user.assert_called_with(mocked_check_user)
    assert not actual, 'returned True'

def test_get_user():
    #setup
    mocked_user = Mock()
    expected = {'email': 'test_email', 'display_name': 'test_name'}
    db_conn = Mock()
    db_conn.get_user = Mock(return_value=expected)
    user_service = UserService(db_conn)
    #functionality
    actual = user_service.get_user(mocked_user)
    #test
    db_conn.get_user.assert_called_with(mocked_user)
    assert actual == expected, 'actual: {} != expected: {}'.format(actual, expected)
