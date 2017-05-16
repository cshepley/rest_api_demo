# Create the widget DB using SQLAlchemy's ORM code first abilities
# Mapping to SQLite in example, MySQL would be prod most likely.

from datetime import datetime

from rest_api_demo.database import db


class Widget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    size = db.Column(db.Integer)
    finish = db.Column(db.String(80))
    quantity = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('widgets', lazy='dynamic'))

    def __init__(self, name, size, finish, quantity, category, create_date=None):
        self.name = name
        self.size = size
        self.finish = finish
        self.quantity = quantity
        if create_date is None:
            create_date = datetime.utcnow()
        self.create_date = create_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name
