from flask import Flask
from flask_socketio import SocketIO
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key@deliveryapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/sms_deliveryapp_sms'
io = SocketIO(app,async_handlers=True)
jwt = JWTManager(app)
ma = Marshmallow(app)
db = SQLAlchemy(app)