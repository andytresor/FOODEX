from flask import Blueprint # type:ignore

from controllers.admin_controller import index,profile, view_admin, update_admin

admin = Blueprint('owner' , __name__)

admin.route('/' , methods=['GET'] , strict_slashes=False)(index)
admin.route('/profile' , methods=['POST'] , strict_slashes=False)(profile)
admin.route('/view/<order_id>' , methods=['GET'] , strict_slashes=False)(view_admin)
admin.route('/update/<order_id>' , methods=['GET' , "POST"] , strict_slashes=False)(update_admin)
# owner.route('/add_order' , methods=['GET'] , strict_slashes=False)(add_order)
# order.route('/create_order' , methods=['POST'] , strict_slashes=False)(newOrder)
# order.route('/delete/<order_id>' , methods=['POST' , "DELETE"] , strict_slashes=False)(delete_order)
