from main.rest.v1_rest_controller import app
from main.rest import v1_rest_controller as module
from main.user import User
from flask import current_app
import json
from mock import Mock

client = app.test_client()

def test_create_user():
    #setup
    parameters = {'email': 'test@test.com', 'display_name': 'test_name'}
    expected = User(**parameters)
    with app.app_context():
        current_app.user_service = Mock()
        current_app.user_service.create_user = Mock()
    #functionality
    r = client.post('/users/', data=json.dumps(parameters))
    #test
    with app.app_context():
        current_app.user_service.create_user\
            .assert_called_with(expected)
    assert r.get_data() == json.dumps(dict(expected))
    assert r.status_code == 201

def test_check_user_by_email():
    #setup
    incomplete_parameters = {'email': 'test@test.com'}
    expected_check = User(**incomplete_parameters)
    exists = True
    with app.app_context():
        current_app.user_service = Mock()
        current_app.user_service.check_user = Mock(return_value=exists)
    #functionality
    r = client.get('/users/check', query_string=incomplete_parameters)
    #test
    with app.app_context():
        current_app.user_service.check_user\
            .assert_called_with(expected_check)
    assert r.get_data() == json.dumps({'exists': exists})
    assert r.status_code == 200

def test_check_user_by_display_name():
    #setup
    incomplete_parameters = {'display_name': 'test_name'}
    expected_check = User(**incomplete_parameters)
    exists = True
    with app.app_context():
        current_app.user_service = Mock()
        current_app.user_service.check_user = Mock(return_value=exists)
    #functionality
    r = client.get('/users/check', query_string=incomplete_parameters)
    #test
    with app.app_context():
        current_app.user_service.check_user\
            .assert_called_with(expected_check)
    assert r.get_data() == json.dumps({'exists': exists})
    assert r.status_code == 200

def test_get_user_success():
    #setup
    id = 'test_id'
    parameters = {'email': 'test@test.com', 'display_name': 'tet_name'}
    expected = User(**parameters)
    expected_check = User(_id=id)
    with app.app_context():
        current_app.user_service = Mock()
        current_app.user_service.get_user = Mock(return_value=parameters)
    #functionality
    r = client.get('/users', query_string={'id': id})
    #test
    with app.app_context():
        current_app.user_service.get_user\
            .assert_called_with(expected_check)
    assert r.get_data() == json.dumps(dict(expected))
    assert r.status_code == 200

def test_get_user_failure():
    #setup
    id = 'test_id'
    parameters = None
    expected = User()
    expected_check = User(_id=id)
    with app.app_context():
        current_app.user_service = Mock()
        current_app.user_service.get_user = Mock(return_value=parameters)
    #functionality
    r = client.get('/users', query_string={'id': id})
    #test
    with app.app_context():
        current_app.user_service.get_user\
            .assert_called_with(expected_check)
    assert r.get_data() == json.dumps(dict(expected))
    assert r.status_code == 200
