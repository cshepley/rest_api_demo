import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.widget.business import create_widget, update_widget, delete_widget
from rest_api_demo.api.widget.serializers import widget_description, category_with_widgets, page_of_widget_descriptions

from rest_api_demo.api.restplus import api
from rest_api_demo.api.widget.parsers import pagination_arguments
from rest_api_demo.database.models import Widget

log = logging.getLogger(__name__)

ns = api.namespace('widget/widgets', description='Operations related to widget widgets')


@ns.route('/')
class WidgetsCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_widget_descriptions)
    def get(self):
        """
        Returns list of widget widgets.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        widgets_query = Widget.query
        widgets_page = widgets_query.paginate(page, per_page, error_out=False)

        return widgets_page

    @api.response(201, 'Widget successfully created.')
    @api.expect(widget_description)
    def post(self):
        """
        Creates a new widget widget.
        """

        data = request.json
        create_widget(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Widget not found.')
class WidgetItem(Resource):

    @api.marshal_with(widget_description)
    def get(self, id):
        """
        Returns a widget widget.
        """
        return Widget.query.filter(Widget.id == id).one()

    @api.expect(widget_description)
    @api.response(204, 'Widget successfully updated.')
    def put(self, id):
        """
        Updates a widget widget.
        """
        data = request.json
        update_widget(id, data)
        return None, 204

    @api.response(204, 'Widget successfully deleted.')
    def delete(self, id):
        """
        Deletes widget widget.
        """
        delete_widget(id)
        return None, 204


@ns.route('/archive/<int:year>/')
@ns.route('/archive/<int:year>/<int:month>/')
@ns.route('/archive/<int:year>/<int:month>/<int:day>/')
class WidgetsArchiveCollection(Resource):

    @api.expect(pagination_arguments, validate=True)
    @api.marshal_with(page_of_widget_descriptions)
    def get(self, year, month=None, day=None):
        """
        Returns list of widget widgets from a specified time period.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        start_month = month if month else 1
        end_month = month if month else 12
        start_day = day if day else 1
        end_day = day + 1 if day else 31
        start_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, start_month, start_day)
        end_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, end_month, end_day)
        widgets_query = Widget.query.filter(Widget.create_date >= start_date).filter(Widget.create_date <= end_date)

        widgets_page = widgets_query.paginate(page, per_page, error_out=False)

        return widgets_page
