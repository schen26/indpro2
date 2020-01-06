from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.models import
from application import routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@35.242.133.237/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'm8c4m5c899284m'
db = SQLAlchemy(app)
