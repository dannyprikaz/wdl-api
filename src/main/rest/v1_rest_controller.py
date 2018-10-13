from flask import Flask, current_app, request
from flask_cors import CORS
from main.user import User, UserService
from main.mongo import MongoConn
from main import MONGO_URL
import json

app = Flask(__name__)
CORS(app)
app.url_map.strict_slashes = False
app.user_service = UserService(MongoConn(MONGO_URL))

@app.route('/users', methods=['POST'])
def create_user():
    parameters = json.loads(request.data)
    new_user = User(**parameters)
    with app.app_context():
        current_app.user_service.create_user(new_user)
    return (json.dumps(dict(new_user)), 201)

@app.route('/users', methods=['GET'])
def get_user():
    id = json.loads(request.data)['id']
    with app.app_context():
        user_result = current_app.user_service.get_user(id)
    return json.dumps(dict(user_result))

@app.route('/users/check', methods=['GET'])
def check_user():
    parameters = json.loads(request.data)
    check_user = User(**parameters)
    with app.app_context():
        exists = current_app.user_service.check_user(check_user)
    return json.dumps({'exists': exists})
