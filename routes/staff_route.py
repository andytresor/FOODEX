from flask import Blueprint # type:ignore

from controllers.staff_controller import index, add_staff, members,membersTwo, view_staff, newStaff, delete_staff, update_staff, logout
staff = Blueprint('staff' , __name__)

staff.route('/' , methods=['GET'] , strict_slashes=False)(index)
staff.route('/add_staff' , methods=['GET'] , strict_slashes=False)(add_staff)
staff.route('/members' , methods=['GET'] , strict_slashes=False)(members)
staff.route('/memberstwo' , methods=['GET'] , strict_slashes=False)(membersTwo)
# staff.route('/display' , methods=['GET'] , strict_slashes=False)(cook_index)
staff.route('/create_staff' , methods=['POST'] , strict_slashes=False)(newStaff)
staff.route('/view/<staff_id>' , methods=['GET'] , strict_slashes=False)(view_staff)
staff.route('/update/<staff_id>' , methods=['GET' , "POST"] , strict_slashes=False)(update_staff)
staff.route('/delete/<staff_id>' , methods=['POST' , "DELETE"] , strict_slashes=False)(delete_staff)
staff.route('/logout', methods=['POST', 'DELETE'], strict_slashes=False)(logout)
