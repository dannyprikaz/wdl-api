from flask import Flask, current_app, request
from flask_mail import Mail, Message
from flask_cors import CORS
from main.user import User, UserService
from main.mongo import MongoConn
from main import MONGO_URL
import json
import os

app = Flask(__name__)
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}

CORS(app)
app.config.update(mail_settings)
mail = Mail(app)
app.url_map.strict_slashes = False
app.user_service = UserService(MongoConn(MONGO_URL))

@app.route('/users', methods=['POST'])
def create_user():
    parameters = json.loads(request.data)
    new_user = User(**parameters)
    mail_params = {
        'subject': 'Welcome the WDL Fantasy League!',
        'sender': app.config.get("MAIL_USERNAME"),
        'recipients': [new_user.email],
        'html': '<h1>Welcome to the WDL Fantasy League, {}!</h1>'
                    .format(new_user.display_name)\
                + '<p>Your id is {}</p>'.format(new_user._id)\
                + '<p>and your link is http://whodunnitleague.com/fantasy/team.html?id={}'
                    .format(new_user._id)
    }
    with app.app_context():
        current_app.user_service.create_user(new_user)
        msg = Message(**mail_params)
        mail.send(msg)
    return (json.dumps(dict(new_user)), 201)

@app.route('/users', methods=['GET'])
def get_user():
    id = request.args['id']
    with app.app_context():
        parameters = current_app.user_service.get_user(User(_id=id))
        user_result = User(**parameters) if parameters else User()
    return json.dumps(dict(user_result))

@app.route('/users/check', methods=['GET'])
def check_user():
    parameters = dict([(key, value[0])\
                       for key, value\
                       in dict(request.args).iteritems()])
    check_user = User(**parameters)
    with app.app_context():
        exists = current_app.user_service.check_user(check_user)
    return json.dumps({'exists': exists})
