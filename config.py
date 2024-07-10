import os
from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pamelajo25@127.0.0.1:3306/FOODEX'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(32)