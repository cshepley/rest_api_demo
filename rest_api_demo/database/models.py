# Create the widget DB using SQLAlchemy's ORM code first abilities
# Mapping to SQLite in example, MySQL would be prod most likely.

from datetime import datetime

from rest_api_demo.database import db


class Widget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    finish = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.now())

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('widget', lazy='dynamic'))

    def __init__(self, name, size, finish, quantity, category):
        self.name = name
        self.size = size
        self.finish = finish
        self.quantity = quantity
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


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(30), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    order_items = db.relationship("OrderItem", cascade="all, delete-orphan",
                                  backref='order')

    def __init__(self, customer_name):
        self.customer_name = customer_name


class OrderItem(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('widget.id'), primary_key=True)


    def __init__(self, item):
        self.item = item

    item = db.relationship(Widget, lazy='joined')
