from config import db
from sqlalchemy.sql import func # type: ignore

class Auth(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(500), nullable = False)
    created_at = db.Column(db.DateTime(timezone = True), default = func.now())