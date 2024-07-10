from flask import Blueprint # type:ignore

from controllers.order_controller import cook, orders, view_order, newOrder, delete_order

order = Blueprint('order' , __name__)

order.route('/' , methods=['GET'] , strict_slashes=False)(cook)
order.route('/orders' , methods=['GET'] , strict_slashes=False)(orders)
order.route('/view_order' , methods=['GET'] , strict_slashes=False)(view_order)
order.route('/create_order' , methods=['POST'] , strict_slashes=False)(newOrder)
order.route('/delete/<order_id>' , methods=['POST' , "DELETE"] , strict_slashes=False)(delete_order)