from config import db
from sqlalchemy.sql import func # type: ignore

class Menu(db.Model):
    menu_id = db.Column(db.Integer, primary_key = True)
    img = db.Column(db.String(500), nullable = False)
    menu_name = db.Column(db.String(100), nullable = False)
    price = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(100), nullable = False)
    created_at = db.Column(db.DateTime(timezone = True), default = func.now())