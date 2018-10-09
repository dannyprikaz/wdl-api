from flask import Flask, current_app, request
from main.user import User, UserService
from main.mongo import MongoConn
from main import MONGO_URL
import json

app = Flask(__name__)
app.url_map.strict_slashes = False
app.user_service = UserService(MongoConn(MONGO_URL))

@app.route('/users', methods=['POST'])
def create_user():
    parameters = json.loads(request.data)
    new_user = User(**parameters)
    with app.app_context():
        current_app.user_service.create_user(new_user)
    return (json.dumps(dict(new_user)), 201)
