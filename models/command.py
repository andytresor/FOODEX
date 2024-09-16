from flask import session
from config import db
from sqlalchemy.sql import func # type: ignore
from sqlalchemy.dialects.postgresql import JSON


class Commands(db.Model):
    command_id = db.Column(db.Integer, primary_key = True)
    total_qty = db.Column(db.Integer, nullable = False)
    total_price = db.Column(db.Integer, nullable = False)
    items = db.Column(JSON, nullable=False) 
    
    created_at = db.Column(db.DateTime(timezone = True), default = func.now())
    
    