from rest_api_demo.database import db
from rest_api_demo.database.models import Widget, Category, Order, OrderItem


def create_widget(data):
    name = data.get('name')
    size = data.get('size')
    finish = data.get('finish')
    quantity = data.get('quantity')
    category_id = data.get('category_id')
    category = Category.query.filter(Category.id == category_id).one()
    widget = Widget(name, size, finish, quantity, category)
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


def create_order(data):
    customer_name = data.get('customer_name')
    order_id = data.get('id')

    order = Order(customer_name)
    if order_id:
        order.id = order_id

    db.session.add(order)
    db.session.commit()


def update_order(order_id, data):
    order = Order.query.filter(Order.id == order_id).one()
    order.customer_name = data.get('customer_name')
    db.session.add(order)
    db.session.commit()


def delete_order(order_id):
    order = Order.query.filter(Order.id == order_id).one()
    db.session.delete(order)
    db.session.commit()
    
    
def add_order_item(order_id, widget_id):
    order = Order.query.filter(Order.id == order_id).one()
    widget = Order.query.filter(Widget.id == widget_id).one()
    order.order_items.append(OrderItem(widget))
    db.session.add(order)
    db.session.commit()


def delete_order_item(order_id, widget_id):
    order_item = OrderItem.query.filter(OrderItem.order_id == order_id).filter(OrderItem.item_id == widget_id).one()
    db.session.delete(order_item)
    db.session.commit()