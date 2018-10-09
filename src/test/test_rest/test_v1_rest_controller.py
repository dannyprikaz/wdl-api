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
