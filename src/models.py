from .controller import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100))
    login = db.Column(db.String(1000))
    contacts = db.Column(db.String(100))
