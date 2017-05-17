import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.widget.business import create_order, update_order, delete_order, add_order_item, delete_order_item
from rest_api_demo.api.widget.serializers import widget_description, order, order_item

from rest_api_demo.api.restplus import api
from rest_api_demo.api.widget.parsers import pagination_arguments
from rest_api_demo.database.models import Order, OrderItem

log = logging.getLogger(__name__)

ns = api.namespace('widget/orders', description='Operations related to widget orders')


@ns.route('/')
class OrderCollection(Resource):

    @api.marshal_list_with(order)
    def get(self):
        """
        Returns list of widget orders.
        """
        orders = Order.query.all()
        return orders

    @api.response(201, 'Order successfully created.')
    @api.expect(order)
    def post(self):
        """
        Creates a new widget order.
        """
        data = request.json
        create_order(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Order not found.')
class OrderItem(Resource):

    @api.marshal_with(order)
    def get(self, id):
        """
        Returns a order with a list of posts.
        """
        return Order.query.filter(Order.id == id).one()

    @api.expect(order)
    @api.response(204, 'Order successfully updated.')
    def put(self, id):
        """
        Updates a widget order.

        Use this method to change the name of a widget order.

        * Send a JSON object with the new name in the request body.

        ```
        {
          "name": "New Order Name"
        }
        ```

        * Specify the ID of the order to modify in the request URL path.
        """
        data = request.json
        update_order(id, data)
        return None, 204

    @api.response(204, 'Order successfully deleted.')
    def delete(self, id):
        """
        Deletes widget order.
        """
        delete_order(id)
        return None, 204