from config import db
from sqlalchemy.sql import func # type: ignore

class Staff(db.Model):
    staff_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    img = db.Column(db.String(250), unique=True, nullable = False)
    img_name = db.Column(db.Text, nullable = False)
    mimetype = db.Column(db.Text, nullable = False)
    email = db.Column(db.String(50), nullable = False)
    salary = db.Column(db.String(50), nullable = False)
    role = db.Column(db.String(50), nullable = False)
    created_at = db.Column(db.DateTime(timezone = True), default = func.now())