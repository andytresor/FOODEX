from flask import Blueprint # type:ignore

from controllers.order_controller import index, add_order, newOrder, delete_order

order = Blueprint('order' , __name__)

order.route('/' , methods=['GET'] , strict_slashes=False)(index)
order.route('/add_order' , methods=['GET'] , strict_slashes=False)(add_order)
order.route('/create_order' , methods=['POST'] , strict_slashes=False)(newOrder)
order.route('/delete/<order_id>' , methods=['POST' , "DELETE"] , strict_slashes=False)(delete_order)