from flask_restplus import fields
from rest_api_demo.api.restplus import api

widget_description = api.model('Widget', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a widget'),
    'name': fields.String(required=True, description='Widget name'),
    'quantity': fields.String(required=True, description='Widget quantity'),
    'create_date': fields.DateTime,
    'category_id': fields.Integer(attribute='category.id'),
    'category': fields.String(attribute='category.id'),
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
    'posts': fields.List(fields.Nested(widget_description))
})
