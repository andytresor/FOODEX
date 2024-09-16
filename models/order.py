from flask import session
from config import db

class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, default=lambda: session.get('id'))
    quantity = db.Column(db.Integer, nullable=False, default=1)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.menu_id'), nullable=False)
    menu = db.relationship('Menu', backref='menu', lazy=True)
    