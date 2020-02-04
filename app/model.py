from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(120))
    state = db.Column(db.String(120))
    country = db.Column(db.String(60))
    created = db.Column(db.DateTime)
    probability = db.Column(db.String(60))
    precipitation = db.Column(db.String(60))
    minimum = db.Column(db.String(60))
    maximum = db.Column(db.String(60))


    def __repr__(self):
        return '<City %r>' % self.city_name