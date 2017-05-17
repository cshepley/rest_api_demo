from flask_restplus import fields
from rest_api_demo.api.restplus import api

widget_description = api.model('Widget description', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a widget'),
    'name': fields.String(required=True, description='Widget name'),
    'size': fields.Integer(required=True, description='Widget size'),
    'finish': fields.String(required=True, description='Widget finish'),
    'quantity': fields.Integer(required=True, description='Widget quantity'),
    'create_date': fields.DateTime(readOnly=True),
    'category_id': fields.Integer(attribute='category.id'),
    'category': fields.String(attribute='category.name'),
})

order_item = api.model('Order item', {
    'order_id': fields.Integer(required=True, description='The unique identifier of an order'),
    'item_id': fields.Integer(required=True, description='The unique identifier of a widget'),
})

order = api.model('Order', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an order'),
    'customer_name': fields.String(required=True, description='Customer name'),
    'order_date': fields.DateTime(readOnly=True),
    'order_items': fields.List(fields.Nested(order_item))
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_widget_descriptions = api.inherit('Page of widget descriptions', pagination, {
    'items': fields.List(fields.Nested(widget_description))
})

category = api.model('Widget category', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a widget category'),
    'name': fields.String(required=True, description='Category name'),
})

category_with_widgets = api.inherit('Category with widgets', category, {
    'widgets': fields.List(fields.Nested(widget_description))
})
