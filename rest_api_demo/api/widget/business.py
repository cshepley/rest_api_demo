from rest_api_demo.database import db
from rest_api_demo.database.models import Widget, Category


def create_widget(data):
    name = data.get('name')
    quantity = data.get('quantity')
    category_id = data.get('category_id')
    category = Category.query.filter(Category.id == category_id).one()
    widget = Widget(name, quantity, category)
    db.session.add(widget)
    db.session.commit()


def update_widget(widget_id, data):
    widget = Widget.query.filter(Widget.id == widget_id).one()
    widget.name = data.get('name')
    widget.quantity = data.get('quantity')
    category_id = data.get('category_id')
    widget.category = Category.query.filter(Category.id == category_id).one()
    db.session.add(widget)
    db.session.commit()


def delete_widget(widget_id):
    widget = Widget.query.filter(Widget.id == widget_id).one()
    db.session.delete(widget)
    db.session.commit()


def create_category(data):
    name = data.get('name')
    category_id = data.get('id')

    category = Category(name)
    if category_id:
        category.id = category_id

    db.session.add(category)
    db.session.commit()


def update_category(category_id, data):
    category = Category.query.filter(Category.id == category_id).one()
    category.name = data.get('name')
    db.session.add(category)
    db.session.commit()


def delete_category(category_id):
    category = Category.query.filter(Category.id == category_id).one()
    db.session.delete(category)
    db.session.commit()
