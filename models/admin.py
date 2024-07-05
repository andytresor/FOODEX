from config import db
from sqlalchemy.sql import func # type: ignore

class Admin(db.Model):
    admin_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    created_at = db.Column(db.DateTime(timezone = True), default = func.now())